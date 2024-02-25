import streamlit as st
from src.utils import get_gender_options, get_lunch_options, get_parental_level_of_education_options, get_race_ethnicity_options, get_test_preparation_course_options
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

def main():

    st.title('Student Performance App')

    gender = st.selectbox('Choose gender', get_gender_options())

    lunch = st.selectbox('Choose lunch', get_lunch_options())

    parental_level_of_education = st.selectbox('Choose parental level of education', get_parental_level_of_education_options())

    race_ethnicity = st.selectbox('Choose race ethnicity', get_race_ethnicity_options())

    test_preparation_course = st.selectbox('Choose test preparation course', get_test_preparation_course_options())

    reading_score = st.number_input('Enter reading score', value= 0)

    writing_score = st.number_input('Enter writing score', value= 0)

    data = CustomData(
        gender= gender,
        race_ethnicity= race_ethnicity,
        parental_level_of_education= parental_level_of_education,
        lunch= lunch,
        test_preparation_course= test_preparation_course,
        reading_score= reading_score,
        writing_score= writing_score
    )

    button = st.button(
        label= 'Predict Math score'
    )

    if button:

        pred_df=data.get_data_as_data_frame()

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)

        st.write(f'your math score is {results[0]}')




if __name__ == '__main__':

    main()