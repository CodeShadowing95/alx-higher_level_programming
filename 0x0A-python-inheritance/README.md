<h1>Python - Inheritance</h1>
<h2>Why Python is Awesome?</h2>
Created by Guido van Rossum and released in 1991, Python is now an advanced, general-purpose programming language.

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java.

This makes python a very popular programming language used for desktop stand-alone applications or online/ web applications as well as small or large scales development projects.</br>
<h2>General</h2>
a <b>superclass</b> or <b>parentclass</b> is a class that is being inherited from.</br></br>
a <b>subclass</b> is a class that is inheriting from a parent class or superclass.</br></br>
To list all attributes and methods of a class or instance, use the function <code>dir</code>.</br></br>
An instance can have have new attributes through the inheritance (in the method <code>__init__</code>).</br></br>
A class inherits from another class or base class by defining the base class as argument when declaring the class</br></br>
To define a class with multiple base classes, we define these base classes as arguments of the class</br></br>
The default class every class inherit from is the class <code>Object</code>.</br></br>
We can override a method or attribute inherited from the base class by passing less or more arguments in the method overridden</br>
<code>
class Plus:
    def add(self, a, b):
        return a + b

class Plus1(Plus):
    def add(self, a, b, c):
        return a + b + c
</code></br>
or by changing the type of the attribute</br></br>
By heritage, the instance attributes and methods are available in the subclasses</br></br>
The purpose of inheritance is to provide to subclasses all the attibutes and methods from a parent class</br></br>
The built-in function <code>isinstance</code> is used to check an instance's type. It checks if an object belongs to a specific class: <code>isinstance(obj, int)</code> will be True only if <code>obj.__class__</code> is int or some class derived from int.
The built-in function <code>issubclass</code> is used to check class inheritance. It checks if an object is inheriting a specific class: <code>issubclass(bool, int)</code> is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.</br>
The built-in function <code>type</code> prints the type of an object.</br>
The built-in function <code>super</code> is used to call the <code>__init__</code> method from the base class, essentially calling any overridden method of the base class.</br>
<h2>Examples</h2>
0- get the list of available attributes and methods of an object</br>