from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.agent_graph import build_graph

router = APIRouter()

graph = build_graph()


class CoachRequest(BaseModel):
    message: str


class CoachResponse(BaseModel):
    response: str


@router.post("/coach", response_model=CoachResponse)
def coach_endpoint(request: CoachRequest):

    result = graph.invoke({
        "user_input": request.message
    })

    return CoachResponse(response=result["response"])