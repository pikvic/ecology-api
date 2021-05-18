from pydantic import BaseModel
from typing import Optional
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


class ParamTypeEnum(Enum):
    INT = 'int'
    FLOAT = 'float'
    STR = 'str'
    TEXT = 'text'
    FILE = 'file'
    PHOTO = 'photo'
    VIDEO = 'video'
    SET = 'set'

class Template(BaseModel):
    id: int
    name: str
    description: str
    parent_id: Optional[int] = None

class Parameter(BaseModel):
    id: int
    label: str
    type: ParamTypeEnum
    unit: Optional[str] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    allowed_values: Optional[str] = None
    is_multiple: bool = False

class TemplateParameter(BaseModel):
    id: int
    template_id: int
    parameter_id: int
    parameter_order: int = 0
    is_required: bool = False