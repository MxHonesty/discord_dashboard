def replace_name(nume, html):
    print(html.replace("$NUME_BOT$", nume))

def replace_server(server, html):
    print(html.replace("$NUME_SERVER$", server))

with open("src/index.html") as file:
    text = file.read()
    replace_name('Steli', text)
    replace_server('Server', text)
