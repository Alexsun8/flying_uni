from django.conf.urls import url


from account.views import update_profile

urlpatterns = [
    url(r'^edit$', update_profile),
]
