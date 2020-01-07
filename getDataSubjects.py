#similar to getData, only this script delivers data per subject
import mysql.connector

cnx = mysql.connector.connect(user='spacecadet', password='3smashing3',
                              host='127.0.0.1',
                              database='ikon_som')
cursor = cnx.cursor()


query = "select * from (SELECT project_abstract,min(id) as pro_id \
	FROM ikon_som.projects \
    where project_abstract NOT LIKE '%Keine Zusammenfassung%' \
    GROUP BY project_abstract) as a \
    LEFT JOIN (SELECT project_id, subject_area from ikon_som.subject_area) as c \
    ON c.project_id = a.pro_id \
    LIMIT 100;"


cursor.execute(query)
data = cursor.fetchall()

cnx.close()