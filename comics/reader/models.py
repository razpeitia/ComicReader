from django.db import models


class TimestampsModel(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ComicBook(TimestampsModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    pages = models.PositiveIntegerField()
    release_date = models.DateField()
    alternative_names = models.ForeingKey()


class AlternativeNames(TimestampsModel):
    comic = models.ForeignKey('ComicBook')
    name = models.CharField(max_length=150)

    class Meta:
        unique_together = ('comic', 'name')

class ComicPage(TimestampsModel):
    comic = models.ForeignKey('ComicBook')
    page_number = models.PositiveIntegerField()
    image = models.ImageField()
    description = models.TextField()

    class Meta:
        unique_together = ('comic', 'page_number')


class Comment(TimestampsModel):
    page = models.ForeignKey('ComicPage')
    user = models.ForeignKey('User')
    text = models.Text()


class CommentVote(TimestampsModel):
    voter = models.ForeignKey('User')
    comment = models.ForeignKey('Comment')

    class Meta:
        unique_together = ('voter', 'comment')
