import requests
import sys, os
import validators
import argparse, json


def vt_url_submit(dom_url, api_key):

        
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    params = {'apikey': api_key, 'resource':dom_url}
    response = requests.get(url, params=params)
    print(response.json())
    domain_name = dom_url.split("/")[2]
    vt_dom_analyze(domain_name, api_key)

    #iter = (response.json()['scans'].keys())
    #for key in iter:
    #    print("Found Malicious Source {} : {}".format(key, response.json()['scans'][key]))



def vt_dom_analyze(dom_url, api_key):
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':api_key,'domain':dom_url}
    response = requests.get(url, params=params)
    print(response.json())
    



#def vt_url_gather():


def main():
    
    parser = argparse.ArgumentParser(prog = 'vt_engine', description="Virustotal Engine")
    parser.add_argument('-s', "--submit", type=str, required=True, help="Submit your URL or domain")
    parser.add_argument('-f', "--file", type=str, required=True, help="Define the JSON configuration file")
    args = parser.parse_args()
    if args.file is not "":
        if os.path.exists(args.file) and str(args.file).endswith(".json"):
              print("Found the Configuration file")
    else:
        print("Configuration was not found")
        sys.exit(0)

    conf_file = args.file
    with open(conf_file) as config_file:
        data = json.load(config_file)

    vt_api = data['malice_hunter_api']['virustotal_api']
    a = vt_api is not ""
    if a: print("\033[32m" + u'\u2713' + "\033[m" + "Found the virustotal API")
    print("[+] Starting the Detection Engine")

    if args.submit is not "":
        if validators.url(args.submit):
            print("[+]Found the valid URL ".format(args.submit))
            vt_url_submit(args.submit, vt_api)
        elif validators.domain(args.submit):
            print("[+]Found the Domain Name for analyzes")
            vt_dom_analyze(args.submit, vt_api)
        else:
            print("Object given was niether a domain nor a url. Please provide valid URL or a domain")   
    
    


if __name__ == "__main__":
    main()