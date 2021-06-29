# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_age < 37.5 | 3 | 0.226994 |
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education < 3.5 | 1 | 0.125422 |
| Children < 0.5 | 1 | 0.102889 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education <= 2.0 and Husband_education > 1.0 and Children <= 2.0 | 1 | 0.044035 |
| Children > 0.0 and Wife_age > 37.0 and Wife_education > 3.0 and Children > 2.0 and Children <= 8.0 | 2 | 0.040446 |
| Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.030571 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children > 2.0 and Wife_age > 31.0 and Standard-of-living > 3.0 and Wife_age > 32.0 and Wife_education > 3.0 | 2 | 0.018297 |
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education >= 3.5 and Children < 2.5 | 1 | 0.018529 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children <= 2.0 and Wife_age > 30.0 | 1 | 0.024668 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children <= 2.0 and Wife_age <= 30.0 and Husband_occupation <= 1.0 and Wife_age > 20.0 and Wife_age > 23.0 and Wife_working <= 0.0 | 2 | 0.005722 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 | 1 | 0.004967 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children > 2.0 and Wife_age > 31.0 and Standard-of-living <= 3.0 and Wife_working > 0.0 and Children <= 3.0 | 2 | 0.005286 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children <= 2.0 and Wife_age <= 30.0 and Husband_occupation <= 1.0 and Wife_age > 20.0 and Wife_age > 23.0 and Wife_working > 0.0 and Wife_age > 25.0 | 1 | 0.006375 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children <= 2.0 and Wife_age <= 30.0 and Husband_occupation <= 1.0 and Wife_age > 20.0 and Wife_age <= 23.0 | 2 | 0.003976 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education > 2.0 and Children > 2.0 and Wife_age > 31.0 and Standard-of-living <= 3.0 and Wife_working <= 0.0 | 1 | 0.005614 |
| Children > 0.0 and Wife_age <= 37.0 and Wife_education <= 2.0 and Husband_education <= 1.0 | 1 | 0.004611 |
| Wife_age <= 37.5 and Wife_education <= 2.5 and Children > 7.5 | 1 | 0.002114 |
| Children > 0.0 and Wife_age > 37.0 and Wife_education > 3.0 and Children > 2.0 and Children > 8.0 | 3 | 0.003079 |
| Wife_age > 46.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 | 2 | 0.000781 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 7.5 | 3 | 0.002315 |
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.039661 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.5 | 1 | 0.102889 |
| Wife_age > 37.5 and Wife_education <= 3.5 and Media_exposure > 0.5 | 1 | 0.047798 |
| Wife_education <= 3.5 and Wife_age > 35.5 and Children > 1.5 and Wife_age <= 46.5 and Wife_religion > 0.5 | 1 | 0.053826 |
| Wife_age <= 35.5 and Children > 2.5 and Children <= 6.5 and Wife_education <= 3.5 and Husband_occupation > 1.5 and Children <= 4.5 and Wife_religion > 0.5 and Standard-of-living <= 2.5 and Wife_education > 2.5 | 3 | 0.015333 |
| Wife_age <= 35.5 and Children > 2.5 and Standard-of-living > 1.5 and Children <= 6.5 and Wife_education <= 2.5 and Children <= 4.5 and Standard-of-living <= 3.5 | 3 | 0.035469 |
| Wife_age > 44.5 and Children > 2.5 and Standard-of-living > 2.5 and Wife_age <= 48.5 and Wife_education > 3.5 | 2 | 0.013284 |
| Wife_age > 44.5 | 1 | 0.057580 |
| Children > 2.5 and Wife_age > 35.5 and Husband_education > 3.5 and Wife_age <= 42.5 and Wife_age > 37.5 | 2 | 0.038436 |
| Children > 2.5 and Standard-of-living > 1.5 and Wife_education <= 2.5 and Children <= 6.5 and Children > 4.5 | 3 | 0.045144 |
| Wife_education <= 2.5 and Husband_occupation > 1.5 and Children <= 4.5 and Wife_working <= 0.5 | 1 | 0.019695 |
| Wife_education <= 2.5 and Wife_age <= 33.5 and Husband_occupation > 1.5 and Children <= 4.5 and Wife_education > 1.5 and Standard-of-living <= 1.5 | 1 | 0.014493 |
| Children > 2.5 and Wife_education > 2.5 and Wife_age <= 31.5 and Husband_occupation > 2.5 | 3 | 0.046935 |
| Children <= 2.5 and Wife_age <= 22.5 and Husband_occupation > 1.5 and Wife_education <= 3.5 and Husband_education <= 3.5 | 3 | 0.037042 |
| Children <= 2.5 and Standard-of-living <= 2.5 | 1 | 0.034942 |
| Children <= 1.5 and Wife_age > 31.5 | 1 | 0.038057 |
| Wife_education <= 2.5 | 1 | 0.039961 |
| Children > 2.5 and Wife_age > 30.5 and Standard-of-living > 3.5 and Wife_age > 32.5 and Wife_age <= 42.5 and Children <= 5.5 and Wife_religion <= 0.5 | 2 | 0.015051 |
| Wife_age <= 43.5 and Wife_age <= 22.5 and Children <= 1.5 and Wife_age <= 21.5 | 1 | 0.006325 |
| Wife_age > 22.5 and Wife_age <= 43.5 and Wife_age > 23.5 and Children > 1.5 and Wife_age <= 38.5 and Wife_age <= 25.5 | 3 | 0.037470 |
| Wife_age <= 22.5 | 3 | 0.058015 |
| Children > 2.5 and Wife_age > 30.5 and Standard-of-living > 3.5 and Wife_age <= 32.5 | 3 | 0.028174 |
| Children > 5.5 | 3 | 0.054765 |
| Wife_age <= 43.5 and Wife_age > 37.5 | 1 | 0.007873 |
| Wife_age <= 35.5 and Children <= 1.5 and Wife_working > 0.5 | 3 | 0.036518 |
| Children > 1.5 and Wife_age <= 35.5 and Wife_age > 24.5 and Standard-of-living > 2.5 and Wife_working > 0.5 and Wife_age <= 34.5 and Husband_occupation > 1.5 | 3 | 0.050958 |
| Children > 1.5 and Wife_age > 35.5 | 2 | 0.122663 |
| Children > 1.5 and Wife_age > 24.5 and Wife_religion > 0.5 and Husband_occupation <= 2.5 and Wife_working <= 0.5 | 1 | 0.016698 |
| Children > 1.5 and Wife_age > 24.5 and Wife_religion <= 0.5 | 1 | 0.012012 |
| Wife_age > 31.5 and Husband_occupation <= 1.5 and Wife_age > 33.5 | 3 | 0.109379 |
| Wife_age <= 31.5 and Children <= 1.5 | 1 | 0.039376 |
| Wife_age > 31.5 | 2 | 0.159171 |
| Wife_age > 27.5 and Standard-of-living > 3.5 | 1 | 0.034989 |
|  | 2 | 0.444444 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.055787 |
| Wife_age <= 35 and Children >= 3 | 3 | 0.137229 |
| Children >= 1 and Wife_age <= 22 | 3 | 0.037782 |
|  | 1 | 0.585492 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(-inf-37.5]|(3.5-inf)|(7.5-inf)|1
(37.5-46.5]|(3.5-inf)|(7.5-inf)|3
(46.5-inf)|(3.5-inf)|(7.5-inf)|3
(46.5-inf)|(2.5-3.5]|(7.5-inf)|2
(-inf-37.5]|(2.5-3.5]|(7.5-inf)|3
(37.5-46.5]|(2.5-3.5]|(7.5-inf)|1
(46.5-inf)|(-inf-2.5]|(7.5-inf)|1
(37.5-46.5]|(-inf-2.5]|(7.5-inf)|1
(46.5-inf)|(3.5-inf)|(2.5-7.5]|1
(-inf-37.5]|(-inf-2.5]|(7.5-inf)|1
(-inf-37.5]|(3.5-inf)|(2.5-7.5]|3
(37.5-46.5]|(3.5-inf)|(2.5-7.5]|2
(46.5-inf)|(2.5-3.5]|(2.5-7.5]|1
(37.5-46.5]|(2.5-3.5]|(2.5-7.5]|1
(-inf-37.5]|(2.5-3.5]|(2.5-7.5]|3
(46.5-inf)|(3.5-inf)|(0.5-2.5]|1
(46.5-inf)|(-inf-2.5]|(2.5-7.5]|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|1
(37.5-46.5]|(-inf-2.5]|(2.5-7.5]|1
(-inf-37.5]|(-inf-2.5]|(2.5-7.5]|3
(-inf-37.5]|(3.5-inf)|(0.5-2.5]|3
(46.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(0.5-2.5]|1
(-inf-37.5]|(2.5-3.5]|(0.5-2.5]|1
(46.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|1
(-inf-37.5]|(3.5-inf)|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(0.5-2.5]|1
(-inf-37.5]|(-inf-2.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-37.5]|(2.5-3.5]|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(-inf-0.5]|1
(-inf-37.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (185.0/81.0)
(Wife_age <= 35) and (Children >= 3)|3 (343.0/154.0)
(Children >= 1) and (Wife_age <= 22)|3 (107.0/50.0)
|1 (689.0/277.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.5|1 (80.0/2.0)
Wife_age > 37.5 AND Wife_education <= 3.5 AND Media_exposure > 0.5|1 (37.0/2.0)
Wife_education <= 3.5 AND Wife_age > 35.5 AND Children > 1.5 AND Wife_age <= 46.5 AND Wife_religion > 0.5|1 (120.0/50.0)
Wife_age <= 35.5 AND Children > 2.5 AND Children <= 6.5 AND Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Children <= 4.5 AND Wife_religion > 0.5 AND Standard-of-living <= 2.5 AND Wife_education > 2.5|3 (19.0/4.0)
Wife_age <= 35.5 AND Children > 2.5 AND Standard-of-living > 1.5 AND Children <= 6.5 AND Wife_education <= 2.5 AND Children <= 4.5 AND Standard-of-living <= 3.5|3 (39.0/10.0)
Wife_age > 44.5 AND Children > 2.5 AND Standard-of-living > 2.5 AND Wife_age <= 48.5 AND Wife_education > 3.5|2 (25.0/10.0)
Wife_age > 44.5|1 (58.0/13.0)
Children > 2.5 AND Wife_age > 35.5 AND Husband_education > 3.5 AND Wife_age <= 42.5 AND Wife_age > 37.5|2 (51.0/16.0)
Children > 2.5 AND Standard-of-living > 1.5 AND Wife_education <= 2.5 AND Children <= 6.5 AND Children > 4.5|3 (24.0/5.0)
Wife_education <= 2.5 AND Husband_occupation > 1.5 AND Children <= 4.5 AND Wife_working <= 0.5|1 (23.0/7.0)
Wife_education <= 2.5 AND Wife_age <= 33.5 AND Husband_occupation > 1.5 AND Children <= 4.5 AND Wife_education > 1.5 AND Standard-of-living <= 1.5|1 (21.0/7.0)
Children > 2.5 AND Wife_education > 2.5 AND Wife_age <= 31.5 AND Husband_occupation > 2.5|3 (38.0/7.0)
Children <= 2.5 AND Wife_age <= 22.5 AND Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Husband_education <= 3.5|3 (31.0/10.0)
Children <= 2.5 AND Standard-of-living <= 2.5|1 (60.0/30.0)
Children <= 1.5 AND Wife_age > 31.5|1 (27.0/4.0)
Wife_education <= 2.5|1 (69.0/36.0)
Children > 2.5 AND Wife_age > 30.5 AND Standard-of-living > 3.5 AND Wife_age > 32.5 AND Wife_age <= 42.5 AND Children <= 5.5 AND Wife_religion <= 0.5|2 (23.0/10.0)
Wife_age <= 43.5 AND Wife_age <= 22.5 AND Children <= 1.5 AND Wife_age <= 21.5|1 (18.0/11.0)
Wife_age > 22.5 AND Wife_age <= 43.5 AND Wife_age > 23.5 AND Children > 1.5 AND Wife_age <= 38.5 AND Wife_age <= 25.5|3 (23.0/10.0)
Wife_age <= 22.5|3 (18.0/6.0)
Children > 2.5 AND Wife_age > 30.5 AND Standard-of-living > 3.5 AND Wife_age <= 32.5|3 (17.0/5.0)
Children > 5.5|3 (27.0/14.0)
Wife_age <= 43.5 AND Wife_age > 37.5|1 (24.0/14.0)
Wife_age <= 35.5 AND Children <= 1.5 AND Wife_working > 0.5|3 (37.0/23.0)
Children > 1.5 AND Wife_age <= 35.5 AND Wife_age > 24.5 AND Standard-of-living > 2.5 AND Wife_working > 0.5 AND Wife_age <= 34.5 AND Husband_occupation > 1.5|3 (48.0/27.0)
Children > 1.5 AND Wife_age > 35.5|2 (35.0/15.0)
Children > 1.5 AND Wife_age > 24.5 AND Wife_religion > 0.5 AND Husband_occupation <= 2.5 AND Wife_working <= 0.5|1 (27.0/15.0)
Children > 1.5 AND Wife_age > 24.5 AND Wife_religion <= 0.5|1 (21.0/12.0)
Wife_age > 31.5 AND Husband_occupation <= 1.5 AND Wife_age > 33.5|3 (12.0/5.0)
Wife_age <= 31.5 AND Children <= 1.5|1 (19.0/9.0)
Wife_age > 31.5|2 (17.0/5.0)
Wife_age > 27.5 AND Standard-of-living > 3.5|1 (14.0/8.0)
|2 (33.0/20.0)


## J48 Decision Tree

* Children <= 0.0: 1 (91.0/2.0)
* Children > 0.0
	* Wife_age <= 37.0
		* Wife_education <= 2.0
			* Husband_education <= 1.0: 1 (14.0/7.0)
			* Husband_education > 1.0
				* Children <= 2.0: 1 (102.0/43.0)
				* Children > 2.0: 3 (154.0/63.0)
		* Wife_education > 2.0
			* Children <= 2.0
				* Wife_age <= 30.0
					* Husband_occupation <= 1.0
						* Wife_age <= 20.0: 3 (6.0/2.0)
						* Wife_age > 20.0
							* Wife_age <= 23.0: 2 (12.0/5.0)
							* Wife_age > 23.0
								* Wife_working <= 0.0: 2 (17.0/7.0)
								* Wife_working > 0.0
									* Wife_age <= 25.0: 3 (13.0/5.0)
									* Wife_age > 25.0: 1 (30.0/18.0)
					* Husband_occupation > 1.0: 3 (173.0/89.0)
				* Wife_age > 30.0: 1 (65.0/30.0)
			* Children > 2.0
				* Wife_age <= 31.0: 3 (128.0/53.0)
				* Wife_age > 31.0
					* Standard-of-living <= 3.0
						* Wife_working <= 0.0: 1 (15.0/7.0)
						* Wife_working > 0.0
							* Children <= 3.0: 2 (9.0/2.0)
							* Children > 3.0: 3 (30.0/17.0)
					* Standard-of-living > 3.0
						* Wife_age <= 32.0: 3 (14.0/4.0)
						* Wife_age > 32.0
							* Wife_education <= 3.0: 3 (22.0/10.0)
							* Wife_education > 3.0: 2 (65.0/30.0)
	* Wife_age > 37.0
		* Wife_education <= 3.0: 1 (218.0/66.0)
		* Wife_education > 3.0
			* Children <= 2.0: 1 (28.0/8.0)
			* Children > 2.0
				* Children <= 8.0: 2 (112.0/43.0)
				* Children > 8.0: 3 (6.0/2.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(89.0/2.0)
* Children >= 0.5
	* Wife_age < 37.5: 3(392.0/477.0)
	* Wife_age >= 37.5
		* Wife_education < 3.5: 1(152.0/66.0)
		* Wife_education >= 3.5
			* Children < 2.5: 1(20.0/8.0)
			* Children >= 2.5: 2(70.0/48.0)


