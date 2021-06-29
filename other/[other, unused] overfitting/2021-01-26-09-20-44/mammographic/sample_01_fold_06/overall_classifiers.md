# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS <= 4 and Shape <= 3 | 0 | 0.454586 |
| BI-RADS > 4 | 1 | 0.356229 |
| BI-RADS <= 4 and Shape > 3 and Age > 47 | 1 | 0.077864 |
| BI-RADS <= 4.5 and Age > 39.5 and Age <= 57.5 and Margin > 1.5 and Margin <= 4.5 | 0 | 0.103768 |
| BI-RADS < 4.5 and Shape >= 3.5 and Age >= 47.5 and Age < 69.5 and Margin < 3.5 | 0 | 0.012562 |
| BI-RADS <= 4 and Shape > 3 and Age <= 47 | 0 | 0.026494 |
| BI-RADS <= 4.5 and Age > 64.5 and Margin > 1.5 and Margin <= 4.5 | 1 | 0.027056 |
| BI-RADS <= 4.5 and Age > 57.5 and Age <= 64.5 and Margin > 1.5 and Margin <= 4.5 | 0 | 0.039935 |
| BI-RADS <= 4.5 and Age > 57.5 and Age <= 64.5 and Margin > 4.5 | 0 | 0.005583 |
| BI-RADS > 4.5 and Age > 57.5 and Age <= 64.5 and Margin = ? | 0 | 0.007426 |
| BI-RADS <= 4.5 and Age > 64.5 and Margin > 4.5 | 1 | 0.017730 |
| BI-RADS <= 4.5 and Age > 39.5 and Age <= 57.5 and Margin > 4.5 | 1 | 0.013342 |
| BI-RADS > 4.5 and Age <= 39.5 and Margin = ? | 0 | 0.002488 |
| BI-RADS > 4.5 and Age > 64.5 and Margin = ? | 0 | 0.000833 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| BI-RADS > 4.5 and Shape > 3.5 | 1 | 0.303145 |
| BI-RADS > 4.5 and Density > 2.5 and Margin > 1.5 | 1 | 0.071209 |
| Shape <= 3.5 and Age > 40.5 and BI-RADS <= 4.5 | 0 | 0.646993 |
| Age <= 40.5 | 0 | 0.461454 |
| BI-RADS > 3.5 and BI-RADS > 4.5 and Density > 2.5 and BI-RADS <= 5.5 | 1 | 0.030993 |
| Margin > 4.5 | 1 | 0.156331 |
| BI-RADS <= 3.5 | 0 | 0.022727 |
| BI-RADS > 4.5 and Density <= 2.5 | 1 | 0.030000 |
|  | 1 | 0.573099 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

bi-rads|age|margin|severity
---|---|---|---
(-inf-4.5]|(64.5-inf)|(4.5-inf)|1
(4.5-inf)|(64.5-inf)|(4.5-inf)|1
(-inf-4.5]|(64.5-inf)|?|0
(4.5-inf)|(64.5-inf)|?|0
?|(64.5-inf)|?|0
(4.5-inf)|(57.5-64.5]|(4.5-inf)|1
(-inf-4.5]|(57.5-64.5]|(4.5-inf)|0
(-inf-4.5]|?|(4.5-inf)|0
(-inf-4.5]|(57.5-64.5]|?|0
(4.5-inf)|(57.5-64.5]|?|0
(-inf-4.5]|(39.5-57.5]|(4.5-inf)|1
(4.5-inf)|(39.5-57.5]|(4.5-inf)|1
(4.5-inf)|(64.5-inf)|(1.5-4.5]|1
(-inf-4.5]|(64.5-inf)|(1.5-4.5]|1
(4.5-inf)|(39.5-57.5]|?|1
(-inf-4.5]|(39.5-57.5]|?|0
(4.5-inf)|(-inf-39.5]|(4.5-inf)|0
(-inf-4.5]|(57.5-64.5]|(1.5-4.5]|0
(4.5-inf)|(57.5-64.5]|(1.5-4.5]|1
(4.5-inf)|?|(1.5-4.5]|1
(4.5-inf)|(-inf-39.5]|?|0
(-inf-4.5]|(-inf-39.5]|?|0
?|(39.5-57.5]|(1.5-4.5]|0
(4.5-inf)|(64.5-inf)|(-inf-1.5]|1
(4.5-inf)|(39.5-57.5]|(1.5-4.5]|1
(-inf-4.5]|(64.5-inf)|(-inf-1.5]|0
(-inf-4.5]|(39.5-57.5]|(1.5-4.5]|0
(4.5-inf)|(-inf-39.5]|(1.5-4.5]|1
(4.5-inf)|(57.5-64.5]|(-inf-1.5]|1
(-inf-4.5]|(-inf-39.5]|(1.5-4.5]|0
(-inf-4.5]|(57.5-64.5]|(-inf-1.5]|0
(4.5-inf)|(39.5-57.5]|(-inf-1.5]|1
(-inf-4.5]|(39.5-57.5]|(-inf-1.5]|0
(4.5-inf)|(-inf-39.5]|(-inf-1.5]|0
(-inf-4.5]|(-inf-39.5]|(-inf-1.5]|0

## PART

Decision list:

rules | predicted class
---|---
BI-RADS > 4.5 AND Shape > 3.5|1 (218.27/19.14)
BI-RADS > 4.5 AND Density > 2.5 AND Margin > 1.5|1 (49.32/8.13)
Shape <= 3.5 AND Age > 40.5 AND BI-RADS <= 4.5|0 (271.46/42.39)
Age <= 40.5|0 (109.73/3.48)
BI-RADS > 3.5 AND BI-RADS > 4.5 AND Density > 2.5 AND BI-RADS <= 5.5|1 (9.54/2.9)
Margin > 4.5|1 (24.37/6.17)
BI-RADS <= 3.5|0 (8.55/2.19)
BI-RADS > 4.5 AND Density <= 2.5|1 (3.1/0.04)
|1 (73.67/32.96)


## J48 Decision Tree

* BI-RADS <= 4
	* Shape <= 3: 0 (420.42/50.34)
	* Shape > 3
		* Age <= 47: 0 (19.07/4.38)
		* Age > 47: 1 (106.77/43.86)
* BI-RADS > 4: 1 (316.73/33.37)


## SimpleCart Decision Tree

* BI-RADS < 4.5
	* Shape < 3.5: 0(370.08/50.33)
	* Shape >= 3.5
		* Age < 47.5: 0(14.69/4.38)
		* Age >= 47.5
			* Age < 69.5
				* Margin < 3.5: 0(9.8/4.55)
				* Margin >= 3.5: 1(42.98/30.59)
			* Age >= 69.5: 1(15.38/3.46)
* BI-RADS >= 4.5: 1(283.36/33.36)


