
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/', include('myapp.urls')),
    path('homeview/', views.HomeView.as_view(),name="homeview"),
    path('candidate/<int:pk>', views.Candidate.as_view(),name="candidate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
