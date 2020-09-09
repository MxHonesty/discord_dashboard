def replace_name(nume, html):
    print(html.replace("$NUME_BOT$", nume))

def replace_server(server, html):
    print(html.replace("$NUME_SERVER$", server))

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

print(read_main_page())
print(read_server_holder())
