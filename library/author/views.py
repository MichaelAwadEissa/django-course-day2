# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def author_list(request):
    
#     author=[]
#     author1={'id':1,'name':'John'}
#     author2={'id':2,'name':'Mark'}
#     author.append(author1)
#     author.append(author2)
#     context ={}
#     context['authors'] = author
    
#     print(type(request))  # Prints the type of the request object
#     print(request)        # Prints the details of the request
#     # return HttpResponse("Hello, World!")  # Returns a simple HTTP response
#     return render (request,'author/list.html',context)
# def author_create(request):
#     print(type(request))
#     print(request)
#     res = HttpResponse("Hello, world!")
#     res.write("<p>hello open </p>")  # Writes additional HTML to the response
#     return res  # Return the response with the added content

# def author_update(request,id):
#     print(type(request))
#     print(id,type)
#     print(request)
#     return HttpResponse(f"Book update page {id}")  # Returns a simple HTTP response
# def author_delete(request,id):
#     print(type(request))
#     print(id,type)
#     print(request)
#     return HttpResponse(f"Book delete page {id}")  # Returns a simple HTTP response
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def author_list(request):
    author=[]
    auth1={'id':1,'name':'aya'}
    auth2={'id':2,'name':'ali'}
    author.append(auth1)
    author.append(auth2)
    context={}
    context['authors']=author
    return render(request,'author/list.html',context)
    # return  HttpResponse('<h1>list author</h1>')
def author_create(request):
    return  HttpResponse('<h1>create author</h1>')
def author_update(request,id):
    # return  HttpResponse('<h1>update author</h1>')
    context={'id':id}
    return render(request, 'author/update.html', context)
def author_delete(request,id):
    # return  HttpResponse('<h1>Delete author</h1>')
    context = {'id': id}
    return render(request, 'author/delete.html', context)
def author_show(request,id):
    # return  HttpResponse('<h1>Delete author</h1>')
    context = {'id': id}
    return render(request, 'author/show.html', context)