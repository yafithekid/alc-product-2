class MockServiceImpl:
    pass


class Provider:
    def register(self, interface_name, container, containers):
        raise NotImplementedError


class Container:
    def __init__(self, config, containers = None):
        self.__services = {}
        for interface_name, provider in config.items():
            if not isinstance(provider,Provider):
                raise NotAProviderException
            provider.register(interface_name, self, containers)

    def save(self, name, service_impl):
        if name in self.__services:
            raise ServiceAlreadyExistException(name)
        self.__services[name] = service_impl

    def load(self, name):
        if not name in self.__services:
            print(self.__services)
            raise ServiceNotFoundException(name)
        return self.__services[name]


class ServiceNotFoundException(Exception):
    def __init__(self, interface_name):
        super().__init__("Interface " + interface_name + " not found")


class ServiceAlreadyExistException(Exception):
    def __init__(self, interface_name):
        super().__init__("Interface " + interface_name + "already exists")


class NotAProviderException(Exception):
    def __init__(self,provider_name):
        super().__init__(provider_name+ " is not an instance of provider")