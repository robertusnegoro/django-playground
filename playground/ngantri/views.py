from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import PersonForm
from .models import Person
import logging
import io
import base64
import uuid
import re
import pyqrcode

logger = logging.getLogger(__name__)
# Create your views here.
def upload(request):
    if request.method == "POST":
        logger.info(request.POST)
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info("Form is valid")
            # form.save()
            first_name = request.POST['first_name']
            last_name = request.POST['first_name']
            image_base64 = request.POST['image']
            dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
            ImageData = dataUrlPattern.match(image_base64).group(2)

            bin_file = io.BytesIO(base64.b64decode(ImageData))

            person = Person()
            person.last_name = last_name
            person.first_name = first_name
            filename = "%s.png" % (str(uuid.uuid4()))
            person.image.save(filename, bin_file)
            person.save()
        else:
            logger.info(form.errors)
        return redirect("ngantri:upload")
    form = PersonForm()
    persons = Person.objects.all()
    logger.info("Persons data loaded")
    return render(
        request=request,
        template_name="form.html",
        context={"form": form, "persons": persons},
    )


def test(request):
    return render(request=request, template_name="test.html")

def theqr(request, idperson=0):
    if idperson > 0:
        url = 'https://www.example.com'
        qr = pyqrcode(url)
        qr.png('qr_code.png', scale=8)
        return render(request=request, template_name="qr.html")
    else:
        return HttpResponse('bambang 404 tapi tidak 404, bingungkan')
