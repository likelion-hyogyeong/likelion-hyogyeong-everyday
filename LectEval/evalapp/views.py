from django.shortcuts import render, redirect, get_object_or_404
from .models import List, Comment
from .forms import MajorNew, LiberalNew, ElectiveNew, New, CommentForm
from django.db.models import Q
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import date

# Create your views here.
def search(request):          
    title =  request.GET.get('search')
    body = request.GET.get('search')
    status = List.objects.filter(Q(title__icontains=title) | Q(body__icontains = body))
    return render(request,'search.html',{'status':status})  

def home(request):
    new = List.objects.all()[:3]
    popluar = List.objects.filter(Q(score = 5) | Q(score = 4))[:3]

    return render(request, 'home.html', {'new':new, 'popular':popluar})

def detail(request, blog_id):
    blog = get_object_or_404(List, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog})

def home_new(request):
    if request.method == 'POST':
        home_post =  List.objects.all()
        home_form = New(request.POST)
        if home_form.is_valid(): 
            home_post = home_form.save(commit=False)
            home_post.pub_date = timezone.now()
            home_post.writer = request.user
            home_post.save()
        return redirect('home')   
    else:
        home_form = New()
        return render(request, 'home_new.html', {'home_form': home_form})

def new(request):
    new_list = List.objects.all()

    paginator = Paginator(new_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 

    return render(request, 'new.html', {'new_list':new_list, 'posts':posts})

def new_detail(request, new_id):
    new_detail = get_object_or_404(List, pk = new_id)
    return render(request, 'new_detail.html', {'new_detail':new_detail})

def new_create(request, new_id):
    
    if request.method == 'POST':
        post = get_object_or_404(List, pk = new_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        return redirect('/new/' + str(post.id))
    else:
        form = CommentForm()
        return render(request, 'new_detail.html', {'form':form})

def popular(request):
    popular_list = List.objects.filter(Q(score = 5) | Q(score = 4))

    paginator = Paginator(popular_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 

    return render(request, 'popular.html', {'popular_list':popular_list, 'posts':posts})

def popular_detail(request, popular_id):
    popular_detail = get_object_or_404(List, pk = popular_id)
    return render(request, 'popular_detail.html', {'popular_detail':popular_detail})

def popular_detail_full(request, pop_full_id):
    popular_detail_full = get_object_or_404(List, pk = pop_full_id)
    return render(request, 'popular_detail_full.html', {'popular_detail_full':popular_detail_full})
  
def major(request):
    major_list = List.objects.filter(field = '전공')

    paginator = Paginator(major_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'major.html', {'major_list':major_list, 'posts':posts})

def major_detail(request, major_id):
    major_detail = get_object_or_404(List, pk = major_id)
    return render(request, 'major_detail.html', {'major_detail':major_detail})

def major_new(request):
    if request.method == 'POST':
        major_post =  List.objects.filter(field = '전공')
        major_form = MajorNew(request.POST)
        if major_form.is_valid(): 
            major_post = major_form.save(commit=False)
            major_post.field = '전공'
            major_post.pub_date = timezone.now()
            major_post.writer = request.user
            major_post.save()
        return redirect('major')   
    else:
        major_form = MajorNew()
        return render(request, 'major_new.html', {'major_form': major_form})

def major_edit(request, m_edit_id):
    
    major_edit = get_object_or_404(List, pk = m_edit_id)

    if  request.method == 'POST':
        major_form = MajorNew(request.POST, instance=major_edit)
        if major_form.is_valid():
            major_form.save()
        return redirect('/major/' + str(major_edit.id))
    else:
        major_form = MajorNew(instance=major_edit)
        return render(request, 'major_edit.html', {'e_edits':major_edit, 'major_form':major_form})

def major_delete(request, major_id):
    major = get_object_or_404(List, pk = major_id)
    major.delete()
    return redirect('major')

def m_comment_create(request, major_id):
    
    if request.method == 'POST':
        m_post = get_object_or_404(List, pk = major_id)
        m_form = CommentForm(request.POST)
        if m_form.is_valid():
            m_comment = m_form.save(commit=False)
            m_comment.post = m_post
            m_comment.save()
        return redirect('/major/' + str(m_post.id))
    else:
        m_form = CommentForm()
        return render(request, 'major_detail.html', {'m_form':m_form})
    
def m_comment_delete(request, major_id, comment_id):
    
    m_post = get_object_or_404(List, pk = major_id)
    m_comment = get_object_or_404(Comment, pk = comment_id)
    m_comment.delete()

    return redirect('/major/' + str(m_post.id))

def m_comment_edit(request, major_id, comment_id):
    
    m_post = get_object_or_404(List, pk = major_id)
    m_comment = get_object_or_404(Comment, pk = comment_id)
    
    if request.method == 'POST':
        m_comment.text = request.POST['text']
        m_comment.save()
        return redirect('/major/' + str(m_post.id))
    else:
       
        return render(request, 'major_detail_comment_edit.html', {'m_post':m_post,'m_comment':m_comment})
    
def liberal(request):
    liberal_list = List.objects.filter(field = '교양')

    paginator = Paginator(liberal_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'liberal.html', {'liberal_list':liberal_list, 'posts':posts})

def liberal_detail(request, liberal_id):
    liberal_detail = get_object_or_404(List, pk = liberal_id)
    return render(request, 'liberal_detail.html', {'liberal_detail':liberal_detail})

def liberal_new(request):
    if request.method == 'POST':
        liberal_post =  List.objects.filter(field = '교양')
        liberal_form = LiberalNew(request.POST)
        if liberal_form.is_valid(): 
            liberal_post = liberal_form.save(commit=False)
            liberal_post.field = '교양'
            liberal_post.pub_date = timezone.now()
            liberal_post.writer = request.user
            liberal_post.save()
        return redirect('liberal')         
    else:
        liberal_form = LiberalNew()
        return render(request, 'liberal_new.html', {'liberal_form': liberal_form})

def liberal_edit(request, l_edit_id):
    
    liberal_edit = get_object_or_404(List, pk = l_edit_id)

    if  request.method == 'POST':
        liberal_form = LiberalNew(request.POST, instance=liberal_edit)
        if liberal_form.is_valid():
            liberal_form.save()
        return redirect('/liberal/' + str(liberal_edit.id))
    else:
        liberal_form = LiberalNew(instance=liberal_edit)
        return render(request, 'liberal_edit.html', {'e_edits':liberal_edit, 'liberal_form':liberal_form})

def liberal_delete(request, liberal_id):
    liberal = get_object_or_404(List, pk = liberal_id)
    liberal.delete()
    return redirect('liberal')

def l_comment_create(request, liberal_id):
    
    if request.method == 'POST':
        l_post = get_object_or_404(List, pk = liberal_id)
        l_form = CommentForm(request.POST)
        if l_form.is_valid():
            l_comment = l_form.save(commit=False)
            l_comment.post = l_post
            l_comment.save()
        return redirect('/liberal/' + str(l_post.id))
    else:
        l_form = CommentForm()
        return render(request, 'liberal_detail.html', {'l_form':l_form})

def l_comment_delete(request, liberal_id, comment_id):
    
    l_post = get_object_or_404(List, pk = liberal_id)
    l_comment = get_object_or_404(Comment, pk = comment_id)
    l_comment.delete()

    return redirect('/liberal/' + str(l_post.id))

def l_comment_edit(request, liberal_id, comment_id):
    
    l_post = get_object_or_404(List, pk = liberal_id)
    l_comment = get_object_or_404(Comment, pk = comment_id)
    
    if request.method == 'POST':
        l_comment.text = request.POST['text']
        l_comment.save()
        return redirect('/liberal/' + str(l_post.id))
    else:
       
        return render(request, 'liberal_detail_comment_edit.html', {'l_post':l_post,'l_comment':l_comment})

def elective(request):
    elective_list = List.objects.filter(field = '선택')

    paginator = Paginator(elective_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'elective.html', {'elective_list':elective_list, 'posts':posts})

def elective_detail(request, elective_id):
    elective_detail = get_object_or_404(List, pk = elective_id)
    return render(request, 'elective_detail.html', {'elective_detail':elective_detail})

def elective_new(request):
    if request.method == 'POST':
        elective_post =  List.objects.filter(field = '선택')
        elective_form = ElectiveNew(request.POST)
        if elective_form.is_valid(): 
            elective_post = elective_form.save(commit=False)
            elective_post.field = '선택'
            elective_post.pub_date = timezone.now()
            elective_post.writer = request.user
            elective_post.save()
        return redirect('elective')           
    else:
        elective_form = ElectiveNew()
        return render(request, 'elective_new.html', {'elective_form': elective_form})

def elective_edit(request, e_edit_id):

    elective_edit = get_object_or_404(List, pk = e_edit_id)

    if  request.method == 'POST':
        elective_form = ElectiveNew(request.POST, instance=elective_edit)
        if elective_form.is_valid():
            elective_form.save()
        return redirect('/elective/' + str(elective_edit.id))
    else:
        elective_form = ElectiveNew(instance=elective_edit)
        return render(request, 'elective_edit.html', {'e_edits':elective_edit, 'elective_form':elective_form})

def elective_delete(request, elective_id):
    elective = get_object_or_404(List, pk = elective_id)
    elective.delete()
    return redirect('elective')

def e_comment_create(request, elective_id):

    if request.method == 'POST':
        e_post = get_object_or_404(List, pk = elective_id)
        e_form = CommentForm(request.POST)
        if e_form.is_valid():
            e_comment = e_form.save(commit=False)
            e_comment.post = e_post
            e_comment.save()
        return redirect('/elective/' + str(e_post.id))
    else:
        e_form = CommentForm()
        return render(request, 'elective_detail.html', {'e_form':e_form})

def e_comment_delete(request, elective_id, comment_id):

    e_post = get_object_or_404(List, pk = elective_id)
    e_comment = get_object_or_404(Comment, pk = comment_id)
    e_comment.delete()

    return redirect('/elective/' + str(e_post.id))

def e_comment_edit(request, elective_id, comment_id):

    e_post = get_object_or_404(List, pk = elective_id)
    e_comment = get_object_or_404(Comment, pk = comment_id)
    
    if request.method == 'POST':
        e_comment.text = request.POST['text']
        e_comment.save()
        return redirect('/elective/' + str(e_post.id))
    else:
       
        return render(request, 'elective_detail_comment_edit.html', {'e_post':e_post,'e_comment':e_comment})
    

#aside

def February(request):
    february_list = List.objects.filter(pub_date__year='2020', pub_date__month='02',)
    
    paginator = Paginator(february_list, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 

    return render(request, 'February.html', {'february_list':february_list, 'posts':posts})

def February_detail(request, february_id):
    february_detail = get_object_or_404(List, pk = february_id)
    return render(request, 'February_detail.html', {'february_detail':february_detail})

def empty(request):
    return render(request, 'empty.html')