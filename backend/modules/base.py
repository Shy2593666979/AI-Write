from backend.models import Style
from backend.crud.base import mongoDB
from typing import Optional

class mongodb_operate:
    def __init__(self, mongoDB: Optional[mongoDB] = None):
        self.myMongoDB = mongoDB
    
    def getObjectById(self, className, uid):
        return self.myMongoDB.getObjectById(className, uid)
    
    def createStyle(self, styleImage, imageName, styleTitle, styleContent):
        return self.myMongoDB.createStyle(styleImage, imageName, styleTitle, styleContent)
    
    def updateStyle(self, uid, styleImage = None, imageName = None, styleTitle = None, styleContent = None):
        return self.myMongoDB.modifyStyle(uid, styleImage, imageName, styleTitle, styleContent)
    
    def getStyleAll(self):
        return self.myMongoDB.getStyleAll()
    
    def deleteStyle(self, uid):
        return self.myMongoDB.deleteObjectById('style', uid)
    
    def createTool(self, toolImage, toolTitle, toolDescription, toolPrompt):
        return self.myMongoDB.createTool(toolImage, toolTitle, toolDescription, toolPrompt)
    
    def updateTool(self, uid, toolImage = None, toolTitle = None, toolDescription = None, toolPrompt = None):
        return self.myMongoDB.modifyTool(uid, toolImage, toolTitle, toolDescription, toolPrompt)
    
    def deleteTool(self, uid):
        return self.myMongoDB.deleteObjectById('tool', uid)
    
    def getToolAll(self):
        return self.myMongoDB.getToolAll()