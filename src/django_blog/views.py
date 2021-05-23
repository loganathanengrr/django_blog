from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

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

	return HttpResponse(template_obj.render(context))