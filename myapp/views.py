from django.shortcuts import render

# Create your views here.
def view1(request):
	name =input("enter name: ")
	place = input("enter place: ")
	c={'Name':name,'place':place} #dictionory(context), used to fectch in html templates
	return render(request,'htmlpages/1.html',c)