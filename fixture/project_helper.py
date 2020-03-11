from model.project import Project

from selenium.webdriver.support.ui import Select

class ProjectHelper:
    def __init__(self, app):
        self.app = app


    def create_project(self, project):
        wd = self.app.wd
        pass

    def delete_project(self):
        wd = self.app.wd
        pass

    def get_project_list(self):
        wd = self.app.wd
        wd.current_url.endswith("/manage_proj_page.php")
        elements = wd.find_elements_by_css_selector("tr[class=row-category]")
        for element in elements:
            firstname = element.find_elements_by_css_selector("td:nth-child(3)")[0].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            self.contact_cache.append(Project(id=id, name=name))

        contact_cache = None

        def get_contact_list(self):
            if self.contact_cache is None:
                wd = self.app.wd
                self.return_to_homepage()
                self.contact_cache = []
                elements = wd.find_elements_by_css_selector("tr[name=entry]")
                for element in elements:
                    firstname = element.find_elements_by_css_selector("td:nth-child(3)")[0].text
                    lastname = element.find_elements_by_css_selector("td:nth-child(2)")[0].text
                    address = element.find_elements_by_css_selector("td:nth-child(4)")[0].text
                    id = element.find_element_by_name("selected[]").get_attribute("value")
                    all_phones = element.find_elements_by_css_selector("td:nth-child(6)")[0].text
                    all_emails = element.find_elements_by_css_selector("td:nth-child(5)")[0].text
                    self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                      all_phones_from_home_page=all_phones,
                                                      all_emails_from_home_page=all_emails))
            return list(self.contact_cache)












    # открыть страницу создания проекта
    def open_create_page(self):
        wd = self.app.wd
        wd.current_url.endswith("/manage_proj_create_page.php")
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_create_page.php

    # открыть страницу созданных проектов чтобы посчитать длину
    # http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/manage_proj_page.php

