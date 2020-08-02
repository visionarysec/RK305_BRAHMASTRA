import requests
import argparse
import json
from unshortenit import UnshortenIt
import time

start_time = time.time()

def main():
	print("URL---Detection---Tool")
	parser = argparse.ArgumentParser()
	parser.add_argument('-u', "--url", type=str, required=True, help="feed the URL")
	#parser.add_argument("-f", "--format", type=str, required=True, choices=['json','dict','csv']
	args = parser.parse_args()
	# global start_time
	# start_time = time.time()
	print ("Started at {}".format(start_time))
	url_decompress(args.url)

def url_decompress(url):
	print("[+] Now we are in URL Decompression Engine")
	r = UnshortenIt().unshorten(url)
	print("[+] Found the Original URL : ", r)
	check_url(url)
	
def check_url(url):
	print('Checking The Cyrelic IDN Homograph Attack')
	bad_chars = ['\u0430', '\u03F2', '\u0435', '\u043E', '\u0440', '\u0455', '\u0501', '\u051B', '\u051D']
	result = [bad_chars[i] for i in range(len(bad_chars)) if bad_chars[i] in url]
	if result:
		msg = '\n[*] Evil URL detected: {}'.format(url)
		msg += '\n[*] Evil characters used: {}'.format(result)
	else:
		msg = '\n[*] Evil URL NOT detected: {}'.format(url)

	print(msg)
	url_detect(url)

def url_detect(url_detect):
	RED = '\033[31m'
	BLUE = "\033[34m"
	GREEN = "\033[23m"
	YELLOW = "\033[93m"
	ENDC = "\033[m"
	print(BLUE + "[+] Now we are in the URL Detection Engine" + ENDC)
	scanurl = "https://www.virustotal.com/vtapi/v2/url/scan"
	api_key = "10348d6a56143962c1646c73d805fa09be69469757b1b8e71c446b79356c43cc"
	r_scan = requests.post(scanurl, data = {"apikey":api_key,"url":url_detect})
	json_scan_data = json.loads(r_scan.text)
	resource = json_scan_data['scan_id']
	reporturl = "https://www.virustotal.com/vtapi/v2/url/report"
	r_report = requests.post(reporturl, data = {"apikey":api_key,"resource":resource,"scan":1})
	json_report_data = json.loads(r_report.text)
	
	for i in json_report_data['scans'].keys():
		if json_report_data['scans'][str(i)]['detected'] == True:
			print(RED + "{} detected the INPUT URL as MALICIOUS".format(i) + ENDC)
		else:
			print(GREEN + "{} detected the INPUT URL as SAFE".format(i) + ENDC)
	now_time = time.time()
	print('Time of Completing the EXECUTION {}'.format(now_time))
	tt_exec = now_time - start_time
	
	
	# print(json.dumps(json_report_data, indent=4, sort_keys=True))
	print(YELLOW + 'Time Taken in the EXECUTION {:.2f}'.format(tt_exec) + ENDC)
	return json_report_data

# if __name__ == "__main__":
# 	main()
