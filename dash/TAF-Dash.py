import pandas as pd
from pathlib import Path
import streamlit as st
import seaborn as sns
import funcoes as f
import plotly.express as px

# tabelas masculino LEMB
dicio_corrida_m_b = {
    "18-21": {
        "I": (0, 2599),
        "R": (2600, 2799),
        "B": (2800, 3149),
        "MB": (3150, 3199),
        "E": (3200, float('inf'))
    },
    "22-25": {
        "I": (0, 2699),
        "R": (2700, 2849),
        "B": (2850, 3099),
        "MB": (3100, 3249),
        "E": (3250, float('inf'))
    },
    "26-29": {
        "I": (0, 2599),
        "R": (2600, 2749),
        "B": (2750, 2999),
        "MB": (3000, 3149),
        "E": (3150, float('inf'))
    },
    "30-33": {
        "I": (0, 2549),
        "R": (2550, 2649),
        "B": (2650, 2899),
        "MB": (2900, 3099),
        "E": (3100, float('inf'))
    },
    "34-37": {
        "I": (0, 2449),
        "R": (2450, 2549),
        "B": (2550, 2799),
        "MB": (2800, 2949),
        "E": (2950, float('inf'))
    },
    "38-41": {
        "I": (0, 2349),
        "R": (2350, 2449),
        "B": (2450, 2699),
        "MB": (2700, 2849),
        "E": (2850, float('inf'))
    },
    "42-45": {
        "I": (0, 2249),
        "R": (2250, 2399),
        "B": (2400, 2599),
        "MB": (2600, 2749),
        "E": (2750, float('inf'))
    },
    "46-49": {
        "I": (0, 2149),
        "R": (2150, 2299),
        "B": (2300, 2499),
        "MB": (2500, 2649),
        "E": (2650, float('inf'))
    },
    "50-53": 1900,
    "54-57": 1800,
    "58-61": 1600,
    "62-65": 1400
}

dicio_flexao_m_b = {
    "18-21": {
        "I": (0, 21),
        "R": (22, 24),
        "B": (25, 33),
        "MB": (34, 38),
        "E": (39, float('inf'))
    },
    "22-25": {
        "I": (0, 23),
        "R": (24, 26),
        "B": (27, 35),
        "MB": (36, 40),
        "E": (41, float('inf'))
    },
    "26-29": {
        "I": (0, 21),
        "R": (22, 24),
        "B": (25, 33),
        "MB": (34, 38),
        "E": (39, float('inf'))
    },
    "30-33": {
        "I": (0, 20),
        "R": (21, 23),
        "B": (24, 31),
        "MB": (32, 36),
        "E": (37, float('inf'))
    },
    "34-37": {
        "I": (0, 17),
        "R": (18, 20),
        "B": (21, 28),
        "MB": (29, 33),
        "E": (34, float('inf'))
    },
    "38-41": {
        "I": (0, 16),
        "R": (17, 19),
        "B": (20, 27),
        "MB": (28, 31),
        "E": (32, float('inf'))
    },
    "42-45": {
        "I": (0, 14),
        "R": (15, 17),
        "B": (18, 24),
        "MB": (25, 28),
        "E": (29, float('inf'))
    },
    "46-49": {
        "I": (0, 11),
        "R": (12, 14),
        "B": (15, 21),
        "MB": (22, 25),
        "E": (26, float('inf'))
    },
    "50-53": 11,
    "54-57": 9,
    "58-61": 8,
    "62-65": 6
}

dicio_abdominal_m_b = {
    "18-21": {
        "I": (0, 34),
        "R": (35, 44),
        "B": (45, 63),
        "MB": (64, 73),
        "E": (74, float('inf'))
    },
    "22-25": {
        "I": (0, 41),
        "R": (42, 51),
        "B": (52, 68),
        "MB": (69, 78),
        "E": (79, float('inf'))
    },
    "26-29": {
        "I": (0, 37),
        "R": (38, 48),
        "B": (49, 65),
        "MB": (66, 75),
        "E": (76, float('inf'))
    },
    "30-33": {
        "I": (0, 33),
        "R": (34, 42),
        "B": (43, 60),
        "MB": (61, 69),
        "E": (70, float('inf'))
    },
    "34-37": {
        "I": (0, 30),
        "R": (31, 39),
        "B": (40, 56),
        "MB": (57, 65),
        "E": (66, float('inf'))
    },
    "38-41": {
        "I": (0, 28),
        "R": (29, 37),
        "B": (38, 54),
        "MB": (55, 63),
        "E": (64, float('inf'))
    },
    "42-45": {
        "I": (0, 26),
        "R": (27, 35),
        "B": (36, 52),
        "MB": (53, 61),
        "E": (62, float('inf'))
    },
    "46-49": {
        "I": (0, 24),
        "R": (25, 33),
        "B": (34, 50),
        "MB": (51, 59),
        "E": (60, float('inf'))
    },
    "50-53": 23,
    "54-57": 21,
    "58-61": 19,
    "62-65": 17
}

