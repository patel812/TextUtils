
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view( request):
    dict = {'name': 'Abhishek', 'place': 'mumbai'}
    return render(request, 'testapp/home.html', dict)

def removepunc_view(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'one':'Removed Punctuations', 'two': analyzed}
        djtext = analyzed 
        #return render(request, 'testapp/remove.html',params)
    
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        
        params = {'one':'Changed to Upper case', 'two': analyzed}
        djtext = analyzed
        return render(request, 'testapp/remove.html',params)
    

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        
        params = {'one':'Removed NewLines', 'two': analyzed}
        djtext = analyzed
        return render(request, 'testapp/remove.html',params)
    

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1]== " "):
                analyzed = analyzed + char
        
        params = {'one':'Removed NewLines', 'two': analyzed}
        djtext = analyzed
                      
      
    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse('please ')
            
    return render(request, 'testapp/remove.html',params) 
    

def base_view( request):
    return render(request, 'testapp/base.html')