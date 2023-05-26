# Health Insurance Cross Sell Prediction

## 1. Problema de Negócio
O problema de negócio consiste em identificar potenciais clientes que têm maior probabilidade de adquirir um seguro de carro (cross-sell) a fim de direcionar esforços de marketing e vendas de forma mais eficiente. A empresa Golden Shield deseja recomendar o seguro de carro apenas para os clientes que apresentam maior interesse nesse produto. Isso permitirá que o time de marketing faça campanhas direcionadas para os potenciais clientes com maior probabilidade de adquirir o seguro de carro. Como cientista de dados da Golden Shield, a tarefa é desenvolver um modelo preditivo para determinar a propensão de um cliente em adquirir um seguro de veículo.

| Problema  | Objetivo | Questão principal |
|-----------|----------|------------------|
| Identificar potenciais clientes interessados em seguro de carro | Direcionar esforços de marketing e vendas de forma mais eficiente | Quais são os clientes do seguro de saúde que têm maior probabilidade de adquirir um seguro de carro? |


## 2. Premissas de Negócio
A etapa inicial desse projeto foi selecionar uma amostra de clientes e realizar uma pesquisa para avaliar seu interesse pelo novo produto, o seguro de carro. Os dados coletados sobre suas preferências, necessidades e intenções de compra, possibilitam construir um modelo para prever a propensão de cada cliente a comprar um seguro de carro.

Além disso, foram realizadas pesquisas preliminares sobre o mercado de seguros para obter informações sobre as tendências do setor e o comportamento do cliente. Os resultados desta pesquisa foram documentados em um caderno e servem como informações para o desenvolvimento do modelo.

Os dados de resposta dos clientes interessados já foram coletados e estão prontamente disponíveis para o desenvolvimento do modelo. No entanto, para aproveitar esses dados de forma eficaz, eles foram armazenados em um banco de dados SQL para posterior análise e modelagem.

Antes de prosseguir com o projeto, fizemos algumas suposições sobre o contexto de negócios e a disponibilidade de dados. Essas suposições são as seguintes:

- A lista de potenciais clientes contém os dados necessários para a análise de propensão: Partimos do pressuposto de que o conjunto de dados que possuímos inclui informações relevantes sobre os clientes, como dados demográficos, histórico de compras anteriores e outras variáveis que nos permitirão avaliar a probabilidade de cada cliente adquirir um seguro de carro.

- A pontuação de propensão é um indicador confiável: Consideramos que a pontuação de propensão, calculada com base nos dados do cliente e em técnicas de modelagem preditiva, é um indicador confiável da probabilidade de um cliente adquirir um seguro de carro. Quanto maior a pontuação, maior a probabilidade de conversão.

- A ordenação da lista de potenciais clientes com base na pontuação de propensão aumentará a taxa de conversão: Partimos do princípio de que, ao ordenar a lista de potenciais clientes em ordem decrescente de suas pontuações de propensão, poderemos priorizar aqueles com pontuações mais altas, direcionando nossos esforços de marketing e vendas de forma mais eficaz. Esperamos, assim, aumentar a taxa de conversão e otimizar a alocação de recursos.

## 3. Estratégia da solução
### 3.1 Produto Final
O resultado final do projeto é uma planilha interativa criada no Google Sheets que apresenta a propensão de cada cliente em adquirir um seguro de carro. A planilha fornece uma pontuação de propensão para cada cliente com base nos dados disponíveis, permitindo uma análise rápida e eficiente das oportunidades de cross-sell. Através dessa planilha, a equipe de marketing e vendas pode identificar e priorizar os potenciais clientes mais propensos a adquirir um seguro de carro, direcionando seus esforços de forma mais estratégica e aumentando a eficácia das ações de vendas.

### 3.2 Ferramentas utilizadas
Para o desenvolvimento deste projeto, utilizamos as seguintes ferramentas:

- Python: linguagem de programação popular e poderosa usada para desenvolver aplicativos de ciência de dados e aprendizado de máquina. Utilizamos bibliotecas como pandas, numpy, scikit-learn e scipy para manipulação e análise de dados, bem como para a construção do modelo de aprendizado de máquina.
    
- API Flask: um micro-framework web usado para criar aplicativos da web em Python. Utilizamos o Flask para desenvolver uma API que permite a interação com o modelo de propensão e a integração com outras ferramentas.

