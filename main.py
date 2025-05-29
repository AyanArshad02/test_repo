from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app import query_rag_pdf as query_pdf
from sql_rag import query_rag_sql as query_sql
from langchain_community.chat_models import ChatOpenAI

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryInput(BaseModel):
    query: str

@app.post("/query")
async def get_responses(data: QueryInput):
    query = data.query

    pdf_resp = query_pdf(query)
    sql_resp = query_sql(query)

    combined_prompt = f"""
    You are a helpful assistant. Two sources provided the following information:

    PDF-based answer:
    {pdf_resp}

    SQL ticket-based answer:
    {sql_resp}

    Please combine and rewrite both into one helpful answer.
    """
    final_resp = ChatOpenAI().invoke(combined_prompt).content

    return {
        "pdf_response": pdf_resp,
        "sql_response": sql_resp,
        "final_response": final_resp
    }