__version__ = '0.1.1'

  
import sys
import os
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print('Informe o nome do arquivo de emails')
    sys.exit(1)

filename = arguments[0]
templatename  =  arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


with smtplib.SMTP(host="localhost", port=8025) as server:


    for line in open(filepath):
        name, email = line.split(',')

        text = (
            open(templatepath).read() 
            % {
                'nome': name, 
                'produto': 'caneta', 
                'texto': 'Escrever muito bem', 
                'link': 'https://', 
                'quantidade': 1, 
                'preco': 50.5,
            }
        )

        from_ = "henrique.ccda@gmail.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = from_
        message["To"] = to

        server.sendmail(from_, to, message.as_string()) 
