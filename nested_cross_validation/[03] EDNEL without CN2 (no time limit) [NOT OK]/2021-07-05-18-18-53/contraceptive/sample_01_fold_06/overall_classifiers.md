# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.106154 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.061668 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 43.5 | 3 | 0.045186 |
| Children > 0.0 and Wife_education <= 3.0 and Wife_age <= 37.0 and Children <= 2.0 and Wife_age <= 22.0 | 3 | 0.022810 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_religion = all | 3 | 0.010123 |
| Children > 0.0 and Wife_education > 3.0 and Children <= 2.0 and Wife_age <= 32.0 and Husband_occupation <= 1.0 and Wife_age > 23.0 and Wife_age > 25.0 and Children > 1.0 | 2 | 0.007340 |
| Children > 0.0 and Wife_education > 3.0 and Children > 2.0 and Wife_age > 28.0 and Standard-of-living > 3.0 and Wife_age <= 32.0 | 3 | 0.010763 |
| Children > 0.0 and Wife_education > 3.0 and Children <= 2.0 and Wife_age <= 32.0 and Husband_occupation <= 1.0 and Wife_age <= 23.0 | 2 | 0.003190 |
| Wife_age > 41.5 and Wife_education > 3.5 and Children > 7.5 and Wife_religion = all | 3 | 0.002312 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Children > 2.5 and Children <= 7.5 and Wife_religion = all | 3 | 0.023282 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 7.5 and Wife_religion = all | 3 | 0.004152 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.5 | 1 | 0.096370 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Media_exposure > 0.5 | 1 | 0.044301 |
| Wife_age > 41.5 and Husband_education <= 2.5 | 1 | 0.032757 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children <= 9.5 and Children > 1.5 and Wife_working > 0.5 and Wife_age > 45.5 | 1 | 0.019027 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 9.5 | 1 | 0.011719 |
| Wife_education <= 3.5 and Children <= 2.5 and Wife_age <= 25.5 and Husband_occupation <= 2.5 and Wife_age > 20.5 and Standard-of-living > 2.5 | 3 | 0.008819 |
| Wife_education <= 3.5 and Children <= 2.5 and Wife_age <= 23.5 | 3 | 0.028909 |
| Wife_education <= 3.5 and Children <= 2.5 and Media_exposure <= 0.5 and Standard-of-living > 2.5 and Wife_age > 30.5 | 1 | 0.032564 |
| Wife_education <= 2.5 and Children <= 2.5 and Wife_working > 0.5 and Standard-of-living <= 2.5 | 1 | 0.031631 |
| Wife_education <= 3.5 and Children > 2.5 and Wife_age <= 32.5 and Husband_occupation > 1.5 and Husband_education > 1.5 and Wife_age <= 24.5 and Children <= 3.5 | 3 | 0.012719 |
| Wife_education <= 3.5 and Children > 2.5 and Wife_age <= 37.5 and Husband_education > 1.5 and Husband_occupation > 1.5 and Wife_age <= 32.5 and Wife_age > 24.5 and Standard-of-living <= 2.5 and Children <= 4.5 and Husband_education > 2.5 | 3 | 0.025952 |
| Wife_education <= 3.5 and Children > 2.5 and Wife_age <= 37.5 and Standard-of-living > 2.5 and Media_exposure <= 0.5 and Husband_occupation > 2.5 | 3 | 0.070829 |
| Wife_education <= 3.5 and Husband_education > 1.5 and Children <= 1.5 | 1 | 0.044968 |
| Wife_education <= 2.5 and Husband_education > 1.5 and Husband_occupation > 1.5 and Children <= 7.5 and Husband_education <= 2.5 and Standard-of-living > 1.5 | 3 | 0.017653 |
| Wife_education <= 2.5 and Children > 2.5 and Standard-of-living <= 3.5 and Children <= 3.5 | 1 | 0.016581 |
| Wife_education > 3.5 and Wife_age > 44.5 and Children > 1.5 and Wife_working > 0.5 and Wife_age <= 46.5 | 2 | 0.008935 |
| Wife_education > 3.5 and Wife_age > 44.5 and Children <= 1.5 | 1 | 0.017094 |
| Wife_education > 3.5 and Husband_education <= 3.5 | 3 | 0.020028 |
| Husband_education <= 3.5 and Husband_education > 1.5 and Husband_occupation > 1.5 and Children > 6.5 | 1 | 0.013462 |
| Wife_education <= 1.5 | 1 | 0.016618 |
| Wife_age > 37.5 and Children <= 2.5 and Wife_age > 39.5 | 1 | 0.003223 |
| Wife_age > 37.5 and Wife_age <= 47.5 and Wife_education > 3.5 and Children > 3.5 | 2 | 0.054535 |
| Wife_age > 39.5 and Husband_occupation > 1.5 and Wife_age > 40.5 and Standard-of-living > 3.5 | 1 | 0.008641 |
| Wife_age > 40.5 and Wife_age > 42.5 and Wife_age > 44.5 | 1 | 0.006625 |
| Wife_age > 40.5 | 2 | 0.035556 |
| Wife_age > 38.5 and Husband_occupation > 2.5 | 1 | 0.004739 |
| Husband_education > 3.5 and Children > 2.5 and Standard-of-living > 1.5 and Media_exposure <= 0.5 and Wife_education > 2.5 and Wife_age > 35.5 and Wife_education > 3.5 and Husband_occupation > 1.5 and Wife_religion <= 0.5 | 2 | 0.006806 |
| Husband_education > 3.5 and Wife_education > 2.5 and Children > 2.5 and Standard-of-living > 1.5 and Wife_age > 32.5 and Standard-of-living > 2.5 and Wife_education > 3.5 and Wife_age > 36.5 | 2 | 0.005708 |
| Wife_age > 36.5 and Standard-of-living > 3.5 and Wife_education <= 3.5 | 3 | 0.024627 |
| Wife_age > 36.5 and Standard-of-living <= 3.5 and Husband_occupation > 1.5 | 1 | 0.005474 |
| Media_exposure > 0.5 and Husband_occupation <= 2.5 | 2 | 0.003756 |
| Husband_education > 2.5 and Standard-of-living > 1.5 and Children > 2.5 and Wife_age > 33.5 and Husband_occupation <= 2.5 and Wife_working > 0.5 and Children > 3.5 and Husband_occupation <= 1.5 | 3 | 0.046569 |
| Wife_age > 33.5 and Children > 2.5 and Wife_education > 2.5 | 2 | 0.036410 |
| Wife_age > 33.5 and Standard-of-living <= 3.5 | 1 | 0.028383 |
| Wife_age <= 35.5 and Children > 3.5 and Wife_age <= 29.5 and Husband_occupation > 1.5 | 3 | 0.018653 |
| Wife_age > 35.5 | 1 | 0.016752 |
| Standard-of-living <= 1.5 | 3 | 0.022040 |
| Wife_education > 2.5 and Wife_age > 20.5 and Children > 1.5 and Wife_age <= 24.5 and Husband_occupation > 2.5 | 3 | 0.008781 |
| Wife_age > 20.5 and Wife_age <= 24.5 and Children <= 1.5 and Husband_occupation <= 1.5 | 2 | 0.020325 |
| Wife_age <= 22.5 | 3 | 0.012878 |
| Wife_age <= 24.5 and Husband_occupation <= 2.5 | 1 | 0.032470 |
| Children > 1.5 and Wife_education > 2.5 and Wife_age <= 25.5 | 3 | 0.013570 |
| Wife_age > 24.5 and Wife_age > 25.5 and Children <= 1.5 and Husband_occupation <= 1.5 | 1 | 0.015312 |
| Wife_age > 24.5 and Wife_age > 25.5 and Wife_education > 2.5 and Wife_age <= 33.5 and Wife_working <= 0.5 | 3 | 0.058885 |
| Wife_age > 24.5 and Wife_age > 25.5 and Wife_working > 0.5 and Wife_education > 2.5 and Husband_education > 3.5 and Children > 2.5 and Children <= 4.5 and Wife_age <= 32.5 and Standard-of-living > 3.5 | 3 | 0.016598 |
| Wife_age > 24.5 and Wife_age > 25.5 and Wife_working > 0.5 and Wife_education > 2.5 and Children > 2.5 and Children <= 4.5 | 2 | 0.046711 |
| Wife_age > 24.5 and Wife_age > 25.5 and Wife_age > 30.5 and Husband_occupation <= 2.5 | 3 | 0.134660 |
| Wife_age > 24.5 and Wife_age <= 30.5 and Wife_age <= 25.5 | 1 | 0.019036 |
| Wife_age > 25.0 and Wife_age <= 30.5 and Wife_religion <= 0.5 | 2 | 0.022679 |
| Wife_age > 25.0 and Wife_age <= 30.5 and Husband_occupation > 1.5 and Wife_education <= 3.5 and Wife_education <= 2.5 | 1 | 0.019176 |
| Wife_age > 25.0 and Wife_age <= 30.5 and Husband_occupation > 1.5 and Wife_education <= 3.5 | 2 | 0.038007 |
| Wife_age > 25.0 and Children <= 3.5 and Wife_education <= 3.5 | 2 | 0.022695 |
| Wife_age > 25.0 and Wife_age <= 29.5 | 3 | 0.076916 |
| Wife_age > 27.0 | 1 | 0.189598 |
|  | 2 | 0.503067 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age <= 41 and Wife_age >= 38 and Husband_occupation <= 2 and Wife_religion <= 0 | 2 | 0.009662 |
| Wife_education >= 4 and Children >= 3 and Wife_religion >= 1 and Husband_occupation <= 1 and Wife_age >= 37 and Wife_age <= 40 and Wife_working >= 1 and Children <= 5 | 2 | 0.010692 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 33 and Wife_working <= 0 and Wife_religion >= 1 | 2 | 0.012457 |
| Wife_education >= 4 and Standard-of-living >= 4 and Children >= 4 and Children <= 4 and Wife_age >= 37 and Husband_education >= 4 and Wife_age <= 45 | 2 | 0.008792 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 29 and Husband_occupation >= 3 and Wife_age <= 35 and Children <= 4 and Standard-of-living <= 3 | 2 | 0.007135 |
| Wife_education >= 4 and Children >= 3 and Wife_age >= 33 and Standard-of-living >= 4 and Wife_age <= 34 | 2 | 0.006074 |
| Husband_occupation <= 1 and Children >= 2 and Wife_age <= 29 and Children <= 3 and Wife_age >= 26 and Standard-of-living <= 3 | 2 | 0.006074 |
| Wife_education >= 4 and Children >= 6 and Wife_age <= 45 and Children <= 7 and Wife_age >= 40 | 2 | 0.008067 |
| Standard-of-living >= 4 and Wife_education >= 3 and Children >= 2 and Wife_age >= 45 and Wife_age <= 46 | 2 | 0.005722 |
| Children >= 3 and Husband_occupation >= 3 and Wife_age <= 32 and Wife_education >= 3 and Wife_working >= 1 and Wife_age >= 29 | 3 | 0.026718 |
| Children >= 3 and Wife_age <= 29 and Husband_occupation >= 2 and Standard-of-living >= 2 and Wife_age >= 28 and Wife_education <= 2 and Children <= 5 | 3 | 0.017972 |
| Children >= 3 and Husband_occupation >= 3 and Standard-of-living >= 3 and Standard-of-living <= 3 and Wife_age <= 30 and Wife_age >= 24 and Husband_education >= 3 and Children <= 4 | 3 | 0.017972 |
| Children >= 3 and Standard-of-living >= 2 and Wife_education <= 2 and Standard-of-living <= 3 and Wife_age <= 29 and Husband_education <= 2 | 3 | 0.010479 |
| Children >= 2 and Wife_education >= 4 and Wife_age <= 27 and Husband_occupation >= 3 | 3 | 0.014050 |
| Children >= 3 and Husband_education >= 3 and Wife_age <= 33 and Wife_age >= 32 and Children <= 3 | 3 | 0.011643 |
| Wife_age <= 37 and Children >= 4 and Husband_education >= 4 and Wife_age >= 33 and Husband_occupation <= 1 and Wife_working >= 1 | 3 | 0.015260 |
| Husband_occupation >= 2 and Children >= 3 and Husband_education >= 3 and Wife_age <= 29 and Husband_occupation <= 2 | 3 | 0.016083 |
|  | 1 | 0.510388 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|wife_religion|contraceptive_method
---|---|---|---|---
(41.5-inf)|(3.5-inf)|(7.5-inf)|all|3
(31.5-41.5]|(3.5-inf)|(7.5-inf)|all|2
(41.5-inf)|(2.5-3.5]|(7.5-inf)|all|1
(31.5-41.5]|(2.5-3.5]|(7.5-inf)|all|3
(31.5-41.5]|(-inf-2.5]|(7.5-inf)|all|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|all|3
(41.5-inf)|(3.5-inf)|(2.5-7.5]|all|2
(31.5-41.5]|(3.5-inf)|(2.5-7.5]|all|2
(41.5-inf)|(-inf-2.5]|(7.5-inf)|all|1
(41.5-inf)|(2.5-3.5]|(2.5-7.5]|all|1
(31.5-41.5]|(2.5-3.5]|(2.5-7.5]|all|1
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|all|3
(41.5-inf)|(3.5-inf)|(0.5-2.5]|all|1
(41.5-inf)|(-inf-2.5]|(2.5-7.5]|all|1
(31.5-41.5]|(-inf-2.5]|(2.5-7.5]|all|3
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|all|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|all|3
(31.5-41.5]|(3.5-inf)|(0.5-2.5]|all|1
(41.5-inf)|(2.5-3.5]|(0.5-2.5]|all|1
(31.5-41.5]|(2.5-3.5]|(0.5-2.5]|all|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|all|1
(31.5-41.5]|(3.5-inf)|(-inf-0.5]|all|1
(41.5-inf)|(-inf-2.5]|(0.5-2.5]|all|1
(41.5-inf)|(3.5-inf)|(-inf-0.5]|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-41.5]|(-inf-2.5]|(0.5-2.5]|all|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|all|1
(41.5-inf)|(2.5-3.5]|(-inf-0.5]|all|1
(31.5-41.5]|(2.5-3.5]|(-inf-0.5]|all|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|all|1
(41.5-inf)|(-inf-2.5]|(-inf-0.5]|all|1
(31.5-41.5]|(-inf-2.5]|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age <= 41) and (Wife_age >= 38) and (Husband_occupation <= 2) and (Wife_religion <= 0)|2 (10.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_religion >= 1) and (Husband_occupation <= 1) and (Wife_age >= 37) and (Wife_age <= 40) and (Wife_working >= 1) and (Children <= 5)|2 (13.0/1.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 33) and (Wife_working <= 0) and (Wife_religion >= 1)|2 (28.0/9.0)
(Wife_education >= 4) and (Standard-of-living >= 4) and (Children >= 4) and (Children <= 4) and (Wife_age >= 37) and (Husband_education >= 4) and (Wife_age <= 45)|2 (10.0/0.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 29) and (Husband_occupation >= 3) and (Wife_age <= 35) and (Children <= 4) and (Standard-of-living <= 3)|2 (11.0/2.0)
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 33) and (Standard-of-living >= 4) and (Wife_age <= 34)|2 (16.0/6.0)
(Husband_occupation <= 1) and (Children >= 2) and (Wife_age <= 29) and (Children <= 3) and (Wife_age >= 26) and (Standard-of-living <= 3)|2 (16.0/6.0)
(Wife_education >= 4) and (Children >= 6) and (Wife_age <= 45) and (Children <= 7) and (Wife_age >= 40)|2 (12.0/2.0)
(Standard-of-living >= 4) and (Wife_education >= 3) and (Children >= 2) and (Wife_age >= 45) and (Wife_age <= 46)|2 (17.0/7.0)
(Children >= 3) and (Husband_occupation >= 3) and (Wife_age <= 32) and (Wife_education >= 3) and (Wife_working >= 1) and (Wife_age >= 29)|3 (20.0/0.0)
(Children >= 3) and (Wife_age <= 29) and (Husband_occupation >= 2) and (Standard-of-living >= 2) and (Wife_age >= 28) and (Wife_education <= 2) and (Children <= 5)|3 (14.0/0.0)
(Children >= 3) and (Husband_occupation >= 3) and (Standard-of-living >= 3) and (Standard-of-living <= 3) and (Wife_age <= 30) and (Wife_age >= 24) and (Husband_education >= 3) and (Children <= 4)|3 (14.0/0.0)
(Children >= 3) and (Standard-of-living >= 2) and (Wife_education <= 2) and (Standard-of-living <= 3) and (Wife_age <= 29) and (Husband_education <= 2)|3 (10.0/1.0)
(Children >= 2) and (Wife_education >= 4) and (Wife_age <= 27) and (Husband_occupation >= 3)|3 (18.0/4.0)
(Children >= 3) and (Husband_education >= 3) and (Wife_age <= 33) and (Wife_age >= 32) and (Children <= 3)|3 (14.0/4.0)
(Wife_age <= 37) and (Children >= 4) and (Husband_education >= 4) and (Wife_age >= 33) and (Husband_occupation <= 1) and (Wife_working >= 1)|3 (18.0/4.0)
(Husband_occupation >= 2) and (Children >= 3) and (Husband_education >= 3) and (Wife_age <= 29) and (Husband_occupation <= 2)|3 (29.0/10.0)
|1 (1055.0/522.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.5|1 (85.0/2.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Media_exposure > 0.5|1 (41.0/3.0)
Wife_age > 41.5 AND Husband_education <= 2.5|1 (33.0/3.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children <= 9.5 AND Children > 1.5 AND Wife_working > 0.5 AND Wife_age > 45.5|1 (20.0/2.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 9.5|1 (15.0/3.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Wife_age <= 25.5 AND Husband_occupation <= 2.5 AND Wife_age > 20.5 AND Standard-of-living > 2.5|3 (20.0/9.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Wife_age <= 23.5|3 (81.0/41.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Media_exposure <= 0.5 AND Standard-of-living > 2.5 AND Wife_age > 30.5|1 (46.0/13.0)
Wife_education <= 2.5 AND Children <= 2.5 AND Wife_working > 0.5 AND Standard-of-living <= 2.5|1 (24.0/5.0)
Wife_education <= 3.5 AND Children > 2.5 AND Wife_age <= 32.5 AND Husband_occupation > 1.5 AND Husband_education > 1.5 AND Wife_age <= 24.5 AND Children <= 3.5|3 (18.0/6.0)
Wife_education <= 3.5 AND Children > 2.5 AND Wife_age <= 37.5 AND Husband_education > 1.5 AND Husband_occupation > 1.5 AND Wife_age <= 32.5 AND Wife_age > 24.5 AND Standard-of-living <= 2.5 AND Children <= 4.5 AND Husband_education > 2.5|3 (32.0/9.0)
Wife_education <= 3.5 AND Children > 2.5 AND Wife_age <= 37.5 AND Standard-of-living > 2.5 AND Media_exposure <= 0.5 AND Husband_occupation > 2.5|3 (101.0/32.0)
Wife_education <= 3.5 AND Husband_education > 1.5 AND Children <= 1.5|1 (41.0/16.0)
Wife_education <= 2.5 AND Husband_education > 1.5 AND Husband_occupation > 1.5 AND Children <= 7.5 AND Husband_education <= 2.5 AND Standard-of-living > 1.5|3 (22.0/7.0)
Wife_education <= 2.5 AND Children > 2.5 AND Standard-of-living <= 3.5 AND Children <= 3.5|1 (14.0/7.0)
Wife_education > 3.5 AND Wife_age > 44.5 AND Children > 1.5 AND Wife_working > 0.5 AND Wife_age <= 46.5|2 (13.0/5.0)
Wife_education > 3.5 AND Wife_age > 44.5 AND Children <= 1.5|1 (10.0)
Wife_education > 3.5 AND Husband_education <= 3.5|3 (26.0/9.0)
Husband_education <= 3.5 AND Husband_education > 1.5 AND Husband_occupation > 1.5 AND Children > 6.5|1 (18.0/6.0)
Wife_education <= 1.5|1 (24.0/8.0)
Wife_age > 37.5 AND Children <= 2.5 AND Wife_age > 39.5|1 (9.0/4.0)
Wife_age > 37.5 AND Wife_age <= 47.5 AND Wife_education > 3.5 AND Children > 3.5|2 (67.0/23.0)
Wife_age > 39.5 AND Husband_occupation > 1.5 AND Wife_age > 40.5 AND Standard-of-living > 3.5|1 (20.0/8.0)
Wife_age > 40.5 AND Wife_age > 42.5 AND Wife_age > 44.5|1 (15.0/8.0)
Wife_age > 40.5|2 (19.0/9.0)
Wife_age > 38.5 AND Husband_occupation > 2.5|1 (10.0/4.0)
Husband_education > 3.5 AND Children > 2.5 AND Standard-of-living > 1.5 AND Media_exposure <= 0.5 AND Wife_education > 2.5 AND Wife_age > 35.5 AND Wife_education > 3.5 AND Husband_occupation > 1.5 AND Wife_religion <= 0.5|2 (13.0/6.0)
Husband_education > 3.5 AND Wife_education > 2.5 AND Children > 2.5 AND Standard-of-living > 1.5 AND Wife_age > 32.5 AND Standard-of-living > 2.5 AND Wife_education > 3.5 AND Wife_age > 36.5|2 (19.0/8.0)
Wife_age > 36.5 AND Standard-of-living > 3.5 AND Wife_education <= 3.5|3 (11.0/5.0)
Wife_age > 36.5 AND Standard-of-living <= 3.5 AND Husband_occupation > 1.5|1 (13.0/6.0)
Media_exposure > 0.5 AND Husband_occupation <= 2.5|2 (8.0/5.0)
Husband_education > 2.5 AND Standard-of-living > 1.5 AND Children > 2.5 AND Wife_age > 33.5 AND Husband_occupation <= 2.5 AND Wife_working > 0.5 AND Children > 3.5 AND Husband_occupation <= 1.5|3 (19.0/6.0)
Wife_age > 33.5 AND Children > 2.5 AND Wife_education > 2.5|2 (47.0/17.0)
Wife_age > 33.5 AND Standard-of-living <= 3.5|1 (21.0/8.0)
Wife_age <= 35.5 AND Children > 3.5 AND Wife_age <= 29.5 AND Husband_occupation > 1.5|3 (20.0/7.0)
Wife_age > 35.5|1 (13.0/7.0)
Standard-of-living <= 1.5|3 (12.0/6.0)
Wife_education > 2.5 AND Wife_age > 20.5 AND Children > 1.5 AND Wife_age <= 24.5 AND Husband_occupation > 2.5|3 (11.0/4.0)
Wife_age > 20.5 AND Wife_age <= 24.5 AND Children <= 1.5 AND Husband_occupation <= 1.5|2 (15.0/5.0)
Wife_age <= 22.5|3 (19.0/8.0)
Wife_age <= 24.5 AND Husband_occupation <= 2.5|1 (13.0/6.0)
Children > 1.5 AND Wife_education > 2.5 AND Wife_age <= 25.5|3 (15.0/6.0)
Wife_age > 24.5 AND Wife_age > 25.5 AND Children <= 1.5 AND Husband_occupation <= 1.5|1 (19.0/9.0)
Wife_age > 24.5 AND Wife_age > 25.5 AND Wife_education > 2.5 AND Wife_age <= 33.5 AND Wife_working <= 0.5|3 (56.0/28.0)
Wife_age > 24.5 AND Wife_age > 25.5 AND Wife_working > 0.5 AND Wife_education > 2.5 AND Husband_education > 3.5 AND Children > 2.5 AND Children <= 4.5 AND Wife_age <= 32.5 AND Standard-of-living > 3.5|3 (24.0/14.0)
Wife_age > 24.5 AND Wife_age > 25.5 AND Wife_working > 0.5 AND Wife_education > 2.5 AND Children > 2.5 AND Children <= 4.5|2 (23.0/7.0)
Wife_age > 24.5 AND Wife_age > 25.5 AND Wife_age > 30.5 AND Husband_occupation <= 2.5|3 (26.0/14.0)
Wife_age > 24.5 AND Wife_age <= 30.5 AND Wife_age <= 25.5|1 (10.0/5.0)
Wife_age > 25.0 AND Wife_age <= 30.5 AND Wife_religion <= 0.5|2 (10.0/4.0)
Wife_age > 25.0 AND Wife_age <= 30.5 AND Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Wife_education <= 2.5|1 (9.0/5.0)
Wife_age > 25.0 AND Wife_age <= 30.5 AND Husband_occupation > 1.5 AND Wife_education <= 3.5|2 (9.0/4.0)
Wife_age > 25.0 AND Children <= 3.5 AND Wife_education <= 3.5|2 (10.0/4.0)
Wife_age > 25.0 AND Wife_age <= 29.5|3 (17.0/8.0)
Wife_age > 27.0|1 (11.0/4.0)
|2 (8.0/2.0)


## J48 Decision Tree

* Children <= 0.0: 1 (85.0/2.0)
* Children > 0.0
	* Wife_education <= 3.0
		* Wife_age <= 37.0
			* Children <= 2.0
				* Wife_age <= 22.0: 3 (77.0/38.0)
				* Wife_age > 22.0: 1 (156.0/69.0)
			* Children > 2.0: 3 (310.0/138.0)
		* Wife_age > 37.0: 1 (209.0/57.0)
	* Wife_education > 3.0
		* Children <= 2.0
			* Wife_age <= 32.0
				* Husband_occupation <= 1.0
					* Wife_age <= 23.0: 2 (15.0/8.0)
					* Wife_age > 23.0
						* Wife_age <= 25.0: 3 (18.0/8.0)
						* Wife_age > 25.0
							* Children <= 1.0: 1 (18.0/8.0)
							* Children > 1.0: 2 (26.0/12.0)
				* Husband_occupation > 1.0: 3 (79.0/37.0)
			* Wife_age > 32.0: 1 (62.0/29.0)
		* Children > 2.0
			* Wife_age <= 28.0
				* Husband_occupation <= 2.0: 1 (15.0/7.0)
				* Husband_occupation > 2.0: 3 (10.0/2.0)
			* Wife_age > 28.0
				* Standard-of-living <= 3.0: 2 (57.0/28.0)
				* Standard-of-living > 3.0
					* Wife_age <= 32.0: 3 (24.0/9.0)
					* Wife_age > 32.0: 2 (164.0/73.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(83.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/114.0)
			* Children >= 2.5: 3(172.0/138.0)
		* Wife_age >= 37.5: 1(152.0/57.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 43.5: 3(88.0/117.0)
			* Wife_age >= 43.5: 1(12.0/1.0)
		* Children >= 2.5: 2(130.0/140.0)


