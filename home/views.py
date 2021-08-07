from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def main(request):
	return render(request,'navbar.html', {})

def about(request):
	return render(request,'about.html')
