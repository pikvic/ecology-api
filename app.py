from fastapi import FastAPI
from datetime import datetime
from typing import List

from models import Parameter, Report, FreshWaterReport, SeaWaterReport, GasReport, Template, TemplateParameter
import sample_data
import sample_data_api


app = FastAPI()

sample_data.generate_data()

@app.get("/")
def root() -> List[Report]:
    return sample_data.reports

@app.get("/reports")
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


@app.get("/api/templates")
def get_templates() -> List[Template]:
    return sample_data_api.TEMPLATES

@app.get("/api/parameters")
def get_parameters() -> List[Parameter]:
    return sample_data_api.PARAMETERS

@app.get("/api/templates_parameters")
def get_templates_parameters() -> List[TemplateParameter]:
    return sample_data_api.PARAMETERS_TEMPLATES
