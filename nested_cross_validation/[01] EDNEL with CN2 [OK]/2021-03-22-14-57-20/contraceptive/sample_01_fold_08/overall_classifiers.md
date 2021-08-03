# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.099618 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.060192 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 | 3 | 0.043263 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 2.5 and Media_exposure <= 0.5 | 3 | 0.024833 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Media_exposure <= 0.5 | 3 | 0.008782 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living > 2.5 and Husband_occupation <= 2.5 and Standard-of-living <= 3.5 | 2 | 0.014146 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living > 2.5 and Husband_occupation <= 2.5 and Standard-of-living > 3.5 and Wife_age <= 35.5 and Children <= 4.5 | 3 | 0.017514 |
| Children > 0.5 and Wife_education > 2.5 and Children <= 1.5 and Wife_age <= 30.5 and Standard-of-living <= 3.5 and Wife_age <= 23.5 and Husband_occupation <= 1.5 | 2 | 0.003474 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living > 2.5 and Husband_occupation > 2.5 | 3 | 0.026663 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living <= 2.5 and Wife_age <= 36.5 and Wife_age > 34.5 | 2 | 0.001100 |
| Children > 0.5 and Wife_education <= 2.5 and Husband_education > 1.5 and Wife_age > 37.5 and Wife_religion <= 0.5 and Standard-of-living > 3.5 | 3 | 0.003687 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age > 41.5 and Wife_age <= 48.5 and Wife_working <= 0.5 | 2 | 0.008641 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living > 2.5 and Husband_occupation <= 2.5 and Standard-of-living > 3.5 and Wife_age <= 35.5 and Children > 4.5 and Husband_occupation > 1.5 | 2 | 0.002597 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living > 2.5 and Husband_occupation <= 2.5 and Standard-of-living > 3.5 and Wife_age <= 35.5 and Children > 4.5 and Husband_occupation <= 1.5 | 3 | 0.004710 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Media_exposure > 0.5 | 3 | 0.002307 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 2.5 and Media_exposure > 0.5 | 3 | 0.001156 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Media_exposure <= 0.5 | 3 | 0.011402 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Media_exposure <= 0.5 | 3 | 0.022805 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Media_exposure > 0.5 | 2 | 0.000326 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 and Media_exposure <= 0.5 | 3 | 0.004608 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age > 41.5 and Wife_age <= 48.5 and Wife_working > 0.5 and Husband_occupation <= 1.5 | 2 | 0.010362 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Media_exposure <= 0.5 | 3 | 0.010668 |
| Children > 0.5 and Wife_education > 2.5 and Children > 1.5 and Wife_age > 26.5 and Media_exposure <= 0.5 and Wife_age <= 41.5 and Standard-of-living <= 2.5 and Wife_age <= 36.5 and Wife_age <= 34.5 | 3 | 0.011883 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 37 and Wife_age <= 42 and Husband_occupation <= 1 and Wife_religion <= 0 | 2 | 0.007744 |
| Wife_education >= 4 and Children >= 3 and Wife_age <= 42 and Wife_age >= 37 and Husband_occupation <= 1 and Standard-of-living <= 3 | 2 | 0.005820 |
| Wife_education >= 4 and Children >= 3 and Standard-of-living >= 4 and Wife_working <= 0 and Children <= 4 and Husband_occupation >= 2 and Wife_age >= 37 | 2 | 0.005820 |
| Wife_education >= 4 and Standard-of-living >= 4 and Children >= 7 and Children <= 10 and Husband_occupation <= 1 and Wife_age >= 42 | 2 | 0.005820 |
| Wife_education >= 4 and Children <= 4 and Children >= 4 and Husband_occupation >= 2 and Wife_age <= 38 and Wife_age >= 32 and Standard-of-living >= 4 | 2 | 0.006783 |
| Children >= 3 and Wife_age <= 32 and Husband_occupation >= 2 and Husband_education >= 3 and Wife_working >= 1 and Wife_education >= 3 and Husband_education <= 3 and Children <= 3 | 3 | 0.017710 |
| Husband_occupation >= 3 and Wife_age <= 32 and Standard-of-living >= 3 and Wife_age >= 27 and Wife_working >= 1 and Husband_education >= 3 and Children >= 6 | 3 | 0.005974 |
| Children >= 2 and Husband_occupation >= 2 and Standard-of-living >= 2 and Wife_education >= 4 and Wife_age <= 28 and Wife_age >= 25 and Children <= 4 | 3 | 0.020024 |
| Wife_age <= 37 and Children >= 3 and Wife_education <= 2 and Standard-of-living >= 3 and Husband_education >= 3 and Wife_working >= 1 and Husband_occupation >= 3 and Wife_age >= 32 | 3 | 0.013049 |
| Children >= 3 and Husband_occupation >= 2 and Standard-of-living >= 3 and Wife_education <= 3 and Standard-of-living <= 3 and Children <= 5 and Wife_age <= 30 and Wife_age >= 29 | 3 | 0.009524 |
| Husband_occupation >= 2 and Wife_age <= 29 and Standard-of-living >= 2 and Husband_occupation <= 2 and Husband_education >= 3 and Children >= 4 | 3 | 0.010702 |
| Children >= 2 and Wife_age <= 25 and Wife_education <= 1 and Media_exposure <= 0 and Wife_age >= 22 | 3 | 0.009524 |
| Children >= 1 and Wife_age <= 22 and Wife_education >= 3 and Wife_religion <= 0 | 3 | 0.007160 |
|  | 1 | 0.465787 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|media_exposure|contraceptive_method
---|---|---|---|---
(31.5-41.5]|(2.5-3.5]|(7.5-inf)|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(7.5-inf)|(0.5-inf)|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|(0.5-inf)|1
(41.5-inf)|(3.5-inf)|(2.5-7.5]|(0.5-inf)|1
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|(0.5-inf)|1
(31.5-41.5]|(3.5-inf)|(2.5-7.5]|(0.5-inf)|3
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(0.5-inf)|1
(31.5-41.5]|(-inf-2.5]|(7.5-inf)|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|(0.5-inf)|1
(31.5-41.5]|(2.5-3.5]|(2.5-7.5]|(0.5-inf)|1
(31.5-41.5]|(3.5-inf)|(7.5-inf)|(-inf-0.5]|2
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|(0.5-inf)|2
(41.5-inf)|(3.5-inf)|(7.5-inf)|(-inf-0.5]|2
(41.5-inf)|(2.5-3.5]|(7.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(2.5-3.5]|(7.5-inf)|(-inf-0.5]|3
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|(0.5-inf)|3
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(0.5-inf)|1
(31.5-41.5]|(-inf-2.5]|(2.5-7.5]|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|(0.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|(0.5-inf)|3
(31.5-41.5]|(-inf-2.5]|(7.5-inf)|(-inf-0.5]|1
(41.5-inf)|(3.5-inf)|(2.5-7.5]|(-inf-0.5]|2
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|(-inf-0.5]|3
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(3.5-inf)|(2.5-7.5]|(-inf-0.5]|2
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|(0.5-inf)|1
(31.5-41.5]|(-inf-2.5]|(0.5-2.5]|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|(0.5-inf)|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|(-inf-0.5]|3
(31.5-41.5]|(2.5-3.5]|(2.5-7.5]|(-inf-0.5]|3
(41.5-inf)|(3.5-inf)|(0.5-2.5]|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(2.5-7.5]|(-inf-0.5]|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|(-inf-0.5]|3
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|(-inf-0.5]|3
(31.5-41.5]|(3.5-inf)|(0.5-2.5]|(-inf-0.5]|3
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|(0.5-inf)|1
(31.5-41.5]|(-inf-2.5]|(-inf-0.5]|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|(-inf-0.5]|1
(31.5-41.5]|(2.5-3.5]|(0.5-2.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|(-inf-0.5]|3
(41.5-inf)|(3.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|(-inf-0.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|(-inf-0.5]|1
(31.5-41.5]|(3.5-inf)|(-inf-0.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(0.5-2.5]|(-inf-0.5]|1
(31.5-41.5]|(2.5-3.5]|(-inf-0.5]|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(-inf-0.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 37) and (Wife_age <= 42) and (Husband_occupation <= 1) and (Wife_religion <= 0)|2 (8.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age <= 42) and (Wife_age >= 37) and (Husband_occupation <= 1) and (Standard-of-living <= 3)|2 (6.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Standard-of-living >= 4) and (Wife_working <= 0) and (Children <= 4) and (Husband_occupation >= 2) and (Wife_age >= 37)|2 (6.0/0.0)
(Wife_education >= 4) and (Standard-of-living >= 4) and (Children >= 7) and (Children <= 10) and (Husband_occupation <= 1) and (Wife_age >= 42)|2 (6.0/0.0)
(Wife_education >= 4) and (Children <= 4) and (Children >= 4) and (Husband_occupation >= 2) and (Wife_age <= 38) and (Wife_age >= 32) and (Standard-of-living >= 4)|2 (7.0/0.0)
(Children >= 3) and (Wife_age <= 32) and (Husband_occupation >= 2) and (Husband_education >= 3) and (Wife_working >= 1) and (Wife_education >= 3) and (Husband_education <= 3) and (Children <= 3)|3 (15.0/0.0)
(Husband_occupation >= 3) and (Wife_age <= 32) and (Standard-of-living >= 3) and (Wife_age >= 27) and (Wife_working >= 1) and (Husband_education >= 3) and (Children >= 6)|3 (5.0/0.0)
(Children >= 2) and (Husband_occupation >= 2) and (Standard-of-living >= 2) and (Wife_education >= 4) and (Wife_age <= 28) and (Wife_age >= 25) and (Children <= 4)|3 (17.0/0.0)
(Wife_age <= 37) and (Children >= 3) and (Wife_education <= 2) and (Standard-of-living >= 3) and (Husband_education >= 3) and (Wife_working >= 1) and (Husband_occupation >= 3) and (Wife_age >= 32)|3 (11.0/0.0)
(Children >= 3) and (Husband_occupation >= 2) and (Standard-of-living >= 3) and (Wife_education <= 3) and (Standard-of-living <= 3) and (Children <= 5) and (Wife_age <= 30) and (Wife_age >= 29)|3 (8.0/0.0)
(Husband_occupation >= 2) and (Wife_age <= 29) and (Standard-of-living >= 2) and (Husband_occupation <= 2) and (Husband_education >= 3) and (Children >= 4)|3 (9.0/0.0)
(Children >= 2) and (Wife_age <= 25) and (Wife_education <= 1) and (Media_exposure <= 0) and (Wife_age >= 22)|3 (8.0/0.0)
(Children >= 1) and (Wife_age <= 22) and (Wife_education >= 3) and (Wife_religion <= 0)|3 (6.0/0.0)
|1 (1213.0/648.0)


## J48 Decision Tree

* Children <= 0.5: 1 (36.0)
* Children > 0.5
	* Wife_education <= 2.5
		* Husband_education <= 1.5: 1 (16.0/4.0)
		* Husband_education > 1.5
			* Wife_age <= 37.5
				* Children <= 2.5: 1 (53.0/21.0)
				* Children > 2.5: 3 (62.0/25.0)
			* Wife_age > 37.5
				* Wife_religion <= 0.5
					* Standard-of-living <= 3.5: 1 (3.0/1.0)
					* Standard-of-living > 3.5: 3 (3.0/1.0)
				* Wife_religion > 0.5: 1 (51.0/8.0)
	* Wife_education > 2.5
		* Children <= 1.5
			* Wife_age <= 30.5
				* Standard-of-living <= 3.5
					* Wife_age <= 23.5
						* Husband_occupation <= 1.5: 2 (4.0/1.0)
						* Husband_occupation > 1.5: 3 (27.0/11.0)
					* Wife_age > 23.5: 1 (20.0/7.0)
				* Standard-of-living > 3.5: 3 (31.0/19.0)
			* Wife_age > 30.5: 1 (20.0/3.0)
		* Children > 1.5
			* Wife_age <= 26.5: 3 (52.0/25.0)
			* Wife_age > 26.5
				* Media_exposure <= 0.5
					* Wife_age <= 41.5
						* Standard-of-living <= 2.5
							* Wife_age <= 36.5
								* Wife_age <= 34.5: 3 (18.0/8.0)
								* Wife_age > 34.5: 2 (3.0/1.0)
							* Wife_age > 36.5: 1 (8.0/4.0)
						* Standard-of-living > 2.5
							* Husband_occupation <= 2.5
								* Standard-of-living <= 3.5: 2 (31.0/13.0)
								* Standard-of-living > 3.5
									* Wife_age <= 35.5
										* Children <= 4.5: 3 (48.0/26.0)
										* Children > 4.5
											* Husband_occupation <= 1.5: 3 (5.0)
											* Husband_occupation > 1.5: 2 (3.0/1.0)
									* Wife_age > 35.5
										* Children <= 2.5: 1 (4.0/2.0)
										* Children > 2.5
											* Wife_education <= 3.5: 1 (8.0/4.0)
											* Wife_education > 3.5: 2 (35.0/10.0)
							* Husband_occupation > 2.5: 3 (45.0/21.0)
					* Wife_age > 41.5
						* Wife_age <= 48.5
							* Wife_working <= 0.5: 2 (14.0/4.0)
							* Wife_working > 0.5
								* Husband_occupation <= 1.5: 2 (28.0/17.0)
								* Husband_occupation > 1.5: 1 (18.0/7.0)
						* Wife_age > 48.5: 1 (7.0/2.0)
				* Media_exposure > 0.5: 1 (10.0/4.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(84.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/120.0)
			* Children >= 2.5: 3(163.0/136.0)
		* Wife_age >= 37.5: 1(153.0/63.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5: 3(85.0/115.0)
			* Wife_age >= 39.5: 1(17.0/4.0)
		* Children >= 2.5: 2(127.0/137.0)


