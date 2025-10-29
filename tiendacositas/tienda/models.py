from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_index=True)  # índice simple (punto 5)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
    
    class Meta:
        indexes = [
            models.Index(fields=['nombre'], name='idx_producto_nombre'),  # índice compuesto (redundante a db_index, usado a modo didáctico)
        ]