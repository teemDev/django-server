from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class HomePageModel(models.Model):
    banner = models.ImageField(upload_to='banner')
    title = models.CharField(max_length=255)
    mybio = models.CharField(max_length=255)
    mycvfile = models.FileField(upload_to='cvfile')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'home'
        verbose_name_plural = 'home'

class AboutPageModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'about'

class CardPageModel(models.Model):
    numbers = models.CharField(max_length=55)
    title = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'


class SkillPageModel(models.Model):
    title = models.CharField(max_length=55)
    knowledge = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'


class PortfolioPageModel(models.Model):
    image = models.ImageField(upload_to='portofolioimg')
    githublink = RichTextUploadingField()
    youtubelink = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'portfolio'
        verbose_name_plural = 'portfolio'


class BlogPageModel(models.Model):
    image = models.ImageField(upload_to='blogimg')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blog'


class ContactPageModel(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=155)
    mylocation = models.CharField(max_length=55)
    myemail = models.EmailField()
    myedu = models.CharField(max_length=55)
    mynumber = models.PositiveSmallIntegerField()
    langugages = models.CharField(max_length=155)
    mygithub = RichTextUploadingField()
    myyoutube = RichTextUploadingField()
    mytelegram = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'