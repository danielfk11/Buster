Linguagem utilizada 

    Python 3.6

Imports  

    import requests
    import whois11
    import os
    import time

O que e?

Simulando o dirb ou gobuster usado no kali linux de uma forma recriada em python ele tem a funcao de buscar diretorios e subdominios de um site para buscar informacoes a fim de encontrar vulnerabilidades.

Formato URL

    [SITE.COM.BR]

Como funciona?

Ao iniciar o codigo ele ira perguntar a url que voce deseja buscar
escolhendo a wordlist para buscar diretorios [/admin, /login, /index] apos finalizar ele vai pedir outra wordlist para buscar subdominios do site [admin.site.com.br, webmail.site.com.br] ao finalizar a busca ele salva o HTML principal da url no arquivo save.html e ao finalizar ele pergunta se quer mostrar informacoes do site como dominio, emails, etc...

DOWNW

    Downloader de wordlists pelo rawcontent do github 

OBS

    estou disponibilizando 2 wordlists, uma para diretorios e outra para subdominios, voce pode baixar mais e usa-las.

Wordlists

    Salve wordlists na pasta e quando for usar remova os .txt de dentro das pastas.
    
Version

    v1.1.0
