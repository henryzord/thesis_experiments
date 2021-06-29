# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.105930 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.061668 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 43.5 | 3 | 0.045186 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_religion = all and Wife_working = all | 3 | 0.010123 |
| Wife_age > 41.5 and Wife_education > 3.5 and Children > 7.5 and Wife_religion = all and Wife_working = all | 3 | 0.002312 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Wife_religion = all and Wife_working = all | 3 | 0.023282 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 and Wife_religion = all and Wife_working = all | 3 | 0.004152 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0 and Wife_education <= 3 and Wife_age > 37 | 1 | 0.128361 |
| Children <= 0 | 1 | 0.096370 |
| Wife_education <= 3 and Children <= 2 and Wife_age > 30 | 1 | 0.019084 |
| Wife_education <= 3 and Husband_education > 1 and Children <= 2 and Wife_age <= 25 and Husband_occupation <= 2 and Wife_age > 19 and Standard-of-living <= 3 and Husband_education <= 3 and Wife_age <= 22 | 1 | 0.003289 |
| Wife_education <= 3 and Husband_education > 1 and Children <= 2 and Wife_age <= 25 and Husband_occupation <= 2 and Wife_age <= 20 | 3 | 0.011729 |
| Wife_education <= 3 and Husband_education > 1 and Children <= 2 and Standard-of-living > 1 and Husband_education > 2 | 1 | 0.037654 |
| Standard-of-living <= 1 and Wife_age <= 32 and Wife_education <= 2 | 1 | 0.024433 |
| Wife_education <= 3 and Husband_education > 1 and Husband_occupation > 1 and Wife_age <= 32 and Children <= 5 and Children > 1 | 3 | 0.163301 |
| Wife_age > 39 and Children > 1 | 2 | 0.075170 |
| Children > 1 and Wife_age <= 37 and Husband_education > 1 and Wife_education <= 2 and Children <= 7 and Standard-of-living <= 3 | 3 | 0.029959 |
| Children > 1 and Wife_age <= 37 and Husband_education > 2 and Wife_age > 23 and Standard-of-living > 3 and Wife_age > 30 and Wife_age > 31 and Children > 2 and Wife_age > 32 and Wife_education > 3 | 2 | 0.038961 |
| Husband_education > 1 and Wife_age <= 22 | 3 | 0.052428 |
| Standard-of-living > 1 and Children <= 1 and Wife_age <= 31 and Wife_age > 24 | 1 | 0.016217 |
| Standard-of-living > 1 and Wife_age <= 40 and Children <= 7 and Wife_age <= 37 and Children <= 6 and Husband_education > 2 and Children > 1 and Wife_religion > 0 and Husband_occupation > 1 and Wife_age <= 33 | 3 | 0.046009 |
| Wife_age <= 41 and Children <= 7 and Standard-of-living > 1 and Wife_education > 1 and Husband_education > 2 and Wife_age <= 37 and Standard-of-living > 3 and Wife_age > 26 and Wife_age <= 36 | 3 | 0.077671 |
| Wife_age <= 41 and Children <= 7 and Children <= 6 and Standard-of-living > 1 and Wife_age > 37 | 2 | 0.022586 |
| Wife_age <= 40 and Children <= 7 | 2 | 0.256504 |
|  | 1 | 0.569322 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|wife_religion|wife_working|contraceptive_method
---|---|---|---|---|---
(41.5-inf)|(3.5-inf)|(7.5-inf)|all|all|3
(31.5-41.5]|(3.5-inf)|(7.5-inf)|all|all|2
(31.5-41.5]|(2.5-3.5]|(7.5-inf)|all|all|3
(41.5-inf)|(2.5-3.5]|(7.5-inf)|all|all|1
(31.5-41.5]|(-inf-2.5]|(7.5-inf)|all|all|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|all|all|3
(41.5-inf)|(3.5-inf)|(2.5-7.5]|all|all|2
(31.5-41.5]|(3.5-inf)|(2.5-7.5]|all|all|2
(41.5-inf)|(-inf-2.5]|(7.5-inf)|all|all|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|all|all|1
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|all|all|3
(31.5-41.5]|(2.5-3.5]|(2.5-7.5]|all|all|1
(41.5-inf)|(3.5-inf)|(0.5-2.5]|all|all|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|all|all|1
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|all|all|3
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|all|all|3
(31.5-41.5]|(3.5-inf)|(0.5-2.5]|all|all|1
(31.5-41.5]|(-inf-2.5]|(2.5-7.5]|all|all|3
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|all|all|1
(31.5-41.5]|(2.5-3.5]|(0.5-2.5]|all|all|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|all|all|1
(41.5-inf)|(3.5-inf)|(-inf-0.5]|all|all|1
(31.5-41.5]|(3.5-inf)|(-inf-0.5]|all|all|1
(31.5-41.5]|(-inf-2.5]|(0.5-2.5]|all|all|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|all|all|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|all|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|all|1
(31.5-41.5]|(2.5-3.5]|(-inf-0.5]|all|all|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|all|all|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|all|all|1
(31.5-41.5]|(-inf-2.5]|(-inf-0.5]|all|all|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|all|all|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|all|all|1

