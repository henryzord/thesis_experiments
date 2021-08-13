# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 0 and press_type = 2 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer <= 33.5 | 1 | 0.282043 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type = 1 and humifity <= 83.5 | 1 | 0.144444 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 2 and press_type = 2 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer > 33.5 | 0 | 0.100000 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed > 2184.5 and customer != 26 and humifity > 71.0 | 1 | 0.237624 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity > 62.5 and press_speed <= 2035.0 and wax > 2.4 | 0 | 0.078838 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed <= 1495.0 | 1 | 0.109827 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 2 and press_type = 3 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer > 33.5 | 0 | 0.043636 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density = 2 and hardener <= 0.95 | 1 | 0.072289 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity <= 48.5 and blade_pressure > 19.0 and blade_pressure <= 23.5 | 1 | 0.077844 |
| paper_type != 2 and customer = 69 | 0 | 0.034783 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage > 4.25 and solvent_pct > 36.55 | 1 | 0.114943 |
| paper_type != 2 and customer != 69 and ink_type = 1 | 0 | 0.034783 |
| paper_type = 2 | 0 | 0.055319 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number > 47104.0 | 1 | 0.038281 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity <= 48.5 and blade_pressure > 19.0 and blade_pressure > 23.5 and job_number > 34529.5 | 1 | 0.070953 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity > 48.5 and roller_durometer > 33.5 and proof_cut <= 56.25 | 0 | 0.059587 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct > 18.25 | 1 | 0.037500 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed <= 1505.0 | 0 | 0.047210 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content = 1 | 0 | 0.026316 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity > 48.5 and roller_durometer <= 33.5 and customer != 62 | 1 | 0.049383 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity > 62.5 and press_speed > 2035.0 | 1 | 0.031447 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed > 2184.5 and customer != 26 and humifity <= 71.0 and press != 5 | 0 | 0.013333 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 0 and press_type = 3 and unit_number = all and viscosity <= 62.5 and blade_pressure = ? and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer <= 33.5 | 0 | 0.017699 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer = 63 | 0 | 0.013333 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed <= 1385.5 and press_speed <= 1275.0 | 0 | 0.034783 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 2 and press_type = 0 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer > 33.5 | 1 | 0.074280 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer = 58 | 0 | 0.013333 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener <= 0.55 and press != 5 | 0 | 0.030568 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 0 and press_type = 3 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer <= 33.5 | 1 | 0.101025 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity > 48.5 and roller_durometer <= 33.5 and customer = 62 | 0 | 0.010045 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity <= 48.5 and blade_pressure > 19.0 and blade_pressure > 23.5 and job_number <= 34529.5 | 0 | 0.017699 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type = 1 and humifity > 83.5 and job_number <= 47152.5 | 1 | 0.019108 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type = 1 and humifity > 83.5 and job_number > 47152.5 | 0 | 0.008929 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density = 2 and hardener > 0.95 and press_speed > 1655.0 | 1 | 0.014423 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer = 33 | 0 | 0.008929 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity > 62.5 and press_speed <= 2035.0 and wax <= 2.4 | 1 | 0.014423 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper = 14 | 0 | 0.022656 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer = 8 | 1 | 0.012821 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer = 11 | 0 | 0.008929 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature > 16.75 and cylinder_size = 3 | 0 | 0.034783 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 2 and press_type = 3 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct > 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer > 33.5 | 0 | 0.004484 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 0 and press_type = 2 and unit_number = all and viscosity > 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer <= 33.5 | 0 | 0.004505 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed > 2184.5 and customer = 26 and press != 5 | 0 | 0.013333 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density = 2 and hardener > 0.95 and press_speed <= 1655.0 | 0 | 0.008929 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press != 5 and customer != 63 and viscosity > 48.5 and roller_durometer > 33.5 and proof_cut > 56.25 | 1 | 0.008602 |
| ink_color = 1 and blade_mfg = 1 and cylinder_division = 1 and ink_type = 0 and press_type = 3 and unit_number = all and viscosity <= 62.5 and blade_pressure = all and varnish_pct = all and ink_pct <= 63.15 and solvent_pct = all and ESA_Amperage = all and roller_durometer > 33.5 | 1 | 0.029221 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener > 0.55 and customer != 21 and customer != 39 and customer != 43 and caliper != 14 and job_number <= 47104.0 and current_density != 6 and press = 5 | 1 | 0.026371 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed <= 1385.5 and press_speed > 1275.0 | 1 | 0.008602 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity <= 62.5 and press_type != 1 and press_speed <= 2184.5 and customer != 58 and press_speed > 1385.5 and press_speed > 1495.0 and ESA_Voltage <= 4.25 and customer != 11 and customer != 33 and current_density != 2 and customer != 8 and press_speed > 1505.0 and ink_temperature <= 16.75 and varnish_pct <= 18.25 and hardener <= 0.55 and press = 5 | 1 | 0.008602 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and viscosity > 62.5 and press_speed <= 2035.0 and wax > 2.4 | 0 | 0.078838 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_type = 1 and humifity <= 83.5 | 1 | 0.161491 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed > 2184.5 and job_number <= 38126.5 and humifity > 71.0 and customer != 26 | 1 | 0.266304 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press = 5 and job_number > 34704.0 and ink_temperature <= 16.200000000000003 | 1 | 0.134615 |
| paper_type = 2 | 0 | 0.093525 |
| customer = 69 | 0 | 0.059701 |
| ink_type = 1 | 0 | 0.059701 |
| chrome_content = 1 | 0 | 0.045455 |
| customer = 63 and job_number <= 35318.0 | 0 | 0.017578 |
| customer != 63 and current_density = 2 and hardener <= 0.95 | 1 | 0.133929 |
| customer != 63 and ESA_Voltage > 3.5 and varnish_pct <= 8.7 and ink_temperature > 14.25 and anode_space_ratio > 98.44 | 1 | 0.067308 |
| customer != 63 and hardener <= 0.55 and press_type != 2 | 0 | 0.054545 |
| customer != 63 and job_number > 37160.0 and hardener > 0.6499999999999999 and varnish_pct > 8.9 and type_on_cylinder != 0 | 1 | 0.133333 |
| customer != 63 and humifity <= 69.5 and plating_tank != 1 | 1 | 0.024845 |
| customer != 63 and ink_temperature > 16.45 and press_type != 0 and press_speed <= 1950.0 | 0 | 0.104167 |
| customer != 63 and viscosity <= 44.5 and humifity > 69.5 and humifity <= 83.5 and press_speed <= 1900.0 and ink_temperature <= 15.75 and press_type != 3 and humifity > 74.5 | 1 | 0.119565 |
| customer != 63 and anode_space_ratio > 109.83500000000001 and press_speed > 1800.0 | 0 | 0.062500 |
| customer != 63 and press_speed <= 1365.0 and viscosity <= 53.0 | 0 | 0.062500 |
| customer != 63 and press_speed <= 1495.0 and humifity <= 81.0 | 1 | 0.112500 |
| customer != 63 and proof_cut > 55.25 and varnish_pct > 12.5 | 1 | 0.089744 |
| customer != 63 and caliper = 12 and solvent_pct > 36.45 and job_number > 34546.0 | 1 | 0.053333 |
| customer != 63 and humifity > 84.5 and anode_space_ratio <= 106.35 and cylinder_size = 3 | 1 | 0.089744 |
| customer != 63 and humifity > 91.5 | 0 | 0.097035 |
| customer != 63 and humifity > 84.5 and humifity <= 87.5 and press_speed > 1580.0 | 1 | 0.047059 |
| customer != 63 and humifity > 86.5 | 1 | 0.077778 |
| press_speed <= 1505.0 and job_number > 36005.5 | 0 | 0.159091 |
| customer != 63 and ink_temperature > 16.35 | 0 | 0.122449 |
| customer != 63 and ink_temperature <= 16.05 and unit_number > 1.5 and press_speed > 1505.0 and job_number <= 25510.0 and job_number <= 25430.5 | 1 | 0.033962 |
| customer != 63 and ink_temperature <= 16.05 and unit_number > 1.5 and varnish_pct <= 15.4 and ESA_Voltage <= 3.5 and hardener > 0.725 and caliper != 6 and hardener > 0.95 and grain_screened != 1 and viscosity <= 55.0 | 0 | 0.276596 |
| job_number > 25510.0 and customer != 63 and ink_temperature <= 16.05 and unit_number > 1.5 and varnish_pct <= 15.4 and ESA_Voltage <= 3.5 and hardener > 0.725 and humifity <= 81.0 and cylinder_size = 2 | 0 | 0.150000 |
| customer != 63 and unit_number > 1.5 and varnish_pct <= 15.4 and hardener > 0.725 and varnish_pct > 4.65 and job_number > 34503.0 | 1 | 0.216450 |
| job_number > 25510.0 and anode_space_ratio <= 107.05000000000001 and press != 6 and press_speed > 1585.0 and humifity > 71.0 and hardener <= 0.875 | 0 | 0.250000 |
| job_number > 34079.0 and cylinder_size != 1 and anode_space_ratio <= 107.05000000000001 and job_number <= 36725.5 and anode_space_ratio <= 103.16499999999999 and humifity <= 80.5 | 0 | 0.204167 |
| customer != 63 and cylinder_size != 1 and anode_space_ratio <= 107.05000000000001 and customer != 62 | 1 | 0.451563 |
| job_number > 34549.0 | 0 | 0.625926 |
|  | 1 | 0.583333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| blade_pressure <= 42 and viscosity >= 45 and press_speed <= 1650 and job_number <= 37333 and job_number >= 23052 | 0 | 0.087078 |
| humifity >= 74 and viscosity >= 63 and press_speed <= 1800 | 0 | 0.063291 |
| press_speed <= 2180 and blade_pressure <= 42 and job_number <= 34534 and blade_pressure >= 28 and press_type = 2 | 0 | 0.063291 |
| press_speed <= 2180 and press_type = 3 and viscosity <= 52 and paper_type = 1 and viscosity >= 38 | 0 | 0.086599 |
| job_number >= 38061 and unit_number <= 7 and blade_pressure <= 33 | 0 | 0.039234 |
| type_on_cylinder = 0 and solvent_pct >= 40.7 and roller_durometer >= 38 | 0 | 0.043103 |
| press_speed <= 2100 and ink_temperature >= 17 and press_type = 2 | 0 | 0.030568 |
| ink_temperature <= 14.6 and viscosity >= 57 and roller_durometer >= 34 and proof_cut <= 50 | 0 | 0.034783 |
| wax <= 0.5 | 0 | 0.017699 |
| type_on_cylinder = 0 and ink_pct >= 58.1 and press_speed >= 1900 and plating_tank = 1 | 0 | 0.017699 |
| press_speed <= 2100 and blade_pressure <= 40 and proof_cut >= 47.5 and ink_temperature <= 15.2 and proof_cut <= 55 and ink_pct >= 52.1 | 0 | 0.018018 |
| press = 3 and press_speed <= 1950 and humifity <= 78 and job_number <= 37965 | 0 | 0.022026 |
| job_number >= 36858 and ink_pct >= 60.2 and roughness >= 0.75 and viscosity <= 48 | 0 | 0.017699 |
|  | 1 | 0.944681 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

