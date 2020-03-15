from model import project
from model.project import Project

def test_create_project(app):
    login = "administrator"
    password = "root"
    project = Project(name="new_name")
# логинимся
    app.session.login(login, password)
# создаём старый список проектов и запоминаем длинну
    #old_list = app.project_helper.get_project_list_count()
    old_list2 = len(app.soap.get_list_project(login, password))
# создаём проект
    app.project_helper.create_project(project)
# создаём новый список проектов и запоминаем длинну
    #new_list = app.project_helper.get_project_list_count()
    new_list2 = len(app.soap.get_list_project(login, password))
    # проверяем, что стало больше
    assert old_list2 + 1 == new_list2