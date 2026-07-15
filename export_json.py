import mysql.connector
import json
import os

# -----------------------------
# MySQL Connection
# -----------------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yashi123",      # Replace with your password
        database="pvr"              # Replace if your DB name is different
    )

    cursor = conn.cursor(dictionary=True)

    print("Connected to MySQL Successfully!\n")

except mysql.connector.Error as err:
    print("Connection Error:", err)
    exit()

# -----------------------------
# Folder to save JSON files
# -----------------------------
OUTPUT_FOLDER = "data"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# -----------------------------
# List of Tables
# -----------------------------
tables = [
    "movies",
    "theatres",
    "screens",
    "shows",
    "seats",
    "food",
    "offers",
    "bookings",
    "booking_seats",
    "payments"
]

# -----------------------------
# Export Each Table
# -----------------------------
for table in tables:

    try:

        query = f"SELECT * FROM {table}"

        cursor.execute(query)

        rows = cursor.fetchall()

        with open(
            os.path.join(OUTPUT_FOLDER, f"{table}.json"),
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {table: rows},
                file,
                indent=4,
                default=str
            )

        print(f"{table}.json exported successfully.")

    except mysql.connector.Error as err:

        print(f"Error exporting '{table}'")

        print(err)

# -----------------------------
# Close Connection
# -----------------------------
cursor.close()
conn.close()

print("\nAll tables processed.")