from .connector import Connector


class Salesforce:
    def __init__(self):
        self.connector = Connector()

    def do_next(self):
        return self.connector.do_next()
