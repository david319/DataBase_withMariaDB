import mariadb

class Controller:
    def __login(self):
        user = self.userText.getText()
        password = self.passwordText.getText()

        conn = mariadb.connect(
            user=user,
            password=password,
            host="localhost",
            database="employees")

        if conn:
            print("Connected")
        else:
            print("Not connected")
            print("Error: ", conn.error)

        cur = conn.cursor()

        cur.execute("SELECT * FROM test")
        print(cur.fetchall())

        conn.close()




