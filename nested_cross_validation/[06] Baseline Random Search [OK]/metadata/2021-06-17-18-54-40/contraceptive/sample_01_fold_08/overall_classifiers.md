# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426848 |
| Children > 0.0 and Wife_education <= 3.0 and Husband_education > 1.0 and Wife_age <= 37.0 | 3 | 0.140165 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.060133 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 | 3 | 0.043212 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 | 3 | 0.009540 |
| Children > 0.0 and Wife_education > 3.0 and Children <= 2.0 and Wife_age <= 41.0 and Husband_occupation <= 1.0 and Wife_religion > 0.0 and Wife_age <= 25.0 | 2 | 0.005339 |
| Children > 0.0 and Wife_education > 3.0 and Children <= 2.0 and Wife_age <= 41.0 and Husband_occupation <= 1.0 and Wife_religion > 0.0 and Wife_age > 25.0 and Children > 1.0 and Wife_age <= 29.0 | 2 | 0.003670 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 | 3 | 0.024814 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 | 3 | 0.014108 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Children > 2.5 | 3 | 0.030583 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 3 | 0.010656 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.0 | 1 | 0.097442 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Media_exposure > 0.0 | 1 | 0.045495 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working <= 0.0 and Wife_education <= 2.0 | 1 | 0.020349 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working > 0.0 and Wife_age <= 46.0 and Husband_education > 2.0 and Wife_age <= 41.0 | 1 | 0.016628 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working > 0.0 and Wife_age > 46.0 | 1 | 0.033087 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working > 0.0 and Husband_education <= 2.0 | 1 | 0.014474 |
| Wife_education <= 3.0 and Wife_age > 41.0 and Husband_education <= 3.0 and Wife_age <= 43.0 | 1 | 0.005607 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Children <= 2.0 and Wife_age <= 30.0 and Wife_working > 0.0 and Husband_occupation > 1.0 and Husband_occupation <= 2.0 | 3 | 0.017811 |
| Wife_education <= 3.0 and Wife_age <= 41.0 and Children > 2.0 and Husband_occupation > 1.0 and Husband_education > 1.0 and Wife_religion > 0.0 and Standard-of-living > 2.0 | 3 | 0.093314 |
| Wife_education <= 3.0 and Standard-of-living <= 2.0 and Husband_occupation > 1.0 and Wife_age <= 32.0 and Children > 1.0 and Wife_education <= 2.0 and Standard-of-living <= 1.0 | 1 | 0.018519 |
| Wife_education <= 3.0 and Standard-of-living <= 2.0 and Husband_occupation > 1.0 and Wife_age <= 32.0 and Children > 1.0 and Standard-of-living > 1.0 and Children <= 3.0 | 3 | 0.021012 |
| Wife_education <= 2.0 and Wife_religion > 0.0 and Wife_working <= 0.0 | 1 | 0.019453 |
| Children <= 2.0 and Wife_age > 30.0 and Children <= 1.0 | 1 | 0.039392 |
| Wife_education > 3.0 and Wife_age > 28.0 and Wife_age > 47.0 | 1 | 0.006102 |
| Wife_education > 3.0 and Wife_age > 28.0 and Children > 2.0 and Husband_education > 3.0 and Standard-of-living > 3.0 and Wife_religion <= 0.0 and Wife_working > 0.0 and Children > 3.0 | 2 | 0.017396 |
| Wife_education > 3.0 and Husband_education <= 3.0 | 3 | 0.017645 |
| Wife_education > 3.0 and Children > 2.0 and Wife_age <= 28.0 and Husband_occupation > 1.0 | 3 | 0.014881 |
| Wife_education > 3.0 and Children > 2.0 and Wife_age > 28.0 and Standard-of-living <= 3.0 | 2 | 0.026056 |
| Wife_education > 3.0 and Children > 2.0 and Wife_age > 30.0 and Wife_age > 32.0 | 2 | 0.068035 |
| Wife_education <= 2.0 and Husband_education <= 3.0 and Media_exposure <= 0.0 and Husband_education > 2.0 | 1 | 0.036782 |
| Media_exposure > 0.0 | 1 | 0.014056 |
| Wife_religion <= 0.0 and Children <= 3.0 and Wife_age <= 36.0 and Children > 1.0 and Children <= 2.0 and Standard-of-living > 3.0 | 3 | 0.009400 |
| Wife_age > 40.0 and Standard-of-living > 3.0 | 1 | 0.013923 |
| Wife_age <= 41.0 and Wife_education <= 2.0 and Husband_occupation > 1.0 and Children > 1.0 | 1 | 0.018648 |
| Wife_age <= 41.0 and Wife_education <= 2.0 | 3 | 0.081421 |
| Wife_age <= 41.0 and Wife_religion <= 0.0 and Husband_occupation > 2.0 | 3 | 0.026337 |
| Wife_age <= 41.0 and Wife_religion > 0.0 and Husband_occupation > 1.0 and Wife_age <= 34.0 and Standard-of-living <= 3.0 and Children <= 2.0 and Wife_working > 0.0 | 3 | 0.043964 |
| Wife_age <= 41.0 and Standard-of-living > 1.0 and Husband_education <= 3.0 and Wife_age > 25.0 | 2 | 0.053714 |
| Children <= 6.0 and Standard-of-living > 1.0 and Husband_education > 3.0 and Standard-of-living > 3.0 and Wife_working <= 0.0 | 3 | 0.058150 |
| Children <= 6.0 and Standard-of-living > 1.0 and Husband_education > 3.0 and Wife_working <= 0.0 and Wife_age > 25.0 | 2 | 0.042320 |
| Wife_working > 0.0 and Children <= 6.0 and Standard-of-living > 1.0 and Wife_religion <= 0.0 | 2 | 0.026602 |
| Children <= 6.0 and Wife_working > 0.0 and Standard-of-living > 1.0 and Wife_education > 3.0 and Children <= 2.0 and Standard-of-living > 3.0 and Children > 1.0 | 3 | 0.027574 |
| Wife_age <= 35.0 and Standard-of-living > 1.0 and Husband_education > 3.0 and Wife_working > 0.0 and Wife_education > 3.0 and Wife_age > 24.0 | 1 | 0.076123 |
| Wife_working > 0.0 and Wife_age <= 35.0 and Wife_education > 3.0 | 2 | 0.049330 |
| Wife_age <= 35.0 and Children > 1.0 and Standard-of-living > 2.0 and Husband_occupation <= 1.0 and Wife_age > 28.0 | 1 | 0.015898 |
| Wife_age <= 34.0 and Children > 1.0 and Standard-of-living <= 3.0 | 3 | 0.072532 |
| Wife_working > 0.0 | 2 | 0.124077 |
|  | 1 | 0.531381 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 33 | 2 | 0.056043 |
| Wife_age <= 37 and Children >= 3 | 3 | 0.151152 |
|  | 1 | 0.567134 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(31.5-41.5]|(3.5-inf)|(2.5-inf)|2
(-inf-31.5]|(3.5-inf)|(2.5-inf)|3
(41.5-inf)|(3.5-inf)|(2.5-inf)|2
(41.5-inf)|(2.5-3.5]|(2.5-inf)|1
(31.5-41.5]|(2.5-3.5]|(2.5-inf)|3
(-inf-31.5]|(2.5-3.5]|(2.5-inf)|3
(31.5-41.5]|(3.5-inf)|(0.5-2.5]|3
(41.5-inf)|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(2.5-inf)|3
(31.5-41.5]|(-inf-2.5]|(2.5-inf)|3
(41.5-inf)|(-inf-2.5]|(2.5-inf)|1
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|3
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(31.5-41.5]|(2.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|3
(41.5-inf)|(3.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(3.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|1
(31.5-41.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 33)|2 (208.0/98.0)
(Wife_age <= 37) and (Children >= 3)|3 (355.0/165.0)
|1 (763.0/332.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.0|1 (86.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Media_exposure > 0.0|1 (42.0/3.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working <= 0.0 AND Wife_education <= 2.0|1 (27.0/6.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working > 0.0 AND Wife_age <= 46.0 AND Husband_education > 2.0 AND Wife_age <= 41.0|1 (38.0/16.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working > 0.0 AND Wife_age > 46.0|1 (36.0/5.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working > 0.0 AND Husband_education <= 2.0|1 (20.0/4.0)
Wife_education <= 3.0 AND Wife_age > 41.0 AND Husband_education <= 3.0 AND Wife_age <= 43.0|1 (15.0/7.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Children <= 2.0 AND Wife_age <= 30.0 AND Wife_working > 0.0 AND Husband_occupation > 1.0 AND Husband_occupation <= 2.0|3 (42.0/20.0)
Wife_education <= 3.0 AND Wife_age <= 41.0 AND Children > 2.0 AND Husband_occupation > 1.0 AND Husband_education > 1.0 AND Wife_religion > 0.0 AND Standard-of-living > 2.0|3 (147.0/52.0)
Wife_education <= 3.0 AND Standard-of-living <= 2.0 AND Husband_occupation > 1.0 AND Wife_age <= 32.0 AND Children > 1.0 AND Wife_education <= 2.0 AND Standard-of-living <= 1.0|1 (27.0/9.0)
Wife_education <= 3.0 AND Standard-of-living <= 2.0 AND Husband_occupation > 1.0 AND Wife_age <= 32.0 AND Children > 1.0 AND Standard-of-living > 1.0 AND Children <= 3.0|3 (30.0/9.0)
Wife_education <= 2.0 AND Wife_religion > 0.0 AND Wife_working <= 0.0|1 (28.0/11.0)
Children <= 2.0 AND Wife_age > 30.0 AND Children <= 1.0|1 (38.0/7.0)
Wife_education > 3.0 AND Wife_age > 28.0 AND Wife_age > 47.0|1 (17.0/9.0)
Wife_education > 3.0 AND Wife_age > 28.0 AND Children > 2.0 AND Husband_education > 3.0 AND Standard-of-living > 3.0 AND Wife_religion <= 0.0 AND Wife_working > 0.0 AND Children > 3.0|2 (16.0/5.0)
Wife_education > 3.0 AND Husband_education <= 3.0|3 (23.0/9.0)
Wife_education > 3.0 AND Children > 2.0 AND Wife_age <= 28.0 AND Husband_occupation > 1.0|3 (12.0/2.0)
Wife_education > 3.0 AND Children > 2.0 AND Wife_age > 28.0 AND Standard-of-living <= 3.0|2 (42.0/18.0)
Wife_education > 3.0 AND Children > 2.0 AND Wife_age > 30.0 AND Wife_age > 32.0|2 (130.0/60.0)
Wife_education <= 2.0 AND Husband_education <= 3.0 AND Media_exposure <= 0.0 AND Husband_education > 2.0|1 (31.0/10.0)
Media_exposure > 0.0|1 (25.0/12.0)
Wife_religion <= 0.0 AND Children <= 3.0 AND Wife_age <= 36.0 AND Children > 1.0 AND Children <= 2.0 AND Standard-of-living > 3.0|3 (13.0/6.0)
Wife_age > 40.0 AND Standard-of-living > 3.0|1 (20.0/10.0)
Wife_age <= 41.0 AND Wife_education <= 2.0 AND Husband_occupation > 1.0 AND Children > 1.0|1 (24.0/10.0)
Wife_age <= 41.0 AND Wife_education <= 2.0|3 (25.0/10.0)
Wife_age <= 41.0 AND Wife_religion <= 0.0 AND Husband_occupation > 2.0|3 (17.0/7.0)
Wife_age <= 41.0 AND Wife_religion > 0.0 AND Husband_occupation > 1.0 AND Wife_age <= 34.0 AND Standard-of-living <= 3.0 AND Children <= 2.0 AND Wife_working > 0.0|3 (61.0/27.0)
Wife_age <= 41.0 AND Standard-of-living > 1.0 AND Husband_education <= 3.0 AND Wife_age > 25.0|2 (27.0/16.0)
Children <= 6.0 AND Standard-of-living > 1.0 AND Husband_education > 3.0 AND Standard-of-living > 3.0 AND Wife_working <= 0.0|3 (49.0/22.0)
Children <= 6.0 AND Standard-of-living > 1.0 AND Husband_education > 3.0 AND Wife_working <= 0.0 AND Wife_age > 25.0|2 (19.0/11.0)
Wife_working > 0.0 AND Children <= 6.0 AND Standard-of-living > 1.0 AND Wife_religion <= 0.0|2 (29.0/17.0)
Children <= 6.0 AND Wife_working > 0.0 AND Standard-of-living > 1.0 AND Wife_education > 3.0 AND Children <= 2.0 AND Standard-of-living > 3.0 AND Children > 1.0|3 (26.0/12.0)
Wife_age <= 35.0 AND Standard-of-living > 1.0 AND Husband_education > 3.0 AND Wife_working > 0.0 AND Wife_education > 3.0 AND Wife_age > 24.0|1 (37.0/20.0)
Wife_working > 0.0 AND Wife_age <= 35.0 AND Wife_education > 3.0|2 (24.0/11.0)
Wife_age <= 35.0 AND Children > 1.0 AND Standard-of-living > 2.0 AND Husband_occupation <= 1.0 AND Wife_age > 28.0|1 (17.0/10.0)
Wife_age <= 34.0 AND Children > 1.0 AND Standard-of-living <= 3.0|3 (24.0/9.0)
Wife_working > 0.0|2 (27.0/14.0)
|1 (15.0/5.0)


## J48 Decision Tree

* Children <= 0.0: 1 (54.0/2.0)
* Children > 0.0
	* Wife_education <= 3.0
		* Husband_education <= 1.0: 1 (23.0/6.0)
		* Husband_education > 1.0
			* Wife_age <= 37.0: 3 (353.0/194.0)
			* Wife_age > 37.0: 1 (132.0/45.0)
	* Wife_education > 3.0
		* Children <= 2.0
			* Wife_age <= 41.0
				* Husband_occupation <= 1.0
					* Wife_religion <= 0.0: 3 (15.0/8.0)
					* Wife_religion > 0.0
						* Wife_age <= 25.0: 2 (22.0/13.0)
						* Wife_age > 25.0
							* Children <= 1.0: 1 (12.0/2.0)
							* Children > 1.0
								* Wife_age <= 29.0: 2 (9.0/4.0)
								* Wife_age > 29.0: 1 (10.0/5.0)
				* Husband_occupation > 1.0: 3 (65.0/26.0)
			* Wife_age > 41.0: 1 (12.0)
		* Children > 2.0
			* Wife_age <= 28.0
				* Husband_occupation <= 1.0: 1 (9.0/4.0)
				* Husband_occupation > 1.0: 3 (9.0/1.0)
			* Wife_age > 28.0: 2 (159.0/75.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(84.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/120.0)
			* Children >= 2.5: 3(163.0/136.0)
		* Wife_age >= 37.5: 1(154.0/63.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5: 3(85.0/115.0)
			* Wife_age >= 39.5: 1(17.0/4.0)
		* Children >= 2.5: 2(127.0/137.0)


