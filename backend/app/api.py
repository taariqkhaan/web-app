from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Project, Subtask
from schemas import ProjectBase, SubtaskBase

app = FastAPI()

@app.post("/projects/", response_model=ProjectBase)
def create_project(project: ProjectBase, db: Session = Depends(get_db)):
    # Create Project
    db_project = Project(
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
    db.flush()  # Flush to assign project.id without committing

    # Create Subtasks
    db_subtasks = []
    for subtask in project.subtasks:
        db_subtask = Subtask(
            subtask_name=subtask.subtask_name,
            labor_amount=subtask.labor_amount,
            expenses_amount=subtask.expenses_amount,
            travel_amount=subtask.travel_amount,
            tier_fee=subtask.tier_fee,
            budget_amount=subtask.budget_amount,
            project_id=db_project.id
        )
        db.add(db_subtask)
        db_subtasks.append(db_subtask)

    db.commit()
    db.refresh(db_project)

    return db_project  # Return the created project with subtasks
