from django.db import models

# Create your models here.
class product(models.Model):
    id= models.CharField(max_length=20,primary_key=True, serialize=False, verbose_name='Product ID')
    product_name = models.CharField(max_length=120)
    product_price = models.IntegerField()
    before_discount_price = models.FloatField()
    product_description = models.TextField()
    product_pic = models.ImageField(upload_to="product-images/")

    def __str__(self):
        return self.product_name