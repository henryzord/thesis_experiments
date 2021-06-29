# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Wife_age <= 31.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all and Media_exposure <= 0.5 | 3 | 0.113684 |
| Children > 0.5 and Wife_education > 3.5 and Children > 2.5 | 2 | 0.059859 |
| Wife_age > 31.5 and Wife_age <= 39.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all and Media_exposure <= 0.5 | 3 | 0.059798 |
| Children >= 0.5 and Wife_education >= 2.5 and Wife_age < 33.5 and Husband_occupation < 1.5 and Wife_age < 30.5 | 2 | 0.015639 |
| Children >= 0.5 and Wife_education >= 2.5 and Wife_age < 33.5 and Husband_occupation >= 1.5 | 3 | 0.098109 |
| Children >= 0.5 and Wife_education >= 2.5 and Wife_age >= 33.5 and Children >= 1.5 and Wife_education < 3.5 and Wife_age < 36.5 and Standard-of-living < 3.5 | 2 | 0.004929 |
| Wife_age > 39.5 and Wife_age <= 46.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all and Media_exposure <= 0.5 | 2 | 0.027535 |
| Children >= 0.5 and Wife_education < 2.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.059987 |
| Children >= 0.5 and Wife_education < 2.5 and Wife_age < 37.5 and Children < 2.5 and Wife_age < 25.5 and Wife_age >= 20.5 and Husband_education < 3.5 | 3 | 0.010690 |
| Wife_age > 31.5 and Wife_age <= 39.5 and Children > 7.5 and Wife_working = all and Media_exposure <= 0.5 | 3 | 0.004934 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children > 2.5 and Husband_education > 1.5 and Wife_religion > 0.5 and Wife_age > 23.5 and Husband_occupation <= 1.5 and Wife_age <= 34.5 and Children <= 3.5 | 2 | 0.003190 |
| Children > 0.5 and Wife_education > 3.5 and Children <= 2.5 and Wife_age <= 41.5 and Husband_occupation <= 1.5 and Wife_age <= 32.5 | 2 | 0.013150 |
| Children >= 0.5 and Wife_education >= 2.5 and Wife_age >= 33.5 and Children >= 1.5 and Wife_education >= 3.5 and Children < 2.5 | 3 | 0.006906 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children <= 2.5 and Wife_age > 27.5 and Wife_age <= 34.5 and Standard-of-living > 2.5 and Wife_working > 0.5 and Husband_education <= 3.5 | 3 | 0.003205 |
| Children > 0.5 and Wife_education > 3.5 and Children <= 2.5 and Wife_age <= 41.5 and Husband_occupation > 1.5 | 3 | 0.032264 |
| Children > 0.5 and Wife_education <= 3.5 and Wife_age <= 37.5 and Children <= 2.5 and Wife_age <= 27.5 and Standard-of-living <= 3.5 and Wife_age > 20.5 | 3 | 0.023976 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0.0 and Wife_education <= 2.0 and Wife_age > 37.0 | 1 | 0.103753 |
| Children <= 0.0 | 1 | 0.100645 |
| Wife_education <= 3.0 and Wife_age > 39.0 and Wife_working > 0.0 and Husband_education > 3.0 | 1 | 0.013160 |
| Wife_education <= 3.0 and Children <= 2.0 and Media_exposure <= 0.0 and Wife_working > 0.0 and Standard-of-living <= 1.0 and Wife_age <= 25.0 | 3 | 0.011746 |
| Wife_education <= 3.0 and Children <= 2.0 and Standard-of-living > 1.0 and Media_exposure <= 0.0 and Wife_working > 0.0 and Husband_education > 2.0 and Children <= 1.0 and Wife_education <= 2.0 | 1 | 0.019353 |
| Wife_education <= 3.0 and Children <= 2.0 and Standard-of-living > 1.0 and Media_exposure <= 0.0 and Wife_working > 0.0 and Husband_occupation > 1.0 and Husband_occupation <= 2.0 and Wife_education > 2.0 | 1 | 0.014343 |
| Wife_education <= 3.0 and Media_exposure > 0.0 and Standard-of-living <= 2.0 and Children <= 4.0 and Children <= 3.0 and Children <= 2.0 | 1 | 0.008499 |
| Wife_age > 39.0 and Children > 1.0 and Wife_age <= 48.0 and Husband_occupation <= 2.0 and Standard-of-living <= 3.0 | 2 | 0.010952 |
| Wife_education <= 3.0 and Standard-of-living <= 1.0 and Children > 2.0 and Children <= 3.0 and Wife_education <= 2.0 | 1 | 0.008684 |
| Wife_education <= 3.0 and Children > 2.0 and Wife_religion > 0.0 and Husband_occupation > 1.0 and Husband_education > 1.0 and Wife_age <= 33.0 and Media_exposure <= 0.0 and Wife_age <= 24.0 and Wife_education <= 2.0 | 1 | 0.007872 |
| Wife_education <= 3.0 and Children > 2.0 and Wife_religion > 0.0 and Husband_education > 1.0 and Media_exposure <= 0.0 and Wife_age <= 33.0 and Husband_occupation > 1.0 and Standard-of-living > 2.0 and Husband_education <= 3.0 and Wife_age <= 31.0 | 3 | 0.052114 |
| Wife_education <= 3.0 and Children > 2.0 and Wife_religion > 0.0 and Husband_education > 1.0 and Media_exposure <= 0.0 and Wife_age <= 33.0 and Husband_occupation > 1.0 and Standard-of-living <= 2.0 | 3 | 0.046111 |
| Wife_education <= 2.0 and Standard-of-living > 1.0 and Wife_working > 0.0 | 3 | 0.064524 |
| Wife_education <= 2.0 | 1 | 0.076624 |
| Wife_age > 44.0 and Children > 1.0 and Wife_age > 46.0 and Children <= 6.0 | 1 | 0.011702 |
| Children > 2.0 and Media_exposure <= 0.0 and Wife_age > 33.0 and Wife_education > 3.0 and Standard-of-living > 3.0 and Husband_education > 3.0 and Wife_working <= 0.0 and Wife_age > 40.0 | 2 | 0.022266 |
| Children > 2.0 and Media_exposure <= 0.0 and Wife_education > 3.0 and Wife_age > 28.0 and Standard-of-living > 3.0 and Wife_working > 0.0 and Husband_education > 3.0 and Wife_age > 32.0 and Wife_religion > 0.0 and Husband_occupation <= 2.0 and Husband_occupation <= 1.0 and Wife_age > 36.0 | 2 | 0.035891 |
| Children > 2.0 and Media_exposure <= 0.0 and Wife_religion <= 0.0 | 2 | 0.042849 |
| Wife_age > 39.0 and Children > 1.0 and Wife_age <= 44.0 | 1 | 0.016483 |
| Wife_age > 39.0 and Children <= 1.0 | 1 | 0.027670 |
| Children > 2.0 and Children <= 7.0 and Media_exposure <= 0.0 and Husband_education > 3.0 and Husband_occupation > 2.0 and Children <= 4.0 and Wife_education <= 3.0 | 3 | 0.030328 |
| Wife_education > 3.0 and Husband_education > 3.0 and Children > 1.0 and Wife_age > 23.0 and Wife_working <= 0.0 and Standard-of-living > 3.0 | 3 | 0.052595 |
| Wife_working > 0.0 and Husband_occupation > 1.0 and Wife_education > 3.0 and Wife_religion > 0.0 and Husband_education > 3.0 and Husband_occupation <= 2.0 and Standard-of-living <= 3.0 | 3 | 0.016295 |
| Wife_working > 0.0 and Husband_occupation > 1.0 and Wife_age > 20.0 and Children <= 3.0 and Husband_occupation <= 2.0 | 3 | 0.041157 |
| Wife_working > 0.0 and Husband_occupation > 2.0 and Children <= 2.0 and Wife_age > 20.0 and Husband_education > 3.0 and Wife_age <= 29.0 and Children > 1.0 | 3 | 0.021220 |
| Wife_religion <= 0.0 and Wife_age > 26.0 and Wife_working > 0.0 and Wife_age > 34.0 | 3 | 0.035122 |
| Children > 2.0 and Children <= 7.0 and Media_exposure <= 0.0 and Husband_occupation > 2.0 and Wife_age <= 32.0 and Husband_education > 3.0 | 3 | 0.014661 |
| Wife_education <= 3.0 and Media_exposure <= 0.0 and Husband_education > 3.0 and Wife_working <= 0.0 and Standard-of-living <= 3.0 | 1 | 0.018519 |
| Children > 4.0 and Children <= 7.0 and Wife_working > 0.0 and Wife_education > 3.0 | 2 | 0.018071 |
| Wife_religion <= 0.0 and Wife_age > 26.0 | 1 | 0.029989 |
| Wife_working > 0.0 and Husband_occupation > 2.0 and Standard-of-living <= 3.0 and Wife_age > 20.0 and Children <= 1.0 | 3 | 0.040420 |
| Children > 2.0 and Children <= 7.0 and Husband_occupation <= 2.0 and Husband_occupation <= 1.0 and Standard-of-living > 3.0 | 3 | 0.053356 |
| Children > 7.0 | 3 | 0.033449 |
| Children > 2.0 and Wife_working <= 0.0 and Children > 4.0 | 2 | 0.028883 |
| Children > 2.0 and Wife_working <= 0.0 | 1 | 0.009193 |
| Children > 2.0 and Children > 5.0 and Wife_age <= 36.0 | 2 | 0.024366 |
| Children > 2.0 and Children <= 5.0 and Children <= 4.0 and Wife_education > 3.0 | 2 | 0.066569 |
| Husband_occupation <= 1.0 and Wife_education > 3.0 and Wife_working <= 0.0 and Children <= 1.0 | 1 | 0.016532 |
| Wife_working > 0.0 and Standard-of-living > 3.0 and Wife_education <= 3.0 | 2 | 0.078603 |
| Husband_occupation > 1.0 and Wife_education > 3.0 and Children > 1.0 | 3 | 0.052862 |
| Wife_education > 3.0 and Wife_working <= 0.0 | 2 | 0.070244 |
| Wife_education > 3.0 and Wife_age > 25.0 and Standard-of-living <= 3.0 | 1 | 0.054491 |
| Husband_occupation > 1.0 and Standard-of-living <= 3.0 and Husband_occupation > 2.0 and Husband_education <= 3.0 and Children <= 2.0 | 1 | 0.017177 |
| Husband_occupation > 1.0 | 1 | 0.129788 |
| Children <= 2.0 and Wife_education > 3.0 and Standard-of-living > 3.0 and Children <= 1.0 and Wife_age > 24.0 | 1 | 0.014403 |
| Wife_education <= 3.0 and Children > 2.0 | 2 | 0.088479 |
| Wife_education > 3.0 and Children <= 1.0 | 2 | 0.088235 |
| Wife_age > 24.0 and Wife_education > 3.0 | 2 | 0.034946 |
|  | 3 | 0.608392 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.056005 |
| Wife_age <= 35 and Children >= 3 | 3 | 0.137154 |
| Children >= 1 and Wife_age <= 22 and Wife_age >= 21 | 3 | 0.027001 |
|  | 1 | 0.575356 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|children|wife_working|media_exposure|contraceptive_method
---|---|---|---|---
(-inf-31.5]|(7.5-inf)|all|(0.5-inf)|1
(46.5-inf)|(7.5-inf)|all|(0.5-inf)|1
(31.5-39.5]|(7.5-inf)|all|(0.5-inf)|1
(39.5-46.5]|(7.5-inf)|all|(0.5-inf)|1
(46.5-inf)|(1.5-7.5]|all|(0.5-inf)|1
(39.5-46.5]|(1.5-7.5]|all|(0.5-inf)|1
(-inf-31.5]|(1.5-7.5]|all|(0.5-inf)|1
(31.5-39.5]|(1.5-7.5]|all|(0.5-inf)|1
(31.5-39.5]|(0.5-1.5]|all|(0.5-inf)|1
(46.5-inf)|(0.5-1.5]|all|(0.5-inf)|1
(-inf-31.5]|(0.5-1.5]|all|(0.5-inf)|1
(39.5-46.5]|(0.5-1.5]|all|(0.5-inf)|1
(-inf-31.5]|(-inf-0.5]|all|(0.5-inf)|1
(46.5-inf)|(-inf-0.5]|all|(0.5-inf)|1
(31.5-39.5]|(-inf-0.5]|all|(0.5-inf)|1
(31.5-39.5]|(7.5-inf)|all|(-inf-0.5]|3
(39.5-46.5]|(7.5-inf)|all|(-inf-0.5]|1
(46.5-inf)|(7.5-inf)|all|(-inf-0.5]|1
(46.5-inf)|(1.5-7.5]|all|(-inf-0.5]|1
(-inf-31.5]|(1.5-7.5]|all|(-inf-0.5]|3
(39.5-46.5]|(1.5-7.5]|all|(-inf-0.5]|2
(31.5-39.5]|(1.5-7.5]|all|(-inf-0.5]|3
(46.5-inf)|(0.5-1.5]|all|(-inf-0.5]|1
(31.5-39.5]|(0.5-1.5]|all|(-inf-0.5]|1
(39.5-46.5]|(0.5-1.5]|all|(-inf-0.5]|1
(-inf-31.5]|(0.5-1.5]|all|(-inf-0.5]|1
(31.5-39.5]|(-inf-0.5]|all|(-inf-0.5]|1
(39.5-46.5]|(-inf-0.5]|all|(-inf-0.5]|1
(46.5-inf)|(-inf-0.5]|all|(-inf-0.5]|1
(-inf-31.5]|(-inf-0.5]|all|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (196.0/89.0)
(Wife_age <= 35) and (Children >= 3)|3 (346.0/156.0)
(Children >= 1) and (Wife_age <= 22) and (Wife_age >= 21)|3 (66.0/28.0)
|1 (717.0/294.0)


