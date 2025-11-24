from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd

def evaluate_model(model, X_test, y_test):
    print("\n--- 3. Predictor: Evaluation Starting ---")
    
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Evaluation Complete. Total Test Samples: {len(X_test)}")
    print(f"Model Accuracy Score: {accuracy:.4f} ({(accuracy * 100):.2f}%)")
    
    return accuracy

def make_single_prediction(model, target_names):
    print("\n--- 4. Prediction Service: Test a New Flower ---")
    
    try:
        sepal_l = float(input("Enter Sepal Length (cm): "))
        sepal_w = float(input("Enter Sepal Width (cm): "))
        petal_l = float(input("Enter Petal Length (cm): "))
        petal_w = float(input("Enter Petal Width (cm): "))
        
        new_data = pd.DataFrame([[sepal_l, sepal_w, petal_l, petal_w]],
                                columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
        
        prediction_index = model.predict(new_data)[0]
        predicted_species = target_names[prediction_index]
        
        print("\nPrediction Result:")
        print(f"Predicted Species: >>> {predicted_species} <<<")
        
    except ValueError:
        print("\nError: Invalid input. Please ensure all inputs are numbers.")