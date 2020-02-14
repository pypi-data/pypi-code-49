from django.conf.urls import url, include


app_name='bankgateways'

urlpatterns = [
    # url(r'^payments/', include('aparnik.packages.shops.payments.urls', namespace='payments')),
    # url(r'^orders/', include('aparnik.packages.shops.orders.urls', namespace='orders')),
    url(r'^zarinpals/', include('aparnik.packages.bankgateways.zarinpals.urls', namespace='zarinpals')),
    url(r'^bmi/', include('aparnik.packages.bankgateways.bmi.urls', namespace='bmi')),
]
