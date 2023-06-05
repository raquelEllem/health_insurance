# Health Insurance Cross Sell Prediction

## 1. Business Problem

The business problem consists of identifying potential customers who are more likely to purchase a car insurance (cross-sell) in order to direct marketing and sales efforts more efficiently. The company Golden Shield wishes to recommend car insurance only to customers who show a higher interest in this product. This will allow the marketing team to create targeted campaigns for potential customers with a higher likelihood of purchasing car insurance. As a data scientist at Golden Shield, the task is to develop a predictive model to determine a customer's propensity to acquire a vehicle insurance.

| Problem  | Objective | Key Question |
|-----------|----------|------------------|
| Identify potential customers interested in car insurance | Direct marketing and sales efforts more efficiently | Which health insurance customers are more likely to acquire car insurance? |


## 2. Business Assumptions

The initial step of this project was to select a sample of customers and conduct a survey to assess their interest in the new product, car insurance. The data collected about their preferences, needs, and purchase intentions allow building a model to predict the propensity of each customer to purchase car insurance.

Additionally, preliminary research on the insurance market was conducted to gather information about industry trends and customer behavior. The results of this research were documented in a notebook and serve as insights for the development of the model.

The response data from interested customers has already been collected and is readily available for model development. However, to leverage this data effectively, it has been stored in a SQL database for further analysis and modeling.

Before proceeding with the project, we made some assumptions about the business context and data availability. These assumptions are as follows:

- The list of potential customers contains the necessary data for propensity analysis: We assume that the dataset we possess includes relevant information about the customers, such as demographic data, past purchase history, and other variables that will allow us to assess the likelihood of each customer acquiring car insurance.

- The propensity score is a reliable indicator: We consider that the propensity score, calculated based on customer data and predictive modeling techniques, is a reliable indicator of the likelihood of a customer acquiring car insurance. The higher the score, the higher the conversion probability.

- Ordering the list of potential customers based on the propensity score will increase the conversion rate: We assume that by ordering the list of potential customers in descending order of their propensity scores, we can prioritize those with higher scores, directing our marketing and sales efforts more effectively. We expect this to increase the conversion rate and optimize resource allocation.



## 3. Solution Strategy
### 3.1 Final Product
The final outcome of the project is an interactive Google Sheets spreadsheet that presents the propensity of each customer to acquire car insurance. The spreadsheet provides a propensity score for each customer based on the available data, enabling a quick and efficient analysis of cross-sell opportunities. Through this spreadsheet, the marketing and sales team can identify and prioritize potential customers who are more likely to purchase car insurance, directing their efforts in a more strategic manner and increasing the effectiveness of sales actions.

### 3.2 Tools Used
For the development of this project, we utilized the following tools:

- Python: a popular and powerful programming language used for developing data science and machine learning applications. We used libraries such as pandas, numpy, scikit-learn, and scipy for data manipulation and analysis, as well as for building the machine learning model.
    
- Flask API: a web micro-framework used for creating web applications in Python. We used Flask to develop an API that allows interaction with the propensity model and integration with other tools.

- Visual Studio Code: a source code editor that provides advanced features for development, such as debugging, version control, and integration with various extensions. We used Visual Studio Code as the primary development environment.

- Anaconda: a platform that contains various libraries and tools essential for data analysis. We used Anaconda to manage our virtual environments and install the necessary libraries for the project.

- Git: a widely used version control system for managing changes to source code files. We used Git to track the history of changes in our project.

- Render: we utilized Render to host our web application, which includes the Flask API for interacting with the propensity model. The platform allowed us to deploy and make the application available quickly and reliably, ensuring accessibility to end users.
    
- Google Sheets: we used Google Sheets as one of the visualization and presentation tools for the project results. The interactive spreadsheet in Google Sheets enables convenient and shareable viewing and analysis of customer propensity data.


### 3.3 Development
In this project, we followed the CRISP-DM (Cross Industry Process - Data Mining) methodology, which has been widely adopted as a standard analytical process since 1999. Developed by a consortium of over 200 organizations interested in data mining, this methodology is flexible and can be adapted to different analytical methods, including Data Science.

Although the original version of the CRISP-DM methodology consists of six phases, we chose to use an extended version with ten phases to ensure a comprehensive and detailed approach. These additional phases were added to meet the specific needs of this project and ensure the quality and effectiveness of the analytical process.