dicio_barra_m_b = {
    "18-21": {
        "I": (0, 4),
        "R": (5, 6),
        "B": (7, 9),
        "MB": (10, 11),
        "E": (12, float('inf'))
    },
    "22-25": {
        "I": (0, 5),
        "R": (6, 7),
        "B": (8, 10),
        "MB": (11, 12),
        "E": (13, float('inf'))
    },
    "26-29": {
        "I": (0, 4),
        "R": (5, 6),
        "B": (7, 9),
        "MB": (10, 11),
        "E": (12, float('inf'))
    },
    "30-33": {
        "I": (0, 4),
        "R": (5, 5),
        "B": (6, 8),
        "MB": (9, 10),
        "E": (11, float('inf'))
    },
    "34-37": {
        "I": (0, 3),
        "R": (4, 4),
        "B": (5, 6),
        "MB": (7, 8),
        "E": (9, float('inf'))
    },
    "38-39": {
        "I": (0, 2),
        "R": (3, 3),
        "B": (4, 5),
        "MB": (6, 7),
        "E": (8, float('inf'))
    },
    "40-45":2,
    "46-49":1,
    "50-70":0
}

#  tabelas femininas LEMB
dicio_corrida_f_b = {
    "18-21": {
        "I": (0, 2099),
        "R": (2100, 2199),
        "B": (2200, 2449),
        "MB": (2450, 2599),
        "E": (2600, float('inf'))
    },
    "22-25": {
        "I": (0, 2149),
        "R": (2150, 2249),
        "B": (2250, 2449),
        "MB": (2450, 2649),
        "E": (2650, float('inf'))
    },
    "26-29": {
        "I": (0, 2099),
        "R": (2100, 2199),
        "B": (2200, 2399),
        "MB": (2400, 2599),
        "E": (2600, float('inf'))
    },
    "30-33": {
        "I": (0, 2049),
        "R": (2050, 2149),
        "B": (2150, 2349),
        "MB": (2350, 2549),
        "E": (2550, float('inf'))
    },
    "34-37": {
        "I": (0, 1999),
        "R": (2000, 2099),
        "B": (2100, 2299),
        "MB": (2300, 2499),
        "E": (2500, float('inf'))
    },
    "38-41": {
        "I": (0, 1899),
        "R": (1900, 1999),
        "B": (2000, 2199),
        "MB": (2200, 2399),
        "E": (2400, float('inf'))
    },
    "42-45": {
        "I": (0, 1849),
        "R": (1850, 1949),
        "B": (1950, 2149),
        "MB": (2150, 2299),
        "E": (2300, float('inf'))
    },
    "46-49": {
        "I": (0, 1749),
        "R": (1750, 1849),
        "B": (1850, 2049),
        "MB": (2050, 2249),
        "E": (2250, float('inf'))
    },
    "50-53": 1600,
    "54-57": 1500,
    "58-61": 1300,
    "62-65": 1100
}

dicio_flexao_f_b = {
    "18-21": {
        "I": (0, 10),
        "R": (11, 11),
        "B": (12, 16),
        "MB": (17, 19),
        "E": (20, float('inf'))
    },
    "22-25": {
        "I": (0, 11),
        "R": (12, 12),
        "B": (13, 18),
        "MB": (19, 21),
        "E": (22, float('inf'))
    },
    "26-29": {
        "I": (0, 10),
        "R": (11, 11),
        "B": (12, 16),
        "MB": (17, 19),
        "E": (20, float('inf'))
    },
    "30-33": {
        "I": (0, 9),
        "R": (10, 10),
        "B": (11, 15),
        "MB": (16, 18),
        "E": (19, float('inf'))
    },
    "34-37": {
        "I": (0, 8),
        "R": (9, 9),
        "B": (10, 14),
        "MB": (15, 17),
        "E": (18, float('inf'))
    },
    "38-41": {
        "I": (0, 7),
        "R": (8, 8),
        "B": (9, 13),
        "MB": (14, 16),
        "E": (17, float('inf'))
    },
    "42-45": {
        "I": (0, 6),
        "R": (7, 7),
        "B": (8, 12),
        "MB": (13, 15),
        "E": (16, float('inf'))
    },
    "46-49": {
        "I": (0, 5),
        "R": (6, 6),
        "B": (7, 10),
        "MB": (11, 13),
        "E": (14, float('inf'))
    },
    "50-53": 5,
    "54-57": 4,
    "58-61": 3,
    "62-65": 2
}

