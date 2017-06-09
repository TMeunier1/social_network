from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="homepage.html")),
    url(r'^profil/', include("people.urls")),
    url(r'^admin/', admin.site.urls),
    url(r'^profile/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
