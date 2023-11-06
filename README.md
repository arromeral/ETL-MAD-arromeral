# 🛫💺 ETL project - MAD departures 💺🛫

<p align="center">
  <img width="1000" height="400" src="https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/053016ad-fd75-46e3-8bb2-b941fc703e16">
</p>

## Description
This project consists of a complete ETL process (Extract-Transfor-Load) for the generation of a database.
The main guidelines for developing the project are the following:
- Use at least 3 different sources.
- Apply at least two different extraction methods.

The topic on which the project is based will be the generation of a database of all flight departures from the *Madrid-Barajas Adolfo Suárez Airport* over a period of one year **(November 2022 - October 2023)**.
Additionally, [METAR](https://skybrary.aero/articles/meteorological-aerodrome-report-metar) weather reports for the same period will be extracted, as well as daily data about airport congestion in that period, such as number of operations, cancellation rate, average delays, etc.

## Contents
The contents of the project are as follows:

- [**data**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data): Folder that contains the main data used in the project, both extracted and transformed for later loading.
   - [**eurocontrol_MAD_data**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/eurocontrol_MAD_data): Folder with data relating to air traffic obtained from Eurocontrol.      
   - [**flights**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/flights): Folder with data referring to flight records obtained from flightera.
   - [**metar**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/metar): Folder with data referring to the METAR reports obtained from tutiempo.net.
- [**images**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/images): Folder with the images used in this document.
- [**Jupyter Notebooks**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/Jupyter%20Notebooks): Folder with the Jupyter Notebooks used during de Extraction and Transforming stages.
   - [**flights_extraction.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/flights_extraction.ipynb): Jupyter notebook in which the process of extracting the target flight records is developed.
   - [**parallel_webscrapping_metars.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/parallel_webscrapping_metars.ipynb): Jupyter notebook in which the extraction process of the target METAR reports is developed.
   - [**eurocontrol_extract_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/eurocontrol_extract_cleaning.ipynb): Jupyter notebook in which the extraction and cleaning process of daily airport information data is developed.
   - [**flights_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/flights_cleaning.ipynb): Jupyter notebook in which the transformation and cleaning process of the extracted flight records is developed.
   - [**metar_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/metar_cleaning.ipynb): Jupyter notebook in which the transformation and cleaning process of the extracted METAR reports is developed.
   - [**cross_tables.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/cross_tables.ipynb): Jupyter notebook in which the flight records are crossed with the METAR and with the daily airport data to be able to have each of the flights with its closest previous meteorological report and with the air traffic information of the same day.
- [**src**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/src):
   - [**funflights.py**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/src/funflights.py): Python file with the functions used in the transformation and cleaning of the flights.
   - [**funmetar.py**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/src/funmetar.py): Python file with the functions used in the transformation and cleaning of the METAR records.
- [**sql**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/sql):
   - [**flights_EERD_structure.mwb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/sql/flights_EERD_structure.mwb): File with the EER Diagram of the relational Database created.
   - [**mad_flights.sql**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/sql/mad_flights.sql): File to import the Database created.

## Methodology & Sources
Below, the sources and tools used in each of the stages of the project will be briefly explained.

<details close>
<summary>EXTRACT STAGE</summary>
<br>
  
<details close>
<summary>Fligth Departures Records</summary>
<br>
To extract the records of the desired flights, the webscrapping technique has been used on the flightera website (https://www.flightera.net/en/) , which maintains a rich record of flights since at least 2017.
The main tools used have been Selenium and Pandas.
</details>

<details close>
<summary>METARs</summary>
<br>
To extract the desired METAR reports, the webscrapping technique has been used on the tutiempo website (https://www.tutiempo.net/registros/lemd) , which maintains a rich record of METAR reports since many years ago. 
Furthermore, the structure of said website allows the parallelization of the process, which has considerably reduced the extraction time.
The main tools used have been Joblib, Selenium and Pandas.
</details>

<details close>
<summary>Daily MAD Airport traffic data</summary>
<br>
To extract de desired daily traffic data for the MAD Airport the Eurocontrol website (https://www.eurocontrol.int/Economics/DailyTrafficVariation-States.html) has been used, which has an interesting dashboard with valuable information about air traffic in the main European airports.
The website also allows downloading many of the data shown in XLSX format.

Two documents have been downloaded, one related to daily operations at each airport and another with punctuality data.
Once downloaded, the most relevant information has been filtered and a single DataFrame has been generated.

<img width="563" alt="mad_info" src="https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/44352796-768b-4ef1-9f27-dee495a1a655">

The main tools used have been Pandas and Excel.
</details>
</details>
</details>

<details close>
<summary>TRANSFORM STAGE</summary>
<br>
  
<details close>
<summary>Fligth Departures Records</summary>
<br>
In this stage the flight records obtained previously had been cleaned. The final result of the cleanup is a DataFrame with the following columns:
<img width="556" alt="flights" src="https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/2e92310e-ad76-4c94-a42b-57e7d48bc696">

  - **flight_id:** Column with a unique id for each flight, to be able to relate it later with the rest of the data.
  - **Departure_date_time:** Column in Datetime format with the date and time scheduled for flight departure.
  - **cod_flight_IATA:** IATA flight code.
  - **cod_flight_ICAO:** ICAO code of the flight.
  - **day:** Column in Datetime format with the day of the flight.
  - **week_day:** Column with the day of the week.
  - **status:** Column with the status of the flight (Landed, Cancelled, Derived...).
  - **airliner:** Name of the flight operator.
  - **cod_airliner_IATA:** IATA code of the company.
  - **cod_airliner_ICAO:** ICAO code of the company.
  - **Scheduled_dep:** Scheduled time for flight departure.
  - **depart_time:** Actual flight departure time.
  - **dep_situation:** Flight departure status (late, early, on time...).
  - **dep_mins_of_delay:** Minutes late or early in the flight departure.
  - **city:** City of the destination airport.
  - **cod_airport_IATA:** IATA code of the destination airport.
  - **cod_airport_ICAO:** ICAO code of the destination airport.
  - **arrival:** Local time of flight arrival.
  - **arr_situation:** Flight arrival status (late, early, on time..).
  - **arr_mins_of_delay:** Minutes late or early in the arrival of the flight.
  - **duration:** Duration of the flight rounded to hours.
  - **subtraction:** Column that subtracts from p_mins_of_delay and arr_mins_of_delay to detect anomalies in the records.

After the cleaning process, a data frame with **176596 recorded flights** and **22 columns** has been obtained.


</details>

<details close>
<summary>METARs</summary>
<br>
In this stage the METAR reports obtained previously will be cleaned. The final result of the cleanup is a DataFrame with the following columns:

<img width="415" alt="metars" src="https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/7e1022d2-d587-407e-b495-a46cc3487e63">


  - **Metar_id:** Column with a unique id for each Metar part, to be able to later relate it to the flights.
  - **Date_time:** Column in Datetime format with the date and time of issue of the report.
  - **Day:** Column with the day on which the report was issued in YYYY-MM-DD format.
  - **Hour:** Time in which the report was issued in HH:MM format.
  - **Condition:** Meteorological condition of the report.
  - **Temperature:** Temperature in degrees Celsius [º].
  - **Wind:** Wind speed in knots or nautical miles per hour [knots].
  - **Gusts:** Gust speed if any in knots or nautical miles per hour [knots].
  - **Relative_hum:** Relative humidity in percent [%].
  - **Pressure:** Atmospheric pressure in hectopascals [hPa].

After the cleaning process, a data frame with **17722 recorded flights** and **10 columns** has been obtained.
</details>
</details>
</details>

<details close>
<summary>LOAD STAGE</summary>
<br>
Once the three tables have been generated and cleaned, the relational database has been generated. To do this, the flight table has been crossed with the METAR table to add a column to the flight records with the id of the previous weather report closest to the time of the flight.
Similarly, the flight table has been crossed with the airport's daily air traffic information table to include the record of the flight day report.

Once the tables have been related, the database has been generated in MySQL and the data has been loaded.
In the image below is the EERD diagram of the database.
![EERD](https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/f25c87eb-9fda-4053-8b45-723cd99a3fd0)
</details>
