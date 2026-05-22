from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os
from database import init_db

app = Flask(__name__)

# Enforces validation check on runtime environment database file footprint
if not os.path.exists('vuln.db'):
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lab1')
def lab1():
    category = request.args.get('category', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # RAW STR INTERPOLATION CONCATENATION RISK INTENTIONALLY REPLICATING LAB DEFECT
    query = f"SELECT name, description, category FROM products WHERE category='{category}' AND released=1"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 1 — WHERE Clause Hidden Data Bypass",
                               lab_objective="Force query logic modification to retrieve unreleased product fields.",
                               query=query, results=results)
    except Exception as e:
        return f"Database Engine Diagnostics Error: {str(e)}"
    finally:
        conn.close()

@app.route('/lab2', methods=['GET', 'POST'])
def lab2():
    message = ""
    query = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        conn = sqlite3.connect('vuln.db')
        cursor = conn.cursor()
        query = f"SELECT id, username, password FROM users WHERE username='{username}' AND password='{password}'"
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                message = f"✅ Success! Authentication Established. Logged in profile context: '{user[1]}'"
            else:
                message = "❌ Authentication Rejected. Credentials do not align with database storage record rows."
        except Exception as e:
            message = f"Database Syntax Error Payload Failure: {str(e)}"
        finally:
            conn.close()
            
    return render_template('lab_layout.html', 
                           lab_title="Lab 2 — Login Authentication Verification Bypass",
                           lab_objective="Inject logical delimiters within structural query checks to forge authentication approval.",
                           show_login_form=True, login_message=message, query=query)

@app.route('/lab3')
def lab3():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 3 Query returns exactly 3 columns (id, name, description)
    query = f"SELECT id, name, description FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 3 — Determining Vector Schema Column Count",
                               lab_objective="Identify internal schema query element dimensions using structure tests (ORDER BY or UNION SELECT NULL).",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 3 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

@app.route('/lab4')
def lab4():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 4 Query returns columns of mixed types: id (int), name (text), price (int)
    query = f"SELECT id, name, price FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 4 — Text-Bearing Type Boundary Assessment",
                               lab_objective="Locate which structural column sequence element accepts string arguments by injecting text into NULL slots.",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 4 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

@app.route('/lab5')
def lab5():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 5 Query yields 3 columns to match the target secret_users dump payload format
    query = f"SELECT id, name, description FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 5 — Cross-Table Secret Data Delivery Extraction",
                               lab_objective="Pivot active query boundaries to harvest credentials out of the secret_users table.",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 5 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

@app.route('/lab6')
def lab6():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 6 simulates having only ONE usable text column (name) available for data reflection
    query = f"SELECT id, name, price FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 6 — Single-Field Multi-Variable Column Concatenation",
                               lab_objective="Leverage SQLite's || operator to drop multi-item credentials through a single extraction text field.",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 6 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

@app.route('/lab7')
def lab7():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 7 Query accepts 3 columns to easily output the sqlite_version() function string
    query = f"SELECT id, name, description FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 7 — Application Engine Version Discovery Mapping",
                               lab_objective="Query underlying database type details using version functions.",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 7 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

@app.route('/lab8')
def lab8():
    search = request.args.get('search', '')
    conn = sqlite3.connect('vuln.db')
    cursor = conn.cursor()
    # Lab 8 Query allows full structural extraction mapping
    query = f"SELECT id, name, description FROM products WHERE name LIKE '%{search}%'"
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return render_template('lab_layout.html', 
                               lab_title="Lab 8 — Master Structural Configuration Map Harvesting",
                               lab_objective="Extract localized structural control schema variables outlining tracking setups via sqlite_master.",
                               query=query, results=results)
    except Exception as e:
        return render_template('lab_layout.html', lab_title="Lab 8 Error State", query=query, lab_objective="", results=[], login_message=f"Error: {str(e)}")
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)