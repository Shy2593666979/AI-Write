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
    
    def createStyle(self, styleImage, imageName, styleTitle, styleContent):
        style_obj = Style(styleImage=styleImage, styleTitle=styleTitle, styleContent=styleContent)
        
        try:
            resultObj = style_obj.save()
            imageObj = self.updateStyleLogoUrl(str(resultObj.id), imageName)
            
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

    def modifyStyle(self, uid, styleImage = None, imageName = None, styleTitle = None, styleContent = None, imagePath = None):
        #breakpoint()
        styleObj = Style.objects.with_id(uid)
        try:
            if imageName is not None:
                imageObj = self.updateStyleLogoUrl(uid=uid, imageName=imageName)
            if styleImage is not None:
                styleObj.update(styleImage=styleImage)
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
                    "styleImagePath": resultObj.styleImagePath,
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
    
    def updateStyleLogoUrl(self, uid, imageName):
        try:
            obj = self.getObjectById('style', uid)
            if obj.get('Mark'):
                result_dict = json.loads(obj.get('result'))
            
            imagePath = createImage(uid=uid, imageName=imageName, styleImage=result_dict['styleImage'])
            resultObj = self.modifyStyle(uid=uid, imagePath=imagePath)
            if resultObj.get('Mark'):
                return {
                    "Mark": True,
                    "result": "success update ImageUrl"
                }
        except Exception as err:
            deleteObj = self.deleteObjectById('style', uid)
            logger.error(err)
            return {
                "Mark":False,
                "result": "update err"
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
                deleteImage(resultObj.styleImagePath)
            if className == 'tool':
                resultObj = Tool.objects.with_id(uid)
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
    def createTool(self, toolImage, toolTitle, toolDescription, toolPrompt):
        try:
            toolObj = Tool(toolImage=toolImage, toolTitle=toolTitle, toolDescription=toolDescription, toolPrompt=toolPrompt)
            
            resultObj = toolObj.save()
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
                "result": "create fail!"
            }
    
    def modifyTool(self, uid: str, toolImage = None, toolTitle = None, toolDescription = None, toolPrompt = None):
        try:
            toolObj = Tool.objects.with_id(uid)
            
            if toolImage is not None:
                toolObj.update(toolImage=toolImage)
            if toolTitle is not None:
                toolObj.update(toolTitle=toolTitle)
            if toolDescription is not None:
                toolObj.update(toolDescription=toolDescription)
            if toolPrompt is not None:
                toolObj.update(toolPrompt=toolPrompt)
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
                   
            