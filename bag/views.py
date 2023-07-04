from django.shortcuts import render


def view_bag(request):
    """ Bag content page """

    return render(request, 'bag/bag.html')
