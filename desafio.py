import pymysql
import queries

db = pymysql.connect(host='dhauz-instance.cutloqirhpd7.us-east-1.rds.amazonaws.com', user='candidate_user',
                     password='D3@bGh664%$1VHv*', database='db_hiring_test', port=3306)

cursor = db.cursor()

'''
Fase 1 – Análise sobre as transações:
Utilizando a tabela de transações, você deve implementar trechos de código 
que respondam as seguintes perguntas:
'''


# 1. Qual é o endereço (carteira) com maior volume de transações enviadas?
cursor.execute(queries.f1_q1)
cart_maior_vol = cursor.fetchone()


# 2. Qual é o dia do mês com maior volume de transações realizadas?
cursor.execute(queries.f1_q2)
dia_maior_vol = cursor.fetchone()


# 3. Em qual dia da semana geralmente mais transações são realizadas?
cursor.execute(queries.f1_q3)
dia_mais_transf = cursor.fetchone()


'''
4. Quais transações possuem condições atípicas e precisam ser validadas com 
o time responsável pela disponibilização dos dados?
'''
# Existem transações que possuem a mesma carteira como origem e destino.
cursor.execute(queries.f1_q4)
transf_atipicas = cursor.fetchall()


'''
5. Qual a carteira com o maior saldo final? 
(considere que todas as carteiras estejam zeradas no início das análises
e que seja possível existir saldo negativo).
'''
cursor.execute(queries.f1_q5)
cart_maior_saldo = cursor.fetchone()
