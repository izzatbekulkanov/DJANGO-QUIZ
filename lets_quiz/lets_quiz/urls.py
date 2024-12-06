from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

from quiz.views import SystemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quiz.urls')),
]

# Xato sahifalari
handler404 = SystemView.as_view(template_name="quiz/error_404.html", http_status=404)
handler500 = SystemView.as_view(template_name="quiz/error_500.html", http_status=500)

# Statik fayllar (faqat DEBUG rejimida)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
