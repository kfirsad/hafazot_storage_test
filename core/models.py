from django.db import models
from django.utils.text import slugify 
import time
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    copy_link = models.CharField(editable=False, max_length=500, default='not created')
    slug = models.SlugField(unique=True, editable=False)
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    publish_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(time.time())
        self.copy_link = settings.PASTE_WEBSITE_URL + '/' + str(self.slug)
        super(Item, self).save(*args, **kwargs)

    def get_file(self):
        if self.file:
            print('here: ' + self.file.url)
            return settings.PASTE_WEBSITE_URL + self.file.url
        return ''

