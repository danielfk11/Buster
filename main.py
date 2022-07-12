import requests
import whois11
import os

arqs = [f for f in os.listdir('.') if os.path.isfile(os.path.join('.', f)) and f.endswith('.txt')]

GREEN = "\033[0;32m"
RED   = "\033[1;31m"
mytimeout = (2, 5)

url = input('-> URL\n-> ')

if "http" in url:
    print("Informe a URL sem o HTTP\n -> [EXAMPLE][SITE.COM]")
    exit()

print('WORDLISTS ->', arqs)
wrlist = input('-> WORDLIST\n-> ')

if wrlist not in arqs:
    print("Selecione uma wordlist valida!")
    print("->", arqs)
    exit()

else:
    with open(wrlist, "r") as buster:
        buster = buster.readlines()
        buster = list(map(lambda s: s.strip(), buster))
        bust = buster

    for i in bust:
        url_check = f'''https://www.{url}/{i}'''
        r = requests.get(url_check)
       
        if r.status_code == 200:
            print(GREEN,url_check, '[',r.status_code,']')
        else:
            continue

    print("\033[0;0m")

    print('WORDLISTS ->', arqs)
    wrlist_sub = input('-> WORDLISTS SUBDOMAIN\n-> ')      

    with open(wrlist_sub, "r") as buster_subdomain:
        buster_subdomain = buster_subdomain.readlines()
        buster_subdomain = list(map(lambda s: s.strip(), buster_subdomain))
        bustsub = buster_subdomain  

    for x in bustsub:
        url_check_sub = f'''https://{x}.{url}'''
        try: 
            r_sub = requests.get(url_check_sub, timeout=mytimeout)
            print(GREEN,url_check_sub, "[ACESSADO]")
        except:
            continue    

print("\033[0;0m")

print("Criando html da URL..")    

gethmtl = f'''https://{url}'''
rhtml = requests.get(gethmtl)
html = rhtml.text

try:
    with open('save.html', "w", encoding="utf-8") as htmltext:
        htmltext.write(html)
        print("HTML criado em save.html")
except:
    print("Nao foi possivel criar o arquivo html.")


text_whois = input("Deseja procurar info pelo WHOIS11? \n-> Digite S para sim\n-> Digite N para nao\n-> ")

if text_whois not in ['S', 'N']:
    print("Valor digitado incorretamente..")
    text_whois = input("Deseja procurar info pelo WHOIS11? \n-> Digite S para sim\n-> Digite N para nao\n-> ")

if text_whois == 'S':
    model = f'''[MODEL = {url}]'''
    print(model)
    print("Pegando informacoes da URL..")
    print(whois11.whois(url))

if text_whois == 'N':
    print("Saindo...")
    exit()

