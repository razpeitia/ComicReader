import json
import zipfile

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.db import transaction

from reader.models import Comic
from reader.models import Issue
from reader.models import Page


class Command(BaseCommand):
    args = '<comic_info>'
    help = 'Import comic from cbr/cbz file'

    def handle(self, *args, **options):
        comic_info = args[0]
        with open(comic_info, 'rb') as f:
            data = json.load(f)

        with transaction.atomic():
            comic = Comic(**data['comic'])
            comic.save()

            issue = Issue(comic=comic, **data['issue'])
            issue.save()

            comic_file = data['comic_file']
            with zipfile.ZipFile(comic_file, "r") as f:
                for number, name in enumerate(f.namelist(), start=1):
                    data = f.read(name)
                    page = Page(issue=issue, page_number=number)
                    content = ContentFile(data)
                    page.image.save(name, content, save=False)
                    page.save()