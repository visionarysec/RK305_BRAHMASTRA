#/usr/bin/python3

#AUTHOR: Satyam Dubey [Team Brahmastra]

import requests
import json
import validators
import argparse, sys, os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver


def main():
    banner = """
 _______  _______  _                          _       _________ _______  _______ 
(       )(  ___  )( \      |\     /||\     /|( (    /|\__   __/(  ____ \(  ____ )
| () () || (   ) || (      | )   ( || )   ( ||  \  ( |   ) (   | (    \/| (    )|
| || || || (___) || |      | (___) || |   | ||   \ | |   | |   | (__    | (____)|
| |(_)| ||  ___  || |      |  ___  || |   | || (\ \) |   | |   |  __)   |     __)
| |   | || (   ) || |      | (   ) || |   | || | \   |   | |   | (      | (\ (   
| )   ( || )   ( || (____/\| )   ( || (___) || )  \  |   | |   | (____/\| ) \ \__
|/     \||/     \|(_______/|/     \|(_______)|/    )_)   )_(   (_______/|/   \__/
                                                                                 
    """
    print("\033[1;35m " + banner + "\033[m")
    print("\033[1;36m" +"[+] Starting the Server locally on https://localhost:5000"+ "\033[m")
    
    #arguments defined
    parser = argparse.ArgumentParser(prog = 'MALHUNTER', description="MalHunter is a malicious link detection tool with the capability to do automated analysis. For more information visit this link")
    parser.add_argument('-f', "--file", type=str, required=True, help="Hunter needs the JSON configuration file")
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
    
    server = data['server']
    port = data['port']
    vt_api = data['malice_hunter_api']['virustotal_api']
    a = vt_api is not ""
    if a: print("\033[32m" + u'\u2713' + "\033[m" + "Found the virustotal API")
    api1 = data['malice_hunter_api']['app1_api']
    api2 = data['malice_hunter_api']['app2_api']
    print("Starting the server http://{}:{}".format(server, port))
    start_server(server, port)

def start_server(server,port):

    server_address = (server, port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler) 
    httpd.serve_forever()

if __name__ == "__main__":

    main()