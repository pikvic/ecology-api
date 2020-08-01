from fastapi import FastAPI
from datetime import datetime
from typing import List

from models import Report, FreshWaterReport, SeaWaterReport, GasReport
import sample_data

app = FastAPI()

sample_data.generate_data()

@app.get("/")
def reports() -> List[Report]:
    return sample_data.reports


@app.get("/fw/{report_id}")
def get_fw(report_id: int) -> FreshWaterReport:
    if report_id - 1 in range(len(sample_data.fw_reports)):
        return sample_data.fw_reports[report_id - 1]
    else:
        return {"error": "No such report_id!"}

@app.get("/sw/{report_id}")
def get_sw(report_id: int) -> FreshWaterReport:
    if report_id - 1 in range(len(sample_data.sw_reports)):
        return sample_data.sw_reports[report_id - 1]
    else:
        return {"error": "No such report_id!"}

@app.get("/gas/{report_id}")
def get_gas(report_id: int) -> FreshWaterReport:
    if report_id - 1 in range(len(sample_data.gas_reports)):
        return sample_data.gas_reports[report_id - 1]
    else:
        return {"error": "No such report_id!"}

