from model.project import Project


def test_delete_project(app):
    login = "administrator"
    password = "root"
# логинимся
    app.session.login(login, password)
# если проектов не было. создаём новый
    #if app.project_helper.get_project_list_count() == 0:
    if len(app.soap.get_list_project(login, password)) ==0:
        app.project_helper.create_project(Project(name="del_pro"))
# создаём старый список проектов и запоминаем длинну
    #old_list = app.get_project_list_count()
    old_list2 = len(app.soap.get_list_project(login, password))
# удаляем проект
    app.project_helper.delete_project()
# создаём новый список проектов и запоминаем длинну
    #new_list = app.project_helper.get_project_list_count()
    new_list2 = len(app.soap.get_list_project(login, password))
# проверяем, что стало меньше
    assert old_list2 - 1 == new_list2