#!/usr/bin/env python
# -*- coding: utf-8 -*
import urllib2
import json


youtube_api='AIzaSyAYVBZd-ZJxVkYp2YvELtNfRY4BK-s6Vdw'
mychannel_id="UCmwVv2nqokqZzzyyFe8hEuA"
myYoutube_activity="https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId="+mychannel_id+"&key="+youtube_api+"&maxResults=50"
json_data=urllib2.urlopen(myYoutube_activity)
new_data=json.load(json_data)

print json_data
for obj in new_data['items']:

	print obj['snippet']["title"]

