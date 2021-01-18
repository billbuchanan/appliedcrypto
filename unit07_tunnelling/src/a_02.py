import requests
import time
import sys
import logging

API = 'https://api.ssllabs.com/api/v2/'


def requestAPI(path, payload={}):
    '''This is a helper method that takes the path to the relevant
        API call and the user-defined payload and requests the
        data/server test from Qualys SSL Labs.
        Returns JSON formatted data'''

    url = API + path

    try:
        response = requests.get(url, params=payload)
    except requests.exception.RequestException:
        logging.exception('Request failed.')
        sys.exit(1)

    data = response.json()
    return data


def resultsFromCache(host, publish='off', startNew='off', fromCache='on', all='done'):
    path = 'analyze'
    payload = {
                'host': host,
                'publish': publish,
                'startNew': startNew,
                'fromCache': fromCache,
                'all': all
              }
    data = requestAPI(path, payload)
    return data


def newScan(host, publish='off', startNew='on', all='done', ignoreMismatch='on'):
    path = 'analyze'
    payload = {
                'host': host,
                'publish': publish,
                'startNew': startNew,
                'all': all,
                'ignoreMismatch': ignoreMismatch
              }
    results = requestAPI(path, payload)

    payload.pop('startNew')

    while results['status'] != 'READY' and results['status'] != 'ERROR':
        time.sleep(30)
        results = requestAPI(path, payload)

    return results


import csv
with open('sites.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:

		url = row['site'].strip()
		print "Scanning (might take a few minutes): "+url
		a = newScan(url)
		with open("out3.txt", "a") as myfile:
    			myfile.write(str(row['web'])+"\n"+str(a)+"\n\n\n")
			print row['web']
