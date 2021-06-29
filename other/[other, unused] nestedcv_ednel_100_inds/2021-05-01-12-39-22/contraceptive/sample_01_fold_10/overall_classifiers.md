# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age < 37.5 | 3 | 0.105399 |
| Children < 0.5 | 1 | 0.099698 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children < 2.5 | 1 | 0.088628 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education < 2.5 | 1 | 0.079263 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age >= 33.5 | 2 | 0.040725 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation >= 1.5 | 3 | 0.031142 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education < 3.5 and Children >= 2.5 and Wife_age >= 37.5 | 1 | 0.024032 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education >= 3.5 and Children < 10.5 and Wife_age < 48.5 | 2 | 0.018514 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education < 3.5 | 1 | 0.021720 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age < 33.5 | 3 | 0.018786 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children < 1.5 | 1 | 0.020645 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 and Wife_age >= 25.5 and Children < 1.5 | 1 | 0.014492 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 and Wife_age >= 25.5 and Children >= 1.5 and Wife_age < 32.5 | 2 | 0.007340 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 and Wife_age < 25.5 | 2 | 0.005823 |
| Children >= 0.5 and Wife_age < 41.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 and Wife_age >= 25.5 and Children >= 1.5 and Wife_age >= 32.5 | 1 | 0.006005 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education >= 3.5 and Children < 10.5 and Wife_age >= 48.5 | 1 | 0.005461 |
| Children >= 0.5 and Wife_age >= 41.5 and Wife_education >= 2.5 and Children >= 1.5 and Wife_education >= 3.5 and Children >= 10.5 | 3 | 0.003460 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.0 | 1 | 0.099698 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children > 1.0 and Children <= 9.0 and Children <= 8.0 and Standard-of-living > 1.0 and Media_exposure <= 0.0 and Husband_education > 1.0 and Wife_age <= 46.0 and Wife_education > 1.0 and Wife_working > 0.0 and Children > 3.0 and Children > 4.0 and Wife_age <= 44.0 | 1 | 0.008258 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children > 1.0 and Children <= 9.0 and Children <= 8.0 and Standard-of-living > 1.0 and Media_exposure > 0.0 | 1 | 0.025888 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children > 1.0 and Husband_education > 1.0 and Wife_working > 0.0 and Wife_education <= 1.0 | 1 | 0.030072 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Children <= 1.0 | 1 | 0.021907 |
| Wife_education <= 3.0 and Wife_age > 38.0 and Husband_education > 1.0 and Wife_working > 0.0 and Standard-of-living > 2.0 and Children <= 3.0 | 1 | 0.011612 |
| Wife_education <= 3.0 and Wife_age > 38.0 and Husband_education <= 1.0 | 1 | 0.014632 |
| Wife_education <= 3.0 and Wife_age <= 46.0 and Children <= 2.0 and Husband_occupation <= 3.0 and Wife_age > 30.0 | 1 | 0.023014 |
| Wife_education <= 3.0 and Wife_age > 41.0 and Wife_working > 0.0 and Wife_age > 45.0 | 1 | 0.013907 |
| Wife_education <= 3.0 and Children <= 1.0 and Husband_occupation <= 3.0 and Standard-of-living <= 3.0 and Husband_occupation <= 2.0 | 1 | 0.015832 |
| Wife_education <= 3.0 and Wife_age <= 41.0 and Husband_occupation > 1.0 and Wife_age > 36.0 | 1 | 0.007692 |
| Wife_education <= 3.0 and Wife_age <= 32.0 and Husband_occupation > 1.0 and Husband_occupation <= 3.0 and Media_exposure > 0.0 and Children <= 3.0 | 3 | 0.010348 |
| Wife_education <= 3.0 and Wife_age <= 32.0 and Media_exposure <= 0.0 and Husband_occupation > 1.0 and Children > 2.0 and Wife_age > 23.0 and Wife_religion > 0.0 and Children <= 5.0 and Wife_age <= 31.0 and Wife_age > 27.0 | 3 | 0.048148 |
| Wife_education <= 2.0 and Wife_age <= 23.0 | 1 | 0.020553 |
| Husband_occupation > 1.0 and Wife_age <= 28.0 and Children > 2.0 and Wife_working > 0.0 and Husband_education > 3.0 | 3 | 0.038785 |
| Wife_education <= 3.0 and Wife_age > 41.0 and Wife_working <= 0.0 | 1 | 0.007740 |
| Husband_education <= 3.0 and Wife_age > 41.0 and Husband_occupation <= 1.0 | 2 | 0.004830 |
| Husband_education <= 3.0 and Wife_age > 41.0 and Standard-of-living <= 3.0 | 1 | 0.003827 |
| Husband_education <= 3.0 and Husband_education > 1.0 and Media_exposure <= 0.0 and Husband_occupation > 1.0 and Standard-of-living <= 3.0 and Wife_religion > 0.0 and Wife_age <= 33.0 and Wife_age <= 28.0 and Husband_occupation <= 2.0 | 3 | 0.030379 |
| Children > 2.0 and Wife_education <= 2.0 and Children <= 7.0 and Standard-of-living <= 3.0 and Wife_religion > 0.0 and Standard-of-living > 1.0 and Wife_age <= 35.0 | 3 | 0.035998 |
| Children > 2.0 and Media_exposure > 0.0 and Husband_education <= 3.0 | 1 | 0.012107 |
| Children > 2.0 and Wife_age > 33.0 and Children <= 7.0 and Wife_age > 47.0 and Wife_age <= 48.0 | 2 | 0.006932 |
| Children > 2.0 and Wife_age > 30.0 and Wife_age <= 42.0 and Wife_education > 3.0 and Husband_education > 3.0 and Standard-of-living > 2.0 and Wife_age > 33.0 | 2 | 0.077608 |
| Wife_age > 41.0 and Children > 1.0 | 2 | 0.032143 |
| Wife_age <= 38.0 and Husband_occupation > 1.0 and Children <= 2.0 and Husband_occupation <= 3.0 and Wife_education <= 3.0 | 1 | 0.047660 |
| Wife_age > 38.0 | 1 | 0.039346 |
| Wife_age <= 22.0 and Husband_occupation > 1.0 | 3 | 0.094140 |
| Children <= 1.0 and Wife_age <= 31.0 and Husband_occupation <= 3.0 and Wife_age > 24.0 | 1 | 0.011689 |
| Children <= 1.0 and Wife_age <= 25.0 | 2 | 0.031792 |
| Children > 1.0 and Husband_occupation > 2.0 and Wife_age <= 28.0 and Children <= 2.0 | 3 | 0.047389 |
| Children > 1.0 and Wife_education <= 2.0 | 3 | 0.079845 |
| Children > 1.0 and Husband_education > 2.0 and Wife_age > 35.0 | 2 | 0.012207 |
| Children <= 1.0 | 1 | 0.018580 |
| Wife_age <= 23.0 and Wife_age > 22.0 | 1 | 0.006146 |
| Husband_education <= 3.0 | 3 | 0.082446 |
| Wife_age <= 32.0 and Children <= 3.0 and Standard-of-living > 2.0 and Husband_occupation > 2.0 | 2 | 0.041153 |
| Standard-of-living > 3.0 and Wife_age <= 33.0 and Children <= 2.0 | 2 | 0.024794 |
| Standard-of-living <= 3.0 and Wife_age <= 34.0 and Wife_age <= 29.0 and Wife_age > 26.0 | 2 | 0.023671 |
| Wife_education <= 3.0 and Husband_occupation <= 2.0 and Husband_occupation > 1.0 | 1 | 0.049072 |
| Wife_education <= 3.0 and Children > 4.0 and Standard-of-living <= 3.0 | 2 | 0.026578 |
| Children > 4.0 | 3 | 0.140701 |
| Wife_education <= 3.0 and Husband_occupation <= 2.0 and Children <= 3.0 and Standard-of-living > 3.0 | 2 | 0.011850 |
| Wife_education > 3.0 and Husband_occupation <= 2.0 and Children <= 3.0 and Wife_age > 31.0 | 3 | 0.160832 |
| Wife_education <= 3.0 | 3 | 0.100229 |
| Wife_age > 30.0 and Children > 2.0 and Wife_working > 0.0 | 2 | 0.062179 |
| Wife_religion <= 0.0 | 1 | 0.039542 |
| Children <= 3.0 and Wife_age <= 25.0 | 3 | 0.116152 |
| Wife_working > 0.0 | 1 | 0.328195 |
|  | 3 | 0.505051 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 33 | 2 | 0.059110 |
| Wife_age <= 33 and Children >= 3 | 3 | 0.119890 |
| Wife_age <= 28 and Children >= 2 | 3 | 0.032476 |
|  | 1 | 0.576531 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 33)|2 (211.0/97.0)
(Wife_age <= 33) and (Children >= 3)|3 (278.0/117.0)
(Wife_age <= 28) and (Children >= 2)|3 (132.0/67.0)
|1 (703.0/287.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.0|1 (71.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children > 1.0 AND Children <= 9.0 AND Children <= 8.0 AND Standard-of-living > 1.0 AND Media_exposure <= 0.0 AND Husband_education > 1.0 AND Wife_age <= 46.0 AND Wife_education > 1.0 AND Wife_working > 0.0 AND Children > 3.0 AND Children > 4.0 AND Wife_age <= 44.0|1 (23.0/11.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children > 1.0 AND Children <= 9.0 AND Children <= 8.0 AND Standard-of-living > 1.0 AND Media_exposure > 0.0|1 (20.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children > 1.0 AND Husband_education > 1.0 AND Wife_working > 0.0 AND Wife_education <= 1.0|1 (24.0/3.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Children <= 1.0|1 (16.0)
Wife_education <= 3.0 AND Wife_age > 38.0 AND Husband_education > 1.0 AND Wife_working > 0.0 AND Standard-of-living > 2.0 AND Children <= 3.0|1 (14.0/3.0)
Wife_education <= 3.0 AND Wife_age > 38.0 AND Husband_education <= 1.0|1 (11.0)
Wife_education <= 3.0 AND Wife_age <= 46.0 AND Children <= 2.0 AND Husband_occupation <= 3.0 AND Wife_age > 30.0|1 (26.0/6.0)
Wife_education <= 3.0 AND Wife_age > 41.0 AND Wife_working > 0.0 AND Wife_age > 45.0|1 (18.0/4.0)
Wife_education <= 3.0 AND Children <= 1.0 AND Husband_occupation <= 3.0 AND Standard-of-living <= 3.0 AND Husband_occupation <= 2.0|1 (17.0/4.0)
Wife_education <= 3.0 AND Wife_age <= 41.0 AND Husband_occupation > 1.0 AND Wife_age > 36.0|1 (23.0/11.0)
Wife_education <= 3.0 AND Wife_age <= 32.0 AND Husband_occupation > 1.0 AND Husband_occupation <= 3.0 AND Media_exposure > 0.0 AND Children <= 3.0|3 (11.0/4.0)
Wife_education <= 3.0 AND Wife_age <= 32.0 AND Media_exposure <= 0.0 AND Husband_occupation > 1.0 AND Children > 2.0 AND Wife_age > 23.0 AND Wife_religion > 0.0 AND Children <= 5.0 AND Wife_age <= 31.0 AND Wife_age > 27.0|3 (43.0/10.0)
Wife_education <= 2.0 AND Wife_age <= 23.0|1 (32.0/13.0)
Husband_occupation > 1.0 AND Wife_age <= 28.0 AND Children > 2.0 AND Wife_working > 0.0 AND Husband_education > 3.0|3 (33.0/6.0)
Wife_education <= 3.0 AND Wife_age > 41.0 AND Wife_working <= 0.0|1 (14.0/6.0)
Husband_education <= 3.0 AND Wife_age > 41.0 AND Husband_occupation <= 1.0|2 (5.0/2.0)
Husband_education <= 3.0 AND Wife_age > 41.0 AND Standard-of-living <= 3.0|1 (4.0/1.0)
Husband_education <= 3.0 AND Husband_education > 1.0 AND Media_exposure <= 0.0 AND Husband_occupation > 1.0 AND Standard-of-living <= 3.0 AND Wife_religion > 0.0 AND Wife_age <= 33.0 AND Wife_age <= 28.0 AND Husband_occupation <= 2.0|3 (22.0/5.0)
Children > 2.0 AND Wife_education <= 2.0 AND Children <= 7.0 AND Standard-of-living <= 3.0 AND Wife_religion > 0.0 AND Standard-of-living > 1.0 AND Wife_age <= 35.0|3 (35.0/10.0)
Children > 2.0 AND Media_exposure > 0.0 AND Husband_education <= 3.0|1 (11.0/2.0)
Children > 2.0 AND Wife_age > 33.0 AND Children <= 7.0 AND Wife_age > 47.0 AND Wife_age <= 48.0|2 (7.0/2.0)
Children > 2.0 AND Wife_age > 30.0 AND Wife_age <= 42.0 AND Wife_education > 3.0 AND Husband_education > 3.0 AND Standard-of-living > 2.0 AND Wife_age > 33.0|2 (102.0/38.0)
Wife_age > 41.0 AND Children > 1.0|2 (54.0/30.0)
Wife_age <= 38.0 AND Husband_occupation > 1.0 AND Children <= 2.0 AND Husband_occupation <= 3.0 AND Wife_education <= 3.0|1 (92.0/52.0)
Wife_age > 38.0|1 (24.0/8.0)
Wife_age <= 22.0 AND Husband_occupation > 1.0|3 (20.0/7.0)
Children <= 1.0 AND Wife_age <= 31.0 AND Husband_occupation <= 3.0 AND Wife_age > 24.0|1 (35.0/20.0)
Children <= 1.0 AND Wife_age <= 25.0|2 (31.0/16.0)
Children > 1.0 AND Husband_occupation > 2.0 AND Wife_age <= 28.0 AND Children <= 2.0|3 (11.0/3.0)
Children > 1.0 AND Wife_education <= 2.0|3 (39.0/22.0)
Children > 1.0 AND Husband_education > 2.0 AND Wife_age > 35.0|2 (23.0/12.0)
Children <= 1.0|1 (9.0/1.0)
Wife_age <= 23.0 AND Wife_age > 22.0|1 (5.0/2.0)
Husband_education <= 3.0|3 (37.0/18.0)
Wife_age <= 32.0 AND Children <= 3.0 AND Standard-of-living > 2.0 AND Husband_occupation > 2.0|2 (10.0/5.0)
Standard-of-living > 3.0 AND Wife_age <= 33.0 AND Children <= 2.0|2 (21.0/10.0)
Standard-of-living <= 3.0 AND Wife_age <= 34.0 AND Wife_age <= 29.0 AND Wife_age > 26.0|2 (15.0/4.0)
Wife_education <= 3.0 AND Husband_occupation <= 2.0 AND Husband_occupation > 1.0|1 (7.0/3.0)
Wife_education <= 3.0 AND Children > 4.0 AND Standard-of-living <= 3.0|2 (4.0)
Children > 4.0|3 (11.0/4.0)
Wife_education <= 3.0 AND Husband_occupation <= 2.0 AND Children <= 3.0 AND Standard-of-living > 3.0|2 (5.0/2.0)
Wife_education > 3.0 AND Husband_occupation <= 2.0 AND Children <= 3.0 AND Wife_age > 31.0|3 (19.0/10.0)
Wife_education <= 3.0|3 (12.0/5.0)
Wife_age > 30.0 AND Children > 2.0 AND Wife_working > 0.0|2 (10.0/2.0)
Wife_religion <= 0.0|1 (9.0/4.0)
Children <= 3.0 AND Wife_age <= 25.0|3 (7.0/3.0)
Wife_working > 0.0|1 (7.0/2.0)
|3 (5.0/2.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(86.0/2.0)
* Children >= 0.5
	* Wife_age < 41.5
		* Wife_education < 3.5
			* Children < 2.5: 1(130.0/117.0)
			* Children >= 2.5
				* Wife_age < 37.5: 3(170.0/135.0)
				* Wife_age >= 37.5: 1(31.0/21.0)
		* Wife_education >= 3.5
			* Children < 2.5
				* Husband_occupation < 1.5
					* Wife_age < 25.5: 2(14.0/19.0)
					* Wife_age >= 25.5
						* Children < 1.5: 1(17.0/9.0)
						* Children >= 1.5
							* Wife_age < 32.5: 2(14.0/12.0)
							* Wife_age >= 32.5: 1(10.0/12.0)
				* Husband_occupation >= 1.5: 3(51.0/45.0)
			* Children >= 2.5
				* Wife_age < 33.5: 3(35.0/41.0)
				* Wife_age >= 33.5: 2(71.0/47.0)
	* Wife_age >= 41.5
		* Wife_education < 2.5: 1(77.0/14.0)
		* Wife_education >= 2.5
			* Children < 1.5: 1(16.0/0.0)
			* Children >= 1.5
				* Wife_education < 3.5: 1(28.0/19.0)
				* Wife_education >= 3.5
					* Children < 10.5
						* Wife_age < 48.5: 2(37.0/35.0)
						* Wife_age >= 48.5: 1(5.0/1.0)
					* Children >= 10.5: 3(3.0/0.0)


