# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed > 2180.0 | 1 | 0.251808 |
| press_type = 2 and press_speed <= 2184.5 and ink_pct <= 64 | 1 | 0.214353 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location != 4 and press != 5 and ESA_Voltage <= 4.5 and press_type != 1 and customer != 17 and press != 0 | 0 | 0.131494 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper = 10 | 0 | 0.082403 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density != 4 and press != 3 | 1 | 0.178678 |
| paper_type = 2 | 0 | 0.065217 |
| press_type = 0 and press_speed <= 2184.5 and ink_pct <= 64 | 1 | 0.099206 |
| press_type = 3 and press_speed <= 2184.5 and ink_pct <= 64 | 0 | 0.142059 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location != 4 and press != 5 and ESA_Voltage <= 4.5 and press_type = 1 | 1 | 0.050840 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content = 1 | 0 | 0.031532 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location != 4 and press = 5 and caliper = 3 and blade_pressure > 29.0 | 0 | 0.016383 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location = 4 | 0 | 0.016383 |
| press_type = 3 and press_speed <= 2184.5 and ink_pct > 64 | 0 | 0.027149 |
| paper_type != 2 and customer != 69 and ink_type = 1 | 0 | 0.036323 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location != 4 and press != 5 and ESA_Voltage > 4.5 | 1 | 0.041420 |
| paper_type != 2 and customer = 69 | 0 | 0.035874 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer = 1 | 1 | 0.024096 |
| press_type = 2 and press_speed > 2184.5 and ink_pct = ? | 0 | 0.009217 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content != 0 and paper_mill_location != 4 and press != 5 and ESA_Voltage <= 4.5 and press_type != 1 and customer = 17 | 1 | 0.019394 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer = 58 | 0 | 0.013761 |
| paper_type != 2 and customer != 69 and ink_type != 1 and chrome_content != 1 and press_speed <= 2180.0 and current_density = 4 and customer != 58 and customer != 1 and caliper != 10 and chrome_content = 0 | 0 | 0.020548 |
| press_type = 1 and press_speed <= 2184.5 and ink_pct <= 64 | 1 | 0.089489 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and customer != 69 and chrome_content != 1 and ink_type != 1 and press_speed > 2180.0 and type_on_cylinder != 0 and customer != 62 and paper_type = 1 | 1 | 0.201970 |
| paper_type != 2 and customer != 69 and chrome_content != 1 and ink_type != 1 and current_density = 2 and hardener <= 0.9 | 1 | 0.109890 |
| paper_type = 2 | 0 | 0.088757 |
| customer != 69 and chrome_content != 1 and ink_type = 1 | 0 | 0.050000 |
| customer != 69 and chrome_content != 1 and ink_temperature > 16.8 and humifity <= 79.0 and press_type = 2 | 0 | 0.055215 |
| customer != 69 and chrome_content != 1 and press_type != 3 and proof_on_ctd_ink = 1 | 1 | 0.071942 |
| customer != 69 and chrome_content != 1 and press = 7 | 1 | 0.063087 |
| customer != 69 and chrome_content != 1 and press = 0 and hardener > 0.9 and type_on_cylinder != 0 and ink_temperature > 14.7 | 1 | 0.071942 |
| customer = 69 | 0 | 0.061069 |
| chrome_content != 1 and press_type = 1 and humifity <= 78.0 and hardener <= 0.85 | 1 | 0.062016 |
| chrome_content != 1 and chrome_content != 0 and customer = 62 and ink_temperature <= 14.9 | 1 | 0.069930 |
| chrome_content != 1 and chrome_content != 0 and caliper = 10 and press != 3 and grain_screened != 1 and plating_tank = 1 | 1 | 0.022769 |
| chrome_content != 1 and chrome_content != 0 and caliper = 10 and ink_type != 0 | 0 | 0.137931 |
| chrome_content != 1 and ESA_Voltage > 4.0 and varnish_pct <= 1.2 | 1 | 0.070796 |
| chrome_content != 1 and chrome_content != 0 and cylinder_size = 2 | 0 | 0.072886 |
| chrome_content != 1 and chrome_content != 0 and caliper != 15 and press_speed > 1300.0 and paper_type != 1 and press != 2 and ESA_Voltage <= 3.0 and caliper != 12 and press = 4 and unit_number > 2.0 | 0 | 0.098856 |
| chrome_content != 1 and chrome_content != 0 and press = 4 and viscosity <= 47.0 | 1 | 0.125000 |
| chrome_content != 1 and chrome_content != 0 and paper_type != 1 and press != 2 and caliper != 12 and ink_type = 0 and plating_tank != 1 | 1 | 0.096774 |
| chrome_content != 1 and ink_temperature > 16.4 | 0 | 0.116346 |
| chrome_content != 1 and press = 3 and humifity <= 75.0 | 0 | 0.134146 |
| chrome_content != 1 and current_density != 4 and ink_temperature > 14.3 and hardener > 0.9 | 1 | 0.090074 |
| chrome_content != 1 and press = 2 and ink_pct > 57.7 | 0 | 0.158835 |
| chrome_content != 1 and proof_cut > 52.0 and customer != 52 | 1 | 0.115385 |
| chrome_content != 1 and proof_cut <= 52.0 and grain_screened = 1 and roughness > 0.625 and customer != 47 and wax > 2.4 | 1 | 0.052174 |
| chrome_content != 1 and proof_cut <= 52.0 and paper_mill_location = 0 | 1 | 0.151629 |
| chrome_content != 1 and proof_cut <= 52.0 and paper_type = 1 | 0 | 0.226852 |
| chrome_content != 1 and proof_cut > 52.0 | 1 | 0.148352 |
| chrome_content != 1 and ink_type = 0 | 1 | 0.201681 |
| chrome_content != 1 and hardener > 0.9 and cylinder_size = 1 | 0 | 0.380952 |
| chrome_content != 1 and press_type != 2 | 1 | 0.302867 |
| press_speed <= 1800.0 | 0 | 0.764706 |
|  | 0 | 0.714286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| press_speed <= 2180 and blade_pressure <= 40 and ink_temperature >= 17 and viscosity >= 41 | 0 | 0.093003 |
| hardener >= 1 and job_number <= 37335 and roughness <= 0.625 and job_number >= 34092 and press_speed <= 1850 | 0 | 0.088983 |
| press_speed <= 2180 and press_type = 3 and humifity <= 78 and job_number <= 36648 | 0 | 0.073276 |
| press_speed <= 2100 and blade_pressure <= 42 and current_density = 4 and blade_pressure >= 22 and ink_temperature <= 14.8 and ink_temperature >= 14.1 | 0 | 0.053178 |
| press_speed <= 2100 and humifity >= 76 and roughness >= 0.625 and current_density = 4 and viscosity >= 47 and blade_pressure <= 35 and roller_durometer >= 34 and varnish_pct <= 17.1 | 0 | 0.089661 |
| press_speed <= 2100 and hardener >= 1 and unit_number <= 7 and anode_space_ratio <= 103.13 and humifity >= 90 | 0 | 0.031532 |
| press_speed <= 2100 and current_density = 4 and blade_pressure >= 26 and press_type = 2 and job_number <= 34692 | 0 | 0.040179 |
| job_number >= 38064 and ink_temperature >= 16 and humifity >= 75 and roughness >= 0.3125 | 0 | 0.036323 |
| current_density = 4 and press_speed <= 2150 and paper_type = 1 and press_type = 3 and viscosity <= 52 and unit_number <= 7 | 0 | 0.035874 |
| job_number >= 37001 and job_number <= 37335 and roller_durometer <= 30 | 0 | 0.018265 |
| anode_space_ratio >= 106 and roughness >= 1 and hardener <= 1 and paper_type = 1 | 0 | 0.013761 |
| viscosity >= 62 and press_type = 0 | 0 | 0.009217 |
| ink_type = 2 and plating_tank = 2 and hardener >= 1 and humifity <= 72 and type_on_cylinder = 1 | 0 | 0.027149 |
| job_number >= 37502 and roughness >= 0.8125 and ink_temperature <= 15 and anode_space_ratio >= 100 | 0 | 0.018265 |
|  | 1 | 0.942982 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

