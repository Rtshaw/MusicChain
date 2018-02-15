from django.contrib import admin
from myblock import models

# Register your models here.
class TransactionInline(admin.StackedInline):
    model = models.Transaction
    extra = 1

class TransactionblockAdmin( admin.ModelAdmin):
    inlines = [
        TransactionInline
    ]

admin.site.register(models.Music)
admin.site.register(models.Transaction)
admin.site.register(models.Musicblock)
admin.site.register(models.Transactionblock, TransactionblockAdmin)