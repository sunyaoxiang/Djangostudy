# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view(request):
    if not request.user.is_authenticated():
        request_txt = "login failed"
    else:
        request_txt = "login succeed"
    context = {
        "request_txt": request_txt,
        "UserInfo": request.user.groups
    }

    return render(request, 'userm/my_view.html', context)


def checkwords(request):
    from io import BytesIO
    import random
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new(mode="RGB", size=(120, 40), color=(random.randint(0, 255), random.randint(0, 255),
                                                       random.randint(0, 255)))
    draw = ImageDraw.Draw(img, "RGB")
    font = ImageFont.truetype("userm/static/font/SIMLI.ttf", 30)
    vilid_list = []
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_lower_word = chr(random.randint(65, 90))
        random_upper_word = chr(random.randint(97, 122))
        random_char = random.choice([random_num, random_lower_word, random_upper_word])
        draw.text([5+i*24, 10], random_char, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                  font=font)
        vilid_list.append(random_char)
    for i in range(500):
        draw.point([random.randint(0, 133), random.randint(0, 40)], fill=(random.randint(0, 255), random.randint(0, 255)
                                                                          , random.randint(0, 255)))
    f = BytesIO()
    img.save(f, "png")
    # img.show()
    data = f.getvalue()
    vilid_str = "".join(vilid_list)
    request.session["ValidCode"] = vilid_str
    # context = {
    #     "data": (data,"image/jpg"),
    #     "img": img,
    #     "f": f,
    # }
    # return render(request, 'userm/yanzhengma.html', context)
    return HttpResponse(data, "image/jpg")

def viewcode(request):
    return render(request, 'userm/yanzhengma.html')