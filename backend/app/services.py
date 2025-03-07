from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

# Create a new project along with its subtasks
def create_project(db: Session, project: schemas.ProjectBase):
    db_project = models.Project(
        project_name=project.project_name,
        wo_number=project.wo_number,
        activity_code=project.activity_code,
        total_labor_amount=project.total_labor_amount,
        total_expenses_amount=project.total_expenses_amount,
        total_travel_amount=project.total_travel_amount,
        total_tier_fee=project.total_tier_fee,
        total_budget_amount=project.total_budget_amount,
    )
    db.add(db_project)
    db.flush()  # Get project ID without committing

    db_subtasks = [
        models.Subtask(
            subtask_name=subtask.subtask_name,
            labor_amount=subtask.labor_amount,
            expenses_amount=subtask.expenses_amount,
            travel_amount=subtask.travel_amount,
            tier_fee=subtask.tier_fee,
            budget_amount=subtask.budget_amount,
            project_id=db_project.id
        )
        for subtask in project.subtasks
    ]
    db.add_all(db_subtasks)

    db.commit()
    db.refresh(db_project)

    return db_project

# Get all projects (with optional pagination)
def get_projects(db: Session, limit: int = 100, offset: int = 0):
    return db.query(models.Project).offset(offset).limit(limit).all()

# Get a single project by ID
def get_project_by_id(db: Session, project_id: int):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# Delete a project and its subtasks
def delete_project(db: Session, project_id: int):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}

# Update a project's details
def update_project(db: Session, project_id: int, project_data: schemas.ProjectBase):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.project_name = project_data.project_name
    project.wo_number = project_data.wo_number
    project.activity_code = project_data.activity_code
    project.total_labor_amount = project_data.total_labor_amount
    project.total_expenses_amount = project_data.total_expenses_amount
    project.total_travel_amount = project_data.total_travel_amount
    project.total_tier_fee = project_data.total_tier_fee
    project.total_budget_amount = project_data.total_budget_amount

    db.commit()
    db.refresh(project)
    return project

# Get all subtasks for a specific project
def get_subtasks_by_project(db: Session, project_id: int):
    return db.query(models.Subtask).filter(models.Subtask.project_id == project_id).all()
