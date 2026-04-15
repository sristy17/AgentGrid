from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from app.db.database import Base


class AnalysisRun(Base):
    __tablename__ = "analysis_runs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

    input_data = Column(JSON)
    analytics = Column(JSON)
    insights = Column(JSON)
    strategy = Column(JSON)