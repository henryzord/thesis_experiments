# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps!=(0) | 0 | 0.652921 |
| Steel_Plate_Thickness > 45 and Steel_Plate_Thickness <= 64.5 and Log_X_Index > 1.13 and Log_X_Index <= 2.0588 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.014693 |
| Steel_Plate_Thickness > 64.5 and Steel_Plate_Thickness <= 127.5 and Log_X_Index <= 1.13 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.098101 |
| Steel_Plate_Thickness <= 45 and Log_X_Index > 2.35315 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.002625 |
| Steel_Plate_Thickness > 295 and Log_X_Index <= 1.13 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.011275 |
| Steel_Plate_Thickness > 64.5 and Steel_Plate_Thickness <= 127.5 and Log_X_Index > 1.13 and Log_X_Index <= 2.0588 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.088729 |
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.347079 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.347079 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.347079 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

steel_plate_thickness|log_x_index|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---|---
(-inf-45]|(2.35315-inf)|0|0|0|0|0|1|0
(64.5-127.5]|(2.0588-2.35315]|0|0|0|0|0|1|0
(127.5-295]|(1.13-2.0588]|0|0|0|0|0|1|0
(45-64.5]|(1.13-2.0588]|0|0|0|0|0|1|0
(-inf-45]|(1.13-2.0588]|0|0|0|0|0|1|0
(64.5-127.5]|(1.13-2.0588]|0|0|0|0|0|1|0
(45-64.5]|(2.35315-inf)|0|0|1|0|0|0|0
(127.5-295]|(-inf-1.13]|0|0|0|0|0|1|0
(-inf-45]|(2.35315-inf)|0|0|1|0|0|0|0
(45-64.5]|(-inf-1.13]|0|0|0|0|0|1|0
(64.5-127.5]|(1.13-2.0588]|0|0|0|0|1|0|0
(-inf-45]|(-inf-1.13]|0|0|0|0|0|1|0
(64.5-127.5]|(-inf-1.13]|0|0|0|0|0|1|0
(45-64.5]|(-inf-1.13]|0|0|0|0|1|0|0
(64.5-127.5]|(1.13-2.0588]|0|0|0|1|0|0|0
(45-64.5]|(1.13-2.0588]|0|0|0|1|0|0|0
(45-64.5]|(2.0588-2.35315]|0|0|1|0|0|0|0
(127.5-295]|(-inf-1.13]|0|0|0|0|1|0|0
(-inf-45]|(-inf-1.13]|0|0|0|0|1|0|0
(64.5-127.5]|(-inf-1.13]|0|0|0|0|1|0|0
(-inf-45]|(2.0588-2.35315]|0|0|1|0|0|0|0
(64.5-127.5]|(1.13-2.0588]|0|0|1|0|0|0|0
(64.5-127.5]|(2.0588-2.35315]|0|1|0|0|0|0|0
(45-64.5]|(-inf-1.13]|0|0|0|1|0|0|0
(-inf-45]|(1.13-2.0588]|0|0|1|0|0|0|0
(127.5-295]|(1.13-2.0588]|0|1|0|0|0|0|0
(-inf-45]|(1.13-2.0588]|0|1|0|0|0|0|0
(64.5-127.5]|(1.13-2.0588]|0|1|0|0|0|0|0
(-inf-45]|(-inf-1.13]|0|0|1|0|0|0|0
(45-64.5]|(1.13-2.0588]|1|0|0|0|0|0|0
(127.5-295]|(2.35315-inf)|0|0|0|0|0|0|0
(64.5-127.5]|(2.35315-inf)|0|0|0|0|0|0|1
(-inf-45]|(1.13-2.0588]|1|0|0|0|0|0|0
(-inf-45]|(2.35315-inf)|0|0|0|0|0|0|1
(64.5-127.5]|(1.13-2.0588]|1|0|0|0|0|0|0
(127.5-295]|(-inf-1.13]|0|1|0|0|0|0|0
(127.5-295]|(1.13-2.0588]|1|0|0|0|0|0|0
(64.5-127.5]|(-inf-1.13]|0|1|0|0|0|0|0
(64.5-127.5]|(2.0588-2.35315]|0|0|0|0|0|0|1
(-inf-45]|(2.0588-2.35315]|0|0|0|0|0|0|1
(45-64.5]|(-inf-1.13]|1|0|0|0|0|0|0
(64.5-127.5]|(-inf-1.13]|1|0|0|0|0|0|0
(127.5-295]|(-inf-1.13]|1|0|0|0|0|0|0
(-inf-45]|(-inf-1.13]|1|0|0|0|0|0|0
(127.5-295]|(1.13-2.0588]|0|0|0|0|0|0|1
(45-64.5]|(1.13-2.0588]|0|0|0|0|0|0|1
(295-inf)|(1.13-2.0588]|0|0|0|0|0|0|1
(64.5-127.5]|(1.13-2.0588]|0|0|0|0|0|0|1
(-inf-45]|(1.13-2.0588]|0|0|0|0|0|0|1
(45-64.5]|(-inf-1.13]|0|0|0|0|0|0|1
(295-inf)|(-inf-1.13]|0|0|0|0|0|0|1
(64.5-127.5]|(-inf-1.13]|0|0|0|0|0|0|1
(-inf-45]|(-inf-1.13]|0|0|0|0|0|0|1
(127.5-295]|(-inf-1.13]|0|0|0|0|0|0|1

## JRip

Decision list:

rules | predicted class
---|---
(Bumps = 0) and (K_Scatch = 0) and (Z_Scratch = 0) and (Pastry = 0) and (Stains = 0) and (Dirtiness = 0)|1 (606.0/0.0)
|0 (1140.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Bumps = 0 AND K_Scatch = 0 AND Z_Scratch = 0 AND Pastry = 0 AND Stains = 0 AND Dirtiness = 0|1 (606.0)
|0 (1140.0)


## J48 Decision Tree

* Bumps = 0
	* K_Scatch = 0
		* Z_Scratch = 0
			* Pastry = 0
				* Stains = 0
					* Dirtiness = 0: 1 (606.0)
					* Dirtiness != 0: 0 (50.0)
				* Stains != 0: 0 (65.0)
			* Pastry != 0: 0 (142.0)
		* Z_Scratch != 0: 0 (171.0)
	* K_Scatch != 0: 0 (351.0)
* Bumps != 0: 0 (361.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(606.0/0.0)
					* Dirtiness!=(0): 0(50.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(142.0/0.0)
		* Z_Scratch!=(0): 0(171.0/0.0)
	* K_Scatch!=(0): 0(351.0/0.0)
* Bumps!=(0): 0(361.0/0.0)


