"""
This module will briefly go over the various primative datatypes available in python.
"""

########################################################
#################### Comments ##########################
i#######################################################

# Comments can be written by starting a line with a hash

"""
Multi-line comments can be written
by surrounding text with triple qoutes
"""

'''
This can also be  done with triple single
quotes.  Both are effecitvely defining a string without
assigning the string to a variable.
'''

variable = '''Of coures, you could assign a multi-line string
to a variable.'''

#Then we can print the variable
print variable



########################################################
#################### Strings ###########################
########################################################

"""
As demonstrated above, a string can be defined in a number of ways
"""

# These are all valid ways of defining a string.  The only functional difference I know of
# is that the the triple quotes allow line breaks.
string1 = "Hello World"
string2 = 'Hello World'
string25 = 'Hello\nWorld'
string3 = """Hello World"""
string4 = '''Hello
World'''
string5 = str("Hello World")

# As with any object in python you can list the properties of a string 
print dir(string1)
print dir(str)

# There are many useful functions attached to a python string.  There are too many to explore at once, but
# always check to see if there is a built-in function before writting your own.  Here are a few examples


if "1001".isdigit():
    print "That sure is a number"

if "HelloWorld".isalpha():
    print "Those are letters"

if "hello world" == "Hello World".lower():
    print "That gets rid up upper case letters"


