#muse


for url in urls:

	r = requests.get(url[1])

	soup = BeautifulSoup(r.text, "lxml")
		
	if soup.find_all("span", class_= "access_yes"):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Right On!")
 		#print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
 		wx.Yield()
	elif soup.find_all("span", class_= "access_no"):
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



