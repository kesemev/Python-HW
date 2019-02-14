#HW$-Kesem Even-Hen
#Q1 Custom OOP
def make_pair(x, y):
    """Return a function that behaves like a pair."""
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
    return dispatch
def str(p):
    """Return the pair in human-interpretable text ."""
    return '({}, {})'.format(getitem_pair(p, 0), getitem_pair(p, 1))
def getitem_pair(p, i):
    """Return the element at index i of pair p."""
    return p(i)
empty_rlist = None
def make_mutable_rlist():
    """Return a functional implementation of a mutable recursive list."""
    contents = empty_rlist
    def make_rlist(first, rest):
        """Make a recursive list from its first element and the rest."""
        return make_pair(first, rest)

    def first(s):
        """Return the first element of a recursive list s."""
        return getitem_pair(s, 0)

    def rest(s):
        """Return the rest of the elements of a recursive list s."""
        return getitem_pair(s, 1)

    def getitem_rlist(s, i):
        """Return the element at index i of recursive list s."""
        if i >= len_rlist(s):
            return None
        if i == 0:
            return first(s)
        return getitem_rlist(rest(s), i - 1)

    def str(s):
        if s == None:
            return
        return '({},{})'.format(first(s), str(rest(s)))

    def len_rlist(s):
        """Return the length of recursive list s."""
        length = 0
        while s != empty_rlist:
            s, length = rest(s), length + 1
        return length

    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_rlist(contents)
        elif message == 'getitem':
            return getitem_rlist(contents, value)
        elif message == 'push_first':
            contents = make_rlist(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return str(contents)
    return dispatch
def make_dict():
    """Return a functional implementation of a dictionary."""
    records = make_mutable_rlist()
    def getitem(key):
        """Return the value at key of dict."""
        for i in range(records('len')):
            if getitem_pair(records('getitem', i), 0) == key:
                return getitem_pair(records('getitem', i), 1)
    def setitem(key, value):
        """Set the value at key of dict by the value got received. If the key was not found, the key and value will be added"""
        nonlocal records
        if records('len') == 0:
            records('push_first', make_pair(key, value))
            return
        flag = 0
        temp = make_mutable_rlist()
        for i in range(records('len')-1, -1, -1):
            if getitem_pair(records('getitem',i), 0) == key:
                temp('push_first', make_pair(key, value))
                flag = 1
            else:
                temp('push_first', records('getitem',i))
        if flag == 0:
            temp('push_first',make_pair(key,value))
        records = temp
    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
        elif message == 'keys':
            """rlist of all the keys."""
            temp1 = make_mutable_rlist()
            for i in range(records('len') - 1, -1, -1):
                temp1('push_first', getitem_pair(records('getitem', i), 0))
            return temp1
        elif message == 'values':
            """rlist of all the values."""
            temp2 = make_mutable_rlist()
            for i in range(records('len') - 1, -1, -1):
                temp2('push_first', getitem_pair(records('getitem', i), 1))
            return temp2
        return dispatch
def make_instance(cls):
    """Return a new object instance, which is a dispatch dictionary."""
    attributes = make_dict()
    def get_value(name):
        """Returns the value of the variable if it is a class variable, otherwise returns the result of the value found in cls"""
        if attributes('getitem', name) != None:
            return attributes('getitem',name)
        else:
            value=cls('getitem','get')(name)
            if callable(value):
                def method(*args):
                    return value(instance, *args)
                return method
            else:
                return value

    def set_value(name, value):
        """Set the value of the name variable which received"""
        attributes('setitem',name,value)
        #obj = {'get': get, 'set': set}
        # calls constructor if present
    instance = make_dict()
    instance('setitem','get', get_value)
    instance('setitem','set', set_value)
    return instance
def make_class(attributes, base_class=None):
    """Return a new class, which is a dispatch dictionary."""
    def get_value(name):
        """Returns the value of the class variable, and if it is not found - return the value in the base class."""
        if attributes('getitem', name) != None:
            return attributes('getitem',name)
        elif base_class is not None:
            return base_class('getitem', name)
    def set_value(name, value):
        """Set the value of the name variable which received"""
        attributes('setitem',name,value)
    def new(*args):
        """Return new instance"""
        """Return a new object with type cls, initialized with args."""
        instance = make_instance(cls)
        init = cls('getitem', 'get')('__init__')
        if init:
            init(instance, *args)
        return instance
    #Dispatch dictionary
    cls=make_dict()
    cls('setitem','get',get_value)
    cls('setitem','set',set_value)
    cls('setitem','new',new)
    #cls = {'get': get, 'set': set, 'new': new}
    return cls

def make_point_class():
    def __init__(self, x=0,y=0):
        self('getitem', 'set')('x', x)
        self('getitem', 'set')('y', y)
    def getX(self):
        return self('getitem', 'get')('x')
    def getY(self):
        return self('getitem', 'get')('y')
    def setX(self,new_x):
        self('getitem', 'set')('x',new_x)
    def setY(self,new_y):
        self('getitem', 'set')('y', new_y)
    def __str__(self):
        return '({},{})'.format(self('getitem', 'get')('getX')(),self('getitem', 'get')('getY')())
    def distance(self,other):
        return ((self('getitem', 'get')('getX')() - other('getitem', 'get')('getX')())**2 + (self('getitem', 'get')('getY')() - other('getitem', 'get')('getY')())**2)**0.5
    p = make_dict()
    p('setitem', '__init__', __init__)
    p('setitem', 'getX', getX)
    p('setitem', 'getY', getY)
    p('setitem', 'setX', setX)
    p('setitem', 'setY', setY)
    p('setitem', 'str', __str__)
    p('setitem', 'distance', distance)
    return make_class(p)

Point= make_point_class()

def make_line_class():
    def __init__(self, p1=Point('getitem', 'new')(0,0), p2=Point('getitem', 'new')(1,1)):
        self('getitem', 'set')('p1', p1)
        self('getitem', 'set')('p2', p2)
    def getPoint(self,num):
        if num==1:
            return self('getitem', 'get')('P1')('p1')
        elif num==2:
            return self('getitem', 'get')('p2')
        print('Error! you need to chooce 1 for point1 or 2 for point2')
    def setPoint(self,num,x,y):
        if num==1:
            self('getitem','get')('p1')('getitem','get')('setX')(x)
            self('getitem','get')('p1')('getitem', 'get')('setY')(y)
        elif num==2:
            self('getitem','get')('p2')('getitem', 'get')('setX')(x)
            self('getitem','get')('p2')('getitem', 'get')('setY')(y)
        print('Error! you need to chooce 1 for point1 or 2 for point2')
    def __str__(self):
        try:
            m=(self('getitem','get')('p1')('getitem','get')('getY')()-self('getitem','get')('p2')('getitem','get')('getY')())/(self('getitem','get')('p1')('getitem','get')('getX')()-self('getitem','get')('p2')('getitem','get')('getX')())
        except ZeroDivisionError as e: #handling a <class 'ZeroDivisionError'>
            return 'x={}'.format(self('getitem','get')('p1')('getitem','get')('getX')())
        b=self('getitem','get')('p1')('getitem','get')('getY')()-m*self('getitem','get')('p1')('getitem','get')('getX')()
        return 'y={}x+{}'.format(m, b)
    def isOnLine(self,p3):
        m = (self('getitem', 'get')('p1')('getitem', 'get')('getY')() - self('getitem', 'get')('p2')('getitem', 'get')(
            'getY')()) / (self('getitem', 'get')('p1')('getitem', 'get')('getX')() - self('getitem', 'get')('p2')(
            'getitem', 'get')('getX')())
        b = self('getitem', 'get')('p1')('getitem', 'get')('getY')() - m * self('getitem', 'get')('p1')('getitem','get')('getX')()
        if p3('getitem', 'get')('getY')()== m*p3['get']('getitem', 'get')('getX')() + b:
            return True
        else:
            return False
    p = make_dict()
    p('setitem', '__init__', __init__)
    p('setitem', 'getPoint', getPoint)
    p('setitem', 'setPoint', setPoint)
    p('setitem', 'isOnLine', isOnLine)
    p('setitem', 'str', __str__)
    return make_class(p)

Line=make_line_class()


"""--------------------------------------------------------------------------------------------------"""
#Q2
def make_instance(cls):
    """Return a new object instance"""
    attributes = {}
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            value = cls['get'](name)
            if callable(value):
                def method(*args):
                    return value(instance, *args)
                return method
            else:
                return value
    def set_value(name, value):
        attributes[name] = value
    instance = {'get': get_value, 'set': set_value}
    return instance

def make_class(attributes, base_class = None):
    """return a new singleton class"""
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name, value):
        attributes[name] = value
    cls = {'get': get_value, 'set': set_value}
    return cls

