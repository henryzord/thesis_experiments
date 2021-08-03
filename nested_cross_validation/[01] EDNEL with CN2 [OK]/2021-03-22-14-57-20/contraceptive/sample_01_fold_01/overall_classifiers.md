# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426737 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education < 3.5 and Children >= 2.5 | 3 | 0.104170 |
| Children >= 0.5 and Wife_age >= 37.5 and Wife_education >= 3.5 and Children >= 1.5 | 2 | 0.038339 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education >= 3.5 and Wife_age < 28.5 | 3 | 0.038895 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education >= 3.5 and Wife_age >= 28.5 and Children >= 2.5 | 2 | 0.025591 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 0.5 and Children <= 1.5 and Wife_working = all | 3 | 0.013806 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 2 | 0.009331 |
| Children >= 0.5 and Wife_age < 37.5 and Wife_education >= 3.5 and Wife_age >= 28.5 and Children < 2.5 | 3 | 0.011415 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 3 | 0.044264 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 3 | 0.042917 |
| Wife_age > 37.5 and Wife_education > 3.5 and Children > 7.5 and Wife_working = all | 3 | 0.003211 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 2 | 0.023639 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 3 | 0.032578 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 2.5 and Children > 1.5 and Children <= 7.5 and Wife_working = all | 3 | 0.024254 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0 and Wife_age > 37 and Wife_education <= 3 and Wife_working > 0 | 1 | 0.107124 |
| Children <= 0 | 1 | 0.094330 |
| Wife_education <= 3 and Wife_age <= 20 and Husband_occupation <= 2 | 3 | 0.010109 |
| Wife_education <= 2 and Wife_age > 37 and Standard-of-living <= 3 | 1 | 0.015917 |
| Children <= 2 and Wife_age > 34 | 1 | 0.034892 |
| Wife_education <= 3 and Wife_age <= 20 | 1 | 0.022625 |
| Wife_education <= 3 and Husband_occupation > 1 and Husband_education <= 1 and Wife_education > 1 | 2 | 0.005472 |
| Wife_education <= 3 and Husband_occupation > 1 and Children > 2 and Media_exposure <= 0 and Wife_age <= 31 and Standard-of-living <= 2 and Wife_education > 2 | 3 | 0.020312 |
| Wife_education <= 3 and Husband_occupation > 1 and Wife_working > 0 and Children <= 1 and Standard-of-living <= 3 and Husband_occupation <= 2 | 1 | 0.010990 |
| Wife_education <= 2 and Media_exposure <= 0 and Children <= 1 | 1 | 0.016553 |
| Wife_education <= 3 and Husband_occupation > 1 and Children > 7 and Standard-of-living <= 3 | 1 | 0.005586 |
| Wife_education <= 2 and Husband_occupation > 1 and Media_exposure <= 0 and Wife_age > 23 and Husband_education > 1 and Wife_working <= 0 and Children > 3 | 3 | 0.017491 |
| Wife_age > 34 and Wife_age <= 48 and Media_exposure <= 0 and Children <= 7 and Wife_age <= 47 and Wife_education > 3 and Wife_working <= 0 and Standard-of-living > 3 and Wife_age > 38 | 2 | 0.019665 |
| Wife_education <= 2 and Husband_occupation > 1 and Wife_working > 0 and Wife_age > 32 | 3 | 0.035667 |
| Wife_education <= 2 and Husband_occupation > 1 and Media_exposure <= 0 and Wife_age <= 30 and Wife_age > 23 and Wife_working > 0 and Husband_education <= 3 and Children > 2 and Children > 3 | 3 | 0.023024 |
| Wife_education <= 2 and Husband_occupation > 1 and Children <= 6 and Media_exposure <= 0 and Wife_education <= 1 | 3 | 0.016451 |
| Wife_age > 34 and Wife_age <= 48 and Children <= 7 and Media_exposure <= 0 and Wife_age <= 47 and Wife_age <= 46 and Standard-of-living <= 3 | 2 | 0.035175 |
| Standard-of-living <= 2 and Wife_religion > 0 and Husband_education > 2 and Wife_age <= 32 and Husband_education <= 3 | 3 | 0.028815 |
| Standard-of-living <= 2 and Husband_education <= 3 | 1 | 0.035468 |
| Standard-of-living <= 2 and Wife_religion > 0 and Wife_age <= 32 and Wife_age <= 30 and Children <= 3 and Wife_education <= 3 | 1 | 0.005942 |
| Wife_age <= 30 and Husband_occupation > 1 and Standard-of-living > 2 and Wife_education <= 2 and Husband_occupation > 2 and Children > 2 and Wife_age <= 27 | 1 | 0.006130 |
| Children > 2 and Wife_education <= 3 and Children <= 7 and Media_exposure <= 0 and Wife_age <= 30 | 3 | 0.066191 |
| Wife_age <= 26 and Standard-of-living > 2 and Husband_education > 2 and Wife_religion > 0 and Wife_age > 21 and Husband_education > 3 and Wife_education > 2 and Children > 1 | 3 | 0.031225 |
| Wife_age > 22 and Standard-of-living > 3 and Children <= 7 and Wife_age <= 46 and Wife_age > 32 and Children > 2 and Wife_education > 3 and Wife_working > 0 and Wife_age > 33 and Wife_age > 35 and Husband_occupation <= 1 | 2 | 0.046419 |
| Children > 7 | 3 | 0.019356 |
| Wife_age > 47 and Wife_age <= 48 | 2 | 0.008353 |
| Wife_age <= 22 | 3 | 0.068837 |
| Wife_age <= 46 and Wife_age > 36 and Wife_education <= 3 | 3 | 0.017875 |
| Wife_age <= 46 and Wife_education <= 2 and Media_exposure <= 0 and Wife_age > 26 | 1 | 0.034667 |
| Wife_age > 43 | 1 | 0.019378 |
| Wife_age > 36 and Wife_age <= 39 and Wife_working > 0 | 2 | 0.015513 |
| Standard-of-living > 3 and Wife_age > 23 and Wife_age > 32 and Husband_occupation <= 2 and Wife_age > 33 and Children > 2 and Wife_working > 0 and Wife_age > 34 | 3 | 0.040909 |
| Children > 2 and Wife_education > 2 and Wife_age <= 36 and Standard-of-living > 3 | 3 | 0.041679 |
| Wife_age > 32 and Wife_education > 3 and Wife_religion > 0 | 3 | 0.033167 |
| Children > 2 and Wife_age <= 33 and Husband_occupation > 2 and Wife_education <= 3 | 3 | 0.015279 |
| Standard-of-living <= 2 | 1 | 0.018169 |
| Children > 1 and Children <= 5 and Wife_education > 3 and Wife_age <= 29 and Wife_age <= 28 and Husband_occupation <= 1 | 2 | 0.019378 |
| Children > 2 and Wife_age > 31 and Children <= 5 and Children <= 3 | 1 | 0.018715 |
| Children <= 1 and Wife_age <= 31 and Wife_age > 27 | 1 | 0.012759 |
| Children <= 5 and Wife_religion <= 0 and Children > 1 and Standard-of-living <= 3 | 2 | 0.022339 |
| Children <= 5 and Husband_education > 2 and Children <= 2 and Wife_working > 0 and Wife_age > 24 and Wife_age <= 25 | 3 | 0.011836 |
| Husband_education > 2 and Children <= 5 and Children <= 2 and Wife_education <= 3 and Wife_age > 28 | 1 | 0.012339 |
| Husband_education > 2 and Children <= 5 and Wife_age <= 32 and Children <= 2 and Wife_education > 2 and Wife_working <= 0 and Wife_age > 25 | 2 | 0.045714 |
| Husband_education > 2 and Children <= 2 and Wife_age > 26 and Children > 1 | 3 | 0.057665 |
| Husband_education > 2 and Wife_religion > 0 and Wife_working <= 0 | 1 | 0.051610 |
| Husband_education > 2 and Wife_religion > 0 and Children > 1 and Husband_occupation > 1 | 1 | 0.043697 |
| Wife_religion <= 0 | 2 | 0.150943 |
| Husband_education > 2 and Wife_education <= 3 | 2 | 0.289803 |
| Wife_education > 3 and Husband_occupation <= 2 and Standard-of-living > 3 | 1 | 0.055848 |
| Husband_occupation <= 2 | 3 | 0.157143 |
| Wife_education <= 3 | 1 | 0.054236 |
|  | 2 | 0.688073 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.056953 |
| Wife_age <= 35 and Children >= 2 and Husband_occupation >= 2 | 3 | 0.155562 |
|  | 1 | 0.571284 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|wife_working|contraceptive_method
---|---|---|---|---
(31.5-37.5]|(3.5-inf)|(7.5-inf)|all|1
(37.5-inf)|(3.5-inf)|(7.5-inf)|all|3
(31.5-37.5]|(2.5-3.5]|(7.5-inf)|all|3
(37.5-inf)|(2.5-3.5]|(7.5-inf)|all|1
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|all|1
(-inf-31.5]|(3.5-inf)|(1.5-7.5]|all|3
(31.5-37.5]|(-inf-2.5]|(7.5-inf)|all|3
(37.5-inf)|(-inf-2.5]|(7.5-inf)|all|1
(37.5-inf)|(3.5-inf)|(1.5-7.5]|all|2
(31.5-37.5]|(3.5-inf)|(1.5-7.5]|all|2
(31.5-37.5]|(2.5-3.5]|(1.5-7.5]|all|2
(37.5-inf)|(2.5-3.5]|(1.5-7.5]|all|1
(-inf-31.5]|(2.5-3.5]|(1.5-7.5]|all|3
(37.5-inf)|(3.5-inf)|(0.5-1.5]|all|1
(31.5-37.5]|(3.5-inf)|(0.5-1.5]|all|1
(-inf-31.5]|(3.5-inf)|(0.5-1.5]|all|3
(-inf-31.5]|(-inf-2.5]|(1.5-7.5]|all|3
(31.5-37.5]|(-inf-2.5]|(1.5-7.5]|all|3
(37.5-inf)|(-inf-2.5]|(1.5-7.5]|all|1
(37.5-inf)|(2.5-3.5]|(0.5-1.5]|all|1
(31.5-37.5]|(2.5-3.5]|(0.5-1.5]|all|1
(-inf-31.5]|(2.5-3.5]|(0.5-1.5]|all|3
(37.5-inf)|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-2.5]|(0.5-1.5]|all|1
(37.5-inf)|(-inf-2.5]|(0.5-1.5]|all|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-2.5]|(0.5-1.5]|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|all|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|all|1
(37.5-inf)|(2.5-3.5]|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|all|1
(37.5-inf)|(-inf-2.5]|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (192.0/85.0)
(Wife_age <= 35) and (Children >= 2) and (Husband_occupation >= 2)|3 (419.0/193.0)
|1 (713.0/304.0)


