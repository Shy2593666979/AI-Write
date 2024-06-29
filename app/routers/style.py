from fastapi import APIRouter
from models import templateStyle

router = APIRouter(prefix="/api/write/style")


@router.get("/template", summary="获得所有的风格模板")
def get_style_template():
    """
        GET请求获取所有的风格模板
    """
    data = []
    for style in templateStyle.objects():
        data.append({"title": style.title, "content": style.content,
                    "createTime": style.createTime})

    return {"status": 200, "data": data}
