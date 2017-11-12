from django.conf.urls import url
from django.views.generic.base import TemplateView
from .views import subscribe, MemberDeleteView

urlpatterns = (
    url(r'^', subscribe, name='subscribe'),
    url(r'^(?P<slug>[\w-]+)/delete/$', MemberDeleteView.as_view(), name='delete'),
    url(r'^subscribe/success/$', TemplateView.as_view(
        template_name='mailchimp/successful_subscription.html'),
        name='subscribe_success'),
    url(r'^subscribe/failure/$', TemplateView.as_view(
        template_name='mailchimp/failed_subscription.html'),
        name='subscribe_failed'),
)