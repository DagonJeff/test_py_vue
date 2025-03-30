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

        # Filtrar os campos desejados
        filtered_response = []
        for record in response:
            filtered_record = {
                "Registro_ANS": record.get("Registro_ANS"),
                "Razao_Social": record.get("Razao_Social"),
                "Modalidade": record.get("Modalidade"),
                "Cidade": record.get("Cidade"),
                "UF": record.get("UF"),
                "DDD": record.get("DDD"),
                "Telefone": record.get("Telefone")
            }
            filtered_response.append(filtered_record)

        print(filtered_response)  
        return jsonify(filtered_response)
    except Exception as e:
        print(f"Erro ao processar a solicitação: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)