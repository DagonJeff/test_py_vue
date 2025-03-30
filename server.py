from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}) 

# Carregar o CSV
df = pd.read_csv('downloads/Relatorio_cadop.csv', on_bad_lines='skip', delimiter=';', encoding='utf-8')

df['Data_Registro_ANS'] = pd.to_datetime(df['Data_Registro_ANS'], errors='coerce')

@app.route('/search', methods=['GET'])
def search():
    try:
        query = request.args.get('query')
        column = request.args.get('column')

        results = df.copy()

        if query and column:
            
            query_date = pd.to_datetime(query, errors='coerce', dayfirst=True)
            if not pd.isna(query_date):
                results = results[results['Data_Registro_ANS'] == query_date]
            else:
                results = results[results[column].astype(str).str.contains(query, case=False)]

        results = results.fillna('') 
        response = results.to_dict(orient='records')
        print(response)  
        return jsonify(response)
    except Exception as e:
        print(f"Erro ao processar a solicitação: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)