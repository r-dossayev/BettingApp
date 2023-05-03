from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from oneXbet.views import *
from django.views.decorators.cache import cache_page
router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path('register/', registerUser, name="register"),
    path('login/', cache_page(100)(LoginUserForm.as_view()), name="login"),
    path('logout/', custom_logout, name="logout"),
    path('one/', include('oneXbet.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/alpha/auth/register/', RegisterViewAPI.as_view(), name='register_api'),
    # path('api/alpha/auth/login/', adminLogin, name='login_api'),
    # path('api/alpha/auth/logout/', adminLogout, name='logout_api'),
    path('api/alpha/auth/me/', AuthMe.as_view(), name='user_data_api'),
    path('api/alpha/leagues/', FootballLeaguesViewSet.as_view({'get': 'list'})),
    path('api/alpha/leagues/<int:pk>/', FootballLeaguesViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
    path('api/alpha/leagues/<int:pk>/clubs/', LeagueClubsViewSet.as_view({'get': 'list'})),
    path('api/alpha/leagues/<int:id>/clubs/<int:pk>/',  # one club in league get and put
         LeagueClubsViewSet.as_view({'put': 'update', 'get': 'retrieve'})),
    path('api/alpha/', include(router.urls)),
    path('', index)
]
handler404 = handler404
handler500 = handler500

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
