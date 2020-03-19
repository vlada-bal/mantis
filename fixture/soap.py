from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app
        soap_config = self.app.config['web']
        self.base_url = soap_config['baseUrl']

    def can_login(self, username, password):
        client = Client(f"{self.base_url}/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    #работает
    def get_list_project(self, username, password):
        client = Client(f"{self.base_url}/api/soap/mantisconnect.php?wsdl")
        try:
            liast = client.service.mc_projects_get_user_accessible(username, password)
            return liast
        except WebFault:
            return None

