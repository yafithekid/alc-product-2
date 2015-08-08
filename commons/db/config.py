from commons.db.api.factories import MongoClientFactory
from commons.db.providers import MongoClientFactoryProvider

db_providers = [
    MongoClientFactoryProvider('localhost')
]