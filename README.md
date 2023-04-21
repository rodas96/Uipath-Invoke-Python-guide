# Uipath-Invoke-Python
Basic Guide how to invoke python code into uipath

In this example I made a function in python that receives a text read from a pdf as input and performs various regex to retrieve information using key words like Vendor, "tax amount", "Date", etc to register the values in front of it since the pdf files that I'm reading are unsctructured. So inicially my function in python was returning a dictionary((Key)String,(Value) string) after researching and trying out I found out that you can't return lists, dictionaries or arrays. Only simple data types like int or a string. So If you planning to return one of those you will need to parse the dictionary to json in your python function.

So basically you will need to install the python activities <img width="30" alt="image" src="https://user-images.githubusercontent.com/108375741/233706216-47358f61-21bd-4bfc-9d77-9f81423d2a3e.png">



