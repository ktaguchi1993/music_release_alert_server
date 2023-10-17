from django.db import models

class NewRelease(models.Model):
    class Meta:
        db_table = "new_release"
        verbose_name = verbose_name_plural = "リリース情報"

    title = models.CharField(verbose_name="タイトル", max_length=300)
    artist = models.CharField(verbose_name="アーティスト", max_length=100)
    release_date = models.DateField(verbose_name="リリース日")
    url = models.URLField(verbose_name="リンク")
    type = models.CharField(verbose_name="タイプ", max_length=100)  # 後にIntegerFieldに変更
    genre = models.CharField(verbose_name="ジャンル", max_length=100)  # 後にForeignKeyに変更
