# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_education < 3.5 and Wife_age >= 37.5 | 1 | 0.129293 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.105812 |
| Children <= 0.5 | 1 | 0.096370 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.061607 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children < 2.5 | 1 | 0.079447 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Wife_age < 43.5 | 3 | 0.045132 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Wife_age > 28.5 and Children > 2.5 and Wife_age <= 35.5 and Husband_occupation <= 1.5 | 3 | 0.012441 |
| Children > 0.5 and Wife_age > 41.5 and Husband_education > 2.5 and Wife_education > 1.5 and Children <= 3.5 | 1 | 0.025975 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children <= 2.5 and Standard-of-living > 1.5 and Husband_education <= 2.5 | 3 | 0.009022 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children <= 2.5 and Standard-of-living > 1.5 and Husband_education > 2.5 and Wife_age <= 23.5 and Husband_occupation > 2.5 and Wife_age > 20.5 | 3 | 0.008113 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation > 1.5 and Wife_religion > 0.5 and Wife_age > 35.5 | 1 | 0.019586 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Children <= 4.5 and Children <= 3.5 | 2 | 0.004154 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Children <= 4.5 and Children > 3.5 | 1 | 0.005359 |
| Children > 0.5 and Wife_age > 41.5 and Husband_education > 2.5 and Wife_education > 1.5 and Children > 3.5 and Wife_age <= 47.5 | 2 | 0.015733 |
| Children > 0.5 and Wife_age > 41.5 and Husband_education > 2.5 and Wife_education > 1.5 and Children > 3.5 and Wife_age > 47.5 | 1 | 0.014473 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children > 7.5 | 1 | 0.011327 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education <= 1.5 | 1 | 0.006579 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation > 1.5 and Wife_religion <= 0.5 | 1 | 0.004749 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education > 3.5 and Wife_age <= 28.5 | 3 | 0.035600 |
| Children > 0.5 and Wife_age <= 41.5 and Wife_education <= 3.5 and Husband_education > 1.5 and Children > 2.5 and Children <= 7.5 and Husband_occupation <= 1.5 and Children > 4.5 | 3 | 0.005832 |
| Children > 0.5 and Wife_age > 41.5 and Husband_education <= 2.5 | 1 | 0.051798 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.0 | 1 | 0.096370 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Media_exposure <= 0.0 and Wife_working > 0.0 and Husband_education > 2.0 and Wife_age <= 45.0 and Wife_religion > 0.0 | 1 | 0.027802 |
| Wife_education <= 3.0 and Wife_age > 37.0 and Standard-of-living > 2.0 and Wife_working > 0.0 and Wife_religion > 0.0 | 1 | 0.038081 |
| Wife_education <= 2.0 and Wife_age > 37.0 | 1 | 0.048410 |
| Wife_education <= 3.0 and Children <= 2.0 and Wife_age <= 25.0 and Husband_occupation <= 2.0 and Husband_education <= 3.0 and Children > 1.0 | 3 | 0.008193 |
| Wife_education <= 3.0 and Children <= 2.0 and Wife_age <= 23.0 and Wife_education <= 2.0 and Husband_education > 2.0 and Standard-of-living <= 2.0 | 3 | 0.007574 |
| Wife_education <= 3.0 and Children <= 2.0 and Wife_age > 30.0 | 1 | 0.027504 |
| Wife_education <= 3.0 and Standard-of-living <= 1.0 and Wife_education <= 2.0 and Children <= 4.0 and Children <= 3.0 | 1 | 0.030392 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Children > 2.0 and Husband_education > 1.0 and Media_exposure <= 0.0 and Children <= 5.0 and Husband_occupation > 1.0 and Wife_age <= 32.0 and Standard-of-living <= 2.0 and Husband_occupation <= 2.0 | 3 | 0.015513 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Children > 2.0 and Husband_education > 1.0 and Media_exposure <= 0.0 and Wife_education <= 2.0 and Standard-of-living <= 3.0 and Wife_working > 0.0 and Husband_occupation > 2.0 | 3 | 0.043302 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Husband_education > 1.0 and Children > 2.0 and Media_exposure <= 0.0 and Children <= 5.0 and Wife_working <= 0.0 and Husband_education <= 3.0 and Standard-of-living <= 3.0 | 3 | 0.012668 |
| Wife_education <= 3.0 and Husband_education > 1.0 and Wife_working <= 0.0 and Husband_occupation > 1.0 and Wife_religion > 0.0 and Wife_education > 1.0 and Media_exposure <= 0.0 and Husband_occupation <= 2.0 | 1 | 0.010649 |
| Wife_education <= 3.0 and Husband_education <= 1.0 | 2 | 0.007154 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Children > 2.0 and Media_exposure <= 0.0 and Husband_education > 2.0 and Wife_education <= 2.0 and Wife_working <= 0.0 | 1 | 0.006284 |
| Children > 2.0 and Wife_education > 3.0 and Wife_age > 28.0 and Wife_age <= 42.0 and Standard-of-living > 3.0 and Wife_age > 32.0 and Children > 3.0 and Wife_religion <= 0.0 | 2 | 0.014927 |
| Children <= 2.0 and Wife_age <= 43.0 and Wife_education <= 2.0 and Wife_working > 0.0 and Husband_education > 2.0 and Children <= 1.0 | 1 | 0.015305 |
| Wife_education <= 3.0 and Wife_working > 0.0 and Husband_occupation > 1.0 and Wife_education > 1.0 and Wife_age <= 34.0 and Wife_age > 28.0 | 3 | 0.043976 |
| Wife_education <= 3.0 and Husband_occupation <= 1.0 and Children > 4.0 | 3 | 0.016498 |
| Wife_age <= 28.0 and Husband_occupation > 1.0 and Wife_working > 0.0 and Media_exposure <= 0.0 and Wife_education > 3.0 and Children > 1.0 | 3 | 0.027084 |
| Wife_education <= 3.0 and Wife_religion > 0.0 and Husband_occupation > 1.0 and Wife_working > 0.0 and Wife_education <= 1.0 | 3 | 0.019785 |
| Wife_education <= 3.0 and Media_exposure > 0.0 | 1 | 0.020550 |
| Children > 2.0 and Wife_age <= 28.0 and Husband_occupation > 1.0 and Husband_education > 3.0 | 3 | 0.020809 |
| Children > 2.0 and Wife_education > 3.0 and Husband_education <= 3.0 | 3 | 0.006958 |
| Children > 2.0 and Wife_education > 3.0 and Wife_age <= 47.0 and Wife_age > 28.0 and Standard-of-living > 3.0 and Wife_age <= 32.0 and Husband_occupation <= 1.0 | 3 | 0.016589 |
| Children > 2.0 and Wife_education > 3.0 and Wife_age <= 47.0 and Wife_age > 28.0 and Wife_working > 0.0 and Wife_religion > 0.0 and Standard-of-living > 2.0 and Standard-of-living > 3.0 | 2 | 0.059911 |
| Wife_age <= 25.0 and Wife_education <= 3.0 and Children > 1.0 and Standard-of-living > 2.0 and Husband_occupation <= 2.0 | 3 | 0.009804 |
| Wife_age > 41.0 and Children > 1.0 and Wife_age > 47.0 | 1 | 0.011057 |
| Children <= 2.0 and Wife_age > 43.0 | 1 | 0.018634 |
| Children <= 2.0 and Wife_education <= 2.0 and Wife_working > 0.0 and Husband_education > 2.0 | 1 | 0.003854 |
| Children <= 2.0 and Husband_occupation > 1.0 and Standard-of-living <= 3.0 and Wife_religion > 0.0 and Children <= 1.0 and Wife_education <= 3.0 and Husband_occupation > 2.0 and Standard-of-living <= 2.0 | 1 | 0.004264 |
| Children <= 2.0 and Wife_education <= 2.0 and Husband_education > 2.0 | 1 | 0.003373 |
| Children <= 2.0 and Wife_working > 0.0 and Husband_education <= 3.0 and Children <= 1.0 | 3 | 0.041379 |
| Wife_working <= 0.0 and Wife_education > 3.0 and Children > 3.0 | 2 | 0.023784 |
| Wife_education <= 2.0 and Husband_occupation <= 2.0 | 1 | 0.013524 |
| Children > 2.0 and Wife_age > 25.0 and Husband_occupation > 2.0 and Wife_age > 28.0 and Standard-of-living <= 3.0 and Wife_age <= 36.0 | 2 | 0.025960 |
| Husband_occupation > 2.0 and Wife_working > 0.0 and Wife_religion <= 0.0 | 3 | 0.019355 |
| Wife_religion <= 0.0 and Children > 1.0 and Children <= 3.0 and Husband_occupation <= 2.0 and Children <= 2.0 and Wife_age <= 32.0 | 2 | 0.014619 |
| Children <= 2.0 and Wife_working <= 0.0 and Children > 1.0 and Standard-of-living <= 3.0 and Husband_occupation > 1.0 | 3 | 0.009066 |
| Children <= 2.0 and Husband_education <= 3.0 and Wife_age <= 25.0 | 1 | 0.025729 |
| Husband_education <= 3.0 and Wife_age > 25.0 and Children > 2.0 and Children <= 5.0 | 3 | 0.020916 |
| Husband_education <= 3.0 and Wife_age > 25.0 | 2 | 0.051174 |
| Wife_education <= 3.0 and Husband_education > 3.0 and Wife_working > 0.0 and Standard-of-living <= 3.0 and Children <= 2.0 and Husband_occupation <= 2.0 | 1 | 0.014837 |
| Husband_occupation > 2.0 and Husband_education > 3.0 and Wife_working > 0.0 and Wife_education <= 3.0 | 3 | 0.012289 |
| Children > 2.0 and Husband_education > 3.0 and Husband_occupation > 2.0 | 2 | 0.018547 |
| Husband_occupation > 2.0 and Husband_education > 3.0 | 3 | 0.030610 |
| Wife_religion <= 0.0 and Children <= 3.0 and Children <= 2.0 and Wife_working > 0.0 and Husband_occupation <= 1.0 | 1 | 0.007388 |
| Wife_religion <= 0.0 and Children <= 3.0 and Wife_working > 0.0 | 2 | 0.022251 |
| Husband_education > 3.0 and Wife_religion <= 0.0 | 3 | 0.051705 |
| Husband_education > 3.0 and Wife_age <= 42.0 and Wife_age <= 40.0 and Wife_education <= 3.0 and Children <= 3.0 | 2 | 0.036119 |
| Husband_education > 3.0 and Wife_education > 3.0 and Wife_age <= 42.0 and Wife_age <= 39.0 and Husband_occupation > 1.0 and Wife_working > 0.0 | 3 | 0.024550 |
| Husband_education > 3.0 and Wife_education > 3.0 and Husband_occupation <= 1.0 and Standard-of-living <= 3.0 and Wife_working > 0.0 and Children > 2.0 | 2 | 0.022624 |
| Children > 3.0 | 1 | 0.123776 |
| Wife_working > 0.0 and Standard-of-living <= 3.0 and Wife_age <= 25.0 and Children <= 1.0 | 2 | 0.019704 |
| Wife_working > 0.0 and Standard-of-living <= 3.0 and Wife_age > 25.0 | 1 | 0.030120 |
| Wife_working > 0.0 and Standard-of-living > 3.0 and Children > 1.0 | 1 | 0.062810 |
| Wife_working > 0.0 and Children <= 1.0 and Wife_age > 24.0 | 1 | 0.041523 |
| Children <= 1.0 and Wife_age <= 24.0 | 2 | 0.022878 |
| Wife_working <= 0.0 and Children > 1.0 and Standard-of-living > 3.0 and Children <= 2.0 | 3 | 0.040099 |
| Wife_working <= 0.0 and Children > 1.0 | 2 | 0.084247 |
| Children <= 1.0 | 1 | 0.061311 |
|  | 3 | 0.635220 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_education >= 4 and Children >= 3 and Wife_age >= 34 | 2 | 0.053834 |
| Wife_age <= 35 and Children >= 3 | 3 | 0.134602 |
|  | 1 | 0.551657 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Wife_education >= 4) and (Children >= 3) and (Wife_age >= 34)|2 (193.0/89.0)
(Wife_age <= 35) and (Children >= 3)|3 (345.0/158.0)
|1 (788.0/344.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.0|1 (85.0/2.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Media_exposure <= 0.0 AND Wife_working > 0.0 AND Husband_education > 2.0 AND Wife_age <= 45.0 AND Wife_religion > 0.0|1 (57.0/22.0)
Wife_education <= 3.0 AND Wife_age > 37.0 AND Standard-of-living > 2.0 AND Wife_working > 0.0 AND Wife_religion > 0.0|1 (53.0/8.0)
Wife_education <= 2.0 AND Wife_age > 37.0|1 (65.0/9.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Wife_age <= 25.0 AND Husband_occupation <= 2.0 AND Husband_education <= 3.0 AND Children > 1.0|3 (12.0/4.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Wife_age <= 23.0 AND Wife_education <= 2.0 AND Husband_education > 2.0 AND Standard-of-living <= 2.0|3 (13.0/5.0)
Wife_education <= 3.0 AND Children <= 2.0 AND Wife_age > 30.0|1 (39.0/9.0)
Wife_education <= 3.0 AND Standard-of-living <= 1.0 AND Wife_education <= 2.0 AND Children <= 4.0 AND Children <= 3.0|1 (26.0/3.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Children > 2.0 AND Husband_education > 1.0 AND Media_exposure <= 0.0 AND Children <= 5.0 AND Husband_occupation > 1.0 AND Wife_age <= 32.0 AND Standard-of-living <= 2.0 AND Husband_occupation <= 2.0|3 (13.0/2.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Children > 2.0 AND Husband_education > 1.0 AND Media_exposure <= 0.0 AND Wife_education <= 2.0 AND Standard-of-living <= 3.0 AND Wife_working > 0.0 AND Husband_occupation > 2.0|3 (41.0/9.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Husband_education > 1.0 AND Children > 2.0 AND Media_exposure <= 0.0 AND Children <= 5.0 AND Wife_working <= 0.0 AND Husband_education <= 3.0 AND Standard-of-living <= 3.0|3 (16.0/5.0)
Wife_education <= 3.0 AND Husband_education > 1.0 AND Wife_working <= 0.0 AND Husband_occupation > 1.0 AND Wife_religion > 0.0 AND Wife_education > 1.0 AND Media_exposure <= 0.0 AND Husband_occupation <= 2.0|1 (21.0/8.0)
Wife_education <= 3.0 AND Husband_education <= 1.0|2 (14.0/7.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Children > 2.0 AND Media_exposure <= 0.0 AND Husband_education > 2.0 AND Wife_education <= 2.0 AND Wife_working <= 0.0|1 (9.0/4.0)
Children > 2.0 AND Wife_education > 3.0 AND Wife_age > 28.0 AND Wife_age <= 42.0 AND Standard-of-living > 3.0 AND Wife_age > 32.0 AND Children > 3.0 AND Wife_religion <= 0.0|2 (17.0/4.0)
Children <= 2.0 AND Wife_age <= 43.0 AND Wife_education <= 2.0 AND Wife_working > 0.0 AND Husband_education > 2.0 AND Children <= 1.0|1 (16.0/4.0)
Wife_education <= 3.0 AND Wife_working > 0.0 AND Husband_occupation > 1.0 AND Wife_education > 1.0 AND Wife_age <= 34.0 AND Wife_age > 28.0|3 (57.0/19.0)
Wife_education <= 3.0 AND Husband_occupation <= 1.0 AND Children > 4.0|3 (16.0/4.0)
Wife_age <= 28.0 AND Husband_occupation > 1.0 AND Wife_working > 0.0 AND Media_exposure <= 0.0 AND Wife_education > 3.0 AND Children > 1.0|3 (27.0/7.0)
Wife_education <= 3.0 AND Wife_religion > 0.0 AND Husband_occupation > 1.0 AND Wife_working > 0.0 AND Wife_education <= 1.0|3 (18.0/5.0)
Wife_education <= 3.0 AND Media_exposure > 0.0|1 (25.0/10.0)
Children > 2.0 AND Wife_age <= 28.0 AND Husband_occupation > 1.0 AND Husband_education > 3.0|3 (26.0/8.0)
Children > 2.0 AND Wife_education > 3.0 AND Husband_education <= 3.0|3 (16.0/8.0)
Children > 2.0 AND Wife_education > 3.0 AND Wife_age <= 47.0 AND Wife_age > 28.0 AND Standard-of-living > 3.0 AND Wife_age <= 32.0 AND Husband_occupation <= 1.0|3 (14.0/3.0)
Children > 2.0 AND Wife_education > 3.0 AND Wife_age <= 47.0 AND Wife_age > 28.0 AND Wife_working > 0.0 AND Wife_religion > 0.0 AND Standard-of-living > 2.0 AND Standard-of-living > 3.0|2 (90.0/41.0)
Wife_age <= 25.0 AND Wife_education <= 3.0 AND Children > 1.0 AND Standard-of-living > 2.0 AND Husband_occupation <= 2.0|3 (14.0/6.0)
Wife_age > 41.0 AND Children > 1.0 AND Wife_age > 47.0|1 (15.0/5.0)
Children <= 2.0 AND Wife_age > 43.0|1 (13.0/1.0)
Children <= 2.0 AND Wife_education <= 2.0 AND Wife_working > 0.0 AND Husband_education > 2.0|1 (11.0/6.0)
Children <= 2.0 AND Husband_occupation > 1.0 AND Standard-of-living <= 3.0 AND Wife_religion > 0.0 AND Children <= 1.0 AND Wife_education <= 3.0 AND Husband_occupation > 2.0 AND Standard-of-living <= 2.0|1 (14.0/8.0)
Children <= 2.0 AND Wife_education <= 2.0 AND Husband_education > 2.0|1 (8.0/2.0)
Children <= 2.0 AND Wife_working > 0.0 AND Husband_education <= 3.0 AND Children <= 1.0|3 (21.0/5.0)
Wife_working <= 0.0 AND Wife_education > 3.0 AND Children > 3.0|2 (16.0/4.0)
Wife_education <= 2.0 AND Husband_occupation <= 2.0|1 (14.0/6.0)
Children > 2.0 AND Wife_age > 25.0 AND Husband_occupation > 2.0 AND Wife_age > 28.0 AND Standard-of-living <= 3.0 AND Wife_age <= 36.0|2 (18.0/5.0)
Husband_occupation > 2.0 AND Wife_working > 0.0 AND Wife_religion <= 0.0|3 (16.0/7.0)
Wife_religion <= 0.0 AND Children > 1.0 AND Children <= 3.0 AND Husband_occupation <= 2.0 AND Children <= 2.0 AND Wife_age <= 32.0|2 (11.0/3.0)
Children <= 2.0 AND Wife_working <= 0.0 AND Children > 1.0 AND Standard-of-living <= 3.0 AND Husband_occupation > 1.0|3 (10.0/4.0)
Children <= 2.0 AND Husband_education <= 3.0 AND Wife_age <= 25.0|1 (12.0/4.0)
Husband_education <= 3.0 AND Wife_age > 25.0 AND Children > 2.0 AND Children <= 5.0|3 (19.0/10.0)
Husband_education <= 3.0 AND Wife_age > 25.0|2 (19.0/8.0)
Wife_education <= 3.0 AND Husband_education > 3.0 AND Wife_working > 0.0 AND Standard-of-living <= 3.0 AND Children <= 2.0 AND Husband_occupation <= 2.0|1 (13.0/5.0)
Husband_occupation > 2.0 AND Husband_education > 3.0 AND Wife_working > 0.0 AND Wife_education <= 3.0|3 (20.0/11.0)
Children > 2.0 AND Husband_education > 3.0 AND Husband_occupation > 2.0|2 (12.0/6.0)
Husband_occupation > 2.0 AND Husband_education > 3.0|3 (30.0/17.0)
Wife_religion <= 0.0 AND Children <= 3.0 AND Children <= 2.0 AND Wife_working > 0.0 AND Husband_occupation <= 1.0|1 (11.0/6.0)
Wife_religion <= 0.0 AND Children <= 3.0 AND Wife_working > 0.0|2 (21.0/11.0)
Husband_education > 3.0 AND Wife_religion <= 0.0|3 (26.0/13.0)
Husband_education > 3.0 AND Wife_age <= 42.0 AND Wife_age <= 40.0 AND Wife_education <= 3.0 AND Children <= 3.0|2 (12.0/4.0)
Husband_education > 3.0 AND Wife_education > 3.0 AND Wife_age <= 42.0 AND Wife_age <= 39.0 AND Husband_occupation > 1.0 AND Wife_working > 0.0|3 (24.0/12.0)
Husband_education > 3.0 AND Wife_education > 3.0 AND Husband_occupation <= 1.0 AND Standard-of-living <= 3.0 AND Wife_working > 0.0 AND Children > 2.0|2 (15.0/6.0)
Children > 3.0|1 (16.0/4.0)
Wife_working > 0.0 AND Standard-of-living <= 3.0 AND Wife_age <= 25.0 AND Children <= 1.0|2 (9.0/5.0)
Wife_working > 0.0 AND Standard-of-living <= 3.0 AND Wife_age > 25.0|1 (8.0/3.0)
Wife_working > 0.0 AND Standard-of-living > 3.0 AND Children > 1.0|1 (22.0/13.0)
Wife_working > 0.0 AND Children <= 1.0 AND Wife_age > 24.0|1 (14.0/7.0)
Children <= 1.0 AND Wife_age <= 24.0|2 (10.0/5.0)
Wife_working <= 0.0 AND Children > 1.0 AND Standard-of-living > 3.0 AND Children <= 2.0|3 (14.0/7.0)
Wife_working <= 0.0 AND Children > 1.0|2 (18.0/8.0)
Children <= 1.0|1 (7.0/3.0)
|3 (7.0/1.0)


## J48 Decision Tree

* Children <= 0.5: 1 (44.0/1.0)
* Children > 0.5
	* Wife_age <= 41.5
		* Wife_education <= 3.5
			* Husband_education <= 1.5: 1 (13.0/6.0)
			* Husband_education > 1.5
				* Children <= 2.5
					* Standard-of-living <= 1.5: 1 (20.0/4.0)
					* Standard-of-living > 1.5
						* Husband_education <= 2.5: 3 (10.0/4.0)
						* Husband_education > 2.5
							* Wife_age <= 23.5
								* Husband_occupation <= 2.5: 1 (14.0/6.0)
								* Husband_occupation > 2.5
									* Wife_age <= 20.5: 1 (8.0/1.0)
									* Wife_age > 20.5: 3 (12.0/6.0)
							* Wife_age > 23.5: 1 (52.0/21.0)
				* Children > 2.5
					* Children <= 7.5
						* Husband_occupation <= 1.5
							* Children <= 4.5
								* Children <= 3.5: 2 (9.0/4.0)
								* Children > 3.5: 1 (8.0/3.0)
							* Children > 4.5: 3 (8.0/3.0)
						* Husband_occupation > 1.5
							* Wife_religion <= 0.5: 1 (13.0/7.0)
							* Wife_religion > 0.5
								* Wife_age <= 35.5: 3 (111.0/36.0)
								* Wife_age > 35.5: 1 (24.0/12.0)
					* Children > 7.5: 1 (18.0/9.0)
		* Wife_education > 3.5
			* Wife_age <= 28.5: 3 (77.0/39.0)
			* Wife_age > 28.5
				* Children <= 2.5: 3 (36.0/19.0)
				* Children > 2.5
					* Wife_age <= 35.5
						* Husband_occupation <= 1.5: 3 (16.0/5.0)
						* Husband_occupation > 1.5: 2 (14.0/3.0)
					* Wife_age > 35.5: 2 (43.0/12.0)
	* Wife_age > 41.5
		* Husband_education <= 2.5: 1 (26.0/2.0)
		* Husband_education > 2.5
			* Wife_education <= 1.5: 1 (12.0/1.0)
			* Wife_education > 1.5
				* Children <= 3.5: 1 (20.0/5.0)
				* Children > 3.5
					* Wife_age <= 47.5: 2 (39.0/24.0)
					* Wife_age > 47.5: 1 (16.0/4.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(83.0/2.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(119.0/114.0)
			* Children >= 2.5: 3(172.0/139.0)
		* Wife_age >= 37.5: 1(152.0/57.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Wife_age < 43.5: 3(88.0/117.0)
			* Wife_age >= 43.5: 1(12.0/1.0)
		* Children >= 2.5: 2(130.0/140.0)


