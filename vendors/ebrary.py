#ebrary
#here we call Selenium/PhantomJS

 

for url in urls:

	browser = webdriver.PhantomJS() 

	browser.get(url[1])

	soup=BeautifulSoup(browser.page_source)
		
	if soup.find_all(text = re.compile("Your institution has unlimited access to this book")):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Right On!")
 		#print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
 		wx.Yield()
 	elif soup.find_all(text = re.compile("Your institution has access to 1 copy of this book.")):
 		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Right On! [supo]")
 		#print str(count) +  " of " + str(num_lines) + " | " + "Right On! [supo]"  
 		outurls.writerow([url[0], url[1], "Right On! [supo]"])
 		count += 1
 		wx.Yield()
	elif soup.find_all(text = re.compile("Not Available for Online Reading")):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Nope!"])  
		count += 1
		wx.Yield()
 	else: 
 		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1
		wx.Yield()


