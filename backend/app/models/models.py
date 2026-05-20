from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from backend.app.database.session import Base

class Pipeline(Base):
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True, index=True)
    repository = Column(String, index=True)
    branch = Column(String)
    status = Column(String)  # success, failure, pending
    created_at = Column(DateTime, default=datetime.utcnow)

    failures = relationship("Failure", back_populates="pipeline")

class Failure(Base):
    __tablename__ = "failures"

    id = Column(Integer, primary_key=True, index=True)
    pipeline_id = Column(Integer, ForeignKey("pipelines.id"))
    error_log = Column(Text)
    root_cause = Column(String, nullable=True)
    ai_analysis = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    pipeline = relationship("Pipeline", back_populates="failures")
    fixes = relationship("Fix", back_populates="failure")

class Fix(Base):
    __tablename__ = "fixes"

    id = Column(Integer, primary_key=True, index=True)
    failure_id = Column(Integer, ForeignKey("failures.id"))
    fix_description = Column(Text)
    validation_status = Column(String) # pending, passed, failed
    applied_at = Column(DateTime, default=datetime.utcnow)

    failure = relationship("Failure", back_populates="fixes")
    validations = relationship("Validation", back_populates="fix")

class Validation(Base):
    __tablename__ = "validations"

    id = Column(Integer, primary_key=True, index=True)
    fix_id = Column(Integer, ForeignKey("fixes.id"))
    test_status = Column(String)
    security_status = Column(String)
    lint_status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    fix = relationship("Fix", back_populates="validations")
