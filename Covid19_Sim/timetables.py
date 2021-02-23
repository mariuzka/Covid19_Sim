# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 17:10:17 2020

@author: ac135963
"""

import datetime as dt

OPEN = 1
CLOSED = 0

KITA_PHASE_1 = 0.1
KITA_PHASE_2 = 0.3
KITA_PHASE_3 = 0.6
KITA_PHASE_4 = 1

UNIVERSITY_PHASE_1 = 0.1

SCHOOL_PHASE_1 = 0.1
SCHOOL_PHASE_2 = 0.3
SCHOOL_PHASE_3 = 0.6

BW_SCHOOL_PHASE_1 = 0.3
BW_SCHOOL_PHASE_3 = 0.75
BW_SCHOOL_PHASE_4 = 1

HESSEN_SCHOOL_PHASE_1 = 0.25
HESSEN_SCHOOL_PHASE_2 = 0.5
HESSEN_SCHOOL_PHASE_3 = 0.25
HESSEN_SCHOOL_PHASE_4 = 1

# Pfingstferien Bayern 02.06. - 13.06.
# Sommerferien Bayern 27.07. - 07.09.

# Pfingstferien Bawü 02.06. - 13.06.
# Sommerferien Bawü 30.07. - 12.09. 

# Pfingstferuen Hamburg 18.05. - 22.05.
# Sommerferien Hamburg 25.06. - 05.08.

# Osterferien Saarland 14.04. - 24.04.
# Sommerferien Saarland 06.07. - 14.08.


timetable_default = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_1,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_no_reduction_of_work = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_1,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    }

timetable_no_homeoffice = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_1,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_no_quarantine = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_1,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_open_kitas = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_open_schools = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": OPEN,
        "kindergartens": KITA_PHASE_1,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 6): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": OPEN,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": OPEN,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": OPEN,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": OPEN,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": OPEN,
        "kindergartens": KITA_PHASE_3,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_open_universities = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_1,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": SCHOOL_PHASE_1,
        "kindergartens": KITA_PHASE_2,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_2,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": KITA_PHASE_2,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": SCHOOL_PHASE_2,
        "kindergartens": KITA_PHASE_3,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_open_schools_kitas = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 6): {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": UNIVERSITY_PHASE_1,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }

timetable_open_education = {
    dt.datetime(2020, 1, 1) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_freq",
        "quarantine": "none",
        "nace2_lockdown": "General_2020_01_01",
        "nace2_reduction_of_workhours": "quarter1",
        },
    dt.datetime(2020, 3, 16) : {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_03_16",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 6): {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 4, 20): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_04_20",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 6): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_06",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 5, 18): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 2): {
        "school": CLOSED,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 6, 15): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    dt.datetime(2020, 7, 1): {
        "school": OPEN,
        "kindergartens": OPEN,
        "university": OPEN,
        "supermarkets": OPEN,
        "wfh": "wfh_feas",
        "quarantine": "household",
        "nace2_lockdown": "General_2020_05_18",
        "nace2_reduction_of_workhours": "quarter2",
        },
    }