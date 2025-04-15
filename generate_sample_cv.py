from datetime import date, timedelta
import json
from cv_models import CV, ContactInformation, Education, WorkExperience, Project, Skill, Certification, Language

def generate_sample_cv() -> CV:
    """Generate a sample CV for a Data Scientist."""
    
    # Calculate dates
    today = date.today()
    five_years_ago = today - timedelta(days=5*365)
    three_years_ago = today - timedelta(days=3*365)
    one_year_ago = today - timedelta(days=365)
    
    # Create CV object
    cv = CV(
        personal_info=ContactInformation(
            email="sarah.smith@example.com",
            phone="+1 (555) 987-6543",
            location="New York, NY",
            website="https://sarahsmith.ai",
            linkedin="https://linkedin.com/in/sarahsmith",
            github="https://github.com/sarahsmith"
        ),
        summary="Senior Data Scientist with 5 years of experience in machine learning and data analysis. "
               "Expert in Python, TensorFlow, and big data technologies. "
               "Proven track record of developing and deploying ML models in production environments.",
        education=[
            Education(
                institution="Massachusetts Institute of Technology",
                degree="Master of Science",
                field_of_study="Data Science",
                start_date=date(2015, 9, 1),
                end_date=date(2017, 6, 1),
                gpa=3.9,
                location="Cambridge, MA",
                description="Specialized in Machine Learning and Big Data Analytics"
            ),
            Education(
                institution="University of California, Los Angeles",
                degree="Bachelor of Science",
                field_of_study="Computer Science",
                start_date=date(2011, 9, 1),
                end_date=date(2015, 6, 1),
                gpa=3.8,
                location="Los Angeles, CA"
            )
        ],
        work_experience=[
            WorkExperience(
                company="AI Solutions Inc.",
                position="Senior Data Scientist",
                start_date=three_years_ago,
                end_date=None,
                location="New York, NY",
                description="Leading the machine learning team in developing AI solutions for enterprise clients",
                achievements=[
                    "Developed a recommendation system that increased user engagement by 45%",
                    "Implemented automated ML pipeline reducing model deployment time by 70%",
                    "Mentored 3 junior data scientists and improved team productivity"
                ],
                technologies=[
                    "Python",
                    "TensorFlow",
                    "PyTorch",
                    "Spark",
                    "AWS",
                    "Docker",
                    "Kubernetes"
                ]
            ),
            WorkExperience(
                company="Data Analytics Corp",
                position="Data Scientist",
                start_date=five_years_ago,
                end_date=three_years_ago,
                location="Boston, MA",
                description="Worked on predictive analytics and machine learning projects",
                achievements=[
                    "Built a fraud detection system with 95% accuracy",
                    "Developed a customer segmentation model improving marketing ROI by 30%"
                ],
                technologies=[
                    "Python",
                    "Scikit-learn",
                    "Pandas",
                    "NumPy",
                    "SQL",
                    "Tableau"
                ]
            )
        ],
        projects=[
            Project(
                name="Real-time Anomaly Detection System",
                description="Developed a real-time anomaly detection system for financial transactions using deep learning",
                start_date=one_year_ago,
                end_date=None,
                technologies=[
                    "Python",
                    "TensorFlow",
                    "Kafka",
                    "Docker",
                    "AWS"
                ],
                url="https://github.com/sarahsmith/anomaly-detection",
                role="Lead Developer"
            ),
            Project(
                name="Natural Language Processing for Customer Support",
                description="Built an NLP system to automatically categorize and route customer support tickets",
                start_date=date(2022, 1, 1),
                end_date=date(2022, 6, 1),
                technologies=[
                    "Python",
                    "BERT",
                    "FastAPI",
                    "Docker"
                ],
                url="https://github.com/sarahsmith/nlp-support",
                role="Data Scientist"
            )
        ],
        skills=[
            Skill(name="Python", level="Expert", category="Programming Languages"),
            Skill(name="R", level="Advanced", category="Programming Languages"),
            Skill(name="TensorFlow", level="Expert", category="Machine Learning"),
            Skill(name="PyTorch", level="Expert", category="Machine Learning"),
            Skill(name="Scikit-learn", level="Expert", category="Machine Learning"),
            Skill(name="Spark", level="Advanced", category="Big Data"),
            Skill(name="AWS", level="Advanced", category="Cloud"),
            Skill(name="SQL", level="Expert", category="Database")
        ],
        certifications=[
            Certification(
                name="TensorFlow Developer Certificate",
                issuer="Google",
                date_obtained=date(2021, 3, 15),
                expiration_date=date(2024, 3, 15),
                credential_id="TF-123456"
            ),
            Certification(
                name="AWS Certified Machine Learning - Specialty",
                issuer="Amazon Web Services",
                date_obtained=date(2020, 6, 1),
                expiration_date=date(2023, 6, 1),
                credential_id="AWS-ML-789012"
            )
        ],
        languages=[
            Language(name="English", proficiency="Native"),
            Language(name="French", proficiency="Professional")
        ],
        interests=[
            "Machine Learning Research",
            "Open Source Contribution",
            "Data Visualization",
            "Hiking"
        ]
    )
    
    return cv

def save_cv_to_json(cv: CV, file_path: str) -> None:
    """Save CV object to JSON file."""
    # Convert CV to dictionary
    cv_dict = cv.model_dump()
    
    # Convert date objects to ISO format strings
    for education in cv_dict['education']:
        education['start_date'] = education['start_date'].isoformat()
        if education['end_date']:
            education['end_date'] = education['end_date'].isoformat()
    
    for work in cv_dict['work_experience']:
        work['start_date'] = work['start_date'].isoformat()
        if work['end_date']:
            work['end_date'] = work['end_date'].isoformat()
    
    for project in cv_dict['projects']:
        project['start_date'] = project['start_date'].isoformat()
        if project['end_date']:
            project['end_date'] = project['end_date'].isoformat()
    
    for cert in cv_dict['certifications']:
        cert['date_obtained'] = cert['date_obtained'].isoformat()
        if cert.get('expiration_date'):
            cert['expiration_date'] = cert['expiration_date'].isoformat()
    
    # Save to JSON file
    with open(file_path, 'w') as f:
        json.dump(cv_dict, f, indent=4)

def main():
    try:
        # Generate sample CV
        cv = generate_sample_cv()
        
        # Save to JSON file
        save_cv_to_json(cv, 'data_scientist_cv.json')
        print("Sample CV generated and saved to 'data_scientist_cv.json'")
        
        # Print summary
        from create_cv import print_cv_summary
        print_cv_summary(cv)
        
    except Exception as e:
        print(f"Error generating CV: {str(e)}")

if __name__ == "__main__":
    main() 