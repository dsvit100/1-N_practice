from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm): # 입력폼 생성 클래스
    class Meta(): # 폼의 설정을 담당하는 클래스
        model = Article # Article이 가진 필드를 기준으로
        fields = '__all__' # 모든 필드를 이 폼에서 입력할게

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content',) # 튜플로 써야함