- Visual Studio Code: um editor de código-fonte que fornece recursos avançados para desenvolvimento, como depuração, controle de versão e integração com várias extensões. Utilizamos o Visual Studio Code como ambiente de desenvolvimento principal.

- Anaconda: uma plataforma que contém várias bibliotecas e ferramentas importantes para análise de dados. Utilizamos o Anaconda para gerenciar nossos ambientes virtuais e instalar as bibliotecas necessárias para o projeto.

- Git: um sistema de controle de versão amplamente utilizado para gerenciar alterações em arquivos de código-fonte. Utilizamos o Git para controlar o histórico de alterações em nosso projeto.

- Render: utilizamos o Render para hospedar nossa aplicação web, que inclui a API Flask para interação com o modelo de propensão. A plataforma nos permitiu implantar e disponibilizar a aplicação de forma rápida e confiável, garantindo que ela esteja acessível aos usuários finais.
    
- Google Sheets: utilizamos o Google Sheets como uma das ferramentas de visualização e apresentação dos resultados do projeto. A planilha interativa no Google Sheets permite visualizar e analisar os dados de propensão dos clientes de forma conveniente e compartilhável.


### 3.3 Desenvolvimento
Neste projeto, seguimos a metodologia CRISP-DM (Cross Industry Process - Data Mining), que é amplamente adotada como padrão de processo analítico desde 1999. Desenvolvida por um consórcio de mais de 200 organizações interessadas em mineração de dados, essa metodologia é flexível e pode ser adaptada a diferentes métodos analíticos, incluindo Data Science.

Embora a versão original da metodologia CRISP-DM seja composta por seis fases, optamos por utilizar uma versão estendida com dez fases para garantir uma abordagem mais abrangente e detalhada. Essas fases adicionais foram adicionadas para atender às necessidades específicas deste projeto e garantir a qualidade e a eficácia do processo analítico.

Minha estratégia para resolver esse desafio foi a seguinte:

**1. Entendimento dos Dados**

**1.1** Descrição dos Dados:  Neste passo, o objetivo é compreender os dados disponíveis e suas características. Isso envolve examinar as variáveis presentes, entender seu significado e identificar possíveis problemas, como dados faltantes ou inconsistências.
    
**1.2** Feature Engineering: Aqui, o foco é identificar e criar novas variáveis relevantes para a análise de propensão. Isso pode envolver a combinação de variáveis existentes, a criação de variáveis derivadas ou a seleção de atributos específicos que tenham maior impacto na previsão.
    
**1.3** Filtragem de Variáveis: Nesta etapa, o objetivo é filtrar os dados para remover informações irrelevantes ou duplicadas. Isso ajuda a reduzir a complexidade dos dados e a melhorar a eficiência do modelo.
    
**1.4** Análise Exploratória de Dados: Aqui, realiza-se uma exploração mais aprofundada dos dados para identificar padrões, tendências e insights relevantes. Isso pode envolver a visualização dos dados, a análise de correlações entre variáveis e a identificação de possíveis relações entre os atributos e a variável alvo.

**2. Preparação dos Dados**

**2.1** Pré-processamento: Neste passo, os dados são preparados para a modelagem. Isso inclui o tratamento de valores ausentes, a codificação de variáveis categóricas, a normalização ou padronização dos dados e outras transformações necessárias para garantir a qualidade e a consistência dos dados.
    
**2.2** Seleção de Features: Aqui, selecionam-se as variáveis mais relevantes para a análise de propensão. Isso pode ser feito com base em técnicas estatísticas, como análise de correlação, ou algoritmos específicos de seleção de atributos, que ajudam a identificar as variáveis mais informativas para o modelo.

**3. Modelagem**

**3.1** Modelagem de Machine Learning: Neste passo, desenvolve-se um modelo de aprendizado de máquina para prever a propensão de um cliente adquirir um seguro de carro. Isso envolve a escolha do algoritmo adequado, o treinamento do modelo com os dados preparados e a avaliação do desempenho do modelo.
    
**3.2** Ajuste de Hiperparâmetros:Aqui, realiza-se o ajuste dos hiperparâmetros do modelo com o objetivo de otimizar seu desempenho. Isso pode ser feito por meio de técnicas como validação cruzada e busca em grade, que ajudam a encontrar a combinação ideal de hiperparâmetros que maximizam o desempenho do modelo.

