import imaplib
import pprint
import re 
from getpass import getpass


with open('Datos.txt') as d:
    datos = d.read().splitlines()
    FROM = datos[0]
    EXPREG = datos[1]

imap_host = 'imap.gmail.com' 
imap_user = str(input('Ingrese su email:'))
imap_pass = getpass('Ingrese su Password:')
imap = imaplib.IMAP4_SSL(imap_host)
imap.login(imap_user, imap_pass)
imap.select('Inbox')
tmp, data = imap.search(None,'(FROM "'+FROM+'")')

for itera in data[0].split(): 
        tmp, data = imap.fetch(itera, '(BODY[HEADER.FIELDS (FROM MESSAGE-ID DATE)])')
        print('Numero de mensaje en la bandeja de entrada:{0}'.format(itera.decode("utf-8")))
        aux = str(data[0][1]).replace('\r\n', '\n')
        mail = re.compile(r""""""+EXPREG+"""""", re.X)
        mails =  data[0][1].decode('utf-8')
        if re.search(mail, mails):
            x = mail.findall(mails)
            print(str(x)+' Se confirma que es un emisor real\n')
        else:
            print('ALERTA, POSIBLE PHISHING!.\n')
imap.close()