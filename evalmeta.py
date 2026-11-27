from evalsupport deco_alpha
import evaltime
from evalsupport import MetaAlpha
print('<[1] evaltime_meta module start')
class ClassOne():
    print('<[2]> ClassOne body')
    def __init__(self):
        print('<[3]> ClassOne.__init__')
    def __del__(self):
        print('<[4]> ClassOne.__del__')
    def method_x(self):
        print('<[5]> ClassOne.method_x')
class ClassTwo(object):
    print('<[6]> ClassTwo body')
@deco_alpha 
class ClassThree():
    print('<[2]> ClassThree body')
    def method_y(self):
        print('<[3]> ClassThree.method_y')
class ClassFour(ClassThree):
    print('<[4]> ClassFour body')
    def method_y(self):
        print('<[5]> ClassFour.method_y')
class ClassFive(metaclass=MetaAlpha):
    print('<[6]> ClassFive body')
    def __init__(self):
        print('<[7]> ClassFive.__init__')
    def method_z(self):
        print('<[8]> ClassFive.method_y')
class ClassSix(ClassFive):
    print('<[9]> ClassSix body')
    def method_z(self):
        print('<[10]> ClassSix.method_y')
if __name__=='__main__':
    print('<[11]> ClassTree test',30*'.')
    three=ClassThree()
    three.method_y()
    print('<[12]> ClassFour test',30*'.')
    four=ClassFour()
    four.method_y()
    print('<[13]> ClassFive tests',30*'.')
    five=ClassFive()
    five.method_z()
    print('<[14]> ClassSix test',30*'.')
    six=ClassSix()
    six.method_z()
print('<[15]> evalmets module end😍')
