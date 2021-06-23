import sqlite3
def assist_record():

        try:
            sqliteconnect=sqlite3.connect('assistant_record.db')
            cursor=sqliteconnect.cursor()

            cursor.execute('''SELECT * from assist_record''')
            record=cursor.fetchall()
            for row in record:
                print("Name :",row[0])
                print("ID:",row[1])
                print("Date Of Birth :",row[2])
                print("Birth Location :",row[3])
                print("Gender:",row[4])
                print("Owners :",row[5])
                print("Age :",row[6])
            sqliteconnect.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Error connecting to database")
        finally:
            if(sqliteconnect):
                sqliteconnect.close()

def owner_records():
     try:
            sqliteconnect=sqlite3.connect('assistant_record.db')
            cursor=sqliteconnect.cursor()

            cursor.execute('''SELECT * from Owner_records''')
            record=cursor.fetchall()
            for row in record:
                print("Name :",row[0])
                print("Age :",row[1])
                print("ID:",row[2])
                print("Profession :",row[3])
                print("Company/Institute",row[4])
                print("Gender:",row[5])
              
              
            sqliteconnect.commit()
            cursor.close()
     except sqlite3.Error as e:
            print("Error connecting to database")
     finally:
            if(sqliteconnect):
                sqliteconnect.close()
