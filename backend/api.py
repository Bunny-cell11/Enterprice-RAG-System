
from fastapi import FastAPI
from backend.auth import get_user_role
from backend.security import detect_prompt_injection
from backend.retriever import retrieve
from backend.audit_logger import log_event

app = FastAPI()

@app.get("/query")
def query_system(username: str, query: str):

    role = get_user_role(username)

    if not role:
        return {"error": "Unauthorized"}

    if detect_prompt_injection(query):
        log_event(username, role, query, "BLOCKED")
        return {"error": "Prompt injection detected"}

    results = retrieve(query, role)

    log_event(username, role, query, "SUCCESS")

    return {
        "user": username,
        "role": role,
        "results": results
    }
