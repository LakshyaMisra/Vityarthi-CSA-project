from data_processor import load_and_split_data
from model_trainer import train_model
from predictor import evaluate_model, make_single_prediction
import sys

def main():
    print("=================================================================")
    print("  🌸 Iris Species Classifier - Decision Tree Implementation  ")
    print("=================================================================")
    
    X_train, X_test, y_train, y_test, target_names = load_and_split_data()
    
    model = train_model(X_train, y_train)
    
    accuracy = evaluate_model(model, X_test, y_test)
    
    make_single_prediction(model, target_names)
    
    print("\n=================================================================")
    print("  Pipeline Complete. Successfully demonstrated modular design.  ")
    print("=================================================================")


if __name__ == "__main__":
    try:
        import pandas
        import sklearn
        import numpy
    except ImportError:
        print("ERROR: Missing required libraries (pandas, scikit-learn).")
        print("Please ensure you run: pip install -r requirements.txt")
        sys.exit(1)
        
    main()