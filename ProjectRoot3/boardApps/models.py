from django.db import models
import os 
from django.conf import settings 
from datetime import datetime

#게시판 작성을 위한 Post테이블 생성
class Post(models.Model):
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    name1 = models.CharField(default="kosmo", max_length=20)
    pub_date = models.DateTimeField('date published', default=datetime.now())
    view_count = models.IntegerField(default=0)
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.titles
    
    # delete() 함수 오버라이딩 
    def delete(self, *args, **kargs):
        if self.mainphoto:
            print("이미지삭제")
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            # 여기서 이미지 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        super(Post,self).delete(*args,**kargs)

