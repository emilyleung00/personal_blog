from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field

class Education(BaseModel):
    institution: str
    degree: str
    field_of_study: str
    start_date: date
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    location: Optional[str] = None
    description: Optional[str] = None

class WorkExperience(BaseModel):
    company: str
    position: str
    start_date: date
    end_date: Optional[date] = None
    location: Optional[str] = None
    description: Optional[str] = None
    achievements: List[str] = Field(default_factory=list)
    technologies: List[str] = Field(default_factory=list)

class Project(BaseModel):
    name: str
    description: str
    start_date: date
    end_date: Optional[date] = None
    technologies: List[str] = Field(default_factory=list)
    url: Optional[str] = None
    role: Optional[str] = None

class Skill(BaseModel):
    name: str
    level: str
    category: str

class Certification(BaseModel):
    name: str
    issuer: str
    date_obtained: date
    expiration_date: Optional[date] = None
    credential_id: Optional[str] = None
    url: Optional[str] = None

class Language(BaseModel):
    name: str
    proficiency: str

class ContactInformation(BaseModel):
    email: str
    phone: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None

class CV(BaseModel):
    personal_info: ContactInformation
    summary: str 
    education: List[Education]
    work_experience: List[WorkExperience]
    projects: List[Project] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)
    certifications: List[Certification] = Field(default_factory=list)
    languages: List[Language] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list) 