
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),  # Include URLs from the webapp app
]

handler404 = 'webapp.views.custom_404_view'


