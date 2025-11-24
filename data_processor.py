import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

def load_and_split_data(test_size=0.2, random_state=42):
    print("\n--- 1. Data Processor: Starting ---")
    
    iris = load_iris()
    
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Data Loaded: {len(X)} total samples.")
    print(f"Split completed: Training set size: {len(X_train)} | Testing set size: {len(X_test)}")
    
    return X_train, X_test, y_train, y_test, iris.target_names

if __name__ == '__main__':
    X_train, X_test, y_train, y_test, names = load_and_split_data()
    print("\nData Processor successfully ran (Module 1 Test).")