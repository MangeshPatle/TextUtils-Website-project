# i have created this file-harry
from django.http import HttpResponse
#video 8
from django.shortcuts import render

#code video 6
# def index(request):
#     return HttpResponse('''<h1>harry bhai</h1> <a href="F:\collage work\c,c++,java,python programming\c++ video">django code wirh harry</a>''')
#
# def about(request):
#     return HttpResponse("about harry bhai")



#code video 7
# def index(request):
#     return HttpResponse("home")
#
# def removepunc(request):
#     return HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove first")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/charcount'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character count <a href='/'>back</a>")




#video 8,9
# def index(request):
#     # params={'name':'harry','place':'mars'}
#     # return render(request,'index.html',params)
#
#     return render(request, 'index.html')
#
# def removepunc(request):
#     #get the text
#     djtext =request.GET.get('text','default')
#     print(djtext)
#     #analyze the text
#     return HttpResponse("remove punc")
#
# # def removepunc(request):
# #     return render(request,'rvove.html')
#
# def calculator(request):
#     return render(request,'calculator.html')
#
# def act_game(request):
#     return render(request,'action_game.html')
#
# def capfirst(request):
#     #print(request.GET.get('text','default'))
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line remove first")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/charcount'>back</a>")
#
# def charcount(request):
#     return HttpResponse("character count <a href='/'>back</a>")
#

#video 10,12

def index(request):
    # params={'name':'harry','place':'mars'}
    # return render(request,'index.html',params)

    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext =request.GET.get('text','default')

    #check checkbox values
    removepunc =request.GET.get('removepunc','off')
    fullcaps =request.GET.get('fullcaps','off')
    newlineremover =request.GET.get('newlineremover','off')
    spaceremover =request.GET.get('spaceremover','off')
    charcount =request.GET.get('charcount','off')
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
        #analyze the text
        return render(request,'analyze.html',params)
    elif (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'convert to UPPERCASE','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)


    elif(spaceremover=="on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'convert to UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (charcount=="on"):
        analyzed=len(djtext)
        params = {'purpose':'convert to UPPERCASE','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")






