from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #utsav's url start
    path('designer/', include('designer.urls')),
    path('accounts/', include('accounts.urls')),
    #utsav's url end

    #dibya's url start
    path('', views.home, name='home'),
    path('recruiter/', include('recruiter.urls')),
    path('accounts/', include('accounts.urls')),
    #dibya's url end
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 