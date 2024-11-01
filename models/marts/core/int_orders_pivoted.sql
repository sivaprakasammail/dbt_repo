{%- set status_list = ['completed', 'shipped', 'returned', 'return_pending', 'placed'] -%}

with orders as (
    select * from {{ ref('stg_orders') }}
),

pivoted as (
    select
        order_id,
        {% for value in status_list -%}
        (case when status = '{{ value }}' then 1 else 0 end) as {{ value }}_status
        {%- if not loop.last -%}
            ,
        {%- endif %}
        {% endfor %}
    from orders
)

select * from pivoted