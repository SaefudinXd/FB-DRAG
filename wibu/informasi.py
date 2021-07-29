from modul import *

def generate(cookie,html,username=None):
	for x in html.find_all("a",href=True):
		if "/friends?" in x["href"]:
			if "Teman" in x.text:
				username=re.search("\/(.*?)\/friends\?",x["href"]).group(1)
	uid=re.search("c_user=(\d*)",cookie).group(1)
	open("cookies/info.txt","w").write(json.dumps({"uid":uid,"nama":html.find("title").text,"username":username,"cookies":{"cookie":cookie}}))