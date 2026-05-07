from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('sales.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('sales.urls')), 
]

# ថែមផ្នែកខាងក្រោមនេះ ដើម្បីឱ្យរូបភាពបង្ហាញចេញ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)