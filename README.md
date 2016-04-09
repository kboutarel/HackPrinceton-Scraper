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
### Scraper
For the first part of the assignment, you will need to complete the code in the file `submissions.py`.  
We give you a skeleton code to help you get started but you may start from scratch if you prefer.  
Your goal is to create a JSON file named `submissions.json` which will contain all of the submissions as a list of dictionaries.    
Each dictionary will represent a submission and should have the following keys:  
* `Authors` : devpost ids of authors of the submission  

* `Name` : name of the submission  

* `Tagline` : small description of submission  

* `URL` : url of submission  

* `Winner` : whether the submission won or not

For example, a submission should look like this:  

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

### Questions
You will be given the file `participants.json` which contains every registered participant of the hackathon.  
The file is a dictionary of dictionaries, where the key is the devpost id of the participant and the value is information about the participant. The dictionary contains the following keys:  
* `Name` : name of the participant

* `Projects` : number of projects    

* `Followers` : number of followers    

* `Skills` : list of skills    

* `Titles` : list of titles  

* `Portfolio` : url of participant  

For example, a participant should look like this:

    "15tungalbert": {
      "Followers": 1, 
      "Name": "Albert Tung", 
      "Portfolio": "http://devpost.com/15tungalbert", 
      "Projects": 4, 
      "Skills": [
        "ruby-on-rails"
      ], 
      "Titles": [
        "Other"
      ]
    }

Using the provided `participants.json` and your own `submissions.json`, answer the following questions:  
* `Question 1` : For each participant with names starting in 'D', 'G', and 'M', print the tuple: (participant_name, participant_portfolio)  

* `Question 2` : For each participant that has at least 12 followers, print the tuple (participant_name, participant_projects, participant_followers)  

* `Question 3` : For each participant that has 'web' and 'python' skills, print the tuple (participant_name, list of Titles)  

* `Question 4` : For each winning submission, print  

    submission_name  
    submission_tagline  
    (participant_name, participant_projects, participant_followers)  

* `Question 5` : For the authors of the submissions whose name starts with 'M', print the tuple (submission_name, list of distinct skills, list of similar skills)  


## Part 2: Participants
This will be released next week! Stay tuned :)