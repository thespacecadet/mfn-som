import mysql.connector

cnx = mysql.connector.connect(user='spacecadet', password='3smashing3',
                              host='127.0.0.1',
                              database='ikon')
cursor = cnx.cursor()

# enter into the query "test3" for the full data, and "dataset10" for a 10 row sample
query = "SELECT project_abstract,min(id),min(title) \
        FROM test3 WHERE project_abstract NOT LIKE '%Keine Zusammenfassung%' \
                                GROUP BY project_abstract"



cursor.execute(query)
data = cursor.fetchall()
cnx.close()