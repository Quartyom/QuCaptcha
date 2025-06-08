import base64
from io import BytesIO
import cv2


def encode_image(image):
    # buffer = BytesIO()
    # image.save(buffer, format='JPEG')
    # buffer.seek(0)
    # image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    # buffer.close()
    image_base64 = cv2.imencode('.jpeg', image)
    image_base64 = base64.b64encode(image_base64[1]).decode('utf-8')

    return f"data:image/jpeg;base64,{image_base64}"

