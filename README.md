# 🛫💺 ETL project - MAD departures 💺🛫

<p align="center">
  <img width="1000" height="400" src="https://github.com/arromeral/ETL-MAD-arromeral/assets/138980560/e64e0208-2f25-4486-8eb3-cf2a4902dd0a">
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
- [**main**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main): 
   - [**data**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data): Folder that contains the main data used in the project, both extracted and transformed for later loading.
     - [**eurocontrol_MAD_data**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/eurocontrol_MAD_data): Folder with data relating to air traffic obtained from Eurocontrol      
     - [**flights**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/flights): Folder with data referring to flight records obtained from flightera
     - [**metar**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/data/metar): Folder with data referring to the METAR reports obtained from tutiempo.net
   - [**images**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/main/images): Folder with the images used in this document.
- [**Jupyter Notebooks**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/Jupyter%20Notebooks): Folder with the Jupyter Notebooks used during de Extraction and Transforming stages.
   - [**flights_extraction.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/flights_extraction.ipynb): Jupyter notebook in which the process of extracting the target flight records is developed.
   - [**parallel_webscrapping_metars.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/parallel_webscrapping_metars.ipynb): Jupyter notebook in which the extraction process of the target METAR reports is developed.
   - [**eurocontrol_extract_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/eurocontrol_extract_cleaning.ipynb): Jupyter notebook in which the extraction and cleaning process of daily airport information data is developed.
   - [**flights_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/flights_cleaning.ipynb): Jupyter notebook in which the transformation and cleaning process of the extracted flight records is developed
   - [**metar_cleaning.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/metar_cleaning.ipynb): Jupyter notebook in which the transformation and cleaning process of the extracted METAR reports is developed.
   - [**cross_tables.ipynb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/Jupyter%20Notebooks/cross_tables.ipynb): Jupyter notebook in which the flight records are crossed with the METAR and with the daily airport data to be able to have each of the flights with its closest previous meteorological report and with the air traffic information of the same day.
- [**src**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/src):
   - [**funflights.py**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/src/funflights.py): Python file with the functions used in the transformation and cleaning of the flights.
   - [**funmetar.py**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/src/funmetar.py): Python file with the functions used in the transformation and cleaning of the METAR records.
- [**sql**](https://github.com/arromeral/ETL-MAD-arromeral/tree/main/sql):
   - [**flights_EERD_structure.mwb**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/sql/flights_EERD_structure.mwb): File with the EER Diagram of the relational Database created.
   - [**mad_flights.sql**](https://github.com/arromeral/ETL-MAD-arromeral/blob/main/sql/mad_flights.sql): File to import the Database created.
