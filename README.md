# Tourism Analytics & Recommendation System

## 1. Methodology

This project follows an end-to-end data science workflow to analyze tourism transaction data, identify visitor and attraction patterns, develop predictive models, and generate personalized attraction recommendations.

The methodology consists of the following stages:

1. Understand and validate the available datasets.
2. Clean and integrate the related tourism tables.
3. Perform exploratory data analysis to identify important behavioral and geographic patterns.
4. Engineer user-level and attraction-level features.
5. Develop a regression model for attraction rating prediction.
6. Develop a multiclass classification model for visit mode prediction.
7. Build a recommendation system using collaborative and content-based approaches.
8. Integrate the outputs into a Streamlit application.
9. Package the project for reproducibility and deployment.

The objective is to maintain a clear separation between data preparation, analysis, modeling, recommendation, and application layers.

---

# 2. Project Architecture

```text
                    Tourism Data Sources
                            │
                            ▼
                Data Understanding & Validation
                            │
                            ▼
                   Data Cleaning & Integration
                            │
                            ▼
                     Cleaned Tourism Data
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
            EDA      Feature Engineering   Aggregations
             │              │              │
             │              ▼              │
             │      ┌───────┴────────┐     │
             │      │                │     │
             │      ▼                ▼     │
             │  Regression     Classification
             │      │                │
             │      ▼                ▼
             │  Rating Prediction  Visit Mode
             │                     Prediction
             │
             ▼
       Tourism Insights
             │
             ▼
      Recommendation System
             │
       ┌─────┴─────┐
       ▼           ▼
Collaborative   Content-Based
 Filtering       Filtering
       │           │
       └─────┬─────┘
             ▼
     Streamlit Application
             │
             ▼
       Deployed Web App
```

---

# 3. Project Overview

The Tourism Analytics & Recommendation System is an end-to-end data science project built using tourism transaction, visitor, attraction, geographic, and categorical reference datasets.

The project covers:

* Data cleaning and validation
* Exploratory data analysis
* Feature engineering
* Rating prediction
* Visit mode classification
* Collaborative filtering
* Content-based recommendations
* Interactive analytics
* Streamlit application development

The final analytical dataset contains **52,930 tourism transactions**, representing **33,530 users** and **30 attractions**.

---

# 4. Business Problem

Tourism platforms generate large amounts of information about visitors, attractions, ratings, locations, and travel behavior. Without systematic analysis, it is difficult to identify the most important tourism markets, understand visitor preferences, predict visitor behavior, and recommend relevant attractions.

This project addresses the problem through three complementary capabilities:

### Descriptive Analytics

Understand:

* Where visitors are coming from
* Which attractions receive the most activity
* Which attraction categories are popular
* How visitors rate attractions
* How visit modes vary across regions

### Predictive Analytics

Develop machine learning models to:

* Predict attraction ratings
* Predict visitor visit mode

### Recommendation

Recommend attractions using:

* Historical visitor-attraction interactions
* Attraction type
* Geographic characteristics

This creates a complete workflow from historical tourism data to actionable recommendations.

---

# 5. Data Science Pipeline

## 5.1 Data Collection & Understanding

The project began with multiple related tourism datasets.

The primary datasets included:

* Country
* Region
* Continent
* City
* User
* Transaction
* Item
* Updated Item
* Type
* Mode

The first step was to understand the role of each table and identify the keys connecting them.

The main relationships were based on identifiers such as:

* UserId
* AttractionId
* CityId
* CountryId
* RegionId
* ContinentId
* AttractionTypeId
* VisitModeId

This relationship analysis was important because the final analytical dataset was created by integrating information from multiple source tables.

---

## 5.2 Data Quality Assessment

Before cleaning and merging the data, quality checks were performed on each dataset.

The following checks were performed:

### Duplicate Check

Duplicate records were checked across the source tables.

No exact duplicate records were identified in the datasets used for the project.

### Missing Value Analysis

Missing values were examined in important fields.

Some users had missing `CityId` values. These records were retained because their other geographic information was available and their transactions remained valid.

A missing city name was also identified for one city record.

### Referential Integrity

Foreign-key relationships were validated between the tables.

Examples included:

```text
Transaction → User
Transaction → Item
Transaction → Updated_Item
User → City
City → Country
Country → Region
Region → Continent
```

The checks confirmed that the transaction records did not contain invalid user or attraction references.

### Data Type Validation

Column data types were inspected to identify inconsistencies.

One example was the difference in data type between `Updated_Item.AttractionTypeId` and the corresponding type identifier in the reference table.

These inconsistencies were corrected during the cleaning stage.

### Placeholder Values

