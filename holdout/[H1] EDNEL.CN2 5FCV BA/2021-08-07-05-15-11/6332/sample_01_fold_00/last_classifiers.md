# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and press_type != 1 and press_speed > 2025.0 | 1 | 0.274407 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed > 1325.0 and solvent_pct <= 41.8 and ink_pct <= 63.3 and wax <= 2.725 and press != 2 | 1 | 0.153841 |
| paper_type = 2 | 0 | 0.073276 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed > 1325.0 and solvent_pct <= 41.8 and ink_pct <= 63.3 and wax > 2.725 | 1 | 0.145161 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature > 16.9 | 0 | 0.068242 |
| paper_type != 2 and press_type = 1 | 1 | 0.140801 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed > 1325.0 and solvent_pct > 41.8 | 0 | 0.048395 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed > 1325.0 and solvent_pct <= 41.8 and ink_pct <= 63.3 and wax <= 2.725 and press = 2 | 0 | 0.048395 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed <= 1325.0 | 0 | 0.040179 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener <= 0.35 | 0 | 0.032032 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press != 5 and press_speed > 1325.0 and solvent_pct <= 41.8 and ink_pct > 63.3 | 0 | 0.031532 |
| paper_type != 2 and press_type != 1 and press_speed <= 2025.0 and ink_temperature <= 16.9 and hardener > 0.35 and press = 5 | 1 | 0.069376 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and press_type != 1 and press_speed > 2184.5 | 1 | 0.237957 |
| paper_type != 2 and press_type = 1 | 1 | 0.140801 |
| paper_type != 2 and press != 5 and chrome_content = 2 and press != 7 and proof_cut > 55.25 | 1 | 0.099064 |
| paper_type != 2 and press = 5 | 1 | 0.072631 |
| paper_type = 2 | 0 | 0.163462 |
| press != 7 and current_density = 2 and viscosity > 54.5 | 0 | 0.067726 |
| current_density != 2 and blade_pressure > 21.0 and unit_number > 1.5 and press != 4 and job_number > 34567.0 and type_on_cylinder != 0 and job_number <= 37342.0 | 0 | 0.243056 |
| unit_number > 1.5 and current_density != 2 and grain_screened != 1 and blade_pressure > 21.0 and wax <= 2.95 | 0 | 0.284140 |
| unit_number > 1.5 and current_density != 2 and type_on_cylinder != 0 and press != 0 and ESA_Voltage <= 0.5 | 1 | 0.316561 |
| unit_number > 1.5 and current_density = 4 and humifity > 70.5 and type_on_cylinder = 0 | 0 | 0.274363 |
| unit_number > 1.5 and press = 0 | 1 | 0.296296 |
| unit_number > 1.5 and current_density = 4 | 0 | 0.322955 |
| unit_number > 1.5 | 1 | 0.685890 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| press_speed <= 2100 and blade_pressure >= 22 and ink_type = 2 and press_type = 2 and wax <= 2.4 | 0 | 0.073276 |
| press_type = 3 and press_speed <= 1673 and roller_durometer >= 34 | 0 | 0.104167 |
| press_speed <= 2180 and job_number <= 37333 and current_density = 4 and viscosity >= 47 and press = 2 and job_number >= 34551 | 0 | 0.053965 |
| press_speed <= 2100 and blade_pressure >= 22 and unit_number <= 7 and wax <= 2.6 and wax >= 2.5 and unit_number >= 7 and job_number <= 25520 | 0 | 0.044444 |
| press_speed <= 2200 and blade_pressure >= 30 and unit_number <= 7 and press_speed >= 1640 and humifity <= 73 and ink_temperature >= 15 and wax >= 2.2 | 0 | 0.048395 |
| press_speed <= 2180 and humifity >= 81 and viscosity >= 59 and ink_temperature <= 15 | 0 | 0.040584 |
| press_speed <= 2180 and humifity >= 75 and viscosity <= 52 and paper_type = 1 and viscosity >= 42 and anode_space_ratio >= 100 | 0 | 0.049013 |
| press_type = 0 and viscosity >= 62 | 0 | 0.031532 |
| paper_type = 2 | 0 | 0.027149 |
| ink_temperature <= 14.5 and customer = 47 and press_speed >= 1850 | 0 | 0.022727 |
| press_type = 3 and humifity <= 76 and paper_type = 1 and job_number >= 34551 | 0 | 0.013761 |
| ink_temperature <= 14.3 and blade_pressure >= 30 and grain_screened = 2 and job_number >= 34272 and job_number <= 47106 | 0 | 0.028322 |
| ink_temperature >= 16.4 and job_number <= 35462 and anode_space_ratio >= 103.125 and humifity >= 75 | 0 | 0.022727 |
| press_speed >= 1900 and press_speed <= 2000 and viscosity <= 52 and humifity >= 78 and humifity <= 85 and viscosity >= 38 | 0 | 0.035874 |
|  | 1 | 0.926724 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(press_speed <= 2100) and (blade_pressure >= 22) and (ink_type = 2) and (press_type = 2) and (wax <= 2.4)|0 (15.0/0.0)
(press_type = 3) and (press_speed <= 1673) and (roller_durometer >= 34)|0 (22.0/0.0)
(press_speed <= 2180) and (job_number <= 37333) and (current_density = 4) and (viscosity >= 47) and (press = 2) and (job_number >= 34551)|0 (14.0/0.0)
(press_speed <= 2100) and (blade_pressure >= 22) and (unit_number <= 7) and (wax <= 2.6) and (wax >= 2.5) and (unit_number >= 7) and (job_number <= 25520)|0 (10.0/0.0)
(press_speed <= 2200) and (blade_pressure >= 30) and (unit_number <= 7) and (press_speed >= 1640) and (humifity <= 73) and (ink_temperature >= 15) and (wax >= 2.2)|0 (14.0/0.0)
(press_speed <= 2180) and (humifity >= 81) and (viscosity >= 59) and (ink_temperature <= 15)|0 (10.0/0.0)
(press_speed <= 2180) and (humifity >= 75) and (viscosity <= 52) and (paper_type = 1) and (viscosity >= 42) and (anode_space_ratio >= 100)|0 (12.0/0.0)
(press_type = 0) and (viscosity >= 62)|0 (7.0/0.0)
(paper_type = 2)|0 (7.0/0.0)
(ink_temperature <= 14.5) and (customer = 47) and (press_speed >= 1850)|0 (6.0/0.0)
(press_type = 3) and (humifity <= 76) and (paper_type = 1) and (job_number >= 34551)|0 (5.0/0.0)
(ink_temperature <= 14.3) and (blade_pressure >= 30) and (grain_screened = 2) and (job_number >= 34272) and (job_number <= 47106)|0 (9.0/0.0)
(ink_temperature >= 16.4) and (job_number <= 35462) and (anode_space_ratio >= 103.125) and (humifity >= 75)|0 (5.0/0.0)
(press_speed >= 1900) and (press_speed <= 2000) and (viscosity <= 52) and (humifity >= 78) and (humifity <= 85) and (viscosity >= 38)|0 (8.0/0.0)
|1 (233.0/18.0)


