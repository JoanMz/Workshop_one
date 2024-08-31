<h1 align="center">ETL-Candidates-Job-Data-Doc</h1>

![Oso de anteojos bearmu](https://github.com/JoanMz/Workshop_one/assets/103477035/e94bced5-f8a6-4334-b6eb-8691fcfb0b6a)
---
**Description**
<p>A litle etl proyect to practice <b>Sql - python - git -github - notebooks - clean_code </b> make the Exploratory Data Analysis (EDA) process identify the columns, search and clean outliers, understate the context and the data for get insights and know how to handle the data get value from the data and finally do the following visualizations</p>

- Hires by technology (pie chart)
- Hires by year (horizontal bar chart)
- Hires by seniority (bar chart)
- Hires by country over years (USA, Brazil, Colombia and Ecuador only) (multiline chart)

<p>The Initial dataset is a syntetic random dataset have 50.000 entries and 11 attributes the most important are the followings columns</p>

- YOE -> years of experience
- Application Date
- Seniority
- Country
- Technology
- Code_challenge_Score
- Technical_Interview_Score

<p>We are looking for response the basics questions and get the pertinent viz and get some conclusions</p>


<p>ENVIRONMENT VARIABLES</p>
- DB_HOST      <- This is the host of Postgres DB  example (127.0.0.1)
- DB_USER      <- This is the user who access in the connection 
- DB_PASSWORD  <- The password of the Postgres DB
- DB_PORT      <- The port of Postgres DB example (5432 default port)
- DB_DATABASE  <- The name of the Database o Schema
- DB_TABLE1    <- The name of the raw data table
- DB_TABLE2    <- The name of the clean data table


<p>FIRST INSTALL THE TOOLS</p>
•	PYTHON
•	POSTGRESQL
•	JUPYTER NOTEBOOKS
•	POWERBI



<h4 align="center">
🐼 Proyect Done 🐼
</h4>


- `Preload` : we get a csv file and before of work we load the data in  a sql engine in this case postgresql
- `sql_connector` : this directory have the definition of the connection that is used from create the tables and connect our querys trhougth the sqlalchemy engine
- `EDA` : in this notebook we can get the visualizations and see the process of cleaning or analisys and the state of our data
- `load_new_data` : in this part we can add new data without delete the database or the registers

  <h4 alingn="center"> How to Run </h4>


<ol>
  <li>Create a virtual env <pre>python -m venv venv</pre></li>
  <li>Use the virtual env <pre>./venv/Scripts/activate</pre></li>
  <li>Install the libraries <pre>pip install -r requirements.txt</pre></li>
  <li>Create and config yours credentials at the .env file</li>

  ![Captura de pantalla 2024-03-06 163650](https://github.com/JoanMz/Workshop_one/assets/103477035/6f8576ba-864c-4262-b768-6e1581d70fda)

  <li>create the table workshop_one at postgres engine (pgadmin psql)</li>

  ![Captura de pantalla 2024-03-06 173456](https://github.com/JoanMz/Workshop_one/assets/103477035/521a4ccc-8ff4-473b-9c1d-158dc119b2d8)
  ![Captura de pantalla 2024-03-06 173335](https://github.com/JoanMz/Workshop_one/assets/103477035/37f0e512-8bf1-47fa-b487-de50257c3969)
  <li>Run the postgres_connect script</li>
  <li>Run the Pre_load notebook</li>
  <li>Run the EDA Notebook</li>

</ol>