dicio_abdominal_f_b = {
    "18-21": {
        "I": (0, 30),
        "R": (31, 39),
        "B": (40, 55),
        "MB": (56, 64),
        "E": (65, float('inf'))
    },
    "22-25": {
        "I": (0, 32),
        "R": (33, 41),
        "B": (42, 57),
        "MB": (58, 66),
        "E": (67, float('inf'))
    },
    "26-29": {
        "I": (0, 31),
        "R": (32, 40),
        "B": (41, 56),
        "MB": (57, 65),
        "E": (66, float('inf'))
    },
    "30-33": {
        "I": (0, 29),
        "R": (30, 38),
        "B": (39, 54),
        "MB": (55, 63),
        "E": (64, float('inf'))
    },
    "34-37": {
        "I": (0, 27),
        "R": (28, 36),
        "B": (37, 52),
        "MB": (53, 61),
        "E": (62, float('inf'))
    },
    "38-41": {
        "I": (0, 25),
        "R": (26, 34),
        "B": (35, 50),
        "MB": (51, 59),
        "E": (60, float('inf'))
    },
    "42-45": {
        "I": (0, 23),
        "R": (24, 32),
        "B": (33, 48),
        "MB": (49, 57),
        "E": (58, float('inf'))
    },
    "46-49": {
        "I": (0, 21),
        "R": (22, 30),
        "B": (31, 46),
        "MB": (47, 55),
        "E": (56, float('inf'))
    },
    "50-53": 20,
    "54-57": 18,
    "58-61": 16,
    "62-65": 14
}

dicio_barra_f_b = {
    "18-21": {
        "I": (0, 0),
        "R": (1, 2),
        "B": (3, 4),
        "MB": (5, 5),
        "E": (6, float('inf'))
    },
    "22-25": {
        "I": (0, 1),
        "R": (2, 3),
        "B": (4, 5),
        "MB": (6, 6),
        "E": (7, float('inf'))
    },
    "26-29": {
        "I": (0, 1),
        "R": (2, 2),
        "B": (3, 4),
        "MB": (5, 5),
        "E": (6, float('inf'))
    },
    "30-33": {
        "I": (0, 0),
        "R": (1, 2),
        "B": (3, 4),
        "MB": (5, 5),
        "E": (6, float('inf'))
    },
    "34-37": {
        "I": (0, 0),
        "R": (1, 2),
        "B": (3, 3),
        "MB": (4, 4),
        "E": (5, float('inf'))
    },
    "38-39": {
        "I": (0, 0),
        "R": (1, 1),
        "B": (2, 2),
        "MB": (3, 3),
        "E": (4, float('inf'))
    },
    "40-45":45,
    "46-49":30
}

# tabela masculina complementar
dicio_corrida_m_c = {
    "18-21": {
        "I": (0, 2599),
        "R": (2600, 2699),
        "B": (2700, 2899),
        "MB": (2900, 2999),
        "E": (3000, float('inf'))
    },
    "22-25": {
        "I": (0, 2699),
        "R": (2700, 2799),
        "B": (2800, 2949),
        "MB": (2950, 3049),
        "E": (3050, float('inf'))
    },
    "26-29": {
        "I": (0, 2599),
        "R": (2600, 2699),
        "B": (2700, 2849),
        "MB": (2850, 2949),
        "E": (2950, float('inf'))
    },
    "30-33": {
        "I": (0, 2549),
        "R": (2550, 2649),
        "B": (2650, 2799),
        "MB": (2800, 2899),
        "E": (2900, float('inf'))
    },
    "34-37": {
        "I": (0, 2449),
        "R": (2450, 2549),
        "B": (2550, 2649),
        "MB": (2650, 2749),
        "E": (2750, float('inf'))
    },
    "38-41": {
        "I": (0, 2349),
        "R": (2350, 2449),
        "B": (2450, 2549),
        "MB": (2550, 2649),
        "E": (2650, float('inf'))
    },
    "42-45": {
        "I": (0, 2249),
        "R": (2250, 2349),
        "B": (2350, 2499),
        "MB": (2500, 2599),
        "E": (2600, float('inf'))
    },
    "46-49": {
        "I": (0, 2149),
        "R": (2150, 2299),
        "B": (2300, 2399),
        "MB": (2400, 2499),
        "E": (2500, float('inf'))
    },
    "50-53": 1900,
    "54-57": 1800,
    "58-61": 1600,
    "62-65": 1400
}