My strategy to solve this challenge was as follows:

#### 1. Data Understanding

**1.1  Data Description:** In this step, the goal is to understand the available data and its characteristics. This involves examining the variables present, understanding their meaning, and identifying possible issues such as missing data or inconsistencies.
    
**1.2 Feature Engineering:** Here, the focus is on identifying and creating new variables relevant to the propensity analysis. This may involve combining existing variables, creating derived variables, or selecting specific attributes that have a greater impact on the prediction.
    
**1.3 Variable Filtering:** In this step, the aim is to filter the data to remove irrelevant or duplicate information. This helps reduce the complexity of the data and improve the efficiency of the model.
    
**1.4 Exploratory Data Analysis:** Here, a more in-depth exploration of the data is conducted to identify patterns, trends, and relevant insights. This may involve visualizing the data, analyzing correlations between variables, and identifying potential relationships between the attributes and the target variable.

#### 2. Data Preparation

**2.1 Preprocessing:** In this step, the data is prepared for modeling. This includes handling missing values, encoding categorical variables, normalizing or standardizing the data, and other transformations necessary to ensure data quality and consistency.
    
**2.2 Feature Selection:** Here, the most relevant variables for propensity analysis are selected. This can be done based on statistical techniques such as correlation analysis or specific feature selection algorithms, which help identify the most informative variables for the model.

#### 3. Modeling

**3.1 Machine Learning Modeling:** In this step, a machine learning model is developed to predict the propensity of a customer to acquire car insurance. This involves choosing the appropriate algorithm, training the model with the prepared data, and evaluating the model's performance.
    
**3.2 Hyperparameter Tuning:** Here, the model's hyperparameters are tuned to optimize its performance. This can be done using techniques such as cross-validation and grid search, which help find the optimal combination of hyperparameters that maximize the model's performance.

#### 4. Evaluation and Business Performance

**4.1 Performance Metrics:** Evaluate the model's performance based on relevant metrics for the business, such as conversion rate and return on investment.
    
#### 5. Deployment

**5.1 Model Deployment in Production:** Implement the model in a production environment for ongoing use.


## 4. Data Understanding
The first stage of this process is dedicated to data acquisition and understanding. During this stage, we aim to identify and create new relevant variables for propensity analysis, as well as filter the data to eliminate irrelevant or duplicate information. This is the moment where we delve deeper into data exploration, searching for patterns, trends, and significant insights. We employ statistical techniques and visualizations to identify correlations between variables, validate existing hypotheses, and discover new insights that can contribute to the development of the propensity model. These data understanding steps are crucial to ensure a solid understanding of the available data and the relevant characteristics for the project. This understanding enables us to make informed decisions throughout the modeling process and obtain more accurate results in predicting customer propensity.

The dataset used in this project was obtained from the Kaggle platform. The specific dataset can be accessed through the following [link](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction?select=test.csv).

### 4.1 Data Description
In this initial phase, techniques such as column renaming in snakecase format and identification of missing values (NaN) were applied. Additionally, descriptive statistics were used to understand the distribution of the data, both in terms of numerical and categorical attributes, allowing for the detection of possible patterns and trends.

The dataset contains 19 attributes, listed below:

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
The goal of Feature Engineering is to improve the performance of machine learning models through the transformation and creation of new features from the available data. During this stage, mathematical operations or meaningful combinations of existing features can be applied to create new ones. In the scope of this project, transformations were performed on the DataFrame in order to make categorical values more descriptive.

### 4.3 Data Filtering
In this phase, no data filtering process was required as the available information was already suitable, and there was no need to remove irrelevant or duplicate data.

### 4.4 Data Analysis
During this phase, a detailed analysis of the data was conducted to gain meaningful insights into customer characteristics. Univariate analyses of numerical attributes and the target variable were performed, as well as bivariate analyses to examine each feature individually. Visualizations were used to facilitate the interpretation of the results. Additionally, a multivariate analysis of numerical attributes was conducted to better understand the relationships between variables.

**Insights:**

**1.** The data reveals the existence of 135 policy sales channels, covering a wide range of options for customers. However, it is interesting to note that the top three policy sales channels account for the majority of acquired customers, representing an impressive 79.57% of the total. This highlights the importance of directing marketing and sales strategies towards these most effective channels to maximize the reach and impact of promotional activities.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_policy_salles_channel.png" alt="bivariate_analysis_policy_salles_channel">
</p>


