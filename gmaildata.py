import imaplib, email, os
import re
from getpass import getpass


host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
imap_user = str(input('Ingrese su email:'))
imap_pass = getpass('Ingrese su Password:')
imap.login(imap_user, imap_pass)
imap.select('Inbox')


'''

typ, data = imap.search(None,'FROM', 'ximena.geoffroy@udp.cl')
f=open("ximena.geoffroy@udp.cl.txt","w")
for num in data[0].split():

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print(datito)
    f.write(datito+"\n")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    form=data[0][1].decode()
    print(form)
    f.write(form+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    fe=data[0][1].decode()
    print(fe)
    f.write(fe+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    te=data[0][1].decode()
    arr = None
    arr = te.split("Received:")
    largo = len(arr)
    segundo =arr[largo-2]
    primero = arr[largo-1]
    print(primero)
    f.write(primero+"")
    penultimo = arr[2]

    if primero == penultimo:
        print("El correo tiene 2 received.")
        print(segundo)
        f.write(primero+"")
    else:
        print(penultimo)
        f.write(penultimo+"")
'''
'''
typ, data = imap.search(None,'FROM', 'mensajeria@emailbancoestado.cl')
f=open("mensajeria@emailbancoestado.cl.txt","w")
for num in data[0].split():

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print(datito)
    f.write(datito+"\n")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    form=data[0][1].decode()
    print(form)
    f.write(form+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    fe=data[0][1].decode()
    print(fe)
    f.write(fe+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    te=data[0][1].decode()
    arr = None
    arr = te.split("Received:")
    largo = len(arr)
    segundo =arr[largo-2]
    primero = arr[largo-1]
    print(primero)
    f.write(primero+"")
    penultimo = arr[2]

    if primero == penultimo:
        print("El correo tiene 2 received.")
        print(segundo)
        f.write(primero+"")
    else:
        print(penultimo)
        f.write(penultimo+"")

 '''   
'''
typ, data = imap.search(None,'FROM', 'notificaciones@bancoestado.cl')
f=open("notificaciones@bancoestado.cl.txt","w")
for num in data[0].split():

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print(datito)
    f.write(datito+"\n")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    form=data[0][1].decode()
    print(form)
    f.write(form+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    fe=data[0][1].decode()
    print(fe)
    f.write(fe+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    te=data[0][1].decode()
    arr = None
    arr = te.split("Received:")
    largo = len(arr)
    segundo =arr[largo-2]
    primero = arr[largo-1]
    print(primero)
    f.write(primero+"")
    penultimo = arr[2]

    if primero == penultimo:
        print("El correo tiene 2 received.")
        print(segundo)
        f.write(primero+"")
    else:
        print(penultimo)
        f.write(penultimo+"")
'''
'''
typ, data = imap.search(None,'FROM', 'notifications@discordapp.com')
f=open("notifications@discordapp.com.txt","w")
for num in data[0].split():

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print(datito)
    f.write(datito+"\n")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    form=data[0][1].decode()
    print(form)
    f.write(form+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    fe=data[0][1].decode()
    print(fe)
    f.write(fe+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    te=data[0][1].decode()
    arr = None
    arr = te.split("Received:")
    largo = len(arr)
    segundo =arr[largo-2]
    primero = arr[largo-1]
    print(primero)
    f.write(primero+"")
    penultimo = arr[2]

    if primero == penultimo:
        print("El correo tiene 2 received.")
        print(segundo)
        f.write(primero+"")
    else:
        print(penultimo)
        f.write(penultimo+"")
'''

typ, data = imap.search(None,'FROM', 'Info@communications.openenglish.com')
f=open("Info@communications.openenglish.com.txt","w")
for num in data[0].split():

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
    datito= data[0][1].decode()
    datito=datito.replace("Message-ID:", "")
    datito=datito.replace(">", "")
    datito=datito.replace("<", "")
    datito=datito.replace("Message-Id:", "")
    datito=datito.strip()
    print(datito)
    f.write(datito+"\n")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
    form=data[0][1].decode()
    print(form)
    f.write(form+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
    fe=data[0][1].decode()
    print(fe)
    f.write(fe+"")

    typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
    te=data[0][1].decode()
    arr = None
    arr = te.split("Received:")
    largo = len(arr)
    segundo =arr[largo-2]
    primero = arr[largo-1]
    print(primero)
    f.write(primero+"")
    penultimo = arr[2]

    if primero == penultimo:
        print("El correo tiene 2 received.")
        print(segundo)
        f.write(primero+"")
    else:
        print(penultimo)
        f.write(penultimo+"")



imap.close()
imap.logout()