press_type|press_speed|ink_pct|target
---|---|---|---
2|(2184.5-inf)|?|0
0|(-inf-2184.5]|?|0
3|(-inf-2184.5]|?|0
2|(-inf-2184.5]|?|0
3|(-inf-2184.5]|(64-inf)|0
1|?|(-inf-64]|0
3|?|(-inf-64]|0
2|?|(-inf-64]|1
3|(2184.5-inf)|(-inf-64]|1
2|(2184.5-inf)|(-inf-64]|1
1|(-inf-2184.5]|(-inf-64]|1
3|(-inf-2184.5]|(-inf-64]|0
0|(-inf-2184.5]|(-inf-64]|1
2|(-inf-2184.5]|(-inf-64]|1

## JRip

Decision list:

rules | predicted class
---|---
(press_speed <= 2180) and (blade_pressure <= 40) and (ink_temperature >= 17) and (viscosity >= 41)|0 (20.0/0.0)
(hardener >= 1) and (job_number <= 37335) and (roughness <= 0.625) and (job_number >= 34092) and (press_speed <= 1850)|0 (21.0/0.0)
(press_speed <= 2180) and (press_type = 3) and (humifity <= 78) and (job_number <= 36648)|0 (18.0/0.0)
(press_speed <= 2100) and (blade_pressure <= 42) and (current_density = 4) and (blade_pressure >= 22) and (ink_temperature <= 14.8) and (ink_temperature >= 14.1)|0 (13.0/0.0)
(press_speed <= 2100) and (humifity >= 76) and (roughness >= 0.625) and (current_density = 4) and (viscosity >= 47) and (blade_pressure <= 35) and (roller_durometer >= 34) and (varnish_pct <= 17.1)|0 (15.0/0.0)
(press_speed <= 2100) and (hardener >= 1) and (unit_number <= 7) and (anode_space_ratio <= 103.13) and (humifity >= 90)|0 (8.0/0.0)
(press_speed <= 2100) and (current_density = 4) and (blade_pressure >= 26) and (press_type = 2) and (job_number <= 34692)|0 (11.0/0.0)
(job_number >= 38064) and (ink_temperature >= 16) and (humifity >= 75) and (roughness >= 0.3125)|0 (11.0/0.0)
(current_density = 4) and (press_speed <= 2150) and (paper_type = 1) and (press_type = 3) and (viscosity <= 52) and (unit_number <= 7)|0 (8.0/0.0)
(job_number >= 37001) and (job_number <= 37335) and (roller_durometer <= 30)|0 (4.0/0.0)
(anode_space_ratio >= 106) and (roughness >= 1) and (hardener <= 1) and (paper_type = 1)|0 (4.0/0.0)
(viscosity >= 62) and (press_type = 0)|0 (3.0/0.0)
(ink_type = 2) and (plating_tank = 2) and (hardener >= 1) and (humifity <= 72) and (type_on_cylinder = 1)|0 (6.0/0.0)
(job_number >= 37502) and (roughness >= 0.8125) and (ink_temperature <= 15) and (anode_space_ratio >= 100)|0 (4.0/0.0)
|1 (231.0/16.0)