dicio_flexao_m_c = {
    "18-21": {
        "I": (0, 21),
        "R": (22, 24),
        "B": (25, 29),
        "MB": (30, 32),
        "E": (33, float('inf'))
    },
    "22-25": {
        "I": (0, 23),
        "R": (24, 26),
        "B": (27, 31),
        "MB": (32, 34),
        "E": (35, float('inf'))
    },
    "26-29": {
        "I": (0, 21),
        "R": (22, 24),
        "B": (25, 29),
        "MB": (30, 32),
        "E": (33, float('inf'))
    },
    "30-33": {
        "I": (0, 20),
        "R": (21, 23),
        "B": (24, 27),
        "MB": (28, 30),
        "E": (31, float('inf'))
    },
    "34-37": {
        "I": (0, 17),
        "R": (18, 20),
        "B": (21, 25),
        "MB": (26, 28),
        "E": (29, float('inf'))
    },
    "38-41": {
        "I": (0, 16),
        "R": (17, 19),
        "B": (20, 23),
        "MB": (24, 26),
        "E": (27, float('inf'))
    },
    "42-45": {
        "I": (0, 14),
        "R": (15, 17),
        "B": (18, 21),
        "MB": (22, 24),
        "E": (25, float('inf'))
    },
    "46-49": {
        "I": (0, 11),
        "R": (12, 14),
        "B": (15, 18),
        "MB": (19, 21),
        "E": (22, float('inf'))
    },
    "50-53": 11,
    "54-57": 9,
    "58-61": 8,
    "62-65": 6
}

dicio_abdominal_m_c = {
    "18-21": {
        "I": (0, 34),
        "R": (35, 44),
        "B": (45, 63),
        "MB": (64, 73),
        "E": (74, float('inf'))
    },
    "22-25": {
        "I": (0, 41),
        "R": (42, 51),
        "B": (52, 68),
        "MB": (69, 78),
        "E": (79, float('inf'))
    },
    "26-29": {
        "I": (0, 37),
        "R": (38, 48),
        "B": (49, 65),
        "MB": (66, 75),
        "E": (76, float('inf'))
    },
    "30-33": {
        "I": (0, 33),
        "R": (34, 42),
        "B": (43, 60),
        "MB": (61, 69),
        "E": (70, float('inf'))
    },
    "34-37": {
        "I": (0, 30),
        "R": (31, 39),
        "B": (40, 56),
        "MB": (57, 65),
        "E": (66, float('inf'))
    },
    "38-41": {
        "I": (0, 28),
        "R": (29, 37),
        "B": (38, 54),
        "MB": (55, 63),
        "E": (64, float('inf'))
    },
    "42-45": {
        "I": (0, 26),
        "R": (27, 35),
        "B": (36, 52),
        "MB": (53, 61),
        "E": (62, float('inf'))
    },
    "46-49": {
        "I": (0, 24),
        "R": (25, 33),
        "B": (34, 50),
        "MB": (51, 59),
        "E": (60, float('inf'))
    },
    "50-53": 23,
    "54-57": 21,
    "58-61": 19,
    "62-65": 17
}

#Tabela feminina complementar
dicio_corrida_f_c = {
    "18-21": {
        "I": (0, 2099),
        "R": (2100, 2199),
        "B": (2200, 2299),
        "MB": (2300, 2399),
        "E": (2400, float('inf'))
    },
    "22-25": {
        "I": (0, 2149),
        "R": (2150, 2249),
        "B": (2250, 2349),
        "MB": (2350, 2449),
        "E": (2450, float('inf'))
    },
    "26-29": {
        "I": (0, 2099),
        "R": (2100, 2199),
        "B": (2200, 2299),
        "MB": (2300, 2399),
        "E": (2400, float('inf'))
    },
    "30-33": {
        "I": (0, 2049),
        "R": (2050, 2149),
        "B": (2150, 2249),
        "MB": (2250, 2349),
        "E": (2350, float('inf'))
    },
    "34-37": {
        "I": (0, 1999),
        "R": (2000, 2099),
        "B": (2100, 2199),
        "MB": (2200, 2299),
        "E": (2300, float('inf'))
    },
    "38-41": {
        "I": (0, 1899),
        "R": (1900, 1999),
        "B": (2000, 2149),
        "MB": (2150, 2249),
        "E": (2250, float('inf'))
    },
    "42-45": {
        "I": (0, 1849),
        "R": (1850, 1949),
        "B": (1950, 2049),
        "MB": (2050, 2149),
        "E": (2150, float('inf'))
    },
    "46-49": {
        "I": (0, 1749),
        "R": (1750, 1849),
        "B": (1850, 1949),
        "MB": (1950, 2049),
        "E": (2050, float('inf'))
    },
    "50-53": 1600,
    "54-57": 1500,
    "58-61": 1300,
    "62-65": 1100
}

