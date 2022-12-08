from django.urls import path
from . import views

app_name = "ngantri"


urlpatterns = [
    path("upload", views.upload, name="upload"),
    path("test", views.test, name="test"),
    path("qrcode/<int:idperson>", views.theqr, name="theqr")
]