**2.** A relevant finding is the observation that cars over 2 years old have a higher conversion rate compared to others. This indicates that owners of vehicles with longer usage time are more likely to purchase car insurance. This information is valuable for market segmentation definition and the creation of specific strategies to attract this target audience.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_vehicle_age.png" alt="bivariate_analysis_vehicle_age">
</p>


**3.** It has been identified that the age group from 32 to 53 years old shows significant interest in acquiring car insurance. This age group demonstrates a higher propensity to purchase insurance compared to other age groups. This suggests that marketing strategies targeted at this group may be more effective in promoting and selling car insurance.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/bivariate_analysis_age.png" alt="bivariate_analysis_age">
</p>



## 5. Data Preparation
In the second stage, two crucial processes were carried out: data preparation and feature selection.

### 5.1 Data Preparation
In the data preparation phase, specific transformations were applied to the data to allow Machine Learning models to learn the data behavior more efficiently. Some of the transformations performed included standardization, scaling, and encoding.

Standardization is a technique that aims to transform the data to have a mean of zero and a standard deviation of one, which can be useful in certain machine learning algorithms. Scaling, on the other hand, is used to adjust the scale of the data, typically to a specific range, such as [0, 1] or [-1, 1]. This is done to prevent scale differences between variables from affecting the performance of the models.

Encoding is an important step when dealing with categorical variables. It involves transforming these variables into numerical representations, allowing Machine Learning models to work with them.

After applying these transformations, the resulting objects were saved in pickle format. This way, the data preparation in this phase aimed to ensure that Machine Learning models have access to transformed data in an appropriate manner, facilitating their learning and application in future situations.

### 5.2 Feature Selection
During this phase, we performed the selection of the most significant attributes for model training. To achieve this, several strategies were adopted. Firstly, we removed columns considered irrelevant for the analysis. Then, we divided the data into training and testing sets to evaluate the model's performance on previously unseen data.

Additionally, we used the Boruta method, which aims to identify the most relevant features for the model. However, the results obtained with Boruta were not satisfactory, as only one feature was selected. To overcome this situation, we employed the ExtraTreesClassifier algorithm together with the forest.feature_importances_ property. This approach allowed us to identify the most relevant features, and thus we selected the first seven as attributes for the model.

The following figure displays the importance of the features.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/feature_importance.png" alt="feature_importance">
</p>


## 6. Modeling
In this stage, several machine learning models were evaluated, and the performance of each one was analyzed. To optimize the models, specific techniques such as BayesianSearchCV and Random Search were applied to find the ideal combination of hyperparameters that maximize the models' performance.

### 6.1 Machine Learning Modelling
The analysis of different machine learning models, including KNN Classifier, Logistic Regression, Extra Trees Classifier, Random Forest, XGBoost, LGBM, and CatBoost, was conducted in this phase. The cross-validation technique was used to evaluate the actual performance of each model.

During the analysis, Cumulative Gain Curves, a visualization tool, were also used. These curves allow evaluating the performance of a classification model in correctly identifying positive instances. By plotting the cumulative rate of true positives on the y-axis against the cumulative rate of selected positive instances on the x-axis, it is possible to understand how the model behaves at different points of the probability ranking. The following figure presents the Cumulative Gain Curves obtained for the tested models.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/cumulative_gain_all.png" alt="cumulative_gain">
</p>

The Lift Curve analysis was also performed, which is a graphical representation that compares the effectiveness of a predictive model with a random estimate. This metric is commonly used in marketing and customer relationship management to evaluate the performance of models designed to predict customer behavior. The following graph shows the lift curves of the tested models.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/curvas_lift_all.png" alt="curvas_lift_all">
</p>

Performance metrics such as Precision, Recall, and F1-Score were used to evaluate the models' performance, both for simple models and those with cross-validation. The following table displays the results obtained by each model.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/models_CV_metrics.png" alt="models_CV_metrics">
</p>

During the analysis of machine learning models, it was observed that the CatBoostClassifier showed higher values in metrics such as precision, as well as in lift and cumulative gain curves.

However, considering the specific objective of this project, which is to generate a ranking by placing at the top the customers with the highest probability of purchasing car insurance, the recall metric gains greater importance. Recall measures the model's ability to correctly identify customers who are truly interested in acquiring the insurance, thus minimizing the loss of opportunities.

