from commons.db.api.factories import MongoClientFactory
from commons.db.providers import MongoClientFactoryProvider

db_providers = {
    MongoClientFactory.__name__ : MongoClientFactoryProvider('localhost')
}