**4. Avaliação e Desempenho de Negócios**

**4.1** Métricas de Desempenho: Avaliar o desempenho do modelo com base em métricas relevantes para o negócio, como taxa de conversão e retorno sobre o investimento.
    
**5. Implantação**

**5.1** Implantação do Modelo em Produção: Implementar o modelo em um ambiente de produção para uso contínuo.


## 4. Entendimento dos Dados
A primeira etapa deste processo é dedicada à obtenção e compreensão dos dados. Durante essa etapa, buscamos identificar e criar novas variáveis relevantes para a análise de propensão, além de realizar a filtragem dos dados para eliminar informações irrelevantes ou duplicadas. É nesse momento que aprofundamos nossa exploração dos dados, em busca de padrões, tendências e insights significativos. Utilizamos técnicas estatísticas e visualizações para identificar correlações entre as variáveis, validar hipóteses existentes e descobrir novos insights que possam contribuir para o desenvolvimento do modelo de propensão. Essas etapas de compreensão dos dados são cruciais para garantir um entendimento sólido dos dados disponíveis e das características relevantes para o projeto. Essa compreensão nos permite tomar decisões embasadas ao longo do processo de modelagem e obter resultados mais precisos na previsão da propensão dos clientes.

O conjunto de dados utilizado neste projeto foi obtido a partir da plataforma Kaggle. O conjunto de dados específico pode ser acessado através do seguinte [link](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=test.csv).

### 4.1 Descrição dos Dados
Nesta primeira fase, foram aplicadas técnicas, como a renomeação das colunas no formato snakecase e a identificação de valores faltantes (NaN). Além disso, foram utilizadas estatísticas descritivas para compreender a distribuição dos dados, tanto em termos de atributos numéricos quanto categóricos, permitindo assim a detecção de possíveis padrões e tendências.

O conjunto de dados contém 19 atributos, conforme listados abaixo:

|       Variable       |                                                          Definition                                                         |
|:--------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| id                   | Unique ID for the customer                                                                                                  |
| Gender               | Gender of the customer                                                                                                      |
| Age                  | Age of the customer                                                                                                         |
| Driving_License      | 0 : Customer does not have DL, 1 : Customer already has DL                                                                  |
| Region_Code          | Unique code for the region of the customer                                                                                  |
| Previously_Insured   | 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance                                     |
| Vehicle_Age          | Age of the Vehicle                                                                                                          |
| Vehicle_Damage       | 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.          |
| Annual_Premium       | The amount customer needs to pay as premium in the year                                                                     |
| Policy_Sales_Channel | Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc. |
| Vintage              | Number of Days, Customer has been associated with the company                                                               |
| Response             | 1 :  Customer is interested, 0 : Customer is not interested                                                                 |



### 4.2  Feature Engineering
O objetivo da Feature Engineering é aprimorar o desempenho dos modelos de aprendizado de máquina por meio da transformação e criação de novos recursos a partir dos dados disponíveis. Durante esta etapa, podem ser aplicadas operações matemáticas ou combinações significativas de recursos existentes para criar novos recursos. No âmbito deste projeto, foram realizadas transformações no DataFrame com o intuito de tornar os valores categóricos mais descritivos.

### 4.3 Data Filtering
Nesta fase, não foi necessário realizar nenhum processo de filtragem de dados, pois as informações disponíveis já estavam adequadas e não havia necessidade de remoção de dados irrelevantes ou duplicados.

### 4.4 Data Analysis
Durante esta fase, foi conduzida uma análise detalhada dos dados para obter insights significativos sobre as características dos clientes. Foram realizadas análises univariadas dos atributos numéricos e da variável resposta, além de análises bivariadas para examinar cada feature individualmente. Gráficos foram utilizados para facilitar a visualização dos resultados. Além disso, foi realizada uma análise multivariada dos atributos numéricos a fim de compreender melhor as relações entre as variáveis.
 

**Principais Insights:**

**1.** Os dados revelam a existência de 135 canais de vendas de apólice, abrangendo uma ampla variedade de opções para os clientes. No entanto, é interessante notar que os três principais canais de vendas de apólice concentram a maioria dos clientes captados, representando impressionantes 79,57% do total. Isso indica a importância de direcionar estratégias de marketing e vendas para esses canais mais efetivos, a fim de maximizar o alcance e o impacto das ações promocionais.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_policy_salles_channel.png" alt="bivariate_analysis_policy_salles_channel">
</p>


