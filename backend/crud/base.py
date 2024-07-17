import base64
from datetime import datetime
import json
from backend.utils.image import createImage, deleteImage
from mongoengine import connect
from backend.models import Style, Tool
from loguru import logger
from backend.settings import setting

class mongoDB:
    def __init__(self):
        connect(db=setting.mongodb_db, host=setting.mongodb_host)
    
    def createStyle(self, logoPath, styleTitle, styleContent):
        style_obj = Style(logoPath=logoPath, styleTitle=styleTitle, styleContent=styleContent)
        
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
            deleteObj = self.deleteObjectById('style', str(resultObj.id))
            logger.error(err)
            return {
                "Mark": False,
                "result": "create style fail"
            }

    def modifyStyle(self, uid, logoPath = None, styleTitle = None, styleContent = None, imagePath = None):
        #breakpoint()
        styleObj = Style.objects.with_id(uid)
        try:
            if logoPath is not None:
                styleObj.update(logoPath=logoPath)
            if styleTitle is not None:
                styleObj.update(styleTitle=styleTitle)
            if styleContent is not None:
                styleObj.update(styleContent=styleContent)
            if imagePath is not None:
                styleObj.update(styleImagePath=imagePath)    
                
            styleObj.update(updateTime=datetime.utcnow)
            
            styleObj.save()
            resultObj = Style.objects.with_id(uid)
            return {
                "Mark": True,
                "result": {
                    "uid": str(resultObj.id),
                    "styleTitle": resultObj.styleTitle,
                    "styleContent": resultObj.styleContent,
                    "logoPath": resultObj.logoPath,
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
                result.append({"uid": str(style.id), "styleImage": base64.b64encode(style.styleImage).decode('utf-8'), "styleTitle": style.styleTitle, "styleContent": style.styleContent, "styleImagePath": style.styleImagePath,"updateTime": style.updateTime})
            
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
            if className == 'tool':
                resultObj = Tool.objects.with_id(uid)
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
            
    def deleteObjectById(self, className, uid):
        #breakpoint()
        try:
            if className == 'style':
                resultObj = Style.objects.with_id(uid)
                deleteImage(resultObj.logoPath)
            if className == 'tool':
                resultObj = Tool.objects.with_id(uid)
                deleteImage(resultObj.logoPath)
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
    def createTool(self, logoPath, toolTitle, toolDescription, toolPrompt):
        try:
            toolObj = Tool(logoPath=logoPath, toolTitle=toolTitle, toolDescription=toolDescription, toolPrompt=toolPrompt)
            resultObj = toolObj.save()
            return {
                "Mark": True,
                "result": {
                    "uid": str(resultObj.id),
                    "toolTitle": resultObj.toolTitle,
                    "toolDescription": resultObj.toolDescription,
                    "ImagePath": resultObj.logoPath,
                    "toolPrompt": resultObj.toolPrompt
                }
            }
        except Exception as err :
            deleteObj = self.deleteObjectById('tool', str(resultObj.id))
            logger.error(err)
            
            return {
                "Mark": False,
                "result": "create fail!"
            }
    
    def modifyTool(self, uid: str, logoPath = None, imagePath = None, toolTitle = None, toolDescription = None, toolPrompt = None):
        #breakpoint()
        try:
            toolObj = Tool.objects.with_id(uid)
            
            if logoPath is not None:
                toolObj.update(logoPath=logoPath)
            if toolTitle is not None:
                toolObj.update(toolTitle=toolTitle)
            if toolDescription is not None:
                toolObj.update(toolDescription=toolDescription)
            if toolPrompt is not None:
                toolObj.update(toolPrompt=toolPrompt)
            if imagePath is not None:
                toolObj.update(toolImagePath=imagePath)    
            toolObj.update(updateTime=datetime.utcnow)
            toolObj.save()
            
            resultObj = Tool.objects.with_id(uid)
            return {
                "Mark": True,
                "result": {
                    "uid": str(resultObj.id),
                    "toolTitle": resultObj.toolTitle,
                    "toolDescription": resultObj.toolDescription,
                    "toolPrompt": resultObj.toolPrompt
                }
            }
        except Exception as err :
            logger.error(err)
            return {
                "Mark": False,
                "result": "update fail!"
            }
    def getToolAll(self):
        try:
            toolObj = Tool.objects.all()
            result = []
            for tool in toolObj:
                result.append({"uid": str(tool.id), "toolImage": tool.toolImage, "toolTitle": tool.toolTitle, "toolDescription": tool.toolDescription, "toolPrompt": tool.toolPrompt, "updateTime": tool.updateTime})
            
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
            