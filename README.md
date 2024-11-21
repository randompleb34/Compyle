# Compyle is a Python 3 G-Code post-processor for 3D models sliced in Ultimaker Cura 5.9+, allowing files to run on a 3-axis CNC gantry with a compressor-based hydrogel extruder.

##What it does:

  - Removes flowrate commands (e.g. F3600)
  - Removes extruder e-steps (e.g. E1.234)
    
  - Insert calls to toggle compressor (i.e Call toggle_pressure_nordson_updated P0)
  - Insert dwell G-Code after compressor start (e.g. G4 P0.15
  
  - Adds variable for print speed (mm/s)
  - Adds variable for compressor pressure (psi)
  - Adds variable for dwell time (seconds)

##How to use:

  1. Create a custom Ultimaker Cura 5.9+ printer.
  2. Define print

  

  Add custom start and end G-Code to custo
  
  

##Nozzle Support:

  The current custom Cura profile is for 0.20mm nozzles with a layer height and width of 0.20mm. Please change settings accordingly.
  Python script should work with any nozzle size.
