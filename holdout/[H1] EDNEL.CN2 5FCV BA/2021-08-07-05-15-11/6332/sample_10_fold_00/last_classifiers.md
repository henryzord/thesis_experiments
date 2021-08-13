# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.555556 |
| customer != 39 | 0 | 0.440063 |
| customer != 61 | 0 | 0.437140 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| paper_type != 2 and customer != 69 and press = 2 and ink_temperature <= 15.4 | 0 | 0.106541 |
| paper_type != 2 and customer != 69 and customer != 21 and ink_temperature > 16.9 and press_speed <= 2215.0 and press != 0 | 0 | 0.080592 |
| paper_type != 2 and customer != 69 and customer != 21 and ink_type != 1 and customer != 28 and customer != 64 and press_speed > 2112.5 | 1 | 0.307781 |
| paper_type != 2 and customer != 69 and customer != 21 and customer != 28 and ink_type != 1 and press != 3 and customer != 64 and current_density != 2 and humifity <= 69.5 | 1 | 0.148194 |
| paper_type != 2 and customer != 69 and customer != 21 and customer != 28 and ink_type != 1 and current_density != 2 and customer != 1 and press = 3 | 0 | 0.112889 |
| paper_type != 2 and customer != 69 and customer != 21 and customer != 28 and ink_type != 1 and proof_on_ctd_ink != 1 and current_density = 4 and customer != 6 and customer != 1 and job_number > 34552.0 and viscosity <= 61.5 and viscosity > 39.5 and viscosity <= 58.5 and job_number > 34568.5 and press != 6 and type_on_cylinder != 0 | 1 | 0.233021 |
| paper_type != 2 and customer != 69 and customer != 21 and proof_cut > 33.75 and proof_on_ctd_ink != 1 and customer != 1 and viscosity <= 64.5 and ink_pct > 44.05 and customer != 24 and customer != 28 and press != 3 and hardener <= 1.45 and current_density != 4 | 1 | 0.108643 |
| paper_type != 2 and customer != 69 and customer != 21 and proof_cut <= 33.75 | 1 | 0.103364 |
| customer != 1 and customer != 57 and paper_type != 2 and humifity <= 89.0 and proof_on_ctd_ink != 1 and viscosity <= 64.5 and wax > 2.95 and viscosity <= 61.5 | 1 | 0.119237 |
| customer != 1 and customer != 57 and customer != 63 and customer != 68 and blade_pressure > 21.0 and caliper != 12 and customer != 62 and viscosity > 39.5 | 0 | 0.586304 |
| wax <= 2.9 and ink_temperature <= 16.45 and ink_temperature > 14.55 and humifity > 73.5 | 1 | 0.530934 |
|  | 0 | 0.534884 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| press_type = 3 and press_speed <= 2000 and roughness >= 0.625 and wax <= 2.8 and job_number <= 36784 | 0 | 0.090909 |
| press = 2 and ink_temperature <= 15.3 and current_density = 4 | 0 | 0.078947 |
| press_speed <= 2100 and blade_pressure <= 35 and ink_temperature >= 17 | 0 | 0.095491 |
| ink_type = 2 and viscosity >= 57 and wax <= 2.5 | 0 | 0.054054 |
| press_speed <= 2100 and blade_pressure >= 22 and paper_type = 2 | 0 | 0.045455 |
| press_speed <= 2100 and ink_temperature <= 15 and proof_cut <= 55 and grain_screened = 2 and roller_durometer <= 34 and blade_pressure >= 25 | 0 | 0.054054 |
| press_type = 3 and humifity <= 72 and humifity >= 70 | 0 | 0.041096 |
| press_speed <= 2180 and humifity >= 78 and job_number >= 37998 and proof_cut <= 50 and proof_cut >= 45 | 0 | 0.036697 |
| press_speed <= 2180 and humifity >= 78 and unit_number <= 7 and job_number >= 35816 and blade_pressure <= 30 and plating_tank = 1 and wax >= 1.5 | 0 | 0.054054 |
| press_speed <= 2180 and varnish_pct <= 2.3 and roller_durometer >= 38 and hardener >= 1 and blade_pressure >= 24 | 0 | 0.027061 |
| press_speed <= 2180 and job_number <= 37386 and job_number >= 36858 and roller_durometer >= 40 and anode_space_ratio <= 100 | 0 | 0.018692 |
| current_density = 4 and job_number <= 34692 and press_speed <= 2180 and job_number >= 34156 and roughness <= 0.9375 and proof_cut >= 35 | 0 | 0.038226 |
| anode_space_ratio >= 106.45 and ink_temperature >= 16.2 and viscosity >= 56 | 0 | 0.009434 |
| anode_space_ratio >= 107.4 and ink_temperature >= 15.8 and job_number <= 37018 | 0 | 0.023256 |
| plating_tank = 2 and viscosity <= 44 and press_speed >= 1850 and press_type = 2 | 0 | 0.018692 |
|  | 1 | 0.958904 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

