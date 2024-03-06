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


<h4 align="center">
🐼 Proyect Done 🐼
</h4>


- `Preload` : we get a csv file and before of work we load the data in  a sql engine in this case postgresql
- `sql_connector` : this directory have the definition of the connection that is used from create the tables and connect our querys trhougth the sqlalchemy engine
- `EDA` : in this notebook we can get the visualizations and see the process of cleaning or analisys and the state of our data
- `load_new_data` : in this part we can add new data without delete the database or the registers

