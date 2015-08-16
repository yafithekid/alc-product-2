class ErrorBag:
    def __init__(self):
        self.__errors = {}

    def add(self, key: str, value: str):
        if not (key in self.__errors):
            self.__errors[key] = []
        self.__errors[key].append(value)

    def first(self, key: str) -> str:
        if (not (key in self.__errors)) or (self.__errors[key] is None) or (len(self.__errors[key]) == 0):
            return None
        else:
            return self.__errors[key][0]

    def all(self, key: str) -> list:
        return self.__errors[key]

    def has_error(self, key: str) -> bool:
        return not (self.first(key) is None)

    def __str__(self):
        ret = ""
        first = True
        for key_error in self.__errors:
            list_error = self.__errors[key_error]
            if not (list_error is None) and len(list_error) > 0:
                for error in list_error:
                    if not first:
                        ret += ","
                    ret = key_error + ":" + error
                    first = False
        return ret


class Field:
    def validate(self, field_name, value):
        raise NotImplementedError


class StringField(Field):
    def __init__(self, max_length=None, required=False):
        self.max_length = max_length
        self.required = required

    def validate(self, field_name, value):
        if self.required:
            error = False
            if not hasattr(value, field_name):
                error = True
            else:
                instance = getattr(value, field_name)
                if isinstance(instance, Field):
                    error = True
                else:
                    error = instance is None
            if (error):
                value.add_error(field_name, "This field is required")
        else:
            field = getattr(value, field_name)
            if not (isinstance(field, Field)) and not isinstance(field, str):
                value.add_error(field_name, "Not a string")

            if not (self.max_length is None) and len(field) > self.max_length:
                value.add_error(field_name, "Maximum " + field + " characters")


# represent a integer
class NumberField(Field):
    def __init__(self, min=None, max=None, required=False):
        self.min = min
        self.max = max
        self.required = required

    def validate(self, field_name, value):
        if self.required and (
                        not hasattr(value, field_name) or isinstance(getattr(value, field_name), Field) or getattr(
                    value,
                    field_name) is None):
            value.add_error(field_name, "This field is required")
        else:
            field = getattr(value, field_name)
            if not isinstance(field, int):
                value.add_error(field_name, "Not a number")

            if not (self.min is None) and field < self.min:
                value.add_error(field_name, "Minimum value exceeded")

            if not (self.max is None) and (field > self.max):
                value.add_error(field_name, "Maximum value exceeded")


class ListField(Field):
    def __init__(self, required=False):
        self.required = required

    def validate(self, field_name, value):
        if self.required and (not hasattr(value, field_name) or isinstance(getattr(value, field_name), Field)):
            value.add_error(field_name, "This field is required")


class ObjectIdField(Field):
    def __init__(self, required=False):
        self.required = required

    def validate(self, field_name, value):
        # TODO
        return True


class DocumentField(Field):
    def __init__(self, BaseClass, required=False):
        self.BaseClass = BaseClass
        self.required = required

    def validate(self, field_name, value):
        if self.required:
            if isinstance(getattr(value, field_name), Field):
                value.add_error(field_name, "This field is required")
            else:
                field = getattr(value, field_name)
                if not isinstance(field, self.BaseClass):
                    value.add_error(field_name, "Not an instance of " + self.BaseClass.__name__)
        elif not (isinstance(getattr(value, field_name), Field)):
            field = getattr(value, field_name)
            if not isinstance(field, self.BaseClass):
                    value.add_error(field_name, "Not an instance of " + self.BaseClass.__name__)


class ListField(Field):
    def __init__(self, required=False):
        self.required = required

    def validate(self, field_name, value):
        if self.required and isinstance(getattr(value, field_name), Field):
            value.add_error(field_name, "This field is required")
        else:
            field = getattr(value, field_name)
            if not isinstance(field, list):
                value.add_error(field_name, "Not an instance of list")
