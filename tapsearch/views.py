# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.shortcuts import render
from django.http import HttpResponse
from .models import TextMap
from django.db.models import Max


def indexView(request):
	context = {}
	return render(request,'tapsearch/form.html',context)



def searchView(request):
	return render(request,'tapsearch/search.html')

def InputTextView(request):
	if request.method == 'POST':
		global idx
		variable = TextMap.objects.all().aggregate(Max('doc_index'))
		idx = variable['doc_index__max'] if variable['doc_index__max'] else 1
		text = request.POST.get('textfield')
		text = text.lower()
		clean_text = re.sub(r'[^\w\s]','', text)
		clean_text = clean_text.split('\r\n\r\n')
		for item in clean_text:
			mapping = dict()
			regex = re.compile(r'[\n\r\t]')
			item = regex.sub(" ",item)
			words = item.split(' ')
			for word in words:
				if word in mapping:
					word_freq = mapping[word]
				else:
					word_freq = 0
				mapping[word]= word_freq+1

			for word,freq in mapping.items():
				data = TextMap(doc_index=idx,words=word,frequency=freq)
				data.save()
			idx += 1

		context = {}
		return render(request,'tapsearch/success_redirect.html',context)
	else:
		return HttpResponse("Error. Please go Back to previous page")

def search(request):
	if(request.method=='POST'):
		keyword1 = str(request.POST['textfield'])
		keyword1 = keyword1.lower()
		keyword = keyword1.split()
		res = []
		for item in keyword:
			temp = TextMap.objects.filter(words = item).order_by('-frequency')[:10]
			if temp:
				res.append(temp)
		flg = False
		if res:
			flg=True
		context = {
		'result':res,
		'flag':flg,
		'search':keyword1
		}
		return render(request,'tapsearch/results.html',context)
	else:
		return HttpResponse('Invalid Request, Go Back!!')

# def welcome(request):
# 	return HttpResponse("<h2>Welcome to TapSearch<h2><br><a href= '/tapsearch/index'>Index</a><br><a href= '/tapsearch/search'>Search</a><br><a href= '/tapsearch/clear'>Clear</a>")

def clear(request):
	TextMap.objects.all().delete()
	global idx
	idx=1
	return render(request,'tapsearch/clear.html')

def startpage(request):
	return render(request,'tapsearch/welcome.html')
	# return HttpResponse("<a href='/tapsearch/'><h2> Go to TapSearch<h2></a>")
