def cls(obj_or_cls):
    cls=type(obj_or_cls)
    if cls is type:
        cls=obj_or_cls
    return cls.__name__.split('.')[-1]
def display(obj):
    cls=type(obj)
    if cls is type:
        return f'<class {(obj.__name__)}'
    elif cls is [type(None),int]:
        return repr(obj)
    else:
        return f'< object>'