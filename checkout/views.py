from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):

    # get the bag from session and if empty, redirect user to products page
    bag = request.session.get('bag', {})
    if not bag: 
        messages.error(request, 'There is nothing in your bag at the moment')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NQqzwHISqP7PCz88iYHXKXxhyzB7LZDVXo6KuvG3VjQA2wRfJM5ru5nBgrY6SW5PsJ4NFG0Vl2nYYywUu76Sj2600eGmTo526',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
