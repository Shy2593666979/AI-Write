from fastapi import APIRouter, Form, UploadFile, File
from fastapi.encoders import jsonable_encoder
from backend.modules import baseMongoDB
from backend.settings import setting

router = APIRouter()

@router.post("/tool")
async def createTool(toolImage: UploadFile=File(...), toolTitle: str=Form(...), toolDescription: str=Form(...), toolPrompt: str=Form(...)):
    if toolImage is None:
        imageName = setting.tool_default_logo.split('/')[-1]
        with open(setting.tool_default_logo, 'rb') as image:
            imageContent = image.read()
    else:
        imageContent = await toolImage.read()
        imageName = toolImage.filename
        
    resultObj = baseMongoDB.createTool(imageContent, imageName, toolTitle, toolDescription, toolPrompt)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "create fail!"})

@router.get("/tool")
async def getToolAll():
    resultObj = baseMongoDB.getToolAll()
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj["result"]})                               
    else:
        return jsonable_encoder({"code": 400, "message": "get fail!"})

@router.put("/tool")
async def updateTool(uid: str=Form(...), toolImage: UploadFile=File(None), toolTitle: str=Form(None), toolDescription: str=Form(None), toolPrompt: str=Form(None)):
    if toolImage is not None:
       imageContent = await toolImage.read()
       imageName = toolImage.filename
    else:
       imageContent = None
       imageName = None
   
    resultObj = baseMongoDB.updateTool(uid, imageContent, imageName, toolTitle, toolDescription, toolPrompt)
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "update fail!"})
    
@router.delete("/tool")
async def deleteTool(uid: str=Form(...)):
    resultObj = baseMongoDB.deleteTool(uid)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "delete fail!"})