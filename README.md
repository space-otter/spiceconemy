# Spiceconemy

Spiceconemy is a data visualization project that explores the international dynamics of spice production, trade, and consumption using real-world data. Powered by a detailed dataset containing annual trade records for various spices across countries and years, the project brings the hidden networks of the global spice economy to life.

This interactive visualization platform enables users to investigate how different countries participate in the global spice market — as producers, consumers, importers, or exporters — and how these roles shift over time.



## Goals

- Present a visually engaging, intuitive representation of spice trade flows.
- Enable users to explore data by spice type, country, or year.
- Highlight key global players in spice production and consumption.
- Reveal regional dependencies, trade imbalances, and historical patterns.
- Educate users on the cultural and economic relevance of specific spices.

## Features

- 🌐 Interactive world map showing import/export routes
- 📊 Time-series charts for volume and value trends
- 🔍 Filters by spice type, region, or country
- 📈 Rankings of top importers/exporters for selected years

## Dataset Overview

The project uses a structured dataset comprising over 45,000 records from multiple years and countries. Each record contains:

- 🌐 Country (Area)
- 📆 Year
- 🌶️ Spice Type (e.g., "Anise, badian, coriander, cumin, caraway, fennel, and juniper berries")
- 📥 Import volume
- 📤 Export volume
- 🌱 Local production
- 🍽️ Estimated consumption

## Other sources 

- [FAOSTAT](https://www.fao.org/faostat/en/#home)
- [UN Comtrade](https://comtrade.un.org/)

## Setup

1. install python 3
2. create a virtual environment by running `python -m venv .venv` (Linux) or `python -m venv venv` (Windows)
3. activate your virtual environment by running `source .venv/bin/activate` (Linux) or `venv\Scripts\activate` (Windows)
4. install the required packages by running `pip install -r requirements.txt`