
import snowflake.snowpark as snowpark
import pandas as pd
from snowflake.snowpark.functions import col
import os
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split , GridSearchCV
import joblib


#https://docs.snowflake.com/en/developer-guide/snowpark/python/python-snowpark-training-ml
def model(dbt, session):
    #you can add a stage with imports = ['@stage_name/filename]
    dbt.config(materialized="table", packages=['holidays','pandas','scikit-learn','joblib'])
    train_data_df = dbt.ref("agg_to_customer_lvl").to_pandas()
    split_per = float(dbt.config.get('split_percent'))
  # Print a sample of the dataframe to standard output.
    
    X = train_data_df.drop('VALUE_RESPONSE', axis = 1)
    y = train_data_df['VALUE_RESPONSE']

    # Split dataset into training and test
    test_size_ = 1.0 - split_per
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_, random_state = 50)
 
    #Preprocess numeric columns
    numeric_features = [ c for c in train_data_df.columns if c != 'VALUE_RESPONSE']
    numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numeric_features)])

    # Create pipeline and train
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),('classifier', LinearRegression(n_jobs=-1))])
    model = GridSearchCV(pipeline, param_grid={}, n_jobs=1, cv=5)
    model.fit(X_train, y_train)

    # Upload trained model to a stage
    model_file = os.path.join('/tmp', 'model.joblib')
    joblib.dump(model, model_file )
    session.file.put(model_file, "@models",overwrite=True)

    #get saved model
    get_result1 = session.file.get("@models/model.joblib.gz", '/tmp')
    print(get_result1)
    print(os.listdir('/tmp'))
    model_loaded = joblib.load(model_file)
    

    

    ##create return 
    score_pdf = pd.DataFrame(dict(R2_train_score=[model_loaded.score(X_train, y_train)], R2_test_score=[model_loaded.score(X_test, y_test)]))
    score_df = session.create_dataframe(data=score_pdf)

    return score_df

    
    