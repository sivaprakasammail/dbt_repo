{{config(materialized='table')}}

select 


CUSTOMER_ID,
sum(CREDIT_CARD_AMOUNT) CREDIT_CARD_AMOUNT,
sum(COUPON_AMOUNT) COUPON_AMOUNT,
sum(BANK_TRANSFER_AMOUNT) BANK_TRANSFER_AMOUNT,
sum(GIFT_CARD_AMOUNT) GIFT_CARD_AMOUNT,
sum(AMOUNT) AMOUNT,
sum(IS_HOLIDAY) IS_HOLIDAY,
sum("STATUS_completed") "STATUS_completed",
sum("STATUS_placed") "STATUS_placed",
sum("STATUS_return_pending") "STATUS_return_pending",
sum("STATUS_returned") "STATUS_returned",
sum("STATUS_shipped") "STATUS_shipped",
sum("PAYMENT_METHOD_bank_transfer") "PAYMENT_METHOD_bank_transfer",
sum("PAYMENT_METHOD_coupon") "PAYMENT_METHOD_coupon",
sum("PAYMENT_METHOD_credit_card") "PAYMENT_METHOD_credit_card",
sum("PAYMENT_METHOD_gift_card") "PAYMENT_METHOD_gift_card",
max(VALUE_RESPONSE) VALUE_RESPONSE
from {{ref('add_response')}}

group by CUSTOMER_ID