dicio_flexao_f_c = {
    "18-21": {
        "I": (0, 10),
        "R": (11, 11),
        "B": (12, 14),
        "MB": (15, 15),
        "E": (16, float('inf'))
    },
    "22-25": {
        "I": (0, 11),
        "R": (12, 12),
        "B": (13, 15),
        "MB": (16, 16),
        "E": (17, float('inf'))
    },
    "26-29": {
        "I": (0, 10),
        "R": (11, 11),
        "B": (12, 14),
        "MB": (15, 15),
        "E": (16, float('inf'))
    },
    "30-33": {
        "I": (0, 9),
        "R": (10, 10),
        "B": (11, 13),
        "MB": (14, 14),
        "E": (15, float('inf'))
    },
    "34-37": {
        "I": (0, 8),
        "R": (9, 9),
        "B": (10, 12),
        "MB": (13, 13),
        "E": (14, float('inf'))
    },
    "38-41": {
        "I": (0, 7),
        "R": (8, 8),
        "B": (9, 11),
        "MB": (12, 12),
        "E": (13, float('inf'))
    },
    "42-45": {
        "I": (0, 6),
        "R": (7, 7),
        "B": (8, 10),
        "MB": (11, 11),
        "E": (12, float('inf'))
    },
    "46-49": {
        "I": (0, 5),
        "R": (6, 6),
        "B": (7, 9),
        "MB": (10, 10),
        "E": (11, float('inf'))
    },
    "50-53": 5,
    "54-57": 4,
    "58-61": 3,
    "62-65": 2
}

dicio_abdominal_f_c = {
    "18-21": {
        "I": (0, 30),
        "R": (31, 39),
        "B": (40, 55),
        "MB": (56, 64),
        "E": (65, float('inf'))
    },
    "22-25": {
        "I": (0, 32),
        "R": (33, 41),
        "B": (42, 57),
        "MB": (58, 66),
        "E": (67, float('inf'))
    },
    "26-29": {
        "I": (0, 31),
        "R": (32, 40),
        "B": (41, 56),
        "MB": (57, 65),
        "E": (66, float('inf'))
    },
    "30-33": {
        "I": (0, 29),
        "R": (30, 38),
        "B": (39, 54),
        "MB": (55, 63),
        "E": (64, float('inf'))
    },
    "34-37": {
        "I": (0, 27),
        "R": (28, 36),
        "B": (37, 52),
        "MB": (53, 61),
        "E": (62, float('inf'))
    },
    "38-41": {
        "I": (0, 25),
        "R": (26, 34),
        "B": (35, 50),
        "MB": (51, 59),
        "E": (60, float('inf'))
    },
    "42-45": {
        "I": (0, 23),
        "R": (24, 32),
        "B": (33, 48),
        "MB": (49, 57),
        "E": (58, float('inf'))
    },
    "46-49": {
        "I": (0, 21),
        "R": (22, 30),
        "B": (31, 46),
        "MB": (47, 55),
        "E": (56, float('inf'))
    },
    "50-53": 19,
    "54-57": 17,
    "58-61": 15,
    "62-65": 13
}


# Dicionário que mapeia o nome da atividade para as tabelas correspondentes (masculino e feminino)
dicio_atividades = {'B':{
    "CORRIDA": {
        "M": dicio_corrida_m_b,
        "F": dicio_corrida_f_b
    },
    "FLEXAO": {
        "M": dicio_flexao_m_b,
        "F": dicio_flexao_f_b
    },
    "ABDOMINAL": {
        "M": dicio_abdominal_m_b,
        "F": dicio_abdominal_f_b
    },
    "BARRA": {
        "M": dicio_barra_m_b,
        "F": dicio_barra_f_b
    }
},
'CT':{
    "CORRIDA": {
        "M": dicio_corrida_m_c,
        "F": dicio_corrida_f_c
    },
    "FLEXAO": {
        "M": dicio_flexao_m_c,
        "F": dicio_flexao_f_c
    },
    "ABDOMINAL": {
        "M": dicio_abdominal_m_c,
        "F": dicio_abdominal_f_c
    }
}
}

#IMPORTANDO A PLANILHA PARA UM DATAFRAME
diretorio_atual = Path.cwd()
arquivo = diretorio_atual/'PLANILHA TAF.xlsx'
arquivo_excel = pd.ExcelFile(arquivo)#variável recebe todo o arquivo exel com suas abas
dfs = [pd.read_excel(arquivo_excel,sheet_name=sheet).assign(TAF=sheet) for sheet in arquivo_excel.sheet_names] #cria uma lista com as abas da planilha
tabela_tafs = pd.concat(dfs,ignore_index=True)#concatena as abas da planilha em uma só


######### INICIANDO A CRIAÇÃO DA PÁGINA
# CONFIGURANDO A PÁGINA
st.set_page_config(
     layout='wide',
     page_title='TAF - 10º BIL Mth',
 )
