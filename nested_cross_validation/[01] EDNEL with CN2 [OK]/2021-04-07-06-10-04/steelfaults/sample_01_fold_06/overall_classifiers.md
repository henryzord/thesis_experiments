# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Bumps!=(0) | 0 | 0.653295 |
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

y_minimum|y_maximum|pixels_areas|typeofsteel_a300|typeofsteel_a400|empty_index|logofareas|pastry|z_scratch|k_scatch|stains|dirtiness|bumps|other_faults
---|---|---|---|---|---|---|---|---|---|---|---|---|---
(450872-inf)|(450883.5-inf)|(3606.5-inf)|0|1|all|(3.5571-inf)|0|0|0|0|0|1|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|1|0|all|(3.5571-inf)|0|0|0|0|0|1|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|0|1|all|(3.5571-inf)|0|0|1|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(3606.5-inf)|0|1|all|(3.5571-inf)|0|0|1|0|0|0|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|0|1|all|(3.5571-inf)|0|1|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|0|1|all|(3.5571-inf)|1|0|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|1|0|all|(3.5571-inf)|0|1|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(3606.5-inf)|1|0|all|(3.5571-inf)|0|1|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(3606.5-inf)|0|1|all|(3.5571-inf)|1|0|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|0|1|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|1|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|0|1|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|0|0|1|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|1|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|0|1|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|1|0|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|0|0|1|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|1|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|1|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|1|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|1|0|0|0|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|0|1|all|(3.5571-inf)|0|0|0|0|0|0|1
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|1|0|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|1|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(3606.5-inf)|0|1|all|(3.5571-inf)|0|0|0|0|0|0|1
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|1|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(3606.5-inf)|1|0|all|(3.5571-inf)|0|0|0|0|0|0|1
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|1|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|1|0|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|1|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|1|0|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|1|0|0|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|1|0|0|0|0|0|0
(450872-inf)|(450883.5-inf)|(-inf-23.5]|0|1|all|(-inf-1.37015]|0|0|0|1|0|0|0
(450872-inf)|(450883.5-inf)|(-inf-23.5]|0|1|all|(-inf-1.37015]|0|0|1|0|0|0|0
(-inf-450872]|(-inf-450883.5]|(-inf-23.5]|0|1|all|(-inf-1.37015]|0|0|0|1|0|0|0
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|0|0|1
(450872-inf)|(450883.5-inf)|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|0|0|0|1
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|0|1|all|(1.37015-3.5571]|0|0|0|0|0|0|1
(-inf-450872]|(-inf-450883.5]|(23.5-3606.5]|1|0|all|(1.37015-3.5571]|0|0|0|0|0|0|1
(-inf-450872]|(-inf-450883.5]|(-inf-23.5]|1|0|all|(-inf-1.37015]|0|0|0|0|0|0|0

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
					* Dirtiness = 0: 1 (404.0)
					* Dirtiness = 1: 0 (31.0)
				* Stains = 1: 0 (38.0)
			* Pastry = 1: 0 (93.0)
		* Z_Scratch = 1: 0 (116.0)
	* K_Scatch = 1: 0 (236.0)
* Bumps = 1: 0 (246.0)


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


