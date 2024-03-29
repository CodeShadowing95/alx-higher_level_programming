<h1>Python - Input/Output</h1>
<h2>Why Python is Awesome?</h2>
Created by Guido van Rossum and released in 1991, Python is now an advanced, general-purpose programming language.

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java.

This makes python a very popular programming language used for desktop stand-alone applications or online/ web applications as well as small or large scales development projects.</br>
<h2>General</h2>
<ul>
<li>
To open a file, use the instruction <code>open(filename, access_mode, encoding, buffering)</code>, where <code>filename</code> is the path to the file or, if the file is in the working directory, the filename of the file; <code>access_mode</code> is a string value that determines how the file is opened; <code>buffering</code> is an integer value used for optional line buffering
</li>
<li>
To write text in a file, use the <code>write</code> method of the file. But the file must first be opened with access mode <code>w</code>: <code>filename.write("something")</code>
</li>
<li>
To read the full content of a file, use the <code>read</code> method of the file: <code>filename.read()</code>
</li>
<li>
To read a file line by line, use the <code>readLine</code> method of the file: <code>filename.readline()</code>
</li>
<li>
To move the cursor in a file, use the <code>seek</code> method of the file: <code>f.seek(position, whence)</code>, where whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point
</li>
<li>
To make suze a file is closed after using it, use the <code>close</code> method of the file: <code>f.close()</code>
</li>
<li>
The <code>with</code> statement ensures the file handle is closed once the
reading or writing has been completed: <code>with open(filename, mode, encoding) as f: ...</code>
</li>
<li>
JSON or JavaScript Object Notation is a popular data format used for representing structured data. It's commonly used to transmit and receive data between a server web application in JSON format.
</li>
<li>
Serialization is the process of taking a Python data hierarchies, and convert them to JSON string representations
</li>
<li>
Deserialization is the process of reconstructing the data or object from the JSON string representation
</li>
<li>
To convert a Python data structure to a JSON string, import first the module json and use the following syntax: <code>json.dumps(data)</code>
</li>
<li>
Convert a Python data stucture to a JSON string, using the <code>json.dumps(data)</code> method
</li>
<li>
Convert a JSON string to a Python data structure, using the <code>json.loads(data)</code> method
</li>
</ul></br>
<h2>Examples</h2>
0- function that reads a text file and prints it to stdout</br>
1- function that writes a string to a text file and returns the number of characters written</br>
2- function that appends a string at the end of a text file and returns the number of characters added</br>
3- function that returns the JSON representation of an object (string)</br>
4- function that returns an object (Python data structure) represented by a JSON string</br>
5- function that writes an Object to a text file, using a JSON representation</br>
6- function that creates an Object from a "JSON file"</br>
7- script that adds all arguments to a Python list, and then save them to a file</br>
8- function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object</br>
9- create a class student(first_name, last_name, age), and a method <code>to_json</code> that retrieves a dictionary representation of a Student instance</br>
10- based on 9-, modify the method <code>to_json</code> by adding the parameter attrs, that is a list of strings. Only attribute names contained in this list must be retrieved, otherwise all attributes must be retrieved</br>
11- based on 10-, define a method that replaces all attributes of the Student instance</br>
12- function that returns a list of lists of integers representing the Pascal's triangle of a number n</br>
13- insert a line of text to a file, after each line containing a specific string</br>
14- script that read <code>stdin</code> line by line and computes metrics</br>