**2.** Uma descoberta relevante é a observação de que carros com mais de 2 anos apresentam uma taxa de conversão mais alta em comparação aos demais. Isso indica que os proprietários de veículos com maior tempo de uso estão mais propensos a adquirir um seguro de carro. Essa informação é valiosa para a definição de segmentação de mercado e criação de estratégias específicas para atrair esse público-alvo. 

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_vehicle_age.png" alt="bivariate_analysis_vehicle_age">
</p>


**3.** Foi identificado que a faixa etária de 32 a 53 anos apresenta um interesse significativo na aquisição do seguro de carro. Essa faixa etária demonstra uma maior propensão em adquirir o seguro em comparação com outras faixas etárias. Isso sugere que estratégias de marketing direcionadas a esse grupo podem ser mais eficazes na promoção e venda do seguro automotivo.


<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_age.png" alt="bivariate_analysis_age">
</p>



## 5. Preparação dos Dados
Na segunda etapa, foram realizados dois processos cruciais: o preparo dos dados e a seleção de features.

### 5.1 Data Preparation
Na fase de preparação dos dados, foram aplicadas transformações específicas nos dados para permitir que os modelos de Machine Learning aprendam o comportamento dos dados de forma mais eficiente. Algumas das transformações realizadas incluíram a padronização (standardization), o escalonamento (scaling) e a codificação (encoding).

A padronização é uma técnica que visa transformar os dados para que tenham média zero e desvio padrão igual a um, o que pode ser útil em certos algoritmos de aprendizado de máquina. O escalonamento, por sua vez, é usado para ajustar a escala dos dados, normalmente para um intervalo específico, como [0, 1] ou [-1, 1]. Isso é feito para evitar que as diferenças de escala entre as variáveis afetem a performance dos modelos.

A codificação é uma etapa importante quando lidamos com variáveis categóricas. Ela envolve a transformação dessas variáveis em representações numéricas, permitindo que os modelos de Machine Learning trabalhem com elas. 

Após a aplicação dessas transformações, os objetos resultantes foram salvos em formato pickle. 
Dessa forma, a preparação dos dados nesta fase buscou garantir que os modelos de Machine Learning tenham acesso aos dados transformados de maneira adequada, facilitando o aprendizado e a aplicação dos mesmos em situações futuras.

### 5.2 Feature Selection
Durante esta fase, realizamos a seleção dos atributos mais significativos para o treinamento do modelo. Para isso, foram adotadas algumas estratégias. Primeiramente, removemos colunas consideradas irrelevantes para a análise. Em seguida, dividimos os dados em conjuntos de treinamento e teste, visando avaliar o desempenho do modelo em dados não vistos anteriormente.

Além disso, utilizamos o método Boruta, que tem como objetivo identificar as features mais relevantes para o modelo. No entanto, os resultados obtidos com o Boruta não foram satisfatórios, uma vez que apenas uma feature foi selecionada. Para contornar essa situação, empregamos o algoritmo ExtraTreesClassifier juntamente com a propriedade forest.feature_importances_. Essa abordagem nos permitiu identificar as features mais relevantes e, dessa forma, selecionamos as sete primeiras como atributos para o modelo.

A figura a seguir exibe a importância das features.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/feature_importance.png" alt="feature_importance">
</p>


## 6. Modelagem
Nesta etapa, foram avaliados vários modelos de aprendizado de máquina e analisado o desempenho de cada um. Para otimizar os modelos, foram aplicadas técnicas específicas, como BayesianSearchCV e Random Search, a fim de encontrar a combinação ideal de hiperparâmetros que maximizasse o desempenho dos modelos.

### 6.1 Machine Learning Modelling
A análise de diferentes modelos de Machine Learning, incluindo KNN Classifier, Logistic Regression, Extra Trees Classifier, Random Forest, XGBoost, LGBM e CatBoost, foi realizada nesta fase. Utilizou-se a técnica de cross-validation para avaliar o desempenho real de cada modelo.

