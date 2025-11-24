from sklearn.tree import DecisionTreeClassifier

def train_model(X_train, y_train, max_depth=3):
    print("\n--- 2. Model Trainer: Starting ---")
    
    dt_classifier = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    
    dt_classifier.fit(X_train, y_train)
    
    print(f"Decision Tree Model Trained Successfully (Max Depth: {max_depth}).")
    
    return dt_classifier

if __name__ == '__main__':
    print("This module is run via main.py to receive training data.")