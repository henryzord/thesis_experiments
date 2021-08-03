# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.104506 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.065547 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 | 3 | 0.042035 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 5.5 and Wife_working = all | 3 | 0.012139 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 5.5 and Wife_working = all | 3 | 0.003604 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.0 | 1 | 0.094217 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Media_exposure > 0.0 | 1 | 0.044301 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working <= 0.0 and Wife_education <= 2.0 | 1 | 0.017985 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Wife_working > 0.0 | 1 | 0.075546 |
| Wife_education <= 3.0 and Children > 2.0 and Wife_religion > 0.0 and Husband_education > 1.0 and Standard-of-living <= 1.0 and Wife_education <= 2.0 | 1 | 0.006579 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Children > 2.0 and Wife_religion > 0.0 and Husband_occupation > 1.0 and Children <= 5.0 | 3 | 0.122376 |
| Children <= 2.0 and Wife_education <= 2.0 and Wife_working > 0.0 and Children <= 1.0 | 1 | 0.026302 |
| Children <= 2.0 and Wife_age > 34.0 | 1 | 0.035945 |
| Wife_age > 31.0 and Media_exposure <= 0.0 and Wife_education > 2.0 and Children <= 8.0 and Wife_age <= 47.0 and Children > 2.0 and Standard-of-living > 3.0 and Wife_education > 3.0 and Husband_occupation <= 2.0 and Husband_occupation > 1.0 and Children > 3.0 | 2 | 0.022167 |
| Wife_age > 34.0 and Media_exposure <= 0.0 and Wife_age <= 41.0 and Wife_education > 3.0 | 2 | 0.053100 |
| Media_exposure <= 0.0 and Wife_age > 41.0 and Standard-of-living > 3.0 and Husband_occupation <= 1.0 | 2 | 0.031527 |
| Husband_education <= 1.0 | 2 | 0.008375 |
| Standard-of-living <= 1.0 and Wife_age > 23.0 | 1 | 0.018845 |
| Media_exposure > 0.0 | 3 | 0.015855 |
| Wife_religion > 0.0 and Children <= 2.0 and Husband_education > 2.0 and Husband_occupation > 1.0 and Wife_education > 3.0 and Wife_age <= 25.0 and Wife_age <= 22.0 | 3 | 0.020782 |
| Wife_religion > 0.0 and Children <= 2.0 and Husband_education > 2.0 and Husband_occupation > 1.0 and Standard-of-living <= 3.0 | 3 | 0.073219 |
| Wife_education <= 2.0 | 3 | 0.048071 |
| Husband_occupation > 2.0 and Wife_religion > 0.0 and Wife_education > 3.0 and Wife_age <= 32.0 and Children > 2.0 | 3 | 0.018847 |
| Wife_religion <= 0.0 and Wife_age > 25.0 and Children > 1.0 | 2 | 0.024411 |
| Standard-of-living <= 3.0 | 1 | 0.198990 |
| Children <= 5.0 and Husband_education > 3.0 and Wife_working > 0.0 and Wife_religion > 0.0 and Children > 1.0 | 3 | 0.110285 |
| Children <= 1.0 and Husband_education > 3.0 and Wife_working > 0.0 | 2 | 0.053178 |
|  | 3 | 0.345506 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 38 and Husband_occupation <= 1 and Wife_age <= 40 and Wife_working >= 1 | 2 | 0.011572 |
| Wife_education >= 4 and Children >= 3 and Wife_working <= 0 and Children <= 4 and Wife_age >= 41 | 2 | 0.009002 |
| Wife_education >= 4 and Wife_age >= 34 and Wife_age <= 42 and Children >= 4 and Wife_religion <= 0 | 2 | 0.009977 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 and Wife_age <= 42 and Wife_religion >= 1 and Wife_working <= 0 | 2 | 0.005253 |
| Wife_education >= 4 and Children >= 3 and Wife_age <= 42 and Wife_age >= 37 and Husband_occupation <= 1 | 2 | 0.007465 |
| Wife_education >= 4 and Wife_age >= 29 and Standard-of-living >= 4 and Children >= 4 and Husband_occupation >= 2 | 2 | 0.008309 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 44 and Standard-of-living >= 4 and Wife_age <= 45 | 2 | 0.004644 |
| Children >= 3 and Husband_occupation >= 3 and Husband_education >= 4 and Wife_age <= 29 and Wife_age >= 27 and Standard-of-living >= 3 | 3 | 0.017610 |
| Children >= 3 and Husband_occupation >= 3 and Husband_education >= 3 and Wife_age >= 24 and Wife_age <= 25 and Children <= 3 | 3 | 0.011392 |
| Children >= 4 and Wife_age <= 33 and Husband_occupation >= 2 and Media_exposure <= 0 and Husband_education >= 2 and Children <= 4 and Wife_education <= 3 and Wife_age >= 31 and Wife_religion >= 1 | 3 | 0.017610 |
| Wife_age <= 30 and Husband_occupation >= 2 and Wife_age >= 26 and Standard-of-living >= 2 and Husband_education >= 2 and Children >= 3 and Standard-of-living <= 3 and Wife_education <= 2 | 3 | 0.011507 |
| Children >= 2 and Wife_age <= 30 and Wife_education >= 3 and Husband_occupation >= 3 and Wife_age >= 30 | 3 | 0.010954 |
| Wife_age <= 37 and Standard-of-living >= 4 and Children >= 4 | 3 | 0.032984 |
| Children >= 2 and Husband_occupation >= 2 and Husband_occupation <= 2 and Wife_age >= 25 and Wife_age <= 25 | 3 | 0.011782 |
| Children >= 2 and Wife_age <= 22 | 3 | 0.017042 |
| Children >= 1 and Wife_age <= 22 and Husband_occupation >= 2 and Wife_age >= 21 and Wife_education >= 3 and Wife_education <= 3 | 3 | 0.007962 |
| Wife_age <= 37 and Children >= 2 and Standard-of-living >= 4 and Wife_education >= 4 and Husband_occupation >= 2 | 3 | 0.017828 |
| Wife_age <= 35 and Wife_education <= 2 and Children >= 4 and Standard-of-living >= 3 and Children <= 6 | 3 | 0.006619 |
| Wife_age <= 34 and Children >= 3 and Standard-of-living >= 4 and Wife_age >= 28 and Wife_religion >= 1 | 3 | 0.007906 |
| Children >= 1 and Standard-of-living <= 3 and Husband_occupation >= 2 and Wife_age <= 22 | 3 | 0.010620 |
| Children >= 2 and Wife_age <= 30 and Standard-of-living <= 2 and Standard-of-living >= 2 and Wife_age >= 26 and Husband_education >= 4 | 3 | 0.008577 |
|  | 1 | 0.559406 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|wife_working|contraceptive_method
---|---|---|---|---
(31.5-37.5]|(3.5-inf)|(5.5-inf)|all|3
(46.5-inf)|(3.5-inf)|(5.5-inf)|all|2
(37.5-46.5]|(3.5-inf)|(5.5-inf)|all|2
(46.5-inf)|(1.5-3.5]|(5.5-inf)|all|1
(-inf-31.5]|(1.5-3.5]|(5.5-inf)|all|3
(37.5-46.5]|(1.5-3.5]|(5.5-inf)|all|1
(31.5-37.5]|(1.5-3.5]|(5.5-inf)|all|3
(-inf-31.5]|(-inf-1.5]|(5.5-inf)|all|1
(31.5-37.5]|(-inf-1.5]|(5.5-inf)|all|3
(46.5-inf)|(-inf-1.5]|(5.5-inf)|all|1
(46.5-inf)|(3.5-inf)|(2.5-5.5]|all|1
(-inf-31.5]|(3.5-inf)|(2.5-5.5]|all|3
(37.5-46.5]|(-inf-1.5]|(5.5-inf)|all|1
(37.5-46.5]|(3.5-inf)|(2.5-5.5]|all|2
(31.5-37.5]|(3.5-inf)|(2.5-5.5]|all|2
(37.5-46.5]|(1.5-3.5]|(2.5-5.5]|all|1
(46.5-inf)|(1.5-3.5]|(2.5-5.5]|all|1
(31.5-37.5]|(1.5-3.5]|(2.5-5.5]|all|3
(-inf-31.5]|(1.5-3.5]|(2.5-5.5]|all|3
(46.5-inf)|(-inf-1.5]|(2.5-5.5]|all|1
(31.5-37.5]|(-inf-1.5]|(2.5-5.5]|all|3
(46.5-inf)|(3.5-inf)|(0.5-2.5]|all|1
(37.5-46.5]|(-inf-1.5]|(2.5-5.5]|all|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|all|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|all|1
(-inf-31.5]|(-inf-1.5]|(2.5-5.5]|all|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|all|3
(46.5-inf)|(1.5-3.5]|(0.5-2.5]|all|1
(37.5-46.5]|(1.5-3.5]|(0.5-2.5]|all|1
(31.5-37.5]|(1.5-3.5]|(0.5-2.5]|all|1
(-inf-31.5]|(1.5-3.5]|(0.5-2.5]|all|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|all|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-1.5]|(0.5-2.5]|all|1
(46.5-inf)|(-inf-1.5]|(0.5-2.5]|all|1
(37.5-46.5]|(-inf-1.5]|(0.5-2.5]|all|1
(-inf-31.5]|(-inf-1.5]|(0.5-2.5]|all|1
(46.5-inf)|(1.5-3.5]|(-inf-0.5]|all|1
(37.5-46.5]|(1.5-3.5]|(-inf-0.5]|all|1
(31.5-37.5]|(1.5-3.5]|(-inf-0.5]|all|1
(-inf-31.5]|(1.5-3.5]|(-inf-0.5]|all|1
(46.5-inf)|(-inf-1.5]|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-1.5]|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-1.5]|(-inf-0.5]|all|1
(37.5-46.5]|(-inf-1.5]|(-inf-0.5]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 38) and (Husband_occupation <= 1) and (Wife_age <= 40) and (Wife_working >= 1)|2 (12.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_working <= 0) and (Children <= 4) and (Wife_age >= 41)|2 (13.0/2.0)
(Wife_education >= 4) and (Wife_age >= 34) and (Wife_age <= 42) and (Children >= 4) and (Wife_religion <= 0)|2 (19.0/5.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34) and (Wife_age <= 42) and (Wife_religion >= 1) and (Wife_working <= 0)|2 (14.0/5.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age <= 42) and (Wife_age >= 37) and (Husband_occupation <= 1)|2 (18.0/5.0)
(Wife_education >= 4) and (Wife_age >= 29) and (Standard-of-living >= 4) and (Children >= 4) and (Husband_occupation >= 2)|2 (26.0/10.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 44) and (Standard-of-living >= 4) and (Wife_age <= 45)|2 (13.0/4.0)
(Children >= 3) and (Husband_occupation >= 3) and (Husband_education >= 4) and (Wife_age <= 29) and (Wife_age >= 27) and (Standard-of-living >= 3)|3 (14.0/0.0)
(Children >= 3) and (Husband_occupation >= 3) and (Husband_education >= 3) and (Wife_age >= 24) and (Wife_age <= 25) and (Children <= 3)|3 (9.0/0.0)
(Children >= 4) and (Wife_age <= 33) and (Husband_occupation >= 2) and (Media_exposure <= 0) and (Husband_education >= 2) and (Children <= 4) and (Wife_education <= 3) and (Wife_age >= 31) and (Wife_religion >= 1)|3 (14.0/0.0)
(Wife_age <= 30) and (Husband_occupation >= 2) and (Wife_age >= 26) and (Standard-of-living >= 2) and (Husband_education >= 2) and (Children >= 3) and (Standard-of-living <= 3) and (Wife_education <= 2)|3 (11.0/1.0)
(Children >= 2) and (Wife_age <= 30) and (Wife_education >= 3) and (Husband_occupation >= 3) and (Wife_age >= 30)|3 (14.0/3.0)
(Wife_age <= 37) and (Standard-of-living >= 4) and (Children >= 4)|3 (73.0/33.0)
(Children >= 2) and (Husband_occupation >= 2) and (Husband_occupation <= 2) and (Wife_age >= 25) and (Wife_age <= 25)|3 (13.0/2.0)
(Children >= 2) and (Wife_age <= 22)|3 (42.0/18.0)
(Children >= 1) and (Wife_age <= 22) and (Husband_occupation >= 2) and (Wife_age >= 21) and (Wife_education >= 3) and (Wife_education <= 3)|3 (10.0/0.0)
(Wife_age <= 37) and (Children >= 2) and (Standard-of-living >= 4) and (Wife_education >= 4) and (Husband_occupation >= 2)|3 (39.0/15.0)
(Wife_age <= 35) and (Wife_education <= 2) and (Children >= 4) and (Standard-of-living >= 3) and (Children <= 6)|3 (15.0/3.0)
(Wife_age <= 34) and (Children >= 3) and (Standard-of-living >= 4) and (Wife_age >= 28) and (Wife_religion >= 1)|3 (24.0/8.0)
(Children >= 1) and (Standard-of-living <= 3) and (Husband_occupation >= 2) and (Wife_age <= 22)|3 (41.0/20.0)
(Children >= 2) and (Wife_age <= 30) and (Standard-of-living <= 2) and (Standard-of-living >= 2) and (Wife_age >= 26) and (Husband_education >= 4)|3 (12.0/3.0)
|1 (879.0/387.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.0|1 (68.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Media_exposure > 0.0|1 (31.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working <= 0.0 AND Wife_education <= 2.0|1 (22.0/5.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Wife_working > 0.0|1 (112.0/36.0)
Wife_education <= 3.0 AND Children > 2.0 AND Wife_religion > 0.0 AND Husband_education > 1.0 AND Standard-of-living <= 1.0 AND Wife_education <= 2.0|1 (15.0/6.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Children > 2.0 AND Wife_religion > 0.0 AND Husband_occupation > 1.0 AND Children <= 5.0|3 (131.0/39.0)
Children <= 2.0 AND Wife_education <= 2.0 AND Wife_working > 0.0 AND Children <= 1.0|1 (39.0/13.0)
Children <= 2.0 AND Wife_age > 34.0|1 (51.0/17.0)
Wife_age > 31.0 AND Media_exposure <= 0.0 AND Wife_education > 2.0 AND Children <= 8.0 AND Wife_age <= 47.0 AND Children > 2.0 AND Standard-of-living > 3.0 AND Wife_education > 3.0 AND Husband_occupation <= 2.0 AND Husband_occupation > 1.0 AND Children > 3.0|2 (20.0/2.0)
Wife_age > 34.0 AND Media_exposure <= 0.0 AND Wife_age <= 41.0 AND Wife_education > 3.0|2 (72.0/28.0)
Media_exposure <= 0.0 AND Wife_age > 41.0 AND Standard-of-living > 3.0 AND Husband_occupation <= 1.0|2 (45.0/19.0)
Husband_education <= 1.0|2 (18.0/10.0)
Standard-of-living <= 1.0 AND Wife_age > 23.0|1 (17.0/5.0)
Media_exposure > 0.0|3 (24.0/13.0)
Wife_religion > 0.0 AND Children <= 2.0 AND Husband_education > 2.0 AND Husband_occupation > 1.0 AND Wife_education > 3.0 AND Wife_age <= 25.0 AND Wife_age <= 22.0|3 (18.0/6.0)
Wife_religion > 0.0 AND Children <= 2.0 AND Husband_education > 2.0 AND Husband_occupation > 1.0 AND Standard-of-living <= 3.0|3 (88.0/45.0)
Wife_education <= 2.0|3 (54.0/28.0)
Husband_occupation > 2.0 AND Wife_religion > 0.0 AND Wife_education > 3.0 AND Wife_age <= 32.0 AND Children > 2.0|3 (14.0/4.0)
Wife_religion <= 0.0 AND Wife_age > 25.0 AND Children > 1.0|2 (40.0/21.0)
Standard-of-living <= 3.0|1 (92.0/54.0)
Children <= 5.0 AND Husband_education > 3.0 AND Wife_working > 0.0 AND Wife_religion > 0.0 AND Children > 1.0|3 (52.0/31.0)
Children <= 1.0 AND Husband_education > 3.0 AND Wife_working > 0.0|2 (32.0/20.0)
|3 (50.0/25.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(81.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(118.0/116.0)
			* Children >= 2.5: 3(169.0/135.0)
		* Wife_age >= 37.5: 1(152.0/62.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5: 3(84.0/118.0)
			* Wife_age >= 39.5: 1(17.0/4.0)
		* Children >= 2.5: 2(134.0/133.0)


