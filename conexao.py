#pip3 instal psycopg2
#pip3 install psycopg2-binary
import psycopg2

try:
    con = psycopg2.connect('host = localhost dbname=projeto user=admin password=4linux port=5432')
    cur = con.cursor()
    # cur.execute("insert into pessoas(nome, email, idade, telefone) values('Lu', 'Lu2@outlook.com', 30, '40209')")
    cur.execute("select * from pessoas")
    conteudo = cur.fetchall()
    print(conteudo)
    # fetchall fetchone
    print('conectou com sucesso!')
   
    con.commit()
    cur.close()
    con.close()
except Exception as e:
    print('Erro conexão: {}'.format(e))
    cur.rollback() #voltar o commit anterior 

# imprimir tudo palavra por palavra
for x in conteudo:
    if x[0] == 10:
        print(x)



