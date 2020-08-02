import requests
import sys, os
import validators
import argparse, json
import dns.resolver
import dns 
import censys.certificates
import censys.ipv4


def investigate(domain, vt_api, api_id, api_secret):
    certificates = censys.certificates.CensysCertificates(api_id, api_secret)
    certificate_query = 'parsed.names: {}'.format(domain)
    certificates_search_results = certificates.search(certificate_query, fields=['parsed.names'])
    #print(certificates_search_results)
    subdomains = []
    for search_result in certificates_search_results:
        subdomains.extend(search_result['parsed.names'])
    for subs in subdomains: 
        print(subs)
    
    result_A = dns.resolver.query(domain, 'A')
    for ipadd in result_A:
        print('[+] A RECORDS :', ipadd)
    result_TXT = dns.resolver.query(domain, 'TXT')
    print('[+] TXT : ', result_TXT.qname)
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':vt_api,'domain':domain}
    response = requests.get(url, params=params)
    for dnsres in response.json()['dns_records']:
        print(dnsres)
    for i in response.json()['detected_urls']:
        print("RELATED URL : {} POSITIVES {}".format(i['url'], i['positives']))

def main():

    parser = argparse.ArgumentParser(prog = 'investigation_script', description="Virustotal Engine")
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
    censys_api = data['malice_hunter_api']['CENSYS_API_ID']
    censys_secret = data['malice_hunter_api']['CENSYS_API_SECRET']
    a = censys_api is not "" and censys_secret is not "" and vt_api is not ""
    if a: print("\033[32m" + u'\u2713' + "\033[m" + "Found the CENSYS API & CENSYS SECRET")
    else: sys.exit(0)
    print("[+] Starting the Investigation Script")
    if validators.domain(args.submit):
        investigate(args.submit, vt_api, censys_api, censys_secret)
    elif validators.url(args.submit):
        domain = str(args.submit).split("/")[2]
        investigate(domain, vt_api, censys_api, censys_secret)
    else:
        print("Please provide a valid URL or domain")
        sys.exit(0)


if __name__ == "__main__":
    main()