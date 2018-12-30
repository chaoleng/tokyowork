from django.shortcuts import render

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
#coding=utf-8
#import time,simplejson,json,os,commands

# Create your views here.
def index(req):
        ##
        ##
        #return HttpResponse("aa")
        return render_to_response('index.html',)
