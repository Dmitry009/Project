from django.shortcuts import render, redirect
from main_gusto.models import Dish, Category
from main_gusto.forms import CreateDish
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def category(request, category):
    try:
        dishes = Dish.objects.filter(category=category)
        return render(request, 'dish.html', context={'category': dishes})
    except Dish.DoesNotExist:
        return HttpResponseNotFound("Page not found")


def dish(request, category, dish):
    dish = Dish.objects.get(pk=dish)
    return render(request, "dish_info.html", context={'dish': dish, 'category_id': category})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
# Вывести все категории на страничку show-all-categories.html
def show_dishes(request):
    dishes = Dish.objects.all()
    context = {
        'dishes': dishes
    }
<<<<<<< Updated upstream
    return render(request, 'administrations/show-all-dishes.html', context)
=======
    return render(request, 'show-all-dishes.html', context)
>>>>>>> Stashed changes


class DishDetailView(DetailView):
    model = Dish
<<<<<<< Updated upstream
    template_name = 'administrations/dish-info.html'
=======
    template_name = 'dish-info.html'
>>>>>>> Stashed changes
    context_object_name = 'dish'


# Вывести форму для редактирования элемента
class DishUpdateView(UpdateView):
    model = Dish
<<<<<<< Updated upstream
    template_name = 'administrations/create-new-dish.html'
=======
    template_name = 'create-new-dish.html'
>>>>>>> Stashed changes
    form_class = CreateDish


# Вывести страничку для удаления категории
class DishDeleteView(DeleteView):
    model = Dish
    success_url = '/menu/dishes/'
<<<<<<< Updated upstream
    template_name = 'administrations/dish-delete.html'
=======
    template_name = 'dish-delete.html'
>>>>>>> Stashed changes


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
def create_new_dish(response):
    error = ''
    if response.method == 'POST':
        form = CreateDish(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("/menu/dishes/")
        else:
            error = 'Форма была не верной!'

    form = CreateDish()
    context = {
        'form': form,
        'error': error,
    }
<<<<<<< Updated upstream
    return render(response, 'administrations/create-new-dish.html', context)
=======
    return render(response, 'create-new-dish.html', context)
>>>>>>> Stashed changes
