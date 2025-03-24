from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article

# Create your views here.

# 사용자가 요청하면(접속) 쓸 수 있는 빈 종이를 마련한다(GET)
# 사용자가 작성한 종이를 제출한다(POST)
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)  # 사용자의 데이터를 담은 제출 서류
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm() # 빈 종이
    context = {
        'form': form,
        }
    return render(request, 'create.html', context)

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)

def detail(request, id):
    article = Article.objects.get(id=id)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)


def update(request, id):
    # edit
    article = Article.objects.get(id=id) # 수정할 글 가져오기
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article) # 앞은 덮어쓸 새정보, 뒤는 이전 정보
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }

    return render(request, 'update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')


# def comment_create(request, id):
    
        
