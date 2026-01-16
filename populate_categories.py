import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storage_project.settings')
django.setup()

from inventory.models import Category

CATEGORIES = [
    "Food",
    "Furniture",
    "Gadget",
    "Fashion",
    "Office"
]

for name in CATEGORIES:
    Category.objects.get_or_create(name=name)

print("Default categories populated.")
