from django.utils.six import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
import qrcode



# Create your views here.
# 生成二维码
def createQrcode(request):
    content = request.POST.get("content")
    qr_img = qrcode.make(content)

    buf = BytesIO()
    qr_img.save(buf)
    qr_image_stream = buf.getvalue()

    response = HttpResponse(qr_image_stream,content_type="image/png")
    return response

# tools 首页
def index(request):
    return render(request,"tools/index.html")


