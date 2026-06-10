# Global Variable
total_candidates = 0

candidates = []

# Function: Add Candidate
def add_candidate(name, age, qualification, score):

    global total_candidates

    candidate = {
        "Name": name,
        "Age": age,
        "Qualification": qualification,
        "Score": score
    }

    candidates.append(candidate)
    total_candidates += 1

    return "Candidate Registered Successfully"


# Function: Eligibility Check
def check_eligibility(score):

    if score >= 70:
        return "Eligible"

    return "Not Eligible"


# Lambda Function: Salary Prediction
salary_predictor = lambda score: 300000 + (score * 1000)


# Function: Display Candidates
def display_candidates():

    if len(candidates) == 0:
        print("No Candidates Found")
        return

    for candidate in candidates:

        status = check_eligibility(candidate["Score"])

        predicted_salary = salary_predictor(
            candidate["Score"]
        )

        print("-" * 50)
        print("Name :", candidate["Name"])
        print("Age :", candidate["Age"])
        print("Qualification :", candidate["Qualification"])
        print("Score :", candidate["Score"])
        print("Status :", status)
        print("Expected Salary :", predicted_salary)


# Recursion: Search Candidate
def search_candidate(index, name):

    if index >= len(candidates):
        return "Candidate Not Found"

    if candidates[index]["Name"].lower() == name.lower():
        return candidates[index]

    return search_candidate(index + 1, name)


# Main Program
while True:

    print("\n===== CYBERYAAN HIRING SYSTEM =====")
    print("1. Register Candidate")
    print("2. View Candidates")
    print("3. Search Candidate")
    print("4. Total Candidates")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        qualification = input("Enter Qualification: ")
        score = int(input("Enter Technical Test Score: "))

        print(
            add_candidate(
                name,
                age,
                qualification,
                score
            )
        )

    elif choice == "2":

        display_candidates()

    elif choice == "3":

        search_name = input("Enter Candidate Name: ")

        result = search_candidate(
            0,
            search_name
        )

        print(result)

    elif choice == "4":

        print("Total Candidates :", total_candidates)

    elif choice == "5":

        print("Thank You")
        break

    else:
        print("Invalid Choice")