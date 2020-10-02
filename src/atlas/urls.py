from django.contrib import admin
from django.urls import path
from Mainapp.views import forminput, ML

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',forminput),
    path('Result/',ML),
]

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
