# i have created this file-harry
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext =request.POST.get('text','default')

    #check checkbox values
    removepunc =request.POST.get('removepunc','off')
    fullcaps =request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')
    spaceremover =request.POST.get('spaceremover','off')
    charcount =request.POST.get('charcount','off')
    print(removepunc)
    print(djtext)

    #check which checkbox is on
    if removepunc=="on":
        #analyzed=djtext
        punctuations='''!@#$%^&*()_{}[]:;"'~|\,.><?/'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'remove punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #analyze the text
        #return render(request,'analyze.html',params)
    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'convert to UPPERCASE','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if(spaceremover=="on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'convert to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'convert to UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (charcount=="on"):
        analyzed=len(djtext)
        params = {'purpose':'character count','analyzed_text':analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)


    if(removepunc != "on" and fullcaps !="on" and newlineremover != "on" and spaceremover != "on" and charcount != "on"):
        return HttpResponse("Error initialize here please select any option from home page")
    return render(request, 'analyze.html', params)
