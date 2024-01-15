# Project Title: Yelp Data Warehouse & Sakila Movie Recommendation System

## Project Overview
This project is aimed at demonstrating advanced data management and analytical skills, primarily focused on two significant tasks: building a data warehouse for Yelp dataset for real-estate investment analysis and developing a movie recommendation system using the Sakila database. It offers practical insights into effective data warehousing, SQL query optimization, and NoSQL database scalability considerations.

## Part 1: Movie Recommendation System Using Sakila Database
### Objective
- Implement a recommendation system for movies using the Sakila database by calculating cosine similarity scores among users based on their movie rental history.

### Key Steps
1. **Cosine Similarity Calculation**:

 Develop SQL queries to compute similarity scores between user pairs, based on their shared movie rental patterns.
2. **Recommendation Algorithm**: Formulate an algorithm to recommend unwatched movies to a user, guided by the calculated similarity scores.

### Deliverables
- SQL queries for computing cosine similarity.
- SQL queries for generating movie recommendations.
- Sample output showing the first 10 rows of similarity results.
- Recommendation results for a selected user, including user ID, name, film ID, and film title.

## Part 2: Yelp Data Warehouse for Real-Estate Investment Planning
### Objective
- Create a data warehouse with a star schema using the Yelp dataset to assist in making informed real-estate investment decisions based on business foot traffic and ratings in various zip codes.

### Data Source
- https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset/versions/6

### Key Steps
1. **Data Import and Preparation**: Load the Yelp dataset into a relational database, focusing on handling large data volumes.
2. **Star Schema Creation**: Develop and implement fact and dimension tables tailored to real-estate investment metrics.
3. **ER Model Development**: Create an Entity-Relationship (ER) model to visually represent the star schema.

### Deliverables
- SQL scripts for data import and initial table creation, along with the first 5 rows of each table as a sample.
- SQL queries for Extract, Transform, Load (ETL) operations into the star schema.
- An ER diagram illustrating the star schema for the data warehouse.

## Part 3: NoSQL Database Scalability (CAP Theorem Discussion)
### Objective
- Analyze and discuss the scalability of Yelp's business database from a global expansion perspective, focusing on the CAP theorem and the potential transition of specific tables to a NoSQL database.

### Deliverable
- A detailed write-up (maximum one page, double-spaced, 12-point font) discussing the application of the CAP theorem in scaling the database, including which tables might be suitable for transition to NoSQL databases.

## Collaboration and Methodology
- **Task Breakdown**: Approach the project by breaking down complex tasks into smaller, manageable components.
- **Data Loading Challenges**: Anticipate and address challenges in loading large datasets, ensuring correct data formatting and server configurations.
- **Teamwork**: Collaborate effectively with team members, sharing insights and align

ing strategies to ensure cohesive and comprehensive solutions. Regular discussions and collective brainstorming sessions are crucial for successful project outcomes.

## Usage
- Follow each step diligently, ensuring accuracy in SQL query formulation and implementation.
- Pay close attention to the design and development of the data warehouse, ensuring it aligns with the project's real-estate investment objectives.
- Engage in thoughtful discussions regarding the scalability of the Yelp database, considering different aspects of the CAP theorem.

## Note
- Emphasis should be placed on practical application of data warehousing principles, SQL querying techniques, and understanding the implications of the CAP theorem in a real-world business scenario.
- The project serves as a demonstration of a data engineer or data scientist's capability to handle large datasets, design efficient data models, and make strategic decisions based on data analysis.

This README provides a structured guideline for the Yelp Data Warehouse & Sakila Movie Recommendation System project. Detailed implementation steps, query formulations, and analytical discussions should be referred to within the respective deliverables and documentation for each part of the project.