#TÍTULO
st.markdown("<h1 style='text-align: center;'>TAF - 10º BIL Mth</h1>", unsafe_allow_html=True)

######CRIANDO A MOLDURA DOS BOTÕES DO TAF
with st.container(border=True):
    col1,col2,col3 = st.columns(3) #cria 3 colunas
    taf_1 = col1.checkbox('1º TAF',value=True)
    taf_2 = col2.checkbox('2º TAF')
    taf_3 = col3.checkbox('3º TAF')

#FILTRANDO A TABELA PELOS TAF ESCOLHIDOS
tabela_do_taf = f.pega_taf(tabela_tafs,taf_1,taf_2,taf_3)#pegando os taf selecionados

#CRIANDO AS COLUNAS CENTRAIS
col_central = st.columns([1, 4, 1])[1] #criando as colunas

col4, mid_col, col7 = st.columns([0.15,0.7,0.15], vertical_alignment='center')
col5,col6 = mid_col.columns([1,3], vertical_alignment='center')

#CONFIGURANDO OS MENUS DA ESQUERDA
with col4:
    #CRIANDO MENUS COM SELEÇÃO DE IDADE, EXERCÍCIOS E MENÇÕES
    st.subheader('ITENS / CONSULTA')
    idade = st.checkbox('IDADE',value=True)
    if idade:
        escolha_idade = st.selectbox('escolha',('TODAS','18-21','22-25','26-29','30-33','34-37','38-41','42-45','46-49','>=50'),label_visibility='hidden', placeholder='Escolha a faixa etária', index=None)
    else:
        escolha_idade = None
    segmento = st.checkbox('SEGMENTO',value=True)
    mas, fem = True, True #colocado só para evitar o erro na linha 84 caso a checkbox do segmento não seja selecionada.
    if segmento:
        mas = st.checkbox('MASCULINO', value=True)
        fem = st.checkbox('FEMININO', value=True)
    corrida = st.checkbox('CORRIDA')
    flexao = st.checkbox('FLEXÃO')
    abdominal = st.checkbox('ABDOMINAL')
    barra = st.checkbox('BARRA')
    mencao = st.checkbox('MENÇÃO')
    #CRIANDO MENUS COM AS CHAMADAS
    st.subheader('CHAMADAS')
    primeira_chamada = st.checkbox('1ª Chamada',value=True)
    segunda_chamada = st.checkbox('2ª Chamada',value=True)
    nr = st.checkbox('Não Realizado')

# CONFIGURANDO O MENU DA DIREITA
with col7:
    #CRIANDO MENU PARA AS SU
    lista_su = ['Geral','1ª Cia Fuz L Mth', '2ª Cia Fuz L Mth','Cia C Ap', 'CFGS','B Mus']
    st.subheader('SUBUNIDADES')
    escolha_su = st.radio('**SUBUNIDADES**', options=lista_su, index=0, label_visibility='hidden')
    #CRIANDO MENU PARA ESCOLHA DO POSTO / GRADUAÇÃO
    st.subheader('POSTOS E GRADUAÇÕES')
    oficiais = st.checkbox('Oficiais',value=True)
    st_sgt = st.checkbox('ST e Sgt')
    cb_sd_ep = st.checkbox('Cb/Sd EP')
    sd_ev = st.checkbox('Sd EV')

#FILTRAR AS TABELA COM AS OPÇÕES ESCOLHIDAS NOS MENUS
tabela_filtrada =(f.filtra_su(
    f.filtra_pg(
        f.filtra_chamadas(
            f.filtra_segmento(
                f.pega_taf(tabela_tafs,taf_1,taf_2,taf_3)
                ,segmento, mas, fem)
        ,primeira_chamada,segunda_chamada,nr)
    ,oficiais,st_sgt,cb_sd_ep,sd_ev)
,escolha_su)
)

#FILTRANDO POR IDADE O QUE SOBROU DA TABELA
tabela_filtrada_idade = f.filtra_idade(tabela_filtrada,escolha_idade)
tabela_filtrada_idade


