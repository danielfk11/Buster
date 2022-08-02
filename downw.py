import time
import requests

#como usar?
#nesse codigo github tem a maioria das wordlists para que voce possa usar, esse sistema foi feito para baixar e deixar o programa mais pratico 
#para pegar o rawcontent e so ir na wordlist selecionada e clicar no [RAW] que fica do lado direito do codigo 
#BOM USO!

print()
print("                  WORDLISTS                 ")
print("[https://github.com/danielmiessler/SecLists]")
perg = input("Digite o rawcontent [github] da wordlist: \n-> ")
wlist = input("Digite o nome que deseja salvar a wordlist: \n-> ")

try:
    r = requests.get(perg)
    rtext = r.text
except:
    print("rawcontent incorreto..")

if wlist:
    wlist = f'{wlist}.txt'
try:
    with open(wlist, "w") as wlist_Create:
        wlist_Create.write(rtext)
        time.sleep(2)
        print("wordlist criada com sucesso [{}]".format(wlist))
except:
    print("error")
    exit()