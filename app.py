from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import json
from datetime import datetime

DB = 'events.db'

app = Flask(__name__)
CORS(app)

def get_db_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/events', methods=['POST'])
def ingest_event():
    data = request.get_json(force=True)
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    event_name = data.get('event_name')
    timestamp = data.get('timestamp') or datetime.utcnow().isoformat() + 'Z'
    if not event_name:
        return jsonify({'error': 'event_name required'}), 400

    user_id = data.get('user_id')
    session_id = data.get('session_id')
    url = data.get('url')
    referrer = data.get('referrer')
    device = data.get('device') or {}
    device_os = device.get('os')
    device_browser = device.get('browser')
    device_type = device.get('device_type')
    metadata = data.get('metadata')
    metadata_json = json.dumps(metadata) if metadata is not None else None

    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('''INSERT INTO events (event_name, timestamp, user_id, session_id, url, referrer, device_os, device_browser, device_type, metadata)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (event_name, timestamp, user_id, session_id, url, referrer, device_os, device_browser, device_type, metadata_json))
    conn.commit()
    conn.close()

    return jsonify({'status': 'ok'})

@app.route('/api/analytics/event_counts', methods=['GET'])
def event_counts():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT event_name, COUNT(*) as cnt FROM events GROUP BY event_name ORDER BY cnt DESC')
    rows = cur.fetchall()
    result = [{'event_name': r['event_name'], 'count': r['cnt']} for r in rows]
    conn.close()
    return jsonify(result)

@app.route('/api/analytics/device_breakdown', methods=['GET'])
def device_breakdown():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute('SELECT device_type, COUNT(*) as cnt FROM events GROUP BY device_type')
    rows = cur.fetchall()
    result = [{'device_type': r['device_type'] or 'unknown', 'count': r['cnt']} for r in rows]
    conn.close()
    return jsonify(result)
@app.route('/api/analytics/hourly')
def hourly():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT strftime('%H', timestamp) as hour, COUNT(*) as count FROM events GROUP BY hour ORDER BY hour")
    rows = cur.fetchall()
    result = [{'hour': r['hour'], 'count': r['count']} for r in rows]
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
