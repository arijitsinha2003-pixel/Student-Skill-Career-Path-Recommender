
CAREERS = {
    "Web Developer": {
        "interests": ["web", "design", "frontend"],
        "skills": ["html", "css", "javascript", "react"],
        "learn": ["HTML/CSS", "JavaScript", "React", "APIs"]
    },
    "AI/ML Engineer": {
        "interests": ["ai", "math", "data", "research"],
        "skills": ["python", "statistics", "pandas", "ml"],
        "learn": ["Python", "Statistics", "Pandas", "ML"]
    },
    "Backend Developer": {
        "interests": ["logic", "servers", "database", "api"],
        "skills": ["python", "sql", "api", "git"],
        "learn": ["Python", "SQL", "REST APIs", "Databases"]
    },
    "Cybersecurity Analyst": {
        "interests": ["security", "network", "linux", "privacy"],
        "skills": ["linux", "networking", "python", "security"],
        "learn": ["Linux", "Networking", "Python", "Security labs"]
    },
    "Data Analyst": {
        "interests": ["data", "business", "math", "charts"],
        "skills": ["python", "sql", "excel", "visualization"],
        "learn": ["Python", "SQL", "Excel", "Data visualization"]
    }
}

def recommend_careers(interests, skills):
    results = []

    for career, info in CAREERS.items():
        interest_matches = set(interests) & set(info["interests"])
        skill_matches = set(skills) & set(info["skills"])

        score = (
            len(interest_matches) * 2
            + len(skill_matches)
        )

        results.append((
            score, career, interest_matches,
            skill_matches, info["learn"]
        ))

    return sorted(results, reverse=True, key=lambda x: x[0])

print("=== CAREER PATH RECOMMENDER ===")
print("Interests: web, design, ai, math, data,")
print("logic, database, security, network, etc.")
print("Skills: python, html, css, sql, git, etc.")

interests = input(
    "\nEnter interests separated by commas: "
).lower().replace(" ", "").split(",")

skills = input(
    "Enter current skills separated by commas: "
).lower().replace(" ", "").split(",")

results = recommend_careers(interests, skills)

print("\n=== YOUR TOP CAREER PATHS ===")

for rank, item in enumerate(results[:3], start=1):
    score, career, interest_matches, skill_matches, learn = item

    print(f"\n{rank}. {career}")
    print("Match points:", score)
    print("Matching interests:", ", ".join(
        sorted(interest_matches) or ["None yet"]
    ))
    print("Matching skills:", ", ".join(
        sorted(skill_matches) or ["None yet"]
    ))
    print("Suggested learning path:", " -> ".join(learn))

print("\nThese are heuristic suggestions, not")
print("scientifically validated career predictions.")