ink_color|blade_mfg|cylinder_division|ink_type|press_type|unit_number|viscosity|blade_pressure|varnish_pct|ink_pct|solvent_pct|esa_amperage|roller_durometer|target
---|---|---|---|---|---|---|---|---|---|---|---|---|---
1|1|1|0|0|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|?|1|2|2|all|?|all|?|?|?|?|?|0
1|?|1|2|2|all|(62.5-inf)|all|?|?|?|?|?|0
1|?|1|2|0|all|?|all|?|?|?|?|?|0
1|?|1|2|2|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|0|2|all|(62.5-inf)|all|?|?|?|?|?|0
1|?|1|0|3|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|0|0|all|?|all|?|?|?|?|?|0
1|?|1|0|2|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|0|0|all|(62.5-inf)|all|?|?|?|?|?|0
1|?|1|2|0|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|1|0|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|0|0|all|(-inf-62.5]|all|?|?|?|?|?|0
1|?|1|1|3|all|(-inf-62.5]|all|?|?|?|all|(33.5-inf)|0
1|1|1|2|2|all|(62.5-inf)|all|all|(63.15-inf)|all|all|(33.5-inf)|0
1|1|1|2|1|all|(62.5-inf)|?|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|2|3|all|(-inf-62.5]|all|all|(63.15-inf)|all|all|(33.5-inf)|0
1|1|1|2|3|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|3|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|1|all|(62.5-inf)|?|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|2|1|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|1|3|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|3|all|(-inf-62.5]|all|all|(63.15-inf)|all|all|(33.5-inf)|0
1|2|1|2|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|3|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|2|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|2|0|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|?|1|2|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|1|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|1|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|2|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|2|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|2|0|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|3|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|1|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|2|1|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|0|3|all|(-inf-62.5]|all|all|(63.15-inf)|all|all|(-inf-33.5]|0
1|?|1|0|2|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|0|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|0|2|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|2|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|0|3|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|2|0|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|0|2|all|(-inf-62.5]|all|all|(63.15-inf)|all|all|(-inf-33.5]|0
1|1|1|0|1|all|(-inf-62.5]|?|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|1|0|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|0
1|1|1|0|2|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|2|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|2|0|all|(62.5-inf)|all|all|(-inf-63.15]|all|all|(-inf-33.5]|0
1|1|1|0|0|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(33.5-inf)|1
1|1|1|0|3|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|0|2|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|1
1|1|1|2|0|all|(-inf-62.5]|all|all|(-inf-63.15]|all|all|(-inf-33.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(blade_pressure <= 42) and (viscosity >= 45) and (press_speed <= 1650) and (job_number <= 37333) and (job_number >= 23052)|0 (23.0/0.0)
(humifity >= 74) and (viscosity >= 63) and (press_speed <= 1800)|0 (15.0/0.0)
(press_speed <= 2180) and (blade_pressure <= 42) and (job_number <= 34534) and (blade_pressure >= 28) and (press_type = 2)|0 (15.0/0.0)
(press_speed <= 2180) and (press_type = 3) and (viscosity <= 52) and (paper_type = 1) and (viscosity >= 38)|0 (22.0/0.0)
(job_number >= 38061) and (unit_number <= 7) and (blade_pressure <= 33)|0 (15.0/0.0)
(type_on_cylinder = 0) and (solvent_pct >= 40.7) and (roller_durometer >= 38)|0 (10.0/0.0)
(press_speed <= 2100) and (ink_temperature >= 17) and (press_type = 2)|0 (7.0/0.0)
(ink_temperature <= 14.6) and (viscosity >= 57) and (roller_durometer >= 34) and (proof_cut <= 50)|0 (9.0/0.0)
(wax <= 0.5)|0 (4.0/0.0)
(type_on_cylinder = 0) and (ink_pct >= 58.1) and (press_speed >= 1900) and (plating_tank = 1)|0 (4.0/0.0)
(press_speed <= 2100) and (blade_pressure <= 40) and (proof_cut >= 47.5) and (ink_temperature <= 15.2) and (proof_cut <= 55) and (ink_pct >= 52.1)|0 (7.0/0.0)
(press = 3) and (press_speed <= 1950) and (humifity <= 78) and (job_number <= 37965)|0 (5.0/0.0)
(job_number >= 36858) and (ink_pct >= 60.2) and (roughness >= 0.75) and (viscosity <= 48)|0 (4.0/0.0)
|1 (236.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
paper_type != 2 AND customer != 69 AND ink_type != 1 AND chrome_content != 1 AND viscosity > 62.5 AND press_speed <= 2035.0 AND wax > 2.4|0 (19.08)
paper_type != 2 AND customer != 69 AND ink_type != 1 AND chrome_content != 1 AND press_type = 1 AND humifity <= 83.5|1 (26.0)
paper_type != 2 AND customer != 69 AND ink_type != 1 AND chrome_content != 1 AND press_speed > 2184.5 AND job_number <= 38126.5 AND humifity > 71.0 AND customer != 26|1 (50.0)
paper_type != 2 AND customer != 69 AND ink_type != 1 AND chrome_content != 1 AND press = 5 AND job_number > 34704.0 AND ink_temperature <= 16.200000000000003|1 (21.11)
paper_type = 2|0 (13.0)
customer = 69|0 (8.0)
ink_type = 1|0 (8.0)
chrome_content = 1|0 (6.0)
customer = 63 AND job_number <= 35318.0|0 (4.0/1.0)
customer != 63 AND current_density = 2 AND hardener <= 0.95|1 (15.0)
customer != 63 AND ESA_Voltage > 3.5 AND varnish_pct <= 8.7 AND ink_temperature > 14.25 AND anode_space_ratio > 98.44|1 (7.88/0.88)
customer != 63 AND hardener <= 0.55 AND press_type != 2|0 (5.89)
customer != 63 AND job_number > 37160.0 AND hardener > 0.6499999999999999 AND varnish_pct > 8.9 AND type_on_cylinder != 0|1 (14.0)
customer != 63 AND humifity <= 69.5 AND plating_tank != 1|1 (7.0/3.0)
customer != 63 AND ink_temperature > 16.45 AND press_type != 0 AND press_speed <= 1950.0|0 (10.0)
customer != 63 AND viscosity <= 44.5 AND humifity > 69.5 AND humifity <= 83.5 AND press_speed <= 1900.0 AND ink_temperature <= 15.75 AND press_type != 3 AND humifity > 74.5|1 (10.12)
customer != 63 AND anode_space_ratio > 109.83500000000001 AND press_speed > 1800.0|0 (4.82)
customer != 63 AND press_speed <= 1365.0 AND viscosity <= 53.0|0 (4.9/0.08)
customer != 63 AND press_speed <= 1495.0 AND humifity <= 81.0|1 (9.22)
customer != 63 AND proof_cut > 55.25 AND varnish_pct > 12.5|1 (7.19/0.05)
customer != 63 AND caliper = 12 AND solvent_pct > 36.45 AND job_number > 34546.0|1 (4.11/0.11)
customer != 63 AND humifity > 84.5 AND anode_space_ratio <= 106.35 AND cylinder_size = 3|1 (7.0)
customer != 63 AND humifity > 91.5|0 (6.95/1.0)
customer != 63 AND humifity > 84.5 AND humifity <= 87.5 AND press_speed > 1580.0|1 (4.89/0.89)
customer != 63 AND humifity > 86.5|1 (7.73/2.0)
press_speed <= 1505.0 AND job_number > 36005.5|0 (5.86)
customer != 63 AND ink_temperature > 16.35|0 (6.82/1.0)
customer != 63 AND ink_temperature <= 16.05 AND unit_number > 1.5 AND press_speed > 1505.0 AND job_number <= 25510.0 AND job_number <= 25430.5|1 (4.91/1.91)
customer != 63 AND ink_temperature <= 16.05 AND unit_number > 1.5 AND varnish_pct <= 15.4 AND ESA_Voltage <= 3.5 AND hardener > 0.725 AND caliper != 6 AND hardener > 0.95 AND grain_screened != 1 AND viscosity <= 55.0|0 (11.51)
job_number > 25510.0 AND customer != 63 AND ink_temperature <= 16.05 AND unit_number > 1.5 AND varnish_pct <= 15.4 AND ESA_Voltage <= 3.5 AND hardener > 0.725 AND humifity <= 81.0 AND cylinder_size = 2|0 (6.06/0.34)
customer != 63 AND unit_number > 1.5 AND varnish_pct <= 15.4 AND hardener > 0.725 AND varnish_pct > 4.65 AND job_number > 34503.0|1 (9.88)
job_number > 25510.0 AND anode_space_ratio <= 107.05000000000001 AND press != 6 AND press_speed > 1585.0 AND humifity > 71.0 AND hardener <= 0.875|0 (8.0)
job_number > 34079.0 AND cylinder_size != 1 AND anode_space_ratio <= 107.05000000000001 AND job_number <= 36725.5 AND anode_space_ratio <= 103.16499999999999 AND humifity <= 80.5|0 (7.69/1.0)
customer != 63 AND cylinder_size != 1 AND anode_space_ratio <= 107.05000000000001 AND customer != 62|1 (15.38)
job_number > 34549.0|0 (11.0)
|1 (7.0/2.0)


## J48 Decision Tree

* paper_type = 2: 0 (13.0)
* paper_type != 2
	* customer = 69: 0 (8.0)
	* customer != 69
		* ink_type = 1: 0 (8.0)
		* ink_type != 1
			* chrome_content = 1: 0 (6.0)
			* chrome_content != 1
				* viscosity <= 62.5
					* press_type = 1
						* humifity <= 83.5: 1 (26.0)
						* humifity > 83.5
							* job_number <= 47152.5: 1 (3.0)
							* job_number > 47152.5: 0 (2.0)
					* press_type != 1
						* press_speed <= 2184.5
							* customer = 58: 0 (3.0)
							* customer != 58
								* press_speed <= 1385.5
									* press_speed <= 1275.0: 0 (8.15/0.15)
									* press_speed > 1275.0: 1 (3.05/1.0)
								* press_speed > 1385.5
									* press_speed <= 1495.0: 1 (19.35)
									* press_speed > 1495.0
										* ESA_Voltage <= 4.25
											* customer = 11: 0 (2.0)
											* customer != 11
												* customer = 33: 0 (2.0)
												* customer != 33
													* current_density = 2
														* hardener <= 0.95: 1 (12.0)
														* hardener > 0.95
															* press_speed <= 1655.0: 0 (2.12)
															* press_speed > 1655.0: 1 (4.23/1.0)
													* current_density != 2
														* customer = 8: 1 (2.0)
														* customer != 8
															* press_speed <= 1505.0: 0 (11.15/0.27)
															* press_speed > 1505.0
																* ink_temperature <= 16.75
																	* varnish_pct <= 18.25
																		* hardener <= 0.55
																			* press = 5: 1 (2.83/0.83)
																			* press != 5: 0 (6.9/0.05)
																		* hardener > 0.55
																			* customer = 21: 1 (2.0)
																			* customer != 21
																				* customer = 39: 1 (2.0)
																				* customer != 39
																					* customer = 43: 1 (2.0)
																					* customer != 43
																						* caliper = 14: 0 (7.71/1.31)
																						* caliper != 14
																							* job_number <= 47104.0
																								* current_density = 6: 1 (2.07/0.02)
																								* current_density != 6
																									* press = 5: 1 (5.75/0.83)
																									* press != 5
																										* customer = 63: 0 (2.84)
																										* customer != 63
																											* viscosity <= 48.5
																												* blade_pressure <= 19.0: 0 (2.05)
																												* blade_pressure > 19.0
																													* blade_pressure <= 23.5: 1 (12.41/0.32)
																													* blade_pressure > 23.5
																														* job_number <= 34529.5: 0 (3.75)
																														* job_number > 34529.5: 1 (21.08/5.46)
																											* viscosity > 48.5
																												* roller_durometer <= 33.5
																													* customer = 62: 0 (4.23/1.0)
																													* customer != 62: 1 (6.82)
																												* roller_durometer > 33.5
																													* proof_cut <= 56.25: 0 (15.38/1.0)
																													* proof_cut > 56.25: 1 (3.0/1.0)
																							* job_number > 47104.0: 1 (8.0/1.0)
																	* varnish_pct > 18.25: 1 (6.23/0.23)
																* ink_temperature > 16.75
																	* cylinder_size = 3: 0 (8.0)
																	* cylinder_size != 3: 1 (2.88/0.88)
										* ESA_Voltage > 4.25
											* solvent_pct <= 36.55: 0 (2.08)
											* solvent_pct > 36.55: 1 (20.77/0.77)
						* press_speed > 2184.5
							* customer = 26
								* press = 5: 1 (2.0)
								* press != 5: 0 (2.92)
							* customer != 26
								* humifity <= 71.0
									* press = 5: 1 (5.14)
									* press != 5: 0 (3.0)
								* humifity > 71.0: 1 (48.96)
				* viscosity > 62.5
					* press_speed <= 2035.0
						* wax <= 2.4: 1 (4.0/1.0)
						* wax > 2.4: 0 (19.08)
					* press_speed > 2035.0: 1 (5.08/0.08)


