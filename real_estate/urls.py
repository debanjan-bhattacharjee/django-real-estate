from django.conf import settings
# q: What does settings do here?
# a: It allows us to access the settings in the settings.py file.
from django.contrib import admin
from django.urls import path, include
# q: What does include do here?
# a: It allows us to include other URL configurations
# from other apps in the project.
from django.conf.urls.static import static
# q: What does this above line do?
# a: It allows us to serve static files such as images, CSS, JavaScript, etc.
urlpatterns = [
    path('supersecret/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