Durante a análise, também foram utilizadas as Curvas de Ganhos Cumulativos, uma ferramenta de visualização. Essas curvas permitem avaliar o desempenho de um modelo de classificação ao identificar corretamente as instâncias positivas. Ao traçar a taxa acumulada de verdadeiros positivos no eixo y em relação à taxa acumulada de instâncias positivas selecionadas no eixo x, é possível compreender como o modelo se comporta em diferentes pontos do ranking de probabilidade.
A figura abaixo apresenta as Curvas de Ganhos obtidas nos modelos testados.


<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/cumulative_gain_all.png" alt="cumulative_gain">
</p>


Também foi realizada a análise da Lift Curve, uma representação gráfica que compara a eficácia de um modelo preditivo com uma estimativa aleatória. Essa métrica é comumente utilizada em marketing e gerenciamento de relacionamento com o cliente para avaliar o desempenho de modelos projetados para prever o comportamento do cliente. A seguir, é apresentado um gráfico com as curvas de lift dos modelos testados.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/curvas_lift_all.png" alt="curvas_lift_all">
</p>

As métricas de desempenho, como Precision, Recall e F1-Score, foram utilizadas para avaliar a performance dos modelos, tanto para os modelos simples quanto para aqueles com cross-validation. A figura a seguir exibe uma tabela com os resultados obtidos por cada modelo.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/models_CV_metrics.png" alt="models_CV_metrics">
</p>

Durante a análise dos modelos de machine learning, observamos que o CatBoostClassifier apresentou valores mais altos em métricas como precision, bem como nas curvas lift e ganhos cumulativos.

No entanto, ao considerar o objetivo específico deste projeto, que é gerar um ranking colocando no topo os clientes com maior probabilidade de adquirir o seguro de carro, a métrica de recall ganha maior importância. O recall mede a capacidade do modelo em identificar corretamente os clientes que realmente têm interesse em adquirir o seguro, minimizando assim a perda de oportunidades.

Ao avaliar as métricas de recall, observamos que o XGBClassifier obteve um valor mais alto em comparação ao CatBoostClassifier. Isso indica que o modelo XGBClassifier tem uma maior capacidade de identificar e classificar corretamente os clientes propensos a adquirir o seguro de carro.

Portanto, mesmo considerando que o CatBoostClassifier apresentou valores superiores em métricas como precision, curva lift e ganhos cumulativos, optaremos pelo XGBClassifier devido à sua melhor performance em recall. Essa escolha é fundamentada no objetivo principal do projeto, que é maximizar a identificação dos clientes com maior probabilidade de adquirir o seguro de carro


### 6.2 Hyperparameter Finetuning
Para encontrar os melhores hiperparâmetros para o modelo XGBoost, foram aplicadas técnicas de busca de hiperparâmetros, como Bayesian Search CV e Random Search. 

Durante a busca de hiperparâmetros, vários parâmetros foram avaliados, incluindo o número de árvores, a profundidade máxima da árvore, a taxa de aprendizado e outros. O objetivo principal foi alcançar o melhor desempenho possível para o modelo XGBoost.

Após ajustar os hiperparâmetros, os modelos resultantes foram avaliados e comparados com o modelo testado anteriormente. Foram utilizadas métricas importantes, como Precision, Recall e F1-Score, para avaliar a capacidade do modelo de classificar corretamente as instâncias positivas e negativas.

Essa etapa de ajuste de hiperparâmetros é crucial para obter um modelo com desempenho otimizado, garantindo que ele seja capaz de identificar corretamente os clientes propensos a adquirir o seguro de carro. A seleção dos melhores parâmetros permite melhorar a precisão, o recall e o F1-Score do modelo, proporcionando resultados mais confiáveis e eficazes na classificação dos clientes.

A figura abaixo apresenta a comparação dos três modelos utilizando métricas de avaliação.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/finetuning_xgb.png" alt="finetuning_xgb">
</p>

Após a avaliação dos resultados, o modelo XGBoost com ajuste de hiperparâmetros utilizando a técnica de Bayesian Search apresentou o melhor desempenho em termos de recall. 


## 7. Avaliação e Desempenho de Negócios
Nesta etapa, além da avaliação do desempenho do modelo de Machine Learning, foi realizada uma análise mais aprofundada dos resultados, convertendo-os em métricas de negócio relevantes para avaliar a eficácia do modelo no ranqueamento dos clientes. Foram calculados indicadores de desempenho, como Precision, Recall, F1-Score e outras métricas específicas do contexto do projeto.

