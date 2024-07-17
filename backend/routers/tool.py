import uuid
from fastapi import APIRouter, Form, UploadFile, File
from fastapi.encoders import jsonable_encoder
from backend.modules import baseMongoDB
from backend.settings import setting

router = APIRouter()

@router.post("/tool")
async def createTool(toolImage: UploadFile=File(None), toolTitle: str=Form(...), toolDescription: str=Form(...), toolPrompt: str=Form(...)):
    uid = uuid.uuid4()
    
    if toolImage is None:
        logoPath = f"upimg/{uid}.jpg"
        tooImage = open(setting.tool_default_logo_binary, 'rb')
        with open(logoPath, 'wb') as file:
            file.write(toolImage.read())        
    else:
        logoPath = f"upimg/{uid}.{toolImage.content_type.split('/')[-1]}"
        with open(logoPath, 'wb') as file:
            file.write(await toolImage.read())
        
    resultObj = baseMongoDB.createTool(logoPath, toolTitle, toolDescription, toolPrompt)
    
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
       uid = uuid.uuid4()
       logoPath = f"upimg/{uid}.{toolImage.content_type.split('/')[-1]}"
       with open(logoPath, 'wb') as file:
           file.write(await toolImage.read())
    else:
       logoPath = None
   
    resultObj = baseMongoDB.updateTool(uid, logoPath, toolTitle, toolDescription, toolPrompt)
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