
'''Implementation of an interpreter in python,
for a simple XML -based programming language
for Inter Arithmetics.'''

import xml.etree.cElementTree as ET 
mytree = ET.parse('C:\\Users\\siva.dasika\\Documents\\Test\\test1.xml')
myroot = mytree.getroot()
my_dict = {}
#Prints variable
def print_var(x1, dictionary):
    try:
        num1 = int(dictionary[x1])
    except:
        if x1.isnumeric():
            num1 = x1
    return num1


# Returns sum of two numbers
def sum(x1,x2,dictionary):
    try:
        num1 = int(dictionary[x1])
        num2 = int(dictionary[x2])
    except:
        if x1.isnumeric():
            num1=x1
        if x2.isnumeric():
            num2=int(x2)    
    total_sum = num1 + num2
    return total_sum


#Looping through root element
for item in myroot:
    if item.tag =="var":    
        try:
            #Check if variable has a value
            if item.attrib["value"]:               
                my_dict[item.attrib["name"]]= item.attrib["value"]
        except:           
            my_dict[item.attrib["name"]]= ""

    if item.tag=="add":
        total = sum(item.attrib['n1'], item.attrib['n2'], my_dict)
        my_dict[item.attrib['to']]= total
    
    if item.tag=="print":  
        final_value = print_var(item.attrib['n'], my_dict) 
        print("Final value is: "+ str(final_value))

     
