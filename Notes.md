// Notes.md

# CSE3120 - Object Oriented Programming 1 - Notes

## Definitions 

__Object-oriented Analysis (00A)__ is tge process of looking at a problem, system or task and identifying the objects and interactions between those objects. It answers the question, what needs to be done. 
    * This term is often called a _use case analysis_.

__Object oriented design (00D)__ is the process of converting the identified objects and interactions from 00A into object behaviours. It answers the question, _how things need to be done_.

__Object oriented programming (00P)__ is the process of implementing the outcomes of 00D and 00A into a digital objects that interact within a program. It uses class templates to create objects that have attributes and methods. 

A __Class__ is a model of an object. Classes contain _attributes_ and _behaviors_ which are inherited when objects are _instantiated_ from the class. Another definition of a class is a blueprint or a template.

* An __Attribute__ is a property or characteristic an object possess. This is like a variable, which the object can have different values for a property, but all objects instantiated from the same class inherit the same attributes. 

* A __Behavior__ is an action that can be performed on the data within the object, Behaviors are formally named _Methods_ and are written in the same manner as a function. Therefore, methods can accept arguments into parameters and return values.
* Methods can accept and return data to an external component of the program. It can also access all internal attributes of the object. 
    * NOTE: An object never has to pass an attribute into a parameter. 
* Objects from a class always have at least one parameter, ```self```, which indicates that the function is referencing the current object.
    * __Constructers__ are methods that provide the object with the default set of attributes. In python, it is ```self.__init__(self)```. Constructors create their objects from the class template with values within the attributes when an objet is constructed, data can be passed through parameters into that object's attributes.
    * In general, all attributes of th object should be present in the Constructor, even if there default value is None.
  
```python
from random import randint
class Die:
    """
    A die object that can be rolled for a number
    """

    # Constructor
    def __init__(self,sides):
        # attributes of the object
        self.max_num = sides 
        self.rolled_value = 0

    # Methods
    def rollDice(self):
        #update the rolled value
        self.rolled_value = randint(1, self.max_num)
    
    def getDiceRoll(self):
        # return the roll value
        return self.rolled_value 

DIE_1 = Die(6)
DIE_1.rollDice()
print(DIE_1.getDiceRoll())

DIE_2 = Die(20)
```

An __object__ is a unique set of data and functions instantiated from a class. An object accesses attributes and methods using _dot notation_, which identifies the object, then the attribute or method.

```
<object name>.<attribute name> --> VALUE
<object name>.<method name>(arguments) --> METHOD
```

## Why OOP? (This section is really important)
1.__Encapsulation__ is the process of protecting or hiding data and data processes through the implementation of an _interface_. This interface is often a collection of methods such as setter (modifier) methods and getter (accessor) methods that other objects can interact with.
    * NOTE: In most programming languages, attributes are _private_ by default; however in python, they are _public_ by default. 
    * A television encapsulate all hardware and software into a small box which the user interfaces with through a series of buttons on the devices or on a remote control.
    * It is important to emphasize the need for setter and getter methods and how each attribute within a class should only be accessible through these methods.
2. __Abstraction__ is the process of setting the level of detail and complexity to what is appropriate for the given task. A driver only needs to interact with the steering, accelerator, brakes and the signals of the car to drive. But a mechanic has a much more complex understanding of the car in order to repair and maintain it. Therefore, the mechanic's abstraction of the car is more complex than the driver
    * To calculate a student's average, one requires the student ID, courses taken, and grades received. While a person has many more traits (i.e. height, hair color, ethnicity, postal code, etc.), they are not needed for the purpose of the calculation and are therefore omitted. 
3. __Aggregation__ is the process of grouping objects together. Objects exist independently of each other.
    * The students in this classroom are an aggregate. If a student is missing, it does not change the lesson progression. 
4. __Composition__ is the process of creating a complex object from a collection of smaller objects.
    * A bicycle is composed of two wheels, a chain, handlebars, frame, pedals, etc. Any one of these objects, when broken, will affect the performance of the bicycle. If enough objects within the bicycle are missing/damaged, the bicycle will no longer function.
    * A pokemon will have type objects, and move objects in addition to their attributes. It cannot battle without a type or move.



    
