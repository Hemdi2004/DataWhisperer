from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.models.database_models import User
from app.api.deps import get_current_active_user
from app.services.agent import run_agent

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
def chat_with_agent(
    payload: QuestionRequest, 
    current_user: User = Depends(get_current_active_user)
):
    """
    Synchronous endpoint for asking questions.
    Requires an active user JWT token via the Authorization header.
    """
    try:
        # Pass the question to the synchronous agent logic
        answer = run_agent(payload.question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
