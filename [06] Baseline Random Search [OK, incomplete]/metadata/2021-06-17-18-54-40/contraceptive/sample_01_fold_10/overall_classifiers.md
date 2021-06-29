# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.427602 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 37 and Children > 2 | 3 | 0.104938 |
| Children > 0 and Wife_education > 3 and Children > 2 and Wife_age > 28 | 2 | 0.064225 |
| Children > 0 and Wife_education > 3 and Children <= 2 and Wife_age <= 41 | 3 | 0.041827 |
| Wife_age <= 32.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 2 | 0.012044 |
| Wife_age <= 32.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation > 1.5 and Media_exposure <= 0.5 | 3 | 0.009815 |
| Wife_age <= 32.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 3 | 0.006410 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation > 1.5 and Media_exposure <= 0.5 | 2 | 0.005278 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age < 37.5 and Husband_occupation < 1.5 and Children < 3.5 | 2 | 0.005612 |
| Wife_age <= 32.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 2.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 3 | 0.003464 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education < 3.5 and Husband_education < 3.5 and Husband_education >= 2.5 and Wife_age >= 43.5 | 2 | 0.004983 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age >= 37.5 and Media_exposure < 0.5 and Children < 9.5 and Wife_working < 0.5 | 3 | 0.003072 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age < 37.5 and Husband_occupation < 1.5 and Children >= 3.5 and Wife_age >= 30.5 and Standard-of-living < 3.5 | 2 | 0.003037 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education < 3.5 and Husband_education < 3.5 and Husband_education >= 2.5 and Wife_age < 43.5 and Wife_age >= 42.5 | 3 | 0.002076 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age < 37.5 and Husband_occupation >= 1.5 and Wife_age < 33.5 and Wife_age >= 23.5 and Husband_education < 2.5 and Standard-of-living >= 2.5 and Standard-of-living >= 3.5 and Husband_occupation >= 2.5 | 2 | 0.002187 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation > 1.5 and Media_exposure <= 0.5 | 3 | 0.017982 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 2 | 0.001297 |
| Wife_age > 32.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 3 | 0.004929 |
| Wife_age > 41.5 and Wife_education > 3.5 and Children > 7.5 and Husband_occupation > 1.5 and Media_exposure <= 0.5 | 3 | 0.000577 |
| Wife_age > 41.5 and Wife_education <= 2.5 and Children > 7.5 and Husband_occupation <= 1.5 and Media_exposure <= 0.5 | 2 | 0.000487 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age < 33.5 and Wife_age < 28.5 and Husband_occupation >= 2.5 | 3 | 0.009535 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education >= 3.5 | 2 | 0.017443 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children > 2.5 | 3 | 0.104938 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age > 30.5 | 1 | 0.210314 |
| Children <= 0.5 | 1 | 0.124882 |
| Children > 2.5 and Wife_religion > 0.5 and Husband_occupation <= 2.5 and Children <= 6.5 and Wife_age > 37.5 | 2 | 0.039802 |
| Children > 2.5 and Wife_religion > 0.5 | 3 | 0.073652 |
| Children > 2.5 | 2 | 0.193092 |
| Wife_age <= 41 and Wife_education <= 3.5 and Wife_working <= 0.5 | 1 | 0.060024 |
| Wife_age <= 41 and Wife_education <= 3.5 and Wife_education <= 2.5 and Husband_occupation <= 2.5 | 1 | 0.040429 |
| Wife_age <= 41 and Husband_occupation > 2.5 and Wife_education > 3.5 | 3 | 0.056660 |
| Wife_age <= 41 and Wife_education <= 3.5 and Husband_occupation <= 2.5 | 3 | 0.067628 |
| Wife_age <= 41 and Wife_education <= 3.5 and Wife_education <= 2.5 and Standard-of-living <= 2.5 | 3 | 0.023575 |
| Wife_age <= 41 and Husband_education <= 3.5 | 3 | 0.027056 |
| Wife_age <= 41 and Wife_education <= 3.5 and Children > 1.5 | 1 | 0.193333 |
| Wife_age <= 41 and Wife_education > 3.5 and Husband_occupation > 1.5 | 3 | 0.033075 |
| Wife_age <= 41 and Wife_religion > 0.5 and Wife_education > 3.5 and Standard-of-living > 3.5 and Children <= 1.5 | 1 | 0.041827 |
| Wife_age <= 41 and Wife_working <= 0.5 | 2 | 0.070436 |
| Wife_age <= 39.5 and Wife_education > 3.5 and Standard-of-living <= 3.5 | 1 | 0.188125 |
|  | 1 | 0.468468 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.056604 |
| Wife_age <= 37 and Children >= 3 | 3 | 0.159728 |
|  | 1 | 0.574468 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|husband_occupation|media_exposure|contraceptive_method
---|---|---|---|---|---
(41.5-inf)|(2.5-3.5]|(7.5-inf)|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(2.5-3.5]|(7.5-inf)|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(3.5-inf)|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(3.5-inf)|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(3.5-inf)|(7.5-inf)|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(3.5-inf)|(7.5-inf)|(1.5-inf)|(-inf-0.5]|3
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|3
(32.5-41.5]|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(0.5-inf)|1
(41.5-inf)|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(-inf-32.5]|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(32.5-41.5]|(-inf-2.5]|(7.5-inf)|(-inf-1.5]|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(-inf-1.5]|(0.5-inf)|1
(32.5-41.5]|(2.5-3.5]|(7.5-inf)|(1.5-inf)|(-inf-0.5]|3
(32.5-41.5]|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(-inf-32.5]|(2.5-3.5]|(0.5-2.5]|(1.5-inf)|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(7.5-inf)|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(2.5-3.5]|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(-inf-32.5]|(3.5-inf)|(-inf-0.5]|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(1.5-inf)|(-inf-0.5]|1
(32.5-41.5]|(2.5-3.5]|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(-inf-32.5]|(3.5-inf)|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|3
(41.5-inf)|(3.5-inf)|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(3.5-inf)|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|2
(-inf-32.5]|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(-inf-2.5]|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(-inf-1.5]|(0.5-inf)|1
(32.5-41.5]|(3.5-inf)|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|2
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(3.5-inf)|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|2
(32.5-41.5]|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|2
(-inf-32.5]|(2.5-3.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|3
(-inf-32.5]|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|(-inf-1.5]|(0.5-inf)|1
(32.5-41.5]|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|1
(-inf-32.5]|(2.5-3.5]|(0.5-2.5]|(-inf-1.5]|(0.5-inf)|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(0.5-inf)|1
(32.5-41.5]|(2.5-3.5]|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|3
(41.5-inf)|(3.5-inf)|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|2
(32.5-41.5]|(3.5-inf)|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|3
(32.5-41.5]|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|3
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(3.5-inf)|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|3
(-inf-32.5]|(-inf-2.5]|(2.5-7.5]|(1.5-inf)|(-inf-0.5]|3
(32.5-41.5]|(-inf-2.5]|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(32.5-41.5]|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|2
(41.5-inf)|(-inf-2.5]|(7.5-inf)|(-inf-1.5]|(-inf-0.5]|2
(41.5-inf)|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|2
(-inf-32.5]|(3.5-inf)|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|3
(-inf-32.5]|(2.5-3.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(32.5-41.5]|(2.5-3.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(3.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(32.5-41.5]|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(2.5-3.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|2
(32.5-41.5]|(2.5-3.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|3
(32.5-41.5]|(3.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(3.5-inf)|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(0.5-2.5]|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|1
(32.5-41.5]|(-inf-2.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|2
(32.5-41.5]|(2.5-3.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(3.5-inf)|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(2.5-3.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|(-inf-1.5]|(-inf-0.5]|1
(32.5-41.5]|(3.5-inf)|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(3.5-inf)|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|2
(32.5-41.5]|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(32.5-41.5]|(2.5-3.5]|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(2.5-3.5]|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|3
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(-inf-0.5]|(1.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(3.5-inf)|(-inf-0.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(0.5-2.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(2.5-3.5]|(-inf-0.5]|(-inf-1.5]|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|(-inf-1.5]|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|(-inf-1.5]|(-inf-0.5]|1
(-inf-32.5]|(-inf-2.5]|(-inf-0.5]|(-inf-1.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (197.0/89.0)
(Wife_age <= 37) and (Children >= 3)|3 (382.0/177.0)
|1 (747.0/313.0)


## PART

Decision list:

rules | predicted class
---|---
Children > 0.5 AND Wife_education <= 3.5 AND Wife_age <= 37.5 AND Children > 2.5|3 (206.0/91.0)
Children > 0.5 AND Wife_education <= 3.5 AND Wife_age > 30.5|1 (171.0/50.0)
Children <= 0.5|1 (55.0)
Children > 2.5 AND Wife_religion > 0.5 AND Husband_occupation <= 2.5 AND Children <= 6.5 AND Wife_age > 37.5|2 (43.0/15.0)
Children > 2.5 AND Wife_religion > 0.5|3 (94.0/55.0)
Children > 2.5|2 (38.0/11.0)
Wife_age <= 41 AND Wife_education <= 3.5 AND Wife_working <= 0.5|1 (25.0/9.0)
Wife_age <= 41 AND Wife_education <= 3.5 AND Wife_education <= 2.5 AND Husband_occupation <= 2.5|1 (17.0/6.0)
Wife_age <= 41 AND Husband_occupation > 2.5 AND Wife_education > 3.5|3 (35.0/13.0)
Wife_age <= 41 AND Wife_education <= 3.5 AND Husband_occupation <= 2.5|3 (22.0/10.0)
Wife_age <= 41 AND Wife_education <= 3.5 AND Wife_education <= 2.5 AND Standard-of-living <= 2.5|3 (15.0/6.0)
Wife_age <= 41 AND Husband_education <= 3.5|3 (28.0/15.0)
Wife_age <= 41 AND Wife_education <= 3.5 AND Children > 1.5|1 (13.0/7.0)
Wife_age <= 41 AND Wife_education > 3.5 AND Husband_occupation > 1.5|3 (30.0/16.0)
Wife_age <= 41 AND Wife_religion > 0.5 AND Wife_education > 3.5 AND Standard-of-living > 3.5 AND Children <= 1.5|1 (20.0/11.0)
Wife_age <= 41 AND Wife_working <= 0.5|2 (19.0/11.0)
Wife_age <= 39.5 AND Wife_education > 3.5 AND Standard-of-living <= 3.5|1 (17.0/11.0)
|1 (36.0/19.0)


## J48 Decision Tree

* Children <= 0: 1 (88.0/2.0)
* Children > 0
	* Wife_education <= 3
		* Wife_age <= 37
			* Children <= 2: 1 (235.0/115.0)
			* Children > 2: 3 (306.0/136.0)
		* Wife_age > 37: 1 (205.0/56.0)
	* Wife_education > 3
		* Children <= 2
			* Wife_age <= 41: 3 (203.0/119.0)
			* Wife_age > 41: 1 (16.0/1.0)
		* Children > 2
			* Wife_age <= 28
				* Husband_occupation <= 2: 1 (15.0/7.0)
				* Husband_occupation > 2: 3 (12.0/2.0)
			* Wife_age > 28: 2 (246.0/118.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(86.0/2.0)
* Children >= 0.5
	* Wife_age < 41.5
		* Wife_education < 3.5
			* Children < 2.5
				* Wife_age < 30.5: 1(96.0/108.0)
				* Wife_age >= 30.5
					* Children < 1.5: 1(16.0/0.0)
					* Children >= 1.5: 1(19.0/9.0)
			* Children >= 2.5
				* Wife_age < 37.5
					* Husband_occupation < 1.5
						* Children < 3.5: 2(9.0/5.0)
						* Children >= 3.5
							* Wife_age < 30.5
								* Standard-of-living < 3.5: 3(2.0/2.0)
								* Standard-of-living >= 3.5: 1(5.0/0.0)
							* Wife_age >= 30.5
								* Standard-of-living < 3.5: 2(5.0/3.0)
								* Standard-of-living >= 3.5: 3(8.0/1.0)
					* Husband_occupation >= 1.5
						* Wife_age < 33.5
							* Wife_age < 23.5
								* Children < 3.5: 3(9.0/5.0)
								* Children >= 3.5: 1(5.0/0.0)
							* Wife_age >= 23.5
								* Husband_education < 2.5
									* Standard-of-living < 2.5
										* Husband_education < 1.5: 1(3.0/3.0)
										* Husband_education >= 1.5
											* Media_exposure < 0.5: 3(7.0/5.0)
											* Media_exposure >= 0.5: 1(4.0/1.0)
									* Standard-of-living >= 2.5
										* Standard-of-living < 3.5: 3(11.0/3.0)
										* Standard-of-living >= 3.5
											* Husband_occupation < 2.5: 1(2.0/3.0)
											* Husband_occupation >= 2.5: 2(3.0/1.0)
								* Husband_education >= 2.5
									* Wife_religion < 0.5: 1(3.0/4.0)
									* Wife_religion >= 0.5
										* Wife_age < 32.5
											* Wife_working < 0.5: 3(13.0/8.0)
											* Wife_working >= 0.5
												* Wife_age < 26.5: 3(18.0/9.0)
												* Wife_age >= 26.5
													* Wife_age < 29.5
														* Wife_age < 28.5
															* Wife_education < 2.5
																* Wife_age < 27.5: 3(3.0/1.0)
																* Wife_age >= 27.5: 3(6.0/0.0)
															* Wife_education >= 2.5: 3(5.0/3.0)
														* Wife_age >= 28.5: 3(13.0/0.0)
													* Wife_age >= 29.5
														* Wife_education < 2.5: 3(9.0/7.0)
														* Wife_education >= 2.5: 3(11.0/1.0)
										* Wife_age >= 32.5
											* Children < 4.5: 3(7.0/0.0)
											* Children >= 4.5: 3(3.0/2.0)
						* Wife_age >= 33.5
							* Wife_education < 1.5: 3(8.0/4.0)
							* Wife_education >= 1.5: 1(25.0/38.0)
				* Wife_age >= 37.5
					* Media_exposure < 0.5
						* Children < 9.5
							* Wife_working < 0.5: 3(4.0/2.0)
							* Wife_working >= 0.5: 1(16.0/17.0)
						* Children >= 9.5: 1(4.0/0.0)
					* Media_exposure >= 0.5: 1(9.0/0.0)
		* Wife_education >= 3.5
			* Children < 2.5
				* Husband_occupation < 1.5
					* Wife_age < 25.5
						* Wife_age < 20.5: 3(3.0/1.0)
						* Wife_age >= 20.5
							* Wife_age < 23.5: 2(7.0/3.0)
							* Wife_age >= 23.5
								* Wife_working < 0.5: 2(3.0/2.0)
								* Wife_working >= 0.5
									* Standard-of-living < 3.5: 3(4.0/1.0)
									* Standard-of-living >= 3.5: 3(5.0/4.0)
					* Wife_age >= 25.5
						* Children < 1.5
							* Wife_age < 26.5: 1(5.0/0.0)
							* Wife_age >= 26.5
								* Standard-of-living < 3.5: 1(6.0/1.0)
								* Standard-of-living >= 3.5: 1(6.0/8.0)
						* Children >= 1.5
							* Wife_age < 32.5: 2(14.0/12.0)
							* Wife_age >= 32.5
								* Wife_working < 0.5
									* Wife_age < 35.5: 1(2.0/4.0)
									* Wife_age >= 35.5: 3(3.0/1.0)
								* Wife_working >= 0.5: 1(7.0/5.0)
				* Husband_occupation >= 1.5
					* Husband_education < 3.5: 3(8.0/0.0)
					* Husband_education >= 3.5
						* Wife_age < 22.5: 3(13.0/6.0)
						* Wife_age >= 22.5
							* Wife_age < 25.5
								* Children < 1.5: 1(8.0/6.0)
								* Children >= 1.5: 3(7.0/6.0)
							* Wife_age >= 25.5
								* Wife_age < 30.5: 3(14.0/8.0)
								* Wife_age >= 30.5
									* Standard-of-living < 3.5: 1(5.0/3.0)
									* Standard-of-living >= 3.5: 3(6.0/6.0)
			* Children >= 2.5
				* Wife_age < 33.5
					* Wife_age < 28.5
						* Husband_occupation < 2.5: 1(8.0/7.0)
						* Husband_occupation >= 2.5: 3(10.0/2.0)
					* Wife_age >= 28.5
						* Standard-of-living < 2.5: 2(4.0/0.0)
						* Standard-of-living >= 2.5
							* Husband_occupation < 1.5
								* Wife_age < 32.5
									* Wife_working < 0.5: 3(7.0/1.0)
									* Wife_working >= 0.5: 3(4.0/3.0)
								* Wife_age >= 32.5: 1(2.0/3.0)
							* Husband_occupation >= 1.5
								* Children < 4.5
									* Wife_age < 30.5: 3(3.0/4.0)
									* Wife_age >= 30.5: 2(9.0/5.0)
								* Children >= 4.5: 1(2.0/2.0)
				* Wife_age >= 33.5
					* Wife_age < 38.5: 2(44.0/38.0)
					* Wife_age >= 38.5
						* Husband_occupation < 2.5
							* Wife_religion < 0.5: 2(10.0/0.0)
							* Wife_religion >= 0.5
								* Standard-of-living < 3.5: 2(4.0/0.0)
								* Standard-of-living >= 3.5: 2(13.0/5.0)
						* Husband_occupation >= 2.5: 1(2.0/2.0)
	* Wife_age >= 41.5
		* Wife_education < 2.5: 1(77.0/14.0)
		* Wife_education >= 2.5
			* Children < 1.5: 1(16.0/0.0)
			* Children >= 1.5
				* Wife_education < 3.5
					* Husband_education < 3.5
						* Husband_education < 2.5: 1(4.0/0.0)
						* Husband_education >= 2.5
							* Wife_age < 43.5
								* Wife_age < 42.5: 1(3.0/2.0)
								* Wife_age >= 42.5: 3(3.0/2.0)
							* Wife_age >= 43.5: 2(6.0/1.0)
					* Husband_education >= 3.5
						* Wife_working < 0.5: 1(2.0/3.0)
						* Wife_working >= 0.5: 1(17.0/4.0)
				* Wife_education >= 3.5: 2(38.0/43.0)


