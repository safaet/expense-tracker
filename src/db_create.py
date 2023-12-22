from db_connection import get_database_connection

cursor, db = get_database_connection()


cursor.execute('''CREATE TABLE expense(id int AUTO_increment PRIMARY KEY,
                                        expense_date TIMESTAMP,
                                        category VARCHAR(128),
                                        amount double,
                                        notes longtext,
                                        documents VARCHAR(512) DEFAULT '',
                                        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
                                                    ON UPDATE CURRENT_TIMESTAMP)

                ''')



cursor.execute("select * from ExpenseDB.espense")
rows = cursor.fetchall()
print(rows)