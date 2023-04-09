from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from oneXbet.views import *

urlpatterns = [
    path('register/', registerUser, name="register"),
    path('login/', LoginUserForm.as_view(), name="login"),
    path('logout/', custom_logout, name="logout"),
    path('one/', include('oneXbet.urls')),
    path('admin/', admin.site.urls),
    path('api/alpha/register/', RegisterViewAPI.as_view(), name='register_api'),
    # path('api/alpha/auth/login/', adminLogin, name='login_api'),
    path('api/alpha/leagues/', FootballLeaguesViewSet.as_view({'get': 'list'})),
    path('api/alpha/leagues/<int:pk>/', FootballLeaguesViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
    path('api/alpha/leagues/<int:pk>/clubs/', LeagueClubsViewSet.as_view({'get': 'list'})),
    path('api/alpha/leagues/<slug:url>/clubs/<int:pk>/',  # one club in league get and put
         LeagueClubsViewSet.as_view({'put': 'update', 'get': 'retrieve'})),

    path('', index)
]
handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