## PART

Decision list:

rules | predicted class
---|---
paper_type != 2 AND customer != 69 AND chrome_content != 1 AND ink_type != 1 AND press_speed > 2180.0 AND type_on_cylinder != 0 AND customer != 62 AND paper_type = 1|1 (40.72)
paper_type != 2 AND customer != 69 AND chrome_content != 1 AND ink_type != 1 AND current_density = 2 AND hardener <= 0.9|1 (20.11)
paper_type = 2|0 (15.0)
customer != 69 AND chrome_content != 1 AND ink_type = 1|0 (10.0/1.0)
customer != 69 AND chrome_content != 1 AND ink_temperature > 16.8 AND humifity <= 79.0 AND press_type = 2|0 (9.0)
customer != 69 AND chrome_content != 1 AND press_type != 3 AND proof_on_ctd_ink = 1|1 (10.79/0.67)
customer != 69 AND chrome_content != 1 AND press = 7|1 (13.76/2.88)
customer != 69 AND chrome_content != 1 AND press = 0 AND hardener > 0.9 AND type_on_cylinder != 0 AND ink_temperature > 14.7|1 (9.56)
customer = 69|0 (8.0)
chrome_content != 1 AND press_type = 1 AND humifity <= 78.0 AND hardener <= 0.85|1 (8.0)
chrome_content != 1 AND chrome_content != 0 AND customer = 62 AND ink_temperature <= 14.9|1 (11.0/1.0)
chrome_content != 1 AND chrome_content != 0 AND caliper = 10 AND press != 3 AND grain_screened != 1 AND plating_tank = 1|1 (9.27/4.58)
chrome_content != 1 AND chrome_content != 0 AND caliper = 10 AND ink_type != 0|0 (13.64/0.56)
chrome_content != 1 AND ESA_Voltage > 4.0 AND varnish_pct <= 1.2|1 (8.54/0.54)
chrome_content != 1 AND chrome_content != 0 AND cylinder_size = 2|0 (12.38/4.0)
chrome_content != 1 AND chrome_content != 0 AND caliper != 15 AND press_speed > 1300.0 AND paper_type != 1 AND press != 2 AND ESA_Voltage <= 3.0 AND caliper != 12 AND press = 4 AND unit_number > 2.0|0 (11.47/1.0)
chrome_content != 1 AND chrome_content != 0 AND press = 4 AND viscosity <= 47.0|1 (11.23/0.23)
chrome_content != 1 AND chrome_content != 0 AND paper_type != 1 AND press != 2 AND caliper != 12 AND ink_type = 0 AND plating_tank != 1|1 (9.0)
chrome_content != 1 AND ink_temperature > 16.4|0 (11.99/1.04)
chrome_content != 1 AND press = 3 AND humifity <= 75.0|0 (10.8)
chrome_content != 1 AND current_density != 4 AND ink_temperature > 14.3 AND hardener > 0.9|1 (8.57/1.39)
chrome_content != 1 AND press = 2 AND ink_pct > 57.7|0 (13.72)
chrome_content != 1 AND proof_cut > 52.0 AND customer != 52|1 (12.9/2.85)
chrome_content != 1 AND proof_cut <= 52.0 AND grain_screened = 1 AND roughness > 0.625 AND customer != 47 AND wax > 2.4|1 (11.65/5.65)
chrome_content != 1 AND proof_cut <= 52.0 AND paper_mill_location = 0|1 (13.62/3.08)
chrome_content != 1 AND proof_cut <= 52.0 AND paper_type = 1|0 (10.08/3.46)
chrome_content != 1 AND proof_cut > 52.0|1 (9.72/0.56)
chrome_content != 1 AND ink_type = 0|1 (8.58/2.24)
chrome_content != 1 AND hardener > 0.9 AND cylinder_size = 1|0 (8.16/1.0)
chrome_content != 1 AND press_type != 2|1 (9.88/2.0)
press_speed <= 1800.0|0 (8.39)
|0 (7.48/3.69)