if idade:
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:#Todos os itens
                        with mid_col:
                            st.subheader(f'Para idade entre {escolha_idade}')
                            st.dataframe(tabela_filtrada_idade.drop(columns=['OBS', 'COMPANHIA', 'CHAMADA','TAF','BI Publicado']))
                    else:#('**SIM** - idade - corrida - flexão - abdominal - barra')('**NÃO** - menção')
                        col5.write('**SIM** - idade - corrida - flexão - abdominal - barra')
                        col6.write('**NÃO** - menção')
                        #colocar gráfico de pontos
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - abdominal - menção')
                        col6.write('**NÃO** - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão - abdominal')
                        col6.write('**NÃO** - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - barra - menção')
                        col6.write('**NÃO** - abdominal')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão - barra')
                        col6.write('**NÃO** - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - flexão - menção')
                        col6.write('**NÃO** - abdominal - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - flexão')
                        col6.write('**NÃO** - abdominal - barra - menção')
        else:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - abdominal - barra - menção')
                        col6.write('**NÃO** - flexão')
                    else:
                        col5.write('**SIM** - idade - corrida - abdominal - barra')
                        col6.write('**NÃO** - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - abdominal- menção')
                        col6.write('**NÃO** - flexão - barra')
                    else:
                        col5.write('**SIM** - idade - corrida - abdominal')
                        col6.write('**NÃO** - flexão - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - barra - menção')
                        col6.write('**NÃO** - flexão - abdominal')
                    else:
                        col5.write('**SIM** - idade - corrida - barra')
                        col6.write('**NÃO** - flexão - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - corrida - menção')
                        col6.write('**NÃO** - flexão - abdominal - barra')
                    else: #IDADE E CORRIDA
                        col5.write(f'Este gráfico de disperção mostra o desempenho na CORRIDA por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'CORRIDA')
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - abdominal - barra - menção')
                        col6.write('**NÃO** - corrida')
                    else:
                        col5.write('**SIM** - idade - flexão - abdominal - barra')
                        col6.write('**NÃO** - corrida - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - abdominal- menção')
                        col6.write('**NÃO** - corrida - barra')
                    else:
                        col5.write('**SIM** - idade - flexão - abdominal')
                        col6.write('**NÃO** - corrida - barra - menção')
            else: #corrida abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - flexão - barra - menção')
                        col6.write('**NÃO** - corrida - abdominal')
                    else:
                        col5.write('**SIM** - idade - flexão - barra')
                        col6.write('**NÃO** - corrida - abdominal - menção')
                else:#barra não
                    if mencao:
                        col5.write('**SIM** - idade - flexão - menção')
                        col6.write('**NÃO** - corrida - abdominal - barra')
                    else:# IDADE E FLEXÃO
                        col5.write(f'Este gráfico de disperção mostra o desempenho na FLEXÃO DE BRAÇO por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'FLEXÃO')
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - abdominal - barra - menção')
                        col6.write('**NÃO** - corrida - flexão')
                    else:
                        col5.write('**SIM** - idade - abdominal - barra')
                        col6.write('**NÃO** - corrida - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - idade - abdominal - menção')
                        col6.write('**NÃO** - corrida - flexão - barra')
                    else:# IDADE E ABDOMINAL
                        col5.write(f'Este gráfico de disperção mostra o desempenho no ABDOMINAL por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'ABDOMINAL')
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:
                        col5.write('**SIM** - idade - barra - menção')
                        col6.write('**NÃO** - corrida - flexão - abdominal')
                    else: #IDADE E BARRA
                        col5.write(f'Este gráfico de disperção mostra o desempenho na BARRA por SEGMENTO E IDADE -> {escolha_idade} anos')
                        with col6:
                            f.idade_seg_atv(tabela_filtrada_idade, 'BARRA')
                else:#barra não
                    if mencao:#MENÇÃO E IDADE
                         with col5:
                            st.write('O gráfico apresenta a porcentagens em cada menção, podendo ser alterado o segmento e a idade')
                         with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade))
                    else:#SOMENTE IDADE
                        col5.write('**SIM** - idade')
                        col6.write('**NÃO** - corrida - flexão - abdominal - barra - menção')
else: #idade não
    if corrida:
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        with mid_col:
                            st.dataframe(tabela_filtrada.drop(columns=['IDADE','OBS', 'COMPANHIA', 'CHAMADA','TAF','BI Publicado']))
                    else: #CORRIDA FLEXÃO ABDOMINAL BARRA
                        col5.write('**SIM**-  corrida - flexão - abdominal - barra')
                        col6.write('**NÃO** - idade - menção')
                       
                else:#idade - barra -não
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - abdominal - menção')
                        col6.write('**NÃO** - idade - barra')
                    else:
                        col5.write('**SIM** - corrida - flexão - abdominal')
                        col6.write('**NÃO** - idade - barra - menção')
            else:#idade - abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - barra - menção')
                        col6.write('**NÃO** - idade - abdominal')
                    else:
                        col5.write('**SIM** - corrida - flexão - barra')
                        col6.write('**NÃO** - idade - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - flexão - menção')
                        col6.write('**NÃO** - idade - abdominal - barra')
                    else:
                        col5.write('**SIM** - corrida - flexão')
                        col6.write('**NÃO** - idade - abdominal - barra - menção')
        else:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - flexão')
                    else:
                        col5.write('**SIM** - corrida - abdominal - barra')
                        col6.write('**NÃO** - idade - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - abdominal- menção')
                        col6.write('**NÃO** - idade - flexão - barra')
                    else:
                        col5.write('**SIM** - corrida - abdominal')
                        col6.write('**NÃO** - idade - flexão - barra - menção')
            else:
                if barra:
                    if mencao:
                        col5.write('**SIM** - corrida - barra - menção')
                        col6.write('**NÃO** - idade - flexão - abdominal')
                    else:
                        col5.write('**SIM** - corrida - barra')
                        col6.write('**NÃO** - idade - flexão - abdominal - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - corrida - menção')
                        col6.write('**NÃO** - idade - flexão - abdominal - barra')
                    else:#SOMENTE CORRIDA
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["CORRIDA"] == 'A') | (tabela_filtrada_idade["CORRIDA"].isna()) | (tabela_filtrada_idade["CORRIDA"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na corrida"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'CORRIDA', row['LEM'], row['SEGMENTO'], row['CORRIDA']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na corrida"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na corrida"))
    else:# corrida não
        if flexao:
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - flexão - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - corrida')
                    else:
                        col5.write('**SIM** - flexão - abdominal - barra')
                        col6.write('**NÃO** - idade - corrida - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - flexão - abdominal- menção')
                        col6.write('**NÃO** - idade - corrida - barra')
                    else:
                        col5.write('**SIM** - flexão - abdominal')
                        col6.write('**NÃO** - idade - corrida - barra - menção')
            else: #corrida abdominal não
                if barra:
                    if mencao:
                        col5.write('**SIM** - flexão - barra - menção')
                        col6.write('**NÃO** -idade -  corrida - abdominal')
                    else:
                        col5.write('**SIM** - flexão - barra')
                        col6.write('**NÃO** -idade -  corrida - abdominal - menção')
                else:#barra não
                    if mencao:
                        col5.write('**SIM** - flexão - menção')
                        col6.write('**NÃO** -idade -  corrida - abdominal - barra')
                    else: #SOMENTE FLEXÃO
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["FLEXÃO"] == 'A') | (tabela_filtrada_idade["FLEXÃO"].isna()) | (tabela_filtrada_idade["FLEXÃO"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na flexão"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'FLEXAO', row['LEM'], row['SEGMENTO'], row['FLEXÃO']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na flexão"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na flexão"))
        else: #corrida - flexão - não
            if abdominal:
                if barra:
                    if mencao:
                        col5.write('**SIM** - abdominal - barra - menção')
                        col6.write('**NÃO** - idade - corrida - flexão')
                    else:
                        col5.write('**SIM** - abdominal - barra')
                        col6.write('**NÃO** - idade - corrida - flexão - menção')
                else:
                    if mencao:
                        col5.write('**SIM** - abdominal - menção')
                        col6.write('**NÃO** - idade - corrida - flexão - barra')
                    else:# SOMENTE ABDOMINAL
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["ABDOMINAL"] == 'A') | (tabela_filtrada_idade["ABDOMINAL"].isna()) | (tabela_filtrada_idade["ABDOMINAL"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção no abdominal"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'ABDOMINAL', row['LEM'], row['SEGMENTO'], row['ABDOMINAL']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção no abdominal"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção no abdominal"))
            else: #corrida - flexão - abdominal
                if barra:
                    if mencao:
                        col5.write('**SIM** - barra - menção')
                        col6.write('**NÃO** - idade - corrida - flexão - abdominal')
                    else:# SOMENTE BARRA
                        tabela_filtrada_idade = tabela_filtrada_idade[~((tabela_filtrada_idade["BARRA"] == 'A') | (tabela_filtrada_idade["BARRA"].isna()) | (tabela_filtrada_idade["BARRA"] == 'X'))] # trata a tabela para tirar "A", nulo e 'X'
                        tabela_filtrada_idade["Menção na barra"] = tabela_filtrada_idade.apply(lambda row: f.determinar_mencao(row['IDADE'],dicio_atividades,'BARRA', row['LEM'], row['SEGMENTO'], row['BARRA']), axis=1)
                        with col5:
                            st.dataframe(tabela_filtrada_idade["Menção na barra"].value_counts())
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada_idade, "Menção na barra"))
                else:#barra não
                    if mencao:#SOMENTE MENÇÃO
                        with col5:
                            st.write('O gráfico apresenta a porcentagens em cada menção, podendo ser alterado o segmento e a idade')
                        with col6:
                            st.pyplot(f.grafico_pizza(tabela_filtrada, "MENÇÃO"))
                    else:#(tudo desmarcado)
                        with mid_col:
                            st.write('NENHUMA ATIVIDADE OU MENÇÃO SELECIONADA')

