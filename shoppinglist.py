# Dies ist ein Programm das als Shopping Liste funktionieren soll
 
# Erstellung der Liste
shoppinglist = []

# Funktion um ein Item der Liste hinzuzufügen
def add_item(item):
    shoppinglist.append(item)
    print(f"Der Artikel {item} wurde der Einkaufsliste hinzugefügt")

# Aufruf der Funktion add_item
add_item(input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: "))

# Funktion um die EInkaufsliste anzuzeigen
def show_shoppinglist():
    print("Deine Einkaufsliste:")
    if len(shoppinglist) != 0:
        for i in (shoppinglist):
            print(i)
    else:
        print("Deine Einkaufliste ist leer")

# Aufruf der Funktion show_shoppinglist
show_shoppinglist()