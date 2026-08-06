
faculty_list = [
    {"faculty_id": "F101", "name": "Dr. Ramesh Iyer", "department": "CSE",
     "publications": 25, "h_index": 12, "budget_requested": 150000, "collab_score": 8},

    {"faculty_id": "F102", "name": "Dr. Anita Rao", "department": "ECE",
     "publications": 18, "h_index": 9, "budget_requested": 90000, "collab_score": 7},

    {"faculty_id": "F103", "name": "Dr. Suresh Kumar", "department": "CSE",
     "publications": 30, "h_index": 15, "budget_requested": 200000, "collab_score": 9},

    {"faculty_id": "F104", "name": "Dr. Priya Menon", "department": "Mechanical",
     "publications": 10, "h_index": 5, "budget_requested": -50000, "collab_score": 4}, 

    {"faculty_id": "F105", "name": "Dr. Vikram Shah", "department": "ECE",
     "publications": 22, "h_index": 10, "budget_requested": 120000, "collab_score": 6}, 
]
def is_budget_valid(budget):
    if isinstance(budget, (int, float)) and budget > 0:
        return True
    return False
def calculate_research_score(fac):
    score = (0.4 * fac["publications"]) + (0.3 * fac["h_index"]) + (0.3 * fac["collab_score"])
    return round(score, 2)
def allocate_grant(fac, score):
    if not is_budget_valid(fac["budget_requested"]):
        return 0  

    if score >= 8:
        percent = 1.0
    elif score >= 6:
        percent = 0.75
    elif score >= 4:
        percent = 0.5
    else:
        percent = 0.25

    return round(fac["budget_requested"] * percent, 2)


def main():
    print("=" * 60)
    print("UNIVERSITY RESEARCH GRANT ALLOCATION SYSTEM")
    print("=" * 60)
    for fac in faculty_list:
        fac["research_score"] = calculate_research_score(fac)
        fac["grant_allocated"] = allocate_grant(fac, fac["research_score"])

    print("\n--- Task 10: Invalid Budget Check ---")
    for fac in faculty_list:
        if not is_budget_valid(fac["budget_requested"]):
            print(f"WARNING: {fac['name']} ({fac['faculty_id']}) has an invalid budget "
                  f"value -> {fac['budget_requested']}. Grant set to 0.")

    print("\n--- Task 1: Research Scores ---")
    for fac in faculty_list:
        print(f"{fac['faculty_id']} - {fac['name']}: Score = {fac['research_score']}")

    print("\n--- Task 2: Grants Allocated ---")
    for fac in faculty_list:
        print(f"{fac['faculty_id']} - {fac['name']}: Grant = Rs.{fac['grant_allocated']}")

    print("\n--- Task 3: Faculty receiving grant above Rs.100000 ---")
    high_grant_faculty = [f for f in faculty_list if f["grant_allocated"] > 100000]
    if high_grant_faculty:
        for f in high_grant_faculty:
            print(f"{f['name']} ({f['department']}) -> Rs.{f['grant_allocated']}")
    else:
        print("No faculty crossed the 100000 mark this time.")

    print("\n--- Task 4: Department with Maximum Funding ---")
    dept_funding = {}
    for f in faculty_list:
        dept = f["department"]
        dept_funding[dept] = dept_funding.get(dept, 0) + f["grant_allocated"]

    top_dept = max(dept_funding, key=dept_funding.get)
    print(f"Department wise total funding: {dept_funding}")
    print(f"Top funded department: {top_dept} (Rs.{dept_funding[top_dept]})")

    print("\n--- Task 5: Faculty Ranking (by research score) ---")
    ranked_faculty = sorted(faculty_list, key=lambda x: x["research_score"], reverse=True)
    rank = 1
    for f in ranked_faculty:
        f["rank"] = rank
        print(f"Rank {rank}: {f['name']} - Score {f['research_score']}")
        rank += 1
    print("\n--- Task 6: Average Research Score ---")
    total_score = sum(f["research_score"] for f in faculty_list)
    avg_score = round(total_score / len(faculty_list), 2)
    print(f"Average Research Score = {avg_score}")

    print("\n--- Task 7: Top Performer ---")
    top_performer = ranked_faculty[0]
    print(f"{top_performer['name']} is the top performer with score {top_performer['research_score']}")

    print("\n--- Task 8: Saving Rankings to File ---")
    with open("grant_rankings.txt", "w") as f:
        f.write("FACULTY GRANT RANKINGS\n")
        f.write("-" * 40 + "\n")
        for fac in ranked_faculty:
            f.write(f"Rank {fac['rank']}: {fac['name']} ({fac['faculty_id']}) - "
                     f"Dept: {fac['department']} - Score: {fac['research_score']} - "
                     f"Grant: Rs.{fac['grant_allocated']}\n")
    print("Saved to grant_rankings.txt")

    
    print("\n--- Task 9: Reading Rankings from File ---")
    with open("grant_rankings.txt", "r") as f:
        content = f.read()
    print(content)


if __name__ == "__main__":
    main()