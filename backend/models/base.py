from mongoengine import Document, StringField, DateTimeField, BinaryField
from datetime import datetime
from backend.settings import setting

class Style(Document):
    styleImage = BinaryField(required=True)
    styleTitle = StringField(required=True)
    styleContent = StringField(required=True)
    styleImagePath = StringField(default=setting.style_default_logo)
    updateTime = DateTimeField(default=datetime.utcnow)

class Tool(Document):
    toolImage = BinaryField(required=True)
    toolTitle = StringField(required=True)
    toolDecription = StringField(required=True)
    toolPrompt = StringField(required=True)
    toolImagePath = StringField(default=setting.tool_default_logo)
    updateTime = DateTimeField(default=datetime.utcnow)