blade_mfg|press|esa_voltage|target
---|---|---|---
1|7|?|0
?|7|?|0
?|6|?|0
?|5|?|0
1|6|(4.25-inf)|1
?|4|?|0
?|7|(-inf-4.25]|1
1|5|(4.25-inf)|1
1|7|(-inf-4.25]|1
?|3|?|0
1|4|(4.25-inf)|1
1|6|(-inf-4.25]|1
?|2|?|0
1|3|(4.25-inf)|1
1|5|(-inf-4.25]|1
1|2|(4.25-inf)|1
?|4|(-inf-4.25]|0
1|4|(-inf-4.25]|0
?|0|?|0
2|3|(-inf-4.25]|0
1|3|(-inf-4.25]|0
?|2|(-inf-4.25]|0
1|0|(4.25-inf)|0
1|2|(-inf-4.25]|0
1|1|(-inf-4.25]|1
1|0|(-inf-4.25]|1

## JRip

Decision list:

rules | predicted class
---|---
(press_type = 3) and (press_speed <= 2000) and (roughness >= 0.625) and (wax <= 2.8) and (job_number <= 36784)|0 (21.0/0.0)
(press = 2) and (ink_temperature <= 15.3) and (current_density = 4)|0 (18.0/0.0)
(press_speed <= 2100) and (blade_pressure <= 35) and (ink_temperature >= 17)|0 (23.0/0.0)
(ink_type = 2) and (viscosity >= 57) and (wax <= 2.5)|0 (12.0/0.0)
(press_speed <= 2100) and (blade_pressure >= 22) and (paper_type = 2)|0 (10.0/0.0)
(press_speed <= 2100) and (ink_temperature <= 15) and (proof_cut <= 55) and (grain_screened = 2) and (roller_durometer <= 34) and (blade_pressure >= 25)|0 (12.0/0.0)
(press_type = 3) and (humifity <= 72) and (humifity >= 70)|0 (9.0/0.0)
(press_speed <= 2180) and (humifity >= 78) and (job_number >= 37998) and (proof_cut <= 50) and (proof_cut >= 45)|0 (8.0/0.0)
(press_speed <= 2180) and (humifity >= 78) and (unit_number <= 7) and (job_number >= 35816) and (blade_pressure <= 30) and (plating_tank = 1) and (wax >= 1.5)|0 (11.0/0.0)
(press_speed <= 2180) and (varnish_pct <= 2.3) and (roller_durometer >= 38) and (hardener >= 1) and (blade_pressure >= 24)|0 (6.0/0.0)
(press_speed <= 2180) and (job_number <= 37386) and (job_number >= 36858) and (roller_durometer >= 40) and (anode_space_ratio <= 100)|0 (5.0/0.0)
(current_density = 4) and (job_number <= 34692) and (press_speed <= 2180) and (job_number >= 34156) and (roughness <= 0.9375) and (proof_cut >= 35)|0 (10.0/0.0)
(anode_space_ratio >= 106.45) and (ink_temperature >= 16.2) and (viscosity >= 56)|0 (3.0/0.0)
(anode_space_ratio >= 107.4) and (ink_temperature >= 15.8) and (job_number <= 37018)|0 (5.0/0.0)
(plating_tank = 2) and (viscosity <= 44) and (press_speed >= 1850) and (press_type = 2)|0 (4.0/0.0)
|1 (221.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
paper_type != 2 AND customer != 69 AND press = 2 AND ink_temperature <= 15.4|0 (25.0/1.0)
paper_type != 2 AND customer != 69 AND customer != 21 AND ink_temperature > 16.9 AND press_speed <= 2215.0 AND press != 0|0 (22.0/2.0)
paper_type != 2 AND customer != 69 AND customer != 21 AND ink_type != 1 AND customer != 28 AND customer != 64 AND press_speed > 2112.5|1 (57.25/5.0)
paper_type != 2 AND customer != 69 AND customer != 21 AND customer != 28 AND ink_type != 1 AND press != 3 AND customer != 64 AND current_density != 2 AND humifity <= 69.5|1 (17.0/1.0)
paper_type != 2 AND customer != 69 AND customer != 21 AND customer != 28 AND ink_type != 1 AND current_density != 2 AND customer != 1 AND press = 3|0 (22.0/7.0)
paper_type != 2 AND customer != 69 AND customer != 21 AND customer != 28 AND ink_type != 1 AND proof_on_ctd_ink != 1 AND current_density = 4 AND customer != 6 AND customer != 1 AND job_number > 34552.0 AND viscosity <= 61.5 AND viscosity > 39.5 AND viscosity <= 58.5 AND job_number > 34568.5 AND press != 6 AND type_on_cylinder != 0|1 (32.48/5.48)
paper_type != 2 AND customer != 69 AND customer != 21 AND proof_cut > 33.75 AND proof_on_ctd_ink != 1 AND customer != 1 AND viscosity <= 64.5 AND ink_pct > 44.05 AND customer != 24 AND customer != 28 AND press != 3 AND hardener <= 1.45 AND current_density != 4|1 (14.15/3.23)
paper_type != 2 AND customer != 69 AND customer != 21 AND proof_cut <= 33.75|1 (12.46/0.37)
customer != 1 AND customer != 57 AND paper_type != 2 AND humifity <= 89.0 AND proof_on_ctd_ink != 1 AND viscosity <= 64.5 AND wax > 2.95 AND viscosity <= 61.5|1 (12.89/1.0)
customer != 1 AND customer != 57 AND customer != 63 AND customer != 68 AND blade_pressure > 21.0 AND caliper != 12 AND customer != 62 AND viscosity > 39.5|0 (53.99/1.7)
wax <= 2.9 AND ink_temperature <= 16.45 AND ink_temperature > 14.55 AND humifity > 73.5|1 (27.4/2.87)
|0 (27.38/13.61)


## J48 Decision Tree

* paper_type = 2: 0 (11.0)
* paper_type != 2
	* press = 2: 0 (35.0/7.0)
	* press != 2
		* press_speed <= 2112.5
			* ink_temperature <= 16.9: 1 (140.13/56.73)
			* ink_temperature > 16.9: 0 (11.07/0.07)
		* press_speed > 2112.5: 1 (54.8/5.27)


## SimpleCart Decision Tree

																																						* customer=(1)|(2)|(3)|(8)|(13)|(14)|(16)|(18)|(20)|(22)|(25)|(34)|(36)|(37)|(44)|(48)|(51)|(53)|(57)|(59)|(60)|(58)|(43)|(68)|(5)|(27)|(39)|(63)|(52)|(62)|(24)|(61)|(65)|(67)|(10)|(26)|(32)|(41)|(42)
							* press=(7)|(6)|(1)|(5)|(0)|(4)|(3): 1(167.0/49.0)
							* press!=(7)|(6)|(1)|(5)|(0)|(4)|(3): 0(28.0/8.0)
																																						* customer!=(1)|(2)|(3)|(8)|(13)|(14)|(16)|(18)|(20)|(22)|(25)|(34)|(36)|(37)|(44)|(48)|(51)|(53)|(57)|(59)|(60)|(58)|(43)|(68)|(5)|(27)|(39)|(63)|(52)|(62)|(24)|(61)|(65)|(67)|(10)|(26)|(32)|(41)|(42): 0(91.0/35.0)


