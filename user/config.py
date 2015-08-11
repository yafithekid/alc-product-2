from user.providers import UserDaoProvider, UserServiceProvider, AuthServiceProvider

dao_providers = [
    UserDaoProvider()
]

service_providers = [
    UserServiceProvider(),
    AuthServiceProvider()
]