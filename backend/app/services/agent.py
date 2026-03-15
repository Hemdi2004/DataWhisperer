import os
from groq import Groq
from app.services.db_tools import get_database_schema, run_read_only_query

# The client will automatically use the GROQ_API_KEY environment variable.
client = Groq()

def ask_agent(question: str) -> str:
    """
    Synchronous agent logic that uses Groq, Llama 3.3 70B, and db_tools
    to generate and execute dynamic SQL based on schema discovery.
    """
    schema = get_database_schema()
    
    # First step: Ask the agent to generate the SQL query
    system_prompt = f"""
You are an expert SQL assistant. Your goal is to answer the user's question by writing a SQL query.
You have access to the following database schema:

{schema}

Always return ONLY the valid SQL query, with no markdown formatting (like ```sql), no explanations, and no preamble.
The query MUST be a SELECT statement. It MUST be valid SQL for the above schema.
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0,
        max_completion_tokens=500,
    )
    
    sql_query = response.choices[0].message.content.strip()
    
    # Just in case the model ignored instructions and included markdown
    if sql_query.startswith("```sql"):
        sql_query = sql_query[6:]
    if sql_query.endswith("```"):
        sql_query = sql_query[:-3]
    sql_query = sql_query.strip()
    
    try:
        results = run_read_only_query(sql_query)
    except Exception as e:
        return f"Error executing query: {str(e)}\nGenerated Query: {sql_query}"
        
    # Second step: Synthesize the final answer
    synthesis_prompt = f"""
You are an expert data analyst. The user asked a question, and we ran a SQL query to get the answer.

User Question: {question}
SQL Query Executed: {sql_query}
Query Results: {results}

Please synthesize the query results into a clear, natural language answer to the user's question.
"""

    synthesis_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": synthesis_prompt}
        ],
        temperature=0.3,
        max_completion_tokens=1000,
    )
    
    return synthesis_response.choices[0].message.content
