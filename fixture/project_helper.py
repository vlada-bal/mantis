from model.project import Project
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    #не работает
    def create_project(self, project):
        wd = self.app.wd
        self.open_create_page
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    #не работает
    def delete_project(self):
        wd = self.app.wd
        self.open_create_page
        wd.find_element_by_css_selector("[cellspacing='1']:not([class*='width75']) [class*='row-']:not([class*='row-category']) td:first-child").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    #не работает
    project_cache = None
    def get_project_list(self):

        if self.project_cache is None:
            wd = self.app.wd
            wd.current_url.endswith("/manage_proj_page.php")
            self.project_cache = []
            elements = wd.find_elements_by_css_selector("[cellspacing='1']:not([class*='width75']) [class*='row-']:not([class*='row-category']) td:first-child")
            for element in elements:
                name = element.find_element_by_css_selector("[cellspacing='1']:not([class*='width75']) [class*='row-']:not([class*='row-category']) td:first-child")
                self.project_cache.append(Project(name=name))
        return list(self.project_cache)




    # открыть страницу создания проекта
    def open_create_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php")
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_create_page.php

    # открыть страницу созданных проектов чтобы посчитать длину
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php

