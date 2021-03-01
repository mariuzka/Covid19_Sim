Note: The documentation of this repository is still under developement

## Instructions

### Preparations
1. Download this repository.
2. Install all packages named in "requirements.txt"
3. Get the SOEP 2017 and replace the empty folder "Covid19_Sim/data/soep.v34" with the original folder "soep.v34" that comes with the SOEP 2017.
4. Open the both STATA-Do-Files and set the working directories. Run the STATA-Do-File "stata_01_merge_soep_datasets.do". Then execute the STATA-Do-File "stata_02_clean_soep_data.do".

### Run the simulation experiment
The simulation experiment compares the effectivness of several NPIs in certain federal states of Germany.
To run the experiment execute one of the following files:
 
- **"run_simulation_experiment_BW.py"** (Baden-Würrtemberg)
- **"run_simulation_experiment_BY.py"** (Bavaria)
- **"run_simulation_experiment_SL.py"** (Saarland)
- **"run_simulation_experiment_HH.py"** (Hamburg)

## Code
The main python-files in which the main classes are defined are:
- **"Sim.py"**: In this file the simulation model is definded. The main simulation procedure is defined here.
- **"Corona_Agent.py"**: In this file classes for agents and locations in the simulated world are defined.
