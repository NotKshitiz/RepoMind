from fastapi import FastAPI
from ingestion.pipeline import ingest
from pydantic import BaseModel
from ingestion.chat import ask_repo as ask
app = FastAPI()

class IngestRequest(BaseModel):
    github_url: str
    
class QueryRequest(BaseModel):
    repo_name: str
    question: str
    

@app.post("/ingest")
async def ingest_repo(req: IngestRequest):
    result = ingest(req.github_url)
    return { "result": result }

@app.post("/chat")
async def chat(req: QueryRequest):
    answer = ask(req.repo_name, req.question)
    return {"answer": answer}
    