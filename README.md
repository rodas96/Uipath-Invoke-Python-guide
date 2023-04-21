# Uipath-Invoke-Python
Basic Guide how to invoke python code into uipath

In this example I made a function in python that receives a text read from a pdf as input and performs various regex to retrieve information using key words like Vendor, "tax amount", "Date", etc to register the values in front of it since the pdf files that I'm reading are unsctructured. So inicially my function in python was returning a dictionary((Key)String,(Value) string) after researching and trying out I found out that you can't return lists, dictionaries or arrays. Only simple data types like int or a string. So If you planning to return one of those you will need to parse the dictionary to json in your python function.

So basically you will need to install the python activities in the manage packages <img width="50" alt="image" src="https://user-images.githubusercontent.com/108375741/233706216-47358f61-21bd-4bfc-9d77-9f81423d2a3e.png"> <img width="150" alt="image" src="https://user-images.githubusercontent.com/108375741/233706339-f8989702-8f2d-4643-bcdb-dd1c45d91c1b.png">.

After that go to your activities panel and you should find those


<img width="140" alt="image" src="https://user-images.githubusercontent.com/108375741/233706515-52eefb0e-672f-4d4c-8249-d16f384c8a76.png">.



In order to invoke your code youl need to drag it by this order - python scope->load python script->Invoke python Script->Get python object



<img width="288" alt="image" src="https://user-images.githubusercontent.com/108375741/233712466-9130f870-28cf-4336-80b5-271c9d2f1853.png">



1st Step is using the python scope - You will define the path for python.exe,your version of python, your target, and the working file that your uipath project is.

<img width="629" alt="image" src="https://user-images.githubusercontent.com/108375741/233706958-c4b4a536-a6ac-49ad-b1ec-c3ee73cc3063.png">

Here it gets tricky, you don't want to run the python version 3.10 or higher, in my case only the 3.7 and 3.8 are possible to run in uipath, so if you want to invoke python code make sure you installed 3.8 or lower otherwise won't work you can check by typing this in the cmd: 
<img width="376" alt="image" src="https://user-images.githubusercontent.com/108375741/233707786-a19defdf-f378-41fe-ad06-3527c4e5c8c6.png">
By using where python command you can see the path, you will copy the first one and put in the path property of the python scope, select your version and your target and in the working folder you put the folder you are working on and my advice put the .py file in it.


2nd Step - You are going to Load your python script basically you are bringing the function to the uipath

<img width="458" alt="image" src="https://user-images.githubusercontent.com/108375741/233709118-7ab0ce22-6e1a-4dc2-bcef-cff917146c2b.png">

In the file you are going to put the path to the .py file something like this "C:\Users\name\Spot\Documents\UiPath\PythonExample\regexScript.py"
And then you create a variable to receive the output of the loaded script in my case is regexScript.

3rd Step - Here you are going to Invoke your function where you will pass the inargument in my case the pdf file that was readed I holded in a var called pdfText

Here you will put the name of the function that you wrote
<img width="259" alt="image" src="https://user-images.githubusercontent.com/108375741/233709967-8f91448a-7861-42d0-ade6-78199c40d833.png">
<img width="611" alt="image" src="https://user-images.githubusercontent.com/108375741/233710186-64bfbfea-7ba0-4667-85c2-ab23d831a6b2.png">

And in the properties

The input parameter is type of IEnumerable object, so in my case I use a string that is holded in the var pdfText you have to use the {pdfText}, for astring {"yourstring"}, int {3}, etc.
INSTANCE is the python object that was returned by the load script activity in this case regexScript and then create another variable to hold the output in this case is regexOuput-



<img width="388" alt="image" src="https://user-images.githubusercontent.com/108375741/233709582-a11afa25-72fd-4b91-9a73-9bec0869f0ce.png">


Final step :D - Just converting the python object to .net 

The input arg corresponds to the output of your function from the invoke method in this case regexOuput and the outargument in this case is finalOutput that now you have your return value from python function in the finalOutput variable

<img width="331" alt="image" src="https://user-images.githubusercontent.com/108375741/233711365-4c8ddf42-1022-405f-bbce-0abb8fe1aea3.png">

Since you returned a json from your python function and now you have a json object in the finalOuput you can use this command to convert it to a type you desire in my case I convert it to a dictionary

<img width="456" alt="image" src="https://user-images.githubusercontent.com/108375741/233711901-66b780ee-20ed-4a83-a922-a25831878b80.png">


Immediate view

<img width="484" alt="image" src="https://user-images.githubusercontent.com/108375741/233712085-dee854fd-a8a5-4395-b0b5-17214962e63a.png">

You can checkout the .py code and uipath :)













