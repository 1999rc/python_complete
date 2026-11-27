class MetaAlpha(type):
    print('<[400]> MetaAlpha body')
    def __init__(cls,name,bases,dict):
        print('<[500] MetaAlpha.__init__')
        def inner_2(self):
            print('<[600]> MetaAlpha.__init__:inner_2')
        cls.method_z=inner_2