import holidays
import snowflake.snowpark as snowpark
import pandas as pd
from snowflake.snowpark.functions import col

def is_holiday(date_col):

    not_french_holidays = holidays.country_holidays('US')
    is_holiday = (date_col in not_french_holidays)
    return is_holiday * 1 


def return_self(x):
    return x 

def model(dbt, session):
    #you can add a stage with imports = ['@stage_name/filename]
    dbt.config(materialized="table", packages=['holidays','pandas'])
    ord = dbt.ref("orders")
    pmts = dbt.source('sales', "raw_payments")
    sel_expr = [ord.col(c).alias(c) for c in ord.columns] + [pmts.col('PAYMENT_METHOD').alias('PAYMENT_METHOD')]
    # join snowpark df
    join_df = ord.join(pmts, ord.ORDER_ID == pmts.ORDER_ID)

    # To pandas for one hot 
    pandas_df =  join_df.select(*sel_expr).to_pandas()
    pandas_df["IS_HOLIDAY"] = pandas_df["ORDER_DATE"].apply(is_holiday)
    dum_df = pd.get_dummies(pandas_df, columns=['STATUS', 'PAYMENT_METHOD'] )
    cols_to_01 = list(set(dum_df.columns) - set(pandas_df.columns )) 
    dum_df[cols_to_01] = dum_df[cols_to_01].apply(lambda x: x *1 )
    
    #back to snowpark df
    snowpark_df = session.create_dataframe(data=dum_df)
   
    # add a column and drop order date so all numeric 
    return snowpark_df.withColumn("return_self", return_self(snowpark_df["order_id"])).drop('order_date')