
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import numpy as np
import sqlite3
import html 


class DatabaseManager:
    def create_database(self):
        conn = sqlite3.connect(self.db_user)
        cursor = conn.cursor()
        with open('SQL.sql', 'r') as f:
            sql_script = f.read()
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

    def __init__(self, db_name="database.db"):
        self.db_user = db_name
        self.create_database()


    def search_user(self, query=""):
        conn = sqlite3.connect(self.db_user)
        cursor = conn.cursor()
        query = query.strip()
        
        if not query:
            cursor.execute("SELECT * FROM users;")
        else:
            pattern = f"%{query}%"
            cursor.execute("SELECT * FROM users WHERE username LIKE ? OR email LIKE ?", (pattern, pattern))
        self.result = cursor.fetchall()
        conn.close()
        return self.result

results = DatabaseManager().search_user("")

def build_table(results):
    render_html = "<table border='1'>"
    render_html += "<tr><th>ID</th><th>Username</th><th>Email</th><th>Age</th></tr>"
    for row in results:
        render_html += "<tr>"
        for cell in row:
            render_html += f"<td>{html.escape(str(cell))}</td>"
        render_html += "</tr>"  
    render_html += "</table>"
    return render_html
def render_page(users, query=""):
    table_html = build_table(users)
    
    with open("Untitled-2.html", "r", encoding="utf-8") as f:
        template = f.read()

    full_html = template.replace("{table_html}", table_html)
    return full_html


db = DatabaseManager()

class SearchRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/":
            query_params = parse_qs(parsed_url.query)
            search_query = query_params.get("query", [""])[0]

            users = db.search_user(search_query)
            html_content = render_page(users, search_query)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        else:
            super().do_GET()
        
if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SearchRequestHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()



# print("Enter the new user:")
# username = input("Username: ")
# email = input("Email: ")

# while True:
#     age = input("Age: ")
#     try:
#         age = float(age)
#         conn.commit()
#         break
#     except ValueError:
#         print("Invalid age. Please enter a number.")
       
# class User:
#     def __init__(self, username, email, age):
#         self.username = username
#         self.email = email
#         self.age = age
# new_user = User(username, email, age)

# sql_insert = """INSERT INTO useres (username, email, age) VALUES (?, ?, ?)"""
# try:
#     cursor.execute(sql_insert, (new_user.username, new_user.email, new_user.age))
#     conn.commit()
#     print("\n Пользователь успешно добавлен!")
# except sqlite3.IntegrityError as e:
#     print(f"\nError inserting user: {e}")

# print("\nCurrent users in the database:")
# cursor.execute("SELECT * FROM useres;")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# delete_id = input("\nEnter the ID of the user to delete (or press Enter to skip): ")
# if delete_id:
#     try:
#         cursor.execute("DELETE FROM useres WHERE id = ?", (delete_id,))
#         conn.commit()
#         print(f"\nUser with ID {delete_id} has been deleted.")
#     except sqlite3.Error as e:
#         print(f"\nError deleting user: {e}")
# cursor.execute("SELECT * FROM useres;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
# conn.close()


