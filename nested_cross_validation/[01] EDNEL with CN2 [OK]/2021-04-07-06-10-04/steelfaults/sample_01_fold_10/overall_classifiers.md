# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps!=(0) | 0 | 0.653295 |
| Steel_Plate_Thickness > 127.5 and Steel_Plate_Thickness <= 295 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.095238 |
| Steel_Plate_Thickness <= 45 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.133739 |
| Steel_Plate_Thickness > 95 and Steel_Plate_Thickness <= 122.5 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.057851 |
| Steel_Plate_Thickness > 64.5 and Steel_Plate_Thickness <= 82.5 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.129106 |
| Steel_Plate_Thickness > 295 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.033079 |
| Steel_Plate_Thickness > 45 and Steel_Plate_Thickness <= 64.5 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.025641 |
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
|  | 0 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

steel_plate_thickness|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---
(82.5-95]|0|0|0|0|0|1|0
(127.5-295]|0|0|0|0|0|1|0
(45-64.5]|0|0|0|0|0|1|0
(95-122.5]|0|0|0|0|0|1|0
(64.5-82.5]|0|0|0|0|0|1|0
(-inf-45]|0|0|0|0|0|1|0
(45-64.5]|0|0|0|0|1|0|0
(127.5-295]|0|0|0|0|1|0|0
(64.5-82.5]|0|0|0|0|1|0|0
(-inf-45]|0|0|0|0|1|0|0
(95-122.5]|0|0|0|0|1|0|0
(45-64.5]|0|0|0|1|0|0|0
(64.5-82.5]|0|0|1|0|0|0|0
(45-64.5]|0|0|1|0|0|0|0
(-inf-45]|0|0|1|0|0|0|0
(95-122.5]|0|1|0|0|0|0|0
(-inf-45]|0|1|0|0|0|0|0
(127.5-295]|0|1|0|0|0|0|0
(64.5-82.5]|0|1|0|0|0|0|0
(-inf-45]|1|0|0|0|0|0|0
(122.5-127.5]|1|0|0|0|0|0|0
(127.5-295]|1|0|0|0|0|0|0
(82.5-95]|1|0|0|0|0|0|0
(95-122.5]|1|0|0|0|0|0|0
(64.5-82.5]|1|0|0|0|0|0|0
(45-64.5]|1|0|0|0|0|0|0
(82.5-95]|0|0|0|0|0|0|0
(45-64.5]|0|0|0|0|0|0|1
(95-122.5]|0|0|0|0|0|0|1
(295-inf)|0|0|0|0|0|0|1
(127.5-295]|0|0|0|0|0|0|1
(64.5-82.5]|0|0|0|0|0|0|1
(-inf-45]|0|0|0|0|0|0|1

## JRip

Decision list:

rules | predicted class
---|---
(Bumps = 0) and (K_Scatch = 0) and (Z_Scratch = 0) and (Pastry = 0) and (Stains = 0) and (Dirtiness = 0)|1 (605.0/0.0)
|0 (1140.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Bumps = 0 AND K_Scatch = 0 AND Z_Scratch = 0 AND Pastry = 0 AND Stains = 0 AND Dirtiness = 0|1 (605.0)
|0 (1140.0)


## J48 Decision Tree

* Bumps = 0
	* K_Scatch = 0
		* Z_Scratch = 0
			* Pastry = 0
				* Stains = 0
					* Dirtiness = 0: 1 (605.0)
					* Dirtiness != 0: 0 (50.0)
				* Stains != 0: 0 (64.0)
			* Pastry != 0: 0 (143.0)
		* Z_Scratch != 0: 0 (171.0)
	* K_Scatch != 0: 0 (351.0)
* Bumps != 0: 0 (361.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(605.0/0.0)
					* Dirtiness!=(0): 0(50.0/0.0)
				* Stains!=(0): 0(64.0/0.0)
			* Pastry!=(0): 0(143.0/0.0)
		* Z_Scratch!=(0): 0(171.0/0.0)
	* K_Scatch!=(0): 0(351.0/0.0)
* Bumps!=(0): 0(361.0/0.0)


