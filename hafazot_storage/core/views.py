from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Item
from django.http import Http404

def get_object(file_slug):
    try:
        return Item.objects.get(slug=file_slug).file.url
    except Item.DoesNotExist:
        raise Http404

def view_file(request, file_slug):
    item = get_object(file_slug)
    print(item)
    return render(request, 'file.html', {'item': item})
