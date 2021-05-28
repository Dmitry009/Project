from django.contrib import admin
<<<<<<< Updated upstream
from .models import Category, Dish, Event, Banners, UserMessages
=======
from .models import Category, Dish, Banners, Event, UserMessages
>>>>>>> Stashed changes

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Banners)
admin.site.register(UserMessages)
