def type_validation(variable, _type):
    if type(variable) == _type:
        return type_validation(42, "int")

