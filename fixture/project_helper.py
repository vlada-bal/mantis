from model.project import Project
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import random
import string

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        symbolList = [random.choice(symbols) for i in range(maxlen)]
        return prefix + "".join(symbolList)

    # работает
    def create_project(self, project):
        wd = self.app.wd
        self.open_create_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()


    #работает
    def delete_project(self):
        wd = self.app.wd
        self.open_create_page()
        wd.find_element_by_css_selector(".row-1 td a").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()



    #работает
    project_cache = None
    def get_project_list_names(self):
        wd = self.app.wd
        self.open_create_page()
        names = []
        elements = wd.find_elements_by_xpath("//table[@class='width100'][ @cellspacing='1']//tr[contains(@class, 'row')][@class != 'row-category']//a")
        for element in elements:
            project_name= element.text
            names.append(project_name)
        return names

    # конвертировать список пришедший из мыла в проджект модель
    def convert_to_project_model(self, list):
        result = []
        for project_soap in list:
            name=project_soap.name
            project = Project(name=name)
            result.append(project)
        return result

    # открыть страницу создания проекта
    # Работает
    def open_create_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

      #  wd.get("http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php")
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_create_page.php

    # открыть страницу созданных проектов чтобы посчитать длину
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php

