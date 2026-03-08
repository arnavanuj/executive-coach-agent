from fastapi import APIRouter
from pydantic import BaseModel
from app.orchestrator.agent_graph import build_graph
from fastapi.responses import StreamingResponse

router = APIRouter()

graph = build_graph()


class CoachRequest(BaseModel):
    message: str
    session_id: str


class CoachResponse(BaseModel):
    response: str


@router.post("/coach", response_model=CoachResponse)
def coach_endpoint(request: CoachRequest):

    result = graph.invoke({
        "user_input": request.message,
        "session_id": request.session_id
    })

    return CoachResponse(response=result["response"])


@router.post("/coach_stream")
async def coach_stream(request: CoachRequest):

    def generate():

        for token in graph.invoke({
            "user_input": request.message,
            "session_id": request.session_id
        })["response"]:
            yield token

    return StreamingResponse(generate(), media_type="text/event-stream")