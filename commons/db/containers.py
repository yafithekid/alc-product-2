from commons.db.config import db_providers
from commons.ioc import Container


class DBContainer(Container):
    def __init__(self,provider):
        super().__init__(provider,None)

db_container = DBContainer(db_providers)