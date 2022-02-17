import sqlite3
connection = sqlite3.connect("data.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);")


def close_connection():
    connection.close()

entries = []

def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries

def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

