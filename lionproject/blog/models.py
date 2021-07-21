from django.db import models

#table의 형식 만들기
class Blog(models.Model): 
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    #upload_to 속성은 업로드할 폴더를 지정 하는 것이다

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #100인덱스까지 슬라이싱