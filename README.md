# Inquisitor-Python#

Another python (2.7) redux of Kristins Spurgin's most super excellent <a href="https://github.com/UNC-Libraries/Ebook-Access-Checker">Ebook-Access-Checker!</a> This one has a GUI.

####What it does

Scrapes ebook/streaming video landing pages and confirms instititional access based on html source code. It does this with a GUI via <a href="http://www.wxpython.org/">wxPython</a>

####What it doesn't . . . 

Trigger DDA autopurchases/short-term loans

####*What's different this time . . .*

1: Speed. The Inquisitor-Python runs on BeautifulSoup and Requests. Speed is much improved in the absence of a headless browser. [note: The javascript heavy Proquest/ebrary pages call for a headless browser, you may have other vendors with similar demands]

2: User interface is a GUI.

3: File input/output is folder specfic.

4: Separate scripts describe each vendor. Add/mod your own as needed.

5: Runtime benchmark.

  
	
####What do you need?

	import os
  
 	import wx

	from bs4 import BeautifulSoup 

	import csv

	import time

	import re 

	import requests 
	
	from selenium import webdriver
	
BeautifulSoup, requests, and Selenium are not part of the standard Python library. So:

	pip install beautifulsoup4
	pip install requests
	pip install selenium
	
You can get PhantomJS <a href="http://phantomjs.org/">here.</a>
and you can get wxPython <a href="http://www.wxpython.org/download.php#osx">here</a>.
  
####Instructions:####

1: Place the scripts in a folder on your machine, and add a output folder.

2: Modify the following lines in InquisitorWx.py to specify your folders for i/o:
    
  	vendorpath = "folder on your your machine/vendors/"
  	csvinpath  = "folder on your your machine/input/" 
  	csvoutpath = "folder on your your machine/output/"

3: Create a .csv with a list of titles in the first column 	url[0] 
and urls in the second column 	url[1]. Remove your EZproxy/Authentication prefix from the urls.
Ensure there are no headers in the .csv

4: Add your input .csv file[s] to /input.

5: Mod/add your own vendor scripts as needed based on the apprropriate matching syntax [from your vendor's html source code].

6: Add these vendor files to /vendors.

4: Run inquisitorWx.py from the terminal.

5: Follow the GUI prompts.

6: The status bar on the GUI will count and display access messages + urls and titles for access failures.

7: Terminal display will write out errors.

8: When the script is complete, the status bar will write out the total run time.

9:The script will write the access message to the third column of the .csv, now located in /output.

####Roadmap####

1: Windows testing [it's all OSX so far]

