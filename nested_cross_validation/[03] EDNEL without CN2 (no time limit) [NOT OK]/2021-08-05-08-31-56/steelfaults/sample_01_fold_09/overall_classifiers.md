# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.653295 |
| Length_of_Conveyer > 1435.5 and Length_of_Conveyer <= 1623.5 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.010417 |
| Length_of_Conveyer > 1353.5 and Length_of_Conveyer <= 1359 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.063270 |
| Length_of_Conveyer > 1623.5 and Length_of_Conveyer <= 1649 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.012132 |
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

length_of_conveyer|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---
(1435.5-1623.5]|0|0|0|0|0|1|0
(-inf-1352.5]|0|0|0|0|0|1|0
(1352.5-1353.5]|0|0|0|0|0|1|0
(1369-1375]|0|0|0|0|0|1|0
(1353.5-1359]|0|0|0|0|0|1|0
(1623.5-1649]|0|0|0|0|0|1|0
(1359-1369]|0|0|0|0|0|1|0
(1375-1389.5]|0|0|0|0|0|1|0
(1649-inf)|0|0|0|0|0|1|0
(1623.5-1649]|0|0|0|0|1|0|0
(1359-1369]|0|0|0|0|1|0|0
(1352.5-1353.5]|0|0|0|0|1|0|0
(1649-inf)|0|0|0|0|1|0|0
(-inf-1352.5]|0|0|0|0|1|0|0
(1353.5-1359]|0|0|0|0|1|0|0
(1359-1369]|0|0|0|1|0|0|0
(1353.5-1359]|0|0|0|1|0|0|0
(-inf-1352.5]|0|0|1|0|0|0|0
(1389.5-1397]|0|0|1|0|0|0|0
(1369-1375]|0|0|1|0|0|0|0
(1359-1369]|0|0|1|0|0|0|0
(1649-inf)|0|0|1|0|0|0|0
(1397-1435.5]|0|0|1|0|0|0|0
(1353.5-1359]|0|0|1|0|0|0|0
(1375-1389.5]|0|0|1|0|0|0|0
(-inf-1352.5]|0|1|0|0|0|0|0
(1353.5-1359]|0|1|0|0|0|0|0
(1359-1369]|0|1|0|0|0|0|0
(-inf-1352.5]|1|0|0|0|0|0|0
(1435.5-1623.5]|1|0|0|0|0|0|0
(1352.5-1353.5]|1|0|0|0|0|0|0
(1369-1375]|1|0|0|0|0|0|0
(1389.5-1397]|1|0|0|0|0|0|0
(1359-1369]|1|0|0|0|0|0|0
(1353.5-1359]|1|0|0|0|0|0|0
(1375-1389.5]|1|0|0|0|0|0|0
(1649-inf)|1|0|0|0|0|0|0
(1623.5-1649]|1|0|0|0|0|0|0
(1435.5-1623.5]|0|0|0|0|0|0|1
(1623.5-1649]|0|0|0|0|0|0|1
(1375-1389.5]|0|0|0|0|0|0|1
(1369-1375]|0|0|0|0|0|0|1
(-inf-1352.5]|0|0|0|0|0|0|1
(1359-1369]|0|0|0|0|0|0|1
(1353.5-1359]|0|0|0|0|0|0|1
(1649-inf)|0|0|0|0|0|0|1
(1389.5-1397]|0|0|0|0|0|0|1
(1352.5-1353.5]|0|0|0|0|0|0|1

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
					* Dirtiness = 0: 1 (303.0)
					* Dirtiness = 1: 0 (31.0)
				* Stains = 1: 0 (37.0)
			* Pastry = 1: 0 (72.0)
		* Z_Scratch = 1: 0 (80.0)
	* K_Scatch = 1: 0 (169.0)
* Bumps = 1: 0 (181.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(605.0/0.0)
					* Dirtiness!=(0): 0(50.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(143.0/0.0)
		* Z_Scratch!=(0): 0(171.0/0.0)
	* K_Scatch!=(0): 0(350.0/0.0)
* Bumps!=(0): 0(361.0/0.0)


