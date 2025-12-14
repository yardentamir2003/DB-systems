import subprocess
import os
import re
import sys
import mysql.connector

# Python interpreter to use
PYTHON = sys.executable

OUTPUT_FILE = "output_all.txt"

# Database connection details (based on q1.py)
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "port": "3307"
}

def drop_old_database():
    """Drops the database 'biu_shoes' if it exists to ensure a clean slate."""
    try:
        # Connect to MySQL server (not a specific DB)
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("DROP DATABASE IF EXISTS biu_shoes")
        print("Dropped database 'biu_shoes' if it existed.")
        conn.close()
    except Exception as e:
        print(f"Error dropping database: {e}")

def natural_sort_key(filename):
    """Sorts filenames naturally (e.g., q2.py before q10.py)."""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', filename)]

def main():
    # 1. Delete old tables (Drop Database)
    drop_old_database()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
        out.write(f"RUN_ALL USING PYTHON = {PYTHON}\n\n")

        # 2. Find all q*.py files
        files = [f for f in os.listdir(".") if re.fullmatch(r"q\d+(_\d+)?\.py", f)]
        
        # 3. Sort them naturally
        files.sort(key=natural_sort_key)

        # 4. Run each file
        for filename in files:
            out.write("=" * 40 + "\n")
            out.write(f"Running: {filename}\n")
            out.write("=" * 40 + "\n")
            print(f"Running {filename}...")

            try:
                result = subprocess.run(
                    [PYTHON, filename], capture_output=True, text=True
                )

                out.write(result.stdout)
                if result.stderr.strip():
                    out.write("\n[stderr]\n")
                    out.write(result.stderr)

            except Exception as e:
                out.write(f"\n[ERROR] {e}\n")

            out.write("\n\n")

    print(f"Done. Output saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
