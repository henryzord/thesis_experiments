# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.652921 |
| Y_Minimum > 457727 and Y_Maximum > 457744.5 and Pixels_Areas > 23 and Pixels_Areas <= 3607 and TypeOfSteel_A300 = 1 and Empty_Index = all and LogOfAreas > 1.3613 and LogOfAreas <= 3.55715 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.144144 |
| Y_Minimum <= 457727 and Y_Maximum <= 457744.5 and Pixels_Areas > 3607 and TypeOfSteel_A300 = 0 and Empty_Index = all and LogOfAreas > 3.55715 and Pastry = 0 and Z_Scratch = 0 and K_Scatch = 0 and Stains = 0 and Dirtiness = 0 and Bumps = 0 | 1 | 0.002625 |
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

y_minimum|y_maximum|pixels_areas|typeofsteel_a300|empty_index|logofareas|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---|---|---|---|---|---
(457727-inf)|(457744.5-inf)|(3607-inf)|1|all|(3.55715-inf)|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(3607-inf)|0|all|(3.55715-inf)|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(3607-inf)|1|all|(3.55715-inf)|0|1|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(3607-inf)|1|all|(3.55715-inf)|0|1|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(3607-inf)|1|all|(3.55715-inf)|1|0|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(3607-inf)|0|all|(3.55715-inf)|0|0|1|0|0|0|0
(457727-inf)|(457744.5-inf)|(3607-inf)|0|all|(3.55715-inf)|0|1|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(3607-inf)|0|all|(3.55715-inf)|0|0|1|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(3607-inf)|0|all|(3.55715-inf)|1|0|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|0|1|0|0
(-inf-457727]|(-inf-457744.5]|(3607-inf)|0|all|(3.55715-inf)|1|0|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|1|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|0|0|1|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(3607-inf)|1|all|(3.55715-inf)|0|0|0|0|0|0|1
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|0|1|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|0|1|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|1|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|1|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|1|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|1|all|(1.3613-3.55715]|0|1|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|1|0|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|1|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|1|all|(1.3613-3.55715]|1|0|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|0|1|0|0|0|0
(457727-inf)|(457744.5-inf)|(3607-inf)|0|all|(3.55715-inf)|0|0|0|0|0|0|1
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|1|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|0|1|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(3607-inf)|0|all|(3.55715-inf)|0|0|0|0|0|0|1
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|1|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|1|0|0|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|1|0|0|0|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|0|0|0|1
(-inf-457727]|(-inf-457744.5]|(23-3607]|1|all|(1.3613-3.55715]|0|0|0|0|0|0|1
(457727-inf)|(457744.5-inf)|(-inf-23]|0|all|(-inf-1.3613]|0|0|0|1|0|0|0
(457727-inf)|(457744.5-inf)|(-inf-23]|0|all|(-inf-1.3613]|0|0|1|0|0|0|0
(-inf-457727]|(-inf-457744.5]|(-inf-23]|0|all|(-inf-1.3613]|0|0|0|1|0|0|0
(457727-inf)|(457744.5-inf)|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|0|0|1
(-inf-457727]|(-inf-457744.5]|(23-3607]|0|all|(1.3613-3.55715]|0|0|0|0|0|0|1
(-inf-457727]|(-inf-457744.5]|(-inf-23]|1|all|(-inf-1.3613]|0|0|0|0|0|0|1

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
					* Dirtiness = 1: 0 (49.0)
				* Stains = 1: 0 (65.0)
			* Pastry = 1: 0 (142.0)
		* Z_Scratch = 1: 0 (170.0)
	* K_Scatch = 1: 0 (352.0)
* Bumps = 1: 0 (362.0)


## SimpleCart Decision Tree

* Bumps=(0)
	* K_Scatch=(0)
		* Z_Scratch=(0)
			* Pastry=(0)
				* Stains=(0)
					* Dirtiness=(0): 1(606.0/0.0)
					* Dirtiness!=(0): 0(49.0/0.0)
				* Stains!=(0): 0(65.0/0.0)
			* Pastry!=(0): 0(142.0/0.0)
		* Z_Scratch!=(0): 0(170.0/0.0)
	* K_Scatch!=(0): 0(352.0/0.0)
* Bumps!=(0): 0(362.0/0.0)


