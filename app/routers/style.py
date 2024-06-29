from fastapi import APIRouter, Form, File, UploadFile
from models import Style
from app.modules import styleMongoDB

router = APIRouter(tags=["风格模板管理"])

router.post("/style")
async def createStyle(styleTitle = Form(...), styleContent = Form(...), styleImage = UploadFile(...)):
    
    if styleImage is not None:
        imageContent = await styleImage.read() 
    else:
        imageContent = None
        
    resultObj = styleMongoDB.createStyle(styleImage=imageContent, styleTitle=styleTitle, styleContent=styleContent)
    
    if resultObj.get('Mark'):
        return {"code": 200, "message": "success", "result": resultObj['result']}
    else:
        return {"code": 400, "message": "fail"}

router.put("/style")
async def modifyStyle(uid = Form(...), styleImage = UploadFile(None), styleTitle = Form(None), styleContent = Form(None)):
    resultObj = styleMongoDB.updateStyle(uid, styleImage=styleImage, styleTitle=styleTitle, styleContent=styleContent)
    
    if resultObj.get('Mark'):
        return {"code": 200, "message": "success", "result":resultObj["result"]}
    else:
        return {"code": 400, "message": "fail"}

router.get("/style")
async def getStyle():
    resultObj = styleMongoDB.getStyleAll()
    
    if resultObj.get('Mark'):
        return {"code": 200, "message": "success", "result":resultObj["result"]}
    else:
        return {"code": 400, "message": "fail"}
    
router.delete("style")
async def deleteStyle(uid = Form(...)):
    resultObj = styleMongoDB.deleteStyle(uid)
    
    if resultObj.get('Mark'):
        return {"code": 200, "message": "success", "result":resultObj["result"]}
    else:
        return {"code": 400, "message": "fail"}