import pickle
import numpy  as np
import pandas as pd

class HealthInsurance:
    
    def __init__(self):
        # Definindo o caminho dos arquivos do projeto
        self.home_path = r'C:\Users\raquel\Documents\Comunidade DS\repos\06-PA-Health-Insurance-Cross-Sell\health_insurance\health_insurance_ross_sell'
        # Carregando os objetos scaler gerados no treinamento do modelo
        self.age_scaler =                       pickle.load(open(self.home_path + r'\src\features\age_scaler.pkl', 'rb')) 
        self.annual_premium_scaler =            pickle.load(open(self.home_path + r'\src\features\annual_premium_scaler.pkl', 'rb'))
        self.vintage_scaler =                   pickle.load(open(self.home_path + r'\src\features\vintage_scaler.pkl', 'rb')) 
        self.target_encode_gender_scaler =      pickle.load(open(self.home_path + r'\src\features\target_encode_gender_scaler.pkl', 'rb'))
        self.target_encode_region_code_scaler = pickle.load(open(self.home_path + r'\src\features\target_encode_region_code_scaler.pkl', 'rb'))
        self.fe_policy_sales_channel_scaler =   pickle.load(open(self.home_path + r'\src\features\fe_policy_sales_channel_scaler.pkl', 'rb'))
        
    def data_cleaning(self, df1):
        # 1.1. Renaming columns
        cols_new = ['id', 'gender', 'age', 'driving_license', 'region_code', 'previously_insured', 'vehicle_age', 
                    'vehicle_damage', 'annual_premium', 'policy_sales_channel', 'vintage']

        df1.columns = cols_new

        return df1

    
    def feature_engineering(self, df2):
        # Criando a coluna 'vehicle_damage_num' para representar os veículos que já foram danificados (1) e os que não foram danificados (0)
        df2['vehicle_damage'] = df2['vehicle_damage'].apply( lambda x: 1 if x == 'Yes' else 0 )

        # Transformando a coluna 'vehicle_age' em uma coluna categórica para aplicação de técnicas de codificação
        df2['vehicle_age'] =  df2['vehicle_age'].apply( lambda x: 'over_2_years' if x == '> 2 Years' else 'between_1_2_year' if x == '1-2 Year' else 'below_1_year' )
        
        return df2
    
   
    
    def data_preparation(self, df5):
        # Aplicando a transformação de Escalonamento Padrão na coluna 'annual_premium'
        df5['annual_premium'] = self.annual_premium_scaler.transform( df5[['annual_premium']].values )

        # Aplicando a transformação de Escalonamento Mínimo e Máximo na coluna 'age'
        df5['age'] = self.age_scaler.transform(df5[['age']].values)

        # Aplicando a transformação de Escalonamento Mínimo e Máximo na coluna 'vintage'
        df5['vintage'] = self.vintage_scaler.transform(df5[['vintage']].values)

        # Codificando a coluna 'gender' utilizando a técnica de Target Encoding
        df5.loc[:, 'gender'] = df5['gender'].map(self.target_encode_gender_scaler)

        # Aplica o processo de target encoding na coluna region_code
        df5.loc[:, 'region_code'] = df5['region_code'].map(self.target_encode_region_code_scaler)

        # Cria variáveis dummy para a coluna vehicle_age usando a função pd.get_dummies
        df5 = pd.get_dummies(df5, prefix='vehicle_age', columns=['vehicle_age'])

        # Aplica o processo de frequency encoding na coluna policy_sales_channel
        df5.loc[:, 'policy_sales_channel'] = df5['policy_sales_channel'].map(self.fe_policy_sales_channel_scaler)

        # Feature Selection
        # Seleciona as colunas relevantes para o modelo
        cols_selected = ['annual_premium', 'vintage', 'age', 'region_code', 'vehicle_damage', 'previously_insured', 'policy_sales_channel']

        # Retorna o dataframe com as colunas selecionadas
        return df5[cols_selected]


    def get_prediction(self, model, original_data, test_data):
        # Usa o modelo treinado para fazer as predições em test_data       
        pred = model.predict_proba(test_data)
        
        # Adiciona as predições ao dataframe original
        original_data['score'] = pred[:, 1].tolist()
        
        # Retorna o dataframe em formato JSON
        return original_data.to_json(orient='records', date_format='iso')