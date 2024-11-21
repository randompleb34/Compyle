# Compyl

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

     **Printer Tab:**
     
     Printer Settings:

       - XYZ dimensions can be changed according to available print volume
       - Set Build Plate Shape = **Rectangular**
       - Origin at Center = **OFF**
       - Heated Bed = **OFF**
       - Heated Build Volume = **OFF**
       - G-Code Flavor = **Marlin**
     
     Printhead Settings:
       
       - Apply Extruder Offset to G-Code = **OFF**
       - Leave all else = **default**
     
     Start G-code:
         Copy and paste the Start G-Code below:

     <details>
          <summary>Start G-Code</summary>
       
          DVAR $hFile
          DVAR $cCheck
          DVAR $press
          DVAR $length
          DVAR $lame
          DVAR $comport
          DVAR $vacpress
          DVAR $FORLOOP
          DVAR $OUTER
          DVAR $Xnow
          DVAR $Ynow
          DVAR $Znow
          DVAR $Cnow
          DVAR $Bnow
          DVAR $Anow
          DVAR $Var1
          DVAR $Var2
          DVAR $Var3
          DVAR $Var4
          DVAR $Var5
          DVAR $Var6
          DVAR $Var7
          DVAR $Var8
          DVAR $Var9
          DVAR $Pos
          DVAR $Pre
          DVAR $alicatFiles[2]
          DVAR $nordsonFiles[2]
          
          
          
          $DO0.0=0
          $DO1.0=0
          $DO2.0=0
          $DO3.0=0
          
          Primary ;
          G65 F2000; accel speed mm/s^2
          G66 F2000;accel speed mm/s^2
          
          
          Call open_communication_nordson_updated P0 Q31
          G90 ;absolute
          G92 X0.000000 Y0.000000 ;set home
          ;Setting units to mm/s
          G76
          G1 F20.0
          Call set_pressure_nordson_updated P0 Q65.0
          
          ;Translater Call ID
  
     </details>
     

        End G-code
             Copy and paste the Start G-Code below:

            G1 X0.000000 Y0.000000
            G91 ;relative
            G1 Z0.200000
            G90 ;absolute
            Call close_communication_nordson_updated P0
            ;#################################### Code ##########################################
            
            M2
            
            ;##########Functions############;
            DFS setPress
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
                    $press = $Q * 10.0
                    $strtask2 = DBLTOSTR( $press , 0 )
            
            
                    $length = STRLEN( $strtask2 )
                    WHILE $length < 4.0
                            $strtask2 = "0" + $strtask2
                            $length = STRLEN( $strtask2 )
                    ENDWHILE
            
            
                    $strtask2 = "08PS  " + $strtask2
            
                    $cCheck = 0.00
                    $lame = STRTOASCII ($strtask2, 0)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 1)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 2)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 3)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 4)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 5)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 6)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 7)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 8)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 9)
                    $cCheck = $cCheck - $lame
            
                    WHILE( $cCheck) < 0
                            $cCheck = $cCheck + 256
                    ENDWHILE
            
            
                    $strtask3 = makestring "{#H}" $cCheck
                    $strtask3 = STRUPR( $strtask3 )
                    $strtask2 = "\x02" + $strtask2 + $strtask3 + "\x03"
            
                    FILEWRITE $hFile "\x05"
                    FILEWRITE $hFile $strtask2
                    FILEWRITE $hFile "\x04"
            
            
                    FILECLOSE $hFile
            
            
            ENDDFS
            
            DFS setVac
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
                    $vacpress = $Q * 10.0
                    $strtask2 = DBLTOSTR( $vacpress , 0 )
            
            
                    $length = STRLEN( $strtask2 )
                    WHILE $length < 4.0
                            $strtask2 = "0" + $strtask2
                            $length = STRLEN( $strtask2 )
                    ENDWHILE
            
            
                    $strtask2 = "08VS  " + $strtask2
            
                    $cCheck = 0.00
                    $lame = STRTOASCII ($strtask2, 0)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 1)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 2)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 3)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 4)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 5)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 6)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 7)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 8)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 9)
                    $cCheck = $cCheck - $lame
            
                    WHILE( $cCheck) < 0
                            $cCheck = $cCheck + 256
                    ENDWHILE
            
            
                    $strtask3 = makestring "{#H}" $cCheck
                    $strtask3 = STRUPR( $strtask3 )
                    $strtask2 = "\x02" + $strtask2 + $strtask3 + "\x03"
            
                    FILEWRITE $hFile "\x05"
                    FILEWRITE $hFile $strtask2
                    FILEWRITE $hFile "\x04"
            
            
                    FILECLOSE $hFile
            
            
            ENDDFS
            
            DFS togglePress
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
            
                    $strtask2 = "04DI  "
            
                    $cCheck = 0.00
                    $lame = STRTOASCII ($strtask2, 0)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 1)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 2)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 3)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 4)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 5)
                    $cCheck = $cCheck - $lame
            
                    WHILE( $cCheck) < 0
                            $cCheck = $cCheck + 256
                    ENDWHILE
            
            
                    $strtask3 = makestring "{#H}" $cCheck
                    $strtask3 = STRUPR( $strtask3 )
                    $strtask2 = "\x02" + $strtask2 + $strtask3 + "\x03"
            
                    FILEWRITE $hFile "\x05"
                    FILEWRITE $hFile $strtask2
                    FILEWRITE $hFile "\x04"
            
            
                    FILECLOSE $hFile
                    G4 P0.15
            
            ENDDFS
            
            DFS open_communication_nordson_updated
                    $strtask2 = DBLTOSTR( $Q, 0 )
                    $strtask2 = "\\.\COM" + $strtask2
                    $hFile = FILEOPEN $strtask2, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    $nordsonFiles[$P] = $hFile
            ENDDFS
            
            DFS close_communication_nordson_updated
                    FILECLOSE $nordsonFiles[$P]
            ENDDFS
            
            DFS set_pressure_nordson_updated
                    $press = $Q * 10.0
                    $strtask2 = DBLTOSTR( $press , 0 )
            
                    $length = STRLEN( $strtask2 )
                    WHILE $length < 4.0
                            $strtask2 = "0" + $strtask2
                            $length = STRLEN( $strtask2 )
                    ENDWHILE
            
            
                    $strtask2 = "08PS  " + $strtask2
            
                    $cCheck = 0.00
                    $lame = STRTOASCII ($strtask2, 0)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 1)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 2)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 3)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 4)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 5)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 6)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 7)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 8)
                    $cCheck = $cCheck - $lame
                    $lame = STRTOASCII( $strtask2, 9)
                    $cCheck = $cCheck - $lame
            
                    WHILE( $cCheck) < 0
                            $cCheck = $cCheck + 256
                    ENDWHILE
            
            
                    $strtask3 = makestring "{#H}" $cCheck
                    $strtask3 = STRUPR( $strtask3 )
                    $strtask2 = "\x02" + $strtask2 + $strtask3 + "\x03"
            
                    $hFile = $nordsonFiles[$P]
                    FILEWRITE $hFile "\x05"
                    FILEWRITE $hFile $strtask2
                    FILEWRITE $hFile "\x04"
            ENDDFS
            
            DFS toggle_pressure_nordson_updated
                    $strtask2 = "\x02" + "04DI  CF" + "\x03"
                    $hFile = $nordsonFiles[$P]
                    FILEWRITE $hFile "\x05"
                    FILEWRITE $hFile $strtask2
                    FILEWRITE $hFile "\x04"
            ENDDFS
            
            DFS open_communication_alicat_updated
                    $strtask2 = DBLTOSTR( $Q, 0 )
                    $strtask2 = "\\.\COM" + $strtask2
                    $hFile = FILEOPEN $strtask2, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    $alicatFiles[$P] = $hFile
            ENDDFS
            
            DFS close_communication_alicat_updated
                    FILECLOSE $alicatFiles[$P]
            ENDDFS
            
            DFS set_pressure_alicat_updated
                    $strtask2 = DBLTOSTR( $Q , 2 )
                    $strtask2 =  "As" + $strtask2 + "\x0D"
                    $hFile = $alicatFiles[$P]
                    FILEWRITENOTERM $hFile $strtask2
            ENDDFS
            
            DFS read_alicat
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
            
                    $strtask2 =  "A"
            
            
            		'FILEWRITE $hFile $strtask2
            		FILEWRITENOTERM $hFile $strtask2
            		FILEWRITENOTERM $hFile "\x0D"
            
            		DWELL 0.005
            		FILEREAD $hFile, 4, $Var1,$Var2,$Var3,$Var4,$Var5,$Var6,$Var7,$Var8,$Var9
            
            
            
                    FILECLOSE
            ENDDFS
            
            DFS setPress_alicat
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
                    $press = $Q
            
            		$strtask2 = DBLTOSTR( $press , 0 )
            
                    $strtask2 =  "As" + $strtask2
            
            
                    FILEWRITENOTERM $hFile $strtask2
            		FILEWRITENOTERM $hFile "\x0D"
            
            
            
            
                    FILECLOSE
            
            
            ENDDFS
            
            DFS close_valve_alicat
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
                    $strtask2 =  "AE"
            
            
                    FILEWRITENOTERM $hFile $strtask2
            		FILEWRITENOTERM $hFile "\x0D"
            
            
            
            
                    FILECLOSE
            
            
            ENDDFS
            
            DFS open_valve_alicat
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
            
                    $strtask2 =  "AC"
            
            
                    FILEWRITENOTERM $hFile $strtask2
            		FILEWRITENOTERM $hFile "\x0D"
            
            
            
            
                    FILECLOSE
            
            
            ENDDFS
            
            
            
            DFS pressure_on_D3
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "31"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 1
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_off_D3
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "30"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 0
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_on_D4
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "41"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 1
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_off_D4
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "40"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 0
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_on_D5
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "51"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 1
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_off_D5
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "50"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 0
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_on_D6
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "61"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 1
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_off_D6
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "60"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 0
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_on_D7
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "71"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 1
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
            
            DFS pressure_off_D7
            
                    $strtask1 = DBLTOSTR( $P, 0 )
                    $strtask1 = "\\.\COM" + $strtask1
                    $hFile = FILEOPEN $strtask1, 2
                    COMMINIT $hFile, "baud=115200 parity=N data=8 stop=1"
                    COMMSETTIMEOUT $hFile, -1, -1, 1000
                    DWELL 2
                    $strtask2 =  "70"
            		FILEWRITE $hFile $strtask2
                    //FILEWRITENOTERM $hFile $strtask2
            		//FILEWRITENOTERM $hFile "\x0D"
                    DWELL 0.5
            		FILEREAD $hFile, 0, $global[0]
            		WHILE $global[0] != 0
            			FILEWRITE $hFile $strtask2
            			DWELL 0.5
            			FILEREAD $hFile, 0, $global[0]
            		ENDWHILE
            		FILECLOSE
            ENDDFS
     
     <img width="787" alt="Screenshot 2024-11-21 at 10 16 19 AM" src="https://github.com/user-attachments/assets/5edc7f02-27bd-4a8e-9b69-52c101404908">
     
     **Extruder 1 Tab:**
         Nozzle Settings:
             - Nozzle Size = **0.2**
             - Leave all else = **default**

     <img width="782" alt="Screenshot 2024-11-21 at 10 16 29 AM" src="https://github.com/user-attachments/assets/f62814e5-54a8-45d2-b93d-5d3cac7c1ba8">

  3. Slice the file like normal and export as G-Code.
         Note: Make sure to turn of print cooling fan setting.
  6. Using Compyle, input the name of your orginal file under **#Main Program** and change variables accordingly:

         #Main Program
         import_file = 'BenchyTest.gcode' # original G-Code filename
         export_file = 'newgcode.txt' # new G-Code filename
         v = 20.0 # speed [mm/s]
         pressure = 65.0 # psi
         dwell = 0.15 # seconds

  7. Check your new G-Code in a text-viewer or G-Code visualizer

## Nozzle Support:

  The current custom Cura profile is for 0.20mm nozzles with a layer height and width of 0.20mm. Please change settings accordingly.
  Python script should work with any nozzle size.
