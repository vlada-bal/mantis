from model import project
from model.project import Project

def test_create_project(app):
    login = "administrator"
    password = "root"
    project = Project(name="new_name")
# логинимся
    app.session.login(login, password)
# создаём старый список проектов и запоминаем имена
    old_list = app.project_helper.get_project_list_names()
    #old_list2 = len(app.soap.get_list_project(login, password))
# создаём проект
    app.project_helper.create_project(project)
# создаём новый список проектов и запоминаем имена
    new_list = app.project_helper.get_project_list_names()
    #new_list2 = len(app.soap.get_list_project(login, password))
# проверяем, что они не равны
    old_list.append(project.name)
    assert old_list.sort() == new_list.sort()
