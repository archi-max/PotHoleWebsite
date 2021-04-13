from django.db import models
from gdstorage.storage import GoogleDriveStorage
import os
from uuid import uuid4

gd_storage = GoogleDriveStorage()

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
    image = models.ImageField(upload_to=path_to_file, storage=gd_storage)
    username = models.CharField(max_length=128)