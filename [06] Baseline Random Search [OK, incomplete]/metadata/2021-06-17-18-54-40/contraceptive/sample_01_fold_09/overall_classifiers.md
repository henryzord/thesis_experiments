# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_education < 3.5 and Wife_age >= 37.5 | 1 | 0.124348 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.104163 |
| Children < 0.5 | 1 | 0.100645 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children < 2.5 | 1 | 0.078977 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.057506 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 | 3 | 0.040486 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 2.5 | 3 | 0.025355 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age >= 39.5 | 1 | 0.017430 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 5.5 | 3 | 0.012756 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.010654 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 5.5 | 1 | 0.004665 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 5.5 | 1 | 0.003649 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 5.5 | 1 | 0.002111 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 5.5 | 3 | 0.002076 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.012754 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.052155 |
| Children >= 3 and Husband_occupation >= 3 and Wife_age <= 30 | 3 | 0.063905 |
| Wife_age <= 37 and Wife_education <= 2 and Children >= 3 | 3 | 0.037473 |
| Children >= 2 and Wife_age <= 27 and Husband_occupation >= 2 and Husband_occupation <= 2 | 3 | 0.020672 |
| Children >= 1 and Wife_age <= 22 and Husband_occupation >= 2 | 3 | 0.031661 |
| Wife_education >= 3 and Wife_working <= 0 and Standard-of-living >= 4 and Children >= 3 | 3 | 0.021113 |
|  | 1 | 0.572874 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(46.5-inf)|(3.5-inf)|(5.5-inf)|1
(31.5-37.5]|(3.5-inf)|(5.5-inf)|3
(37.5-46.5]|(3.5-inf)|(5.5-inf)|2
(46.5-inf)|(2.5-3.5]|(5.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(5.5-inf)|3
(37.5-46.5]|(2.5-3.5]|(5.5-inf)|1
(31.5-37.5]|(2.5-3.5]|(5.5-inf)|1
(37.5-46.5]|(-inf-2.5]|(5.5-inf)|1
(-inf-31.5]|(-inf-2.5]|(5.5-inf)|3
(46.5-inf)|(3.5-inf)|(2.5-5.5]|1
(-inf-31.5]|(3.5-inf)|(2.5-5.5]|3
(31.5-37.5]|(3.5-inf)|(2.5-5.5]|2
(31.5-37.5]|(-inf-2.5]|(5.5-inf)|3
(46.5-inf)|(-inf-2.5]|(5.5-inf)|1
(37.5-46.5]|(3.5-inf)|(2.5-5.5]|2
(37.5-46.5]|(2.5-3.5]|(2.5-5.5]|1
(46.5-inf)|(2.5-3.5]|(2.5-5.5]|1
(-inf-31.5]|(2.5-3.5]|(2.5-5.5]|3
(31.5-37.5]|(2.5-3.5]|(2.5-5.5]|3
(46.5-inf)|(3.5-inf)|(0.5-2.5]|1
(46.5-inf)|(-inf-2.5]|(2.5-5.5]|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|1
(37.5-46.5]|(-inf-2.5]|(2.5-5.5]|1
(31.5-37.5]|(-inf-2.5]|(2.5-5.5]|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|3
(-inf-31.5]|(-inf-2.5]|(2.5-5.5]|3
(46.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|3
(31.5-37.5]|(2.5-3.5]|(0.5-2.5]|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(37.5-46.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(-inf-2.5]|(0.5-2.5]|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(-inf-0.5]|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (180.0/81.0)
(Children >= 3) and (Husband_occupation >= 3) and (Wife_age <= 30)|3 (112.0/36.0)
(Wife_age <= 37) and (Wife_education <= 2) and (Children >= 3)|3 (110.0/49.0)
(Children >= 2) and (Wife_age <= 27) and (Husband_occupation >= 2) and (Husband_occupation <= 2)|3 (43.0/15.0)
(Children >= 1) and (Wife_age <= 22) and (Husband_occupation >= 2)|3 (91.0/42.0)
(Wife_education >= 3) and (Wife_working <= 0) and (Standard-of-living >= 4) and (Children >= 3)|3 (25.0/6.0)
|1 (765.0/336.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(87.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/116.0)
			* Children >= 2.5: 3(169.0/136.0)
		* Wife_age >= 37.5: 1(151.0/66.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5: 3(83.0/123.0)
			* Wife_age >= 39.5: 1(16.0/3.0)
		* Children >= 2.5: 2(122.0/133.0)


