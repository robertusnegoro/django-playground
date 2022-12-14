from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .form import PersonForm
from .models import Person
import logging
import io
import base64
import uuid
import re
from django.conf import settings

logger = logging.getLogger(__name__)
# Create your views here.


def index(request):
    return HttpResponse("hey, this is index")


def upload(request):
    form = PersonForm()
    persons = Person.objects.all()
    logger.info("Persons data loaded")
    return render(
        request=request,
        template_name="form.html",
        context={"form": form, "persons": persons},
    )


def uploadSave(request):
    if request.method == "POST":
        logger.info(request.POST)
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            logger.info("Form is valid")
            # form.save()
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            image_base64 = request.POST["image"]
            dataUrlPattern = re.compile("data:image/(png|jpeg);base64,(.*)$")
            ImageData = dataUrlPattern.match(image_base64).group(2)

            bin_file = io.BytesIO(base64.b64decode(ImageData))

            person = Person()
            person.last_name = last_name
            person.first_name = first_name
            filename = "%s.png" % (str(uuid.uuid4()))
            person.image.save(filename, bin_file)
            person.save()
            return JsonResponse({"id": person.id, "status": "OK"})
        else:
            logger.info(form.errors)
            return JsonResponse({"status": "failed"})
    else:
        return Http404()


def test(request):
    return render(request=request, template_name="test.html")


def theqr(request, idperson=0):
    if idperson > 0:
        person = Person.objects.get(pk=idperson)
        qrtxt = "%s ; Person: %s %s ; Queue No: %s" % (person.comingdate, person.first_name, person.last_name, person.id)
        context = {"person": person, "qrtxt": qrtxt}
        return render(request=request, template_name="qr.html", context=context)
    else:
        return HttpResponse("bambang 404 tapi tidak 404, bingungkan")
