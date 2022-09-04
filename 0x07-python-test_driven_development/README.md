<h1>Python - Test-driven development</h1>
<h2>General</h2>
<h3>Why Python programming is awesome</h3>
Created by Guido van Rossum and released in 1991, Python is now an advanced, general-purpose programming language.

It is designed to stress on code readability by utilizing substantial white space and simplicity as it allows programmers to write models and conceptions in less amounts of code lines compared to other languages like C++ or Java.

This makes python a very popular programming language used for desktop stand-alone applications or online/ web applications as well as small or large scales development projects.</br>
<h3>What's an interactive test</h3>
<p>An interactive test is a test (from the doctest module) that searches for pieces of text that look like interactive Python sessions in docstrings, and executes those sessions to verify that they work exactly as shown.</p></br>

<h3>Why tests are important?</h3>
<p>We all make mistakes and if left unchecked, some of these mistakes can lead to failures or bugs that can be very expensive to recover from. Testing our code helps to catch these mistakes or avoid getting them into production in the first place. Testing therefore is very important in software development. Used effectively, tests help to identify bugs, ensure the quality of the product and to verify that the software does what it is meant to do.</p></br>

<h3>How to write Docstrings to create tests</h3>
<p>We should write these tests in Docstrings like interactive Python sessions like this:</br>
"""</br>
This is the "example" module.</br>
</br>
The example module supplies one function, factorial().  For example,</br>
</br>
>>> factorial(5)</br>
120</br>
"""
</p>

<h3>How to write documentation for each module and function</h3>
<p>We should write these documentation inside each module and function like specified above.</p></br>

<h3>What are the basic option flags to create tests?</h3>
<p>There are many different options flags to create tests like:</p>
<ul>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.DONT_ACCEPT_TRUE_FOR_1">doctest.DONT_ACCEPT_TRUE_FOR_1</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.DONT_ACCEPT_BLANKLINE">doctest.DONT_ACCEPT_BLANKLINE</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.NORMALIZE_WHITESPACE">doctest.NORMALIZE_WHITESPACE</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.ELLIPSIS">doctest.ELLIPSIS</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.IGNORE_EXCEPTION_DETAIL">doctest.IGNORE_EXCEPTION_DETAIL</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.SKIP">doctest.SKIP</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.COMPARISON_FLAGS">doctest.COMPARISON_FLAGS</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.REPORT_UDIFF">doctest.REPORT_UDIFF</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.REPORT_CDIFF">doctest.REPORT_CDIFF</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.REPORT_NDIFF">doctest.REPORT_NDIFF</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.REPORT_ONLY_FIRST_FAILURE">doctest.REPORT_ONLY_FIRST_FAILURE</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.FAIL_FAST">doctest.FAIL_FAST</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.REPORTING_FLAGS">doctest.REPORTING_FLAGS</a></li>
<li><a href="https://docs.python.org/3.4/library/doctest.html#doctest.register_optionflag">doctest.register_optionflag(name)</a></li>
</ul></br>

<h3>How to find edges cases</h3>
<p>An "edge" has two meanings, and both are relevant when it comes to edge cases. An edge is either an area where a small change in the input leads to a large change in the output, or the end of a range. </br>So, to identify the edge cases of an algorithm, first look at the input domain. Its edge values could lead to edge cases of the algorithm. Secondly, look at the output domain, and look back at the input values that might create them. This is less commonly a problem with algorithms, but it helps find problems in algorithms that are designed to generate output which spans a given output domain. E.g. a random-number generator should be able to generate all intended output values. </br>For example, the algorithm takes a string and an integer as input and does some sorting of the characters of the string. </br>Here we have:</br>
<pre>
<b>String</b> with some known special cases:
<ul>
<li>Empty string</li>
<li>Long string</li>
<li>Unicode string (special characters)</li>
<li>If limited to a specific set of characters, what happens when some are not in the range</li>
<li>Odd/even length string</li>
<li>Null (as argument)</li>
<li>Non-null terminated</li>
</ul>

<b>Integer</b> with known special cases:
<ul>
<li>0</li>
<li>Min/MaxInt</li>
<li>Negative/Positive</li>
</ul>

<b>Sort algorithm</b> that could fail in the following boundary cases:
<ul>
<li>Empty input</li>
<li>1 element input</li>
<li>Very long input (maybe of length max(data type used for index))</li>
<li>Garbage inside the collection that will be sorted</li>
<li>Null input</li>
<li>Duplicate elements</li>
<li>Collection with all elements equal</li>
<li>Odd/even length input</li>
</ul>

Then, take all these cases and create a long list trying to understand how they overlap. Ex:
<ul>
<li>Empty string case covers the empty collection case</li>
<li>Null string == null collection</li>
<li>etc...</li>
</ul>
</pre>
</p></br>

<h3>Examples</h3>
0- function that adds 2 integers</br>
1- function that divides all elements of a matrix</br>
