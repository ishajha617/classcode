total_candidates = 0

candidates = []

def add_candidate(name, age, qualification, score):
    global total_canmdidates
    candidate = {
        "name": name,
        "age": age,
        "qualification": qualification,
        "score": score
    }

    candidates.append(candidate)
    total_candidates += 1

    return "candidates added successfully"
# eligibility check 
def check_eligibility(score):
    if score >= 85:
        return "eligible"
    return "not eligible"

#lambda function call

salary_predictor = lambda score: 300000 + (score * 1000)

# display all candidates 
def display_all(candidates):

    if len(candidates) == 0:
        print("no candidates found")
        return 
    for candidate in candidates:
        status = check_eligibility(candidate["score"])

        predicted_salary = salary_predictor(candidate["score"])

        print("-" * 50)
        print()