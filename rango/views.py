from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	#construct a dictionary to pass to template engine as its context
	# Note the key is boldmessage (same as template index.html file)
	context_dict = {'boldmessage': "Big olleee sleep panda"}
	#return rendered response to send to client
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_about = {'bigmsg':"Big ollleeeeee camel"}
	return render(request, 'rango/about.html', context=context_about)
	#HttpResponse("Rangos about page <a href='/rango/'>Index</a>")