# COSC-11001-Final-Chatbot-Assignment
Introduction to Computer Programming COSC 11001 Final Chatbot Assignment 2022. 
This is a simple chatbot that can do many tasks using assumptions of the English language and includes a login system with basic encoding.

**Package Dependencies: **
(Run ‘**requirements.bat**’ for easy install of **all** required packages)
Required packages: 
 pip install yfinance
 pip install screeninfo
pip install wmi
pip install requests
Yahoo Finance is required to obtain stock prices
Screeninfo is required to display info about monitor
Wmi is required to obtain info about the OS, CPU, GPU, and RAM size

If pip can not be used to install the required packages, running python setup.py install in each folder in the ‘Packages’ folder will install them (There is a install.bat file in each folder that can be used.)


**Features:**
-Login system
-Saves users to database
-Encodes user login data with rot13 to make file more secure
-Ability to change user password once logged in
-Math module
-Can solve math expressions given to it
-Ask chatbot for current time
-Ask chatbot for current stock prices
-Ask chatbot for current cryptocurrency prices
-Exception handling
-Ask bot how are you (changes based on type of bot)
-Saves chat log with bot as .log file
-Ask the bot who is in space right now
-Returns name of each person and space station they’re on
-Ask bot to roll a die
-Ask bot to flip a coin
-Changes its emotion on command 
-Tells user their monitor size
-Tells user their system info (OS, RAM size, CPU, GPU)

**Examples of commands:**
I want to flip a coin
Can you solve an equation for me?
Tell me who is in space right now
I want to roll a die
I want to change my password
How are you?
Turn into an angry chat bot
I don’t like the happy chatbot
What time is it?
Change to the default bot
Tell me a crypto price
Tell me a stock price
Goodbye
What is my monitor size
Do you know my name
What are my system specs

*When the bot asks ‘What type of chatbot would you like to talk to?’ it is asking if you would like to talk to the grumpy or happy bot.*

**Files:**

-main.py
The main file. Run this to execute the program

-ChatBot.py
Functions:
ChatBot.sayhi() - Says hi
ChatBot.howareyou() - answers ‘how are you’
ChatBot.emotion() - displays emotion after messages
ChatBot.time() - tells the user the current time
ChatBot.changePassword() - Changes the user’s password in the database
ChatBot.getuser_response() - awaits user input

-ExtraFeatures.py
Functions:
titlescreen() - Displays a title screen for the bot
Games.diceroll() - Rolls a die
InSpace.list() - Lists everyone in space and the spaceship they are on
Games.coinflip() - Flips a coin
systemSpecs.monitorSize() - Tells the user the size of their monitor
systemSpecs.systemSpecs() - Tells user their os, cpu, gpu, and ram size

-FetchCryptoPrice.py
Functions:
FetchPrice.fetchStockPrice() - Gets the value of a stock and displays % rise/fall from previous day
FetchPrice.fetchCryptoPrice() - Gets the value of a cryptocurrency

-Math.py
Functions:
Math.parser() - Parse and solve math expressions

-SaveData.py
Functions:
SaveData.getFileName() return filename
SaveData.initiateSaveData() Creates an encoded .log file to save chatlog in
SaveData.getUsername() - return username
SaveData.Login() - Brings up the login screen
SaveData.setPassword() - Changes the user’s password in the database
SaveData.print()*
SaveData.input()*
* Print and input functions were overrided so they also output their contents to log file
  
-Database.data (File is created if it doesn’t exist)
-requirements.bat (Installs package dependencies with pip)

