from pyBunniApi.objects.category import Category
from pyBunniApi.resources.base import BaseListResource


class Categories(BaseListResource[Category]):
    endpoint = 'categories'
    model = Category
