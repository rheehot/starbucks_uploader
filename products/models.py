from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)
    class Meta:
        db_table = 'menus'

class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'categories'

class Drink(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, null = True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null = True)
    class Meta:
        db_table = 'drinks'
