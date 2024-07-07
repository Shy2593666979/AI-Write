import os, io, base64
from backend.settings import setting
from PIL import Image

def createImage(uid, imageContent, imageName):
    imageContent = imageContent.get('$binary')
    
    imageType = imageName.split('.')[-1]
    
    image_data = base64.b64decode(imageContent)
    # 使用BytesIO创建一个可读的二进制流
    image_stream = io.BytesIO(image_data)

    # 使用Pillow打开这个二进制流中的图片
    image = Image.open(image_stream)

    imagePath = fr"upimg/{uid}.{imageType}"
    # 保存图片到文件系统，指定格式（如果知道的话），例如JPEG
    image.save(imagePath, "JPEG" if imageType == "jpg" else imageType.upper())
    
    return setting.host + ":" + setting.port + "/" + imagePath


def deleteImage(imagePath):
    imagePath = "upimg/" + imagePath.split('/')[-1]
    print(imagePath)
    if os.path.exists(imagePath):
        os.remove(imagePath)
    else:
        raise ValueError(f"can not find {imagePath}!")