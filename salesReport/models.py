from django.db import models

# Create your models here.

class order(models.Model):
    increment_id = models.CharField(max_length=500, primary_key=True)
    created_at = models.DateField(max_length=500, null=True, blank=True)
    updated_at = models.DateField(max_length=500, null=True, blank=True)
    is_active = models.CharField(max_length=500, null=True, blank=True)
    customer_id = models.CharField(max_length=500, null=True, blank=True)
    subtotal = models.CharField(max_length=500, null=True, blank=True)
    grand_total = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=500, null=True, blank=True)
    shipping_method = models.CharField(max_length=500, null=True, blank=True)
    customer_email = models.CharField(max_length=500, null=True, blank=True)
    customer_firstname = models.CharField(max_length=500, null=True, blank=True)
    customer_lastname = models.CharField(max_length=500, null=True, blank=True)
    order_id = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
        return '%s' % self.increment_id

class orderItem(models.Model):
    item_id = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.CharField(max_length=500, null=True, blank=True)
    updated_at = models.CharField(max_length=500, null=True, blank=True)
    product_id = models.CharField(max_length=500, null=True, blank=True)
    weight = models.CharField(max_length=500, null=True, blank=True)
    sku = models.CharField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    free_shipping = models.CharField(max_length=500, null=True, blank=True)
    cost = models.CharField(max_length=500, null=True, blank=True)
    price = models.CharField(max_length=500, null=True, blank=True)

    order = models.ForeignKey(order, related_name='orderItem')

    def __unicode__(self):
        return '%s - %s' % (self.sku , self.order.increment_id)

class brands(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'brands'
        verbose_name_plural = 'brands'