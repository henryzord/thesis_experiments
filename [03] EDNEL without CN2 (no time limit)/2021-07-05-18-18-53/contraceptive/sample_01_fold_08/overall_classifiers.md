# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.426415 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.099618 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age >= 28.5 | 2 | 0.062020 |
| Children > 0 and Wife_education > 3 and Husband_education > 3 and Children <= 2 and Wife_age <= 39 | 3 | 0.038224 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 39.5 and Husband_occupation < 1.5 and Wife_age < 29.5 | 2 | 0.011389 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Husband_education <= 3.5 and Children > 0.5 and Children <= 2.5 | 3 | 0.015663 |
| Children > 0 and Wife_education > 3 and Husband_education <= 3 | 3 | 0.010898 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Husband_education > 3.5 and Children > 2.5 | 3 | 0.008411 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 41 and Husband_occupation > 1 and Media_exposure <= 0 and Children <= 2 and Wife_age <= 30 and Wife_working > 0 and Husband_occupation <= 2 | 3 | 0.013295 |
| Wife_age > 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Husband_education <= 3.5 and Children > 2.5 | 2 | 0.004644 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 41 and Husband_occupation <= 1 and Children > 1 and Husband_education <= 3 | 2 | 0.002704 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 41 and Husband_occupation <= 1 and Children > 1 and Husband_education > 3 | 3 | 0.011236 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 41 and Husband_occupation > 1 and Media_exposure <= 0 and Children > 2 and Husband_education > 2 and Wife_religion > 0 and Wife_age > 33 and Wife_education <= 2 and Wife_working > 0 | 3 | 0.010345 |
| Wife_age <= 31.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Husband_education <= 1.5 and Children > 0.5 and Children <= 2.5 | 2 | 0.001947 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Husband_education <= 1.5 and Children > 0.5 and Children <= 2.5 | 2 | 0.001947 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education <= 2.5 and Husband_education > 3.5 and Children > 2.5 | 3 | 0.012275 |
| Wife_age > 31.5 and Wife_age <= 41.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Husband_education > 3.5 and Children > 2.5 | 3 | 0.010123 |
| Children > 0 and Wife_education <= 3 and Wife_age <= 41 and Husband_occupation > 1 and Media_exposure <= 0 and Children > 2 and Husband_education <= 2 | 3 | 0.010917 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0 and Husband_education > 2 | 1 | 0.085439 |
| Wife_education <= 3 and Wife_age > 37 and Media_exposure > 0 and Husband_occupation <= 2 | 1 | 0.024390 |
| Wife_education <= 3 and Wife_age > 37 and Children <= 1 | 1 | 0.019431 |
| Wife_education <= 3 and Wife_age > 41 and Standard-of-living > 1 and Wife_working > 0 and Children <= 3 | 1 | 0.013415 |
| Wife_education <= 3 and Wife_age > 41 and Wife_religion > 0 and Standard-of-living <= 2 and Wife_age > 44 | 1 | 0.019431 |
| Wife_education <= 3 and Wife_age > 41 and Wife_working > 0 and Wife_education <= 1 and Children <= 7 | 1 | 0.010029 |
| Wife_education <= 3 and Husband_education <= 1 and Standard-of-living <= 2 | 1 | 0.008145 |
| Wife_education <= 3 and Wife_age > 41 and Wife_working > 0 and Wife_age <= 47 and Wife_age <= 45 and Children <= 8 and Standard-of-living > 3 | 2 | 0.005242 |
| Wife_education <= 3 and Wife_age > 37 and Children <= 9 and Wife_working <= 0 and Standard-of-living > 3 | 3 | 0.010681 |
| Wife_education <= 3 and Wife_age > 37 and Children <= 9 and Wife_age <= 47 and Media_exposure <= 0 and Wife_education > 1 and Children > 3 and Wife_age <= 42 and Husband_occupation <= 2 | 1 | 0.006073 |
| Wife_education <= 3 and Wife_age > 37 and Wife_age <= 42 and Standard-of-living <= 3 and Husband_education <= 3 and Standard-of-living <= 2 | 1 | 0.011126 |
| Wife_education <= 3 and Wife_age > 41 and Wife_age <= 47 and Wife_education > 1 and Wife_age > 43 | 2 | 0.003488 |
| Wife_education <= 3 and Wife_age > 41 and Wife_age > 47 | 1 | 0.012938 |
| Wife_education <= 3 and Wife_age > 41 and Wife_education <= 1 | 1 | 0.009033 |
| Wife_education <= 3 and Husband_occupation > 1 and Children > 2 and Children > 7 and Wife_age <= 37 | 3 | 0.004247 |
| Wife_education <= 3 and Standard-of-living <= 1 and Wife_education <= 2 and Children <= 3 and Wife_age <= 25 and Husband_education <= 2 | 1 | 0.007296 |
| Wife_education <= 3 and Husband_occupation > 1 and Children > 2 and Children <= 7 and Wife_age <= 32 and Wife_age > 23 and Standard-of-living <= 2 and Wife_education > 2 and Standard-of-living > 1 | 3 | 0.007597 |
| Wife_education <= 3 and Children <= 2 and Wife_age <= 25 and Husband_occupation <= 2 and Standard-of-living <= 3 and Husband_education <= 3 | 3 | 0.010582 |
| Wife_education <= 3 and Children <= 2 and Wife_age > 30 and Children > 1 and Wife_age > 33 | 1 | 0.008533 |
| Wife_education <= 3 and Standard-of-living <= 1 and Children <= 1 and Wife_education <= 2 | 1 | 0.009467 |
| Wife_education <= 3 and Wife_age > 37 and Wife_age <= 41 and Children > 5 | 1 | 0.005658 |
| Wife_education <= 3 and Husband_occupation > 1 and Children > 2 and Wife_age <= 40 and Wife_age <= 32 and Wife_age > 23 and Standard-of-living <= 2 and Wife_education <= 2 and Wife_age <= 29 | 3 | 0.009317 |
| Wife_education <= 3 and Children > 2 and Wife_age > 40 | 1 | 0.016840 |
| Wife_education <= 3 and Children > 2 and Husband_occupation > 1 and Wife_age <= 32 and Wife_age <= 23 | 1 | 0.005014 |
| Wife_education <= 3 and Children > 2 and Husband_occupation > 1 and Wife_age <= 32 and Standard-of-living <= 2 and Wife_education > 2 | 3 | 0.009953 |
| Wife_education <= 2 and Children > 2 and Wife_age > 35 and Husband_occupation <= 2 | 3 | 0.009354 |
| Children > 2 and Wife_education <= 2 and Standard-of-living > 2 and Standard-of-living <= 3 and Wife_age <= 32 and Husband_education > 2 | 3 | 0.026582 |
| Children <= 2 and Wife_age > 41 | 1 | 0.015420 |
| Wife_education <= 3 and Children <= 2 and Wife_age > 30 and Wife_education > 2 | 1 | 0.007962 |
| Wife_education <= 3 and Standard-of-living <= 1 and Wife_age > 24 | 1 | 0.016750 |
| Wife_education <= 3 and Children <= 2 and Wife_age <= 25 and Husband_education <= 2 and Wife_age <= 21 | 3 | 0.008967 |
| Wife_education <= 2 and Children <= 2 and Wife_age <= 23 and Children <= 1 | 1 | 0.011536 |
| Wife_age > 34 and Children <= 2 and Children > 1 | 3 | 0.011743 |
| Wife_age > 34 and Children <= 2 | 1 | 0.010563 |
| Wife_age > 34 and Wife_education <= 2 and Children > 5 | 3 | 0.010117 |
| Wife_age > 34 and Wife_age <= 42 and Standard-of-living > 2 and Wife_education > 3 and Standard-of-living > 3 and Wife_age > 35 and Husband_occupation <= 2 and Wife_age <= 41 and Wife_age > 36 and Wife_religion > 0 and Children > 3 | 2 | 0.015873 |
| Wife_age > 34 and Wife_age <= 47 and Husband_education > 3 and Wife_education > 3 and Wife_age <= 39 and Husband_occupation > 1 and Wife_religion <= 0 | 2 | 0.009529 |
| Wife_age > 34 and Wife_age <= 47 and Wife_education > 2 and Husband_occupation <= 1 and Wife_age > 37 and Wife_religion > 0 and Wife_age <= 42 | 2 | 0.014269 |
| Wife_education <= 2 and Children <= 1 | 1 | 0.013997 |
| Husband_occupation > 1 and Wife_age <= 30 and Children > 2 and Husband_education > 2 and Wife_working > 0 and Husband_education <= 3 | 3 | 0.032076 |
| Wife_age > 34 and Wife_age > 47 | 1 | 0.005644 |
| Wife_age > 34 and Wife_education > 2 and Wife_working <= 0 and Wife_religion > 0 and Wife_age > 36 | 2 | 0.009779 |
| Wife_age > 34 and Wife_working <= 0 and Husband_occupation > 1 | 2 | 0.007788 |
| Wife_education <= 2 and Wife_age > 23 and Wife_working <= 0 | 1 | 0.015069 |
| Husband_occupation > 1 and Children <= 2 and Standard-of-living <= 3 and Wife_religion > 0 and Wife_age > 20 and Wife_working > 0 and Wife_education > 2 and Husband_occupation > 2 and Wife_age <= 22 | 3 | 0.022274 |
| Husband_occupation > 1 and Wife_age > 32 and Wife_education <= 2 | 3 | 0.019378 |
| Wife_education <= 2 and Wife_age <= 30 and Wife_age > 23 and Husband_education > 3 | 3 | 0.013033 |
| Wife_education <= 2 and Wife_age <= 25 | 1 | 0.006790 |
| Wife_education <= 2 and Wife_age <= 30 | 3 | 0.043172 |
| Wife_age > 34 and Wife_working > 0 and Wife_age <= 39 and Standard-of-living <= 3 | 2 | 0.014435 |
| Husband_occupation > 1 and Wife_education <= 2 | 1 | 0.024368 |
| Husband_occupation > 1 and Wife_age <= 28 and Children > 1 and Wife_age > 24 and Wife_education > 3 and Children <= 2 | 3 | 0.026178 |
| Children > 2 and Children > 5 and Standard-of-living > 3 | 2 | 0.027100 |
| Children > 2 and Children <= 5 and Wife_age > 30 and Husband_education <= 3 | 3 | 0.019150 |
| Children > 2 and Children <= 5 and Husband_occupation > 2 and Wife_age > 27 and Wife_education <= 3 | 3 | 0.022700 |
| Children > 2 and Children <= 5 and Wife_age <= 28 and Husband_occupation > 1 and Wife_education <= 3 | 3 | 0.016323 |
| Children > 2 and Children <= 5 and Wife_age > 30 and Standard-of-living > 3 and Wife_education > 3 and Wife_age > 32 and Wife_age <= 39 and Wife_age > 35 | 2 | 0.011971 |
| Standard-of-living > 3 and Husband_education <= 3 | 1 | 0.010409 |
| Standard-of-living > 3 and Wife_age <= 22 and Wife_education > 3 | 3 | 0.012299 |
| Standard-of-living > 3 and Wife_age > 22 and Wife_education <= 3 and Husband_occupation <= 1 | 3 | 0.007935 |
| Wife_education <= 3 and Children <= 2 and Standard-of-living <= 3 and Wife_age <= 25 and Children <= 1 | 1 | 0.021019 |
| Wife_age <= 28 and Husband_occupation > 1 and Husband_education > 3 and Children <= 2 and Wife_age <= 22 | 3 | 0.018286 |
| Children > 2 and Children > 5 | 1 | 0.009879 |
| Children > 2 and Wife_age > 28 and Husband_occupation > 1 and Wife_age <= 35 and Wife_working > 0 and Husband_occupation <= 2 | 2 | 0.023034 |
| Children > 3 and Wife_age > 29 and Wife_age > 32 and Wife_religion <= 0 | 3 | 0.017065 |
| Wife_age <= 43 and Wife_education <= 3 and Children <= 2 and Standard-of-living > 2 and Wife_age > 25 | 3 | 0.007990 |
| Wife_age > 43 | 2 | 0.029825 |
| Wife_education <= 3 and Children <= 2 and Standard-of-living > 2 | 3 | 0.010686 |
| Wife_age > 22 and Children <= 1 and Wife_age > 24 and Standard-of-living <= 3 and Wife_working > 0 | 1 | 0.020627 |
| Wife_age <= 37 and Wife_age > 22 and Wife_age > 34 | 2 | 0.008232 |
| Children > 1 and Wife_age > 23 and Children > 4 | 1 | 0.010130 |
| Children > 3 and Husband_occupation <= 1 | 3 | 0.075078 |
| Children > 3 | 2 | 0.073068 |
| Wife_age > 29 and Standard-of-living <= 3 and Wife_working <= 0 | 1 | 0.017699 |
| Standard-of-living <= 2 and Wife_age <= 26 | 3 | 0.013196 |
| Standard-of-living > 2 and Wife_age > 31 and Wife_working > 0 and Children > 2 | 3 | 0.088052 |
| Wife_age <= 32 and Standard-of-living <= 3 and Wife_age > 25 and Husband_occupation <= 1 | 2 | 0.037618 |
| Wife_age <= 32 and Wife_religion <= 0 and Wife_age > 27 | 1 | 0.011834 |
| Wife_age > 29 and Wife_age <= 32 | 1 | 0.019268 |
| Wife_age <= 31 and Wife_age <= 27 and Wife_religion > 0 and Children > 1 and Husband_occupation > 1 | 3 | 0.016543 |
| Wife_age <= 31 and Wife_age > 23 and Husband_occupation <= 2 and Wife_age <= 25 | 3 | 0.021515 |
| Wife_age <= 31 and Wife_age <= 27 and Wife_age <= 25 | 1 | 0.094222 |
| Wife_age > 31 | 1 | 0.059371 |
| Wife_age <= 27 and Wife_working > 0 | 1 | 0.014611 |
| Wife_age > 27 | 2 | 0.306220 |
|  | 2 | 0.448819 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 37 and Wife_age <= 41 | 2 | 0.027195 |
| Children >= 2 and Wife_age <= 26 and Husband_occupation >= 2 and Wife_education >= 4 | 3 | 0.019889 |
| Children >= 3 and Husband_occupation >= 2 and Husband_education >= 3 and Wife_age <= 29 | 3 | 0.048902 |
| Wife_age <= 37 and Wife_education <= 2 and Children >= 6 and Wife_working >= 1 and Husband_education >= 2 | 3 | 0.014978 |
|  | 1 | 0.477196 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|husband_education|children|contraceptive_method
---|---|---|---|---
(41.5-inf)|(3.5-inf)|(3.5-inf)|(2.5-inf)|2
(31.5-41.5]|(3.5-inf)|(3.5-inf)|(2.5-inf)|2
(-inf-31.5]|(3.5-inf)|(3.5-inf)|(2.5-inf)|3
(41.5-inf)|(2.5-3.5]|(3.5-inf)|(2.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(3.5-inf)|(2.5-inf)|3
(31.5-41.5]|(2.5-3.5]|(3.5-inf)|(2.5-inf)|3
(-inf-31.5]|(3.5-inf)|(1.5-3.5]|(2.5-inf)|2
(41.5-inf)|(3.5-inf)|(1.5-3.5]|(2.5-inf)|2
(31.5-41.5]|(3.5-inf)|(1.5-3.5]|(2.5-inf)|3
(41.5-inf)|(-inf-2.5]|(3.5-inf)|(2.5-inf)|1
(31.5-41.5]|(-inf-2.5]|(3.5-inf)|(2.5-inf)|3
(-inf-31.5]|(-inf-2.5]|(3.5-inf)|(2.5-inf)|3
(41.5-inf)|(2.5-3.5]|(1.5-3.5]|(2.5-inf)|2
(31.5-41.5]|(2.5-3.5]|(1.5-3.5]|(2.5-inf)|1
(41.5-inf)|(3.5-inf)|(3.5-inf)|(0.5-2.5]|1
(31.5-41.5]|(3.5-inf)|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(1.5-3.5]|(2.5-inf)|3
(-inf-31.5]|(3.5-inf)|(3.5-inf)|(0.5-2.5]|3
(-inf-31.5]|(3.5-inf)|(-inf-1.5]|(2.5-inf)|1
(31.5-41.5]|(2.5-3.5]|(3.5-inf)|(0.5-2.5]|1
(41.5-inf)|(-inf-2.5]|(1.5-3.5]|(2.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(3.5-inf)|(0.5-2.5]|1
(41.5-inf)|(2.5-3.5]|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(1.5-3.5]|(2.5-inf)|3
(31.5-41.5]|(-inf-2.5]|(1.5-3.5]|(2.5-inf)|1
(41.5-inf)|(2.5-3.5]|(-inf-1.5]|(2.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(-inf-1.5]|(2.5-inf)|1
(31.5-41.5]|(3.5-inf)|(1.5-3.5]|(0.5-2.5]|3
(31.5-41.5]|(-inf-2.5]|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(1.5-3.5]|(0.5-2.5]|3
(41.5-inf)|(-inf-2.5]|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-1.5]|(2.5-inf)|1
(41.5-inf)|(3.5-inf)|(3.5-inf)|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(1.5-3.5]|(0.5-2.5]|1
(31.5-41.5]|(2.5-3.5]|(1.5-3.5]|(0.5-2.5]|1
(31.5-41.5]|(3.5-inf)|(3.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(-inf-1.5]|(2.5-inf)|1
(-inf-31.5]|(3.5-inf)|(3.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(-inf-1.5]|(2.5-inf)|1
(-inf-31.5]|(2.5-3.5]|(1.5-3.5]|(0.5-2.5]|3
(31.5-41.5]|(2.5-3.5]|(3.5-inf)|(-inf-0.5]|1
(41.5-inf)|(2.5-3.5]|(3.5-inf)|(-inf-0.5]|1
(41.5-inf)|(-inf-2.5]|(1.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(3.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(1.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(1.5-3.5]|(0.5-2.5]|1
(31.5-41.5]|(3.5-inf)|(1.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(3.5-inf)|(1.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-1.5]|(0.5-2.5]|2
(-inf-31.5]|(-inf-2.5]|(3.5-inf)|(-inf-0.5]|1
(31.5-41.5]|(2.5-3.5]|(-inf-1.5]|(0.5-2.5]|1
(31.5-41.5]|(-inf-2.5]|(-inf-1.5]|(0.5-2.5]|1
(41.5-inf)|(-inf-2.5]|(-inf-1.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(1.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-1.5]|(0.5-2.5]|2
(41.5-inf)|(-inf-2.5]|(1.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(1.5-3.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(1.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-1.5]|(-inf-0.5]|1
(31.5-41.5]|(-inf-2.5]|(-inf-1.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 37) and (Wife_age <= 41)|2 (65.0/22.0)
(Children >= 2) and (Wife_age <= 26) and (Husband_occupation >= 2) and (Wife_education >= 4)|3 (24.0/4.0)
(Children >= 3) and (Husband_occupation >= 2) and (Husband_education >= 3) and (Wife_age <= 29)|3 (86.0/26.0)
(Wife_age <= 37) and (Wife_education <= 2) and (Children >= 6) and (Wife_working >= 1) and (Husband_education >= 2)|3 (25.0/7.0)
|1 (1125.0/589.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0 AND Husband_education > 2|1 (71.0)
Wife_education <= 3 AND Wife_age > 37 AND Media_exposure > 0 AND Husband_occupation <= 2|1 (19.0)
Wife_education <= 3 AND Wife_age > 37 AND Children <= 1|1 (17.0/1.0)
Wife_education <= 3 AND Wife_age > 41 AND Standard-of-living > 1 AND Wife_working > 0 AND Children <= 3|1 (18.0/4.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_religion > 0 AND Standard-of-living <= 2 AND Wife_age > 44|1 (16.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_working > 0 AND Wife_education <= 1 AND Children <= 7|1 (11.0/1.0)
Wife_education <= 3 AND Husband_education <= 1 AND Standard-of-living <= 2|1 (13.0/4.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_working > 0 AND Wife_age <= 47 AND Wife_age <= 45 AND Children <= 8 AND Standard-of-living > 3|2 (12.0/6.0)
Wife_education <= 3 AND Wife_age > 37 AND Children <= 9 AND Wife_working <= 0 AND Standard-of-living > 3|3 (16.0/5.0)
Wife_education <= 3 AND Wife_age > 37 AND Children <= 9 AND Wife_age <= 47 AND Media_exposure <= 0 AND Wife_education > 1 AND Children > 3 AND Wife_age <= 42 AND Husband_occupation <= 2|1 (17.0/8.0)
Wife_education <= 3 AND Wife_age > 37 AND Wife_age <= 42 AND Standard-of-living <= 3 AND Husband_education <= 3 AND Standard-of-living <= 2|1 (10.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_age <= 47 AND Wife_education > 1 AND Wife_age > 43|2 (17.0/9.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_age > 47|1 (14.0/2.0)
Wife_education <= 3 AND Wife_age > 41 AND Wife_education <= 1|1 (12.0/3.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Children > 2 AND Children > 7 AND Wife_age <= 37|3 (13.0/7.0)
Wife_education <= 3 AND Standard-of-living <= 1 AND Wife_education <= 2 AND Children <= 3 AND Wife_age <= 25 AND Husband_education <= 2|1 (11.0/3.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Children > 2 AND Children <= 7 AND Wife_age <= 32 AND Wife_age > 23 AND Standard-of-living <= 2 AND Wife_education > 2 AND Standard-of-living > 1|3 (13.0/5.0)
Wife_education <= 3 AND Children <= 2 AND Wife_age <= 25 AND Husband_occupation <= 2 AND Standard-of-living <= 3 AND Husband_education <= 3|3 (20.0/9.0)
Wife_education <= 3 AND Children <= 2 AND Wife_age > 30 AND Children > 1 AND Wife_age > 33|1 (15.0/6.0)
Wife_education <= 3 AND Standard-of-living <= 1 AND Children <= 1 AND Wife_education <= 2|1 (10.0/2.0)
Wife_education <= 3 AND Wife_age > 37 AND Wife_age <= 41 AND Children > 5|1 (11.0/3.0)
Wife_education <= 3 AND Husband_occupation > 1 AND Children > 2 AND Wife_age <= 40 AND Wife_age <= 32 AND Wife_age > 23 AND Standard-of-living <= 2 AND Wife_education <= 2 AND Wife_age <= 29|3 (14.0/5.0)
Wife_education <= 3 AND Children > 2 AND Wife_age > 40|1 (13.0/4.0)
Wife_education <= 3 AND Children > 2 AND Husband_occupation > 1 AND Wife_age <= 32 AND Wife_age <= 23|1 (12.0/5.0)
Wife_education <= 3 AND Children > 2 AND Husband_occupation > 1 AND Wife_age <= 32 AND Standard-of-living <= 2 AND Wife_education > 2|3 (11.0/1.0)
Wife_education <= 2 AND Children > 2 AND Wife_age > 35 AND Husband_occupation <= 2|3 (14.0/6.0)
Children > 2 AND Wife_education <= 2 AND Standard-of-living > 2 AND Standard-of-living <= 3 AND Wife_age <= 32 AND Husband_education > 2|3 (17.0/1.0)
Children <= 2 AND Wife_age > 41|1 (16.0/2.0)
Wife_education <= 3 AND Children <= 2 AND Wife_age > 30 AND Wife_education > 2|1 (13.0/3.0)
Wife_education <= 3 AND Standard-of-living <= 1 AND Wife_age > 24|1 (19.0/6.0)
Wife_education <= 3 AND Children <= 2 AND Wife_age <= 25 AND Husband_education <= 2 AND Wife_age <= 21|3 (11.0/3.0)
Wife_education <= 2 AND Children <= 2 AND Wife_age <= 23 AND Children <= 1|1 (13.0/5.0)
Wife_age > 34 AND Children <= 2 AND Children > 1|3 (19.0/10.0)
Wife_age > 34 AND Children <= 2|1 (11.0/4.0)
Wife_age > 34 AND Wife_education <= 2 AND Children > 5|3 (11.0/2.0)
Wife_age > 34 AND Wife_age <= 42 AND Standard-of-living > 2 AND Wife_education > 3 AND Standard-of-living > 3 AND Wife_age > 35 AND Husband_occupation <= 2 AND Wife_age <= 41 AND Wife_age > 36 AND Wife_religion > 0 AND Children > 3|2 (21.0/7.0)
Wife_age > 34 AND Wife_age <= 47 AND Husband_education > 3 AND Wife_education > 3 AND Wife_age <= 39 AND Husband_occupation > 1 AND Wife_religion <= 0|2 (18.0/8.0)
Wife_age > 34 AND Wife_age <= 47 AND Wife_education > 2 AND Husband_occupation <= 1 AND Wife_age > 37 AND Wife_religion > 0 AND Wife_age <= 42|2 (18.0/5.0)
Wife_education <= 2 AND Children <= 1|1 (22.0/6.0)
Husband_occupation > 1 AND Wife_age <= 30 AND Children > 2 AND Husband_education > 2 AND Wife_working > 0 AND Husband_education <= 3|3 (18.0/2.0)
Wife_age > 34 AND Wife_age > 47|1 (17.0/9.0)
Wife_age > 34 AND Wife_education > 2 AND Wife_working <= 0 AND Wife_religion > 0 AND Wife_age > 36|2 (13.0/8.0)
Wife_age > 34 AND Wife_working <= 0 AND Husband_occupation > 1|2 (13.0/5.0)
Wife_education <= 2 AND Wife_age > 23 AND Wife_working <= 0|1 (19.0/8.0)
Husband_occupation > 1 AND Children <= 2 AND Standard-of-living <= 3 AND Wife_religion > 0 AND Wife_age > 20 AND Wife_working > 0 AND Wife_education > 2 AND Husband_occupation > 2 AND Wife_age <= 22|3 (15.0/3.0)
Husband_occupation > 1 AND Wife_age > 32 AND Wife_education <= 2|3 (18.0/5.0)
Wife_education <= 2 AND Wife_age <= 30 AND Wife_age > 23 AND Husband_education > 3|3 (17.0/9.0)
Wife_education <= 2 AND Wife_age <= 25|1 (16.0/7.0)
Wife_education <= 2 AND Wife_age <= 30|3 (15.0/9.0)
Wife_age > 34 AND Wife_working > 0 AND Wife_age <= 39 AND Standard-of-living <= 3|2 (18.0/8.0)
Husband_occupation > 1 AND Wife_education <= 2|1 (15.0/7.0)
Husband_occupation > 1 AND Wife_age <= 28 AND Children > 1 AND Wife_age > 24 AND Wife_education > 3 AND Children <= 2|3 (10.0)
Children > 2 AND Children > 5 AND Standard-of-living > 3|2 (19.0/8.0)
Children > 2 AND Children <= 5 AND Wife_age > 30 AND Husband_education <= 3|3 (14.0/6.0)
Children > 2 AND Children <= 5 AND Husband_occupation > 2 AND Wife_age > 27 AND Wife_education <= 3|3 (15.0/4.0)
Children > 2 AND Children <= 5 AND Wife_age <= 28 AND Husband_occupation > 1 AND Wife_education <= 3|3 (14.0/4.0)
Children > 2 AND Children <= 5 AND Wife_age > 30 AND Standard-of-living > 3 AND Wife_education > 3 AND Wife_age > 32 AND Wife_age <= 39 AND Wife_age > 35|2 (19.0/8.0)
Standard-of-living > 3 AND Husband_education <= 3|1 (16.0/9.0)
Standard-of-living > 3 AND Wife_age <= 22 AND Wife_education > 3|3 (11.0/5.0)
Standard-of-living > 3 AND Wife_age > 22 AND Wife_education <= 3 AND Husband_occupation <= 1|3 (14.0/8.0)
Wife_education <= 3 AND Children <= 2 AND Standard-of-living <= 3 AND Wife_age <= 25 AND Children <= 1|1 (18.0/8.0)
Wife_age <= 28 AND Husband_occupation > 1 AND Husband_education > 3 AND Children <= 2 AND Wife_age <= 22|3 (18.0/8.0)
Children > 2 AND Children > 5|1 (11.0/6.0)
Children > 2 AND Wife_age > 28 AND Husband_occupation > 1 AND Wife_age <= 35 AND Wife_working > 0 AND Husband_occupation <= 2|2 (10.0/2.0)
Children > 3 AND Wife_age > 29 AND Wife_age > 32 AND Wife_religion <= 0|3 (12.0/6.0)
Wife_age <= 43 AND Wife_education <= 3 AND Children <= 2 AND Standard-of-living > 2 AND Wife_age > 25|3 (19.0/11.0)
Wife_age > 43|2 (16.0/8.0)
Wife_education <= 3 AND Children <= 2 AND Standard-of-living > 2|3 (12.0/4.0)
Wife_age > 22 AND Children <= 1 AND Wife_age > 24 AND Standard-of-living <= 3 AND Wife_working > 0|1 (13.0/4.0)
Wife_age <= 37 AND Wife_age > 22 AND Wife_age > 34|2 (12.0/6.0)
Children > 1 AND Wife_age > 23 AND Children > 4|1 (16.0/9.0)
Children > 3 AND Husband_occupation <= 1|3 (12.0/7.0)
Children > 3|2 (11.0/5.0)
Wife_age > 29 AND Standard-of-living <= 3 AND Wife_working <= 0|1 (10.0/5.0)
Standard-of-living <= 2 AND Wife_age <= 26|3 (13.0/7.0)
Standard-of-living > 2 AND Wife_age > 31 AND Wife_working > 0 AND Children > 2|3 (15.0/8.0)
Wife_age <= 32 AND Standard-of-living <= 3 AND Wife_age > 25 AND Husband_occupation <= 1|2 (16.0/6.0)
Wife_age <= 32 AND Wife_religion <= 0 AND Wife_age > 27|1 (16.0/10.0)
Wife_age > 29 AND Wife_age <= 32|1 (18.0/11.0)
Wife_age <= 31 AND Wife_age <= 27 AND Wife_religion > 0 AND Children > 1 AND Husband_occupation > 1|3 (14.0/5.0)
Wife_age <= 31 AND Wife_age > 23 AND Husband_occupation <= 2 AND Wife_age <= 25|3 (21.0/11.0)
Wife_age <= 31 AND Wife_age <= 27 AND Wife_age <= 25|1 (20.0/11.0)
Wife_age > 31|1 (13.0/7.0)
Wife_age <= 27 AND Wife_working > 0|1 (12.0/7.0)
Wife_age > 27|2 (12.0/6.0)
|2 (10.0/6.0)


## J48 Decision Tree

* Children <= 0: 1 (68.0/1.0)
* Children > 0
	* Wife_education <= 3
		* Wife_age <= 41
			* Husband_occupation <= 1
				* Children <= 1: 1 (8.0/3.0)
				* Children > 1
					* Husband_education <= 3: 2 (12.0/7.0)
					* Husband_education > 3: 3 (44.0/25.0)
			* Husband_occupation > 1
				* Media_exposure <= 0
					* Children <= 2
						* Wife_age <= 30
							* Wife_working <= 0: 1 (23.0/13.0)
							* Wife_working > 0
								* Husband_occupation <= 2: 3 (43.0/22.0)
								* Husband_occupation > 2: 1 (86.0/46.0)
						* Wife_age > 30: 1 (29.0/8.0)
					* Children > 2
						* Husband_education <= 2: 3 (52.0/31.0)
						* Husband_education > 2
							* Wife_religion <= 0
								* Husband_occupation <= 2: 1 (9.0/5.0)
								* Husband_occupation > 2: 3 (9.0/3.0)
							* Wife_religion > 0
								* Wife_age <= 33
									* Wife_age <= 23: 1 (8.0/3.0)
									* Wife_age > 23: 3 (96.0/26.0)
								* Wife_age > 33
									* Wife_education <= 2
										* Wife_working <= 0: 1 (10.0/4.0)
										* Wife_working > 0: 3 (20.0/8.0)
									* Wife_education > 2: 1 (18.0/7.0)
				* Media_exposure > 0: 1 (45.0/18.0)
		* Wife_age > 41: 1 (124.0/30.0)
	* Wife_education > 3
		* Husband_education <= 3: 3 (24.0/9.0)
		* Husband_education > 3
			* Children <= 2
				* Wife_age <= 39: 3 (153.0/94.0)
				* Wife_age > 39: 1 (19.0/4.0)
			* Children > 2
				* Wife_age <= 28
					* Husband_occupation <= 1: 1 (9.0/4.0)
					* Husband_occupation > 1: 3 (11.0/2.0)
				* Wife_age > 28
					* Wife_age <= 42: 2 (134.0/60.0)
					* Wife_age > 42
						* Standard-of-living <= 3: 1 (9.0/5.0)
						* Standard-of-living > 3
							* Husband_occupation <= 1: 2 (31.0/15.0)
							* Husband_occupation > 1: 1 (11.0/6.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(83.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/120.0)
			* Children >= 2.5: 3(163.0/136.0)
		* Wife_age >= 37.5: 1(154.0/63.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 39.5
				* Husband_occupation < 1.5
					* Wife_age < 29.5: 2(27.0/36.0)
					* Wife_age >= 29.5
						* Wife_religion < 0.5: 3(7.0/7.0)
						* Wife_religion >= 0.5: 1(14.0/12.0)
				* Husband_occupation >= 1.5: 3(53.0/44.0)
			* Wife_age >= 39.5: 1(17.0/4.0)
		* Children >= 2.5
			* Wife_age < 28.5
				* Husband_occupation < 1.5: 1(7.0/4.0)
				* Husband_occupation >= 1.5: 3(11.0/2.0)
			* Wife_age >= 28.5: 2(124.0/116.0)


