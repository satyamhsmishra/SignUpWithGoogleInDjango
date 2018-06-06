from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import login
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',login,{'template_name':'authentication/login.html'}),
    path('',include('django.contrib.auth.urls')),
    path('oauth/',include('social_django.urls',namespace='social')),

]
