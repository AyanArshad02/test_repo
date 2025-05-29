# combine_rag.py
from app import query_rag_pdf
from sql import query_rag_sql
from langchain_community.chat_models import ChatOpenAI

query = "what do you think about tajmahal"

pdf_response = query_rag_pdf(query)
sql_response = query_rag_sql(query)

combined_prompt = f"""
You are a helpful assistant. Below are two responses retrieved from different sources for the same user query.

Response from PDF-based documentation:
{pdf_response}

Response from previously resolved SQL tickets:
{sql_response}

Please merge and rewrite these into a single, clear, concise, and helpful answer for the user.
"""

model = ChatOpenAI()
final_response = model.invoke(combined_prompt)

print("###########PDF RESPONSE###########")
print(pdf_response.content)

print("###########SQL RESPONSE###########")
print(sql_response)

print("###########FINAL RESPONSE###########")
print(final_response.content)