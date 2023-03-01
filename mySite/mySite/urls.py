from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from oneXbet.views import handler404, handler500, RegisterUser, LoginUserForm, custom_logout, index

urlpatterns = [
    path('register/', RegisterUser.as_view(), name="register"),
    path('login/', LoginUserForm.as_view(), name="login"),
    path('logout/', custom_logout, name="logout"),
    path('one/', include('oneXbet.urls')),
    path('admin/', admin.site.urls),
    path('', index)
]

handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