## PART

Decision list:

rules | predicted class
---|---
Children > 0.0 AND Wife_education <= 2.0 AND Wife_age > 37.0|1 (136.0/27.0)
Children <= 0.0|1 (89.0/2.0)
Wife_education <= 3.0 AND Wife_age > 39.0 AND Wife_working > 0.0 AND Husband_education > 3.0|1 (28.0/9.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Media_exposure <= 0.0 AND Wife_working > 0.0 AND Standard-of-living <= 1.0 AND Wife_age <= 25.0|3 (22.0/9.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Standard-of-living > 1.0 AND Media_exposure <= 0.0 AND Wife_working > 0.0 AND Husband_education > 2.0 AND Children <= 1.0 AND Wife_education <= 2.0|1 (21.0/3.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Standard-of-living > 1.0 AND Media_exposure <= 0.0 AND Wife_working > 0.0 AND Husband_occupation > 1.0 AND Husband_occupation <= 2.0 AND Wife_education > 2.0|1 (30.0/12.0)
Wife_education <= 3.0 AND Media_exposure > 0.0 AND Standard-of-living <= 2.0 AND Children <= 4.0 AND Children <= 3.0 AND Children <= 2.0|1 (10.0/2.0)
Wife_age > 39.0 AND Children > 1.0 AND Wife_age <= 48.0 AND Husband_occupation <= 2.0 AND Standard-of-living <= 3.0|2 (24.0/12.0)
Wife_education <= 3.0 AND Standard-of-living <= 1.0 AND Children > 2.0 AND Children <= 3.0 AND Wife_education <= 2.0|1 (10.0/2.0)
Wife_education <= 3.0 AND Children > 2.0 AND Wife_religion > 0.0 AND Husband_occupation > 1.0 AND Husband_education > 1.0 AND Wife_age <= 33.0 AND Media_exposure <= 0.0 AND Wife_age <= 24.0 AND Wife_education <= 2.0|1 (14.0/5.0)
Wife_education <= 3.0 AND Children > 2.0 AND Wife_religion > 0.0 AND Husband_education > 1.0 AND Media_exposure <= 0.0 AND Wife_age <= 33.0 AND Husband_occupation > 1.0 AND Standard-of-living > 2.0 AND Husband_education <= 3.0 AND Wife_age <= 31.0|3 (48.0/11.0)
Wife_education <= 3.0 AND Children > 2.0 AND Wife_religion > 0.0 AND Husband_education > 1.0 AND Media_exposure <= 0.0 AND Wife_age <= 33.0 AND Husband_occupation > 1.0 AND Standard-of-living <= 2.0|3 (45.0/11.0)
Wife_education <= 2.0 AND Standard-of-living > 1.0 AND Wife_working > 0.0|3 (111.0/49.0)
Wife_education <= 2.0|1 (53.0/22.0)
Wife_age > 44.0 AND Children > 1.0 AND Wife_age > 46.0 AND Children <= 6.0|1 (19.0/7.0)
Children > 2.0 AND Media_exposure <= 0.0 AND Wife_age > 33.0 AND Wife_education > 3.0 AND Standard-of-living > 3.0 AND Husband_education > 3.0 AND Wife_working <= 0.0 AND Wife_age > 40.0|2 (13.0/2.0)
Children > 2.0 AND Media_exposure <= 0.0 AND Wife_education > 3.0 AND Wife_age > 28.0 AND Standard-of-living > 3.0 AND Wife_working > 0.0 AND Husband_education > 3.0 AND Wife_age > 32.0 AND Wife_religion > 0.0 AND Husband_occupation <= 2.0 AND Husband_occupation <= 1.0 AND Wife_age > 36.0|2 (43.0/15.0)
Children > 2.0 AND Media_exposure <= 0.0 AND Wife_religion <= 0.0|2 (74.0/38.0)
Wife_age > 39.0 AND Children > 1.0 AND Wife_age <= 44.0|1 (30.0/18.0)
Wife_age > 39.0 AND Children <= 1.0|1 (17.0/1.0)
Children > 2.0 AND Children <= 7.0 AND Media_exposure <= 0.0 AND Husband_education > 3.0 AND Husband_occupation > 2.0 AND Children <= 4.0 AND Wife_education <= 3.0|3 (14.0/2.0)
Wife_education > 3.0 AND Husband_education > 3.0 AND Children > 1.0 AND Wife_age > 23.0 AND Wife_working <= 0.0 AND Standard-of-living > 3.0|3 (37.0/15.0)
Wife_working > 0.0 AND Husband_occupation > 1.0 AND Wife_education > 3.0 AND Wife_religion > 0.0 AND Husband_education > 3.0 AND Husband_occupation <= 2.0 AND Standard-of-living <= 3.0|3 (16.0/6.0)
Wife_working > 0.0 AND Husband_occupation > 1.0 AND Wife_age > 20.0 AND Children <= 3.0 AND Husband_occupation <= 2.0|3 (28.0/12.0)
Wife_working > 0.0 AND Husband_occupation > 2.0 AND Children <= 2.0 AND Wife_age > 20.0 AND Husband_education > 3.0 AND Wife_age <= 29.0 AND Children > 1.0|3 (21.0/8.0)
Wife_religion <= 0.0 AND Wife_age > 26.0 AND Wife_working > 0.0 AND Wife_age > 34.0|3 (10.0/3.0)
Children > 2.0 AND Children <= 7.0 AND Media_exposure <= 0.0 AND Husband_occupation > 2.0 AND Wife_age <= 32.0 AND Husband_education > 3.0|3 (12.0/3.0)
Wife_education <= 3.0 AND Media_exposure <= 0.0 AND Husband_education > 3.0 AND Wife_working <= 0.0 AND Standard-of-living <= 3.0|1 (8.0/1.0)
Children > 4.0 AND Children <= 7.0 AND Wife_working > 0.0 AND Wife_education > 3.0|2 (20.0/9.0)
Wife_religion <= 0.0 AND Wife_age > 26.0|1 (22.0/11.0)
Wife_working > 0.0 AND Husband_occupation > 2.0 AND Standard-of-living <= 3.0 AND Wife_age > 20.0 AND Children <= 1.0|3 (19.0/4.0)
Children > 2.0 AND Children <= 7.0 AND Husband_occupation <= 2.0 AND Husband_occupation <= 1.0 AND Standard-of-living > 3.0|3 (40.0/23.0)
Children > 7.0|3 (9.0/1.0)
Children > 2.0 AND Wife_working <= 0.0 AND Children > 4.0|2 (8.0/2.0)
Children > 2.0 AND Wife_working <= 0.0|1 (7.0/3.0)
Children > 2.0 AND Children > 5.0 AND Wife_age <= 36.0|2 (7.0/2.0)
Children > 2.0 AND Children <= 5.0 AND Children <= 4.0 AND Wife_education > 3.0|2 (20.0/11.0)
Husband_occupation <= 1.0 AND Wife_education > 3.0 AND Wife_working <= 0.0 AND Children <= 1.0|1 (10.0/3.0)
Wife_working > 0.0 AND Standard-of-living > 3.0 AND Wife_education <= 3.0|2 (18.0/9.0)
Husband_occupation > 1.0 AND Wife_education > 3.0 AND Children > 1.0|3 (13.0/4.0)
Wife_education > 3.0 AND Wife_working <= 0.0|2 (19.0/10.0)
Wife_education > 3.0 AND Wife_age > 25.0 AND Standard-of-living <= 3.0|1 (10.0/2.0)
Husband_occupation > 1.0 AND Standard-of-living <= 3.0 AND Husband_occupation > 2.0 AND Husband_education <= 3.0 AND Children <= 2.0|1 (15.0/8.0)
Husband_occupation > 1.0|1 (37.0/20.0)
Children <= 2.0 AND Wife_education > 3.0 AND Standard-of-living > 3.0 AND Children <= 1.0 AND Wife_age > 24.0|1 (15.0/8.0)
Wife_education <= 3.0 AND Children > 2.0|2 (11.0/4.0)
Wife_education > 3.0 AND Children <= 1.0|2 (16.0/7.0)
Wife_age > 24.0 AND Wife_education > 3.0|2 (12.0/6.0)
|3 (14.0/4.0)


## J48 Decision Tree

* Children <= 0.5: 1 (82.0/1.0)
* Children > 0.5
	* Wife_education <= 3.5
		* Wife_age <= 37.5
			* Children <= 2.5
				* Wife_age <= 27.5
					* Standard-of-living <= 3.5
						* Wife_age <= 20.5: 1 (24.0/9.0)
						* Wife_age > 20.5: 3 (86.0/46.0)
					* Standard-of-living > 3.5: 1 (39.0/23.0)
				* Wife_age > 27.5
					* Wife_age <= 34.5
						* Standard-of-living <= 2.5: 1 (13.0/1.0)
						* Standard-of-living > 2.5
							* Wife_working <= 0.5: 1 (10.0/3.0)
							* Wife_working > 0.5
								* Husband_education <= 3.5: 3 (12.0/7.0)
								* Husband_education > 3.5: 1 (15.0/6.0)
					* Wife_age > 34.5: 1 (9.0)
			* Children > 2.5
				* Husband_education <= 1.5: 1 (11.0/5.0)
				* Husband_education > 1.5
					* Wife_religion <= 0.5
						* Husband_occupation <= 2.5: 1 (9.0/5.0)
						* Husband_occupation > 2.5: 3 (9.0/3.0)
					* Wife_religion > 0.5
						* Wife_age <= 23.5: 1 (14.0/7.0)
						* Wife_age > 23.5
							* Husband_occupation <= 1.5
								* Wife_age <= 34.5
									* Children <= 3.5: 2 (11.0/5.0)
									* Children > 3.5: 1 (15.0/9.0)
								* Wife_age > 34.5: 3 (9.0/2.0)
							* Husband_occupation > 1.5
								* Wife_age <= 31.5: 3 (112.0/31.0)
								* Wife_age > 31.5
									* Media_exposure <= 0.5: 3 (73.0/37.0)
									* Media_exposure > 0.5: 1 (10.0/5.0)
		* Wife_age > 37.5: 1 (189.0/57.0)
	* Wife_education > 3.5
		* Children <= 2.5
			* Wife_age <= 41.5
				* Husband_occupation <= 1.5
					* Wife_age <= 32.5: 2 (70.0/41.0)
					* Wife_age > 32.5: 1 (28.0/15.0)
				* Husband_occupation > 1.5: 3 (90.0/42.0)
			* Wife_age > 41.5: 1 (14.0/1.0)
		* Children > 2.5: 2 (239.0/126.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(87.0/2.0)
* Children >= 0.5
	* Wife_education < 2.5
		* Wife_age < 37.5
			* Children < 2.5
				* Wife_age < 25.5
					* Wife_age < 20.5: 1(9.0/4.0)
					* Wife_age >= 20.5
						* Husband_education < 3.5: 3(18.0/17.0)
						* Husband_education >= 3.5: 1(8.0/4.0)
				* Wife_age >= 25.5
					* Standard-of-living < 2.5: 1(14.0/2.0)
					* Standard-of-living >= 2.5
						* Wife_working < 0.5: 1(10.0/2.0)
						* Wife_working >= 0.5: 1(10.0/12.0)
			* Children >= 2.5: 3(95.0/75.0)
		* Wife_age >= 37.5
			* Standard-of-living < 3.5: 1(82.0/12.0)
			* Standard-of-living >= 3.5: 1(27.0/15.0)
	* Wife_education >= 2.5
		* Wife_age < 33.5
			* Husband_occupation < 1.5
				* Wife_age < 30.5: 2(40.0/62.0)
				* Wife_age >= 30.5
					* Children < 2.5: 1(9.0/10.0)
					* Children >= 2.5: 3(15.0/11.0)
			* Husband_occupation >= 1.5: 3(163.0/143.0)
		* Wife_age >= 33.5
			* Children < 1.5
				* Wife_age < 41.5: 1(12.0/4.0)
				* Wife_age >= 41.5: 1(15.0/0.0)
			* Children >= 1.5
				* Wife_education < 3.5
					* Wife_age < 36.5
						* Standard-of-living < 3.5: 2(9.0/7.0)
						* Standard-of-living >= 3.5: 3(8.0/6.0)
					* Wife_age >= 36.5
						* Wife_age < 40.5: 1(13.0/14.0)
						* Wife_age >= 40.5: 1(26.0/24.0)
				* Wife_education >= 3.5
					* Children < 2.5: 3(14.0/19.0)
					* Children >= 2.5: 2(107.0/89.0)


