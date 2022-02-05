from django.db import models

# Create your models here.


class lunch_go(models.Model):
    title = models.CharField('팀이름', max_length=200)
    description = models.TextField('내용')
    type = models.CharField('점심종류', max_length=100)
    image = models.ImageField('식당 이미지', blank=True, null=True, upload_to='project')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# https://zodlab.tistory.com/111?category=699316  << 여기 하던 중