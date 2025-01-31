import json
from fastapi import APIRouter, Form, File, UploadFile
from fastapi.encoders import jsonable_encoder
from backend.crud.base import mongoDB
from backend.modules.base import mongodb_operate
from backend.models.base import Style
from backend.modules import baseMongoDB
from backend.utils.chatAI import chat_deepseek
from backend.settings import setting
from loguru import logger
import uuid

router = APIRouter(tags=["风格模板管理"])

@router.post("/style")
async def createStyle(styleTitle: str = Form(...), styleContent: str = Form(...), styleImage: UploadFile = File(None)):
    uid = uuid.uuid4()
    if styleImage is not None:
        logoPath = f"upimg/{uid}.{styleImage.content_type.split('/')[-1]}"
        with open(logoPath, 'wb') as file:
            file.write(await styleImage.read())
    else:
        styleImage = open(setting.style_default_logo_binary, "rb") 
        logoPath = f"upimg/{uid}.jpg"
        with open(logoPath, 'wb') as file:
            file.write(styleImage.read())
        
    resultObj = baseMongoDB.createStyle(logoPath=logoPath, styleTitle=styleTitle, styleContent=styleContent)
    
    if resultObj.get('Mark'):
        return jsonable_encoder({"code": 200, "message": "success", "result": resultObj['result']})
    else:
        return jsonable_encoder({"code": 400, "message": "fail"})

@router.put("/style")
async def modifyStyle(uid: str = Form(...), styleImage: UploadFile = File(None), styleTitle: str = Form(None), styleContent: str = Form(None)):
    if styleImage is not None:
       uid = uuid.uuid4()
       logoPath = f"upimg/{uid}.{styleImage.content_type.split('/')[-1]}"
       with open(logoPath, 'wb') as file:
           file.write(await styleImage.read())
    else:
       logoPath = None
       
    resultObj = baseMongoDB.updateStyle(uid, logoPath, styleTitle=styleTitle, styleContent=styleContent)
    
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
            styleResult = json.loads(styleObj.get('result'))
            toolResult = json.loads(toolObj.get('result'))
            
            prompt = toolResult['toolPrompt'].format(originalContent, styleResult['styleContent'])
            response = chat_deepseek(prompt)
            return jsonable_encoder({"code": 200, "message": "success", "result": response})
        except Exception as err:
            logger.error(err)
            return jsonable_encoder({"code": 400, "message": "run fail"})