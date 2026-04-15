from app.db.database import engine, Base
from app.db.models import AnalysisRun

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done!")