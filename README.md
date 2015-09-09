# Inquisitor-Python-Wx#

Another python (2.7) redux of Kristina Spurgin's most super excellent <a href="https://github.com/UNC-Libraries/Ebook-Access-Checker">Ebook-Access-Checker!</a> This one has a GUI.

![](http://www2.viu.ca/ds-dev/gitimages/kaneview1.png)

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
	
Windows users - if you get SSL errors after installing ```requests``` try ```pip install requests[security]``` instead.
	
You can get PhantomJS <a href="http://phantomjs.org/">here </a>
and you can get wxPython <a href="http://www.wxpython.org/download.php#osx">here</a>.
  
####Instructions:####
[tested in OSX and Windows]

1: Place the Inquisitor-Python-Wx folders and files in a folder on your machine. [.gitkeep lets us load an empty folder structure - so you don't have to create it manually on your machine]

2: Modify the following lines in InquisitorWx.py to specify your folders for i/o:
    
  	vendorpath = "folder on your machine/vendors/"
  	csvinpath  = "folder on your machine/input/" 
  	csvoutpath = "folder on your machine/output/"

3: Windows users, modify line 154 to give the full path to the image ``` bmp = wx.Bitmap("kanelong.png")```

4: Create a .csv with a list of titles in the first column 	url[0] 
and urls in the second column 	url[1]. Remove your EZproxy/Authentication prefix from the urls.
Ensure there are no headers in the .csv

5: Add your input .csv file[s] to /input.

6: Mod/add your own vendor scripts as needed based on the appropriate matching syntax [from your vendor's html source code].

7: Add these vendor files to /vendors.

8: Run inquisitorWx.py from the terminal.

9: Follow the GUI prompts: select a vendor file; select a .csv input file; name your .csv output; start. Each selection will be confirmed in the status bar.

10: The status bar on the GUI will count and display access messages + urls + titles for access failures.

11: Terminal display will write out errors.

12: When the script is complete, the status bar will display the total run time.

13: The script will write the access message to the third column of the .csv, now located in /output.

####Roadmap####

1: Correct BeautifulSoup markup warning for windows.


