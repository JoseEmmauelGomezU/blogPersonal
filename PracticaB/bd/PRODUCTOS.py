import sqlite3
con=sqlite3.connect("BlogVentas")
cur=con.cursor()
cur.execute(''' 
CREATE TABLE Productos(
id_productos INTEGER PRIMARY KEY,
id_tipo INTEGER,
Titulo VARCHAR(50),
Autor_Artista VARCHAR(30),
Precio INTEGER)
''')
listaproductos=[
    (1,"LITERATURA","OVERLORD:El rey no muerto","Kugane Maruyama",289),
    (2,"LITERATURA","Overlord Vol.2:The Dark Warrior","Kugane Maruyama",289),
    (3,"LITERATURA","Overlord Vol.3:The Bloody Valkyrie","Kugane Maruyama",249),
    (4,"LITERATURA","Overlord Vol. 4: The Lizardman Heroes","Kugane Maruyama",330),
    (5,"MUSICA","Brave Shine","Aimer",400),
    (6, "MUSICA", "Song Machine: Season One - Strange Timez", "Gorillaz", 499),
    (7, "MUSICA", "Future Nostalgia", "Dua Lipa", 399),
    (8, "MUSICA", "Fine Line", "Harry Styles", 450),
    (9, "MUSICA", "When We All Fall Asleep, Where Do We Go?", "Billie Eilish", 350),
    (10, "MUSICA", "Rumors", "Lizzo", 299)
    ]
cur.executemany("INSERT INTO Productos VALUES(?,?,?,?,?)",listaproductos)
con.commit()
con.close()
