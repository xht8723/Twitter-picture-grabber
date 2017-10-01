import urllib2
import urllib
import re
import sys
import os
import urllib3
	
generalurl='https://twitter.com/'

INPUT_id = raw_input('Please input the target userid:')
GETurl = 'https://twitter.com/i/profiles/show/'+INPUT_id+'/media_timeline?include_available_features=1&include_entities=1&max_position=906430782419361793&oldest_unread_id=0&reset_error_state=false'
targetpage = generalurl + INPUT_id + '/media'
fo = open('test0.html','w')
page = urllib2.urlopen(targetpage)
fo.write(page.read())
fo.close()
fo = open('test0.html','r')
pics = re.findall('(https://pbs.twimg.com/media/\S+.jpg)',fo.read())
print pics
fo.close()



for everyid in pics:
	open_ = urllib.urlopen(everyid)
	filename = re.findall('https://pbs.twimg.com/media/(\S+.jpg)',everyid)
	f=open(filename[0],'wb')
	f.write(open_.read())
	f.close()
		
data = {
			':authority': 'twitter.com',
			
			':method':'GET',
			
			':path':'/i/profiles/show/'+'INPUT_id'+'/media_timeline?include_available_features=1&include_entities=1&max_position=906430782419361793&oldest_unread_id=0&reset_error_state=false',
			
			':scheme':'https',
			
			'accept':'application/json, text/javascript, */*; q=0.01',
			
			'accept-encoding': 'gzip, deflate, br',
			
			'accept-language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
			
			'cookie':'guest_id=v1%3A150503827398932119; personalization_id="v1_asdOA7n5X1InKv8aeYCdSA=="; ct0=57f85654ea950289d1736e05a5a4cb19; tip_nightmode=true; ads_prefs="HBERAAA="; kdt=oOHr8LvjqY2AcY6hAxiKPadgnHDVaXIxUSqngCCA; remember_checked_on=1; twid="u=949796682"; auth_token=bc6c048704006a81677175240c2b51bdcd58a7b3; lang=zh-cn; _ga=GA1.2.764661769.1506264934; _gid=GA1.2.1230813260.1506837780; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCA6lm9deAToMY3NyZl9p%250AZCIlYzE0NjkyMzQwZDYwY2E4YzYzOTI2NzdjNDgwMDNmNzI6B2lkIiU5NzIw%250AZjYyZDkzMGVkNTFlOGI3MWQ3OWIzYTM2MjBmNg%253D%253D--ec92f995a5c7c9283b5481afb307afae5098e9b9',
			
			'referer' : 'https://twitter.com/rei_0828/media',
			
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
			
			'x-requested-with' : 'XMLHttpRequest',
			
			'x-twitter-active-user' : 'yes'
	}