import mysql.connector
import sys

DB_CONFIG = {
	"host": "db",
	"user": "user",
	"password": "password",
	"database": "app_db",
}

def init_db():
	conn = mysql.connector.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS records (
			id INT AUTO_INCREMENT PRIMARY KEY,
			name VARCHAR(255) NOT NULL,
			age INT NOT NULL
		)
	''')
	conn.commit()
	conn.close()

def add_record(name, age):
	conn = mysql.connector.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute('INSERT INTO records (name, age) VALUES (%s, %s)', (name, age))
	conn.commit()
	conn.close()
	print(f"Added record: {name}, {age}")

def list_records():
	conn = mysql.connector.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM records')
	rows = cursor.fetchall()
	conn.close()
	if rows:
		for row in rows:
			print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
	else:
		print("There are no entries in the database.")

def delete_record(record_id):
	conn = mysql.connector.connect(**DB_CONFIG)
	cursor = conn.cursor()
	cursor.execute('DELETE FROM records WHERE id = %s', (record_id,))
	conn.commit()
	if cursor.rowcount > 0:
		print(f"Entry with ID {record_id} was deleted.")
	else:
		print(f"There's no entry with ID {record_id}.")
	conn.close()

def main():
	if len(sys.argv) < 2:
		print("Usage:")
		print("app.py add <name> <age>")
		print("app.py list")
		print("app.py delete <id>")
		return

	command = sys.argv[1]

	if command == "add":
		if len(sys.argv) != 4:
			print("Usage: app.py add <name> <age>")
			return
		name = sys.argv[2]
		try:
			age = int(sys.argv[3])
		except ValueError:
			print("Age must be an integer.")
			return
		add_record(name, age)
	elif command == "list":
		list_records()
	elif command == "delete":
		if len(sys.argv) != 3:
			print("Usage: app.py delete <id>")
			return
		try:
			record_id = int(sys.argv[2])
		except ValueError:
			print("ID must be an integer.")
			return
		delete_record(record_id)
	else:
		print(f"Unknown command '{command}'. Use 'add', 'list' or 'delete'.")

if __name__ == "__main__":
	init_db()
	main()
