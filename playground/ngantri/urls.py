from django.urls import path
from . import views

app_name = "ngantri"


urlpatterns = [
    path("", views.index, name="index"),
    path("qrcode/<int:idperson>", views.theqr, name="theqr"),
    path("test", views.test, name="test"),
    path("upload-save", views.uploadSave, name="uploadsave"),
    path("upload", views.upload, name="upload"),
]
