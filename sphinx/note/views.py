#-*- coding:utf-8 -*-
from django.shortcuts  import redirect, render

from note.models import Notepad
from note.forms import NotepadForm
from note.func import generateStr
from note.hash_url  import get_hash_key

def index(request):
    """  Define the index request.      
        当没有输入内容的时候，随即生成的字符串url保存到数据库里面
    """
    #url = request.get_full_path()
    #print url
    baStr = generateStr()
    #shStr = get_hash_key(url)
    #实现数据库里面保存把生成的字符串保存 
    t1 = Notepad(basicStr = baStr, shareStr = "", text = "")
    t1.save()
    return redirect('/%s' %baStr) 

def noteprocess(request, basic,):
    """
        process function.    
    """
    if request.method == "POST":
        noteform = NotepadForm(request.POST)
        if noteform.is_valid():
            mytext = noteform.cleaned_data['text']
            url = request.get_full_path()
            shStr = get_hash_key(url)
            t1=Notepad.objects.get(basicStr=basic)
            t1.text = mytext
            t1.shareStr = shStr
            p = t1.shareStr 
            t1.save()
            host = request.get_host()
            str_a = ['http://',host,'/share/',p]
            str_b = ''.join(str_a)
            return render(request,'return.html', {'text':str_b})
            #Later we need to refactoring. 
    else:
        noteform = NotepadForm()    
    mynotepad = Notepad.objects.get(basicStr = basic)
    return render(request, 'noteprocess.html',{'noteform':noteform,'mynotepad':mynotepad })

def share(request,q):
    p = Notepad.objects.get(shareStr=q)
    return render(request,'return.html', {'text':p.text})
