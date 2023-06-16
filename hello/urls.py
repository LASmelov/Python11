from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from firstapp import views
from firstapp import views


urlpatterns = [

    path('', views.index),
    path('', views.index),
    # path('about/', views.about),
    # path('contact/', views.contact),
    # path('details/', views.details),
    ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)