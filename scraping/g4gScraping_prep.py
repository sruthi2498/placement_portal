from bs4 import BeautifulSoup
import requests
import re
import os
import json
# Move to parent dir
cwd= os.getcwd()
cwd="/".join(cwd.split("/")[:-1])
os.chdir(cwd+"/data/CompanyPrepQuestions")
allcomp_dir= os.getcwd()


tags_data={"tags":[]}
filename_tags=cwd+"/data/CompanyPrepQuestions/tags.json"

url ="https://www.geeksforgeeks.org/company-preparation/"
r  = requests.get(url)
data = r.text
main_soup = BeautifulSoup(data, "lxml")

print("Finding all_companies...")
div_left=main_soup.find("div",attrs={'style':'width: 50%; float: left;'}).findAll("li")
div_right=main_soup.find("div",attrs={'style':'width: 50%; float: right;'}).findAll("li")

all_companies =div_left+div_right

j=0
while(j<len(all_companies)):
	all_companies = div_left+div_right
	comp=all_companies[j].find("a" ,href=True)
	
	if(comp):
		comp_url=comp["href"]
		
		name=comp.getText().strip()
		comp_url="https://www.geeksforgeeks.org"+comp_url
		comp_r=requests.get(comp_url)
		print("company ",j,name,comp_url)

		comp_soup=BeautifulSoup(comp_r.text, "lxml")

		pattern = re.compile(r'Show All Articles')
		all_show=comp_soup.findAll("a",attrs={'style':'background-color: #4CB96B;color: #fff;padding: 5px;box-shadow: 0 1px 5px #777;'})
		if(all_show):
			show_all_articles=all_show[0]
			comp_url=show_all_articles["href"]
			
			comp_r=requests.get(comp_url)
			comp_soup=BeautifulSoup(comp_r.text, "lxml")

		content_div=comp_soup.find("div",{"id":"content"})
		all_questions=content_div.findAll("li")

		i=0
		total_q=0
		while(i<len(all_questions)):
			
			filename=os.getcwd()+"/"+name+"_"+str(total_q)+".txt"
			total_q=total_q+1

			content_div=comp_soup.find("div",{"id":"content"})
			all_questions=content_div.findAll("li")

			question=all_questions[i].find("a" ,href=True)
			if(question):
				question_url=question["href"]
				print("\t\tQuestion ",i)
				quest_r=requests.get(question_url)
				quest_soup=BeautifulSoup(quest_r.text, "lxml")

				header_div=quest_soup.find("header",{"class":"entry-header"})
				content=header_div.getText()+"\n\n"

				article_div=quest_soup.find("div",{"class":"entry-content"})


				all_p=article_div.findAll()
				k=0
				while(k<len(all_p)):
					p=all_p[k]
					k=k+1
					if(p.name != 'button' and p.name!="script"):
						text=p.getText()
						if(text):
							no=1
							if("PRACTICE" in text or "adsbygoogle" in text):
								no=0
							elif("If you like GeeksforGeeks and would like to contribute" in text or "Please write comments if you find anything incorrect" in text or "Write your Interview Experience or mail it to contribute@geeksforgeeks.org" in text or "Writing code in comment? Please use ide.geeksforgeeks.org" in text or "Extended Problem" in text or "This article is contributed by" in text):
								k=len(all_p)
								no=0
							if(no):
								content=content+text+"\n"


				tags=quest_soup.findAll("a", {"rel": "category tag"})
				tags=[t.getText() for t in tags]
				#print("\t\ttags : ",tags)
				new_dict={"filename":filename,"company":name,"exp_num":str(total_q),"tags":tags}
				tags_data["tags"].append(new_dict)

				f=open(filename,"w")
				f.write(content)
				f.close()
			i=i+1
	j=j+1


with open(filename_tags,"w") as f:
	json.dump(tags_data,f)
