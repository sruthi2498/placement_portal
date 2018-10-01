from bs4 import BeautifulSoup
import requests
import re
import os
import json
import time
# Move to parent dir
cwd= os.getcwd()
cwd="/".join(cwd.split("/")[:-1])
new_dir=cwd+"/data/CompanyInterviewExperience"
os.chdir(cwd+"/data/CompanyInterviewExperience")
allcomp_dir= os.getcwd()

with open(new_dir+"/tags.json") as f:
    tags_data = json.load(f)
#tags_data={"tags":[]}
filename_tags=cwd+"/data/CompanyInterviewExperience/tags.json"

url =("https://www.geeksforgeeks.org/company-interview-corner/")
r  = requests.get(url)
data = r.text
main_soup = BeautifulSoup(data, "lxml")
t1=time.time()
print("Finding all_companies...")
all_companies = main_soup .findAll("li", {"class": "sLiClass"})
all_tags=[]
j=250

while(j<len(all_companies)):
	all_companies = main_soup.findAll("li", {"class": "sLiClass"})
	comp=all_companies[j].find("a" ,href=True)
	comp_url=comp["href"]
	j=j+1
	m=re.search(r'([A-Za-z -\.])*',comp.getText())
	name=m.group(0).strip()
	print("company ",j,name)

	comp_r=requests.get(comp_url)
	comp_soup=BeautifulSoup(comp_r.text, "lxml")

	total_q=1
	found_all=0
	page=1
	while(found_all==0):
		print("\tPage",page)
		all_questions=comp_soup.findAll("h2", {"class": "entry-title"})

		i=0
		while(i<len(all_questions)):
			
			filename=os.getcwd()+"/"+name+"_"+str(total_q)+".txt"
			total_q=total_q+1
			all_questions=comp_soup.findAll("h2", {"class": "entry-title"})
			question=all_questions[i].find("a" ,href=True)
			question_url=question["href"]
			print("\t\tQuestion ",i)
			quest_r=requests.get(question_url)
			quest_soup=BeautifulSoup(quest_r.text, "lxml")

			content_div=quest_soup.find("div", {"class": "entry-content"})
			content=""
			all_p=content_div.findAll("p")
			for p in all_p:
				text=p.getText()
				no=1
				if("If you like GeeksforGeeks and would like to contribute" in text or "Please write comments if you find anything incorrect" in text or "Write your Interview Experience or mail it to contribute@geeksforgeeks.org" in text or "Writing code in comment? Please use ide.geeksforgeeks.org" in text):
					no=0
				if(no):
					content=content+text+"\n"

			tags=quest_soup.findAll("a", {"rel": "category tag"})
			tags=[t.getText() for t in tags]
			all_tags=list(set(tags+all_tags))
			#print("\t\ttags : ",tags)
			new_dict={"filename":filename,"company":name,"exp_num":str(total_q-1),"tags":tags}
			tags_data["tags"].append(new_dict)

			f=open(filename,"w")
			f.write(content)
			f.close()
			i=i+1

		next_page=comp_soup.find("a",{"class": "nextpostslink"},href=True)
		if(next_page==None):
			found_all=1
			print("len(tags_data['tags']))",len(tags_data['tags']))
		else:
			page=page+1
			next_page_url=next_page["href"]

			comp_r=requests.get(next_page_url)
			comp_soup=BeautifulSoup(comp_r.text, "lxml")

with open(filename_tags,"w") as f:
	json.dump(tags_data,f)
t2=time.time()
print(t2-t1)