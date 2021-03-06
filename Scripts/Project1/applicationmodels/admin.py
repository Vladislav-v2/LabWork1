from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Example)
#admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Place)
admin.site.register(models.Restaurant)
admin.site.register(models.Waiter)
admin.site.register(models.Publication)
admin.site.register(models.Article)

class AuthorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Author._meta.fields]
    fields = ["name",'surname', 'date_birth']
    list_filter = ['name']
    search_fields = [field.name for field in models.Author._meta.fields]
    class Meta:
        model = models.Author
admin.site.register(models.Author, AuthorAdmin)