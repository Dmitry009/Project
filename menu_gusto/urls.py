from django.urls import path
from .views import *


urlpatterns = [
<<<<<<< Updated upstream
    path('<category>', category),
    #path('<category>/<dish>', dish),
=======
>>>>>>> Stashed changes
    path('dishes/', show_dishes, name='dishes'),
    path('dishes/<int:pk>', DishDetailView.as_view(), name='dish-details'),
    path('dishes/<int:pk>/update', DishUpdateView.as_view(), name='dish-update'),
    path('dishes/<int:pk>/delete', DishDeleteView.as_view(), name='dish-delete'),
    path('dishes/create-new-dish/', create_new_dish),
]
