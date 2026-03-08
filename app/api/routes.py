from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.executive_coach import ExecutiveCoachAgent

router = APIRouter()

# request structure
class CoachRequest(BaseModel):
    message: str


# response structure
class CoachResponse(BaseModel):
    response: str


agent = ExecutiveCoachAgent()


@router.post("/coach", response_model=CoachResponse)
def coach_endpoint(request: CoachRequest):

    result = agent.run(request.message)

    return CoachResponse(response=result)