## PART

Decision list:

rules | predicted class
---|---
Children > 0 AND Wife_age > 37 AND Wife_education <= 3 AND Wife_working > 0|1 (122.0/28.0)
Children <= 0|1 (69.0/1.0)
Wife_education <= 3 AND Wife_age <= 20 AND Husband_occupation <= 2|3 (15.0/6.0)
Wife_education <= 2 AND Wife_age > 37 AND Standard-of-living <= 3|1 (16.0)
Children <= 2 AND Wife_age > 34|1 (43.0/12.0)
Wife_education <= 3 AND Wife_age <= 20|1 (15.0/3.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Husband_education <= 1 AND Wife_education > 1|2 (7.0/1.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Children > 2 AND Media_exposure <= 0 AND Wife_age <= 31 AND Standard-of-living <= 2 AND Wife_education > 2|3 (13.0/2.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Wife_working > 0 AND Children <= 1 AND Standard-of-living <= 3 AND Husband_occupation <= 2|1 (11.0/2.0)
Wife_education <= 2 AND Media_exposure <= 0 AND Children <= 1|1 (28.0/11.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Children > 7 AND Standard-of-living <= 3|1 (12.0/3.0)
Wife_education <= 2 AND Husband_occupation > 1 AND Media_exposure <= 0 AND Wife_age > 23 AND Husband_education > 1 AND Wife_working <= 0 AND Children > 3|3 (16.0/5.0)
Wife_age > 34 AND Wife_age <= 48 AND Media_exposure <= 0 AND Children <= 7 AND Wife_age <= 47 AND Wife_education > 3 AND Wife_working <= 0 AND Standard-of-living > 3 AND Wife_age > 38|2 (14.0/2.0)
Wife_education <= 2 AND Husband_occupation > 1 AND Wife_working > 0 AND Wife_age > 32|3 (29.0/9.0)
Wife_education <= 2 AND Husband_occupation > 1 AND Media_exposure <= 0 AND Wife_age <= 30 AND Wife_age > 23 AND Wife_working > 0 AND Husband_education <= 3 AND Children > 2 AND Children > 3|3 (17.0/3.0)
Wife_education <= 2 AND Husband_occupation > 1 AND Children <= 6 AND Media_exposure <= 0 AND Wife_education <= 1|3 (15.0/4.0)
Wife_age > 34 AND Wife_age <= 48 AND Children <= 7 AND Media_exposure <= 0 AND Wife_age <= 47 AND Wife_age <= 46 AND Standard-of-living <= 3|2 (28.0/7.0)
Standard-of-living <= 2 AND Wife_religion > 0 AND Husband_education > 2 AND Wife_age <= 32 AND Husband_education <= 3|3 (24.0/10.0)
Standard-of-living <= 2 AND Husband_education <= 3|1 (16.0/5.0)
Standard-of-living <= 2 AND Wife_religion > 0 AND Wife_age <= 32 AND Wife_age <= 30 AND Children <= 3 AND Wife_education <= 3|1 (8.0/3.0)
Wife_age <= 30 AND Husband_occupation > 1 AND Standard-of-living > 2 AND Wife_education <= 2 AND Husband_occupation > 2 AND Children > 2 AND Wife_age <= 27|1 (11.0/6.0)
Children > 2 AND Wife_education <= 3 AND Children <= 7 AND Media_exposure <= 0 AND Wife_age <= 30|3 (44.0/13.0)
Wife_age <= 26 AND Standard-of-living > 2 AND Husband_education > 2 AND Wife_religion > 0 AND Wife_age > 21 AND Husband_education > 3 AND Wife_education > 2 AND Children > 1|3 (32.0/11.0)
Wife_age > 22 AND Standard-of-living > 3 AND Children <= 7 AND Wife_age <= 46 AND Wife_age > 32 AND Children > 2 AND Wife_education > 3 AND Wife_working > 0 AND Wife_age > 33 AND Wife_age > 35 AND Husband_occupation <= 1|2 (40.0/11.0)
Children > 7|3 (14.0/4.0)
Wife_age > 47 AND Wife_age <= 48|2 (8.0/3.0)
Wife_age <= 22|3 (29.0/10.0)
Wife_age <= 46 AND Wife_age > 36 AND Wife_education <= 3|3 (11.0/3.0)
Wife_age <= 46 AND Wife_education <= 2 AND Media_exposure <= 0 AND Wife_age > 26|1 (11.0/2.0)
Wife_age > 43|1 (17.0/7.0)
Wife_age > 36 AND Wife_age <= 39 AND Wife_working > 0|2 (6.0/3.0)
Standard-of-living > 3 AND Wife_age > 23 AND Wife_age > 32 AND Husband_occupation <= 2 AND Wife_age > 33 AND Children > 2 AND Wife_working > 0 AND Wife_age > 34|3 (17.0/10.0)
Children > 2 AND Wife_education > 2 AND Wife_age <= 36 AND Standard-of-living > 3|3 (52.0/28.0)
Wife_age > 32 AND Wife_education > 3 AND Wife_religion > 0|3 (14.0/6.0)
Children > 2 AND Wife_age <= 33 AND Husband_occupation > 2 AND Wife_education <= 3|3 (9.0/4.0)
Standard-of-living <= 2|1 (19.0/10.0)
Children > 1 AND Children <= 5 AND Wife_education > 3 AND Wife_age <= 29 AND Wife_age <= 28 AND Husband_occupation <= 1|2 (7.0/1.0)
Children > 2 AND Wife_age > 31 AND Children <= 5 AND Children <= 3|1 (7.0/4.0)
Children <= 1 AND Wife_age <= 31 AND Wife_age > 27|1 (13.0/7.0)
Children <= 5 AND Wife_religion <= 0 AND Children > 1 AND Standard-of-living <= 3|2 (7.0/3.0)
Children <= 5 AND Husband_education > 2 AND Children <= 2 AND Wife_working > 0 AND Wife_age > 24 AND Wife_age <= 25|3 (9.0/4.0)
Husband_education > 2 AND Children <= 5 AND Children <= 2 AND Wife_education <= 3 AND Wife_age > 28|1 (11.0/4.0)
Husband_education > 2 AND Children <= 5 AND Wife_age <= 32 AND Children <= 2 AND Wife_education > 2 AND Wife_working <= 0 AND Wife_age > 25|2 (18.0/7.0)
Husband_education > 2 AND Children <= 2 AND Wife_age > 26 AND Children > 1|3 (14.0/4.0)
Husband_education > 2 AND Wife_religion > 0 AND Wife_working <= 0|1 (15.0/7.0)
Husband_education > 2 AND Wife_religion > 0 AND Children > 1 AND Husband_occupation > 1|1 (8.0/4.0)
Wife_religion <= 0|2 (7.0/3.0)
Husband_education > 2 AND Wife_education <= 3|2 (6.0/2.0)
Wife_education > 3 AND Husband_occupation <= 2 AND Standard-of-living > 3|1 (6.0/4.0)
Husband_occupation <= 2|3 (5.0/2.0)
Wife_education <= 3|1 (4.0/2.0)
|2 (4.0/2.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(81.0/2.0)
* Children >= 0.5
	* Wife_age < 37.5
		* Wife_education < 3.5
			* Children < 2.5: 1(121.0/115.0)
			* Children >= 2.5: 3(169.0/137.0)
		* Wife_education >= 3.5
			* Wife_age < 28.5: 3(70.0/77.0)
			* Wife_age >= 28.5
				* Children < 2.5: 3(26.0/44.0)
				* Children >= 2.5: 2(55.0/61.0)
	* Wife_age >= 37.5
		* Wife_education < 3.5: 1(152.0/59.0)
		* Wife_education >= 3.5
			* Children < 1.5: 1(16.0/1.0)
			* Children >= 1.5: 2(74.0/64.0)