## PART

Decision list:

rules | predicted class
---|---
paper_type != 2 AND press_type != 1 AND press_speed > 2184.5|1 (68.04/9.0)
paper_type != 2 AND press_type = 1|1 (34.0/4.0)
paper_type != 2 AND press != 5 AND chrome_content = 2 AND press != 7 AND proof_cut > 55.25|1 (30.67/7.13)
paper_type != 2 AND press = 5|1 (23.0/6.0)
paper_type = 2|0 (17.0)
press != 7 AND current_density = 2 AND viscosity > 54.5|0 (10.37/4.17)
current_density != 2 AND blade_pressure > 21.0 AND unit_number > 1.5 AND press != 4 AND job_number > 34567.0 AND type_on_cylinder != 0 AND job_number <= 37342.0|0 (43.12/9.55)
unit_number > 1.5 AND current_density != 2 AND grain_screened != 1 AND blade_pressure > 21.0 AND wax <= 2.95|0 (38.6/3.4)
unit_number > 1.5 AND current_density != 2 AND type_on_cylinder != 0 AND press != 0 AND ESA_Voltage <= 0.5|1 (40.3/11.2)
unit_number > 1.5 AND current_density = 4 AND humifity > 70.5 AND type_on_cylinder = 0|0 (22.71/6.86)
unit_number > 1.5 AND press = 0|1 (14.4/0.23)
unit_number > 1.5 AND current_density = 4|0 (13.38/6.08)
unit_number > 1.5|1 (12.39/0.32)
|0 (9.0)


## J48 Decision Tree

* paper_type = 2: 0 (13.0)
* paper_type != 2
	* press_type = 1: 1 (28.0/3.0)
	* press_type != 1
		* press_speed <= 2025.0
			* ink_temperature <= 16.9
				* hardener <= 0.35: 0 (8.1/1.0)
				* hardener > 0.35
					* press = 5: 1 (12.0/1.0)
					* press != 5
						* press_speed <= 1325.0: 0 (7.1/0.15)
						* press_speed > 1325.0
							* solvent_pct <= 41.8
								* ink_pct <= 63.3
									* wax <= 2.725
										* press = 2: 0 (10.69/2.0)
										* press != 2: 1 (63.75/28.5)
									* wax > 2.725: 1 (33.66/6.3)
								* ink_pct > 63.3: 0 (6.14)
							* solvent_pct > 41.8: 0 (13.31/2.0)
			* ink_temperature > 16.9: 0 (20.12/3.12)
		* press_speed > 2025.0: 1 (67.11/12.0)


