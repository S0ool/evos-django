from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DeleteView, UpdateView

from app.forms import CategoryForm, DishForm
from app.models import Category, Dish, Basket


@method_decorator(login_required(login_url='login'), name='dispatch')
class Home(View):
    def get(self, request):
        dishes = Dish.objects.all()
        ctx = {
            'categories': Category.objects.all(),
            'dishes':dishes,

        }
        return render(request, 'app/menu.html', ctx)

@method_decorator(login_required(login_url='login'), name='dispatch')
class CatHome(View):
    def get(self, request,pk):
        category = Category.objects.get(id=pk)
        dishes = Dish.objects.filter(category=category)
        ctx = {
            'categories': Category.objects.all(),
            'dishes':dishes,

        }
        return render(request, 'app/menu.html', ctx)



@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoryDetail(View):
    def get(self, request, pk):
        ctx = {
            'dishes': Dish.objects.filter(category_id=pk),
        }
        return render(request, 'app/category_detail.html', ctx)


# Create your views here.
class Redir(View):
    def get(self, request):
        if request.user.is_staff:
            return redirect('staff')
        return redirect('menu')


@method_decorator(login_required(login_url='login'), name='dispatch')
class StaffView(View):
    def get(self, request):
        return render(request, 'app/staff/staff.html')

@method_decorator(login_required(login_url='login'), name='dispatch')
class UsersView(View):
    def get(self, request):
        users_orders = []
        for user in Basket.objects.all().values_list('client', flat=True).distinct():
            users_orders.append(Basket.objects.filter(client=user))
        clients = User.objects.filter(baskets__isnull=False).distinct()
        ctx = {
            'clients': clients,
            'users_orders': users_orders,
        }
        return render(request, 'app/staff/users.html',context=ctx)

@method_decorator(login_required(login_url='login'), name='dispatch')
class DishView(View):
    def get(self, request):

        ctx = {
            'dishes': Dish.objects.all(),
            'form': DishForm(),
        }
        return render(request, 'app/dishes_staff/dishes.html', ctx)

    def post(self, request):
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('dishes')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DishDelete(DeleteView):
    model = Dish
    template_name = 'app/dishes_staff/delete_dish.html'
    success_url = reverse_lazy('dishes')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DishEdit(UpdateView):
    model = Dish
    template_name = 'app/dishes_staff/edit_dish.html'
    success_url = reverse_lazy('dishes')
    form_class = DishForm


@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoryView(View):
    def get(self, request):
        ctx = {
            'categories': Category.objects.all(),
            'form': CategoryForm(),
        }
        return render(request, 'app/category_staff/categories.html', ctx)

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('categories')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoryDelete(DeleteView):
    model = Category
    template_name = 'app/category_staff/delete_category.html'
    success_url = reverse_lazy('categories')


@method_decorator(login_required(login_url='login'), name='dispatch')
class CategoryEdit(UpdateView):
    model = Category
    template_name = 'app/category_staff/edit_category.html'
    success_url = reverse_lazy('categories')
    form_class = CategoryForm


@method_decorator(login_required(login_url='login'), name='dispatch')
class AddDishToBasket(View):
    def get(self, request, pk):
        dish = Dish.objects.get(id=pk)
        if Basket.objects.filter(client=request.user, dish=dish).exists():
            basket = Basket.objects.get(client=request.user, dish=dish)
            basket.quantity += 1
            basket.save()
        else:
            basket = Basket(
                client=request.user,
                dish=dish,
                quantity=1
            )
            basket.save()
        return redirect('menu')

@method_decorator(login_required(login_url='login'), name='dispatch')
class AddDishInBasket(View):
    def get(self, request, pk):
        basket = Basket.objects.get(id=pk)
        basket.quantity += 1
        basket.save()
        return redirect('basket')


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteOneDishToBasket(View):
    def get(self, request, pk):
        basket = Basket.objects.get(id=pk)
        if basket.quantity > 1:
            basket.quantity -= 1
            basket.save()
        else:
            basket.delete()
        return redirect('basket')

@method_decorator(login_required(login_url='login'), name='dispatch')
class BasketView(View):
    def get(self, request):
        ctx = {
            'baskets': Basket.objects.filter(client=request.user),
        }
        return render(request, 'app/basket.html', ctx)
@method_decorator(login_required(login_url='login'), name='dispatch')

class BasketDelete(DeleteView):
    model = Basket
    template_name = 'app/basket.html'
    success_url = reverse_lazy('basket')

