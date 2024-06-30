from fastapi import APIRouter, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from crud.base import mongoDB
from modules.base import mongodb_operate
from models import Style
from modules import baseMongoDB
from utils.chatAI import chat_deepseek
from loguru import logger

router = APIRouter(tags=["风格模板管理"])


@router.post("/style")
async def createStyle(styleTitle: str = Form(...), styleContent: str = Form(...), styleImage: UploadFile = File(...)):
    
    if styleImage is not None:
        imageContent = await styleImage.read() 
    else:
        imageContent = None
        
    resultObj = baseMongoDB.createStyle(styleImage=imageContent, styleTitle=styleTitle, styleContent=styleContent)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj['result']})
    else:
        return jsonable_encoder({"code": 400, "message": "fail"})

@router.put("/style")
async def modifyStyle(uid: str = Form(...), styleImage: UploadFile = File(None), styleTitle: str = Form(None), styleContent: str = Form(None)):
    resultObj = baseMongoDB.updateStyle(uid, styleImage=styleImage, styleTitle=styleTitle, styleContent=styleContent)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result":resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "fail"})

@router.get("/style")
async def getStyle():
    resultObj = baseMongoDB.getStyleAll()
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result":resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "fail"})
    
@router.delete("/style")
async def deleteStyle(uid: str = Form(...)):
    resultObj = baseMongoDB.deleteStyle(uid)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result":resultObj["result"]})
    else:
        return jsonable_encoder({"code": 400, "message": "fail"})
    
@router.post("/style/run")
async def runStyle(styleId: str = Form(...), originalContent: str = Form(...), toolId: str = Form(...)):
    styleObj = baseMongoDB.getObjectById(className='style', uid=styleId)
    toolObj = baseMongoDB.getObjectById(className='tool', uid=toolId)
    
    if styleObj is None or toolObj is None:
        return jsonable_encoder({"code": 400, "message": "run fail"})
    else:
        try:
            prompt = toolObj.toolPrompt.format(originalContent, styleObj.styleContent)
            
            response = chat_deepseek(prompt)
            return jsonable_encoder({"code": 200, "message": "success", "result": response})
        except Exception as err:
            logger.error(err)
            return jsonable_encoder({"code": 400, "message": "run fail"})