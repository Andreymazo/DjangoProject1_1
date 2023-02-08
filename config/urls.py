from django.views.generic import TemplateView
from config import settings ##No good
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from catalog.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', hello, name='home'),#WRONG
    path('', TemplateView.as_view(template_name='users/home.html'), name='home'),
    path('users/password_reset', TemplateView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    path('', include('catalog.urls', namespace='catalog')),
    path('users/', include('users.urls', namespace='users'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)