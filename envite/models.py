from django.db import models

# Create your models here.
class SeatingTable(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=8)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def guest_count(self):
        return self.guests.count()


class SeatingGuest(models.Model):
    table = models.ForeignKey(SeatingTable, on_delete=models.CASCADE, related_name='guests')
    name = models.CharField(max_length=255)
    seat = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} → {self.table.name}"