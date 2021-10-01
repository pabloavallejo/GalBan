import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

login_data = {
    'Usuario': 'pabloavallejo',
    'Password': 'yo314780JMP',
    'UrlRedireccion': 'https://iol.invertironline.com/'
}  

# Making a get request

url = 'https://micuenta.invertironline.com/ingresar'

url2 = 'https://iol.invertironline.com/MiCuenta/MiPortafolio'

with requests.Session() as s:
    url = 'https://micuenta.invertironline.com/ingresar'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name': '__RequestVerificationToken'})['value']
    r = s.post(url, data=login_data, headers=headers)
    r2 = s.get(url2)
    print(r2.content)


# __RequestVerificationToken: brCETZhkSMBxM7bTxanN8ixeDheIrAPy_lmtLj8bt3RfS8Gqk5eJ4cqJuG0LQXEOXtbcXupmpdgec8GDJmoQNSQmpbY1
# UrlRedireccion: https://iol.invertironline.com/
# Usuario: pabloavallejo
# Password: yo314780JMP