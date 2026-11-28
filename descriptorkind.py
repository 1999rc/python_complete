def cls(obj_or_cls):
    cls=type(obj_or_cls)
    if cls is type:
        cls=obj_or_cls
    return cls.__name__.split('.')[-1]
def display(obj):
    cls=type(obj)
    if cls is type:
        return f'<class {(obj.__name__)}'
    elif cls == [type(None),int]:
        return repr(obj)
    else:
        return f'<{cls_name(obj)} object>'
def print_args(name,*args):
    pseudo_args=','.join(display(x)for x in args)
    print(f'-> {cls_name(args[0])}.__{name}__({pseudo_args})')
    #print('-> {}.__{}__({})'.format(cls_name(args[0]),name,qseudo_args))
class Overriding:
    '''a.k.a data descriptionr or enforced descriptor'''
    def __get__(self,instance,owner):
        print_args('get',self,instance,owner)
    def __set__(self,instance,value):
        print_args('set',self,instance,value)
class OverridingNoGet:
    '''an overriding descriptor with ``__get__``'''
    def __set__(self,instance,value):
        print_args('set',self,instance,value)
class NonOverriding:
    '''a.k.a. non-data or shadowable descriptor'''
    def __get__(self,instance,owner):
        print_args('get',self,instance,owner)
class Managed:
    over=Overriding()
    over_no_get=OverridingNoGet()
    non_over=NonOverriding()
    def spam(self):
        print('-> Managed.spam(display{self})')
obj=Managed()
obj.over()