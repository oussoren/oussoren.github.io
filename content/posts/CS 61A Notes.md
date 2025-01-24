+++
author = "max"
title = "CS 106/61A Notes"
date = "2024-12-19"
description = "Intro CS notes"
math = true
tags = ["math", "programming"]
+++
# Lecture notes
Here I will ramble about my brief course in introductory CS :)

## Week 1

### Broad Basics of Computer Science:
A computer program is a collection of code for the computer to run.
The code in a program is divided into smaller, logical units of code called functions,
much as all the words that make up an essay are divided into logical paragraphs.

### Python Syntax:
In python functions are made by writing def function_name (parameter1, parameter2,... parameter n).
The function is called by writing function_name(parameters).

This executes the function with the given parameters and outputs a specific value of some sort
The potential values could be an array, number, a true/false value,
or it could return a string or function.

Often times there are libraries of functions which are given to programmers to use, so it becomes
very important that the functions output and parameters are well understood.

There are certain built-in functions/operations like pow, +, -, //, *, **, sort, sum, %, etc.
which can be interpreted as part of pythons included library of functions

There will be syntax errors--they are inevitable--so you need to know what to do about the errors
Best option is to read the error message. Sometimes the message will hint at the source of the error which
will save a bunch of time.

### Loops and Logic Operations:
Loops essentially iterate a specific line of actions based on certain logic operations. 
Example:
```python
# you can add code with backticks
for i in range(10):
    print(i**2)
```
There may be loops nested in other loops which iterate a separate action within each larger iteration of a
function depending on another logic operation.
Example:
```python
for i in range(10):
    for j in range(10):
        print(i * j, end="\t")
    print()
"""
prints a multiplication table up to 10x10
"""
```
I have only listed for loops, but there are other loops such as while loops which perform similar functions but carry
a different syntax and have varied uses.

While loops evaluate the expression that follows them and runs the body if the test is true/otherwise the code runs the
code that follows the while loop.

Logic operations such as ==, !=, <=, <, >=, >, etc. all evaluate the true/false value of a comparison then perform an
action based on the result of the comparison.

'None' represents a null value

Can also make use of 'not' in logic operations to invert it.
```python
x=21
a=7
while x>7:
    if not x<=a:
        x-=7
"""Yes this code is kinda pointless but it shows how 'not' works"""
```

Another Example of Logic Operations:
```python
x=0
while x<=10:
    x=x+1
    print(x)
"""
Just writes all the values of x from 1-10
"""
```
In this case the logic operation was proceeded by a while statement, but it can also be proceeded by if or elif which
perform an operation depending on the output of the logic operation.

An "expression" is a piece of code that, when it runs, returns a value to that spot in the code. True/false are referred
to as boolean values.

The if statement syntax has four parts — the word "if", boolean test-expression, colon, indented body lines. The if
statement doesn't continue to run on its own, instead it evaluates the expression once, if it's true then it evaluates
the body of the statement, if it's false it simply moves on.

### Coding Style
This is very basic stuff but will be essential in simplifying and optimizing code.

**Indent 4 Spaces:**
Indent 4 spaces whenever defining a function or writing out the body of a loop.

**One Space between items:** always space between items except for the space to the left of a comma and in a function
name and its parenthesis. No space between parenthesis and their contents.

**pass:** 
The word pass in Python means is a placeholder that does nothing. Often pass in the code marks the place where
you add code. Remove the pass when you put your code in, it's just a placeholder.

**def - 2 Blank Lines:**
In code with multiple functions, leave 2 blank lines between defs.

**Single quote:**
Use single quotes when enclosing texts/strings.

**Helper Functions:**
Usually helpers are put first in the program text.

### Misc. Keyboard Shortcuts

A few keyboard tricks for editing code. On the Mac, "command" here refers to the "command" key. On windows it's either
the control key or the windows key.

1. Select multiple lines - tab, shift-tab to indent and un-indent.

2. Select multiple lines - command-/ (command slash) comments and un-comments lines.

3. Control-k "kills" a line of text, deleting it. Works in gmail and all web forms and in a lot of editors.

### Bigger Picture of Programs and How to Decompose a Program

Broadly, Programs are made up by many functions. So if we want to understand the overall function of a program, what we
should do is to break it down into its composite functions. Then we can look at smaller "helper functions" which seem to
solve a sub-problem. By understanding the helper functions, we can understand larger functions and mesh it all together 
to understand the overall program.

