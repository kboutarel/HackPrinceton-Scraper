# Author:
# Date:
# Purpose: 
# Usage: 

import json

def Q1(participants):
	'''
	For each participant with names starting in 'D', 'G', and 'M',
	print the tuple: (participant_name, participant_portfolio)
	'''
	print("QUESTION1:")



def Q2(participants):
	'''
	For each participant that has at least 12 followers,
	print the tuple (participant_name, participant_projects, participant_followers)
	'''
	print("QUESTION2:")


def Q3(participants):
	'''
	For each participant that has 'web' and 'python' skills,
	print the tuple (participant_name, list of Titles)
	'''
	print("QUESTION3:")


def Q4(participants, submissions):
	'''
	For each winning submission, print
	submission_name
	submission_tagline
	(participant_name, participant_projects, participant_followers)
	'''
	print("QUESTION4:")


def Q5(participants, submissions):
	'''
	For the authors of the submissions whose name starts with 'M',
	print the tuple (submission_name, list of distinct skills, list of similar skills)
	'''
	print("QUESTION5:")



def main():
	# Filenames for participants and submissions, respectively
	pfilename = ""
	sfilename = ""

	participants = []

	Q1(participants)
	Q2(participants)
	Q3(participants)

	submissions = []

	Q4(participants, submissions)
	Q5(participants, submissions)


if __name__ == "__main__":
	main()