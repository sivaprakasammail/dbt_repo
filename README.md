> [!IMPORTANT]
> This repo is no longer actively maintained. It’s been preserved for continuity and free access. The Jaffle Shop has lived a rich life as dbt’s demo project, but has been superseded by two newer repositories: [`jaffle-shop`](https://github.com/dbt-labs/jaffle-shop), the premier demo project for dbt Cloud, and [`jaffle_shop_duckdb`](https://github.com/dbt-labs/jaffle_shop_duckdb) which supports working locally via DuckDB for those without access to a cloud warehouse. You’re welcome to continue using this repo as an open source resource, just know it will not be actively maintained moving forward.

## Testing dbt project: `jaffle_shop`

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.

### What is this repo?
What this repo _is_:
- A self-contained playground dbt project, useful for testing out scripts, and communicating some of the core dbt concepts.

What this repo _is not_:
- A tutorial — check out the [Getting Started Tutorial](https://docs.getdbt.com/tutorial/setting-up) for that. Notably, this repo contains some anti-patterns to make it self-contained, namely the use of seeds instead of sources.
- A demonstration of best practices — check out the [dbt Learn Demo](https://github.com/dbt-labs/dbt-learn-demo) repo instead. We want to keep this project as simple as possible. As such, we chose not to implement:
    - our standard file naming patterns (which make more sense on larger projects, rather than this five-model project)
    - a pull request flow
    - CI/CD integrations
- A demonstration of using dbt for a high-complex project, or a demo of advanced features (e.g. macros, packages, hooks, operations) — we're just trying to keep things simple here!

### What's in this repo?



### Running this project
To get up and running with this project:
>This was build on arm mac, otherwise packages are `dbt-core` & `dbt-snowflake` 
1. 
```python
python -m venv venv 
source venv/bin/activate
pip install -r requirements.txt 
```




2. Fill out the  `./snowflake/.envrc_template` --> `./snowflake/.envrc`

3. Ensure your profile is setup correctly from the command line:
```bash
$ dbt debug
```

4. Load the CSVs with the demo data set. This materializes the CSVs as tables in your target schema. Note that a typical dbt project **does not require this step** since dbt assumes your raw data is already in your warehouse.
```bash
$ dbt seed
```

5. Run the models:
```bash
$ dbt run --vars '{"split_percent":".7"}'
```


6. Test the output of the models:
```bash
$ dbt test
```

7. Generate documentation for the project:
```bash
$ dbt docs generate
```

8. View the documentation for the project:
```bash
$ dbt docs serve
```


