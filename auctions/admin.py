from django.contrib import admin

from .models import itemDetails,bidDetails,comments,watchlist
from .models import User
# Register your models here.

admin.site.register(itemDetails)
admin.site.register(User)
admin.site.register(bidDetails)
admin.site.register(comments)
admin.site.register(watchlist)