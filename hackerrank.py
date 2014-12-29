#python
import urllib,urllib2,json,time
from cookielib import CookieJar

def run_code(h_url,fname):
	#cookies
	cj = CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)

	#set url
	base_url="https://www.hackerrank.com/"
	url=base_url+"rest/contests/master/challenges/"+h_url+"/compile_tests/"
	#print url

	#get content of code
	with open(fname,'r') as content_file:
		content = content_file.read()
	
	#add paramaters and send request
	values={'code':content,'language':'cpp'}
	data=urllib.urlencode(values)
	req=urllib2.Request(url,data)
	response=urllib2.urlopen(req)
	page=response.read()
	#print page
	j_data=json.loads(page)
	#print x

	#make new url
	i=1
	sid=j_data['model']['id']
	query_url=url+str(sid)+"?="
	#print query_url
	
	#loop until compiling and output doesn't come back in response
	while j_data['model']['status']==0:
		time.sleep(1)
		try:
			status_msg=j_data['model']['status_string']
			print status_msg
		except KeyError:
			pass
		q_url=query_url+str(i)
		#print q_url
		req=urllib2.Request(q_url)
	        response=urllib2.urlopen(req)
	        page=response.read()
	        #print page
	        j_data=json.loads(page)
	        #print x,i
		i=i+1
		if i==10:
			break

	#print output
	if j_data['model']['status']==1:
		printResult(j_data)
	else:
		if i==10:
			print "Operation Timed Out"
		else:
			print "Some error occured"

def printResult(data):
	l=len(data['model']['testcase_message'])
	for i in range(l):
		print "Input:";print data['model']['stdin'][i]
		print "Output:";print data['model']['stdout'][i]
		print "Expected Output:";print data['model']['expected_output'][i]
		print "Result:",data['model']['testcase_message'][i]








