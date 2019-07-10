from django.shortcuts import render , get_object_or_404
from random import randint
from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from MainApp.models import Cart
from django.views.decorators.csrf import csrf_exempt

def payment_process(request):
    host = request.get_host()
    all = Cart.objects.filter(cart_user=request.user)
    total = []
    for i in all:
        total.append(i.total)
    x=sum(total)
    paypal_dict = {
         'busiess':settings.PAYPAL_RECEIVER_EMAIL,
         'amount':'%.2f'% x,
         'item_name':all,
         'invoice':randint(1,1000000),
         'currency_code':'USD',
         'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
         'return_url':'http://{}{}'.format(host,reverse('payment:done')),
         'cancel_return':'http://{}{}'.format(host,reverse('payment:cancelled'))
        }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'process.html', {'form':form})
@csrf_exempt
def payment_done(request):
    return render(request, 'done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'canceled.html')
