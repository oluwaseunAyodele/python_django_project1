"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_1.views import apphome,appabout,appblog, appcontact, appblog_details,shop

from django.conf import settings # new
from django.conf.urls.static import static # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', apphome,name="App home page" ),
     path('about/', appabout,name="App About page" ),
     path('contact/', appcontact,name="AppContact  page" ),
     path('blog/', appblog,name="App Blog page" ),
     path('blog/<int:cid>',  appblog_details,name="App Blog Details page" ),
     path('shop/', shop,name="shop page" ),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
    