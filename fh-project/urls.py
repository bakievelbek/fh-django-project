from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from app.views import Index, StudentsList, ProfessorsList

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('students/', StudentsList.as_view(), name='students'),
    path('professors/', ProfessorsList.as_view(), name='professors'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
