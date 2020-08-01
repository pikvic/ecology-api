import models
import random
import datetime

N_ITEMS = 7

reports = []
fw_reports = []
sw_reports = []
gas_reports = []
types = [
    models.ReportTypeEnum.fresh_water, 
    models.ReportTypeEnum.sea_water,
    models.ReportTypeEnum.gas
]

fw_types = [
    models.FreshWaterTypeEnum.river,
    models.FreshWaterTypeEnum.lake,
]

sw_types = [
    models.SeaWaterTypeEnum.sea,
    models.SeaWaterTypeEnum.ocean,
]

def get_last_id(report_type):
    if report_type == models.ReportTypeEnum.fresh_water:
        return len(fw_reports) + 1
    elif report_type == models.ReportTypeEnum.sea_water:
        return len(sw_reports) + 1
    elif report_type == models.ReportTypeEnum.gas:
        return len(gas_reports) + 1

def generate_report(report_type, lat, lon, id):
    if report_type == models.ReportTypeEnum.fresh_water:
        report = models.FreshWaterReport(
            id=id,
            lat=lat,
            lon=lon,
            temperature=float(random.randrange(0, 30)),
            salinity=float(random.randrange(0, 30)),
            water_type=random.choice(fw_types)
        )
        fw_reports.append(report)
    elif report_type == models.ReportTypeEnum.sea_water:
        report = models.SeaWaterReport(
            id=id,
            lat=lat,
            lon=lon,
            temperature=float(random.randrange(0, 30)),
            salinity=float(random.randrange(0, 30)),
            water_type=random.choice(sw_types)
        )
        sw_reports.append(report)
    elif report_type == models.ReportTypeEnum.gas:
        report = models.GasReport(
            id=id,
            lat=lat,
            lon=lon,
            co=float(random.randrange(0, 30)),
            so=float(random.randrange(0, 30)),
            sio=float(random.randrange(0, 30))
        )
        gas_reports.append(report)
    

def generate_data():
    for i in range(1, N_ITEMS + 1):
        report_type = random.choice(types)
        report = models.Report(
            id=i,
            type=report_type,
            lat=float(random.randrange(-90, 90)),
            lon=float(random.randrange(-180, 180)),
            created=datetime.datetime.now(),
            filled=random.choice([True, False]),
            uploaded=random.choice([True, False]),
            title=f'Мой отчёт {random.randrange(0, 1000)}',
            description=f'Lorem Ipsum etc.',
            id_in_table=get_last_id(report_type)
        )
        reports.append(report)
        generate_report(report.type, report.lat, report.lon, report.id_in_table)
