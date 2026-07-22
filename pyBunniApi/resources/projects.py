from pyBunniApi.objects.project import Project
from pyBunniApi.resources.base import BaseListResource


class Projects(BaseListResource[Project]):
    endpoint = 'projects'
    model = Project
