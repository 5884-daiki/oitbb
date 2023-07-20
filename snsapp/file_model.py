from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='files/')
    # 他のフィールドや関連フィールドを追加する場合はここに記述します

    def __str__(self):
        return self.file.name
