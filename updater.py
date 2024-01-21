import requests
print(f"Use 'requests' {requests.__version__}")
import argparse
import os
# print(f"{os.path.dirname(__file__)}")
os.chdir(os.path.dirname(__file__))

parser = argparse.ArgumentParser(description="tacformer pretraining")
parser.add_argument("--input", "-i", default="aria2.conf",
                    help="The filename of aria2 config file. Default: 'aria2.conf'.")
args = parser.parse_args()

aria2confFilename = args.input
assert os.path.exists(aria2confFilename), f"Cannot find '{aria2confFilename}', please make sure this script is under the same folder of '{aria2confFilename}'."

# download tracker list

trackerListUrls = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ip.txt",
    "https://ngosang.github.io/trackerslist/trackers_all_ip.txt",
    "https://cdn.jsdelivr.net/gh/ngosang/trackerslist@master/trackers_all_ip.txt",
]

trackerListFile = None
for trackerListUrl in trackerListUrls:
    try:
        trackerListFile = requests.get(trackerListUrl)
    except requests.exceptions.ConnectionError:
        print(f"Connection error with '{trackerListUrl}'. Trying next.")
        continue
    print(f"Download successfully from '{trackerListUrl}'.")
    break
trackerList = str(trackerListFile.content, encoding='utf-8')
trackerList = trackerList.replace("\n\n", ",")
numTrackers = trackerList.count(",")
if trackerList[-1] == ",": # remove the last comma
    trackerList = trackerList[: -1]
# print(f"{trackerList = }")

# aria2conf = 
with open(aria2confFilename,'r', encoding='utf-8') as file:
    lines = file.readlines()

with open(aria2confFilename,'w', encoding='utf-8') as file:
    for line in lines:
        if line.find("bt-tracker") != -1:
            pass
            print("Remove existing tracker list.")
        else:
            file.write(line)
    print(f"Append {numTrackers} new trackers to '{aria2confFilename}'.")
    file.write("bt-tracker="+trackerList+"\n")