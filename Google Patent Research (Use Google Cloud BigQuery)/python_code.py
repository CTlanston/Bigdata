from google.cloud import bigquery
from google.oauth2 import service_account
import matplotlib.pyplot as plt
import numpy as np

## construct credentials from service account key file
credentials = service_account.Credentials.from_service_account_file("C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\manage_bigdata\\HW3\\tche368-big-data-fall2023_srvacct.json")

# construct a BigQuery client object
client = bigquery.Client(credentials=credentials)

from google.cloud import bigquery


# List of dates
ls = [202004, 202007, 202101, 202105, 202111, 202204, 202208, 202212, 202304]

# Dictionary to store counts
count_dict = {}

for date in ls:
    table_name = f'`patents-public-data.google_patents_research.publications_{date}`'
    QUERY = f'''
    SELECT count(distinct publication_number) as cnt
    FROM {table_name}
    where lower(title) like '%covid%'
    '''
    query_job = client.query(QUERY)

    for row in query_job:
        count_dict[date] = row.cnt

# Sort by date
sorted_dates = sorted(count_dict.keys())
sorted_counts = [count_dict[date] for date in sorted_dates]

# Indices for X-axis
indices = np.arange(len(sorted_dates))

# Plotting using Matplotlib
plt.figure(figsize=(12, 6))
bars = plt.bar(indices, sorted_counts, color='blue', alpha=0.7)
plt.xlabel('Index')
plt.ylabel('Count')
plt.title('COVID-related Publications Count')
plt.xticks(indices, [str(i) for i in sorted_dates], rotation=45)
plt.grid(axis='y')

# Annotate each bar with its count
for bar, count in zip(bars, sorted_counts):
    plt.text(bar.get_x() + bar.get_width() / 2 - 0.1, bar.get_height() - 5, str(count))

plt.show()
