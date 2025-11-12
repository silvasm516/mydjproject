from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import Template
from django.template import loader

# def doubledb(request):
    # c = {   'tit' : 'Double Declining Balance Depreciation Calculator'}
    # temp = loader.get_template('DDB.html')
    # return HttpResponse(temp.render(c, request))






class HomePageView(TemplateView):
    template_name =  ('modcities.html')
    
    
    
    
    
    
    