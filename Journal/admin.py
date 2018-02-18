from .models import Question
from .models import Choice
from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Register your models here.
#admin.site.register(Question)