**Web Browser:**
Web Browsers are made up of millions of lines of code. It's an inconceivable amount of code, but if we decompose the 
browser into smaller helper functions such as, draw_png_image() or check_ssl_keys(), we can get an idea of how the 
browser executes some of its functions. The idea is that the web browser has been shattered into thousands of smaller 
functions and the coherence of all the smaller functions is what produces the browser the user sees.

### Calling Functions

In Python there are 2 ways of calling functions: call--noun.verb() and call--function_name(parameter).

To define a function we write def function_name or function.name() and we follow this by a colon and indented lines of
code which define the operation of the function. We can then define the value that the function returns when it is 
evaluated by writing return 'value'. 

When a function is called in code, the computer is redirected to read the code within the function before returning to 
the space after the function call.

**Function Pre/Post Conditions:**

-Think careful about each function's boundaries, so that they fit together when called together
-Think about pre/post conditions of each function
-pre: assumptions--*required* before it runs
-post: results after it runs--*promised* after it runs
-Pre/post make the contract of function - i.e. what lines in the function get to assume and what to expect after it runs

## Week 2

### Variables
When setting a variable, all that is needed is to simply state the name of the variable, follow it by an equal sign, 
then add a value that the variable is equal to. On later lines when this variable is called, the program will retrieve 
the stored value of the variable. Variables in CS are different since once declared, they can be set to different values
and when retrieved/called later in the code, the value retrieved will be the most recently declared value of the variable.
In other words, it is not like math where the equal sign sets up a permanent equality.

### Digital Images
Images are broken down into pixels. These pixels store the information for a single color. This data can be stored in a
number of ways, but for now we will focus on RGB. RGB values are stored as the set of 3 values (red, green, blue) with 
ranges for these values from 0 to 255. Pixels are arranged in an x,y coordinate system with origin at the top left and 
positive y in the downwards direction and positive x in the rightwards direction. We can edit an image by uploading it 
into python, then creating a variable for pixel which refers to one pixel inside an image. We can edit the RGB values of
this pixel by using pixel.color=value(from 0-255)

### For Loop
This is probably the single most useful loop. The for loop executes an action or collection of lines FOR each value in 
some collection. In other words it iterates a function n times, where n is the number of items in a collection.

