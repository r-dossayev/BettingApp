from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from oneXbet.views import handler404, handler500, RegisterUser, login

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', login, name="login"),
    path('one/', include('oneXbet.urls')),
    path('admin/', admin.site.urls),
]



handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

