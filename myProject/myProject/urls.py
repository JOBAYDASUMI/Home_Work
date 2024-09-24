
from django.contrib import admin
from django.urls import path
from myProject.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
    path('loginPage/', loginPage, name='loginPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('registerPage/', registerPage, name='registerPage'),
    
    path('JobFeedPage/', JobFeedPage,name='JobFeedPage'),
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
