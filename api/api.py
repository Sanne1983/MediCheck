import json
from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from utils.dosage_utils import get_dosage_text

app = Flask(__name__)
CORS(app)

# Datenbankverbindung
DATABASE = 'api/medicheck.sqlite3'

# Helper-Funktion: Verbindung zur SQLite-Datenbank
def query_db(query, args=(), one=False):
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row  
    cursor = connection.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    connection.close()
    return (result[0] if result else None) if one else result

# Route für Dosierungsabfrage
@app.route('/dosage', methods=['GET'])
def get_dosage():
    pzn = request.args.get('pzn')
    weight = request.args.get('weight')
    if not pzn:
        return jsonify({"error": "PZN erforderlich"}), 400
    if not weight:
        return jsonify({"error": "weight erforderlich"}), 400

    # Datenbankabfrage
    result = query_db("SELECT name, dosage FROM medikamente WHERE pzn = ?", [pzn], one=True)
    if result:
        return jsonify({"name": result['name'], "dosage_for_weight": get_dosage_text(result['dosage'], float(weight)) })
    else:
        return jsonify({"error": "Medikament nicht gefunden"}), 404

# Route für Wechselwirkungsabfrage
@app.route('/interactions', methods=['GET'])
def get_interactions():
    pzn1 = request.args.get('pzn1')
    pzn2 = request.args.get('pzn2')
    if not pzn1 or not pzn2:
        return jsonify({"error": "Beide PZN erforderlich"}), 400

    # Datenbankabfrage
    result = query_db(
        """
        SELECT interaktion FROM interaktionen
        WHERE (pzn1 = ? AND pzn2 = ?) OR (pzn1 = ? AND pzn2 = ?)
        """,
        [pzn1, pzn2, pzn2, pzn1],
        one=True
    )
    if result:
        return jsonify({"interaction": result["interaktion"]})
    else:
        return jsonify({"interaction": "Keine Wechselwirkungen gefunden"})

if __name__ == "__main__":
    app.run(port=8080, debug=True)
