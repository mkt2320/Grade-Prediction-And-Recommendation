import streamlit as st
from model.model import RegressorModel
from genai import GeminiPro
import pandas as pd

# Load the image
# st.image("src/std.webp", caption='Optional caption')

# Load dataset and model
test_dataset = pd.read_csv("C:/Users/hp/Downloads/src/src/test_dataset.csv")
columnList = ['age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel',
           'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2',
           'school_MS', 'sex_M', 'address_U', 'famsize_LE3', 'Pstatus_T',
           'Mjob_health', 'Mjob_other', 'Mjob_services', 'Mjob_teacher',
           'Fjob_health', 'Fjob_other', 'Fjob_services', 'Fjob_teacher',
           'reason_home', 'reason_other', 'reason_reputation', 'guardian_mother',
           'guardian_other', 'schoolsup_yes', 'famsup_yes', 'paid_yes',
           'activities_yes', 'nursery_yes', 'higher_yes', 'internet_yes',
           'romantic_yes']

print("Dataset loaded")
regressorModel = RegressorModel(columnList)
print("Model loaded")
geminiPro = GeminiPro()
print("Gemini pro loaded")

def main():
    st.title("Student Suggestion Generator")
    st.image("src/std.jpg")
    
    
    st.write("### Generate Suggestion")
        
        # Dropdown for selecting student ID
    student_id = st.selectbox("Select Student ID:", test_dataset['student_id'])

        # Button to trigger text generation
    if st.button("Generate Suggestion"):
        if not student_id:
                st.error("Please select a student ID.")
        else:
                input_data = test_dataset[test_dataset['student_id'] == student_id][columnList]
                with st.spinner("Generating suggestion..."):  # Show loading spinner
                    # Predict on the dataset
                    g3 = regressorModel.predict(input_data)
                    shap_dict = regressorModel.getSHAPValues(input_data)
                    
                    # Call function to generate text
                    suggested_text = geminiPro.getModelResponse(shap_dict, input_data, g3)
                
                st.subheader("Suggested Text:")
                st.write(suggested_text)
            
                st.image("src/tea.gif")
            
if __name__ == "__main__":
    main()
