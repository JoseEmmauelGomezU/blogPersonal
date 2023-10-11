import sqlite3
con=sqlite3.connect("BlogVentas")
cur=con.cursor()
cur.execute(''' 
CREATE TABLE Genero(
id_Genero INTEGER PRIMARY KEY,
Nombre_Genero VARCHAR(30))
''')
listagenero=[
    (1,"Rock en español"),
    (2,"J-Pop"),
    (3,"Urbano latino"),
    (4,"Hip-hop/Rap"),
    (5,"Argentinian Trap"),
    ]
cur.executemany("INSERT INTO Genero VALUES(?,?)",listagenero)
con.commit()
con.close()
