import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "artem.suchov@gmail.com"
    password = "secret"

    receiver = "artem.suchov@gmail.com"
    context = ssl.create_default_context()

    message = """\
    Subject: Hi!
    How are you?
    Bye!
    """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
