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

# Citeste index.html ca string
def read_main_page():
    with open("src/index.html") as f:
        return f.read()

# Citeste template-ul pentru grid server ca string
def read_server_holder():
    with open("src/server_grid.html") as f:
        return f.read()

#test_list = ["Server1" , "Server2", "Server3", "Server4", "ServerNeb"] # Lista nume servere

# Functia care primeste lista de nume ale serverelor
# Si returneaza html-ul final ca string
def get_appened_html(list):

    # Index html
    html = read_main_page()

    # Template server grid
    template = read_server_holder()

    # Html final cu listat aduagata
    html_final = ""

    for element in list:   # Pentru fiecare element din lista
        personalizat = replace_server(element, template)    # Inlocuieste numele serverului in template
        html_final = html_final + personalizat              # Adauga template-ul inlocuit in acelasi string

    return add_server_list(html_final, html)

# Functia care primeste lista si numele botului si returneaza html-ul final pentru afisat
def get_final_html(list, nume_bot):
    return replace_name(nume_bot, get_appened_html(list))
