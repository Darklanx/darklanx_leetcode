from re import L
import requests
from bs4 import BeautifulSoup
import argparse
import os
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="Number of the problem", required=True)
parser.add_argument("-f", "--folder", help="Folder of your repo", required=False)
args = parser.parse_args()


url = f"https://leetcode.com/problemset/all/?search={args.number}&page=1"
leetcode_url = "https://leetcode.com"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
all = soup.find_all("a", class_="h-5") 
FOLDER = args.folder if args.folder is not None else "./"



for a in all:
    if a.contents[0] == str(args.number):
        title = f"{args.number}. {a.contents[-1]}"
        problem_url = leetcode_url + a.attrs['href']
        code_filename = a.attrs['href'].split('problems')[-1][1:] 

problem_folder = os.path.join(FOLDER, title)

if not os.path.exists(problem_folder):
    os.makedirs(problem_folder)
    # TODO 
    # support more file format, with possibly a argument to specify langugage
    with open(os.path.join(problem_folder, code_filename + ".py"), 'w') as f:
        pass
    with open(os.path.join(problem_folder,  "explanation.md"), 'w') as f:
        f.write(f"[{title}]({problem_url})\n ===\n")
        f.write("Nothing here! I'm probably too lazy QQ.")



    print("Folder created!")
else:
    print("Folder already exists")
