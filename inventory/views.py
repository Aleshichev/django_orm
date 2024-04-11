from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Brand

def create(request):
    
    Brand.objects.create(brand_id=6, name='trpuma')
    
    return HttpResponse('Brand created')
    
