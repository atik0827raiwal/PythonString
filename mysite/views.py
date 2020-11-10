from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    final_text = ""
    text = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    upper = request.POST.get('upper','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",\<>./?@#$%^&*_~'''
        final_text = ""
        for char in text:
            if char not in punctuations:
                final_text = final_text + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': final_text}
        text = final_text


    if upper=="on":
        final_text = ""
        for char in text:
            final_text = final_text + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': final_text}
        text = final_text
        
    
    if newlineremover=="on":
        final_text = ""
        for char in text:
            if char!="\n" and char!="\r":
                final_text = final_text + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': final_text}
        text = final_text
    
    if(extraspaceremover=="on"):
        final_text = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                final_text= final_text + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': final_text}
        text = final_text
    
    if(extraspaceremover == "off" and newlineremover=="off" and upper=="off" and removepunc=="off"):
        params = {'purpose': 'No operation is seleceted', 'analyzed_text': final_text}
        # Analyze the text
    


    return render(request, 'analyze.html', params)