from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
                    #ForeignKey -> 연동  (연동안된자료는 출력/입력 불가)
    title = models.CharField(max_length=200)
    text = models.TextField()   #본문 (글자제한x)
    created_date = models.DateTimeField(default=timezone.now) #만든시간
    published_date = models.DateTimeField(blank = True, null=True) #게시시간
    
    def publish(self):
        self.published_date = timezone.now()  #timezone -> 서버시간기준으로잡아옴
        self.save()
        
    def __str__(self):
        return  str(self.pk) + ". " + self.title 
    
    # django --> shell with environment  -->  모든작업전에 임포트해야됨
    # Post.objects.get(title = '글')  --> 타이틀이 글인것을 뽑아옴 (2개이상일시에러)
    #  Post.objects.filter(published_date__lte=timezone.now())   -> lte= 현재시점이후
    #Post.objects.filter(author=me)  -> auther가 me인것들을 전부가져옴 (get은한개이상이면오류지만 이건다가져옴)
    # post = Post.objects.get(title="Sample title") 
    #Post.objects.filter(title__contains = '글')  --> 글이라는단어가포함된 모든글을찾음
    #  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #  ㄴ   발행시간이 지금이전인것들을  발행시간순으로 모두뽑아옴