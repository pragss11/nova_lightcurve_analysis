# nova_lightcurve_analysis
Python scripts for photometric and spectroscopic data visualization.
# Light Curve Plotting Scripts

This repository contains Python scripts used to generate light curve plots for a classical nova research project. 
The code reads photometric data, processes time–magnitude information, and produces visualizations for two datasets:
a V-band light curve and a combined-band (“complete band”) light curve.

## Contents
- `vband_lightcurve.py` — Script for plotting the V-band light curve.
- `complete_lightcurve.py` — Script for plotting the full/combined-band light curve.
- `plots/` — Example output figures (optional).

## Features
- Reads time-series photometric data from CSV files.
- Generates clean, publication-style light curve plots.
- Supports magnitude uncertainties (if included in the dataset).
- Uses standard Python scientific libraries (NumPy, Pandas, Matplotlib).

## How to Run
1. Install required libraries:
   pip install numpy pandas matplotlib
2. Run the script:
   python vband_lightcurve.py or
   python complete_lightcurve.py
3. Replace the sample CSV files with your own data to generate custom plots.

## Notes
- Full observational datasets are not uploaded here.
- Time values may be in JD, HJD, or BJD depending on the project; adjust labels accordingly.
- These scripts were developed as part of an ongoing multiwavelength study of a classical nova.
