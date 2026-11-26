import collections


class Validated:
    pass

class EntityMeta(type):
    '''Metaclass for business entities with validation fields'''
    @classmethod 
    def __prepare__(cls,name,bases):
        return collections.OrderDict()
    def __init__(cls,name,bases,attr_dict):
        super().__init__(name,bases,attr_dict)
        cls._field_names=[]
        for key,attr in attr_dict.items():
            if isinstance(attr,Validated):
                type_name=type(attr).__name__ 
                attr.storage_name=f'_{type_name}#{key}'
                cls._field_names.append(key)
class Entity(metaclass=EntityMeta):
    '''business entity with validated fields'''
    @classmethod
    def field_names(cls):
        yield from cls._field_names
