import json
from datetime import date
from cv_models import CV, ContactInformation, Education, WorkExperience, Project, Skill, Certification, Language

def load_cv_from_json(file_path: str) -> CV:
    """Load and validate CV data from a JSON file."""
    with open(file_path, 'r') as f:
        cv_data = json.load(f)
    
    # Convert string dates to date objects
    for education in cv_data['education']:
        education['start_date'] = date.fromisoformat(education['start_date'])
        if education['end_date']:
            education['end_date'] = date.fromisoformat(education['end_date'])
    
    for work in cv_data['work_experience']:
        work['start_date'] = date.fromisoformat(work['start_date'])
        if work['end_date']:
            work['end_date'] = date.fromisoformat(work['end_date'])
    
    for project in cv_data['projects']:
        project['start_date'] = date.fromisoformat(project['start_date'])
        if project['end_date']:
            project['end_date'] = date.fromisoformat(project['end_date'])
    
    for cert in cv_data['certifications']:
        cert['date_obtained'] = date.fromisoformat(cert['date_obtained'])
        if cert.get('expiration_date'):
            cert['expiration_date'] = date.fromisoformat(cert['expiration_date'])
    
    # Create and validate CV object
    cv = CV(**cv_data)
    return cv

def print_cv_summary(cv: CV) -> None:
    """Print a summary of the CV."""
    print("\n=== CV Summary ===")
    print(f"\nName: {cv.personal_info.email.split('@')[0].replace('.', ' ').title()}")
    print(f"Location: {cv.personal_info.location}")
    print(f"LinkedIn: {cv.personal_info.linkedin}")
    print(f"GitHub: {cv.personal_info.github}")
    
    print("\n=== Professional Summary ===")
    print(cv.summary)
    
    print("\n=== Education ===")
    for edu in cv.education:
        print(f"\n{edu.degree} in {edu.field_of_study}")
        print(f"{edu.institution} ({edu.start_date.year}-{edu.end_date.year if edu.end_date else 'Present'})")
        if edu.gpa:
            print(f"GPA: {edu.gpa}")
    
    print("\n=== Work Experience ===")
    for work in cv.work_experience:
        print(f"\n{work.position} at {work.company}")
        print(f"{work.start_date.year}-{work.end_date.year if work.end_date else 'Present'}")
        print("Key Technologies:", ", ".join(work.technologies))
    
    print("\n=== Skills ===")
    skills_by_category = {}
    for skill in cv.skills:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(f"{skill.name} ({skill.level})")
    
    for category, skills in skills_by_category.items():
        print(f"\n{category}:")
        print(", ".join(skills))

def main():
    try:
        cv = load_cv_from_json('sample_cv.json')
        print_cv_summary(cv)
    except Exception as e:
        print(f"Error loading CV: {str(e)}")

if __name__ == "__main__":
    main() 