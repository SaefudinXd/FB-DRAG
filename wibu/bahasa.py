from modul import *

def lang(url,cookie):
	try:
		respon=req.get(f"{url}/language.php",cookies=cookie).text
		saatini=parser(respon,"html.parser").find("strong",{"class":False})
		saatini=saatini.text.replace("Bahasa ","").replace("Basa ","") if saatini is not None else saatini
		#print(" ! yahahah jawa:v" if "Jawa" in saatini else "")
		print(f" ! bahasa {saatini} terdeteksi, mohon tunggu sedang memindahkan ke bahasa Indonesia" if saatini is not None else " ! memindahkan bahasa, mohon tunggu..")
		for x in parser(respon,"html.parser").find_all("a",{"href":True}):
			if "id_ID" in x["href"]:
				req.get(url+x["href"],cookies=cookie)
	except koneksi_error: exit(" ! kesalahan pada koneksi")
		