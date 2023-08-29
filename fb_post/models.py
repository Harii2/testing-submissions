from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = models.URLField()


class Post(models.Model):
    content = models.TextField(max_length=1000)
    posted_at = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=1000)
    commented_at = models.DateField(auto_now_add=True)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)


class Reaction(models.Model):
    REACTION_CHOICES = [
        ('WOW', 'Wow'),
        ('LIT', 'Lit'),
        ('LOVE', 'Love'),
        ('HAHA', 'Haha'),
        ('THUMBS-UP', 'Thumbs Up'),
        ('THUMBS-DOWN', 'Thumbs Down'),
        ('ANGRY', 'Angry'),
        ('SAD', 'Sad'),
    ]
    reaction = models.CharField(max_length=100, choices=REACTION_CHOICES)
    reacted_at = models.DateTimeField(auto_now_add=True)
    reacted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)


