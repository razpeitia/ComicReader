from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class TimestampsModel(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Comic(TimestampsModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    cover = models.ImageField(blank=True, null=True, upload_to='cover')
    slug = models.SlugField(unique=True)
    publisher = models.CharField(max_length=100)
    release_date = models.DateField()


class Issue(TimestampsModel):
    comic = models.ForeignKey('Comic')
    number = models.IntegerField()
    title = models.CharField(max_length=200)

    class Meta:
        unique_together = ('comic', 'number')


class Page(TimestampsModel):
    issue = models.ForeignKey('Issue')
    page_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to=lambda instance, filename: "%s/%s/%s.jpg" % (instance.issue.comic.slug, instance.issue.number, instance.page_number))

    def before(self):
        page_number = max(1, self.page_number-1)
        kwargs = {"slug": self.issue.comic.slug, 'issue': self.issue.number, 'number': page_number}
        return reverse("reader:page", kwargs=kwargs)

    def next(self):
        count = self.issue.page_set.all().count()
        page_number = min(count, self.page_number+1)
        kwargs = {"slug": self.issue.comic.slug, 'issue': self.issue.number, 'number': page_number}
        return reverse("reader:page", kwargs=kwargs)

    class Meta:
        unique_together = ('issue', 'page_number')


class Comment(TimestampsModel):
    page = models.ForeignKey('Issue')
    user = models.ForeignKey(User)
    text = models.TextField()


class CommentVote(TimestampsModel):
    voter = models.ForeignKey(User)
    comment = models.ForeignKey('Comment')

    class Meta:
        unique_together = ('voter', 'comment')
