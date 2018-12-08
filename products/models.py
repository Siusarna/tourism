from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, blank=True,null=True,default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' %(self.name, )
    class Meta:
        verbose_name = 'Категорія товара'
        verbose_name_plural = 'Категорії товарів'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=True,null=True,default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(default=0)
    price_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    type = models.ForeignKey(ProductCategory,on_delete=models.PROTECT,blank=True,null=True,default=None)
    short_description = models.TextField(blank=True, null=True, default = None)
    description = models.TextField(blank=True, null=True, default = None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' %(self.name, )
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def save(self, *args, **kwargs):
        self.price_discount=self.price-self.price*self.discount/100

        super(Product, self).save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True,default=None)
    image = models.ImageField(upload_to='')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' %(self.id, )
    class Meta:
        verbose_name = 'Фотографія'
        verbose_name_plural = 'Фотографії'




# Create your models here.
