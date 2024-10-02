# Dies ist ein Programm das als Shopping Liste funktionieren soll
 
# Erstellung der Liste
shoppinglist = []

# Funktion um ein Item der Liste hinzuzufügen
def add_item(x):
    item = x
    shoppinglist.append(item)
    print(f"Der Artikel {item} wurde der Einkaufsliste hinzugefügt")
    print(shoppinglist)

# Aufruf der Funktion
add_item(input("Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll: "))