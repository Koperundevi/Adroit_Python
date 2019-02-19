import re

#Below function does the clean string process using inbuilt function
def cleanString_A(string):
    regex = re.compile('[^a-zA-Z]')
    cleanstring = (regex.sub('',string)).upper()
    return cleanstring

#Below function does the clean string process without using inbuilt function
def cleanString_B(String):
    return ''.join([i.upper() for i in String if i.isalpha()])
    
String = raw_input("Please enter the string to clean:")
print '\nCleaned string using inbuilt function',(cleanString_A(String))
print 'Cleaned string without inbuilt function',(cleanString_B(String))

#To find weight of the provided string based of ASCII code
def getWeight(String):
    properString = cleanString_A(String)
    return sum(map(ord,properString))/len(properString)

String = raw_input('\n\nPlease enter the string to get weight:')
print '\n\nWeight of provided string is: ', (getWeight(String))

#To find no. of occurrence of string 1 in string 2
def getOccurence(String1, String2):
    return sum(String2[i:].startswith(String1) for i in range(len(String2)))

String1 = raw_input("\nPlease enter the sub string to be compared:")
String2 = raw_input("Please enter the main string:")
if 1<=len(String1)<=len(String2):
    print '\n\nNo. of occurrences of `'+String1+ '` in `'+String2+'` is ',(getOccurence(String1,String2))
else:
    print '\nError: Provided input does not match the required condition.\nCondition : 1<=len(str1)<=len(str2)'

