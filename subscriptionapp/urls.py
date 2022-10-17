from django.urls import path
from subscriptionapp.views import SubscriptionListView, SubscriptionView
app_name = 'subscriptionapp'

urlpatterns = [

    path('subscribe/',SubscriptionView.as_view(),name='subscription'),
    path('list/',SubscriptionListView.as_view(),name='list')
]