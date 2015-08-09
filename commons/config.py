from commons.db.providers import MongoSerializationFactoryProvider, MongoDatabaseFactoryProvider

mongo_providers = [
    MongoSerializationFactoryProvider(),
    MongoDatabaseFactoryProvider(default_host='localhost')
]