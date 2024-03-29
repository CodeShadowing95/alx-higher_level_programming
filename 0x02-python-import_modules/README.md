<h1>Python - import & modules</h1>
<h2>General</h2>
<h3>Why Python programming is Awesome?</h3>
Created by Guido van Rossum and released in 1991, Python is now an advanced, general-purpose programming language.

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java.

This makes python a very popular programming language used for desktop stand-alone applications or online/ web applications as well as small or large scales development projects.</br>

Import a function from a file and print the result of the addition 1+2=3</br>
<ul>
<li>
To import a function from a file, write <code>import</code> followed by the name of the file(without .py), and then the function: <code>import filename.function</code>
</li>
<li>
To use imported functions, if the name of the module has been specified at first place, write simply the name of the function
</li>
<li>
To create a module, create a file with the extension <code>.py</code> that contains some functions, that will be used
</li>
<li>
When running a Python module with <code>python module_name.py arguments</code>, the code in the module will be executed, just as if we imported it, but with the <code>__name__</code> set to <code>__main__</code>. That means that by adding this code at the end of our module like:</br>
<code>if __name__ == '__main__':</code></br>
<code>____import sys</code></br>
<code>____fib(int(sys.argv[1]))</code></br>
we can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the "main" file</br>
<code>$ python fibo.py 50</code></br>
<code>0 1 1 2 3 5 8 13 21 34</code></br>
If the module is imported, the code is not run:</br>
<code>>>> import fibo</code></br>
<code>>>> </code></br>
This is often used either to provide a convenient user interface to a module, or for testing purposes (running the module as a script executes a test suite).
</li>
<li>
The built-in function <code>dir()</code> is uesd to find out which names (functions names) a module defines. It returns a sorted list of strings that retrieves all the names of functions in the modules and the <code>__name__</code> of the module
</li>
<li>
To prevent code in the script from being executed when imported, the package author should provide an explicit index of the package: if a package's <code>__init__.py</code> code defines a list named <code>__all__</code>, it is taken to be list of module names that should be imported when <code>from package import * </code> is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released.
</li>
<li>
To use command line arguments with Python programs, import the module <code>sys</code>. The arguments appended, when executing the program are stored in the <code>sys</code> module's <code>argv</code> attribute as a list</br>
<code>>>> import sys</code></br>
<code>>>> python demo.py one two three</code></br>
<code>>>> print(sys.argv)</code></br>
<code>['demo.py', 'one', 'two', 'three']</code>
</li>
</ul></br>
<h3>Examples</h3>
0- program that imports the function <code>def add(a, b): </code> from the file <code>add_0.py</code> and prints the result of the addition <code>1 + 2 = 3</code></br>
1- program that imports functions from the file <code>calculator_1.py</code>, does some Maths, and prints the result</br>
2- program that prints the number of and the list of its arguments</br>
3- program that prints the result of the addition of all arguments</br>
4- program that prints all the names defined by the compiled module <code>hidden_4.pyc</code></br>
5- program that imports the variable <code>a</code> from the file <code>variable_load_5.py</code> and prints its value</br>
6- program that imports all functions from the file <code>calculator_1.py</code> and handles basic operations</br>
7- program that prints <code>#pythoniscool</code>, in the standard output</br>
8- Bytecode#3</br>
9- program that prints the alphabet in uppercase</br>
