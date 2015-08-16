from commons.fields import Field, ErrorBag


class Entity:
    def __init__(self):
        self.field_names = Entity.get_field_names()
        self.errors = ErrorBag()

    def validate(self, field_name=None):
        if field_name is None:
            field_names = self.__class__.get_field_names()
            print(field_names)
            for field_name in field_names:
                self.validate(field_name)
        else:
            if hasattr(self.__class__, field_name):
                field = getattr(self.__class__, field_name)
                if isinstance(field, Field):
                    print(field_name)
                    field.validate(field_name, self)

    def field_exist(self, name: str) -> bool:
        return name in self.field_names

    def add_error(self, field: str, value: str):
        self.errors.add(field, value)

    def has_error(self, field: str = None) -> bool:
        if field is None:
            field_names = self.__class__.get_field_names()
            for field_name in field_names:
                if (self.has_error(field_name)):
                    return True
            return False
        else:
            return self.errors.has_error(field)

    def get_error_first(self, field: str) -> str:
        return self.errors.first(field)

    @classmethod
    def get_field_names(cls):
        ret = []
        for field_name in vars(cls):
            # if it is not ignored and it is an instance of field, we must inspect it
            if isinstance(getattr(cls, field_name), Field):
                # initialize the field names
                ret.append(field_name)
        return ret