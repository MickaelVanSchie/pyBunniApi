

from pyBunniApi.client import Client
from pyBunniApi.objects.project import Project



def test_invoice_list_untyped(project: Project, untypedClient: Client):
    untypedClient.create_http_request.return_value = {"items": [project, project]}
    resp = untypedClient.projects.list()
    assert len(resp) == 2
    assert isinstance(resp[0], dict)

def test_invoice_list_typed(project: Project, testClient: Client):
    testClient.create_http_request.return_value = {"items": [project, project]}
    resp = testClient.projects.list()
    assert len(resp) == 2
    assert isinstance(resp[0], Project)


def test_initiate_project_model(project: Project):
    # For this model both snake_case and camel_case are the same.
    project = Project(**project)

    assert project.color == '#FFFFFF'
    assert project.id == '1'
    assert project.name == 'Test project'