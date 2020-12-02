import os
import django
import csv
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "starbucksup.settings")
django.setup()


from products.models import Menu, Category, Drink

CSV_PATH_PRODUCTS = './products.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader), None
    for row in data_reader:
        if row[0]:
            menu_name = row[0]
        if row[1]:
            category_name = row[1]
            menu_id = Menu.objects.get(name = menu_name).id
            category_id = Category.objects.get(name = category_name).id
        drink_name = row[2]
        Drink.objects.create(name = drink_name, menu_id = menu_id, category_id = category_id)


