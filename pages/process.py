import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

introduction = dbc.Row(
    [
        dcc.Markdown(
            """
            # Process

            
            """
        ),

    ],
)
data_set = dbc.Row(
    [
        dcc.Markdown(
            """
            ## Data

            #### Description:
            *	The data was **extracted from the Chicago Police Department's** CLEAR (Citizen Law Enforcement Analysis and Reporting) system.
            *	For the analysis I selected **2015 – 2017** data. 
            *	This data set contains **539,814 observations** and **23 features**


            ####  Features:    

            I focused on 12 key features for my analyses:
            
            1. **Case Number** - The Chicago Police Department RD Number (Records Division Number), which is unique to the incident.
            2. **Date** - Date when the incident occurred.
            3. **Primary Type** - The primary description of the IUCR code.
            4. **Arrest** - Indicates whether an arrest was made.
            5. **Domestic** - Indicates whether the incident was domestic-related as defined by the Illinois Domestic Violence Act.
            6. **Beat** - Indicates the beat where the incident occurred. A beat is the smallest police geographic area – each beat has a dedicated police beat car. 
            Three to five beats make up a police sector, and three sectors make up a police district. The Chicago Police Department has 22 police districts. See the beats at[ *1](https://data.cityofchicago.org/d/aerh-rz74).
            7. **District** - Indicates the police district where the incident occurred. See the districts at[ *2] (https://data.cityofchicago.org/d/fthy-xz3r).
            8. **Ward** - The ward (City Council district) where the incident occurred. See the wards at[ *3] (https://data.cityofchicago.org/d/sp34-6z76).
            9. **FBI Code** - Indicates the crime classification as outlined in the FBI's National Incident-Based Reporting System (NIBRS). See the Chicago Police Department listing of these classifications at[ *4] (http://gis.chicagopolice.org/clearmap_crime_sums/crime_types.html).
            10. **Year** - Year the incident occurred.
            11. **Latitude** - The latitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
            12. **Longitude** - The longitude of the location where the incident occurred. This location is shifted from the actual location for partial redaction but falls on the same block.
            """
        ),

    ],
)

analysis = dbc.Row(
    [
        dcc.Markdown(
            """
            ## Model

            #### Feature Engineering:

            I started with feature engineering the data set. The approach to clean up the data had 7 steps:

            1. Check how many missing values there are in each feature. If the missing values are less than 10% of total values in the feature was dropped
            2.	Check the feature type and correct it if necessary
            3.	Drop duplicate rows
            4.	Check for location outliers and eliminate them if needed
            5.	Replace False and True by zeros and ones
            6.	Create new features by extracting the month, day and hour from the 'Date' column
            7.	Drop features such as 'ID' and 'UpUpdated On' because they don't have any relevant information for the analyses and 'Date' to avoid duplication (See step n6) 

            #### Target selection:

            I defined three things that would be interesting to predict with this data: 

            1.	The ward where a crime will happen
            2.	The type of crime (Column ‘Primary Type’)
            3.	If a crime will end up in an arrest
            
            Due to the high cardinality of Ward and Primary Type (see table below), **I decided to use ‘Arrest’ feature as the target**

            """
        ),

    ],
)
unique_values = dbc.Row([
    dbc.Col(
        
    html.Img(src='/assets/unique_values.png',style={'width':'20%','height':'100%'})

    )
    ]
    
)
split_title = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            #### Data Split:
            """
        )
        )
    ],
)
split_data = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            The process of splitting the data set was done in two steps:

            1.	Extract the X_features and the y_target from my data frame 
            2.	Split the data using train_test_split from Scikit Learn
            """
        )
        ),
    dbc.Col(
        html.Img(src='/assets/split.png',style={'width':'100%','height':'80%'}
        )
    )
    ],
)
baseline = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            #### Baseline definition:

            The objective of a baseline is to create an initial prediction and calculate an accuracy percentage. This will be the benchmark to beat with the future predictive model. 
            In this case, I used the mode as the prediction because my target is categorical.

            ** Results:** The accuracy of baseline is: 77.19%
            """
        )
        )
    ],
)
base_roc = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/base_result.png',style={'width':'100%','height':'100%'},)
        )
    ],
)
roc = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            My ROC curve tells me this model has no discrimination capacity to distinguish between positive class and 
            negative class
            """
        )
        )
    ],
)
baseline_graph = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/ROC_baseline.png',style={'width':'390px','height':'340px'}
        ))
    ],
)

