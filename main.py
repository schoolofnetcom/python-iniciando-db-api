import MySQLdb
from MySQLdb import connect

user = 'root'
password = 'root'
database = 'son_python_db_api'
host = '127.0.0.1'
port = 3306

# PEP 249
db = connect(
    user=user,
    passwd=password,
    db=database,
    host=host,
    port=port,
    autocommit=True
)
print('Conexão feita com sucesso')

# MÉTODOS DE UMA INSTÂNCIA CONNECTION
# db.close()

# db.commit()

# db.rollback()

# db.cursor()

cursor = db.cursor()

# INTERAGINDO COM CURSORES
#########################
# row_affected = cursor.execute('SELECT * FROM bank_accounts')
# print(row_affected)
#
# #print(list(cursor))
#
# rows = cursor.fetchall()
# print(rows)
# for row in rows:
#     print(row)
#
# for row in cursor:
#     print(row)

# CHAMANDO SEQUENCIALMENTE OS MÉTODOS FETCHES
############################################
# cursor.execute('SELECT * FROM bank_accounts')
# print(cursor.fetchone())
# print(cursor.fetchall())

# cursor.execute('SELECT * FROM bank_accounts')
# row = cursor.fetchone()
# while row is not None:
#     print(row)
#     row = cursor.fetchone()

# QUANDO USAR O FETCHONE
#######################
# cursor.execute('SELECT * FROM bank_accounts WHERE number = "0001-02"')
# ##row = cursor.fetchall()
# row = cursor.fetchone()
# print(row)

# USANDO FETCHMANY
#################
# cursor.execute('SELECT * FROM bank_accounts')
#
# rows = cursor.fetchmany(2)
#
# print(rows)
#
# rows = cursor.fetchall()
#
# print(rows)
#
# print(cursor.fetchmany(2))

# INSERINDO INFORMAÇÕES NO BANCO DE DADOS
########################################
# cursor.execute("""INSERT INTO
#                   `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
#                   VALUES ('1111-99','Outro fulano da Silva','123456',450.50,0,1)""")
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))
# #db.commit()


# ATUALIZANDO E EXCLUINDO INFORMAÇÕES
########################################
# row_affected = cursor.execute("""UPDATE `bank_accounts`
#                   SET `value` = 10000 WHERE number ='1111-99'""")
# print(row_affected)
# print(cursor.rowcount)
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))

# row_affected = cursor.execute("DELETE FROM `bank_accounts` WHERE number ='1111-99'")
# print(cursor.rowcount)
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))

# SQL Injection
##############
# name = "Luiz Carlos' , value = 100000, name = 'Luiz Carlos" #SQL Injection
# cursor.execute("""UPDATE `bank_accounts`
#                   SET `name` = '%s' WHERE number ='0001-01'""" % name)
#
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))

# EXECUÇÃO DE QUERIES COM PARÂMETROS
####################################
# name = "Luiz Carlos' , value = 100000, name = 'Luiz Carlos1111"  # SQL Injection
# number = '0001-01'
# cursor.execute("""UPDATE `bank_accounts` SET `name` = %s WHERE number = %s""",
#                (name, number)
#                )
# cursor.execute("""INSERT INTO
#                `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
#                  VALUES (%s,%s,%s,%s,%s,%s)""",
#                ('2222-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1))
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))

# EXECUÇÃO DE QUERIES MÚLTIPLAS
# cursor.executemany("""INSERT INTO
#                       `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
#                       VALUES (%s,%s,%s,%s,%s,%s)""",
#                    (
#                        ('9223-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1),
#                        ('9224-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1),
#                        ('9225-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1),
#                        ('9226-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1),
#                    )
#                    )
# cursor.execute('SELECT * FROM bank_accounts')
# print(tuple(cursor))

# PEGAR O ÚLTIMO ID GERADO PELO BANCO DE DADOS
##############################################
# cursor.execute("""INSERT INTO
#                `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
#                  VALUES (%s,%s,%s,%s,%s,%s)""",
#                ('0000-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1))
# print(cursor.lastrowid)
# cursor.execute('SELECT * FROM bank_accounts')
# print(list(cursor))

db.autocommit(False)
try:
    cursor.execute("""INSERT INTO
                   `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
                     VALUES (%s,%s,%s,%s,%s,%s)""",
                   ('5555-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1))
    cursor.execute("""INSERT INTO
                   `bank_accounts` (`number`,`name`,`password`,`value`,`admin`,`agency_id`)
                     VALUES (%s,%s,%s,%s,%s,%s)""",
                   ('5556-99', 'Outro fulano da Silva', '123456', 450.50, 0, 1))
    db.commit()
except:
    db.rollback()

cursor.execute('SELECT * FROM bank_accounts')
print(list(cursor))