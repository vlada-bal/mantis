from model.project import Project


def test_delete_project(app):
    login = "administrator"
    password = "root"
# логинимся
    app.session.login(login, password)
# если проектов не было. создаём новый
    #if len(app.project_helper.get_project_list_names()) == 0:
    if len(app.soap.get_list_project(login, password)) ==0:
        app.project_helper.create_project(Project(name="del_pro"))
# создаём старый список проектов
    #old_list = app.project_helper.get_project_list_names()
    old_list2 = app.soap.get_list_project(login, password)
    converted_old_list = app.project_helper.convert_to_project_model(old_list2)
# удаляем проект
    app.project_helper.delete_project()
# создаём новый список проектов и запоминаем имена
    #new_list = app.project_helper.get_project_list_names()
    new_list2 = app.soap.get_list_project(login, password)
    converted_new_list = app.project_helper.convert_to_project_model(new_list2)# проверяем
    excluded_first = converted_old_list[1:]
    assert excluded_first == converted_new_list