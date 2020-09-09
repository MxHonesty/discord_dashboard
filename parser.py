def replace_name(nume, html):           # introduce numele botului in html principal
    return html.replace("$NUME_BOT$", nume)

def replace_server(server, html):
    return html.replace("$NUME_SERVER$", server)    #introduce numele serverului in template

def add_server_list(lista_finala, html):    # introduce lista finala cu toate serverele in html principal
    return html.replace("$SERVER$", lista_finala)

#with open("src/index.html") as file:
#    text = file.read()
#    replace_name('Steli', text)
#    replace_server('Server', text)

#with open("src/server_grid.html") as file:
#    print(file.read())

def read_main_page():
    with open("src/index.html") as f:
        return f.read()

def read_server_holder():
    with open("src/server_grid.html") as f:
        return f.read()

html = read_main_page()
template = read_server_holder()

test_list = ["Server1" , "Server2", "Server3", "Server4"]

html_final = ""

for element in test_list:
    personalizat = replace_server(element, template)
    html_final = html_final + personalizat

print(add_server_list(html_final, html))
