from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

STATE_CHOICE=(
    ('maharastra','maharastra'),
    ('mp','mp'),
    ('goa','goa'),
)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    address_2=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(choices=STATE_CHOICE,max_length=100)
    pin_code=models.IntegerField()

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('m','mobile'),
    ('ele','electronic')
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discripition=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    product_img=models.ImageField(upload_to='product_img')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)



    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
#-------------------


STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('packed','packed'),
    ('delivered','delivered'),
)

class Orderplace(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='pending')

    def __str__(self):
        return str(self.id)

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=CASCADE)
    email=models.EmailField(max_length=30)
    feedback=models.CharField(max_length=200)
