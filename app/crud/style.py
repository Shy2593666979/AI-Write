from app.models import templateStyle
from fastapi import APIRouter
from app.schemas import modelStyle, updateStyle
from bson import ObjectId
from datetime import datetime

router = APIRouter(prefix="api/write/style")

@router.post("/create", summary="创建一个风格模板")
def create_style(model_style: modelStyle):
    template_style = templateStyle(title=model_style.title, content=model_style.content)
    template_style.save()
    
    return {"status":200, "message":"Created Successful !"}

@router.delete("/delete/{_id}", summary="删除风格模板")
def delete_style(_id: str):
    delete_obj = templateStyle.objects.with_id(ObjectId(_id))
    
    if delete_obj:
        delete_obj.delete()
        return {"status":200, "message":"Delete Successfule !"}
    else:
        return {"status":400, "message":"No ID found"}
    
@router.put("/update/{_id}", summary="更新风格模板")
def update_style(_id :str, model_style:updateStyle):
    update_obj = templateStyle.objects.with_id(ObjectId(_id))
    
    if update_obj:
        if model_style.title:
            update_obj.title = modelStyle.title
        
        if model_style.content:
            update_obj.content = modelStyle.content
        
        update_obj.createTime = datetime.utcnow

        return {"status":200, "message":"Update Successful !"}
    else:
        return {"status":400, "message":"No ID found"}
        