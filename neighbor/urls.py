from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.signup, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.update_profile, name='update_profile'),
    path('newbusiness/', views.new_business, name='new_business'),
    path('newpost/', views.new_post, name='new_post'),
    path('newneighborhood/', views.new_neighborhood, name='new_neighborhood'),
    path('all-neighborhood/', views.all_neighborhood, name='neighborhood'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

