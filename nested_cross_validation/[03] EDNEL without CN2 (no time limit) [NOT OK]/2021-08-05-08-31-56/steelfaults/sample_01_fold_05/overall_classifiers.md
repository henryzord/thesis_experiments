# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps!=(0) | 0 | 0.653295 |
| Log_X_Index > 2.0588 and Log_X_Index <= 2.3522 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.008696 |
| Log_X_Index > 2.3522 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.009557 |
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

Non matches covered by Majority class

log_x_index|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---
(-inf-0.81165]|0|0|0|0|0|1|0
(2.3522-inf)|0|0|0|0|0|1|0
(2.0588-2.3522]|0|0|0|0|0|1|0
(1.13-2.0588]|0|0|0|0|0|1|0
(0.81165-1.13]|0|0|0|0|0|1|0
(1.13-2.0588]|0|0|0|0|1|0|0
(-inf-0.81165]|0|0|0|0|1|0|0
(0.81165-1.13]|0|0|0|0|1|0|0
(1.13-2.0588]|0|0|0|1|0|0|0
(-inf-0.81165]|0|0|0|1|0|0|0
(0.81165-1.13]|0|0|0|1|0|0|0
(-inf-0.81165]|0|0|1|0|0|0|0
(0.81165-1.13]|0|0|1|0|0|0|0
(1.13-2.0588]|0|0|1|0|0|0|0
(2.0588-2.3522]|0|0|1|0|0|0|0
(2.3522-inf)|0|0|1|0|0|0|0
(-inf-0.81165]|0|1|0|0|0|0|0
(1.13-2.0588]|0|1|0|0|0|0|0
(0.81165-1.13]|0|1|0|0|0|0|0
(-inf-0.81165]|1|0|0|0|0|0|0
(1.13-2.0588]|1|0|0|0|0|0|0
(0.81165-1.13]|1|0|0|0|0|0|0
(2.0588-2.3522]|0|0|0|0|0|0|1
(-inf-0.81165]|0|0|0|0|0|0|1
(0.81165-1.13]|0|0|0|0|0|0|1
(2.3522-inf)|0|0|0|0|0|0|1
(1.13-2.0588]|0|0|0|0|0|0|1

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
					* Dirtiness = 1: 0 (49.0)
				* Stains = 1: 0 (65.0)
			* Pastry = 1: 0 (142.0)
		* Z_Scratch = 1: 0 (171.0)
	* K_Scatch = 1: 0 (351.0)
* Bumps = 1: 0 (362.0)


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
		* Z_Scratch!=(0): 0(171.0/0.0)
	* K_Scatch!=(0): 0(351.0/0.0)
* Bumps!=(0): 0(362.0/0.0)


