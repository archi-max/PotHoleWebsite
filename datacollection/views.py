from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.
from .models import UploadForm
from django.views.decorators.csrf import csrf_exempt

from django.urls import reverse
from .models import Data



class IndexView(TemplateView):

    template_name = "index.html"


class UploadFormView(FormView):

    form_class = UploadForm
    template_name = "upload.html"
    success_url = '/upload'

    def post(self, request, *args, **kwargs):
        print("post callled on upload")
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('images')
        print("files", files)
        if form.is_valid():
            username = form.cleaned_data['username']
            for f in files:
                d = Data(username=username, image=f)
                d.save()
                print("File Uploaded:", d)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

