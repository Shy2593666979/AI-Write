from fastapi import APIRouter, Form, UploadFile, File
from fastapi.encoders import jsonable_encoder
from modules import baseMongoDB

router = APIRouter()

@router.post("/tool")
async def createTool(toolImage: UploadFile=File(...), toolTitle: str=Form(...), toolDescription: str=Form(...), toolPrompt: str=Form(...)):
    if toolImage is None:
        imageContent = None
    else:
        imageContent = await toolImage.read()
        
    resultObj = baseMongoDB.createTool(imageContent, toolTitle, toolDescription, toolPrompt)
    
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
async def updateTool(uid: str=Form(...), toolImage: UploadFile=File(None), toolTitle: str=Form(None), toolDescription: str=Form(None), toolPrompt: str=Form(...)):
    if toolImage is not None:
       imageContent = await toolImage.read()
    else:
       imageContent = None
   
    resultObj = baseMongoDB.updateTool(uid, imageContent, toolTitle, toolDescription, toolPrompt)
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