import requests
import re 
from urllib.parse import urljoin
import os
from random import choice, randint, shuffle
import optparse

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'

def clearScr():
    os.system('clear')

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-u", "--url", dest="url", help="URL to scan.")
    (options, arguments) = parser.parse_args()
    if not options.url:
        parser.error(color.NOTICE + "[-] Please specify the url, use --help for more info" + color.END)
    return options

options = get_arguments()
clearScr()


color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
shuffle(color_random)

weblogo = color_random[0] + '''
Yb        dP       8       .d88b                      8            
 Yb  db  dP  .d88b 88b.    8P    8d8b .d88 Yb  db  dP 8 .d88b 8d8b 
  YbdPYbdP   8.dP' 8  8    8b    8P   8  8  YbdPYbdP  8 8.dP' 8P   
   YP  YP    `Y88P 88P'    `Y88P 8    `Y88   YP  YP   8 `Y88P 8    
                                                                                                                                       
        ''' + color.END

print (weblogo + color.RED + '''
       }--------------{+} Coded By Sirwolf {+}--------------{
       }--------{+}    GitHub.com/Sir-wolf :)    {+}--------{
    ''' + color.END)

target_url = str(options.url)

def extract_links(url):
	response = requests.get(url)
	return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

href_link = extract_links(target_url)

for link in href_link:
	link = urljoin(target_url, link)
	print(color.OKBLUE + "[+] url find : " + link + color.END + "\n")
