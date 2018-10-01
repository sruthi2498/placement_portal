import os
import json
import pprint 
import shutil
pp = pprint.PrettyPrinter(indent=4)


# Move to parent dir
cwd= os.getcwd()
cwd="/".join(cwd.split("/")[:-1])
new_dir=cwd+"/data/CompanyInterviewExperience"

with open(new_dir+"/tags.json") as f:
    data = json.load(f)

tags=data["tags"]
all_tag_names=[]
print("Number of entries in tags.json : ",len(tags))

for i,t in enumerate(tags):
	all_tag_names.append(t["tags"])

all_tag_names = [item for sublist in all_tag_names for item in sublist]
all_tag_names=list(set(all_tag_names))
print("Total number of tags : ",len(all_tag_names))


with open(new_dir+"/all_tags.json","w") as f:
    json.dump(all_tag_names,f)



with open(new_dir+"/all_tags.json") as f:
    data = json.load(f)
    data=sorted(data)

tag_files={}
for tag in data:
	tag_files[tag]=[]
	