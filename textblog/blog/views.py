from django.shortcuts import render_to_response,HttpResponse
from blog.models import *
from textblog.hash_url  import get_hash_key


def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET:
		message = request.GET['q']
		message2 = request.get_full_path()
		
		message3 = request.get_host()
		message4 = get_hash_key(message2)
		print message4[2]
		
		str_a = ['http://',message3,'/share/',message4[2]]

		str_b = ''.join(str_a)



		ringo = Book.objects.create(name=message,url=message4[2])
		
		ringo.save()

	else:
		message = 'You submitted an empty form.'
	return render_to_response('return.html',{'message':message,'str_b':str_b})

def share(request,message):


	p = Book.objects.raw('SELECT id FROM blog_book where url = %s limit 1',[message])
	print p[0].id
	print p[0].name
	print p[0].url
		
	


	return render_to_response('return.html',{'message':p[0].name})
