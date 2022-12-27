#!/usr/bin/env python3
"""Exemplos de envia de e-mail"""

import smtplib

SERVER = "localhost"
PORT = 8025


FROM = "henrique.ccda@gmail.com"
TO = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo</b>
"""

# SMPT
message = f"""\
From: {FROM}
To: {", ".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
