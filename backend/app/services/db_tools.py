from sqlalchemy import inspect, text
from app.database.session import engine, SessionLocal

def get_database_schema() -> str:
    """
    Uses SQLAlchemy inspect to automatically pull table names, columns, and types.
    Returns a formatted string describing the schema, to be used as context for the AI.
    """
    inspector = inspect(engine)
    schema_info = []
    
    for table_name in inspector.get_table_names():
        schema_info.append(f"Table: {table_name}")
        for column in inspector.get_columns(table_name):
            col_name = column['name']
            col_type = str(column['type'])
            schema_info.append(f"  - {col_name} ({col_type})")
        
        for fk in inspector.get_foreign_keys(table_name):
            constrained_columns = ", ".join(fk['constrained_columns'])
            referred_table = fk['referred_table']
            referred_columns = ", ".join(fk['referred_columns'])
            schema_info.append(f"  - FOREIGN KEY ({constrained_columns}) REFERENCES {referred_table}({referred_columns})")
    
    return "\n".join(schema_info)

def run_read_only_query(query: str) -> list[dict]:
    """
    Executes a raw SQL SELECT query safely.
    Rejects any query that is not a SELECT statement.
    """
    import re
    # Extract text from the first ```sql block it finds
    sql_match = re.search(r"```sql\s+(.*?)\s+```", query, re.DOTALL | re.IGNORECASE)
    if sql_match:
        extracted_sql = sql_match.group(1).strip()
    else:
        # Fallback if no ```sql is found
        select_match = re.search(r"(SELECT\s+.*)", query, re.DOTALL | re.IGNORECASE)
        if select_match:
            extracted_sql = select_match.group(1).strip()
        else:
            extracted_sql = query.strip()
            
    # Clean up SQL comments from the extracted code for the security check
    clean_sql = re.sub(r"--.*?(\n|$)", "", extracted_sql).strip()
    
    # Targeted Security Check: ONLY apply to the extracted code
    if not clean_sql.upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed for security reasons.")
    
    query = extracted_sql
    
    db = SessionLocal()
    try:
        # Execute the query
        result = db.execute(text(query))
        
        # Convert results to a list of dicts for JSON serialization
        columns = result.keys()
        rows = [dict(zip(columns, row)) for row in result.fetchall()]
        return rows
    finally:
        db.close()
