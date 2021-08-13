# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.586207 |
| paper_type != 2 and customer != 69 and ink_type != 1 and customer != 58 and current_density != 2 and press != 2 and customer != 68 and ink_temperature <= 16.8 and chrome_content != 0 and customer != 5 and press != 4 and press != 3 and cylinder_size != 2 and ink_type != 0 and press_type != 2 and proof_cut <= 50.0 and humifity > 78.0 | 0 | 0.022756 |
| customer != 17 and current_density!=(6) | 0 | 0.405983 |
| customer = 17 and customer != 62 and press != 0 and caliper != 19 | 0 | 0.013393 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and current_density != 3 and current_density = 2 and customer != 67 | 1 | 0.170369 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and press = 2 and press_speed <= 1625.0 | 0 | 0.073892 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and press != 4 and customer != 58 and customer != 1 and customer != 10 and customer != 43 and customer != 68 and current_density != 6 and caliper != 14 and press_type = 1 and caliper != 6 | 1 | 0.107928 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and ESA_Voltage <= 4.25 and customer != 10 and current_density != 6 and press_speed > 2184.5 and type_on_cylinder != 0 | 1 | 0.160920 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and customer != 10 and ink_type != 1 and customer != 1 and ESA_Voltage > 4.25 | 1 | 0.145688 |
| paper_type != 2 and customer != 10 and customer != 1 and customer != 43 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and current_density != 6 and customer != 68 and press = 3 and unit_number <= 5.5 | 0 | 0.120301 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and customer != 10 and ink_type != 1 and customer != 1 and customer != 43 and proof_on_ctd_ink != 1 and current_density != 6 and customer != 68 and caliper != 16 and customer != 67 and ink_temperature > 16.9 and cylinder_size = 3 | 0 | 0.106870 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and customer != 1 and customer != 10 and customer != 43 and proof_on_ctd_ink != 1 and current_density != 6 and customer != 68 and caliper != 16 and caliper != 14 and press != 7 and ESA_Voltage <= 2.5 and ESA_Voltage > 0.5 and customer != 52 | 0 | 0.134680 |
| paper_type != 2 and customer != 69 and customer != 35 and chrome_content != 1 and ink_type != 1 and customer != 1 and customer != 10 and customer != 43 and caliper != 14 and proof_on_ctd_ink != 1 and current_density != 6 and customer != 68 and caliper != 16 and ESA_Voltage <= 0.5 and type_on_cylinder != 0 and cylinder_size != 2 and roughness <= 0.96875 and anode_space_ratio > 103.0325 | 1 | 0.221675 |
| paper_type != 2 and customer != 69 and customer != 35 and customer != 32 and customer != 17 and chrome_content != 1 and customer != 10 and ink_type != 1 and customer != 1 and current_density != 6 and customer != 43 and proof_on_ctd_ink != 1 and customer != 68 and caliper != 16 and ESA_Voltage > 0.5 and press != 6 and wax > 2.15 | 1 | 0.129555 |
| paper_type != 2 and customer != 69 and customer != 35 and customer != 32 and customer != 17 and chrome_content != 1 and customer != 10 and customer != 1 and customer != 43 and proof_on_ctd_ink != 1 and current_density != 6 and customer != 68 and caliper != 16 and press = 6 and viscosity > 42.5 | 1 | 0.087302 |
| customer != 1 and paper_type != 2 and customer != 10 and customer != 43 and customer != 68 and current_density != 6 and customer != 63 and customer != 69 and customer != 35 and caliper != 16 and press != 7 and customer != 47 and chrome_content != 1 and customer != 32 and customer != 17 and ESA_Voltage <= 0.5 and unit_number > 4.5 and press != 2 | 0 | 0.225861 |
| paper_type != 2 and customer != 69 and customer != 35 and customer != 32 and chrome_content != 1 and customer != 17 and press != 6 and ink_type != 1 and customer != 47 and caliper != 3 and ink_type = 0 and anode_space_ratio > 98.38499999999999 | 1 | 0.220280 |
| customer != 1 and current_density != 6 and customer != 64 and press != 0 and caliper != 3 | 0 | 0.532289 |
| customer != 69 and customer != 1 and customer != 10 and ink_type != 1 and customer != 47 and plating_tank = 1 | 1 | 0.444912 |
| paper_type = 3 and ink_type = 0 | 1 | 0.250000 |
| customer != 64 and viscosity <= 53.5 | 0 | 0.661327 |
|  | 1 | 0.533333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| press_speed <= 2000 and blade_pressure <= 40 and unit_number <= 7 and blade_pressure >= 22 and current_density = 4 and job_number <= 37333 and proof_cut >= 50 | 0 | 0.067745 |
| press_speed <= 2100 and hardener >= 1 and blade_pressure <= 32 and unit_number <= 7 and ink_temperature >= 15.6 and job_number >= 34749 and roughness <= 0.75 | 0 | 0.064451 |
| press_speed <= 2000 and blade_pressure >= 22 and ink_temperature <= 15.2 and wax <= 2.5 and job_number <= 36568 and viscosity >= 55 | 0 | 0.051502 |
| ink_type = 2 and hardener >= 1 and varnish_pct <= 2.2 and job_number >= 38121 | 0 | 0.039130 |
| press_speed <= 2180 and humifity >= 72 and viscosity <= 52 and viscosity >= 51 and ink_temperature <= 16.5 | 0 | 0.043290 |
| ink_temperature >= 17 and press_type = 2 and humifity <= 85 | 0 | 0.051502 |
| ink_temperature <= 15 and press_speed <= 1500 and viscosity <= 53 and viscosity >= 45 | 0 | 0.030702 |
| hardener <= 0.3 | 0 | 0.034934 |
| press_speed <= 2180 and hardener >= 1 and humifity >= 85 and blade_pressure <= 29 and ink_temperature <= 15.5 | 0 | 0.034934 |
| press_speed <= 2180 and hardener >= 1 and job_number <= 37191 and ink_temperature <= 14.5 and wax <= 2.9 | 0 | 0.024090 |
| ink_type = 2 and viscosity >= 57 and wax <= 2.5 | 0 | 0.026432 |
| press_speed <= 2180 and humifity >= 72 and humifity <= 75 and blade_pressure >= 26 and plating_tank = 2 | 0 | 0.032297 |
| humifity >= 78 and press_speed <= 1650 and solvent_pct >= 40.8 and press_speed >= 1470 | 0 | 0.030702 |
| roughness >= 0.875 and press = 2 | 0 | 0.017778 |
| press = 4 and hardener >= 1 and unit_number >= 7 | 0 | 0.013393 |
| job_number >= 47204 and customer = 52 | 0 | 0.013393 |
|  | 1 | 0.928571 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cylinder_division|press_type|paper_mill_location|roller_durometer|target
---|---|---|---|---
1|2|4|(33.5-inf)|0
1|3|3|(33.5-inf)|0
1|3|?|?|0
1|2|3|(33.5-inf)|1
1|2|?|?|0
1|1|3|(33.5-inf)|0
1|3|2|(33.5-inf)|0
1|3|?|(33.5-inf)|0
1|2|2|(33.5-inf)|0
1|2|?|(33.5-inf)|1
1|3|1|(33.5-inf)|0
1|0|?|?|0
1|1|2|(33.5-inf)|1
1|1|?|(33.5-inf)|0
1|3|2|(-inf-33.5]|1
1|0|2|(33.5-inf)|1
1|3|?|(-inf-33.5]|0
1|0|?|(33.5-inf)|1
1|3|0|(33.5-inf)|0
1|2|2|(-inf-33.5]|0
1|2|?|(-inf-33.5]|1
1|0|1|(33.5-inf)|1
1|2|0|(33.5-inf)|1
1|1|?|(-inf-33.5]|1
1|2|1|(-inf-33.5]|1
1|0|2|(-inf-33.5]|1
1|0|?|(-inf-33.5]|0
1|0|0|(33.5-inf)|1
1|1|1|(-inf-33.5]|1
1|3|0|(-inf-33.5]|1
1|0|1|(-inf-33.5]|0
1|2|0|(-inf-33.5]|1
1|1|0|(-inf-33.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(press_speed <= 2000) and (blade_pressure <= 40) and (unit_number <= 7) and (blade_pressure >= 22) and (current_density = 4) and (job_number <= 37333) and (proof_cut >= 50)|0 (17.0/0.0)
(press_speed <= 2100) and (hardener >= 1) and (blade_pressure <= 32) and (unit_number <= 7) and (ink_temperature >= 15.6) and (job_number >= 34749) and (roughness <= 0.75)|0 (16.0/0.0)
(press_speed <= 2000) and (blade_pressure >= 22) and (ink_temperature <= 15.2) and (wax <= 2.5) and (job_number <= 36568) and (viscosity >= 55)|0 (12.0/0.0)
(ink_type = 2) and (hardener >= 1) and (varnish_pct <= 2.2) and (job_number >= 38121)|0 (9.0/0.0)
(press_speed <= 2180) and (humifity >= 72) and (viscosity <= 52) and (viscosity >= 51) and (ink_temperature <= 16.5)|0 (10.0/0.0)
(ink_temperature >= 17) and (press_type = 2) and (humifity <= 85)|0 (12.0/0.0)
(ink_temperature <= 15) and (press_speed <= 1500) and (viscosity <= 53) and (viscosity >= 45)|0 (7.0/0.0)
(hardener <= 0.3)|0 (8.0/0.0)
(press_speed <= 2180) and (hardener >= 1) and (humifity >= 85) and (blade_pressure <= 29) and (ink_temperature <= 15.5)|0 (8.0/0.0)
(press_speed <= 2180) and (hardener >= 1) and (job_number <= 37191) and (ink_temperature <= 14.5) and (wax <= 2.9)|0 (7.0/0.0)
(ink_type = 2) and (viscosity >= 57) and (wax <= 2.5)|0 (6.0/0.0)
(press_speed <= 2180) and (humifity >= 72) and (humifity <= 75) and (blade_pressure >= 26) and (plating_tank = 2)|0 (9.0/0.0)
(humifity >= 78) and (press_speed <= 1650) and (solvent_pct >= 40.8) and (press_speed >= 1470)|0 (7.0/0.0)
(roughness >= 0.875) and (press = 2)|0 (4.0/0.0)
(press = 4) and (hardener >= 1) and (unit_number >= 7)|0 (3.0/0.0)
(job_number >= 47204) and (customer = 52)|0 (3.0/0.0)
|1 (239.0/18.0)


## PART

Decision list:

rules | predicted class
---|---
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND current_density != 3 AND current_density = 2 AND customer != 67|1 (34.59/1.35)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND press = 2 AND press_speed <= 1625.0|0 (15.0)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND press != 4 AND customer != 58 AND customer != 1 AND customer != 10 AND customer != 43 AND customer != 68 AND current_density != 6 AND caliper != 14 AND press_type = 1 AND caliper != 6|1 (19.0/1.0)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND ESA_Voltage <= 4.25 AND customer != 10 AND current_density != 6 AND press_speed > 2184.5 AND type_on_cylinder != 0|1 (29.04/0.89)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND customer != 10 AND ink_type != 1 AND customer != 1 AND ESA_Voltage > 4.25|1 (27.21/2.2)
paper_type != 2 AND customer != 10 AND customer != 1 AND customer != 43 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND current_density != 6 AND customer != 68 AND press = 3 AND unit_number <= 5.5|0 (15.48)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND customer != 10 AND ink_type != 1 AND customer != 1 AND customer != 43 AND proof_on_ctd_ink != 1 AND current_density != 6 AND customer != 68 AND caliper != 16 AND customer != 67 AND ink_temperature > 16.9 AND cylinder_size = 3|0 (13.84)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND customer != 1 AND customer != 10 AND customer != 43 AND proof_on_ctd_ink != 1 AND current_density != 6 AND customer != 68 AND caliper != 16 AND caliper != 14 AND press != 7 AND ESA_Voltage <= 2.5 AND ESA_Voltage > 0.5 AND customer != 52|0 (17.47/2.0)
paper_type != 2 AND customer != 69 AND customer != 35 AND chrome_content != 1 AND ink_type != 1 AND customer != 1 AND customer != 10 AND customer != 43 AND caliper != 14 AND proof_on_ctd_ink != 1 AND current_density != 6 AND customer != 68 AND caliper != 16 AND ESA_Voltage <= 0.5 AND type_on_cylinder != 0 AND cylinder_size != 2 AND roughness <= 0.96875 AND anode_space_ratio > 103.0325|1 (34.72/4.0)
paper_type != 2 AND customer != 69 AND customer != 35 AND customer != 32 AND customer != 17 AND chrome_content != 1 AND customer != 10 AND ink_type != 1 AND customer != 1 AND current_density != 6 AND customer != 43 AND proof_on_ctd_ink != 1 AND customer != 68 AND caliper != 16 AND ESA_Voltage > 0.5 AND press != 6 AND wax > 2.15|1 (15.32/1.3)
paper_type != 2 AND customer != 69 AND customer != 35 AND customer != 32 AND customer != 17 AND chrome_content != 1 AND customer != 10 AND customer != 1 AND customer != 43 AND proof_on_ctd_ink != 1 AND current_density != 6 AND customer != 68 AND caliper != 16 AND press = 6 AND viscosity > 42.5|1 (12.66/2.0)
customer != 1 AND paper_type != 2 AND customer != 10 AND customer != 43 AND customer != 68 AND current_density != 6 AND customer != 63 AND customer != 69 AND customer != 35 AND caliper != 16 AND press != 7 AND customer != 47 AND chrome_content != 1 AND customer != 32 AND customer != 17 AND ESA_Voltage <= 0.5 AND unit_number > 4.5 AND press != 2|0 (21.7/3.0)
paper_type != 2 AND customer != 69 AND customer != 35 AND customer != 32 AND chrome_content != 1 AND customer != 17 AND press != 6 AND ink_type != 1 AND customer != 47 AND caliper != 3 AND ink_type = 0 AND anode_space_ratio > 98.38499999999999|1 (21.45/1.25)
customer != 1 AND current_density != 6 AND customer != 64 AND press != 0 AND caliper != 3|0 (50.65/2.43)
customer != 69 AND customer != 1 AND customer != 10 AND ink_type != 1 AND customer != 47 AND plating_tank = 1|1 (21.29/2.23)
paper_type = 3 AND ink_type = 0|1 (8.23/0.23)
customer != 64 AND viscosity <= 53.5|0 (11.33)
|1 (8.01/1.5)


## J48 Decision Tree

* paper_type = 2: 0 (12.0)
* paper_type != 2
	* customer = 69: 0 (7.0)
	* customer != 69
		* ink_type = 1: 0 (13.0/2.0)
		* ink_type != 1
			* customer = 58: 1 (15.0/1.0)
			* customer != 58
				* current_density = 2: 1 (37.57/4.34)
				* current_density != 2
					* press = 2
						* press_speed <= 1620.0: 0 (15.0)
						* press_speed > 1620.0
							* humifity <= 87.0: 0 (15.77/3.89)
							* humifity > 87.0: 1 (9.0/2.0)
					* press != 2
						* customer = 68: 1 (10.0)
						* customer != 68
							* ink_temperature <= 16.8
								* chrome_content = 0: 1 (7.03/0.03)
								* chrome_content != 0
									* customer = 5: 1 (10.0/1.0)
									* customer != 5
										* press = 4
											* blade_pressure <= 23.0
												* unit_number <= 2.0: 1 (9.89)
												* unit_number > 2.0: 0 (8.89/4.0)
											* blade_pressure > 23.0: 0 (18.0/2.0)
										* press != 4
											* press = 3
												* customer = 62: 1 (8.0/1.0)
												* customer != 62
													* paper_type = 1: 0 (12.86/3.0)
													* paper_type != 1
														* ink_pct <= 51.0: 0 (10.31/2.0)
														* ink_pct > 51.0
															* solvent_pct <= 39.0: 1 (14.44/1.44)
															* solvent_pct > 39.0: 0 (8.25/4.0)
											* press != 3
												* cylinder_size = 2: 0 (8.0/3.0)
												* cylinder_size != 2
													* ink_type = 0
														* paper_type = 1
															* proof_on_ctd_ink = 1: 1 (8.5/0.5)
															* proof_on_ctd_ink != 1
																* ESA_Voltage <= 0.5
																	* anode_space_ratio <= 100.0: 1 (9.22/0.52)
																	* anode_space_ratio > 100.0: 0 (8.52/4.0)
																* ESA_Voltage > 0.5: 1 (7.76/0.46)
														* paper_type != 1: 1 (21.0)
													* ink_type != 0
														* press_type = 2: 0 (8.0/2.0)
														* press_type != 2
															* proof_cut <= 50.0
																* humifity <= 78.0: 1 (17.0/5.0)
																* humifity > 78.0: 0 (7.0/1.0)
															* proof_cut > 50.0: 1 (16.81)
							* ink_temperature > 16.8
								* press_type = 2: 0 (13.0)
								* press_type != 2: 1 (10.19/4.0)


## SimpleCart Decision Tree

																																									* customer=(1)|(2)|(3)|(8)|(13)|(14)|(15)|(16)|(18)|(20)|(22)|(25)|(36)|(42)|(48)|(50)|(51)|(59)|(60)|(58)|(68)|(39)|(24)|(43)|(57)|(62)|(40)|(53)|(63)|(65)|(5)|(10)|(27)|(26)|(61)|(67)|(52)|(34)|(41)|(47)|(64)|(17)
																										* customer=(1)|(2)|(3)|(8)|(13)|(14)|(15)|(16)|(18)|(20)|(22)|(25)|(36)|(42)|(48)|(50)|(51)|(59)|(60)|(58)|(68)|(39)|(24)|(43)|(57)|(62): 1(97.0/14.0)
																										* customer!=(1)|(2)|(3)|(8)|(13)|(14)|(15)|(16)|(18)|(20)|(22)|(25)|(36)|(42)|(48)|(50)|(51)|(59)|(60)|(58)|(68)|(39)|(24)|(43)|(57)|(62)
						* press=(1)|(5)|(7)|(6)|(0)
			* ink_temperature < 16.9
				* ink_type=(0): 1(49.0/6.0)
				* ink_type!=(0)
					* varnish_pct < 1.1
						* hardener < 0.95: 1(4.0/1.68)
						* hardener >= 0.95: 0(9.96/0.0)
					* varnish_pct >= 1.1: 1(25.0/7.34)
			* ink_temperature >= 16.9: 0(9.0/3.0)
						* press!=(1)|(5)|(7)|(6)|(0)
											* caliper=(16)|(3)|(12)|(15)|(8)|(10)|(14)|(5)|(19)
				* press_speed < 1735.0
					* proof_cut < 63.5: 0(14.88/1.0)
					* proof_cut >= 63.5: 1(2.0/0.55)
				* press_speed >= 1735.0
					* anode_space_ratio < 96.83500000000001: 0(5.0/0.07)
					* anode_space_ratio >= 96.83500000000001: 1(31.36/14.71)
											* caliper!=(16)|(3)|(12)|(15)|(8)|(10)|(14)|(5)|(19): 0(24.84/2.56)
																																									* customer!=(1)|(2)|(3)|(8)|(13)|(14)|(15)|(16)|(18)|(20)|(22)|(25)|(36)|(42)|(48)|(50)|(51)|(59)|(60)|(58)|(68)|(39)|(24)|(43)|(57)|(62)|(40)|(53)|(63)|(65)|(5)|(10)|(27)|(26)|(61)|(67)|(52)|(34)|(41)|(47)|(64)|(17)
	* current_density=(6): 1(2.0/0.11)
	* current_density!=(6): 0(47.88/4.0)


