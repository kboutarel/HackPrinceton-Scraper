# Author:
# Date:
# Purpose: 
# Usage: 

# Imports
from lxml import etree
import requests
import json
import sys
import os

DEBUG = True

class Submissions(object):

	def __init__(self):
		self.base_url = 'http://hackprincetons2016.devpost.com'
		self.submissions = []

	def get_page(self, main_url):
		'''
		TODO:
		Performs a GET request with the relative url
		Check that request has correct return code,
		print error if not and exit

		Args:
		main_url (str) : relative url of page to GET

		Returns:
		page (requests.Response) : response of GET request
		'''


	def get_body(self, html_string):
		'''
		TODO:
		Gets the body element of the HTML code

		Args:
		html_string (str) : html code to parse to get the body

		Returns:
		body (lxml.etree.Element) : body element of parsed html
		'''

	
	def get_html_string(self, page_num, page_url):
		'''
		TODO:
		Gets the HTML code from the appropriate page.
		First, check if page has been saved on local host.
		If so, just return html code from the file.
		Otherwise, perform GET request with relative url and save
		the request on local host

		Args:
		page_num (str) : page number to retrieve
		page_url (str) : relative url of page

		Returns:
		html_string (str) : html code of page
		'''
		directory_name = "hackprinceton_pages"
		directory = os.getcwd() + os.path.sep + directory_name
		page_name = "page%s.html" % page_num
		page = directory + os.path.sep + page_name


	def create_submission(self, submission_element):
		'''
		TODO:
		Creates a dictionary representing a submission given a submission_element.
		Has the following keys: Winner, Name, Tagline, Authors, URL

		Args:
		submission_element (lxml.etree.Element) : element representing a submission_pages
		    A submission_element contains the tag 'div' and the attrib 'data-software-id'

		Returns:
		submission (dict) : dictionary representing a submission
		'''


	def get_submission_pages(self, main_url="/submissions"):
		'''
		TODO:
		Gets the number of submission pages containing submissions

		Args:
		main_url (str) : relative url containing pages information

		Returns:
		pages (list of tuples (page_number:str, page_url:str)) : 
		    list of tuples representing the pages of submissions
		'''


	def get_submissions_from_page(self, page_num, page_url):
		'''
		TODO:
		Scrapes all of the submissions from a submission page

		Args:
		page_num (str) : page number
		page_url (str) : relative url of page

		Returns:
		submissions (list of dict) : list of submissions
		'''


	def get_submissions(self):
		'''
		TODO:
		Scrapes all of the submissions
		'''

	def toJSON(self, filename):
		'''
		TODO:
		Writes the submissions to the json file
		You may assume that filename is a json file
		(If you have time, try handling all possible errors with handling a non json file)
		'''



# You can use this function to print some debugging information
def debug(msg):
	if(DEBUG):
		print(msg)


def main():



if __name__ == '__main__':
	main()
