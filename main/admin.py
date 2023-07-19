from django.contrib import admin
# from .forms import Addblog
from .models import Post,Profile
# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
