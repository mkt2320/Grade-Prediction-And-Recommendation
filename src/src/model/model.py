import pickle
import numpy as np
import shap

class RegressorModel:
    def __init__(self, columnList) -> None:
        try:
            # Load the pickle file
            with open('C:\\Users\\hp\\Downloads\\src\\src\\model\\lasso_all_features_best.pkl', 'rb') as file:
                self.model = pickle.load(file)
        except Exception as e:
            print(f"Model loading unsuccessful because of error {e}")
            exit(1)
    
        '''try:
            self.explainer = shap.KernelExplainer(self.model)
        except Exception as e:
            print(f"SHAP explainer load unsuccessful because of error {e}")
            exit(1)'''
            
        self.columnList = columnList
            
    def predict(self, input):
        print(type(input))
        print(self.columnList)
        print(np.array(input))
        self.out = self.model.predict(input)
        print("-- G3 score : ", self.out)
        return self.out[0]

    def getSHAPValues(self, input):
        # Convert input DataFrame to a numpy array
        input_array = input.values
        # Create a SHAP explainer instance with the predict method
        explainer = shap.Explainer(self.model, input_array)
        # Compute SHAP values
        shap_values = explainer.shap_values(input_array)
        # Create a dictionary mapping column names to SHAP values
        shap_dict = dict(zip(self.columnList, shap_values))
        return shap_dict