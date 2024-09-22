![image](https://github.com/user-attachments/assets/5fbee72a-0246-426a-a927-2c0456293bf1)

# Mini Project: Polars Descriptive Statistics
Adil Keku Gazder <br>
ag825, adil.gazder@duke.edu <br>
IDS 706: Data Engineering Systems <br>
Duke University, Fall 2024 <br >
##

### About the project
[![CI](https://github.com/nogibjj/ag825_polars_descriptive_statistics/actions/workflows/hello.yml/badge.svg)](https://github.com/nogibjj/ag825_polars_descriptive_statistics/actions/workflows/hello.yml) <br>
The aim with this project was to read a .csv file and generate summary statistics and plots describing the data. The dataset used for this project was acquired from Kaggle (Olympic Summer Games - Paris 2024 -> medallists.csv)

Link to the dataset: (https://www.kaggle.com/datasets/muhammadehsan02/olympic-summer-games-paris-2024?select=medallists.csv)

##
### Repository Structure
The structure of this file is as follows:
- .gitignore file
- .github/workflows file
    - Used to define an automated process which will run the pipeline before publishing
    - Will be defined using a YAML file
- Makefile
    - Compilation and maintainence of code
    - Helps manage dependinces
    - Install / Format / Lint / Test
- Requirements file
    - Text file (.txt) detailing the required packages to be installed for this program to run
- main.py
    - aboutdata(): Creates descriptive statistics about the data
    - createplots(): Creates two plots describing the dataset
    - createsummary(): Creates a summary of this analysis and writes to a markdown file (summary_report.md)
- testmain.py
    - Tests that the functions aboutdata() and createplots() in main.py work as expected
- medallists.csv
    - Source data in .csv format
- summary_report.md
    - Final output in a markdown file

##
### Expected Output
This file generates the following on execution:
- Head of the data (top 5 rows of the entire dataset)
- Descriptive statistics about the dataset
    - Count
    - Mean
    - Standard Deviation
    - Minimum value
    - 25th percentile
    - 50th percentile
    - 75th percentile
    - Maximum value
- Bar graph detailing the number of total medals won per country
- Line chart detailing the total medals won per day for each day of the athletics
