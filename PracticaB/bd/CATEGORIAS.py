import sqlite3
con=sqlite3.connect("BlogVentas")
cur=con.cursor()
cur.execute(''' 
CREATE TABLE Categoria(
id_categoria INTEGER PRIMARY KEY,
Nombre_Categoria VARCHAR(30))
''')
listacategoria=[
    (1,"Literatura fantasiosa"),
    (2,"Ciencia ficción"),
    (3,"Fantasía cómica"),
    (4,"Acción"),
    (5,"Ficción de aventuras"),
    ]
cur.executemany("INSERT INTO Categoria VALUES(?,?)",listacategoria)
con.commit()
con.close()
