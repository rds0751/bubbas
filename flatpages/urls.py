from flatpages import views
from django.urls import path

urlpatterns = [
    path('<path:url>', views.flatpage, name='flatpages.views.flatpage'),
]
