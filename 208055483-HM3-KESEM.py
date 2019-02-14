"""HM3, Kesem Even-Hen, 208055483"""

class Collection(object):
    """ 1
     The constructor is defined as being able (but not required) to accept any iterable object except for dict
     :param iterable object except for dictionary
    """
    def __init__(self, iterable=None):
        if iterable != None:
            self.iterable = tuple(iterable)

    def first(self):
        """ 2
        :return: return a copy of the first item stored in the internal collection
        """
        return self.iterable[0]

    def last(self):
        """ 3
        :return: return a copy of the last item stored in the internal collection.
        """
        return self.iterable[-1]

    def take(self,amount):
        """ 4
        :param amount: the amount to return
        :return: return a new Collection contain a subset of
        the original items based on the amount desired. If the amount provided is greater than the
        total length of the collection, the additional amount should be ignored.
        """
        return Collection(self.iterable[:amount])

    def append(self, *elements):
        """ 5
        :param elements: elements to add to the end of the collection
        :return:  return a new Collection with the new elements appended to the end.
        """
        x=(*self.iterable, *elements)
        return Collection(x)

    def prepend(self, *elements):
        """ 6
        adds elements to the beginning of the new Collection .
        :param elements: elements to add to the start of the collection
        :return: return a new Collection with the new elements appended to the beginning.
        """
        x = (*elements,*self.iterable)
        return Collection(x)

    def filter(self, *callbacks):
        """ 7
         like the global method, however, it can receive many callbacks instead of just one.
        :param callbacks: functions to apply the filtering by.
        :return:  return an new filtered Collection
        """
        return Collection(item for item in self.iterable if all(func(item) for func in callbacks))

    def map(self, *callbacks):
        """ 8
        act just like the global method
        :param callbacks: functions to apply to the collection
        :return: return a new mapped Collection
        """
        new = self.iterable
        for i in range(len(callbacks)):
            new = list(map(callbacks[i], new))
        return Collection(type(self.iterable)(new))

    def reduce(self, callback, initial=0):
        """ 9
        act just like the global method
        :param callback: a function to calculate the collection value result
        :param initial: initial value to calculate from- default 0.
        :return: return reduced value
        """
        for item in self.iterable:
            initial = callback(initial, item)
        return initial

    def sort(self, key=None, reversed=False):
        """ 10
        :param key: specifies a function of one argument that is used to extract a comparison key from each list element. If no key was provided, the collection should be sorted using standard sorting strategies
        :param reversed: optional boolean argument. If specified as True then elements are sorted in reverse order.
        :return: return a new sorted Collection based on the key provided.
        """
        if key is not None:
            return Collection(sorted(self.iterable, key=lambda x: x[key], reverse=reversed))
        else:
            return Collection(sorted(self.iterable, key=key, reverse=reversed))

    def set(self, position, value):
        """ 11
        :param position: position to set the value in the collection
        :param value: value to set in the collection
        :return: return a new Collection while setting the value at the position provided.
        If the position does not exist, no action should be taken and a copy of the Collection should be returned
        """
        if position>len(self.iterable):
            return Collection(self.iterable)
        else:
            new=(*self.iterable[:position],value,*self.iterable[position+1:])
            return Collection(new)

    def pluck(self, key):
        """ 12
        :param key: the key to look for
        :return: return a new Collection with the only the
        key of each element. If the internal elements are not dictionaries, then no action should
        be taken and a copy of the current collection should be returned.
        """
        new = map(lambda x: type(x) is not dict, self.iterable)
        if any(new):
            return Collection(self.iterable)
        return Collection([i[key] for i in self.iterable])

    def values(self):
        """ 13
        :return: return a copy of the internal values
        """
        return self.iterable

    def unique(self):
        """ 14
        :return: return a new Collection with only unique items
        """
        return Collection(self.iterable[index] for index in range(len(self)) if self.iterable[:index].count(self[index])==0 )

    def tap(self, callback):
        """ 15
        :param callback: a function
        :return: each element of the collection by-value to a callback function
        """
        for x in self.iterable:
            callback(x)

    #Special Methods
    def  __getitem__(self, position):
        """ 1
        :param position: position of the item that i want to get
        :return: return the item at a given position
         If the position provided does not exist, None should be returned
        """
        if position>abs(len(self.iterable)):
            return None
        return self.iterable[position]

    def __add__(self, other):
        """ 2
        should concatenate two collections or a collection with an iterable object.
        :param other: collection or iterable object
        :return: new collections
        """
        return Collection((*self.iterable, *other))

    def  __sub__(self, other):
        """ 3
        :param other: collections or iterable object
        :return: return a new Collection containing items that exist in the first collection but not in the other
        """
        return Collection(item for item in self.iterable if item not in (*other,))

    def __len__(self):
        """ 4
        :return: return the length of the Collection .
        """
        return len(self.iterable)

    def __contains__(self, element):
        """ 5
        :param element: the element to check if it's in the collection
        :return:  True or False return the existence of an element in the Collection
        """
        return element in self.iterable

    def __eq__(self, other):
        """ 6
        :param other: another collection to compare
        :return: return the whether all the elements of the two Collection s are equal
        """
        return (*self.iterable,)==(*other,)

    def  __ne__(self, other):
        """ 7
         should be the negation of the equals operator.
        :param other: another collection to compare
        :return: return the whether all the elements of the two Collection s are not equal
        """
        return not self==other

    def __str__(self):
        """ 8
        :return: return a string representation of the elements of the object
        """
        return str(self.iterable)

    def __repr__(self):
        """ 9
        :return: return a programatic representation of the elements of the object.
        """
        return "Collection{}".format(self.iterable)

