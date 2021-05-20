import MySQLdb
host = "localhost"
user = "lucas"
password = "120301"
db = "hospital"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor()    


def excluir_linha():
    global c
    query = " truncate table ja_chamado "
    c.execute(query)


def select(fields, tables, where= None):
    global c
    query = "SELECT "+ fields+ " FROM " + tables
    if (where):
        query = query + " WHERE "+ where

    c.execute(query)
    return c.fetchall()

def select_name(pos):
    global c
    pos = str(pos)
    query = "SELECT nome from pacientes_novos where id_paciente = "+pos

    c.execute(query)
    return c.fetchall()

def select_maxmin():
    global c
    query = "SELECT id_pac, prioridade FROM fila_pacientes ORDER BY prioridade DESC, id_pac ASC"
    c.execute(query)
    return c.fetchall()


def insert_ja_chamados(id_paciente, value):
    value = str(value)
    value = "'"+value+"'"
    id_paciente = str(id_paciente)
    id_paciente = "'"+id_paciente+"'"
    global c, con
    query = "INSERT INTO ja_chamado " 
    query = query + " VALUES " + "("+id_paciente+","+value+")"
    c.execute(query)
    con.commit()

def insert(table1, fields=None):
    nome =  str(input("Nome paciente: "))                                              
    nome = "'"+nome+"'"
    data = str(input("Data nascimento AAAA-MM-DD: ")) 
    data = "'"+data+"'"
    tipo_sang = str(input("Tipo sanguineo: "))
    tipo_sang = "'"+ tipo_sang+"'"
    prioridade = str(input("Prioridade: "))
    prioridade = "'"+prioridade+"'"

    global c, con
    query1 = "INSERT INTO " + table1
    query2 = "INSERT INTO fila_pacientes " 
    if (fields):
        query = query1 +" (" + fields + ") "
    query1 = query1 + " VALUES " + "(DEFAULT,"+nome+","+tipo_sang+","+prioridade+","+data+")"
    query2 = query2 + " VALUES " + "(DEFAULT,"+prioridade+")"
    
    c.execute(query1)
    c.execute(query2)
    con.commit()

def ultimo_ci():
    global c
    query = "SELECT * FROM ja_chamado LIMIT 5"
    c.execute(query)
    return c.fetchall()

def delet(pessoa):
    global c
    pessoa = str(pessoa)
    query = " DELETE FROM fila_pacientes WHERE id_pac = "+pessoa
    c.execute(query)
    con.commit()
