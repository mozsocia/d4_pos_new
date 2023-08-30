from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

from django.contrib import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect

from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView

from django.http import JsonResponse

from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()
# @login_required
def index(request):
    return render(request, 'pos_dashboard/index.html')


#User

@login_required
# @daseboard_required
def user_list(request):
    user=User.objects.all()
    context={
        'user':user
    }
    return render(request, 'pos_dashboard/user/userlist.html', context)


@login_required
# @daseboard_required
def user_add(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add')
            return redirect('user_list')
    else:
        form =RegisterForm()
    return render(request,'pos_dashboard/user/adduser.html',{'form':form})


@login_required
# @daseboard_required
def user_update(request,pk):
    user =get_object_or_404(User,pk=pk)
    form =UserForm(request.POST,instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully update')
            return redirect('user_list')
    else:
        form =UserForm(instance=user)
    context={
        'form':form,
    }
    return render(request, 'pos_dashboard/user/user-add.html',context)


@login_required
# @daseboard_required
# def user_delete(request, pk):
#     user = User.objects.get(pk=pk)
#     if request.method == 'POST':
#         user.delete()
#         messages.success(request, 'Successfully delete')
#         return redirect('user_list')
#     return render (request, 'dashboard/user/user-delete.html',{'user':user})


# Product
def productlist(request):
    products = Product.objects.all()

    context={
        'products':products
    }
    return render(request, 'pos_dashboard/product_list.html', context)


class ProductInline():
    form_class = ProductForm
    model = Product
    template_name = "pos_dashboard/add_product.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('dashboard-product-list')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.item = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving. Useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.product = self.object
            image.save()


class ProductCreate(ProductInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

class ProductUpdate(ProductInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx




# Supplier
def supplier_add(request):
    if request.method == 'POST':

        form=SupplierAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new Purchas Product')
            return redirect('supplierlist')
    else:
        form = SupplierAddForm()
        context = {
            'form':form
        }
    return render(request, 'pos_dashboard/supplier/add_supplier.html', context)


def supplier_list(request):
    supplier_list = Supplier.objects.all()
    context ={
        'supplier_list':supplier_list
    }
    return render(request, 'pos_dashboard/supplier/supplier_list.html', context)


# Category

def category_add(request):
    categorys = Category.objects.all()
    if request.method == 'POST':
        form=CategoryAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new category')
            return redirect('category_list')
    else:
        form = CategoryAddForm()

    context = {
        'categorys': categorys,
        'form':form 
    }
    return render(request,'pos_dashboard/category/category_add.html',context)


def category_list(request):
    category_list = Category.objects.all()
    context ={
        'category_list':category_list
    }
    return render(request, 'pos_dashboard/category/category_list.html', context)

# Brand

def brand_add(request):
    if request.method == 'POST':
        form=BrandAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new brand')
            return redirect('brand_list')
    else:
        form =BrandAddForm()
    context= {
        'form':form,
        
    }
    return render(request,'pos_dashboard/brand/brand_add.html',context)

def brand_list(request):
    brand_list = Brand.objects.all()
    context={
        'brand_list':brand_list
    }
    return render(request,'pos_dashboard/brand/brand_list.html', context)

# Unit 
def unit_add(request):
    unit_list = Unit.objects.all()

    if request.method == 'POST':
        form=UnitAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new Unit')
            return redirect('unit_add')
    else:
        form =UnitAddForm()

    context={
        'unit_list':unit_list,
        'form':form,
    }
    return render(request,'pos_dashboard/unit/unit_add.html',context)

     
# Purchage
def purchase_product(request):
    unit = Unit.objects.all()
    supplier = Supplier.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()

    if request.method == 'POST':

        form=Purchase_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request,'successfully add your new Purchas Product')
            return redirect('purchase_list')
    else: 
        form = Purchase_Product_Form()
    
    context = {
        'form':form,
        'category':category,
        'unit':unit,
        'supplier':supplier,
        'brand':brand,

    }
    return render(request, 'pos_dashboard/purchase_product/add_purchase.html',context)
 

def purchase_product_list(request):
    purchase_list = Purchase_Product.objects.all()
    context ={
        'purchase_list':purchase_list
    }
    return render(request, 'pos_dashboard/purchase_product/purchase_list.html', context)


def new_purchase_return(request):
    return render(request, 'pos_dashboard/purchase_product/create_purchase_return.html')


def purchase_due_list(request):

    due_purchase_list = Purchase_Product.objects.filter(due__gt=0)
    context ={
        'due_purchase_list':due_purchase_list
    }
    return render(request, 'pos_dashboard/purchase_product/due_purchase_list.html', context)


from django.http import JsonResponse

def sales_product(request):

    sale_product_name = Purchase_Product.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    customer = Customer.objects.all()
    unit = Unit.objects.all()

    if request.method == 'POST':
        form = Sales_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added your new Sales Product')
            return redirect('sales_list')
    else:
        form = Sales_Product_Form()
    
    context = {
        'form': form,
        'sale_product_name': sale_product_name,
        'category': category,
        'brand':brand,
        'customer':customer,
        'unit':unit
    }
    
    return render(request, 'pos_dashboard/sales/add_sales.html', context)



def sales_list(request):
    sales_li = Sales_Product.objects.all()

    context = {
        'sales_li':sales_li
    }
    return render(request, 'pos_dashboard/sales/sales_list.html', context)


def sales_due_list(request):

    due_sales_list = Sales_Product.objects.filter(due__gt=0)
    context ={
        'due_sales_list':due_sales_list
    }
    return render(request, 'pos_dashboard/sales/due_sales_list.html', context)


# customer
def add_customer(request):
    if request.method == 'POST':

        form=CustomersAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'successfully add your new customer')
            return redirect('customers_list')
    else:
        form = CustomersAddForm()
        context = {
            'form':form
        }
    return render(request, 'pos_dashboard/customers/add_customers.html', context)


def customers_list(request):
    customer_list = Customer.objects.all()
    context ={
        'customer_list':customer_list
    }
    return render(request, 'pos_dashboard/customers/customers_list.html', context)


def add_quotation(request):
    return render(request, 'pos_dashboard/quotation/add_quotation.html')

def quotation_list(request):
    return render(request, 'pos_dashboard/quotation/quotation_list.html')


def purchase_return_list(request):
    return render(request, 'pos_dashboard/purchase_return/p_return_list.html')

def add_purchase_return(request):
    return render(request, 'pos_dashboard/purchase_return/p_return_add.html')

def add_sales_return(request):
    return render(request, 'pos_dashboard/sales_return/s_return_add.html')

def sales_return_list(request):
    return render(request, 'pos_dashboard/sales_return/s_return_list.html')