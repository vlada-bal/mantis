from model.project import Project


def test_delete_project(app):
    login = "administrator"
    password = "root"
# логинимся
    app.session.login(login, password)
# если проектов не было. создаём новый
    if len(app.project_helper.get_project_list_names()) == 0:
    #if len(app.soap.get_list_project(login, password)) ==0:
        app.project_helper.create_project(Project(name="del_pro"))
# создаём старый список проектов и запоминаем имена
    old_list = app.project_helper.get_project_list_names()
    #old_list2 = len(app.soap.get_list_project(login, password))
# удаляем проект
    app.project_helper.delete_project()
# создаём новый список проектов и запоминаем имена
    new_list = app.project_helper.get_project_list_names()
    #new_list2 = len(app.soap.get_list_project(login, password))
# проверяем
    assert len(old_list) - 1 == len(new_list)