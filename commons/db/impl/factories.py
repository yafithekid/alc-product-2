from pymongo import MongoClient
from commons.db.api.factories import MongoClientFactory


class MongoClientFactoryImpl(MongoClientFactory):
    def __init__(self,host='localhost'):
        self.host = host

    def get_lc_client(self):
        return MongoClient(self.host,27017)

    def get_user_client(self):
        return MongoClient(self.host,27017)
