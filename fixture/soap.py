
from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    # не работает
    def get_list_project(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            liast = client.service.mc_projects_get_user_accessible(username, password)
            return liast
        except WebFault:
            return None

