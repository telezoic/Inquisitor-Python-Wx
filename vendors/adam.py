#adam



for url in urls:


	r = requests.get(url[1])

	soup = BeautifulSoup(r.text)
		
	if soup.find_all(text = re.compile("Download whole document")) or soup.find_all(text = re.compile("Download entire document")):
		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Right On!")
 		#print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
 		wx.Yield()
 	else: 
 		self.SetStatusText(str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0])
		#print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1
		wx.Yield()



