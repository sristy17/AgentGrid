from fastapi import FastAPI, UploadFile, File, HTTPException
from app.agents.orchestrator import Orchestrator
from app.models.schemas import AnalyzeRequest
from app.utils.parser import parse_csv

app = FastAPI(title="AgentGrid AI API")

orchestrator = Orchestrator()


@app.get("/")
def home():
    return {"message": "AgentGrid AI Running"}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    input_data = request.model_dump()
    return orchestrator.run(input_data)


@app.post("/analyze-csv")
def analyze_csv(file: UploadFile = File(...)):
    try:
        data = parse_csv(file.file)
        input_data = {"data": data}

        return orchestrator.run(input_data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))