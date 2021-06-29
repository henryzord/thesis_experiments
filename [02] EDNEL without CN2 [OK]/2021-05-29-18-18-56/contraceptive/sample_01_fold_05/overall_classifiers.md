# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Wife_age <= 31.5 and Wife_education > 1.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.057840 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.065547 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 3 | 0.031636 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 1.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.018812 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.012139 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 and Husband_occupation < 1.5 and Wife_age < 32.5 | 2 | 0.010857 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 1.5 and Wife_education <= 3.5 and Children > 5.5 and Wife_working = all | 3 | 0.011843 |
| Wife_age <= 31.5 and Wife_education <= 1.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.008181 |
| Children > 0.5 and Wife_education > 3.5 and Husband_education > 3.5 and Children > 2.5 and Wife_age <= 42.5 and Wife_age <= 35.5 and Wife_age > 26.5 and Children <= 3.5 | 3 | 0.008592 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 and Husband_occupation >= 1.5 and Wife_age >= 33.5 and Wife_education < 1.5 | 3 | 0.007348 |
| Children > 0.5 and Wife_education > 3.5 and Husband_education <= 3.5 | 3 | 0.009032 |
| Wife_age <= 31.5 and Wife_education <= 1.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 3 | 0.003549 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 and Husband_occupation < 1.5 and Children < 3.5 | 2 | 0.005183 |
| Children > 0.5 and Wife_education > 3.5 and Husband_education > 3.5 and Children <= 2.5 and Wife_age <= 43.5 and Wife_age > 32.5 and Children > 1.5 and Wife_working <= 0.5 | 3 | 0.004624 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 5.5 and Wife_working = all | 3 | 0.003604 |
| Wife_age <= 31.5 and Wife_education > 1.5 and Wife_education <= 3.5 and Children > 5.5 and Wife_working = all | 3 | 0.004710 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 and Husband_occupation < 1.5 and Children >= 3.5 and Standard-of-living < 3.5 | 2 | 0.002927 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 and Husband_occupation < 1.5 and Wife_age >= 32.5 and Wife_religion < 0.5 | 3 | 0.003208 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age > 36.5 and Media_exposure <= 0.5 and Wife_working > 0.5 and Wife_age <= 46.5 and Children <= 9.5 and Children > 1.5 and Husband_occupation <= 1.5 and Standard-of-living <= 3.5 | 2 | 0.002927 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 1.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.005672 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 and Husband_occupation >= 1.5 | 3 | 0.030268 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 1.5 and Children > 5.5 and Wife_working = all | 3 | 0.003456 |
| Children > 0.5 and Wife_education > 3.5 and Husband_education > 3.5 and Children <= 2.5 and Wife_age <= 43.5 and Wife_age <= 32.5 | 3 | 0.029006 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 38 and Husband_occupation <= 1 and Wife_age <= 40 and Wife_working >= 1 | 2 | 0.011572 |
| Wife_education >= 4 and Wife_working <= 0 and Children <= 4 and Wife_age >= 41 and Children >= 4 | 2 | 0.005820 |
| Wife_education >= 4 and Children >= 4 and Wife_religion <= 0 and Wife_age >= 38 and Wife_age <= 41 | 2 | 0.005820 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 and Wife_working <= 0 and Wife_age <= 36 and Wife_religion >= 1 | 2 | 0.004854 |
| Wife_education >= 4 and Children >= 3 and Wife_age <= 42 and Husband_occupation <= 2 and Wife_age >= 37 and Children <= 4 and Wife_religion <= 0 | 2 | 0.004854 |
| Wife_education >= 4 and Children >= 7 and Children <= 8 and Husband_occupation <= 1 and Wife_age >= 42 | 2 | 0.005820 |
| Children >= 3 and Husband_occupation >= 3 and Husband_education >= 4 and Wife_age <= 29 and Wife_age >= 27 and Standard-of-living >= 3 | 3 | 0.016687 |
| Husband_occupation >= 2 and Children >= 3 and Standard-of-living >= 2 and Standard-of-living <= 3 and Children <= 3 and Wife_age <= 22 | 3 | 0.006024 |
| Children >= 2 and Husband_occupation >= 2 and Wife_age >= 25 and Husband_education >= 3 and Wife_age <= 25 and Husband_education <= 3 and Standard-of-living >= 3 | 3 | 0.007220 |
| Children >= 3 and Husband_occupation >= 3 and Husband_education >= 3 and Wife_age >= 24 and Wife_age <= 25 and Children <= 3 | 3 | 0.009604 |
| Children >= 4 and Wife_education <= 3 and Wife_age <= 33 and Media_exposure <= 0 and Standard-of-living <= 3 and Husband_education >= 2 and Husband_education <= 2 and Husband_occupation <= 3 | 3 | 0.017857 |
| Children >= 2 and Husband_occupation >= 2 and Wife_age >= 26 and Standard-of-living >= 2 and Wife_education >= 4 and Wife_age <= 28 and Husband_education >= 4 | 3 | 0.010791 |
|  | 1 | 0.460098 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|wife_working|contraceptive_method
---|---|---|---|---
(31.5-37.5]|(3.5-inf)|(5.5-inf)|all|3
(37.5-46.5]|(3.5-inf)|(5.5-inf)|all|2
(46.5-inf)|(3.5-inf)|(5.5-inf)|all|2
(-inf-31.5]|(1.5-3.5]|(5.5-inf)|all|3
(46.5-inf)|(1.5-3.5]|(5.5-inf)|all|1
(37.5-46.5]|(1.5-3.5]|(5.5-inf)|all|1
(31.5-37.5]|(1.5-3.5]|(5.5-inf)|all|3
(46.5-inf)|(3.5-inf)|(2.5-5.5]|all|1
(31.5-37.5]|(-inf-1.5]|(5.5-inf)|all|3
(46.5-inf)|(-inf-1.5]|(5.5-inf)|all|1
(-inf-31.5]|(3.5-inf)|(2.5-5.5]|all|3
(31.5-37.5]|(3.5-inf)|(2.5-5.5]|all|2
(-inf-31.5]|(-inf-1.5]|(5.5-inf)|all|1
(37.5-46.5]|(3.5-inf)|(2.5-5.5]|all|2
(37.5-46.5]|(-inf-1.5]|(5.5-inf)|all|1
(31.5-37.5]|(1.5-3.5]|(2.5-5.5]|all|3
(37.5-46.5]|(1.5-3.5]|(2.5-5.5]|all|1
(46.5-inf)|(1.5-3.5]|(2.5-5.5]|all|1
(-inf-31.5]|(1.5-3.5]|(2.5-5.5]|all|3
(31.5-37.5]|(-inf-1.5]|(2.5-5.5]|all|3
(46.5-inf)|(3.5-inf)|(0.5-2.5]|all|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|all|1
(37.5-46.5]|(-inf-1.5]|(2.5-5.5]|all|1
(-inf-31.5]|(-inf-1.5]|(2.5-5.5]|all|3
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|all|1
(46.5-inf)|(-inf-1.5]|(2.5-5.5]|all|1
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|all|3
(46.5-inf)|(1.5-3.5]|(0.5-2.5]|all|1
(37.5-46.5]|(1.5-3.5]|(0.5-2.5]|all|1
(-inf-31.5]|(1.5-3.5]|(0.5-2.5]|all|1
(31.5-37.5]|(1.5-3.5]|(0.5-2.5]|all|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-1.5]|(0.5-2.5]|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|1
(37.5-46.5]|(-inf-1.5]|(0.5-2.5]|all|1
(46.5-inf)|(-inf-1.5]|(0.5-2.5]|all|1
(-inf-31.5]|(-inf-1.5]|(0.5-2.5]|all|3
(46.5-inf)|(1.5-3.5]|(-inf-0.5]|all|1
(37.5-46.5]|(1.5-3.5]|(-inf-0.5]|all|1
(31.5-37.5]|(1.5-3.5]|(-inf-0.5]|all|1
(-inf-31.5]|(1.5-3.5]|(-inf-0.5]|all|1
(46.5-inf)|(-inf-1.5]|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-1.5]|(-inf-0.5]|all|1
(37.5-46.5]|(-inf-1.5]|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-1.5]|(-inf-0.5]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 38) and (Husband_occupation <= 1) and (Wife_age <= 40) and (Wife_working >= 1)|2 (12.0/0.0)
(Wife_education >= 4) and (Wife_working <= 0) and (Children <= 4) and (Wife_age >= 41) and (Children >= 4)|2 (6.0/0.0)
(Wife_education >= 4) and (Children >= 4) and (Wife_religion <= 0) and (Wife_age >= 38) and (Wife_age <= 41)|2 (6.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34) and (Wife_working <= 0) and (Wife_age <= 36) and (Wife_religion >= 1)|2 (5.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age <= 42) and (Husband_occupation <= 2) and (Wife_age >= 37) and (Children <= 4) and (Wife_religion <= 0)|2 (5.0/0.0)
(Wife_education >= 4) and (Children >= 7) and (Children <= 8) and (Husband_occupation <= 1) and (Wife_age >= 42)|2 (6.0/0.0)
(Children >= 3) and (Husband_occupation >= 3) and (Husband_education >= 4) and (Wife_age <= 29) and (Wife_age >= 27) and (Standard-of-living >= 3)|3 (14.0/0.0)
(Husband_occupation >= 2) and (Children >= 3) and (Standard-of-living >= 2) and (Standard-of-living <= 3) and (Children <= 3) and (Wife_age <= 22)|3 (5.0/0.0)
(Children >= 2) and (Husband_occupation >= 2) and (Wife_age >= 25) and (Husband_education >= 3) and (Wife_age <= 25) and (Husband_education <= 3) and (Standard-of-living >= 3)|3 (6.0/0.0)
(Children >= 3) and (Husband_occupation >= 3) and (Husband_education >= 3) and (Wife_age >= 24) and (Wife_age <= 25) and (Children <= 3)|3 (8.0/0.0)
(Children >= 4) and (Wife_education <= 3) and (Wife_age <= 33) and (Media_exposure <= 0) and (Standard-of-living <= 3) and (Husband_education >= 2) and (Husband_education <= 2) and (Husband_occupation <= 3)|3 (15.0/0.0)
(Children >= 2) and (Husband_occupation >= 2) and (Wife_age >= 26) and (Standard-of-living >= 2) and (Wife_education >= 4) and (Wife_age <= 28) and (Husband_education >= 4)|3 (9.0/0.0)
|1 (1228.0/663.0)


