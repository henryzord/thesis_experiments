# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 2 | 0.402516 |
| OD280/OD315 > 2.15 and Alcohol > 12.82 and Proline > 750.0 | 1 | 0.320636 |
| OD280/OD315 <= 2.15 | 3 | 0.228707 |
| Alcohol > 12.78 and Ash > 2.03 and flavanoids > 2.31 and ColorIntensity > 3.46 and ColorIntensity <= 7.075 | 1 | 0.298013 |
| Proline < 755.0 and OD280/OD315 >= 2.115 and flavanoids < 0.7949999999999999 | 3 | 0.016807 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| OD280/OD315 <= 2.11 and Hue <= 0.82 | 3 | 0.230263 |
| flavanoids <= 0.92 and Alcohol >= 12.84 | 3 | 0.056452 |
| Proline >= 760 and ColorIntensity >= 3.52 | 1 | 0.443478 |
| Alcohol >= 13.24 and Alcohol <= 13.24 | 1 | 0.030303 |
|  | 2 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

alcohol|ash|flavanoids|colorintensity|class
---|---|---|---|---
(12.78-inf)|(2.03-inf)|(2.31-inf)|(7.075-inf)|1
(12.78-inf)|(2.03-inf)|(2.31-inf)|(3.46-7.075]|1
(-inf-12.78]|(2.03-inf)|(2.31-inf)|(3.46-7.075]|2
(12.78-inf)|(2.03-inf)|(0.975-1.58]|(7.075-inf)|3
(12.78-inf)|(-inf-2.03]|(2.31-inf)|(3.46-7.075]|1
(12.78-inf)|(2.03-inf)|(1.58-2.31]|(3.46-7.075]|1
(-inf-12.78]|(2.03-inf)|(1.58-2.31]|(3.46-7.075]|1
(-inf-12.78]|(-inf-2.03]|(1.58-2.31]|(3.46-7.075]|1
(-inf-12.78]|(2.03-inf)|(-inf-0.975]|(7.075-inf)|3
(12.78-inf)|(-inf-2.03]|(1.58-2.31]|(3.46-7.075]|1
(12.78-inf)|(2.03-inf)|(-inf-0.975]|(7.075-inf)|3
(12.78-inf)|(2.03-inf)|(2.31-inf)|(-inf-3.46]|2
(-inf-12.78]|(2.03-inf)|(2.31-inf)|(-inf-3.46]|2
(-inf-12.78]|(2.03-inf)|(0.975-1.58]|(3.46-7.075]|2
(12.78-inf)|(2.03-inf)|(0.975-1.58]|(3.46-7.075]|3
(-inf-12.78]|(-inf-2.03]|(2.31-inf)|(-inf-3.46]|2
(-inf-12.78]|(-inf-2.03]|(0.975-1.58]|(3.46-7.075]|2
(-inf-12.78]|(2.03-inf)|(1.58-2.31]|(-inf-3.46]|2
(-inf-12.78]|(-inf-2.03]|(1.58-2.31]|(-inf-3.46]|2
(12.78-inf)|(2.03-inf)|(-inf-0.975]|(3.46-7.075]|3
(-inf-12.78]|(2.03-inf)|(-inf-0.975]|(3.46-7.075]|3
(12.78-inf)|(2.03-inf)|(0.975-1.58]|(-inf-3.46]|1
(-inf-12.78]|(2.03-inf)|(0.975-1.58]|(-inf-3.46]|2
(-inf-12.78]|(-inf-2.03]|(0.975-1.58]|(-inf-3.46]|2
(-inf-12.78]|(-inf-2.03]|(-inf-0.975]|(-inf-3.46]|1

## JRip

Decision list:

rules | predicted class
---|---
(OD280/OD315 <= 2.11) and (Hue <= 0.82)|3 (35.0/0.0)
(flavanoids <= 0.92) and (Alcohol >= 12.84)|3 (7.0/0.0)
(Proline >= 760) and (ColorIntensity >= 3.52)|1 (51.0/0.0)
(Alcohol >= 13.24) and (Alcohol <= 13.24)|1 (2.0/0.0)
|2 (64.0/0.0)


## J48 Decision Tree

* OD280/OD315 <= 2.15: 3 (41.0/6.0)
* OD280/OD315 > 2.15
	* Alcohol <= 12.82: 2 (42.0)
	* Alcohol > 12.82
		* Proline <= 750.0: 2 (6.0/2.0)
		* Proline > 750.0: 1 (44.0/1.0)


## SimpleCart Decision Tree

* Proline < 755.0
	* OD280/OD315 < 2.115
		* Hue < 0.935: 3(35.0/1.0)
		* Hue >= 0.935: 2(4.0/1.0)
	* OD280/OD315 >= 2.115
		* flavanoids < 0.7949999999999999: 3(2.0/0.0)
		* flavanoids >= 0.7949999999999999
			* Alcohol < 13.175: 2(52.0/0.0)
			* Alcohol >= 13.175
				* Alcohol < 13.365: 1(2.0/0.0)
				* Alcohol >= 13.365: 2(3.0/0.0)
* Proline >= 755.0
	* flavanoids < 2.165
		* Alcohol < 12.37: 2(2.0/0.0)
		* Alcohol >= 12.37: 3(4.0/0.0)
	* flavanoids >= 2.165
		* Magnesium < 133.5: 1(51.0/0.0)
		* Magnesium >= 133.5: 2(2.0/0.0)