Placeholder values such as `-` were identified in reference datasets and handled appropriately during data preparation.

---

# 5.3 Data Cleaning & Integration

After the quality assessment, the source tables were cleaned and integrated.

The main steps were:

1. Standardize column names and data types.
2. Check duplicate records.
3. Investigate missing values.
4. Validate primary and foreign-key relationships.
5. Handle placeholder values.
6. Resolve data-type inconsistencies.
7. Merge the related datasets.
8. Validate the resulting dataset.

The final cleaned dataset contains:

```text
52,930 rows
22 columns
```

The cleaned dataset was saved as:

```text
data/cleaned_data.csv
```

A separate documentation file was created to record the cleaning decisions:

```text
docs/cleaning_notes.md
```

---

# 5.4 Exploratory Data Analysis

EDA was performed after the data cleaning stage.

The purpose was to understand visitor behavior, geographic distribution, attraction popularity, ratings, and visit-mode patterns before developing machine learning models.

The analysis included:

* User geographic distribution
* Country-level activity
* Region-level activity
* City-level activity
* Attraction popularity
* Attraction type distribution
* Rating distribution
* Visit mode distribution
* Visit Mode vs Region analysis
* Numeric correlation analysis

### User and Geographic Analysis

Geographic distributions were analyzed at country, region, and city levels.

**Why:**
Geographic analysis helps identify the major tourism markets represented in the data and provides context for location-based recommendation.

### Attraction Popularity

Attractions were ranked according to transaction volume.

**Why:**
This identifies frequently visited attractions and provides a measure of attraction popularity.

### Attraction Type Analysis

Attractions were grouped by type.

**Why:**
Attraction type is an important content feature and was later used in the recommendation system.

### Rating Distribution

Ratings were analyzed across the available 1–5 rating scale.

**Why:**
Understanding the distribution of ratings is important because `Rating` was later used as the regression target.

### Visit Mode Distribution

Visit modes were analyzed across the dataset.

The available categories included:

* Business
* Couples
* Family
* Friends
* Solo

**Why:**
Visit mode became the target variable for the classification problem.

### Visit Mode vs Region

A heatmap was used to compare visit modes across regions.

**Why:**
The heatmap makes it easier to identify combinations where particular visitor segments are concentrated.

### Numeric Correlation

A correlation heatmap was used for numerical variables.

**Why:**
Correlation analysis helps identify relationships between numerical variables and supports feature selection and feature engineering decisions.

The EDA findings were documented separately in:

```text
docs/insights.md
```

---

# 5.5 Feature Engineering

Feature engineering was performed to transform the cleaned tourism data into datasets suitable for machine learning.

Two types of aggregate features were created.

## User-Level Features

### UserVisitCount

Number of recorded visits made by a user.

**Purpose:**
Provides an indication of visitor activity and experience.

### UserAverageRating

Average rating given by a user.

**Purpose:**
Provides information about a user's historical rating behavior.

### UserMostCommonVisitMode

Most frequently recorded visit mode for a user.

**Purpose:**
Provides information about the user's historical travel behavior.

---

## Attraction-Level Features

### AttractionVisitCount

Number of recorded visits for an attraction.

**Purpose:**
Provides a measure of attraction popularity.

### AttractionAverageRating

Average historical rating received by an attraction.

**Purpose:**
Provides a measure of historical visitor perception.

---

## Target Leakage Prevention

Target leakage was specifically considered when constructing the modeling datasets.

For the **rating regression model**, the target is:

```text
Rating
```

Therefore, features directly derived from the rating target were excluded:

```text
UserAverageRating
AttractionAverageRating
```

For the **visit mode classification model**, the target is:

```text
VisitMode
```

Therefore:

```text
UserMostCommonVisitMode
```

was excluded from the classification predictors.

Safe behavioral aggregates such as:

```text
UserVisitCount
AttractionVisitCount
```

were retained.

This prevents information from the target variable from being unintentionally passed into the model.

---

## Categorical Feature Encoding

Categorical variables were transformed into numerical representations suitable for machine learning.

High-cardinality geographic variables such as:

```text
CityName
Country
```

were handled using frequency encoding rather than creating a large number of one-hot columns.

Lower-cardinality categorical variables were encoded using one-hot encoding.

This approach reduced memory usage while preserving useful categorical information.

---

## Model Datasets

Two modeling datasets were created:

```text
data/model_data_regression.csv
data/model_data_classification.csv
```

The regression dataset was prepared for rating prediction.

The classification dataset was prepared for visit-mode prediction.

---

# 5.6 Regression Modeling

The regression task predicts the visitor rating associated with an attraction.

### Target

```text
Rating
```

### Models Evaluated

The following models were considered:

1. Linear Regression
2. Random Forest Regressor
3. XGBoost Regressor

The models were evaluated using:

* R²
* Mean Squared Error
* Root Mean Squared Error

### R²

R² measures how much of the variation in the target variable is explained by the model.

Higher values are generally preferred.

### MSE

Mean Squared Error measures the average squared prediction error.

Lower values are preferred.

### RMSE

Root Mean Squared Error converts the error back to the scale of the target variable, making it easier to interpret.

Lower values are preferred.

A model comparison table was generated and saved as:

```text
data/regression_model_comparison.csv
```

The selected regression model was saved as:

```text
models/regression_model.pkl
```

The final model was selected based on the overall regression performance rather than relying on a single metric.

---

# 5.7 Classification Modeling

The classification task predicts the visitor's visit mode.

### Target

```text
VisitMode
```

The classes are:

```text
Business
Couples
Family
Friends
Solo
```

### Models Evaluated

Three models were evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. XGBoost Classifier

### Evaluation Metrics

The models were evaluated using:

* Accuracy
* Macro Precision
* Macro Recall
* Macro F1 Score

Macro averaging was used because the classification problem contains multiple visitor segments and each class should contribute equally to the evaluation.

### XGBoost Label Encoding

XGBoost requires numerical class labels for multiclass classification.

Therefore, `LabelEncoder` was used to convert the visit-mode labels into numerical values during training.

The predictions were converted back to the original visit-mode labels before evaluation.

This keeps the application output understandable:

```text
Business
Couples
Family
Friends
Solo
```

rather than displaying numerical class identifiers.

### Model Comparison

The classification models were compared using the generated evaluation metrics.

The comparison was saved as:

```text
data/classification_model_comparison.csv
```

The classification report was saved as:

```text
data/classification_report.txt
```

A confusion matrix was also generated to examine class-level prediction performance.

The selected classification model was saved as:

```text
models/classification_model.pkl
```

---

# 5.8 Recommendation System

A recommendation system was developed to suggest attractions based on historical visitor behavior and attraction characteristics.

Two approaches were implemented.

---

## 5.8.1 Item-Based Collaborative Filtering

A user-attraction rating matrix was created.

```text
Rows    → Users
Columns → Attractions
Values  → Average Rating
```

The resulting matrix contains:

```text
33,530 users × 30 attractions
```

Cosine similarity was then calculated between attractions.

The approach works on the principle that attractions receiving similar ratings from similar users may be relevant to one another.

### Recommendation Process

```text
User ID
   ↓
Historical ratings
   ↓
Attractions rated by user
   ↓
Similar attractions
   ↓
Weighted recommendation score
   ↓
Ranked attractions
```

Already-rated attractions are removed from the final recommendation list.

The recommendation system therefore focuses on attractions that the user has not previously rated.

---

## 5.8.2 Content-Based Filtering

A complementary content-based approach was developed using attraction metadata.

The content information included:

* Attraction Type
* City
* Country
* Region
* Continent

The metadata was combined into a textual representation and transformed using TF-IDF.

Cosine similarity was then used to identify attractions with similar characteristics.

This provides a fallback/complementary recommendation approach when historical user interaction is limited.

---

## Recommendation Function

The final recommendation workflow is exposed through:

```python
recommend(user_id, n=5)
```

The function returns ranked attractions together with their recommendation scores and relevant attraction information.

The recommendation artifacts were saved as:

```text
models/recommendation_system.pkl
```

---

# 5.9 Model & Artifact Saving

The important project artifacts were saved separately so that the Streamlit application can load them without retraining the models.

### Datasets

```text
data/cleaned_data.csv
data/model_data_regression.csv
data/model_data_classification.csv
```

### Models

```text
models/regression_model.pkl
models/classification_model.pkl
models/recommendation_system.pkl
```

### Documentation

```text
docs/cleaning_notes.md
docs/insights.md
docs/regression_modeling_notes.md
docs/classification_modeling_notes.md
```

This separation allows the application layer to remain independent from the model training notebooks.

---

# 6. Streamlit Application

A Streamlit application was developed to provide an interactive interface for the project.

The application is organized into separate pages to keep the user interface simple and maintainable.

## Application Pages

### Home

Provides:

* Project overview
* Dataset statistics
* Project objectives
* Navigation to the main modules

### Recommendations

Provides:

* User selection/input
* Number of recommendations
* Ranked attraction recommendations
* Attraction details

### Predictions

Provides access to the machine learning prediction functionality.

The application uses the trained:

```text
Classification Model
Regression Model
```

to generate predictions without retraining the models.

### Analytics

Provides interactive visualizations based on the tourism dataset.

The analytics page focuses on important tourism measures such as:

* Popular attractions
* Regional tourism activity
* Other selected EDA results

---

# 7. Business Insights

The project provides several areas of business value.

### Tourism Market Analysis

Country, region, and city-level analysis helps identify important tourism markets and destinations.

### Attraction Demand

Transaction volume provides a useful indicator of attraction popularity.

This can support:

* Destination promotion
* Capacity planning
* Marketing prioritization

### Visitor Segmentation

Visit mode classification provides a way to categorize visitors into groups such as:

* Business
* Couples
* Family
* Friends
* Solo

These segments can support more targeted recommendations.

### Personalized Recommendations

The recommendation system can help visitors discover attractions based on historical interaction patterns and attraction characteristics.

### Rating Analysis

Rating prediction provides a machine learning approach for estimating visitor ratings based on available visitor, attraction, and geographic information.

---

# 8. Model Evaluation

Model performance is documented separately for the two supervised learning tasks.

## Regression

Evaluation metrics:

```text
R²
MSE
RMSE
```

The complete comparison is available in:

```text
data/regression_model_comparison.csv
```

## Classification

Evaluation metrics:

```text
Accuracy
Macro Precision
Macro Recall
Macro F1
```

The complete comparison is available in:

```text
data/classification_model_comparison.csv
```

This separation makes it possible to compare the evaluated models and justify the selected model.

---

# 9. Technology Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost

### Recommendation System

* Cosine Similarity
* TF-IDF
* Collaborative Filtering
* Content-Based Filtering

### Application

* Streamlit

### Model Persistence

* Joblib

### Development

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# 10. Project Structure

```text
tourism-analytics/
│
├── app/
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── 1_Recommendations.py
│   │   ├── 2_Predictions.py
│   │   └── 3_Analytics.py
│   │
│   └── utils/
│       ├── data_loader.py
│       ├── recommendation.py
│       └── prediction.py
│
├── data/
│   ├── cleaned_data.csv
│   ├── model_data_regression.csv
│   └── model_data_classification.csv
│
├── models/
│   ├── regression_model.pkl
│   ├── classification_model.pkl
│   └── recommendation_system.pkl
│
├── notebooks/
│   ├── cleaning.ipynb
│   ├── eda.ipynb
│   ├── feature_engineering.ipynb
│   ├── regression_modeling.ipynb
│   ├── classification_modeling.ipynb
│   └── recommendation_system.ipynb
│
├── charts/
│   └── generated_visualizations
│
├── docs/
│   ├── cleaning_notes.md
│   ├── insights.md
│   ├── regression_modeling_notes.md
│   └── classification_modeling_notes.md
│
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 11. How to Run Locally

Clone the repository:

```bash
git clone <GITHUB_REPOSITORY_URL>
```

Move into the project:

```bash
cd tourism-analytics
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Streamlit application:

```bash
streamlit run app/app.py
```

The application will then be available through the local Streamlit URL displayed in the terminal.

---

12. Deployment

The Streamlit application can be deployed using Streamlit Community Cloud.

Deployment workflow:

Local Project
     │
     ▼
Git Repository
     │
     ▼
GitHub
     │
     ▼
Streamlit Community Cloud
     │
     ▼
Public Application URL

The deployed application link will be added here after deployment:

Live Demo:
https://tourism-analytics-recommendation-system.streamlit.app/

The source repository will be available at:

GitHub:
https://github.com/kusumasutar/tourism-analytics-recommendation-system/

# 14. Future Improvements

The current system provides a functional foundation for tourism analytics and recommendations. Possible improvements include:

* Introduce a hybrid recommendation model combining collaborative and content-based scores more systematically.
* Add cold-start handling for completely new users.
* Incorporate additional attraction metadata.
* Add time-based visitor behavior features.
* Improve model validation using cross-validation.
* Add model explainability using SHAP or similar techniques.
* Monitor recommendation quality using recommendation-specific metrics.
* Add database integration instead of loading static CSV files.
* Add authentication and user profiles to the deployed application.
* Introduce model retraining pipelines as new tourism data becomes available.

---

# 15. Conclusion

This project demonstrates an end-to-end data science workflow using real-world tourism data.

The workflow progresses from:

```text
Raw Data
   ↓
Data Validation
   ↓
Data Cleaning
   ↓
EDA
   ↓
Feature Engineering
   ↓
Machine Learning
   ↓
Recommendation System
   ↓
Streamlit Application
   ↓
Deployment
```

The project combines descriptive analytics, predictive modeling, and recommendation techniques within a single application.

The final system provides a practical foundation for understanding tourism behavior, predicting visitor-related outcomes, and supporting attraction discovery through personalized recommendations.
