from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def author_list(request):
    
    author=[]
    author1={'id':1,'name':'John'}
    author2={'id':2,'name':'Mark'}
    author.append(author1)
    author.append(author2)
    context ={}
    context['authors'] = author
    
    print(type(request))  # Prints the type of the request object
    print(request)        # Prints the details of the request
    # return HttpResponse("Hello, World!")  # Returns a simple HTTP response
    return render (request,'author/list.html',context)
def author_create(request):
    print(type(request))
    print(request)
    res = HttpResponse("Hello, world!")
    res.write("<p>hello open </p>")  # Writes additional HTML to the response
    return res  # Return the response with the added content

def author_update(request,id):
    print(type(request))
    print(id,type)
    print(request)
    return HttpResponse(f"Book update page {id}")  # Returns a simple HTTP response
def author_delete(request,id):
    print(type(request))
    print(id,type)
    print(request)
    return HttpResponse(f"Book delete page {id}")  # Returns a simple HTTP response