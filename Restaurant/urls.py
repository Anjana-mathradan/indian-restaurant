from django.contrib import admin
from django.urls import path,include
import backend.urls
import frontend.urls
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from Restaurant import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include(backend.urls)),
    path('',include(frontend.urls))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
