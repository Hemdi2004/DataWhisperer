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
    
    return "\n".join(schema_info)

def run_read_only_query(query: str) -> list[dict]:
    """
    Executes a raw SQL SELECT query safely.
    Rejects any query that is not a SELECT statement.
    """
    # Basic safety check
    if not query.strip().upper().startswith("SELECT"):
        raise ValueError("Only SELECT queries are allowed for security reasons.")
    
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
