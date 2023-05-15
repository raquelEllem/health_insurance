import pickle
import pandas as pd
from flask import Flask, request, Response
from HealthInsurance import HealthInsurance

# carregando o modelo
path = r'C:\Users\raquel\Documents\Comunidade DS\repos\06-PA-Health-Insurance-Cross-Sell\health_insurance\health_insurance_ross_sell'
model = pickle.load(open(path + r'\src\models\model_linear_regression.pkl', 'rb'))

# inicializando a API
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def health_insurance_predict():
    test_json = request.get_json()

    if test_json: # se houver dados
        if isinstance(test_json, dict): # único exemplo
            test_raw = pd.DataFrame(test_json, index=[0])

        else: # múltiplos exemplos
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instanciando a classe HealthInsurance
        pipeline = HealthInsurance()

        # Limpeza dos dados
        df1 = pipeline.data_cleaning(test_raw)

        # Engenharia de Recursos
        df2 = pipeline.feature_engineering(df1)

        # Preparação dos dados
        df3 = pipeline.data_preparation(df2)

        # Previsão
        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
