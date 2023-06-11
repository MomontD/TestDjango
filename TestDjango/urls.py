from django.contrib import admin
from django.urls import path,include

from django.conf import settings             # необхідно для папки static
from django.conf.urls.static import static   # необхідно для папки static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('governments/',include('governments.urls')),
    path('deposits/',include('deposits.urls')),
    path('loans/',include('loans.urls')),
    path('operations/',include('operations.urls')),
    path('generalreport/',include('generalreport.urls')),
    path('currency/',include('currency.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # необхідно для папки static
