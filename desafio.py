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

cursor.execute(queries.drop_transactions_table)
cursor.execute(queries.transactions_table)

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


'''
Fase 2 – Análise sobre as taxas:
Utilizando a tabela de transações e a de taxas, você deve implementar trechos de código 
que respondam as seguintes perguntas:
'''

cursor.execute(queries.drop_transactions_table)
cursor.execute(queries.drop_fees_table)
cursor.execute(queries.transactions_table)
cursor.execute(queries.fees_table)


'''
1. Considerando que a carteira origem é responsável por pagar as taxas de envio, 
qual carteira seria responsável pelo maior pagamento de taxas em janeiro de 2021?
'''

cursor.execute(queries.f2_q1)
maior_taxa_jan = cursor.fetchone()


# 2. E em fevereiro de 2021?

cursor.execute(queries.f2_q2)
maior_taxa_fev = cursor.fetchone()


# 3. Qual é o id da transação com a maior taxa paga?

cursor.execute(queries.f2_q3)
transacao_maior_taxa = cursor.fetchone()


# 4. Qual é a média de taxa paga considerando todas as transações realizadas?

cursor.execute(queries.f2_q4)
media_taxas = cursor.fetchone()