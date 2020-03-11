from model import project
from model.project import Project

def test_create_project(app):
    # логинимся
    app.session.login("administrator", "root")
    # создаём старый список проектов и запоминаем длинну
    old_list = len(app.get_project_list())
    # создаём проект
    app.project_helper.create_project(project)
    # создаём новый список проектов и запоминаем длинну
    new_list = len(app.get_project_list())
    # проверяем, что стало больше
    assert old_list + 1 == new_list