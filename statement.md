# Project Statement: Iris Species Classifier

## 1. Problem Statement
The primary problem addressed is the need for an efficient and automated method to categorize data points based on observed features. This project specifically tackles the **multi-class classification** challenge of identifying the species of an Iris flower from its four physical measurements (sepal length, sepal width, petal length, petal width). This acts as a foundation for understanding supervised machine learning techniques.

## 2. Scope of the Project
The project scope is limited to the essential functions of a classic Machine Learning pipeline:
* **In-Scope:** Data loading, **Train-Test Split (80/20)**, model instantiation using the **Decision Tree Classifier**, model training, and performance evaluation using the **Accuracy** metric.
* **Out-of-Scope:** Advanced model tuning (e.g., GridSearch), feature engineering, visualization of the decision tree itself, or deployment via a web framework.

## 3. Target Users
* **Students/Researchers:** To understand and implement fundamental classification algorithms.
* **Botanists/Scientists:** To quickly and automatically classify new samples in the field based on reliable data.

## 4. High-Level Features
1.  **Dedicated Data Processing Module:** Ensures data preparation is separated from model logic.
2.  **Simple Model Training:** Utilizes a highly **interpretable** model (Decision Tree).
3.  **Validation Engine:** Provides objective proof of performance via the **Accuracy Score** on unseen test data.
