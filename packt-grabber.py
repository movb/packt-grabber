__author__ = 'Mike'

# Grab free Pack books

import requests
from bs4 import BeautifulSoup

email    = 'YOUR_EMAIL_HERE'
password = 'YOUR_PASSWORD_HERE'

form_url = 'https://www.packtpub.com/packt/offers/free-learning'

def claim_book(form_url, email, password):
    s = requests.Session()
    r = s.get(form_url)
    soup = BeautifulSoup(r.text)

    form = soup.find(attrs={"name": "form_build_id"})
    if not form:
        print 'Cannot find login form'
        return

    payload = {
        'email': email,
        'password': password,
        'op': 'Login',
        'form_build_id': form.id,
        'form_id': 'packt_user_login_form'
    }
    r = s.post(form_url, data=payload)
    soup = BeautifulSoup(r.text)
    if soup.find('div', class_='error'):
        print 'Login failed'
        return

    url = soup.find('a', class_='twelve-days-claim')
    if not url:
        print 'Failed to find claim url'

    r = s.get('https://www.packtpub.com'+url['href'])

    if r.status_code == 200:
        print 'Success'
    else:
        print 'Error claiming book'

    # messages error


if __name__ == "__main__":
    claim_book(form_url, email, password)