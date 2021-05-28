from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import UserMessageForm, CreateCategory, CreateEvent
from django.shortcuts import render, redirect
from .models import Category, Dish, Event, Banners
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def main(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    banners = Banners.objects.filter(is_visible=True)

    special_categories = Category.objects.filter(is_visible=True).filter(
        is_special=True).order_by('category_order')
    for item in special_categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    categories = Category.objects.filter(is_visible=True).filter(
        is_special=False).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)

    events = Event.objects.all()

<<<<<<< Updated upstream
    special_dish = Dish.objects.filter(is_special=True)

=======
>>>>>>> Stashed changes
    reservation_form = UserMessageForm()

    return render(request, 'index.html', context={'categories': categories,
                                                  'special_categories': special_categories,
                                                  'events': events,
                                                  'banners': banners,
<<<<<<< Updated upstream
                                                  'special_dish': special_dish,
=======
>>>>>>> Stashed changes
                                                  'form': reservation_form, })


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
# Вывести все категории на страничку show-all-categories.html
def show_category(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
<<<<<<< Updated upstream
    return render(request, 'administrations/show-all-categories.html', context)
=======
    return render(request, 'show-all-categories.html', context)
>>>>>>> Stashed changes


# Вывести на страничке category-info.html данные про выбранный элемент
class CategoryDetailView(DetailView):
    model = Category
<<<<<<< Updated upstream
    template_name = 'administrations/category-info.html'
=======
    template_name = 'category-info.html'
>>>>>>> Stashed changes
    context_object_name = 'category'


# Вывести форму для редактирования элемента
class CategoryUpdateView(UpdateView):
    model = Category
<<<<<<< Updated upstream
    template_name = 'administrations/create-new-category.html'
=======
    template_name = 'create-new-category.html'
>>>>>>> Stashed changes
    form_class = CreateCategory


# Вывести страничку для удаления категории
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/categories/'
<<<<<<< Updated upstream
    template_name = 'administrations/category-delete.html'
=======
    template_name = 'category-delete.html'
>>>>>>> Stashed changes


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
def create_new_category(request):
    error = ''
    if request.method == 'POST':
        form = CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/categories/")
        else:
            error = 'Форма была не верной!'

    form = CreateCategory()
    context = {
        'form': form,
        'error': error,
    }
<<<<<<< Updated upstream
    return render(request, 'administrations/create-new-category.html', context)
=======
    return render(request, 'create-new-category.html', context)
>>>>>>> Stashed changes


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
def create_new_event(response):
    error = ''
    if response.method == 'POST':
        form = CreateEvent(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("/events/")
        else:
            error = 'Форма была не верной!'

    form = CreateEvent()
    context = {
        'form': form,
        'error': error,
    }
    return render(response, 'events/create-new-event.html', context)


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
def show_events(response):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(response, 'events/show-all-events.html', context)


class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event-info.html'
    context_object_name = 'event'


class EventUpdateView(UpdateView):
    model = Event
    template_name = 'events/create-new-event.html'
    form_class = CreateEvent


class EventDeleteView(DeleteView):
    model = Event
    success_url = '/events/'
    template_name = 'events/event-delete.html'
