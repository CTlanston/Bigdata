 Google Cloud Public Patent Database Query Project README

 Project Overview
This project involves connecting to Google Cloud BigQuery's public datasets using Python, specifically focusing on the Google Patent Research Dataset. The primary goal is to query the dataset for patents containing the word "covid" in their titles, across different periods from April 2020 to April 2023, and visualize this data using matplotlib.

 Data Source
- Google Cloud BigQuery Public Datasets: [Google Marketplace Datasets](https://console.cloud.google.com/marketplace/browse;page=1?filter=solution-type:dataset)
- Google Patent Research Dataset: [Google Patents Research Data](https://console.cloud.google.com/marketplace/product/google_patents_public_datasets/google-patents-research-data?project=black-function-184718)

 Key Steps
1. Cloud Connection: Set up a connection to Google Cloud BigQuery using Python. Refer to the provided tutorial for guidance.
2. Dataset Exploration: Explore the available public datasets and specifically the Google Patent Research Dataset.
3. Data Querying: Write a Python script to query the dataset, focusing on patents with "covid" in the title from April 2020 to April 2023.
4. Data Visualization: Utilize matplotlib in Python to visualize the frequency of these patents over the specified period.

 Requirements
- Python environment with necessary libraries (`google-cloud-bigquery`, `matplotlib`).
- Google Cloud account with access to BigQuery.

 Project Deliverables
- Python script for connecting to Google Cloud BigQuery, querying the dataset, and visualizing the results.
- A chart or graphical representation of the patent data over the specified period.

 Usage
- Ensure you have a Google Cloud account with access to BigQuery.
- Install required Python libraries and set up authentication for Google Cloud in your Python environment.
- Run the provided Python script to perform the data query and visualization.

Note: This README provides an overview of the project. Detailed instructions, Python code, and visualization examples are included in the accompanying files.
