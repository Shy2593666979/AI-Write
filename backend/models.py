from mongoengine import Document, StringField, DateTimeField, BinaryField
from datetime import datetime

class Style(Document):
    styleImage = BinaryField(required=True)
    styleTitle = StringField(required=True)
    styleContent = StringField(required=True)
    updateTime = DateTimeField(default=datetime.utcnow)

