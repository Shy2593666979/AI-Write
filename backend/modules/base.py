from backend.models import Style
from backend.crud.base import mongoDB
from typing import Optional

class mongodb_operate:
    def __init__(self, mongoDB: Optional[mongoDB] = None):
        self.myMongoDB = mongoDB
    
    def getObjectById(self, className, uid):
        return self.myMongoDB.getObjectById(className, uid)
    
    def createStyle(self, logoPath, styleTitle, styleContent):
        return self.myMongoDB.createStyle(logoPath, styleTitle, styleContent)
    
    def updateStyle(self, uid, logoPath, styleTitle = None, styleContent = None):
        return self.myMongoDB.modifyStyle(uid, logoPath, styleTitle, styleContent)
    
    def getStyleAll(self):
        return self.myMongoDB.getStyleAll()
    
    def deleteStyle(self, uid):
        return self.myMongoDB.deleteObjectById('style', uid)
    
    def createTool(self, logoPath, toolTitle, toolDescription, toolPrompt):
        return self.myMongoDB.createTool(logoPath, toolTitle, toolDescription, toolPrompt)
    
    def updateTool(self, uid, logoPath = None, toolTitle = None, toolDescription = None, toolPrompt = None):
        return self.myMongoDB.modifyTool(uid, logoPath, toolTitle, toolDescription, toolPrompt)
    
    def deleteTool(self, uid):
        return self.myMongoDB.deleteObjectById('tool', uid)
    
    def getToolAll(self):
        return self.myMongoDB.getToolAll()