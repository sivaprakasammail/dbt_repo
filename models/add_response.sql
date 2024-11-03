select ptt.* , c.CUSTOMER_LIFETIME_VALUE VALUE_RESPONSE  
from {{ ref('prepare_train_test') }} ptt
JOIN 
{{ref('customers')}} c 
ON c.customer_id = ptt.customer_id 