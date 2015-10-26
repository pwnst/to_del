# import requests
# header = {"Authorization": "Bearer 1687aeb2698dee47cbc9b50881680ef"}

# def get_dayofweek(campaignid):
# 	url = 'http://qa-api.cadreon.com:8280/amp/v1/campaign/results/dayofweek/campaignid/' + str(campaignid)
# 	r = requests.get(url=url, headers=header)
# 	return r
# l = []
# for i in range(5000):
# 	try:
#  		r = get_dayofweek(i).json()
#  		print i
#  		if r.has_key('response'):
#  			l.append(r['response'])
#  	except:
#  		pass

# print l


d = (9.11, 16.45, 18.65, 1.85, 53.94)
d2 = (10.97, 53.94, 35.1)
print sum(d2)