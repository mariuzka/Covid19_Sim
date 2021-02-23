from def_run_simulation_experiment import *
from def_get_params import *

spotpy_params = get_spotpy_params("important_outputs/params/LHS_BW_2021_01_20.csv")

results = run_simulation_experiment(
    state = 8,
    infection_prob = spotpy_params["infection_prob"],
    n_ticks_to_quarantine = spotpy_params["ticks_to_quarantine"],
    parallel = False,
    )