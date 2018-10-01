import os
import json
import pprint 
import shutil
pp = pprint.PrettyPrinter(indent=4)


# Move to parent dir
cwd= os.getcwd()
cwd="/".join(cwd.split("/")[:-1])
new_dir=cwd+"/data/CompanyInterviewExperience/JSONfiles"

with open(new_dir+"/tags.json") as f:
    data = json.load(f)

tags=data["tags"]
print("Number of entries in tags.json : ",len(tags))

for i,t in enumerate(tags):
	#/home/sruthi/dev/fourth_year/sem_7/SE/placement_portal/data/CompanyInterviewExperience/Amazon_1.txt
	filename=t["filename"]
	filename=filename.split("/")
	tags[i]["filename"]=filename[len(filename)-1]

data["tags"]=tags

with open(new_dir+"/revised_tags.json","w") as f:
    json.dump(data,f)

with open(new_dir+"/revised_tags.json") as f:
    data = json.load(f)
tags=data["tags"]
pp.pprint(tags[0])