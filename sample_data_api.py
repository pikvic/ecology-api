from models import Parameter as P, Template as T, TemplateParameter as TP, ParamTypeEnum as PTE
import random
import datetime

PARAMETERS = [
    P(id=1, label='Температура воды', type=PTE.FLOAT),
    P(id=2, label='Температура воздуха', type=PTE.FLOAT),
    P(id=3, label='Запах', type=PTE.STR, allowed_values='Слабый, Сильный'),
    P(id=4, label='Скорость течения', type=PTE.FLOAT),
    P(id=5, label='Название реки', type=PTE.STR),
    P(id=6, label='Оценка загрязнения', type=PTE.INT),
    P(id=7, label='Краткое описание', type=PTE.TEXT),
    P(id=8, label='Название отчёта', type=PTE.STR),
    P(id=9, label='Название озера', type=PTE.STR),
    P(id=10, label='Название моря', type=PTE.STR),
]

TEMPLATES = [
    T(id=1, name='Исследование реки', description='Исследование реки с целью выявления загрязнений'),
    T(id=2, name='Исследование озера', description='Исследование озера с целью выявления загрязнений'),
    T(id=3, name='Исследование моря', description='Исследование моря с целью выявления загрязнений')
]

PARAMETERS_TEMPLATES = [
    TP(id=1, template_id=1, parameter_id=8),
    TP(id=2, template_id=1, parameter_id=5),
    TP(id=3, template_id=1, parameter_id=7),
    TP(id=4, template_id=1, parameter_id=4),
    TP(id=5, template_id=1, parameter_id=1),
    TP(id=6, template_id=1, parameter_id=2),
    TP(id=7, template_id=1, parameter_id=6),

    TP(id=8, template_id=2, parameter_id=8),
    TP(id=9, template_id=2, parameter_id=9),
    TP(id=10, template_id=2, parameter_id=7),
    TP(id=11, template_id=2, parameter_id=3),
    TP(id=12, template_id=2, parameter_id=1),
    TP(id=13, template_id=2, parameter_id=2),
    TP(id=14, template_id=2, parameter_id=6),

    TP(id=15, template_id=3, parameter_id=8),
    TP(id=16, template_id=3, parameter_id=10),
    TP(id=17, template_id=3, parameter_id=7),
    TP(id=18, template_id=3, parameter_id=1),
    TP(id=19, template_id=3, parameter_id=2),
    TP(id=20, template_id=3, parameter_id=6)
]