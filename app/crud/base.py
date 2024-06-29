from datetime import datetime
from fastapi import APIRouter
from mongoengine import connect
from app.models import Style
from loguru import logger

class mongoDB:
    def __init__(self):
        pass
    
    def createStyle(self, styleImage, styleTitle, styleContent):
        style_obj = Style(styleImage, styleTitle, styleContent)
        
        try:
            resultObj = style_obj.save()
            return {
                "Mark": True,
                "result": {
                    "uid": str(resultObj.id),
                    "styleTitle": resultObj.styleTitle,
                    "styleContent": resultObj.styleContent,
                    "updateTime": resultObj.updateTime
                }
            }
        except Exception as err:
            logger.error(err)
            return {
                "Mark": False,
                "result": "create style fail"
            }

    def modifyStyle(self, uid, styleImage = None, styleTitle = None, styleContent = None):
        styleObj = Style.objects.with_id(uid)
        
        try:
            if styleImage is not None:
                styleObj.update(styleImage=styleImage)
            if styleTitle is not None:
                styleObj.update(styleTitle=styleTitle)
            if styleContent is not None:
                styleObj.update(styleContent=styleContent)
            styleObj.update(updateTime=datetime.utcnow)
            
            styleObj.save()
            resultObj = Style.objects.with_id(uid)
            return {
                "Mark": True,
                "result": {
                    "uid": str(resultObj.id),
                    "styleTitle": resultObj.styleTitle,
                    "styleContent": resultObj.styleContent,
                    "updateTime": resultObj.updateTime
                }
            }
            
        except Exception as err:
            logger.error(err)
            return {
                "Mark": False,
                "result": "create style fail"
            }
    def getStyleAll(self):
        try:
            styleObj = Style.objects.all()
            result = []
            for style in styleObj:
                result.append({"uid": style.id,"styleImage": style.styleImage, "styleTitle": style.styleTitle, "styleContent": style.styleContet, "updateTime": style.updateTime})
            return {
                "Mark": True,
                "result": result
            }
        except Exception as err :
            logger.error(err)
            
            return {
                "Mark": False,
                "result": "can not find target"
            }
    def getObjectById(self, className, uid):
        try:
            if className == 'style':
                resultObj = Style.objects.with_id(uid)
            
            return {
                "Mark": True,
                "result": resultObj.to_json()
            }
        except Exception as err:
            logger.error(err)
            return {
                "Mark": False,
                "result": "fail"
            }