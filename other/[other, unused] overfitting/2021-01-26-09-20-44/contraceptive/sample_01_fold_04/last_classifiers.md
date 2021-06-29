# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_education < 3.5 and Wife_age >= 37.5 | 1 | 0.124224 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.104851 |
| Children <= 0.5 | 1 | 0.099540 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children <= 2.5 | 1 | 0.082362 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.062382 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation >= 1.5 | 3 | 0.033479 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 | 1 | 0.029840 |
| Children > 0.5 and Wife_education > 3.5 and Children > 2.5 and Wife_age <= 32.5 | 3 | 0.018791 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 | 2 | 0.007890 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 | 1 | 0.006931 |
| Children > 0.5 and Wife_education > 3.5 and Children <= 2.5 and Wife_age <= 43.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age <= 29.5 and Children <= 1.5 and Wife_age <= 24.5 | 2 | 0.006201 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 3 | 0.031674 |
| Children > 0.5 and Wife_education > 3.5 and Children <= 2.5 and Wife_age <= 43.5 and Husband_education > 3.5 and Husband_occupation <= 1.5 and Wife_age <= 29.5 and Children > 1.5 and Wife_age > 25.5 | 2 | 0.006080 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children > 2.5 and Husband_education <= 1.5 | 1 | 0.004953 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 7.5 | 3 | 0.002315 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 2.5 and Children > 7.5 | 1 | 0.002111 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.010318 |
| Wife_age > 46.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 | 2 | 0.000782 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Children > 7.5 | 1 | 0.001314 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.005236 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.009630 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.0 | 1 | 0.099540 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Media_exposure <= 0.0 and Wife_working > 0.0 and Wife_age > 46.0 | 1 | 0.032757 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children > 1.0 and Media_exposure > 0.0 | 1 | 0.037081 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children > 1.0 and Children <= 9.0 and Wife_age <= 45.0 and Wife_age > 41.0 and Husband_education > 2.0 and Wife_education > 1.0 and Children > 3.0 | 2 | 0.007412 |
| Wife_education <= 3.0 and Wife_age > 37.0 | 1 | 0.070897 |
| Wife_education <= 3.0 and Children <= 2.0 and Wife_age <= 30.0 and Husband_occupation <= 3.0 and Wife_age <= 25.0 and Wife_working > 0.0 and Husband_education <= 3.0 and Wife_age <= 24.0 and Wife_education <= 2.0 | 1 | 0.012430 |
| Wife_education <= 3.0 and Children <= 2.0 and Husband_occupation <= 3.0 and Wife_age > 30.0 | 1 | 0.020024 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Children <= 2.0 and Husband_occupation <= 3.0 and Wife_religion > 0.0 and Wife_working <= 0.0 | 1 | 0.014547 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Husband_occupation > 1.0 and Wife_religion > 0.0 and Children > 2.0 and Wife_age <= 31.0 and Wife_age <= 24.0 and Wife_education <= 2.0 | 1 | 0.007036 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Husband_occupation > 1.0 and Standard-of-living <= 2.0 and Children <= 6.0 and Husband_education <= 3.0 and Wife_age > 24.0 and Children > 2.0 and Standard-of-living > 1.0 | 3 | 0.025494 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Standard-of-living <= 2.0 and Wife_age <= 32.0 and Husband_occupation > 1.0 and Wife_education > 1.0 and Husband_occupation <= 2.0 and Wife_age > 22.0 and Standard-of-living <= 1.0 | 3 | 0.012917 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Standard-of-living <= 2.0 and Wife_age <= 31.0 and Media_exposure <= 0.0 and Children <= 3.0 and Wife_age > 23.0 | 1 | 0.026267 |
| Wife_age <= 32.0 and Husband_occupation > 1.0 and Husband_education > 1.0 and Husband_occupation <= 3.0 and Wife_education <= 3.0 and Wife_education > 1.0 and Wife_age <= 23.0 and Wife_age > 20.0 and Children > 1.0 | 1 | 0.006984 |
| Husband_occupation > 1.0 and Wife_age <= 31.0 and Husband_education > 1.0 and Husband_occupation <= 3.0 and Wife_age > 20.0 and Wife_age > 22.0 and Wife_religion > 0.0 and Wife_education <= 3.0 | 3 | 0.128543 |
| Wife_age > 39.0 and Children > 1.0 and Wife_age <= 48.0 and Children > 3.0 | 2 | 0.051884 |
| Wife_age > 43.0 and Children <= 1.0 | 1 | 0.015977 |
| Standard-of-living <= 1.0 and Wife_age > 22.0 | 1 | 0.010271 |
| Wife_age <= 39.0 and Wife_education <= 2.0 and Children > 2.0 and Children <= 3.0 | 3 | 0.015836 |
| Wife_age <= 39.0 and Wife_education <= 2.0 and Husband_education > 1.0 and Wife_education > 1.0 and Husband_education > 2.0 and Standard-of-living <= 3.0 | 3 | 0.019456 |
| Wife_age <= 39.0 and Wife_age > 34.0 and Children > 2.0 and Children <= 7.0 and Wife_age <= 37.0 and Wife_working > 0.0 and Wife_education > 2.0 and Standard-of-living > 3.0 and Wife_education > 3.0 | 2 | 0.017762 |
| Wife_age > 39.0 and Husband_occupation <= 1.0 | 2 | 0.007631 |
| Wife_age > 20.0 and Wife_age > 22.0 and Children > 1.0 and Children <= 7.0 and Wife_age <= 27.0 | 3 | 0.030149 |
| Wife_age > 20.0 and Wife_age <= 22.0 | 3 | 0.063668 |
| Children > 1.0 and Wife_age <= 39.0 and Wife_age > 37.0 | 2 | 0.028205 |
| Wife_age <= 37.0 and Children > 2.0 and Children <= 7.0 and Wife_education > 2.0 and Wife_age <= 36.0 and Husband_occupation <= 2.0 and Wife_age <= 34.0 and Wife_working > 0.0 and Husband_education > 3.0 | 2 | 0.027411 |
| Wife_age <= 37.0 and Children > 2.0 and Standard-of-living > 3.0 | 3 | 0.107971 |
| Wife_age <= 37.0 and Wife_age <= 21.0 | 3 | 0.019709 |
| Wife_age <= 37.0 and Wife_education > 1.0 and Wife_education <= 3.0 and Children <= 5.0 | 2 | 0.070216 |
| Wife_age > 36.0 and Standard-of-living > 3.0 | 1 | 0.058235 |
| Children <= 6.0 and Wife_education > 2.0 and Children <= 2.0 and Standard-of-living > 2.0 and Wife_age > 32.0 | 3 | 0.045370 |
| Husband_education > 3.0 and Wife_age <= 32.0 and Children <= 2.0 and Children <= 1.0 and Wife_age > 24.0 | 1 | 0.050214 |
| Husband_education > 3.0 and Standard-of-living > 2.0 and Wife_age <= 33.0 and Husband_occupation <= 2.0 and Wife_age <= 29.0 | 2 | 0.056524 |
| Husband_education > 3.0 and Standard-of-living > 2.0 and Wife_age <= 33.0 and Husband_occupation > 2.0 | 2 | 0.011710 |
| Wife_age > 29.0 and Wife_age > 30.0 and Wife_education > 2.0 and Standard-of-living > 2.0 | 2 | 0.048844 |
| Wife_age > 29.0 and Wife_age > 31.0 | 3 | 0.240874 |
| Wife_age > 29.0 | 1 | 0.506667 |
|  | 2 | 0.173228 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 37 and Husband_occupation <= 1 | 2 | 0.035336 |
| Children >= 3 and Husband_occupation >= 2 and Wife_age <= 29 | 3 | 0.067610 |
| Wife_age <= 37 and Children >= 6 and Husband_education >= 3 | 3 | 0.021085 |
|  | 1 | 0.490435 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(46.5-inf)|(3.5-inf)|(7.5-inf)|2
(37.5-46.5]|(3.5-inf)|(7.5-inf)|3
(31.5-37.5]|(2.5-3.5]|(7.5-inf)|3
(37.5-46.5]|(2.5-3.5]|(7.5-inf)|1
(46.5-inf)|(2.5-3.5]|(7.5-inf)|2
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|1
(31.5-37.5]|(-inf-2.5]|(7.5-inf)|1
(37.5-46.5]|(-inf-2.5]|(7.5-inf)|1
(31.5-37.5]|(3.5-inf)|(2.5-7.5]|2
(46.5-inf)|(-inf-2.5]|(7.5-inf)|1
(37.5-46.5]|(3.5-inf)|(2.5-7.5]|2
(46.5-inf)|(3.5-inf)|(2.5-7.5]|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|3
(46.5-inf)|(2.5-3.5]|(2.5-7.5]|1
(37.5-46.5]|(2.5-3.5]|(2.5-7.5]|1
(31.5-37.5]|(2.5-3.5]|(2.5-7.5]|2
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|3
(46.5-inf)|(3.5-inf)|(0.5-2.5]|1
(46.5-inf)|(-inf-2.5]|(2.5-7.5]|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|1
(31.5-37.5]|(-inf-2.5]|(2.5-7.5]|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|3
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|3
(37.5-46.5]|(-inf-2.5]|(2.5-7.5]|1
(46.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(31.5-37.5]|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 37) and (Husband_occupation <= 1)|2 (94.0/35.0)
(Children >= 3) and (Husband_occupation >= 2) and (Wife_age <= 29)|3 (129.0/43.0)
(Wife_age <= 37) and (Children >= 6) and (Husband_education >= 3)|3 (47.0/19.0)
|1 (1054.0/548.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.0|1 (79.0/1.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Media_exposure <= 0.0 AND Wife_working > 0.0 AND Wife_age > 46.0|1 (34.0/5.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children > 1.0 AND Media_exposure > 0.0|1 (30.0/3.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children > 1.0 AND Children <= 9.0 AND Wife_age <= 45.0 AND Wife_age > 41.0 AND Husband_education > 2.0 AND Wife_education > 1.0 AND Children > 3.0|2 (24.0/13.0)
Wife_education <= 3.0 AND Wife_age > 37.0|1 (99.0/32.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Wife_age <= 30.0 AND Husband_occupation <= 3.0 AND Wife_age <= 25.0 AND Wife_working > 0.0 AND Husband_education <= 3.0 AND Wife_age <= 24.0 AND Wife_education <= 2.0|1 (28.0/13.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Husband_occupation <= 3.0 AND Wife_age > 30.0|1 (24.0/5.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Children <= 2.0 AND Husband_occupation <= 3.0 AND Wife_religion > 0.0 AND Wife_working <= 0.0|1 (27.0/8.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Husband_occupation > 1.0 AND Wife_religion > 0.0 AND Children > 2.0 AND Wife_age <= 31.0 AND Wife_age <= 24.0 AND Wife_education <= 2.0|1 (16.0/8.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Husband_occupation > 1.0 AND Standard-of-living <= 2.0 AND Children <= 6.0 AND Husband_education <= 3.0 AND Wife_age > 24.0 AND Children > 2.0 AND Standard-of-living > 1.0|3 (25.0/7.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Standard-of-living <= 2.0 AND Wife_age <= 32.0 AND Husband_occupation > 1.0 AND Wife_education > 1.0 AND Husband_occupation <= 2.0 AND Wife_age > 22.0 AND Standard-of-living <= 1.0|3 (12.0/4.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Standard-of-living <= 2.0 AND Wife_age <= 31.0 AND Media_exposure <= 0.0 AND Children <= 3.0 AND Wife_age > 23.0|1 (37.0/12.0)
Wife_age <= 32.0 AND Husband_occupation > 1.0 AND Husband_education > 1.0 AND Husband_occupation <= 3.0 AND Wife_education <= 3.0 AND Wife_education > 1.0 AND Wife_age <= 23.0 AND Wife_age > 20.0 AND Children > 1.0|1 (19.0/9.0)
Husband_occupation > 1.0 AND Wife_age <= 31.0 AND Husband_education > 1.0 AND Husband_occupation <= 3.0 AND Wife_age > 20.0 AND Wife_age > 22.0 AND Wife_religion > 0.0 AND Wife_education <= 3.0|3 (97.0/32.0)
Wife_age > 39.0 AND Children > 1.0 AND Wife_age <= 48.0 AND Children > 3.0|2 (64.0/24.0)
Wife_age > 43.0 AND Children <= 1.0|1 (9.0)
Standard-of-living <= 1.0 AND Wife_age > 22.0|1 (14.0/5.0)
Wife_age <= 39.0 AND Wife_education <= 2.0 AND Children > 2.0 AND Children <= 3.0|3 (13.0/4.0)
Wife_age <= 39.0 AND Wife_education <= 2.0 AND Husband_education > 1.0 AND Wife_education > 1.0 AND Husband_education > 2.0 AND Standard-of-living <= 3.0|3 (20.0/8.0)
Wife_age <= 39.0 AND Wife_age > 34.0 AND Children > 2.0 AND Children <= 7.0 AND Wife_age <= 37.0 AND Wife_working > 0.0 AND Wife_education > 2.0 AND Standard-of-living > 3.0 AND Wife_education > 3.0|2 (33.0/17.0)
Wife_age > 39.0 AND Husband_occupation <= 1.0|2 (23.0/13.0)
Wife_age > 20.0 AND Wife_age > 22.0 AND Children > 1.0 AND Children <= 7.0 AND Wife_age <= 27.0|3 (58.0/30.0)
Wife_age > 20.0 AND Wife_age <= 22.0|3 (33.0/14.0)
Children > 1.0 AND Wife_age <= 39.0 AND Wife_age > 37.0|2 (25.0/11.0)
Wife_age <= 37.0 AND Children > 2.0 AND Children <= 7.0 AND Wife_education > 2.0 AND Wife_age <= 36.0 AND Husband_occupation <= 2.0 AND Wife_age <= 34.0 AND Wife_working > 0.0 AND Husband_education > 3.0|2 (45.0/27.0)
Wife_age <= 37.0 AND Children > 2.0 AND Standard-of-living > 3.0|3 (70.0/30.0)
Wife_age <= 37.0 AND Wife_age <= 21.0|3 (30.0/17.0)
Wife_age <= 37.0 AND Wife_education > 1.0 AND Wife_education <= 3.0 AND Children <= 5.0|2 (29.0/12.0)
Wife_age > 36.0 AND Standard-of-living > 3.0|1 (12.0/1.0)
Children <= 6.0 AND Wife_education > 2.0 AND Children <= 2.0 AND Standard-of-living > 2.0 AND Wife_age > 32.0|3 (23.0/12.0)
Husband_education > 3.0 AND Wife_age <= 32.0 AND Children <= 2.0 AND Children <= 1.0 AND Wife_age > 24.0|1 (40.0/22.0)
Husband_education > 3.0 AND Standard-of-living > 2.0 AND Wife_age <= 33.0 AND Husband_occupation <= 2.0 AND Wife_age <= 29.0|2 (18.0/8.0)
Husband_education > 3.0 AND Standard-of-living > 2.0 AND Wife_age <= 33.0 AND Husband_occupation > 2.0|2 (15.0/8.0)
Wife_age > 29.0 AND Wife_age > 30.0 AND Wife_education > 2.0 AND Standard-of-living > 2.0|2 (19.0/8.0)
Wife_age > 29.0 AND Wife_age > 31.0|3 (18.0/8.0)
Wife_age > 29.0|1 (8.0/3.0)
|2 (7.0/3.0)


## J48 Decision Tree

* Children <= 0.5: 1 (86.0/1.0)
* Children > 0.5
	* Wife_education <= 3.5
		* Wife_age <= 37.5
			* Children <= 2.5: 1 (235.0/113.0)
			* Children > 2.5
				* Husband_education <= 1.5: 1 (13.0/6.0)
				* Husband_education > 1.5: 3 (290.0/124.0)
		* Wife_age > 37.5: 1 (211.0/62.0)
	* Wife_education > 3.5
		* Children <= 2.5
			* Wife_age <= 43.5
				* Husband_education <= 3.5: 3 (8.0/1.0)
				* Husband_education > 3.5
					* Husband_occupation <= 1.5
						* Wife_age <= 29.5
							* Children <= 1.5
								* Wife_age <= 24.5: 2 (19.0/8.0)
								* Wife_age > 24.5: 1 (20.0/9.0)
							* Children > 1.5
								* Wife_age <= 25.5: 3 (8.0/4.0)
								* Wife_age > 25.5: 2 (16.0/6.0)
						* Wife_age > 29.5: 1 (43.0/21.0)
					* Husband_occupation > 1.5: 3 (88.0/42.0)
			* Wife_age > 43.5: 1 (11.0/1.0)
		* Children > 2.5
			* Wife_age <= 32.5: 3 (63.0/31.0)
			* Wife_age > 32.5: 2 (213.0/97.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(85.0/1.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(122.0/113.0)
			* Children >= 2.5: 3(169.0/134.0)
		* Wife_age >= 37.5: 1(149.0/62.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Husband_occupation < 1.5: 1(51.0/66.0)
			* Husband_occupation >= 1.5: 3(53.0/43.0)
		* Children >= 2.5: 2(132.0/144.0)


