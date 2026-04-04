SKILLS_DB = ["python", "java", "sql", "react", "spring", "django"]

def analyze_resume(text):
    text = text.lower()

    found_skills = [skill for skill in SKILLS_DB if skill in text]

    score = len(found_skills) * 20  # simple scoring

    return {
        "skills": ", ".join(found_skills),
        "score": score
    }