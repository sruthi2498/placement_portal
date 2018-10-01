import os
import json
import pprint 
import shutil
pp = pprint.PrettyPrinter(indent=4)

# Move to parent dir
cwd= os.getcwd()
cwd="/".join(cwd.split("/")[:-1])
new_dir=cwd+"/data/CompanyInterviewExperience/JSONfiles"
with open(new_dir+"/revised_tags.json") as f:
    tags = json.load(f)
    tags=tags["tags"]
    print(len(tags))
with open(new_dir+"/all_tags.json") as f:
    all_tags = json.load(f)

tag_files={}

for i,t in enumerate(tags):
	tf=t["tags"]
	filename=t["filename"]
	for tag in tf :
		if tag not in tag_files:
			tag_files[tag]=[filename]
		else:
			tag_files[tag].append(filename)

#pp.pprint(tag_files)
with open(new_dir+"/tags_filenames.json","w") as f:
    json.dump(tag_files,f)

company_files={}

for i,t in enumerate(tags):
	company=t["company"]
	filename=t["filename"]
	if company not in company_files:
		company_files[company]=[filename]
	else:
		company_files[company].append(filename)

#pp.pprint(company_files)
with open(new_dir+"/company_filenames.json","w") as f:
    json.dump(company_files,f)

 