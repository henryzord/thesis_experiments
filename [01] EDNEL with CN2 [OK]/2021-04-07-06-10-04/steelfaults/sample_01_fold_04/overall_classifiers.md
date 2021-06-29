# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.653295 |
| Outside_X_Index > 0.16565 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.006969 |
| Outside_X_Index > 0.00825 and Outside_X_Index <= 0.08885 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.241517 |
| Outside_X_Index <= 0.00825 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.164835 |
| Bumps = 0 and K_Scatch = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
| Bumps!=(0) | 0 | 0.653295 |
| Log_X_Index > 0.81165 and Log_X_Index <= 1.13 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.182796 |
| Log_X_Index <= 0.81165 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.014693 |
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
| K_Scatch = 0 and Bumps = 0 and Z_Scratch = 0 and Pastry = 0 and Stains = 0 and Dirtiness = 0 | 1 | 0.346705 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

log_x_index|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---
(2.35315-inf)|0|0|0|0|0|1|0
(2.0588-2.35315]|0|0|0|0|0|1|0
(-inf-0.81165]|0|0|0|0|0|1|0
(1.13-2.0588]|0|0|0|0|0|1|0
(0.81165-1.13]|0|0|0|0|0|1|0
(1.13-2.0588]|0|0|0|0|1|0|0
(0.81165-1.13]|0|0|0|0|1|0|0
(-inf-0.81165]|0|0|0|0|1|0|0
(1.13-2.0588]|0|0|0|1|0|0|0
(-inf-0.81165]|0|0|0|1|0|0|0
(0.81165-1.13]|0|0|0|1|0|0|0
(-inf-0.81165]|0|0|1|0|0|0|0
(2.35315-inf)|0|0|1|0|0|0|0
(0.81165-1.13]|0|0|1|0|0|0|0
(1.13-2.0588]|0|0|1|0|0|0|0
(2.0588-2.35315]|0|0|1|0|0|0|0
(-inf-0.81165]|0|1|0|0|0|0|0
(2.0588-2.35315]|0|1|0|0|0|0|0
(1.13-2.0588]|0|1|0|0|0|0|0
(0.81165-1.13]|0|1|0|0|0|0|0
(-inf-0.81165]|1|0|0|0|0|0|0
(1.13-2.0588]|1|0|0|0|0|0|0
(0.81165-1.13]|1|0|0|0|0|0|0
(2.35315-inf)|0|0|0|0|0|0|1
(2.0588-2.35315]|0|0|0|0|0|0|1
(-inf-0.81165]|0|0|0|0|0|0|1
(1.13-2.0588]|0|0|0|0|0|0|1
(0.81165-1.13]|0|0|0|0|0|0|1

## JRip

Decision list:

rules | predicted class
---|---
(K_Scatch = 0) and (Bumps = 0) and (Z_Scratch = 0) and (Pastry = 0) and (Stains = 0) and (Dirtiness = 0)|1 (605.0/0.0)
|0 (1140.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
Bumps = 0 AND K_Scatch = 0 AND Z_Scratch = 0 AND Pastry = 0 AND Stains = 0 AND Dirtiness = 0|1 (529.0)
|0 (998.0)


## J48 Decision Tree

* Bumps = 0
	* K_Scatch = 0
		* Z_Scratch = 0
			* Pastry = 0
				* Stains = 0
					* Dirtiness = 0: 1 (605.0)
					* Dirtiness != 0: 0 (49.0)
				* Stains != 0: 0 (65.0)
			* Pastry != 0: 0 (142.0)
		* Z_Scratch != 0: 0 (170.0)
	* K_Scatch != 0: 0 (352.0)
* Bumps != 0: 0 (362.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(605.0/0.0)
					* Dirtiness!=(0): 0(49.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(142.0/0.0)
		* Z_Scratch!=(0): 0(170.0/0.0)
	* K_Scatch!=(0): 0(352.0/0.0)
* Bumps!=(0): 0(362.0/0.0)