When evaluating the recall metrics, it was observed that the XGBClassifier obtained a higher value compared to the CatBoostClassifier. This indicates that the XGBClassifier model has a greater ability to correctly identify and classify customers prone to acquiring car insurance.

Therefore, even though the CatBoostClassifier showed higher values in metrics such as precision, lift curve, and cumulative gain, we will opt for the XGBClassifier due to its better recall performance. This choice is based on the project's main objective, which is to maximize the identification of customers with the highest probability of acquiring car insurance.


### 6.2 Hyperparameter Finetuning
To find the best hyperparameters for the XGBoost model, hyperparameter search techniques such as Bayesian Search CV and Random Search were applied.

During the hyperparameter search, several parameters were evaluated, including the number of trees, maximum tree depth, learning rate, and others. The main goal was to achieve the best possible performance for the XGBoost model.

After tuning the hyperparameters, the resulting models were evaluated and compared to the previously tested model. Important metrics such as Precision, Recall, and F1-Score were used to assess the model's ability to correctly classify positive and negative instances.

This hyperparameter tuning step is crucial to obtain a model with optimized performance, ensuring that it can correctly identify customers who are likely to acquire car insurance. Selecting the best parameters helps improve the model's precision, recall, and F1-Score, providing more reliable and effective results in customer classification.

The figure below presents the comparison of the three models using evaluation metrics.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/finetuning_xgb.png" alt="finetuning_xgb">
</p>

After evaluating the results, the XGBoost model with hyperparameter tuning using the Bayesian Search technique demonstrated the best performance in terms of recall.


## 7. Evaluation and Business Performance
During this stage, in addition to evaluating the performance of the Machine Learning model, a more in-depth analysis of the results was conducted, converting them into relevant business metrics to assess the effectiveness of the model in ranking customers. Performance indicators such as Precision, Recall, F1-Score, and other project-specific metrics were calculated.

Furthermore, graphs and visualizations were generated to aid in the interpretation of errors and the identification of potential improvements in the model's performance. These visualizations allowed for a more detailed analysis of the results and the identification of patterns or trends that could affect the model's effectiveness in the task of customer ranking.

This comprehensive analysis of the results and the use of relevant business metrics provided a more complete understanding of the model's performance and identified areas for improvement. Based on these analyses, adjustments and refinements can be made to the model to further optimize its performance and ensure better ranking of customers according to their probability of purchasing car insurance.

### 7.1 Model Performance Metrics

Various metrics were used to evaluate the model's performance during the evaluation process. Among these metrics, we have Accuracy, Precision, Recall, F1-Score, and the Area Under the ROC Curve (ROC AUC).

The figure below presents a graph with the values of the metrics obtained by the model:

- Accuracy: Measures the model's rate of correct predictions in relation to the total number of predictions made.
- Precision: Evaluates the proportion of correct positive predictions out of all positive predictions made by the model.
- Recall: Measures the proportion of correctly identified positive instances out of all instances that are truly positive.
- F1-Score: A metric that combines precision and recall into a single measure, providing a balanced evaluation of the model's performance.
- ROC AUC: The Area Under the Receiver Operating Characteristic (ROC) curve is a numerical measure that indicates the model's ability to correctly classify instances.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/model_metrics.png" alt="model_metrics">
</p>

The graph below illustrates the discriminative power of the model in identifying customers with a higher probability of purchase compared to random classification. It represents the model's ability to distinguish between customers with a higher propensity to purchase and those who do not possess this characteristic. The greater the distance between the model's curve and the random reference line, the higher the model's classification capacity.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/cumulative_curve_xgb.png" alt="cumulative_curve_xgb">
</p>

The graph below represents the variation of lift in relation to the accumulated percentage of the dataset. This visualization is useful for identifying that the model performs better compared to the reference situation.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/lift_curve_xgb.png" alt="lift_curve_xgb">
</p>

Below, we have the ROI curve, which allows visualizing the relative improvement provided by the model compared to the baseline over the accumulated percentage of the dataset. This curve is useful for evaluating the model's performance in terms of expected return. The ROI curve shows how the model outperforms expectations compared to the reference situation measured by the baseline. It shows the cumulative proportion of the expected return over time as more customers are considered.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/roi_curve_xgb.png" alt="roi_curve_xgb">
</p>


