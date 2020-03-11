from model.project import Project


def test_delete_project(app):
    # логинимся
    app.session.login("administrator", "root")
    # если проектов не было. создаём новый
    if len(app.get_project_list()) == 0:
        app.project_helper.create_project(Project(name="del_pro"))
    # создаём старый список проектов и запоминаем длинну
    old_list = len(app.get_project_list())
    # удаляем проект
    app.project_helper.delete_project()
    # создаём новый список проектов и запоминаем длинну
    new_list = len(app.get_project_list())
    # проверяем, что стало меньше
    assert old_list - 1 == new_list