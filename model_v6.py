def entity(cls):
    for key in cls.__dict__.items():
        if isinstance(attr,Validated):
            type_name=type(attr).__name__
            attr.storage_name=f'_{type_name}#{key}'
    return cls 