# Compyle

Compyle is a Python 3 G-Code post-processor for 3D models sliced in Ultimaker Cura 5.9+, allowing files to run on a 3-axis CNC gantry with a compressor-based hydrogel extruder.

## What it does:

  - Removes flowrate commands (e.g. F3600)
  - Removes extruder e-steps (e.g. E1.234)
    
  - Insert calls to toggle compressor (i.e Call toggle_pressure_nordson_updated P0)
  - Insert dwell G-Code after compressor start (e.g. G4 P0.15
  
  - Adds variable for print speed (mm/s)
  - Adds variable for compressor pressure (psi)
  - Adds variable for dwell time (seconds)

## How to use:

  1. Create a custom Ultimaker Cura 5.9+ printer.
  2. Fill in the proper settings:
       - XYZ dimensions can be changed according to available print volume
       - Set Build Plate Shape = Rectangular

  <img width="787" alt="Screenshot 2024-11-21 at 10 16 19 AM" src="https://github.com/user-attachments/assets/5edc7f02-27bd-4a8e-9b69-52c101404908">

  

  <img width="782" alt="Screenshot 2024-11-21 at 10 16 29 AM" src="https://github.com/user-attachments/assets/f62814e5-54a8-45d2-b93d-5d3cac7c1ba8">


  Add custom start and end G-Code to custo

  
  

## Support:

  The current custom Cura profile is for 0.20mm nozzles with a layer height and width of 0.20mm. Please change settings accordingly.
  Python script should work with any nozzle size.
