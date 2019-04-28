import sqlite3
from sqlite3 import Error
import os
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.isolation_level = None
        return conn
    except Error as e:
        print(e)
 
    return None
  
def consulta(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def readfile(file):
    if os.path.exists(file):
        with open(file, 'r') as f:
            try:
                regs = f.readlines()
                return regs
            except:
                return None    

def insertadatos(database, file):

    regs = readfile(file)

    if regs:
        with create_connection(database) as conn: 
            try:
                cur = conn.cursor()
                cur.execute("begin")
                for r in regs:
                    cur.execute(r.strip())
                    #print(r)
                cur.execute("commit")
                print(" Registros ",cur.lastrowid)
                return True
            except:
                print(" ERROR en ", r.strip())
                cur.execute("rollback")
                return False        
    else:
        print("No se pudo abrir el archivo o no existen datos en ", file)        
        return False   


def main():
    database = "/home/ciecbase/db.sqlite3"
    pathd = "/home/datos/"
    #catalogos = ['tipo_movimiento','tipo_documento','situacion','banco','condominio','proveedore','periodo','cuenta_contable']
    #condominio = ['sadi_asiento','sadi_condomino','sadi_estacionamiento','sadi_condomino_estacionamiento','sadi_cuenta_banco','sadi_documento',,'sadi_detalle_movimiento','sadi_movimiento']
    condominio =  ['sadi_condomino','sadi_movimiento']

    for t in condominio:
        file  = pathd + t + ".sql"
        with create_connection(database) as conn: 
            consulta(conn, "select count(*) as registros from " + t )
            print(t)
            insertadatos(database, file)
    
if __name__ == '__main__':
    main()
 