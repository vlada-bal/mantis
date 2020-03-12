from model import project
from model.project import Project

def test_create_project(app):
    project = Project(name="new_name")
    # логинимся
    app.session.login("administrator", "root")
    # создаём старый список проектов и запоминаем длинну
    old_list = len(app.project_helper.get_project_list())
    # создаём проект
    app.project_helper.create_project(project)
    # создаём новый список проектов и запоминаем длинну
    new_list = len(app.project_helper.get_project_list())
    # проверяем, что стало больше
    assert old_list + 1 == new_list