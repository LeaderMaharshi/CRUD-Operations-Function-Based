
from django.contrib import admin
from django.urls import include, path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enroll.urls'))
]