## PART

Decision list:

rules | predicted class
---|---
Children > 0 AND Wife_education <= 3 AND Wife_age > 37|1 (179.0/46.0)
Children <= 0|1 (76.0/2.0)
Wife_education <= 3 AND Children <= 2 AND Wife_age > 30|1 (24.0/3.0)
Wife_education <= 3 AND Husband_education > 1 AND Children <= 2 AND Wife_age <= 25 AND Husband_occupation <= 2 AND Wife_age > 19 AND Standard-of-living <= 3 AND Husband_education <= 3 AND Wife_age <= 22|1 (9.0/4.0)
Wife_education <= 3 AND Husband_education > 1 AND Children <= 2 AND Wife_age <= 25 AND Husband_occupation <= 2 AND Wife_age <= 20|3 (11.0/3.0)
Wife_education <= 3 AND Husband_education > 1 AND Children <= 2 AND Standard-of-living > 1 AND Husband_education > 2|1 (111.0/56.0)
Standard-of-living <= 1 AND Wife_age <= 32 AND Wife_education <= 2|1 (40.0/13.0)
Wife_education <= 3 AND Husband_education > 1 AND Husband_occupation > 1 AND Wife_age <= 32 AND Children <= 5 AND Children > 1|3 (133.0/40.0)
Wife_age > 39 AND Children > 1|2 (97.0/48.0)
Children > 1 AND Wife_age <= 37 AND Husband_education > 1 AND Wife_education <= 2 AND Children <= 7 AND Standard-of-living <= 3|3 (34.0/11.0)
Children > 1 AND Wife_age <= 37 AND Husband_education > 2 AND Wife_age > 23 AND Standard-of-living > 3 AND Wife_age > 30 AND Wife_age > 31 AND Children > 2 AND Wife_age > 32 AND Wife_education > 3|2 (62.0/29.0)
Husband_education > 1 AND Wife_age <= 22|3 (37.0/16.0)
Standard-of-living > 1 AND Children <= 1 AND Wife_age <= 31 AND Wife_age > 24|1 (42.0/24.0)
Standard-of-living > 1 AND Wife_age <= 40 AND Children <= 7 AND Wife_age <= 37 AND Children <= 6 AND Husband_education > 2 AND Children > 1 AND Wife_religion > 0 AND Husband_occupation > 1 AND Wife_age <= 33|3 (64.0/25.0)
Wife_age <= 41 AND Children <= 7 AND Standard-of-living > 1 AND Wife_education > 1 AND Husband_education > 2 AND Wife_age <= 37 AND Standard-of-living > 3 AND Wife_age > 26 AND Wife_age <= 36|3 (77.0/42.0)
Wife_age <= 41 AND Children <= 7 AND Children <= 6 AND Standard-of-living > 1 AND Wife_age > 37|2 (32.0/15.0)
Wife_age <= 40 AND Children <= 7|2 (141.0/79.0)
|1 (24.0/8.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(83.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/114.0)
			* Children >= 2.5: 3(172.0/139.0)
		* Wife_age >= 37.5: 1(151.0/57.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 43.5: 3(88.0/117.0)
			* Wife_age >= 43.5: 1(12.0/1.0)
		* Children >= 2.5: 2(130.0/140.0)