Além disso, foram gerados gráficos e visualizações para auxiliar na interpretação dos erros e na identificação de possíveis melhorias na performance do modelo. Essas visualizações permitiram uma análise mais detalhada dos resultados e a identificação de padrões ou tendências que poderiam afetar a eficácia do modelo na tarefa de ranqueamento dos clientes.

Essa análise mais abrangente dos resultados e a utilização de métricas de negócio relevantes proporcionaram uma compreensão mais completa do desempenho do modelo e permitiram a identificação de áreas de melhoria. Com base nessas análises, é possível realizar ajustes e refinamentos no modelo, buscando otimizar ainda mais sua performance e garantir um melhor ranqueamento dos clientes de acordo com sua probabilidade de adquirir o seguro de carro.

### 7.1 Métricas de Desempenho do Modelo
Durante a avaliação do modelo, várias métricas foram utilizadas para analisar o desempenho do mesmo. Entre essas métricas, temos a acurácia, precisão, recall, F1-Score e a área sob a curva ROC (ROC AUC).

A figura abaixo apresenta um gráfico com os valores das métricas obtidas pelo modelo:

- Acurácia: Mede a taxa de acertos do modelo em relação ao total de previsões realizadas.
- Precisão: Avalia a proporção de previsões positivas corretas em relação a todas as previsões positivas feitas pelo modelo.
- Recall: Mede a proporção de instâncias positivas corretamente identificadas em relação a todas as instâncias que realmente são positivas.
- F1-Score: É uma métrica que combina a precisão e o recall em uma única medida, fornecendo uma avaliação balanceada do desempenho do modelo.
- ROC AUC: A área sob a curva ROC (Receiver Operating Characteristic) é uma medida numérica que indica a capacidade do modelo de classificar corretamente as instâncias.


<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/model_metrics.png" alt="model_metrics">
</p>

O gráfico abaixo ilustra o poder discriminativo do modelo em identificar os clientes com maior probabilidade de compra em comparação com uma classificação aleatória. Ele representa a capacidade do modelo de distinguir entre clientes com maior propensão à compra e aqueles que não possuem essa característica. Quanto maior a distância entre a curva do modelo e a linha de referência aleatória, maior é a capacidade de classificação do modelo. 

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/cumulative_curve_xgb.png" alt="cumulative_curve_xgb">
</p>

O gráfico abaixo representa a variação do lift em relação à porcentagem acumulada da base. Essa visualização é útil para identificar que o modelo apresenta um desempenho melhor em comparação com a situação de referência. 

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/lift_curve_xgb.png" alt="lift_curve_xgb">
</p>

Abaixo, temos a curva ROI, que permite visualizar a melhoria relativa proporcionada pelo modelo em comparação com o baseline ao longo da porcentagem acumulada da base. Essa curva é útil para avaliar o desempenho do modelo em termos de retorno esperado. A curva ROI mostra como o modelo supera as expectativas em relação à situação de referência, medida pelo baseline. Ela mostra a proporção acumulada do retorno esperado ao longo do tempo à medida que mais clientes são considerados. 

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/roi_curve_xgb.png" alt="roi_curve_xgb">
</p>


### 7.2 Bussiness Metrics
A fim de avaliar o desempenho do negócio, foi desenvolvido um código que realiza o cálculo da porcentagem de clientes a serem contatados, determina a pontuação mínima e calcula a diferença de lucros entre o método tradicional e o modelo utilizado.

A avaliação é baseada no preço do produto e no custo da operação por cliente. Além disso, é necessária a obtenção de uma lista de clientes ordenada de acordo com a pontuação atribuída pelo modelo.

Detalhes do Cálculo:

- Preço do seguro do veículo: $550,00
- Custo para contactar o cliente: $40,00

Na imagem abaixo podemos observar que é recomendado entrar em contato com 47% dos clientes, ordenados de acordo com a pontuação atribuída pelo modelo. Portanto, é estabelecido um limiar de pontuação de 0,02 para determinar quais clientes devem ser contatados.


<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/best_profit.png" alt="best_profit">
</p>

Ao focar apenas nos clientes com maior propensão a comprar, a empresa tem a possibilidade de reduzir os custos de chamadas desnecessárias. Como resultado, a operação se torna 72,13% mais rentável devido à economia de custos obtida, como podemos ver no gráfico abaixo.
    
<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/selected_all_customers.png" alt="selected_all_customers">
</p>

