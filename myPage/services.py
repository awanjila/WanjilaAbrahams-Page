import urllib2
import json
import unirest

class Api(object):
	def youtube(self):
		self.youtube_api='AIzaSyAYVBZd-ZJxVkYp2YvELtNfRY4BK-s6Vdw'
		self.mychannel_id="UCmwVv2nqokqZzzyyFe8hEuA"
		self.myYoutube_activity="https://www.googleapis.com/youtube/v3/subscriptions?part=snippet&channelId="+self.mychannel_id+"&key="+self.youtube_api+"&maxResults=50"
		self.json_data=urllib2.urlopen(self.myYoutube_activity)
		self.new_data=json.load(self.json_data)
		self.target_data=self.new_data["items"]
		return self.target_data
		

		


	
	def quotes(self):
		#self.get_quotes="http://quotes.rest/quote.json?api_key=<your_api_key>"

# These code snippets use an open-source library.
		self.response = unirest.get("https://kashyap-random_quotes.p.mashape.com/",
  			headers={
  					  "X-Mashape-Key": "q0pyYwsqY8mshlSrUTVGBotILX6np1J7mKAjsnZlTPKVRINwjR",
   							 "Accept": "text/plain"
 								 }
									)
		self.json_data=urllib2.urlopen(self.response)
		self.new_data=json.load(self.json_data)
		return self.new_data
	def displayQuotes(self):
		pass

print Api().youtube()


#https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId=UCmwVv2nqokqZzzyyFe8hEuA&key=AIzaSyAYVBZd-ZJxVkYp2YvELtNfRY4BK-s6Vdw&maxResults=50
#https://www.googleapis.com/youtube/v3/subscriptions?part=snippet,contentDetails&channelId=UCmwVv2nqokqZzzyyFe8hEuA&key=AIzaSyAYVBZd-ZJxVkYp2YvELtNfRY4BK-s6Vdw&maxResults=50