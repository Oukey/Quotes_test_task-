from django.urls import path
from .views import QuotesList

urlpatterns = [
    path('quotes_list/', QuotesList.as_view())
]
