from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Carregar o CSV
df = pd.read_csv('downloads\Relatorio_cadop.csv', on_bad_lines='skip', delimiter=';', encoding='utf-8')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
    return jsonify(results.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)