## J48 Decision Tree

* Children <= 0.5: 1 (65.0)
* Children > 0.5
	* Wife_education <= 3.5
		* Wife_age <= 36.5
			* Husband_occupation <= 1.5
				* Children <= 4.5: 1 (33.0/19.0)
				* Children > 4.5: 3 (12.0/4.0)
			* Husband_occupation > 1.5
				* Children <= 2.5: 1 (173.0/86.0)
				* Children > 2.5
					* Husband_education <= 1.5: 1 (11.0/4.0)
					* Husband_education > 1.5
						* Wife_religion <= 0.5: 1 (14.0/8.0)
						* Wife_religion > 0.5
							* Wife_age <= 33.5
								* Media_exposure <= 0.5
									* Children <= 5.5
										* Husband_education <= 3.5
											* Wife_age <= 32.5
												* Standard-of-living <= 3.5
													* Standard-of-living <= 1.5: 1 (12.0/6.0)
													* Standard-of-living > 1.5: 3 (33.0/5.0)
												* Standard-of-living > 3.5: 3 (21.0/10.0)
											* Wife_age > 32.5: 3 (6.0/3.0)
										* Husband_education > 3.5: 3 (46.0/10.0)
									* Children > 5.5: 3 (18.0/7.0)
								* Media_exposure > 0.5: 1 (9.0/5.0)
							* Wife_age > 33.5: 3 (44.0/26.0)
		* Wife_age > 36.5
			* Media_exposure <= 0.5
				* Wife_working <= 0.5: 1 (36.0/17.0)
				* Wife_working > 0.5
					* Wife_age <= 46.5
						* Children <= 9.5
							* Children <= 1.5: 1 (8.0/1.0)
							* Children > 1.5
								* Husband_occupation <= 1.5
									* Standard-of-living <= 3.5: 2 (11.0/6.0)
									* Standard-of-living > 3.5: 1 (8.0/3.0)
								* Husband_occupation > 1.5: 1 (59.0/27.0)
						* Children > 9.5: 1 (7.0)
					* Wife_age > 46.5: 1 (32.0/4.0)
			* Media_exposure > 0.5: 1 (37.0/3.0)
	* Wife_education > 3.5
		* Husband_education <= 3.5: 3 (20.0/8.0)
		* Husband_education > 3.5
			* Children <= 2.5
				* Wife_age <= 43.5
					* Wife_age <= 32.5: 3 (132.0/81.0)
					* Wife_age > 32.5
						* Children <= 1.5: 1 (8.0/3.0)
						* Children > 1.5
							* Wife_working <= 0.5: 3 (14.0/7.0)
							* Wife_working > 0.5: 1 (20.0/9.0)
				* Wife_age > 43.5: 1 (12.0/1.0)
			* Children > 2.5
				* Wife_age <= 42.5
					* Wife_age <= 35.5
						* Wife_age <= 26.5: 1 (6.0/3.0)
						* Wife_age > 26.5
							* Children <= 3.5: 3 (38.0/24.0)
							* Children > 3.5: 2 (32.0/16.0)
					* Wife_age > 35.5: 2 (75.0/26.0)
				* Wife_age > 42.5
					* Wife_working <= 0.5: 2 (7.0/2.0)
					* Wife_working > 0.5
						* Standard-of-living <= 3.5: 1 (9.0/4.0)
						* Standard-of-living > 3.5
							* Husband_occupation <= 1.5: 2 (27.0/13.0)
							* Husband_occupation > 1.5: 1 (10.0/5.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(81.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5
				* Wife_age < 30.5: 1(92.0/109.0)
				* Wife_age >= 30.5
					* Wife_age < 34.5: 1(16.0/7.0)
					* Wife_age >= 34.5: 1(10.0/0.0)
			* Children >= 2.5
				* Husband_occupation < 1.5
					* Children < 3.5: 2(8.0/4.0)
					* Children >= 3.5
						* Standard-of-living < 3.5: 2(6.0/6.0)
						* Standard-of-living >= 3.5: 3(10.0/6.0)
				* Husband_occupation >= 1.5
					* Wife_age < 33.5
						* Husband_education < 1.5: 1(6.0/4.0)
						* Husband_education >= 1.5
							* Wife_age < 24.5: 3(13.0/11.0)
							* Wife_age >= 24.5
								* Wife_religion < 0.5: 1(4.0/5.0)
								* Wife_religion >= 0.5
									* Standard-of-living < 2.5: 3(31.0/19.0)
									* Standard-of-living >= 2.5
										* Children < 5.5
											* Children < 3.5
												* Husband_education < 3.5: 3(11.0/7.0)
												* Husband_education >= 3.5
													* Wife_age < 26.5: 3(7.0/4.0)
													* Wife_age >= 26.5: 3(9.0/1.0)
											* Children >= 3.5: 3(36.0/6.0)
										* Children >= 5.5: 3(9.0/7.0)
					* Wife_age >= 33.5
						* Wife_education < 1.5: 3(8.0/2.0)
						* Wife_education >= 1.5: 1(27.0/36.0)
		* Wife_age >= 37.5
			* Wife_education < 1.5
				* Children < 8.5
					* Wife_age < 41.5: 1(11.0/3.0)
					* Wife_age >= 41.5
						* Husband_occupation < 1.5: 1(8.0/2.0)
						* Husband_occupation >= 1.5: 1(35.0/1.0)
				* Children >= 8.5: 1(8.0/4.0)
			* Wife_education >= 1.5
				* Wife_age < 46.5
					* Children < 1.5: 1(12.0/1.0)
					* Children >= 1.5: 1(53.0/46.0)
				* Wife_age >= 46.5: 1(25.0/5.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5
				* Husband_occupation < 1.5
					* Wife_age < 32.5: 2(29.0/48.0)
					* Wife_age >= 32.5
						* Wife_religion < 0.5: 3(5.0/4.0)
						* Wife_religion >= 0.5: 1(11.0/7.0)
				* Husband_occupation >= 1.5: 3(51.0/48.0)
			* Wife_age >= 39.5: 1(17.0/4.0)
		* Children >= 2.5: 2(134.0/133.0)


