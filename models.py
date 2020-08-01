from pydantic import BaseModel
from enum import Enum, IntEnum
from datetime import datetime

class FreshWaterTypeEnum(Enum):
    river = "Река"
    lake = "Озеро"

class SeaWaterTypeEnum(Enum):
    sea = "Море"
    ocean = "Океан"

class ReportTypeEnum(IntEnum):
    fresh_water = 1
    sea_water = 2
    gas = 3

class Report(BaseModel):
    id: int
    type: ReportTypeEnum
    lat: float
    lon: float
    created: datetime = None
    filled: bool = False
    uploaded: bool = False
    title: str
    description: str
    id_in_table: int


class GasReport(BaseModel):
    id: int
    lat: float
    lon: float
    co: float
    so: float
    sio: float
    
class FreshWaterReport(BaseModel):
    id: int
    lat: float
    lon: float
    temperature: float
    salinity: float
    water_type: FreshWaterTypeEnum

class SeaWaterReport(BaseModel):
    id: int
    lat: float
    lon: float
    temperature: float
    salinity: float
    water_type: SeaWaterTypeEnum
