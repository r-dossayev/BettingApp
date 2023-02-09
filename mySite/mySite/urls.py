
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

from oneXbet.views import handler404,handler500

urlpatterns = [
    path('one/', include('oneXbet.urls')),
    path('admin/', admin.site.urls),
]


handler404 = handler404
handler500 = handler500