## J48 Decision Tree

* paper_type = 2: 0 (14.0)
* paper_type != 2
	* customer = 69: 0 (8.0)
	* customer != 69
		* ink_type = 1: 0 (8.0)
		* ink_type != 1
			* chrome_content = 1: 0 (6.02)
			* chrome_content != 1
				* press_speed <= 2180.0
					* current_density = 4
						* customer = 58: 0 (3.0)
						* customer != 58
							* customer = 1: 1 (3.0)
							* customer != 1
								* caliper = 10: 0 (28.3/4.27)
								* caliper != 10
									* chrome_content = 0: 0 (7.83/1.8)
									* chrome_content != 0
										* paper_mill_location = 4: 0 (5.59/0.65)
										* paper_mill_location != 4
											* press = 5
												* caliper = 3
													* blade_pressure <= 29.0: 1 (3.0)
													* blade_pressure > 29.0: 0 (4.69/1.37)
												* caliper != 3: 1 (9.94/0.46)
											* press != 5
												* ESA_Voltage <= 4.5
													* press_type = 1: 1 (12.93/2.96)
													* press_type != 1
														* customer = 17: 1 (4.89/0.96)
														* customer != 17
															* press = 0: 1 (20.69/5.8)
															* press != 0: 0 (82.16/38.36)
												* ESA_Voltage > 4.5: 1 (7.16/0.27)
					* current_density != 4
						* press = 3: 0 (6.0/2.0)
						* press != 3: 1 (44.42/5.41)
				* press_speed > 2180.0: 1 (60.39/5.0)


