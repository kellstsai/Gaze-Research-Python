import mysql.connector
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

connection = mysql.connector.connect(
    host='localhost',
    user='kellytsai',
    password='coffee',
    database = 'my_database'
)

cursor = connection.cursor()

csv_data = pd.read_csv('c:\\Users\\Kelly\\Desktop\\Research\\Data\\LeftPC\\YennhiThoa\\covid19charts\\result\\user1\\User 0_all_gaze.csv')

filtered_data = csv_data[csv_data['CS'].isin([1,3])]

insert_query = """
    INSERT INTO user1_all_gaze_data (MEDIA_ID, MEDIA_NAME, CNT, TIME, TIMETICK, FPOGX, FPOGY, CS)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

for index, row in filtered_data.iterrows():
    cursor.execute(insert_query, (
        row['MEDIA_ID'],
        row['MEDIA_NAME'],
        row['CNT'],
        row['TIME(2024/03/12 12:23:38.733)'],  
        row['TIMETICK(f=10000000)'],
        row['FPOGX'],
        row['FPOGY'],
        row['CS']
    ))

connection.commit()

print(f"{cursor.rowcount} rows were inserted.")

print("CSV Data: ")
print(filtered_data)
#print(csv_data.head(csv_data))

cursor.close()
connection.close()