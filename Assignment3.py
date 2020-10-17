#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:49:54 2020

@author: bonzilla
"""


'''
Assignment #3

1. Add / modify code ONLY between the marked areas (i.e. "Place code below"). Do not modify or add code elsewhere.
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 03_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch in Github
8. Use the test cases to infer requirements wherever feasible


'''
import csv, json, math, pandas as pd, requests, unittest, uuid

# ------ Create your classes here \/ \/ \/ ------

# Box class declaration below here
 
class Box:
    """
    Represents a box.
    Attributes: length, width
    """
    def __init__( self, length, width ):
        self.length = length
        self.width = width
    def render( self ):
        print( '*' * self.length )
        for line in range( 1, self.length ):
            print( '*'+' ' * ( self.length-2 ) +'*' )
        print( '*' * self.length )
    def get_length( self ):
        return self.length
    def get_width( self ):
        return self.width
    def invert( self ):
        l = self.length
        self.length = self.width
        self.width = l
    def get_area( self ):
        return self.length * self.width
    def get_perimeter( self ):
        return 2*self.length + 2*self.width
    def double( self ):
        self.width = 2*self.width
        self.length = 2*self.length
        return Box( self.length, self.width )
    def __eq__( self,other ):
        return self.length == other.length and self.width == other.width
    def print_dim( self ):
        print( 'length =', self.length, '\nwidth =', self.width )
    def get_dim( self ):
        return ( self.length, self.width )
    def combine( self,other ):
        self.length = self.length + other.length
        self.width = self.width + other.width
        return Box( self.length, self.width )
    def get_hypot( self ):
        return math.sqrt( self.width**2 + self.length**2 )

# MangoDB class declaration below here

class MangoDB:
    """
    Dictionary of Dictionaries: way better than MongoDB
    """
    def __init__( self ):
        self.database = { 'default' : {
            'version':1.0,
            'db':'mangodb',
            'uuid':str( uuid.uuid4() )
            } }
    def add_collection( self, collection_name ):
        self.database[ collection_name ] = {}
    def update_collection( self, collection_name, updates ):
        #allows the caller to insert new items into a collection
        self.database[ collection_name ].update( updates )
    def remove_collection( self, collection_name ): 
        #allows caller to delete a specific collection by name and its associated data
        self.database.pop( collection_name )
    def list_collections( self ): 
        #displays a list of all the collections
        print( self.database.keys() )
    def get_collection_size( self,collection_name ): 
        #finds the number of key/value pairs in a given collection
        contents = self.database[ collection_name ]
        print( len( contents ) )
        return len( contents )
    def to_json( self,collection_name ): 
        #that converts the collection to a JSON string
        contents_json = json.dumps( self.database[ collection_name ] )
        return contents_json
    def wipe( self ): 
        #that cleans out the db and resets it with just a default collection
        self.database = { 'default' : {
            'version':1.0,
            'db':'mangodb',
            'uuid':str( uuid.uuid4() )
            } }
    def get_collection_names( self ): 
        #that returns a list of collection names
        return self.database.keys()
        
        
# ------ Create your classes here /\ /\ /\ ------





def exercise01():

    '''
        Create an immutable class Box that has private attributes length and 
        width that takes values for length and width upon construction 
        (instantiation via the constructor). Make sure to use Python 3 
        semantics. Make sure the length and width attributes are private and 
        accessible only via getters. Immutable here means that any change to 
        its internal state results in a new Box being returned.
        
        Remember, here immutable means there are no setter methods. 
        States can change with the methods required below i.e. combine(), invert().
        
        In addition, create...
        X A method called render() that prints out to the screen a box made 
        with asterisks of length and width dimensions
        X A method called invert() that switches length and width with each other
        X Methods get_area() and get_perimeter() that return appropriate 
        geometric calculations
        X A method called double() that doubles the size of the box. 
        Hint: Pay attention to return value here
        X Implement __eq__ so that two boxes can be compared using ==. 
        Two boxes are equal if their respective lengths and widths are identical.
        X A method print_dim that prints to screen the length and width 
        details of the box
        X A method get_dim that returns a tuple containing the length and 
        width of the box
        X A method combine() that takes another box as an argument and 
        increases the length and width by the dimensions of the box passed in
        X A method get_hypot() that finds the length of the diagonal that cuts 
        throught the middle

        In the function exercise01():
        X Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to 
        variables box1, box2 and box3 respectively 
        X Print dimension info for each using print_dim()
        X Evaluate if box1 == box2, and also evaluate if box1 == box3, print 
        True or False to the screen accordingly
        X Combine box3 into box1 (i.e. box1.combine())
        - Double the size of box2
        - Combine box2 into box1
        - Using a for loop, iterate through and print the tuple received from 
        calling box2's get_dim()
        - Find the size of the diagonal of box2

'''

    # ------ Place code below here \/ \/ \/ ------
    
    box1 = Box( 5,10 )
    box2 = Box( 3,4 )
    box3 = Box( 5,10 )
    box1.print_dim()
    box2.print_dim()
    box3.print_dim()
    res1 = box1.__eq__( box2 )
    res2 = box1.__eq__( box3 )
    print( res1 )
    print( res2 )
    box1.combine( box3 )
    box2.double()
    box1.combine( box2 )
    for dim in box2.get_dim():
        print( dim )
    box2.get_hypot()

    return box1, box2, box3

    # ------ Place code above here /\ /\ /\ ------


def exercise02():
    '''
    Create a class called MangoDB. The MangoDB class wraps a dictionary of 
    dictionaries. At the the root level, each key/value will be called a 
    collection, similar to the terminology used by MongoDB, an inferior 
    version of MangoDB ;) A collection is a series of 2nd level key/value 
    paries. The root value key is the name of the collection and the value is 
    another dictionary containing arbitrary data for that collection.

    For example:

        {
            'default': {
            'version':1.0,
            'db':'mangodb',
            'uuid':'0fd7575d-d331-41b7-9598-33d6c9a1eae3'
            },
        {
            'temperatures': {
                1: 50,
                2: 100,
                3: 120
            }
        }
    
    The above is a representation of a dictionary of dictionaries. Default and 
    temperatures are dictionaries or collections. The default collection has a 
    series of key/value pairs that make up the collection. The MangoDB class 
    should create only the default collection, as shown, on instantiation 
    including a randomly generated uuid using the uuid4() method and have the 
    following methods:
        - display_all_collections() which iterates through every collection 
        and prints to screen each collection names and the collection's content 
        underneath and may look something like:
            collection: default
                version 1.0
                db mangodb
                uuid 739bd6e8-c458-402d-9f2b-7012594cd741
            collection: temperatures
                1 50
                2 100 
        - add_collection(collection_name) allows the caller to add a new 
        collection by providing a name. The collection will be empty but will 
        ave a name.
        - update_collection(collection_name,updates) allows the caller to 
        insert new items into a collection i.e. 
                db = MangoDB()
                db.add_collection('temperatures')
                db.update_collection('temperatures',{1:50,2:100})
        - remove_collection() allows caller to delete a specific collection by 
        name and its associated data
        - list_collections() displays a list of all the collections
        - get_collection_size(collection_name) finds the number of key/value 
        pairs in a given collection
        - to_json(collection_name) that converts the collection to a JSON string
        - wipe() that cleans out the db and resets it with just a default collection
        - get_collection_names() that returns a list of collection names


        Make sure to never expose the underlying data structures

        For exercise02(), perform the following:

        - Create an instance of MangoDB
        - Add a collection called testscores
        - Take the test_scores list and insert it into the testscores 
        collection, providing a sequential key i.e 1,2,3...
        - Display the size of the testscores collection
        - Display a list of collections
        - Display the db's UUID
        - Wipe the database clean
        - Display the db's UUID again, confirming it has changed
    '''

    test_scores = [99,89,88,75,66,92,75,94,88,87,88,68,52]

    # ------ Place code below here \/ \/ \/ ------
    
    a_mango = MangoDB()
    a_mango.add_collection( 'testscores' )
    a_mango.update_collection( 'testscores', 
                              {1:99,2:89,3:88,4:75,5:66,6:92,7:75,8:94,9:88,
                               10:87,11:88,12:68,13:52})
    a_mango.get_collection_size('testscores' )
    a_mango.list_collections()
    a_mango.database[ 'default' ][ 'uuid' ]
    a_mango.wipe()
    a_mango.database[ 'default' ][ 'uuid' ]

    # ------ Place code above here /\ /\ /\ ------


def exercise03():
    '''
    1. Avocado toast is expensive but enormously yummy. What's going on with 
    avocado prices? Read about avocado prices 
    (https://www.kaggle.com/neuromusic/avocado-prices/home)
    2. Load the avocado.csv file included in this Githb repository and display 
    every line to the screen
    3. Open the file name under csv_file
    4. The reader should be named reader
    5. Use only the imported csv library to read and print out the avacodo file
    
    '''

    # ------ Place code below here \/ \/ \/ ------
    from contextlib import closing
    
    daturl = 'https://raw.githubusercontent.com/SmilodonCub/DATA602/master/avocado.csv'
    
    with closing(requests.get(daturl, stream=True)) as r:
        f = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            print(row)
        

    # ------ Place code above here /\ /\ /\ ------

class TestAssignment3(unittest.TestCase):
    def test_exercise01(self):
        print('Testing exercise 1')
        b1, b2, b3 = exercise01()
        self.assertEqual(b1.get_length(),16)
        self.assertEqual(b1.get_width(),28)
        self.assertTrue(b1==Box(16,28))
        self.assertEqual(b2.get_length(),6)
        self.assertEqual(b2.get_width(),8)
        self.assertEqual(b3.get_length(),5)
        self.assertEqual(b2.get_hypot(),10)
        self.assertEqual(b1.double().get_length(),32)
        self.assertEqual(b1.double().get_width(),112)
        self.assertTrue(6 in b2.get_dim())
        self.assertTrue(8 in b2.get_dim())
        self.assertTrue(b2.combine(Box(1,1))==Box(7,9))

    def test_exercise02(self):
        print('Testing exercise 2')
        exercise02()
        db = MangoDB()
        self.assertEqual(db.get_collection_size('default'),3)
        self.assertEqual(len(db.get_collection_names()),1)
        self.assertTrue('default' in db.get_collection_names() )
        db.add_collection('temperatures')
        self.assertTrue('temperatures' in db.get_collection_names() )
        self.assertEqual(len(db.get_collection_names()),2)
        db.update_collection('temperatures',{1:50})
        db.update_collection('temperatures',{2:100})
        self.assertEqual(db.get_collection_size('temperatures'),2)
        self.assertTrue(type(db.to_json('temperatures')) is str)
        self.assertEqual(db.to_json('temperatures'),'{"1": 50, "2": 100}')
        db.wipe()
        self.assertEqual(db.get_collection_size('default'),3)
        self.assertEqual(len(db.get_collection_names()),1)
        
    def test_exercise03(self):
        print('Exercise 3 not tested')
        exercise03()
     

if __name__ == '__main__':
    unittest.main()