### 7.2 Business Metrics
In order to evaluate the business performance, a code was developed to calculate the percentage of customers to be contacted, determine the minimum score, and calculate the profit difference between the traditional method and the model used.

The evaluation is based on the product price and the cost of operation per customer. Additionally, obtaining a list of customers ordered according to the score assigned by the model is necessary.

Calculation Details:

- Vehicle insurance price: $550.00
- Cost to contact the customer: $40.00

In the image below, we can observe that it is recommended to contact 47% of the customers, sorted according to the score assigned by the model. Therefore, a score threshold of 0.02 is established to determine which customers should be contacted.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/best_profit.png" alt="best_profit">
</p>

By focusing only on customers with a higher propensity to purchase, the company has the opportunity to reduce unnecessary call costs. As a result, the operation becomes 72.13% more profitable due to the cost savings obtained, as shown in the graph below.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/selected_all_customers.png" alt="selected_all_customers">
</p>

## 8. Deployment
After validating the ranking generation model, the next step was to make it available to end users through an API. This API was developed using the Flask module and is contained in the 'handler.py' file. With this API, users have the ability to obtain rankings of customers with accurate and up-to-date scores.

The API is responsible for loading the trained model, and the HealthInsurance class was created to prepare and transform the necessary data before being provided to the model for score generation. This preparation and transformation ensure that the data is in a suitable format to be processed by the model.

The selected model was deployed in a cloud environment, making it accessible to other individuals or services. This allows them to use the results generated by the model to enhance business decision-making. To facilitate access and sharing of the results, we used Google Sheets, a platform that allows storage and real-time visualization of the data generated by the model. This way, the information is quickly and conveniently available to users who need it, facilitating collaboration and utilization of the results in different business contexts.

<p align="center">
  <img src="https://github.com/raquelEllem/health_insurance/blob/main/img/deploy_healthInsuance.png" alt="deploy_healthInsuance" width="500">
</p>

The final product is a spreadsheet document linked to the deployed machine learning model. This document provides a list of customers with a probability of purchasing car insurance, based on the predictions made by the model. To obtain the predictions, simply enter the customer data, click on "Health Insurance Prediction" - "Get Prediction".

The spreadsheet has been integrated with the deployed model, allowing the scoring of each customer and generating a prediction. Additionally, customers are reorganized based on their scores, creating a ranking that indicates the order in which they should receive the offer.

Within the spreadsheet, customers who have a higher probability of purchasing car insurance are highlighted, allowing for a quick visual identification of the target customers. This integration between the spreadsheet and the model provides a more efficient approach to selecting customers for the offer, maximizing the chances of success for the sales campaign. See the functionality in the demonstration below:

![gif bot](https://github.com/raquelEllem/health_insurance/blob/main/img/gif_func.gif) 


## 9. Conclusion
Based on the results of this project, it can be concluded that the trained model is a precise and reliable tool for generating a ranking of customers with a higher probability of purchasing car insurance. Developed with the XGBoost algorithm, the model achieved improved recall after fine-tuning, indicating its effectiveness in identifying potential customers.

Furthermore, the project demonstrated significant cost savings by reducing unnecessary call-related expenses, resulting in a 72.13% less costly operation. This highlights the potential of the trained model as a valuable tool for the sales and finance teams.

Another relevant aspect is the acquisition of valuable insights for further improvements, such as identifying sales channels with higher returns. This information can guide future strategic decisions of the company, generating additional improvements and potential savings.

In summary, this project illustrates how data analysis can bring tangible and substantial benefits to companies, enabling more efficient and informed decision-making.


## 10. Next Steps

- Collecting new data: Continue the search for relevant data that can contribute to the improvement of the model. This involves expanding the current database, looking for new data sources, and collecting specific information that can enhance the model's performance.
- Explore different feature combinations: Investigate various combinations of features available in the data. This includes creating new variables, selecting the most relevant ones, and transforming existing ones to improve the overall performance of the model.
- Model refinement: Make adjustments and refinements to the current model. This includes hyperparameter optimization, experimenting with different machine learning algorithms, evaluating regularization techniques, and even considering advanced approaches such as using deep learning to achieve even better performance.
- Incorporating user feedback: Collect feedback from end users of the model and use their suggestions and needs to continuously improve the model. This involves conducting review and feedback sessions, identifying gaps and areas for improvement, and implementing adjustments based on the information provided by users.






