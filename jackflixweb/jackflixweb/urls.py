
from django.contrib import admin
from django.urls import path, include
from .views import redirect_root

urlpatterns = [

    path('', redirect_root),
    path('admin/', admin.site.urls),
    path(route='principal/', view=include('principal.urls')),
    path(route='genero/', view=include('genero.urls')),
    path(route='serie/', view=include('serie.urls')),
    path(route='filme/', view=include('filme.urls'))
]
