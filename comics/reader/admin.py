from django.contrib import admin
from .models import Comic
from .models import Issue
from .models import Page
from .models import Comment


admin.site.register(Comic)
admin.site.register(Issue)
admin.site.register(Page)
admin.site.register(Comment)