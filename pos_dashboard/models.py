from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Category_image')

    class Meta:
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        
        return self.category_name

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    discription = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='media/Brand_image')

    class Meta:
        
        verbose_name = 'Brand'
        verbose_name_plural = 'Brand'

    def __str__(self):
        
        return self.name

class Product (models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 100,blank=True, null=True,unique=True)  
    categoris = models.ForeignKey(Category, verbose_name='Product Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='ProductImg',default='ProductImg/noimg.jpg')
    hover_image = models.ImageField(upload_to='ProductImg',default='noimg.jpg', blank=True, null=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    product_purchase_price = models.IntegerField()
    sort_discription = models.TextField(blank=True, null=True)
    discription = models.TextField()
    aditional_discription = models.TextField(blank=True, null=True)
    stock_quantity = models.PositiveIntegerField()
    show_status  = models.BooleanField(default=False)
    flash_sale_add_and_expire_date = models.DateTimeField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True, null=True)
    meta_title = models.CharField(blank=True, null=True,max_length=100)
    meta_keyword = models.CharField(blank=True, null=True,max_length=100)
    
    
    def saving_price(self):
        return self.price  - self.discount_price

    def saving_percent(self):
        return self.saving_price() / self.price  * 100
        
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['-id']
    




class Supplier(models.Model):
    name = models.CharField(max_length=100)
    supplier_type = models.CharField(max_length=100)
    supplier_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    amount = models.FloatField(max_length=30)
    guarantor_name = models.CharField(max_length=100)
    guarantor_phone = models.IntegerField()
    Chassis_no = models.CharField(max_length=30)
    Transport_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to ='media/supplier_image')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    class Meta:
   
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
    def __str__(self):

        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    customer_ID = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    start_date = models.DateField(max_length=50)
    image = models.ImageField(upload_to ='media/supplier_image')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    class Meta:
   
        verbose_name = 'Customer'
        verbose_name_plural = 'Customer'
    def __str__(self):

        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

    def __str__(self):
        
        return self.name


class Purchase_Product(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    billing_date = models.DateField()
    product_name = models.CharField(max_length=100, blank=True, null=True)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    buy_price = models.FloatField()
    sale_price = models.FloatField()
    whole_sale_price = models.FloatField()
    total_price = models.FloatField()
    total_descount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField()
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    image = models.ImageField(upload_to='media/')
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    unit = models.ForeignKey("pos_dashboard.Unit", related_name="unit", blank=True, null=True, on_delete=models.CASCADE)
    supplier_name = models.ForeignKey(Supplier, related_name="purchase_Product", blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey("pos_dashboard.Category", related_name="category", blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey("pos_dashboard.Brand", related_name="brand", blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        
        verbose_name = 'Purchase_Product'
        verbose_name_plural = 'Purchase_Products'

    def __str__(self):
            
        return self.product_name

class Sales_Product(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    billing_date = models.DateField()
    product_code = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    unit_price = models.FloatField()
    sale_price = models.FloatField()
    total_price = models.FloatField()
    total_descount = models.FloatField(blank=True, null=True)
    sub_total = models.FloatField()
    paid = models.FloatField()
    due = models.FloatField(blank=True, null=True)
    Created_at = models.DateTimeField(max_length=100, blank=True, null=True)
    Updated_at = models.DateTimeField(max_length=100, blank=True, null=True)

    sale_product_name = models.ForeignKey(Purchase_Product, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, null=True, on_delete=models.CASCADE)
    customer_name = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Sales_Product'
        verbose_name_plural = 'Sales_Products'

    def __str__(self):
        return self.sale_product_name.product_name

    def save(self, *args, **kwargs):
        if self.sale_product_name:
            self.product_code = self.sale_product_name.product_code
            self.unit_price = self.sale_product_name.unit_price
        super().save(*args, **kwargs)


class return_purchase(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)

    # TODO: Define fields here

    class Meta:

        verbose_name = 'return_purchase'
        verbose_name_plural = 'return_purchases'

    def __str__(self):
        return self.name
    
# class Quotation(models.Model):
#     biller = models.CharField(max_length=50)
#     supplier = models.CharField(max_length=50)
#     customer = models.CharField(max_length=50)
#     warehouse = models.CharField(max_length=50)
#     note = models.CharField(max_length=50)
#     order_tax = models.CharField(max_length=50)
#     order_discount = models.IntegerField()
#     shipping_cost = models.IntegerField()
#     status = models.IntegerField()
#     class Meta:
#         verbose_name = 'Quotation'
#         verbose_name_plural = 'Quotations'

#     def __str__(self):
#         pass
     
    
    


class Purchase(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    status = models.IntegerField()
    payment_status = models.IntegerField()
    total_quantity = models.IntegerField()
    total = models.FloatField()
    discount= models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    grand_total = models.FloatField()
    
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    supplier = models.ForeignKey(Supplier,  blank=True, null=True, on_delete=models.CASCADE)
 

    def __str__(self):
            
        return self.product_name
    
    
class Purchase_order_product(models.Model):
    sub_total = models.FloatField()
    quantity = models.IntegerField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    
    



class Sale(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    date = models.DateField()

    status = models.IntegerField()
    payment_status = models.IntegerField()
    total_quantity = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    discount= models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    grand_total = models.FloatField()
    
    paid = models.FloatField()
    due = models.FloatField( blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    customer = models.ForeignKey(Customer,  blank=True, null=True, on_delete=models.CASCADE)


    def __str__(self):
            
        return self.product_name
    
class Sale_order_product(models.Model):
    sub_total = models.FloatField()
    quantity = models.IntegerField()
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    