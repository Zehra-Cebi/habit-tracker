import sqlite3
from datetime import date
from habit import Habit

def get_db(name= "main.db"):
    """
    Connects to the SQLite database.

    :param name: Name of the database file.
    :return: SQLite database connection object or None.
    """
    try:
        db = sqlite3.connect(name)
        create_tables(db)
        return db
    except sqlite3.Error as error:
        print(f"[DB Error] Could not connect to database: {error}")
        return None

def create_tables(db):
    """
    Creates tables in the SQLite database, if they don't exist yet.

    :param db: SQLite database connection object.
    """

    try:
        cur = db.cursor()

        # Table for habit definitions
        cur.execute("""CREATE TABLE IF NOT EXISTS habits (
            name TEXT PRIMARY KEY,
            description TEXT,
            frequency TEXT,
            created_at TEXT)""")

        # Table for individual check-ins
        cur.execute("""CREATE TABLE IF NOT EXISTS check_ins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            habit_name TEXT,
            date TEXT,
            FOREIGN KEY(habit_name) REFERENCES habits(name))""")

        db.commit()
    except sqlite3.Error as error:
        print(f"[DB Error] Failed to create tables: {error}")

def save_habit(db, habit):
    """
    Saves habit and its ckeck-ins in SQLite database.
    If the habit was renamed, old records will be deleted first.
    :param db: SQLite database connection.
    :param habit: A Habit object to  save.
    """

    try:
        cur = db.cursor()

        # If name of habit was changed, delete the former name.
        if hasattr(habit, 'original_name') and habit.original_name != habit.name:
            cur.execute("DELETE FROM habits WHERE name = ?", (habit.original_name,))
            cur.execute("DELETE FROM check_ins WHERE habit_name = ?", (habit.original_name,))

        # Insert oder replace habit info.
        cur.execute("""INSERT OR REPLACE INTO habits(name, description, frequency, created_at) 
            VALUES (?, ?, ?, ?)""", (habit.name, habit.description, habit.frequency, habit.created_at.isoformat()))

        # Delete old check-ins and insert new ones.
        cur.execute("DELETE FROM check_ins WHERE habit_name = ?", (habit.name,))
        for check in habit.check_ins:
            cur.execute("INSERT INTO check_ins (habit_name, date) VALUES (?, ?)", (habit.name, check.isoformat()))

        db.commit()
    except sqlite3.Error as error:
        print(f"[DB Error] Failed to save habit '{habit.name}': {error}")

def load_habits(db):
    """
    Loads all habits and their check-in data from the SQLite database.
    :param db: SQLite database connection.
    :return: List of Habit objects.
    """

    habits = []
    try:
        cur = db.cursor()
        cur.execute("SELECT * FROM habits")
        rows = cur.fetchall()

        for row in rows:
            name, description, frequency, created_at = row
            habit = Habit(name, description, frequency)
            habit.created_at = date.fromisoformat(created_at)

            cur.execute("SELECT date FROM check_ins WHERE habit_name = ?", (name,))
            checkins = cur.fetchall()
            habit.check_ins = [date.fromisoformat(d[0]) for d in checkins]

            habits.append(habit)

    except sqlite3.Error as error:
        print(f"[DB Error] Failed to load habits: {error}")

    return habits