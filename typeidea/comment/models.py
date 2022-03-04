from django.db import models
from blog.models import Post
# Create your models here.

class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = [
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    ]
    nickname = models.CharField(max_length=255, verbose_name="标题")
    email = models.EmailField(verbose_name="邮箱")
    website = models.URLField(verbose_name="链接")
    content = models.CharField(max_length=500, verbose_name="内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    post = models.ForeignKey(Post, verbose_name="作者", on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS,
                                         verbose_name="状态")

    class Meta:
        verbose_name = verbose_name_plural = '评论'