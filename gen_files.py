from re import L
import argparse
import os
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.google
headers = {'user-agent': user_agent}


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="Number of the problem", required=True)
parser.add_argument("-f", "--folder", help="Folder of your repo", required=False)
args = parser.parse_args()
FOLDER = args.folder if args.folder is not None else "./"

url = f"https://leetcode.com/problemset/all/?search={args.number}?page=1"
leetcode_url = "https://leetcode.com"

from requests_html import HTMLSession
s = HTMLSession()
response = s.get(url)
response.html.render(sleep=1)
all = response.html.find('a.h-5', containing=str(args.number))

found = False
for a in all:
    if a.text.split('.')[0] == str(args.number):
        # title = f"{args.number}. {a.contents[-1]}"
        title = a.text
        problem_url = leetcode_url + a.attrs['href']
        code_filename = a.attrs['href'].split('problems')[1].strip('/')
        
        found = True
if not found:
    print("Fail to find the problem!!!")
    print(all)
    exit(-1)
    
problem_folder = os.path.join(FOLDER, title)

if not os.path.exists(problem_folder):
    os.makedirs(problem_folder)
    # TODO 
    # support more file format, with possibly a argument to specify langugage
    with open(os.path.join(problem_folder, code_filename + ".py"), 'w') as f:
        pass
    with open(os.path.join(problem_folder,  "explanation.md"), 'w') as f:
        f.write(f"[{title}]({problem_url})\n===\n")
        f.write("Nothing here! I'm probably too lazy QQ.")

    print("Folder created!")
else:
    print("Folder already exists")
