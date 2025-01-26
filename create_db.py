import sqlite3

def create_database():
    # Connect to SQLite database (this will create the file if it doesn't exist)
    connection = sqlite3.connect("faq.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    """)

    # Sample data to insert into the table
    sample_data = [
        ("What are your hours?", "We are open Monday to Friday, 9 AM to 5 PM."),
        ("What is your phone number?", "Our phone number is 555-1234."),
        ("Where are you located?", "We are located at 123 Main Street, Springfield."),
        ("Do you offer online support?", "Yes, we provide online support through our website."),
        ("What payment methods do you accept?", "We accept credit cards, PayPal, and bank transfers.")
    ]

    # Insert the data if the table is empty
    cursor.executemany("""
    INSERT INTO faq (question, answer) VALUES (?, ?)
    """, sample_data)

    # Commit changes and close connection
    connection.commit()
    connection.close()

if __name__ == "_main_":
    create_database()