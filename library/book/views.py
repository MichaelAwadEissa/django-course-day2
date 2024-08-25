from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def book_list(request):
    print(type(request))  # Prints the type of the request object
    print(request)        # Prints the details of the request
    # return HttpResponse("Hello, World!")  # Returns a simple HTTP response
    return render(request,'book/list.html')
def book_create(request):
    print(type(request))
    print(request)
    res = HttpResponse("Hello, world!")
    res.write("<p>hello open </p>")  # Writes additional HTML to the response
    return res  # Return the response with the added content

def book_update(request,id):
    print(type(request))
    print(id,type)
    print(request)
    return HttpResponse(f"Book update page {id}")  # Returns a simple HTTP response
def test_base(request):
    # Attempt to render the 'base.html' template
    return render(request, 'base.html')