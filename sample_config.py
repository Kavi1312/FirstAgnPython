import configparser
import json
import sqlite3
from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

def read_config(file_path):
    config = configparser.ConfigParser()

    try:
        config.read(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

    config_dict = {}
    for section in config.sections():
        config_dict[section] = dict(config.items(section))

    return config_dict

# Function to save the data to the database as JSON
def save_to_database(data):
    conn = sqlite3.connect('config_data.db')
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS config_data (id INTEGER PRIMARY KEY, data TEXT)''')

    # Insert JSON data
    cursor.execute("INSERT INTO config_data (data) VALUES (?)", [json.dumps(data)])
    conn.commit()
    conn.close()

# Function to fetch data from the database
@app.route('/get_config', methods=['GET'])
def get_config():
    conn = sqlite3.connect('config_data.db')
    cursor = conn.cursor()

    # Fetch the latest entry
    cursor.execute("SELECT data FROM config_data ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify(json.loads(result[0]))
    else:
        return jsonify({"error": "No data found"}), 404

if __name__ == "__main__":
    config_file_path = 'sample_config.ini'
    config_data = read_config(config_file_path)

    if config_data:
        save_to_database(config_data)
        print("Configuration data saved to database successfully.")

    # Run Flask server
    app.run(debug=True)