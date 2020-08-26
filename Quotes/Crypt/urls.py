from django.urls import path
from .views import QuotesList, QuotesNow

urlpatterns = [
    path('quotes_list/', QuotesList.as_view()),
    path('quotes_now/', QuotesNow.as_view())
]
