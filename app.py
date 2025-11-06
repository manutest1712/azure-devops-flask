from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HELLO_HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello</title>
    <style>
        body {
            font-family: system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial;
            padding: 2rem;
        }
        .card {
            max-width: 640px;
            margin: 2rem auto;
            padding: 1.5rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
        }
        h1 {
            margin: 0 0 0.5rem 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello, World!</h1>
        <p>This is a minimal Flask app served from <code>app.py</code>.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def hello():
    return render_template_string(HELLO_HTML)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
