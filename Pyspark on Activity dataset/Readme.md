# pySpark Activity Tracker 

## Project Overview
This project aims to develop a structured Spark streaming application using pySpark for recommending activities based on data analysis. The primary task is to process and analyze activity data using various tumble window sizes to generate insights and recommendations.

## Key Steps

1. **Data Preparation**
   - Download the activity-data from the provided source.
   - Upload the data to an AWS S3 bucket.

2. **Spark Streaming Setup**
   - Use pySpark to load the data as Spark structured streaming data.
   - Set `maxFilesPerTrigger` to 5 for the streaming process.

3. **Data Analysis and Recommendation**
   - Analyze the data to estimate counts and mean values of “x”, “y”, and “z” for different activities ("gt") using tumble windows of 5, 15, and 30 minutes.
   - Append these results to a results table, continuing the query until all data is read.
   - Determine a reasonable sleep value and loop range for processing the data.
   - For a 15-minute tumble window:
       - Recommend "standing" if the count of “sit” activities is more than “stand” activities.
       - Recommend "movement" if the average distance moved is smaller in the current window compared to the previous one.

4. **Data Visualization (Optional)**
   - Plot a chart comparing time-varying values with static values to identify trends.

5. **Case Study Review**
   - Watch Conviva's Spark application case

 study on streaming data.
   - Develop and discuss a similar Spark framework for the activity tracker based on the insights gained from the case study.

## Submissions

1. **Python Code**
   - Submit the Python code developed for the activity tracker.
   - Ensure the code is well-commented and structured for readability and maintainability.

2. **Framework Write-up**
   - A one-page (double-spaced) write-up discussing the Spark framework used for the activity tracker.
   - Include key aspects of the framework, challenges faced, and how they were addressed.

## Tips and Collaboration

- Collaborate with team members to share insights and strategies for effective data processing and analysis.
- Experiment with different configurations and parameters to

 optimize the streaming process and achieve accurate results.
- Discuss each step and its implications within the team to ensure a comprehensive understanding and approach.

This project not only demonstrates technical prowess in using pySpark for streaming data analysis but also emphasizes the importance of teamwork and effective communication in a data science environment. The practical application of Spark streaming, combined with theoretical insights from the case study, provides a robust understanding of real-world data processing challenges and solutions.