## 8. Deployment
Após a validação do modelo de geração de ranking, o próximo passo foi disponibilizá-lo aos usuários finais por meio de uma API. Essa API foi desenvolvida utilizando o módulo Flask e está contida no arquivo 'handler.py'. Com essa API, os usuários têm a capacidade de obter o ranking dos clientes com scores precisos e atualizados.

A API é responsável por carregar o modelo treinado e a classe HealthInsurance foi criada para preparar e transformar os dados necessários antes de serem fornecidos ao modelo para a geração dos scores. Essa preparação e transformação garantem que os dados estejam em um formato adequado para serem processados pelo modelo.

O modelo selecionado foi implantado em um ambiente de nuvem, tornando-o acessível para outras pessoas ou serviços. Isso permite que eles utilizem os resultados gerados pelo modelo para aprimorar a tomada de decisões de negócios. Para facilitar o acesso e o compartilhamento dos resultados, utilizamos o Google Sheets, uma plataforma que permite o armazenamento e a visualização dos dados gerados pelo modelo em tempo real. Dessa forma, as informações estão disponíveis de maneira rápida e prática para os usuários que necessitam delas, facilitando a colaboração e a utilização dos resultados em diferentes contextos de negócios.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/deploy_healthInsuance.png" alt="deploy_healthInsuance">
</p>


O produto final é um documento de planilha vinculado ao modelo de aprendizado de máquina implantado. Este documento fornece uma lista de clientes com probabilidade de comprar seguro de carro, com base nas previsões feitas pelo modelo. Para obter as previsões, basta inserir os dados do cliente, clicar em "Health Insurance Prediction" - "Get Prediction". Assim a planilha se conectará com o modelo implantado e retornará a pontuação, com a previsão, destacando os clientes que devem receber a oferta. Essa integração entre a planilha e o modelo permite uma análise fácil e eficiente dos clientes com maior potencial de compra, auxiliando nas estratégias de oferta e aumentando as chances de sucesso nas vendas. 
Veja o funcionamento na demonstração abaixo:

# DEMO funcionamento


## 9. Conclusão
Com base nos resultados deste projeto, conclui-se que o modelo treinado é uma ferramenta precisa e confiável para gerar um ranking dos clientes com maior probabilidade de adquirir o seguro de carro. Desenvolvido com o algoritmo XGBoost, o modelo obteve um melhor recall após o ajuste fino, o que indica sua eficácia na identificação dos clientes potenciais.

Além disso, o projeto demonstrou uma economia significativa ao reduzir os custos relacionados às chamadas desnecessárias, resultando em uma operação 72,13% menos onerosa. Isso destaca o potencial do modelo treinado como uma ferramenta valiosa para a equipe comercial e financeira.

Outro aspecto relevante é a obtenção de insights valiosos para melhorias adicionais, como a identificação dos canais de vendas com maior retorno. Essas informações podem guiar futuras decisões estratégicas da empresa, gerando melhorias adicionais e possíveis economias.

Em resumo, este projeto ilustra como a análise de dados pode trazer benefícios tangíveis e substanciais para as empresas, permitindo uma tomada de decisão mais eficiente e informada.


## 10. Próximos passos
- Coletar novos dados: Continuar a busca por dados relevantes que possam contribuir para o aprimoramento do modelo. Isso envolve expandir a base de dados atual, procurar novas fontes de dados e coletar informações específicas que possam aumentar o desempenho do modelo.
- Explorar diferentes combinações de recursos:  Investigar várias combinações de recursos disponíveis nos dados. Isso inclui criar novas variáveis, selecionar as mais relevantes e transformar as existentes para melhorar o desempenho geral do modelo.
- Refinamento do modelo: Realizar ajustes e refinamentos no modelo atual. Isso abrange a otimização de hiperparâmetros, a experimentação com diferentes algoritmos de machine learning, a avaliação de técnicas de regularização e até mesmo a consideração de abordagens avançadas, como o uso de deep learning, para alcançar um desempenho ainda melhor.
- Incorporação de feedback do usuário: Coletar feedback dos usuários finais do modelo e utilizar suas sugestões e necessidades para aprimorar continuamente o modelo. Isso envolve a realização de sessões de revisão e feedback, identificação de lacunas e áreas de melhoria, e implementação de ajustes com base nas informações fornecidas pelos usuários.





