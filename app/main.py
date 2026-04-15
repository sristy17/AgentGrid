from fastapi import FastAPI, UploadFile, File, HTTPException
from app.agents.orchestrator import Orchestrator
from app.models.schemas import AnalyzeRequest
from app.utils.parser import parse_csv

from app.db.database import SessionLocal
from app.db.models import AnalysisRun


app = FastAPI(title="AgentGrid AI API")

orchestrator = Orchestrator()


@app.get("/")
def home():
    return {"message": "AgentGrid AI Running"}


# JSON ANALYSIS
@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        input_data = request.model_dump()

        result = orchestrator.run(input_data)
        # SAVE TO DB
        db = SessionLocal()
        db_run = AnalysisRun(
            input_data=input_data,
            analytics=result["analytics"],
            insights=result["insights"],
            strategy=result["strategy"]
        )
        db.add(db_run)
        db.commit()
        db.close()

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# CSV ANALYSIS
@app.post("/analyze-csv")
def analyze_csv(file: UploadFile = File(...)):
    try:
        data = parse_csv(file.file)
        input_data = {"data": data}

        result = orchestrator.run(input_data)

        # SAVE TO DB
        db = SessionLocal()
        db_run = AnalysisRun(
            input_data=input_data,
            analytics=result["analytics"],
            insights=result["insights"],
            strategy=result["strategy"]
        )
        db.add(db_run)
        db.commit()
        db.close()

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# HISTORY API
@app.get("/history")
def get_history(limit: int = 5):
    db = SessionLocal()

    runs = db.query(AnalysisRun)\
        .order_by(AnalysisRun.id.desc())\
        .limit(limit)\
        .all()

    result = []
    for run in runs:
        result.append({
            "id": run.id,
            "timestamp": run.timestamp,
            "analytics": run.analytics,
            "insights": run.insights,
            "strategy": run.strategy
        })

    db.close()
    return result