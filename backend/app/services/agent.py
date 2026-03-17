import os
from groq import Groq
from app.services.db_tools import get_database_schema, run_read_only_query

# The client will automatically use the GROQ_API_KEY environment variable.
client = Groq()

def run_agent(question: str) -> str:
    """
    Synchronous agent logic that uses Groq, Llama 3.3 70B, and db_tools
    to generate and execute dynamic SQL based on schema discovery.
    """
    schema = get_database_schema()
    
    # First step: Ask the agent to generate the SQL query
    system_prompt = f"""You are a data assistant. Here is the LIVE schema of the database you are connected to:
{schema}

When a user asks a question, first output the SQL block, then provide the natural language answer. Always use triple backticks for SQL. 
For string searches like city names, always use LOWER() and LIKE %keyword% to ensure fuzzy matching (e.g., LOWER(city) LIKE '%rio%').
Generate the correct SQL based ONLY on this structure."""
    
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
