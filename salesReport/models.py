from django.db import models

class item(models.Model):
    product_id = models.IntegerField(primary_key=True)
    weight = models.CharField(max_length=500, null=True, blank=True)
    sku = models.IntegerField(unique=True)
    name = models.CharField(max_length=500)
    cost = models.FloatField(max_length=500, null=True, blank=True)
    price = models.FloatField(max_length=500)
    brand = models.ForeignKey('brands', null=True, blank=True)

    def __unicode__(self):
        return self.name

class order(models.Model):
    increment_id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField()
    customer_id = models.BigIntegerField(null=True, blank=True)
    subtotal = models.FloatField()
    grand_total = models.FloatField()
    status = models.CharField(max_length=500)
    shipping_method = models.CharField(max_length=500, null=True, blank=True)
    customer_email = models.CharField(max_length=500, null=True, blank=True)
    customer_firstname = models.CharField(max_length=500, null=True, blank=True)
    customer_lastname = models.CharField(max_length=500, null=True, blank=True)
    order_id = models.FloatField()

    item = models.ManyToManyField(item, through='orderItem')

    def __unicode__(self):
        return '%s' % self.increment_id



class orderItem(models.Model):
    created_at = models.DateTimeField(max_length=500, null=True, blank=True)
    updated_at = models.DateTimeField(max_length=500, null=True, blank=True)
    quantidade = models.FloatField()

    item = models.ForeignKey(item)
    order = models.ForeignKey(order)

    def __unicode__(self):
        return '%s - %s' % (self.item.name, self.order.increment_id)


class brands(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'brands'
        verbose_name_plural = 'brands'