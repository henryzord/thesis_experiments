# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps!=(0) | 0 | 0.653295 |
| Length_of_Conveyer > 1353.5 and Length_of_Conveyer <= 1359 and Log_X_Index > 2.0588 and Log_X_Index <= 2.3607 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.002625 |
| Length_of_Conveyer > 1359 and Log_X_Index > 1.13 and Log_X_Index <= 2.0588 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.179856 |
| Length_of_Conveyer > 1353.5 and Length_of_Conveyer <= 1359 and Log_X_Index <= 1.13 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.023973 |
| Length_of_Conveyer > 1359 and Log_X_Index > 2.0588 and Log_X_Index <= 2.3607 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.005236 |
| Length_of_Conveyer <= 1352.5 and Log_X_Index <= 1.13 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.005236 |
| Length_of_Conveyer > 1353.5 and Length_of_Conveyer <= 1359 and Log_X_Index > 2.3607 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.003497 |
| Length_of_Conveyer <= 1352.5 and Log_X_Index > 1.13 and Log_X_Index <= 2.0588 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.005236 |
| Length_of_Conveyer > 1359 and Log_X_Index > 2.3607 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.003497 |
| Length_of_Conveyer > 1353.5 and Length_of_Conveyer <= 1359 and Log_X_Index > 1.13 and Log_X_Index <= 2.0588 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.033079 |
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

length_of_conveyer|log_x_index|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---|---
(1359-inf)|(2.3607-inf)|0|0|0|0|0|1|0
(-inf-1352.5]|(1.13-2.0588]|0|0|0|0|0|1|0
(1352.5-1353.5]|(1.13-2.0588]|0|0|0|0|0|1|0
(1353.5-1359]|(1.13-2.0588]|0|0|0|0|0|1|0
(1359-inf)|(1.13-2.0588]|0|0|0|0|0|1|0
(1353.5-1359]|(2.3607-inf)|0|0|1|0|0|0|0
(1359-inf)|(1.13-2.0588]|0|0|0|0|1|0|0
(1352.5-1353.5]|(1.13-2.0588]|0|0|0|0|1|0|0
(-inf-1352.5]|(-inf-1.13]|0|0|0|0|0|1|0
(1352.5-1353.5]|(-inf-1.13]|0|0|0|0|0|1|0
(1359-inf)|(2.3607-inf)|0|0|1|0|0|0|0
(1353.5-1359]|(-inf-1.13]|0|0|0|0|0|1|0
(1359-inf)|(-inf-1.13]|0|0|0|0|0|1|0
(-inf-1352.5]|(2.0588-2.3607]|0|0|1|0|0|0|0
(1359-inf)|(1.13-2.0588]|0|0|0|1|0|0|0
(1353.5-1359]|(1.13-2.0588]|0|0|0|1|0|0|0
(-inf-1352.5]|(-inf-1.13]|0|0|0|0|1|0|0
(1353.5-1359]|(-inf-1.13]|0|0|0|0|1|0|0
(1359-inf)|(-inf-1.13]|0|0|0|0|1|0|0
(1353.5-1359]|(2.0588-2.3607]|0|0|1|0|0|0|0
(1359-inf)|(2.0588-2.3607]|0|0|1|0|0|0|0
(1352.5-1353.5]|(-inf-1.13]|0|0|0|0|1|0|0
(1353.5-1359]|(2.0588-2.3607]|0|1|0|0|0|0|0
(1359-inf)|(-inf-1.13]|0|0|0|1|0|0|0
(1353.5-1359]|(1.13-2.0588]|0|0|1|0|0|0|0
(1359-inf)|(1.13-2.0588]|0|0|1|0|0|0|0
(1353.5-1359]|(-inf-1.13]|0|0|0|1|0|0|0
(1353.5-1359]|(-inf-1.13]|0|0|1|0|0|0|0
(-inf-1352.5]|(1.13-2.0588]|0|1|0|0|0|0|0
(1359-inf)|(-inf-1.13]|0|0|1|0|0|0|0
(1359-inf)|(1.13-2.0588]|0|1|0|0|0|0|0
(1353.5-1359]|(1.13-2.0588]|0|1|0|0|0|0|0
(-inf-1352.5]|(-inf-1.13]|0|1|0|0|0|0|0
(1353.5-1359]|(2.3607-inf)|0|0|0|0|0|0|1
(1352.5-1353.5]|(1.13-2.0588]|1|0|0|0|0|0|0
(-inf-1352.5]|(2.3607-inf)|0|0|0|0|0|0|0
(1359-inf)|(-inf-1.13]|0|1|0|0|0|0|0
(1359-inf)|(2.3607-inf)|0|0|0|0|0|0|1
(1359-inf)|(1.13-2.0588]|1|0|0|0|0|0|0
(1353.5-1359]|(-inf-1.13]|0|1|0|0|0|0|0
(1352.5-1353.5]|(2.0588-2.3607]|0|0|0|0|0|0|0
(1353.5-1359]|(2.0588-2.3607]|0|0|0|0|0|0|1
(1359-inf)|(2.0588-2.3607]|0|0|0|0|0|0|1
(-inf-1352.5]|(-inf-1.13]|1|0|0|0|0|0|0
(1352.5-1353.5]|(-inf-1.13]|1|0|0|0|0|0|0
(1353.5-1359]|(-inf-1.13]|1|0|0|0|0|0|0
(1359-inf)|(-inf-1.13]|1|0|0|0|0|0|0
(-inf-1352.5]|(1.13-2.0588]|0|0|0|0|0|0|1
(1352.5-1353.5]|(1.13-2.0588]|0|0|0|0|0|0|1
(1353.5-1359]|(1.13-2.0588]|0|0|0|0|0|0|1
(1359-inf)|(1.13-2.0588]|0|0|0|0|0|0|1
(-inf-1352.5]|(-inf-1.13]|0|0|0|0|0|0|1
(1352.5-1353.5]|(-inf-1.13]|0|0|0|0|0|0|1
(1353.5-1359]|(-inf-1.13]|0|0|0|0|0|0|1
(1359-inf)|(-inf-1.13]|0|0|0|0|0|0|1

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
					* Dirtiness != 0: 0 (49.0)
				* Stains != 0: 0 (65.0)
			* Pastry != 0: 0 (142.0)
		* Z_Scratch != 0: 0 (171.0)
	* K_Scatch != 0: 0 (352.0)
* Bumps != 0: 0 (361.0)


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
	* K_Scatch!=(0): 0(352.0/0.0)
* Bumps!=(0): 0(361.0/0.0)


