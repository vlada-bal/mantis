from model import project
from model.project import Project

def test_create_project(app):
    login = "administrator"
    password = "root"
    name = app.project_helper.random_string('new_name', 4)
    project = Project(name=name)
# логинимся
    app.session.login(login, password)
# создаём старый список проектов и конвертируем в список как в модели проект
    #old_list = app.project_helper.get_project_list_names()
    old_list2 = app.soap.get_list_project(login, password)
    converted_old_list = app.project_helper.convert_to_project_model(old_list2)
# создаём проект
    app.project_helper.create_project(project)
# создаём новый список проектов
    #new_list = app.project_helper.get_project_list_names()
    new_list2 = app.soap.get_list_project(login, password)
    converted_new_list = app.project_helper.convert_to_project_model(new_list2)
# проверяем, что они равны
    converted_old_list.append(project)
    #assert old_list2.sort() == new_list2.sort()
    assert sorted(converted_old_list, key=Project.name) == sorted(converted_new_list, key=Project.name)
