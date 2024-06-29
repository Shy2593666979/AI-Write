from app.models import Style
from app.crud.base import mongoDB
from typing import Optional

class mongodb_operate:
    def __init__(self, mongoDB: Optional[mongoDB] = None):
        self.myMongoDB = mongoDB
    
    def getObjectById(self, uid):
        return self.myMongoDB.getObjectById('style', uid)
    
    def createStyle(self, styleImage, styleTitle, styleContent):
        return self.myMongoDB.createStyle(styleImage, styleTitle, styleContent)
    
    def updateStyle(self, styleImage = None, styleTitle = None, styleContent = None):
        return self.myMongoDB.modifyStyle(styleImage, styleTitle, styleContent)
    
    def getStyleAll(self):
        return self.myMongoDB.getStyleAll()
    
    def deleteStyle(self, uid):
        return self.myMongoDB.deleteStyleById('style', uid)