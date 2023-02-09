from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from app.views import IndexView, StudentsListView, ProfessorsListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('students/', StudentsListView.as_view(), name='students'),
    path('professors/', ProfessorsListView.as_view(), name='professors'),
    path('student-update/<int:pk>/', UserUpdateView.as_view(), name='student-update'),
    path('professor-update/<int:pk>/', UserUpdateView.as_view(), name='professor-update'),
    path('user/<int:pk>/delete', UserDeleteView.as_view(), name='user-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
