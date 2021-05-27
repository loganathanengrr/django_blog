from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth import  get_user_model

User =  get_user_model()

def home_page(request):
	template_name = "home.html"
	context = {}
	return render(request, template_name, context)

def about_page(request):
	context = {
	"body":"Hey this is an about_page",
	"item_list":[1,2,3,5]
	}
	template_obj = get_template("about.html")
	
	qs =  User.objects.all()
	print(qs)

	return HttpResponse(template_obj.render(context))