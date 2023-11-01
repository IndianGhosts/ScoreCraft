import streamlit as st


st.title("ScoreCraft")
st.subheader("This app was developed in hopes of helping students calculate their expected grades.")
st.write("A category is a section of the gradebook. Enter how many grading categories you have along with the weights of each one based on your syllabus.")
# A selection for the user to specify the number of rows
num_rows = st.slider('Number of Categories', min_value=1, max_value=20, value=1)


# Create an empty dictionary to store category and weight mappings
category_weights = {}


# Columns to lay out the inputs
grid = st.columns(2)


tolerance = 1e-10


def add_row(row):
    with grid[0]:
        category = st.text_input('Category', key=f'input_category{row}', help="Categories are the labels that the assignment is under, so like tests are weighted as Tests or Assessments")
    with grid[1]:
        weight = st.number_input('Weight (%)', key=f'input_weight{row}', help="Express this as a decimal (e.g., .2 is 20%)", min_value=0.0, max_value=1.00)
   
    if category and weight is not None:
        category_weights[category] = weight


for r in range(num_rows):
    add_row(r)


# Create a button to submit categories and center it
grid_for_button_one=st.columns(3)
with grid_for_button_one[1]:
    submitted_categories = st.button("Submit your Categories", help="Don't worry you can go back and change anything you need to")


# Display the selected category and its weight
if submitted_categories:


    total_weight = sum(category_weights.values())


    if abs(total_weight - 1.0) <= tolerance:
        st.write("The sum of these percentages is equal to 1.00 (100%).")
        st.write("Enter each grade and which category they are in. Note that you can enter tentative scores to see how they could affect your overall grade.")
    else:
        st.write("The sum of these percentages is not equal to 1.00 (100%). Please correct it.")


grid_two = st.columns(3)
def add_row_for_grades(row):
    with grid_two[0]:
        category = st.selectbox("Select the Category for the grade", list(category_weights.keys()), key=f'grade_category{row}')
    with grid_two[1]:
        grade_name = st.text_input("Grade Name", key=f"grade_name{row}")
    with grid_two[2]:
        grade = st.number_input('Grade', key=f'grade{row}', help="Enter your grade for this category", min_value=0, max_value=100)
       
        if category and grade is not None:
            # Set the grade as the user's input for that category
            st.session_state[f'grade{category}'] = grade


num_rows_two = st.slider('Number of Grades', min_value=0, max_value=200, value=1)
for r in range(num_rows_two):
    add_row_for_grades(r)


# Calculate the overall grade
def calculate_overall_grade():


  overall_grade = 0


  for category, weight in category_weights.items():
      grade = st.session_state.get(f'grade{category}')
      if grade is not None:
          overall_grade += grade * weight


  return overall_grade


# Center Button
grid_for_button_2=st.columns(3)
with grid_for_button_2[1]:
    calculate_grade_button = st.button("Calculate your overall grade")
# Display the overall grade
if calculate_grade_button:
    overall_grade = calculate_overall_grade()
    st.write(f'Overall Grade: {overall_grade:.2f}')
st.caption(" ")
st.caption(" ")
st.caption(" ")
st.caption(" ")
st.caption(" ")
st.caption(" ")
st.caption("For suggestions please email anay.ashish27@gmail.com (Created by Anay & Anya Ashish)")



