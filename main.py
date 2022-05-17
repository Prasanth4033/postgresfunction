import psycopg2


conn = psycopg2.connect(
    database="postgres", user='postgres', password='postgres', host='192.168.0.0', port='12345'
)
conn.autocommit = True
cursor = conn.cursor()
location = 2
nodealias = 'Wendy Darling'
if location == 1:
    cursor.execute('''select id from books where name like ('%%Crooked%%') and id in (%s) UNION select id from 
    characters where name like ('%%Peter%%') and id in (%s)''' % (location, location))
elif nodealias == "Wendy Darling":
    cursor.execute('''select id from books where id in (2) and name in ('%s') UNION select id from 
        characters where id in (2) and name in ('%s')''' % (nodealias, nodealias))

result = cursor.fetchall()
ref_circuit_design_id = [i[0] for i in result]
conn.commit()
conn.close()



