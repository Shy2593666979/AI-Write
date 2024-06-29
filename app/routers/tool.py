from fastapi import APIRouter

router = APIRouter(prefix="/api/write")

@router.get("/tool", summary="获得所有工具的信息")
def get_tool():
    pass