**Syntax:**
```python
for var in collection:
    #use variable here(do something for each iteration)
    return value
```
The value will be returned as the output of the function. Often times we will use range(set) instead of collection. Note:
in python and all code for that matter, indexing begins at index 0. Therefore we must consider this when discussing the
range of a set. I.e. range(10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. If we want to update the value of a variable in a loop
it is common practice to use shorthand forms of certain operations. I.e. x = x + 1 --> x += 1; x = x - 1 --> x-= 1; 
x = x * 1 --> x *= 1.

Example:
```python
def red_channel(filename):
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image
```
Nested for loops: when we have two for loops, we iterate through the entire inner loop for each iteration of the outer loop.

Example related to images:
```python
def darker(filename):
    image = SimpleImage(filename)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image
```
1.
```python
def aqua_stripe(filename):
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width+10, image.height)
    for y in range(image.height):
        for x in range(10):
            out_pixel = out.get_pixel(x, y)
            out_pixel.red = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            out_pixel = out.get_pixel(x+10, y)
            out_pixel.red = pixel.red
            out_pixel.green = pixel.green
            out_pixel.blue = pixel.blue
    return out
"""Takes an image, makes a separate image 10 pixels wider with an aqua stripe on the left 10 pixels of width of the image.
Does this by looping through the first width of pixel"""
```
2.
```python
def mirror2(filename):
    image = SimpleImage(filename)
    out = SimpleImage.blank(image.width * 2, image.height)
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(x, y)
            # left copy
            pixel_left = out.get_pixel(x, y)
            pixel_left.red = pixel.red
            pixel_left.green = pixel.green
            pixel_left.blue = pixel.blue
            # right copy
            # this is the key spot
            # have: pixel at x,y in image
            # want: pixel_right at ??? to write to
    for y in range(image.height):
        for x in range(image.width):
            pixel = image.get_pixel(image.width-1-x, y)
            pixel_left = out.get_pixel(image.width+x, y)
            pixel_left.red = pixel.red
            pixel_left.green = pixel.green
            pixel_left.blue = pixel.blue
    return out
"""Creates a mirror image by copying the original then setting the coordinates of the copy pixel equal to the mirror 
coordinate by taking the width-1(accounting for zero-based indexing) and subtracting the x coordinate"""
```
*Note that both 1 and 2 use helper functions which I have not defined here*

*(i.e. image.get_pixel(x, y), SimpleImage.blank)*

**Math systems:**
In python there are two math systems: int and float. Int includes...well...integers. Wow, shocker. Float includes 
numbers that are not whole numbers(or they are and they just are followed by a .0. Both int and float support the usual
operators: +, -, *, /. These languages follow pemdas, after accounting for pemdas the evaluation goes from left to right.
Int-inputs lead to int-outputs(excpet/below). Presence of a float value makes the whole expression float. Python int 
values do not have a fixed "max"-unusual since must languages do. Float is not actually precise. Even if the answer 
evaluates to a whole number, a float input forces the result to be float. Must pay attention to float vs int because 
when these numbers are used as parameters, their type may cause a function to fail. 

We can convert between int and float values by writing int(value) which will round down to the integer value of the 
input. float(value) will simply attach a dot and zero to the end.

Division: / is unique. a / b returns a float value no matter the input. // will round down(essentially int(a/b))

**How do parameters work:**
The parenthesis part of the function call contains the parameter values for the function, also known as the arguments of
the functions. When a function is called it essentially takes the argument it is given in the call and uses that value
as a stored variable for the body of the function. Functions must be called with the correct number of parameters--
sometimes functions can be called with a blank() this just runs the function with some default parameters that can be 
optionally set. 

## Week 3

### Deciphering Functions

One of the best ways to not only develop functions, but also decipher them is to break them down into certain test cases
where we fix the inputs and outputs and look at/come up with a way for the computer to get from fixed input to fixed 
output.

**Return value pick-off strategy:**
One way we can make sure the function is returning the right value for certain test cases is a pick-off strategy in 
which we have a set number of outcomes and conditions needed to get those outcomes and we simply make an if statement
for eachu condition followed by the appropriate outcome return value.

### Boolean Values
Boolean values are simply true false values. If-test and while-test work with boolean inputs. Booleans are produced by
==, !=, <=, >=, <, >

### Strings
-Very widely used data type

-e.g. 'Hello'

-Strings are basically just sequences of characters

-A string in code is called a "literal"

-Python strings are written on one line with single quotes

-Can also use double quotes if you need a '

**len() function:**
-Returns the number of characters in a string

-Empty string is zero chars

-''

-Valid string with len()=0


-Strings are also zero-based indexed

-String characters/and array values can be accessed by string/array[index]

-Valid from 0 to len-1

-Strings are not editable like other variables

-They are called immutable

-e.g. s='python'

-->s[0]='P'

-s[0]='x'

-->error

-Strings can be combined by the plus operator which simply concatenates the two strings on either side

-uses a new memory to hold the result

-a='hello'

-b='there'

-a+b

-->'hello there'

-a

-->'hello'

A string is made of characters, aka chars. Characters are divided into character classes:

1. Alpha (alphabetic) - e.g. 'a', 'k', 'R', 'Z' .. used to make words

2. Digits - '0' '1' .. '9' used to make numbers

3. Space - space ' ' , newline '\n' tab '\t', - aka "whitespace"

Newline '\n' is char from the return/enter key on keyboard

The backslash form '\XXX` is a way to write special characters, e.g. '\n' is newline

4. Misc - '$' '%' ';' ... miscellaneous chars not in the first 3 categories

There are noun.verb tests s.isalpha() s.isdigit() s.isspace() returning boolean True or False if a char is in a category

There is not a test for "misc", which is just a char which is not alpha or digit or space

For empty string these return False (a weird edge case)

--> 'abc'.isalpha(): True   # Works for multiple chars too


--> '9'.isdigit(): True

### Else, Elif, and More If
So far we know that if we use an if statement it will execute a certain number of lines if the test case is valid.
We will use the if/else form when we have two actions, and we always want to run one action or the other.
*The regular if with 1 action is more common*. 

**Example:**
*not the best*

if some_test:

     pass  # do nothing here
else:

     do_something()

The correct way to do that is with not:

if not some_test:

    do_something()


