from db import fetchall
print("TABELLA UTENTI")
result = fetchall("Select * from utenti")
print(result)

print("TABELLA ORDINI")
result = fetchall("Select * from ordini")
print(result)

print("#"*5 + "citta" + "#"*5)
citta = input("Inserisci città: ")
result = fetchall("""
SELECT *
FROM ordini AS o
JOIN carrello AS ca ON o.id_carrello = ca.id_carrello
JOIN utenti AS u ON ca.id_utente = u.id_utente 
WHERE u.citta LIKE %s
""", [f"%{citta}%"])
print(result)


from db import fetchall

print("\n" + "="*40)
print("TABELLA UTENTI")
print("="*40)

result = fetchall("Select * from utenti")
for r in result:
    print(f"- id_utente: {r['id_utente']}, "
          f"nome: {r['nome']}, "
          f"cognome: {r['cognome']}, "
          f"citta: {r['citta']}, "
          f"id_ruolo: {r['id_ruolo']}")

print("\n" + "="*40)
print("TABELLA ORDINI")
print("="*40)

result = fetchall("Select * from ordini")
for r in result:
    print(f"- id_ordine: {r['id_ordine']}, "
          f"stato: {r['stato']}, "
          f"anno: {r['anno']}, "
          f"id_carrello: {r['id_carrello']}")

print("\n" + "#"*5 + " CITTA' " + "#"*5)
citta = input("Inserisci città: ")

result = fetchall("""
SELECT *
FROM ordini AS o
JOIN carrello AS ca ON o.id_carrello = ca.id_carrello
JOIN utenti AS u ON ca.id_utente = u.id_utente 
WHERE u.citta LIKE %s
""", [f"%{citta}%"])

print("\n" + "="*40)
print(f"RISULTATI PER CITTA': {citta}")
print("="*40)

if not result:
    print("Nessun ordine trovato.")
else:
    for r in result:
        print(f"- id_ordine: {r['id_ordine']}, "
              f"stato: {r['stato']}, "
              f"anno: {r['anno']}, "
              f"id_carrello: {r['id_carrello']}, "
              f"id_utente: {r['id_utente']}, "
              f"nome: {r['nome']}, "
              f"cognome: {r['cognome']}, "
              f"citta: {r['citta']}, "
              f"id_ruolo: {r['id_ruolo']}")





























































































































































