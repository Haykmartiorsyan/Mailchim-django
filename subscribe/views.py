from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SubscribeForm
import urllib
import json
from django.conf import settings


key = str(settings.MAILCHIMP_API_KEY)
list_sub = str(settings.MAILCHIMP_SUBSCRIBE_LIST_ID)
data_center = str(settings.MAILCHIMP_DATA_CENTER)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            if form.save():
                return HttpResponseRedirect(reverse('subscribe_success'))
            else:
                return HttpResponseRedirect(reverse('subscribe_failed'))
    else:
        form = SubscribeForm()

    url = 'https://' + data_center + '.api.mailchimp.com/3.0/lists/' + list_sub + '/members?apikey=' + key + ''
    r = urllib.request.urlopen(url)
    data = json.loads(r.read())

    return render(request, 'mailchimp/subscribe.html', {
        'form': form,
        'data': data,
        'key': key,
        'list_id': list_sub,
        'data_center': data_center,
    })










