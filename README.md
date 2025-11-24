# 🌸 Iris Species Classifier (Decision Tree Model)

## 🎯 Project Overview
This project implements a complete, modular Machine Learning pipeline using Python to solve a classification problem. The goal is to accurately predict the species of an Iris flower (**Setosa, Versicolor, or Virginica**) based on its physical measurements.

The system is built using three distinct modules: Data Preprocessing, Model Training, and Evaluation, demonstrating a clean, scalable architectural design.

## ✨ Key Features
* **Modular Architecture:** Logic separated into three distinct Python files (`data_processor.py`, `model_trainer.py`, `predictor.py`).
* **Classification:** Utilizes the simple and highly interpretable **Decision Tree Classifier**.
* **Data Handling:** Implements a standard **80/20 Train-Test Split** to ensure unbiased model evaluation.
* **Performance Reporting:** Calculates and reports the model's **Accuracy Score** on unseen test data.
* **Interactive Prediction:** Allows the user to input new measurements to receive a real-time prediction.

## 🛠️ Technologies & Tools Used
* **Language:** Python 3.x
* **Libraries:** Pandas, Scikit-learn (sklearn), NumPy
* **Model:** Decision Tree Classifier

## 🚀 Setup & Run Instructions

### A. Repository Location
The source code for this project is hosted on GitHub at the following location:
`https://github.com/LakshyaMisra/Vityarthi-CSA-project`

### B. Installation
1.  **Clone the Repository:** Use the following command to download the code to your local machine:
    ```bash
    git clone https://github.com/LakshyaMisra/Vityarthi-CSA-project
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd [installation folder]
    ```
3.  **Install the Libraries:** Install the required Python libraries using the `requirements.txt` file:
    ```bash
    python -m pip install -r requirements.txt
    ```

### C. Execution
Run the main script to start the full ML pipeline:
```bash
python main.py
