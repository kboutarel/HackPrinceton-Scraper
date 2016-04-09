# HackPrinceton-Scraper
-----------------------
Scraper for the HackPrinceton website


The goal of this assignment is to build a Python scraper for the HackPrinceton 2016 website.  
In the first part, you will create a parser for the submissions of the hackathon and answer some questions through coding exercises.  
In the second part, you will deal with parsing all of the participants of the hackathon.  


## Requirements
As described above, this assignment will be coded in Python.  
Therefore, you will need a working version of Python.  
We highly recommend you use version 2.7, but version 3.x will work as well.  

You will be using two third-party librairies to build the scrapers:
* `requests` :  used to perform HTTP requests and easily handle the responses.  

* `lxml` : used to parse HTML code.  

After installing Python, a tool called `pip` will be installed as well and will be used to install these librairies.  
However, you might need to modify your PATH environment variable and add the folder where `pip` is installed.  
* `Windows`: `C:\Python27\Scripts`

* `Mac OS X`: `/Library/Frameworks/Python.framework/Versions/2.7/bin`

* `Linux`: `/usr/lib/python2.7/Scripts`

Once that is done, run both of these commands to download the librairies:  

    pip install requests  

    pip install lxml  

Note: You might need to be in Administrator mode for Windows, or use `sudo` for the others. 

At this point, you have all the tools necessary to start the assignment! YAY!  


## Part 1: Submissions  
For the first part of the assignment, you will need to complete the code in the file `submissions.py`.  
We give you a skeleton code to help you get started but you may start from scratch if you prefer.  
Your goal is to create a JSON file named `submission.json` which will contain a list of dictionaries.  
Each dictionary should have the following keys:  
* `Authors` : devpost ids of authors of the submission  

* `Name` : name of the submission  

* `Tagline` : small description of submission  

* `URL` : url of submission  

* `Winner` : whether the submission won or not

For example, the first submission should look like this:  

    {
        "Authors": [
          "yarabarla", 
          "cyrusroshan"
        ], 
        "Name": "Spin to Win", 
        "Tagline": "a 3d arduino-based scanner for under $20", 
        "URL": "http://devpost.com/software/spin-to-win", 
        "Winner": true
    }