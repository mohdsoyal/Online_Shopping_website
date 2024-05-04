from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator 

# Create your models here.
State_choice = (
    ('UP', 'Utter Pradesh'),
    ('MP', 'Madhya Pradesh'),
    ('GA', 'Goa'),
    ('MH', 'Mumbai'),
    ('DL', 'Delhi'),
    ('WB', 'Kolkata'),
    ('JH', 'Jharkhand'),
    ('BR', 'Bihar'),
    ('AS', 'Assam'),
    ('JK', 'Jammu Kashmir'),
)

class Custumer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=State_choice, max_length=2)

    def __str__(self):
        return str(self.id)


    
    def __str__(self):
        return str(self.id)
    
    
Category_Choice =(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)    
    
class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    discription=models.TextField(default='null')
    brand=models.CharField(max_length=200)
    category=models.CharField(choices=Category_Choice ,max_length=200)
    img=models.ImageField(upload_to='static')
  
    
    
    def __str__(self):
        return str(self.id)
        


class Cart(models.Model):
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return str(self.id)
    
    
    @property
    def total(self):
        return self.quantity * self.product.selling_price
    
    
Status_Choice = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class Orderplaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Custumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=Status_Choice, default='Pending')

    def __str__(self):
        return str(self.id)
    
    
    @property
    def total(self):
        return self.quantity * self.product.selling_price

           
