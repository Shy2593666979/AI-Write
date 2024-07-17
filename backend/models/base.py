from mongoengine import Document, StringField, DateTimeField, BinaryField
from datetime import datetime
from backend.settings import setting

class Style(Document):
    styleTitle = StringField(required=True)
    styleContent = StringField(required=True)
    logoPath = StringField(default=setting.style_default_logo)
    updateTime = DateTimeField(default=datetime.utcnow)

class Tool(Document):
    toolTitle = StringField(required=True)
    toolDescription = StringField(required=True)
    toolPrompt = StringField(required=True)
    logoPath = StringField(default=setting.tool_default_logo)
    updateTime = DateTimeField(default=datetime.utcnow)
