from django.db import models

# Create your models here.

class Student(models.Model):
    SEX_ITEM = [
        (1, "男"),
        (2, '女'),
        (0, '未知')
    ]
    STATUS_ITEMS = [
        (1, "通过"),
        (2, '拒绝'),
        (0, '申请')
    ]
    id = models.AutoField(primary_key=True)  # 设置为主键
    name = models.CharField(max_length=128, verbose_name="姓名")
    sex = models.IntegerField(choices=SEX_ITEM, verbose_name="性别")
    profession = models.CharField(max_length=128, verbose_name="职业")
    email = models.EmailField(verbose_name="Email")
    qq = models.CharField(max_length=128, verbose_name="QQ")
    phone = models.CharField(max_length=128, verbose_name="电话")
    status = models.IntegerField(choices=STATUS_ITEMS, verbose_name="审核状态")
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="创建时间")

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def __str__(self):
        return '<Student: {}'.format(self.name)

    class Meta:
        verbose_name = verbose_name_plural = "学员信息"