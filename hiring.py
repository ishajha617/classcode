# # Global Variable
# total_candidates = 0

# candidates = []

# # Function: Add Candidate
# def add_candidate(name, age, qualification, score):

#     global total_candidates

#     candidate = {
#         "Name": name,
#         "Age": age,
#         "Qualification": qualification,
#         "Score": score
#     }

#     candidates.append(candidate)
#     total_candidates += 1

#     return "Candidate Registered Successfully"


# # Function: Eligibility Check
# def check_eligibility(score):

#     if score >= 70:
#         return "Eligible"

#     return "Not Eligible"


# # Lambda Function: Salary Prediction
# salary_predictor = lambda score: 300000 + (score * 1000)


# # Function: Display Candidates
# def display_candidates():

#     if len(candidates) == 0:
#         print("No Candidates Found")
#         return

#     for candidate in candidates:

#         status = check_eligibility(candidate["Score"])

#         predicted_salary = salary_predictor(
#             candidate["Score"]
#         )

#         print("-" * 50)
#         print("Name :", candidate["Name"])
#         print("Age :", candidate["Age"])
#         print("Qualification :", candidate["Qualification"])
#         print("Score :", candidate["Score"])
#         print("Status :", status)
#         print("Expected Salary :", predicted_salary)


# # Recursion: Search Candidate
# def search_candidate(index, name):

#     if index >= len(candidates):
#         return "Candidate Not Found"

#     if candidates[index]["Name"].lower() == name.lower():
#         return candidates[index]

#     return search_candidate(index + 1, name)


# # Main Program
# while True:

#     print("\n===== CYBERYAAN HIRING SYSTEM =====")
#     print("1. Register Candidate")
#     print("2. View Candidates")
#     print("3. Search Candidate")
#     print("4. Total Candidates")
#     print("5. Exit")

#     choice = input("Enter Choice: ")

#     if choice == "1":

#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         qualification = input("Enter Qualification: ")
#         score = int(input("Enter Technical Test Score: "))

#         print(
#             add_candidate(
#                 name,
#                 age,
#                 qualification,
#                 score
#             )
#         )

#     elif choice == "2":

#         display_candidates()

#     elif choice == "3":

#         search_name = input("Enter Candidate Name: ")

#         result = search_candidate(
#             0,
#             search_name
#         )

#         print(result)

#     elif choice == "4":

#         print("Total Candidates :", total_candidates)

#     elif choice == "5":

#         print("Thank You")
#         break

#     else:
#         print("Invalid Choice")



import streamlit as st
import pandas as pd

# Session State
if "candidates" not in st.session_state:
    st.session_state.candidates = []

st.title("🚀 Cyberyaan Hiring System")

# Functions
def check_eligibility(score):
    if score >= 70:
        return "Eligible"
    return "Not Eligible"

salary_predictor = lambda score: 300000 + (score * 1000)

def search_candidate(name):
    for candidate in st.session_state.candidates:
        if candidate["Name"].lower() == name.lower():
            return candidate
    return None

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Register Candidate",
        "View Candidates",
        "Search Candidate",
        "Total Candidates"
    ]
)

# Register Candidate
if menu == "Register Candidate":

    st.subheader("Candidate Registration")

    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=18, max_value=100)
    qualification = st.text_input("Enter Qualification")
    score = st.number_input(
        "Technical Test Score",
        min_value=0,
        max_value=100
    )

    if st.button("Register"):

        candidate = {
            "Name": name,
            "Age": age,
            "Qualification": qualification,
            "Score": score
        }

        st.session_state.candidates.append(candidate)

        st.success("Candidate Registered Successfully")

# View Candidates
elif menu == "View Candidates":

    st.subheader("Candidate Records")

    if len(st.session_state.candidates) == 0:
        st.warning("No Candidates Found")

    else:

        records = []

        for candidate in st.session_state.candidates:

            records.append({
                "Name": candidate["Name"],
                "Age": candidate["Age"],
                "Qualification": candidate["Qualification"],
                "Score": candidate["Score"],
                "Status": check_eligibility(
                    candidate["Score"]
                ),
                "Expected Salary":
                salary_predictor(
                    candidate["Score"]
                )
            })

        st.dataframe(pd.DataFrame(records))

# Search Candidate
elif menu == "Search Candidate":

    st.subheader("Search Candidate")

    search_name = st.text_input("Enter Candidate Name")

    if st.button("Search"):

        result = search_candidate(search_name)

        if result:

            st.success("Candidate Found")

            st.json(result)

        else:

            st.error("Candidate Not Found")

# Total Candidates
elif menu == "Total Candidates":

    st.metric(
        "Total Candidates",
        len(st.session_state.candidates)
    )