chose_model = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            #### Model Selection:
            In this process I used three relevant methods and compared their results in order to choose the best method to predict with greater accuracy
           
            1. **Logistic Regression- ** Used when the dependent variable (target) is categorical 
                
             * Accuracy for the validation data = 0.7722

             * Accuracy for the test data = 0.7708
            """
        )
        )
    ],
)
lr_grapgh = dbc.Row([
    dbc.Col(
        html.Img(src='/assets/roc_lr.png',style={'width':'390px','height':'340px'}
        ))
    ],
)

chose_model2 = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            2. **XGBoost- ** A decision-tree-based Machine Learning algorithm that GBT build trees one at a time, where each new tree helps to correct errors made by previously trained tree
                           
             * Accuracy for the validation data = 0.8833

             * Accuracy for the test data = 0.8831
            """
        )
        )
    ],
)
xgb_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/roc_xb.png',style={'width':'390px','height':'340px', 'image-align':'center'},)
        )
    ],
)
chose_model3 = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            3. **RandomForestClassifier- ** RFs train each tree independently, using a random sample of the data. This randomness helps to make the model more robust than a single decision tree, 
            and less likely to overfit on the training data[*5](https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80)
                           
             * Accuracy for the validation data = 0.8891

             * Accuracy for the test data = 0.8904
            """
        )
        )
    ],
)
rf_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/roc_rf.png',style={'width':'390px','height':'340px', 'image-align':'center'},)
        )
    ],
)

answer = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            ##### **Selection **  
           
            ###### **Random Forest Classifier had the best performance with an 89% accuracy**
            """
        )
        )
    ],
)
consfusion_rf = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            #### Confusion for Random forest Classifier

            The number of correct and incorrect predictions are summarized with count values and broken down by each class

            As the table below shows, it predicted 72,840 (sum of the diagonal) out of the 81,660 predictions for the validation set correctly, resulting in an 89% accuracy 

           """
        )
        )
    ],
)
confusion_rf_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/cunfusion_rf.png',style={'width':'400px','height':'340px'},)
        ),
        dbc.Col(
        html.Img(src='/assets/rf_class_rep.png',style={'width':'380px','height':'180px'},)
        )
    ],
)
feature_imp = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
           #### Feature Importances

           Checked the feature importances using the following methods

            * **Dropping Manually**: The tree based feature importance ranks the features


           """
        )
        )
    ],
)

feature_imp_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/feature_imp.png',style={'width':'700px','height':'500px'},)
        )
    ],
)
feature_imp_eli5 = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            * **Using Eli5**: Provides a way to compute feature importance for any black-box estimator by measuring how score decreases when a feature is not available[ *6](https://eli5.readthedocs.io/en/latest/blackbox/permutation_importance.html)
           """
        )
        )
    ],
)
eli_feature_imp_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/eli_imp.png',style={'width':'390px','height':'380px'},)
        ),
        dbc.Col
        (dcc.Markdown(
           """
            The table shows that ‘Primary type’, ‘Description’, ‘IUCR’, and ‘FBI code’ have the highest weights in the predictions
           """
        )
        
        )
    ],
)
shap = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            #### Sample Explanation:

            SHAP (SHapley Additive exPlanations) is a method to explain individual predictions. 

            "SHAP values attribute to each feature the change in the expected model prediction when conditioning on that feature. 
            They explain how to get from the base value that would be predicted if we did not know any features to the current output. 
            This diagram shows a single ordering. When the model is non-linear or the input features are not independent, however, the order in which 
            features are added to the expectation matters, and the SHAP values arise from averaging the values across all possible orderings"[Source](https://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf)
           """
        )
        )
    ],
)
shap_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/shap.png',style={'width':'100%','height':'100%'},)
        )
    ],
)
shap_2 = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            Top 3 reasons for prediction:

            1. IUCR is 1,320
            2. Description is ‘TO VEHICLE’
            3. FBI CODE is 14

            Top counter-argument against prediction:
            ‘Case number’ is HZ353030
            """
        )
        )
    ],
)
pdp = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            ### Partial Dependence:

            """
        )
        )
    ],
)
pdp_grapgh = dbc.Row([
     dbc.Col(
        html.Img(src='/assets/pdp.png',style={'width':'80%','height':'80%'},)
        )
    ],
)
pdp_codes = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            **Primary Type codes:**

            1) Assaults

            2) Battery

            3) Criminal Damage
            
            5) Theft 

            6) Burglary

            8) Narcotics

            10) Deceptive Practive
            
            30) Non-Criminal

            """
        )
        )
    ],
)
pdp2 = dbc.Row([
    dbc.Col(
        dcc.Markdown(
            """
            **PDP** shows the probability  and the interaction of Primary Type  and Domestic features  in the arrest. The plot shows the increase in an arrest probability when the Primary Type is Narcotics. On the other hand, crimes such as criminal damage, 
            theft and burglary have a lower predicted arrest. 

            ###### To clarify, the PDP shows a correlation between the features and the target and don’t pretend to explain causality.
            
            [Documentation and NoteBook here](https://github.com/johanaluna/Chicago)
            """
        )
        )
    ],
)
empty_rows= dbc.Row([
    dbc.Col(
        html.Div(' ',style={'text-align': 'center','font-size':16,'font-weight':'bold','height':'36px'})
    )
])
column_list=[introduction,
empty_rows,
data_set, 
analysis,
unique_values,
empty_rows,
split_title,
split_data,
empty_rows,
baseline,
base_roc,
empty_rows,
roc,
baseline_graph,
empty_rows,
chose_model,
lr_grapgh,
empty_rows,
chose_model2,
xgb_grapgh,
empty_rows,
chose_model3,
rf_grapgh,
answer,
empty_rows,
consfusion_rf,
confusion_rf_grapgh,
empty_rows,
feature_imp,
feature_imp_grapgh,
empty_rows,
feature_imp_eli5,
eli_feature_imp_grapgh,
empty_rows,
shap,
shap_grapgh,
shap_2,
empty_rows,
pdp,
pdp_grapgh,
pdp_codes,
pdp2
]
layout = dbc.Col(column_list)