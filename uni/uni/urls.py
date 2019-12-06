from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^uni/', include('core.urls')),
    url(r'^api/', include('rest.urls')),
    url(r'^accounts/', include('account.urls')),
]
