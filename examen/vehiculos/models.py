# vehiculos/models.py

from django.db import models

class Vehiculoo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()

    def __str__(self):
        return self.nombre

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def add(self, vehiculo, quantity=1):
        cart_item, created = CartItem.objects.get_or_create(cart=self, vehiculo=vehiculo)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

    def remove(self, vehiculo):
        CartItem.objects.filter(cart=self, vehiculo=vehiculo).delete()

    def get_total(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    vehiculo = models.ForeignKey(Vehiculoo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.vehiculo.nombre}"

    def get_total_price(self):
        return self.quantity * self.vehiculo.precio
