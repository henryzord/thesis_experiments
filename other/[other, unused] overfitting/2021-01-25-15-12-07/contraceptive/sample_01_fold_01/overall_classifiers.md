# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education < 3.5 | 1 | 0.127587 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education < 3.5 and Children >= 2.5 | 3 | 0.104287 |
| Children < 0.5 | 1 | 0.094330 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education < 3.5 and Children < 2.5 | 1 | 0.081096 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education >= 3.5 | 3 | 0.072665 |
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education >= 3.5 and Children >= 1.5 | 2 | 0.038376 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 | 2 | 0.021120 |
| Wife_age > 37.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.019698 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 | 2 | 0.007931 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 1 | 0.010241 |
| Wife_age > 37.5 and Wife_education > 3.5 and Children > 7.5 | 3 | 0.003215 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 2.5 and Children > 7.5 | 1 | 0.002114 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Children > 7.5 | 1 | 0.001316 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0.0 and Wife_education <= 2.0 and Husband_education > 1.0 and Wife_age <= 37.0 and Wife_working > 0.0 and Children > 1.0 and Wife_age > 23.0 and Standard-of-living > 1.0 | 3 | 0.051747 |
| Children > 0.0 and Wife_education <= 2.0 | 1 | 0.186490 |
| Children <= 0.0 | 1 | 0.103602 |
| Wife_age > 37.0 and Children > 1.0 and Wife_education > 3.0 and Husband_occupation <= 2.0 and Wife_working > 0.0 and Wife_age > 40.0 and Children <= 6.0 and Wife_religion > 0.0 | 1 | 0.008547 |
| Wife_age > 37.0 and Children > 1.0 and Wife_education > 3.0 | 2 | 0.067866 |
| Wife_age > 37.0 | 1 | 0.059305 |
| Wife_age <= 22.0 | 3 | 0.108621 |
| Standard-of-living > 1.0 and Children > 2.0 and Husband_occupation > 2.0 and Wife_age > 28.0 and Wife_education <= 3.0 | 3 | 0.062235 |
| Standard-of-living > 1.0 and Wife_education > 3.0 and Children > 1.0 and Wife_age > 26.0 and Standard-of-living > 3.0 and Wife_working > 0.0 and Husband_occupation <= 1.0 and Wife_religion > 0.0 | 2 | 0.015008 |
| Media_exposure <= 0.0 and Wife_age <= 35.0 and Husband_occupation > 2.0 and Wife_working > 0.0 | 3 | 0.069472 |
| Standard-of-living > 1.0 and Standard-of-living > 3.0 and Husband_occupation <= 2.0 and Wife_working <= 0.0 | 3 | 0.063472 |
| Standard-of-living > 1.0 and Wife_working <= 0.0 and Standard-of-living <= 3.0 and Wife_education <= 3.0 | 1 | 0.013315 |
| Standard-of-living > 1.0 and Wife_working <= 0.0 and Standard-of-living <= 3.0 and Children > 1.0 | 2 | 0.027563 |
| Standard-of-living > 1.0 and Wife_working > 0.0 and Children > 2.0 and Wife_age <= 35.0 and Wife_religion > 0.0 | 3 | 0.041812 |
| Standard-of-living > 2.0 | 2 | 0.285627 |
|  | 1 | 0.481250 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_working <= 0 and Wife_age >= 39 and Children <= 4 | 2 | 0.011824 |
| Wife_education >= 4 and Children >= 3 and Wife_age <= 40 and Wife_age >= 38 and Husband_occupation <= 1 | 2 | 0.012763 |
| Wife_education >= 4 and Wife_age >= 34 and Standard-of-living >= 4 and Children >= 7 and Children <= 10 | 2 | 0.009293 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 and Standard-of-living >= 3 and Husband_occupation >= 2 and Wife_age <= 35 | 2 | 0.007461 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 36 and Children <= 4 and Husband_occupation <= 1 and Wife_age <= 45 | 2 | 0.010157 |
| Wife_education >= 3 and Wife_age >= 29 and Wife_religion <= 0 and Children >= 4 | 2 | 0.008789 |
| Children >= 2 and Wife_age >= 27 and Wife_education >= 4 and Standard-of-living <= 3 and Wife_age <= 29 | 2 | 0.007342 |
| Wife_education >= 3 and Children >= 2 and Wife_age >= 32 and Wife_age <= 36 and Husband_occupation >= 3 | 2 | 0.005749 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 30 and Wife_age <= 42 and Husband_occupation >= 2 and Wife_working >= 1 | 2 | 0.006011 |
| Husband_occupation <= 1 and Children >= 2 and Husband_education <= 3 and Wife_age <= 46 | 2 | 0.005415 |
| Wife_age <= 37 and Children >= 3 and Husband_occupation >= 3 and Wife_education >= 3 and Children <= 4 and Standard-of-living >= 3 and Wife_education <= 3 | 3 | 0.024359 |
| Wife_age <= 37 and Children >= 3 and Husband_occupation >= 3 and Standard-of-living <= 3 and Standard-of-living >= 3 and Wife_age >= 24 and Media_exposure <= 0 and Husband_education >= 3 and Children <= 4 | 3 | 0.015091 |
| Wife_age <= 37 and Children >= 3 and Husband_occupation >= 3 and Wife_education <= 1 | 3 | 0.017657 |
| Children >= 2 and Husband_occupation >= 2 and Wife_education >= 4 and Wife_age <= 28 and Wife_age >= 26 | 3 | 0.015708 |
| Children >= 4 and Media_exposure <= 0 and Standard-of-living <= 3 and Husband_education >= 2 and Wife_age >= 24 and Wife_age <= 30 | 3 | 0.024357 |
| Children >= 2 and Wife_education >= 4 and Wife_age <= 25 | 3 | 0.015305 |
| Wife_age <= 37 and Standard-of-living >= 4 and Children >= 4 and Wife_age >= 35 and Husband_occupation <= 1 | 3 | 0.014410 |
| Children >= 1 and Wife_age <= 22 and Husband_occupation >= 2 and Wife_education >= 4 | 3 | 0.012312 |
| Children >= 2 and Husband_occupation >= 2 and Husband_occupation <= 2 and Wife_age <= 29 and Wife_age >= 25 | 3 | 0.021317 |
| Children >= 1 and Wife_age <= 22 and Standard-of-living <= 3 and Husband_education <= 3 and Wife_education >= 3 | 3 | 0.012844 |
| Wife_age <= 37 and Children >= 2 and Wife_education >= 4 and Wife_working <= 0 and Standard-of-living >= 4 | 3 | 0.016604 |
| Wife_age <= 35 and Children >= 2 and Husband_occupation >= 2 and Wife_age >= 28 and Wife_working >= 1 and Standard-of-living >= 4 | 3 | 0.017919 |
| Wife_age <= 35 and Standard-of-living <= 3 and Husband_education <= 3 and Children >= 3 and Husband_education >= 3 and Children <= 4 | 3 | 0.011233 |
| Children >= 1 and Wife_age <= 22 | 3 | 0.017480 |
| Wife_age <= 41 and Children >= 1 and Wife_education >= 4 and Wife_religion <= 0 | 3 | 0.011686 |
| Wife_age <= 37 and Wife_education <= 2 and Husband_education >= 2 and Children <= 7 and Children >= 6 and Standard-of-living <= 3 | 3 | 0.013581 |
|  | 1 | 0.632287 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(31.5-37.5]|(3.5-inf)|(7.5-inf)|1
(37.5-inf)|(3.5-inf)|(7.5-inf)|3
(31.5-37.5]|(2.5-3.5]|(7.5-inf)|3
(37.5-inf)|(2.5-3.5]|(7.5-inf)|1
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|1
(31.5-37.5]|(-inf-2.5]|(7.5-inf)|1
(37.5-inf)|(-inf-2.5]|(7.5-inf)|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|3
(37.5-inf)|(3.5-inf)|(2.5-7.5]|2
(31.5-37.5]|(3.5-inf)|(2.5-7.5]|2
(37.5-inf)|(2.5-3.5]|(2.5-7.5]|1
(31.5-37.5]|(2.5-3.5]|(2.5-7.5]|2
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|3
(31.5-37.5]|(-inf-2.5]|(2.5-7.5]|3
(37.5-inf)|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|3
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|1
(37.5-inf)|(-inf-2.5]|(2.5-7.5]|1
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|3
(31.5-37.5]|(2.5-3.5]|(0.5-2.5]|1
(37.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|1
(31.5-37.5]|(-inf-2.5]|(0.5-2.5]|1
(37.5-inf)|(3.5-inf)|(-inf-0.5]|1
(37.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|1
(37.5-inf)|(2.5-3.5]|(-inf-0.5]|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|1
(37.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_working <= 0) and (Wife_age >= 39) and (Children <= 4)|2 (16.0/2.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age <= 40) and (Wife_age >= 38) and (Husband_occupation <= 1)|2 (17.0/2.0)
(Wife_education >= 4) and (Wife_age >= 34) and (Standard-of-living >= 4) and (Children >= 7) and (Children <= 10)|2 (15.0/3.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34) and (Standard-of-living >= 3) and (Husband_occupation >= 2) and (Wife_age <= 35)|2 (13.0/3.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 36) and (Children <= 4) and (Husband_occupation <= 1) and (Wife_age <= 45)|2 (27.0/9.0)
(Wife_education >= 3) and (Wife_age >= 29) and (Wife_religion <= 0) and (Children >= 4)|2 (34.0/16.0)
(Children >= 2) and (Wife_age >= 27) and (Wife_education >= 4) and (Standard-of-living <= 3) and (Wife_age <= 29)|2 (16.0/5.0)
(Wife_education >= 3) and (Children >= 2) and (Wife_age >= 32) and (Wife_age <= 36) and (Husband_occupation >= 3)|2 (40.0/24.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 30) and (Wife_age <= 42) and (Husband_occupation >= 2) and (Wife_working >= 1)|2 (33.0/17.0)
(Husband_occupation <= 1) and (Children >= 2) and (Husband_education <= 3) and (Wife_age <= 46)|2 (18.0/8.0)
(Wife_age <= 37) and (Children >= 3) and (Husband_occupation >= 3) and (Wife_education >= 3) and (Children <= 4) and (Standard-of-living >= 3) and (Wife_education <= 3)|3 (16.0/0.0)
(Wife_age <= 37) and (Children >= 3) and (Husband_occupation >= 3) and (Standard-of-living <= 3) and (Standard-of-living >= 3) and (Wife_age >= 24) and (Media_exposure <= 0) and (Husband_education >= 3) and (Children <= 4)|3 (11.0/0.0)
(Wife_age <= 37) and (Children >= 3) and (Husband_occupation >= 3) and (Wife_education <= 1)|3 (25.0/7.0)
(Children >= 2) and (Husband_occupation >= 2) and (Wife_education >= 4) and (Wife_age <= 28) and (Wife_age >= 26)|3 (14.0/2.0)
(Children >= 4) and (Media_exposure <= 0) and (Standard-of-living <= 3) and (Husband_education >= 2) and (Wife_age >= 24) and (Wife_age <= 30)|3 (27.0/4.0)
(Children >= 2) and (Wife_education >= 4) and (Wife_age <= 25)|3 (29.0/11.0)
(Wife_age <= 37) and (Standard-of-living >= 4) and (Children >= 4) and (Wife_age >= 35) and (Husband_occupation <= 1)|3 (12.0/2.0)
(Children >= 1) and (Wife_age <= 22) and (Husband_occupation >= 2) and (Wife_education >= 4)|3 (16.0/4.0)
(Children >= 2) and (Husband_occupation >= 2) and (Husband_occupation <= 2) and (Wife_age <= 29) and (Wife_age >= 25)|3 (36.0/11.0)
(Children >= 1) and (Wife_age <= 22) and (Standard-of-living <= 3) and (Husband_education <= 3) and (Wife_education >= 3)|3 (18.0/5.0)
(Wife_age <= 37) and (Children >= 2) and (Wife_education >= 4) and (Wife_working <= 0) and (Standard-of-living >= 4)|3 (29.0/12.0)
(Wife_age <= 35) and (Children >= 2) and (Husband_occupation >= 2) and (Wife_age >= 28) and (Wife_working >= 1) and (Standard-of-living >= 4)|3 (24.0/9.0)
(Wife_age <= 35) and (Standard-of-living <= 3) and (Husband_education <= 3) and (Children >= 3) and (Husband_education >= 3) and (Children <= 4)|3 (19.0/5.0)
(Children >= 1) and (Wife_age <= 22)|3 (78.0/45.0)
(Wife_age <= 41) and (Children >= 1) and (Wife_education >= 4) and (Wife_religion <= 0)|3 (41.0/23.0)
(Wife_age <= 37) and (Wife_education <= 2) and (Husband_education >= 2) and (Children <= 7) and (Children >= 6) and (Standard-of-living <= 3)|3 (17.0/4.0)
|1 (682.0/251.0)


## PART

Decision list:

rules | predicted class
---|---
Children > 0.0 AND Wife_education <= 2.0 AND Husband_education > 1.0 AND Wife_age <= 37.0 AND Wife_working > 0.0 AND Children > 1.0 AND Wife_age > 23.0 AND Standard-of-living > 1.0|3 (84.0/31.0)
Children > 0.0 AND Wife_education <= 2.0|1 (187.0/58.0)
Children <= 0.0|1 (54.0/2.0)
Wife_age > 37.0 AND Children > 1.0 AND Wife_education > 3.0 AND Husband_occupation <= 2.0 AND Wife_working > 0.0 AND Wife_age > 40.0 AND Children <= 6.0 AND Wife_religion > 0.0|1 (25.0/16.0)
Wife_age > 37.0 AND Children > 1.0 AND Wife_education > 3.0|2 (67.0/24.0)
Wife_age > 37.0|1 (75.0/26.0)
Wife_age <= 22.0|3 (47.0/16.0)
Standard-of-living > 1.0 AND Children > 2.0 AND Husband_occupation > 2.0 AND Wife_age > 28.0 AND Wife_education <= 3.0|3 (27.0/7.0)
Standard-of-living > 1.0 AND Wife_education > 3.0 AND Children > 1.0 AND Wife_age > 26.0 AND Standard-of-living > 3.0 AND Wife_working > 0.0 AND Husband_occupation <= 1.0 AND Wife_religion > 0.0|2 (33.0/19.0)
Media_exposure <= 0.0 AND Wife_age <= 35.0 AND Husband_occupation > 2.0 AND Wife_working > 0.0|3 (56.0/27.0)
Standard-of-living > 1.0 AND Standard-of-living > 3.0 AND Husband_occupation <= 2.0 AND Wife_working <= 0.0|3 (40.0/18.0)
Standard-of-living > 1.0 AND Wife_working <= 0.0 AND Standard-of-living <= 3.0 AND Wife_education <= 3.0|1 (15.0/5.0)
Standard-of-living > 1.0 AND Wife_working <= 0.0 AND Standard-of-living <= 3.0 AND Children > 1.0|2 (14.0/8.0)
Standard-of-living > 1.0 AND Wife_working > 0.0 AND Children > 2.0 AND Wife_age <= 35.0 AND Wife_religion > 0.0|3 (41.0/25.0)
Standard-of-living > 2.0|2 (94.0/56.0)
|1 (23.0/12.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(81.0/2.0)
* Children >= 0.5
	* Wife_age < 37.5
		* Wife_education < 3.5
			* Children < 2.5: 1(121.0/115.0)
			* Children >= 2.5: 3(169.0/137.0)
		* Wife_education >= 3.5: 3(140.0/193.0)
	* Wife_age >= 37.5
		* Wife_education < 3.5: 1(151.0/59.0)
		* Wife_education >= 3.5
			* Children < 1.5: 1(16.0/1.0)
			* Children >= 1.5: 2(74.0/64.0)


