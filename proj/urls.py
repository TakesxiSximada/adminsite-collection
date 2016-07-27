from django.conf.urls import url, include
from django.contrib import admin

from .pushes import urls as pushes_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(pushes_urls.router.urls)),
]
