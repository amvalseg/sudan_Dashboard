# Sudan humanitarian crisis analysis - Dashboard in Power BI

💡 In this dashboard, we explore different dimensions of the *humanitarian* crisis in Sudan using data from 2023 and 2024. Specifically, it presents data on *internally displaced persons* due to armed conflict, asylum applications filed by Sudanese citizens abroad, responses to asylum requests from Sudanese populations, and irregular migration of Sudanese individuals to Europe.

# 🌐 **Getting DATA** 

For this analysis, we are getting the following data:

1️⃣ Internally Displaced People Data, from the IOM DTM AP: 
https://dtm.iom.int/data-and-analysis/dtm-api
  👉 Access the API directly from Power BI using the "Web" connector. You can find the URLs used in this repository at: IOM_api/urls.
  👀 Two separate connections are made, as each one returns data from a specific tracking operation by IOM, with data that complements each other.

2️⃣ Data on asylum applications filed by Sudanese nationals abroad and responses to these applications by receiving countries, from the UNHCR API:
https://api.unhcr.org/docs/refugee-statistics.html
  👉 Access the API directly from Power BI using the "Python script" connector. You can find the scripts in this repo at: scripts
  👀 Since the base URL changes, each script is designed to handle the specific connection for either the asylum applications dataset or the decisions dataset.

3️⃣ Data on irregular arrivals to Europe, from the IOM Datasets database: https://dtm.iom.int/datasets
  👉 Download the data and conect it using the Excel connector in Power BI. Find the dataset in this repo: data/DTM_Mixed Migration Flows to Europe_Q3_2024.xlsx  &  data/DTM_Mixed Migration Flows to Europe_Yearly_2023.xlsx
  
4️⃣ UNSD Countries and Regions. To provide greater consistency to the report, the dataset from the UNSD (United Nations Statistics Division) on countries and regions is incorporated, ensuring the use of standardized international nomenclatures.
  👉 Find it at: data/Table of countries by UNCHR.xlsx

5️⃣ To construct the shape map, a topoJSON file containing the districts of Sudan (second-level administrative borders) is incorporated.
  👉You can find it at this repo: visuals/Sudan.json
  👀The original version came from: https://geoportal.icpac.net/layers/geonode:sudan_admin_leve2/metadata_detail

6️⃣ Finally, a table containing the current population data of Sudan is manually incorporated to calculate percentages based on this data in the report.
  👉Data from: https://worldpopulationreview.com/countries/sudan
