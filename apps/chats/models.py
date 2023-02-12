from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    content = models.TextField(verbose_name='请求参数', null=False, default=0)
    times = models.IntegerField(verbose_name='次数', null=False, default=0)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '用户请求列表'
        ordering = ['-id']

    def __str__(self):
        return f'{self.id}-{self.user.first_name}'

    def to_json(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))