import json

def enumerate_waze(filename):
    """
    load the dataset from the waze.json file
    :param filename: the name of the JSON file with the data
    :return: A collection with the data from the json file
    """
    with open('waze.json', 'r') as f:
        return Collection(json.load(f))

def clean_noise(c):
    """
     remove any invalid alerts. An alert is considered invalid if it is missing any
     of the following properties: country , reliability , or user
    :param c: The collection to clean
    :return: A new collection object without badly defined data
    """
    return c.filter(lambda x: 'reliability' in x and 'country' in x and 'user' in x)

def complete_values(c):
    """
    :param c: the collection to add type to those that don't have type
    :return: new collection, alerts the do not have a type value should be given a type='other' by default
    """
    new = c.values()
    for i in new:
        if 'type' not in i:
            i['type'] = 'other'
    return Collection(new)

def get_average_reliability(c):
    """
    :param c: A collection including the database of reports
    :return: The average reliability for all alerts in Israel
    """
    reliability = c.filter(lambda data: data['country'] == 'IL').pluck('reliability')
    if len(reliability) == 0:
        return 0
    return reliability.reduce(lambda x, y: x + y) / len(reliability)

def get_top_100_users(c):
    """
    :param c: A collection including the data
    :return: New collection of the top 100 most active users based on the amount of alerts
    they posted sorted from most popular to least
    """
    def count_user(user):
        return len(c.filter(lambda c:c['user']==user))
    return c.pluck('user').unique().sort(key=count_user,reversed=True).take(100)

def get_top_accident_notifyer(c):
    """
    :param c: A collection including the data
    :return: string- name of who posts the most amount of accidents
    """
    temp = c.filter(lambda x: x["type"] == 'accident')
    return get_top_100_users(temp).pluck(key='user').first()

def get_alert_types_by_country(c):
    """
    :param c: A collection including the data
    :return: a collection of alert types and their counts by Country
    """
    return Collection([{"country": i ,"data": Collection([{t:len(c.filter(lambda x:x['country'] == i and x['type'] == t))} for t in c.filter(lambda x:x['country'] == i).pluck('type').unique().values()])} for i in c.pluck(key='country').unique().values()])



