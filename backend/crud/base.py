from datetime import datetime
from fastapi import APIRouter
from mongoengine import connect
from models import Style
from loguru import logger
from settings import setting

class mongoDB:
    def __init__(self):
        connect(db=setting.db, host=setting.host)
    
    def createStyle(self, styleImage, styleTitle, styleContent):
        style_obj = Style(styleImage=styleImage, styleTitle=styleTitle, styleContent=styleContent)
        
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
                result.append({"uid": style.id,"styleImage": style.styleImage, "styleTitle": style.styleTitle, "styleContent": style.styleContent, "updateTime": style.updateTime})
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
            
    def deleteStyleById(self, className, uid):
        try:
            if className == 'style':
                resultObj = Style.objects.with_id(uid)
            
            resultObj.delete()
            return {
                "Mark": True,
                "result": "success delete"
            }
        except Exception as err:
            logger.error(err)
            return {
                "Mark": False,
                "result": "fail"
            }