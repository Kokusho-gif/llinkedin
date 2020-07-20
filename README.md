Name
====
Message sender on LinkedIn

Overview
Written in Python3, using Selenium

## Description
This program help you find suitable people for a market research. You can designate some keywords such as "Engineer", "CEO" and will get a result of a search engine with those keywords remotely. Besides, you can send a message to some of your friends selected by some given conditions.

## Demo
Yet to be written

## Requirement
I clinched the reuired packages for Python3 into Requirements.txt

## Usage
The main program is main.py. This file next to import linkedin_controller.py so linkedin_controller describes main function of this application.
\n
All of required information to login and search are put in parameters.py. 
In parameters.py, you have to write your account information(Mailaddress, password) and so on.
keyword1, keyword2, keyword3 => Searching arguments
maximum_invitation => Maximum number of people to send connection suggestion.
how_many_pages => This program will stop if current page is over "how_many_pages" at a result of search.
linkedin_username => Account name
linkedin_password => Account password

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[Kokusho](https://github.com/Kokusho-gif)
