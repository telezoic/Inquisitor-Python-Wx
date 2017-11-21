#springer


 


for url in urls:


	r = requests.get(url[1])

	soup = BeautifulSoup(r.text, "lxml")

	if soup.find_all("a", class_= "webtrekk-track pdf-link"):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Right On!")
 		#print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
 		wx.Yield()
	elif soup.find_all("a", class_= "access-link"):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Nope!"])  
		count += 1
		wx.Yield()
	elif soup.find_all("title", text = re.compile("Deleted DOI")):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Deleted DOI!" + " | " + url[1] + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Deleted DOI!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Deleted DOI!"]) 
		count += 1
		wx.Yield()	
	elif soup.find_all("div", id = "error"):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Page not found!" + " | " + url[1] + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Page not found!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Page not Found!"])  
		count += 1
		wx.Yield() 
 	else: 
 		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1
		wx.Yield()


