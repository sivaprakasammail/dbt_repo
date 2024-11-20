{% macro sleep(seconds=1) %}
    {% do print('sleeping for ' ~ seconds ~ ' seconds') %}
    {% set query %}
        call system$wait({{ seconds }}, 'SECONDS');
    {% endset %}
    {% set r = run_query(query).columns[0].values()[0] %}
    {% do print(r) %}
{% endmacro %}