def make_printer_driver_class():
    count = 0
    def __init__(self, printer_name):
        self['set']('name', printer_name)
    def getPrinter():
        nonlocal count
        if count == 0:
            __init__(printer, 'printerName')
            count = 1
        else:
            print('Sorry,it can be only one printer')
        return printer
    def activate(self, path):
        print('The printer',self['get']('name'),'is printing the file:', path)
    cls = make_class({'__init__': __init__,'getPrinter': getPrinter, 'activate': activate})
    printer = make_instance(cls)
    return cls

pr = make_printer_driver_class()
HP1= pr['get']('getPrinter')()
HP1['get']('activate')('c:/user/kesem/studies/doc1')
HP2 = pr['get']('getPrinter')()
print(HP1 is HP2)
HP2['get']('activate')('c:/user/kesem/desktop/doc2')


"""----------------------------------------------------------------------"""
#Q3-part A

class Kg(object):
    def __init__(self,value):
        self.value = float(value)
    def __repr__(self):
        return 'Kg({})'.format(self.value)
    def __str__(self):
        return '{} Kg'.format(self.value)
    def amount(self):
        return self.value
    def __add__(self, otherobj):
        return self.amount() + otherobj.amount()

class Pound(object):
    def __init__(self,value):
        self.value = float(value)
    def __repr__(self):
        return 'Pound({})'.format(self.value)
    def __str__(self):
        return '{} Ib'.format(self.value)
    def amount(self):
        return self.value * Conversions[('pound', 'kg')]
    def __add__(self, otherobj):
        return self.amount() + otherobj.amount()

