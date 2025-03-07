# Database models (SQLAlchemy)

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    wo_number = Column(String, index=True)
    activity_code = Column(String, index=True)
    total_labor_amount = Column(Float, default=0.0)
    total_expenses_amount = Column(Float, default=0.0)
    total_travel_amount = Column(Float, default=0.0)
    total_tier_fee = Column(Float, default=0.0)
    total_budget_amount = Column(Float, default=0.0)

    subtasks = relationship("Subtask", back_populates="project", cascade="all, delete-orphan")

class Subtask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    subtask_name = Column(String, index=True)  # Physical, P&C, Telecom, etc.
    labor_amount = Column(Float, default=0.0)
    expenses_amount = Column(Float, default=0.0)
    travel_amount = Column(Float, default=0.0)
    tier_fee = Column(Float, default=0.0)
    budget_amount = Column(Float, default=0.0)

    project = relationship("Project", back_populates="subtasks")
