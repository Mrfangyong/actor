from django.db import models

# Create your models here.
class Actor(models.Model):
    gender=(
        ("male","男"),
        ("famale","女"),
        )
    actor_name=models.CharField(max_length=20,blank=True,verbose_name="艺人名字")
    actor_occupation=models.CharField(max_length=255,verbose_name="艺人职业")
    actor_sex=models.CharField(max_length=32,choices=gender,default="男")
    actor_site=models.CharField(max_length=255,verbose_name="艺人地址")
    actor_email=models.EmailField(unique=True,verbose_name="艺人邮箱")
    actor_brief_introduction=models.CharField(max_length=255,verbose_name="个人简介") 
    actor_personal_experience=models.CharField(max_length=255,verbose_name="个人经历")
    actor_Media_evaluation=models.CharField(max_length=255,verbose_name="媒体经历")
    actor_Sense_of_character_score=models.IntegerField(verbose_name="人物形象感")
    actor_Language_rhythm_score=models.IntegerField(verbose_name="语言节奏的把握")
    actor_Local_details_score=models.IntegerField(verbose_name="局部细节戏的张力")
    actor_internal_monologue_score=models.IntegerField(verbose_name="内心戏的剖析") 
    actor_Number_of_type_works=models.CharField(max_length=255,verbose_name="类型作品数量")
    def __str__(self):
        return self.actor_name           
class Img(models.Model):
    name=models.CharField(max_length=20)
    address=models.ImageField(upload_to="img")
    img_actor=models.ForeignKey(Actor,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name

class Video(models.Model):
    name=models.CharField(max_length=20)
    address=models.FileField(upload_to="videos/", null=True, blank=True, verbose_name="视频内容")
    video_actor=models.ForeignKey(Actor,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name
 
    
class News(models.Model):
    headline=models.CharField(max_length=20)
    link=models.URLField()
    news_actor=models.ForeignKey(Actor,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.headline  
class Background_img(models.Model):
    name=models.CharField(max_length=50)
    address=models.ImageField(upload_to="img")
    Background_actor=models.ForeignKey(Actor,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.name