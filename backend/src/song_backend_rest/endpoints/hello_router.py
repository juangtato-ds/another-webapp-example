from typing import Final

from fastapi import APIRouter, status


ROUTER_TAG: Final[str] = "Dummy"
ROUTER_PREFIX: Final[str] = "/dummy"

router = APIRouter(
    prefix=ROUTER_PREFIX,
    tags=[ROUTER_TAG],
    # route_class= missing # exception handler
)


@router.get(
    "/hello",
    tags=[ROUTER_TAG],
    status_code=status.HTTP_200_OK,
    response_model=dict[str, str],
)
async def hello() -> dict[str, str]:
    return {"hello": "world"}
