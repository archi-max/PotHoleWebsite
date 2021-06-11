from django.db import models
from gdstorage.storage import GoogleDriveStorage
from django.core.files.storage import FileSystemStorage

import os
from uuid import uuid4
from django import forms

USE_GDRIVE =  False
if USE_GDRIVE:
    storage_backend = GoogleDriveStorage()
else:
    storage_backend = FileSystemStorage()

# def path_and_rename(path):
def path_to_file(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join('potholetracker/', filename)

# Create your models here.
class Data(models.Model):
    image = models.ImageField(upload_to=path_to_file, storage=storage_backend)
    username = models.CharField(max_length=128)

    def __str__(self):
        return self.username+"__" + str(self.image)

class UploadForm(forms.Form):
    username = forms.CharField(max_length=128, required=False)
