from django.contrib import admin
from django.urls import path, include



from core.views import list_it, home, about


urlpatterns = [
    path('admin/', admin.site.urls),

    # path("core/", include("core.urls_test") ),

    path('', list_it, name='list'),
    path('home/', home, name='list'),
    path('about/', about, name='list'),
]
