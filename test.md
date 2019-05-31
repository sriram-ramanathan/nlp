### **Project Title**

Attorney Extraction from File Notes

### **Description**

This code will extract attorney\'s or legal representative name if
mentioned in file notes. The code uses two methods for attorney\'s name
extraction. Attorney\'s name are followed by some generic pattern like
\"law firm of\", \"represented by\". So the first method uses this
pattern for extraction, this method will be more accurate in extracting
the attorney\'s name but since it is heavily dependent on exact pattern
might not give exhaustive list. The other method is based on keywords
(related to attorney) like law, legal, handled, represent, it will
extract all keywords surrounding this keywords.It will be more
exhaustive but it might be less precise.

###  **Dependencies**

python library : pandas,re\
input file type: .xlsx

###  **How to run?**

**1. Run from Command Line**

i\. Open the .py file\
ii.Define path, filename & columns which has file notes text

![User Inputs](User%20Inputs.jpg)

iii\. Also change the attorney extraction method in main() function (
available functions are attorney\_extraction\_pattern\_based,
attorney\_extract\_hybrid1, attorney\_extract\_hybrid2)

![Function Selection](Func%20Selection.jpg)

iv\. Run the code, using Jupyter Notebook: %run \"\<.py file name\>.py\"\
or you can run from command prompt

![Function Call](Func%20Call.jpg)

v\. Output file will be exported as \"attorney\_extracted\" in the given
path. \"attorney\_name\" column will have the attorney\'s name against
the file notes

![Output](Output.jpg)

**2. Use functions from the module**

from Attorney\_Extraction\_v2 import \*

data = \'\'File Note Created By: Emily Beaupre\
Date File Note Created: Date Email Received From law firm of\
Sanders Llc Sender: RE: Thomas Hickey Emily,\
Please see below for answers to your questions. Let me know if you need
anything else.\
\[Damien Hess\] Conservative treatments only. Diagnostic testing ?
\[Damien Hess\] No diagnostic testing required for this injury.\
Law firm of ABC Associates firm What is the Tx plan? \[Damien Hess\]
Continue conservative treatments.\
Any lost time from play? \[Damien Hess\] Player has not lost any playing
time due to this injury. Thank you for your time!\"\
\'\'\'

clean\_text = remove\_punctutation(data)\
clean\_text = cleanhtml(clean\_text)\
attorney\_name = attorney\_extract\_hybrid1(clean\_text)

Output: \[\'Sanders Llc ,ABC Associates\'\]

###  **Author**

Bishu Giri (bishu.giri\@chubb.com)

### **Version History**

0.1 Initial Release

### **License**

This code is for exclusive use by Chubb users