class Ounce(object):
    def __init__(self,value):
        self.value = float(value)
    def __repr__(self):
        return 'Ounce({})'.format(self.value)
    def __str__(self):
        return '{} Oz'.format(self.value)
    def amount(self):
        return self.value * Conversions[('qunce', 'kg')]
    def __add__(self, otherobj):
        return self.amount() + otherobj.amount()

def add(object_1, object_2):  # Generic add func.
    return object_1.amount() + object_2.amount()

Conversions={('pound', 'kg'): 0.4536 , ('qunce', 'kg'): 0.028349523125}  #Dictionary of Conversions.

# k = Kg(10)
# p = Pound(10)
# q = Ounce(10)
# print(k.amount())
# print(p.amount())
# print(q.amount())
# print(p+k)
# print(add(p,q))
# x = eval(repr(q))
# print(q)
# print(k)
# print(p)
# print(q)

#Q3- part B

def sub(object_1, object_2):  # Generic sub func.
    return object_1.amount() - object_2.amount()

dict = {'add': add, 'sub': sub}

def apply(operation, object_1, object_2):
    if type(object_1) == Pound:
        return 'Pound({})'.format(dict[operation](object_1, object_2) / Conversions[('pound', 'kg')])
    elif type(object_1) == Ounce:
        return 'Ounce({})'.format(dict[operation](object_2, object_1) / Conversions[('qunce', 'kg')])
    else:
        return 'Km({})'.format(dict[operation](object_1, object_2))

# print(apply('add',Kg(10),Ounce(10)))
# print(apply('add',Pound(40),Ounce(20)))
# print(apply('sub',Pound(40),Ounce(20)))
