# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children >= 0.5 and Wife_education < 3.5 and Wife_age >= 37.5 | 1 | 0.123292 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.104734 |
| Children < 0.5 | 1 | 0.100605 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children < 2.5 | 1 | 0.083254 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age >= 32.5 | 2 | 0.060511 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation >= 1.5 | 3 | 0.033440 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation < 1.5 | 1 | 0.029840 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 and Wife_age < 32.5 | 3 | 0.018769 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 2 | 0.007882 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 1 | 0.006931 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 3 | 0.031636 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 7.5 and Wife_working = all | 3 | 0.002312 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education <= 2.5 and Children > 7.5 and Wife_working = all | 1 | 0.002111 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 7.5 and Wife_working = all | 3 | 0.001156 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 1 | 0.010318 |
| Wife_age <= 31.5 and Wife_education <= 2.5 and Children > 7.5 and Wife_working = all | 1 | 0.001314 |
| Wife_age > 46.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 1 | 0.005236 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 and Wife_working = all | 2 | 0.022283 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 and Wife_working = all | 1 | 0.009630 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children > 0.5 and Wife_education <= 3.5 and Wife_age > 37.5 | 1 | 0.123292 |
| Children <= 0.5 | 1 | 0.100605 |
| Wife_education <= 3.5 and Children <= 2.5 and Wife_age > 30.5 | 1 | 0.020786 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Husband_education > 1.5 and Wife_religion > 0.5 and Children > 2.5 and Media_exposure <= 0.5 and Wife_age <= 29.5 and Wife_age <= 27.5 and Husband_education <= 3.5 and Standard-of-living <= 3.5 | 3 | 0.024496 |
| Wife_education <= 3.5 and Husband_education > 1.5 and Children <= 2.5 and Wife_religion > 0.5 and Husband_occupation <= 3.5 and Wife_working > 0.5 and Media_exposure <= 0.5 and Husband_education <= 3.5 and Husband_occupation <= 2.5 and Wife_age <= 27.0 | 3 | 0.015518 |
| Wife_education <= 3.5 and Husband_education > 1.5 and Children <= 2.5 and Wife_religion > 0.5 and Husband_occupation <= 3.5 and Media_exposure <= 0.5 and Standard-of-living <= 3.5 and Husband_occupation <= 2.5 | 1 | 0.024203 |
| Wife_education <= 3.5 and Husband_education > 1.5 and Husband_occupation > 1.5 and Wife_working > 0.5 and Wife_education <= 1.5 | 3 | 0.028050 |
| Wife_education <= 3.5 and Husband_education <= 1.5 | 1 | 0.003716 |
| Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Children > 2.5 and Wife_working > 0.5 and Standard-of-living > 1.5 and Standard-of-living > 2.5 and Husband_education > 3.5 and Children <= 3.5 and Wife_education <= 2.5 | 3 | 0.017296 |
| Wife_education <= 3.5 and Husband_occupation > 1.5 and Media_exposure > 0.5 and Husband_occupation <= 3.5 and Standard-of-living <= 2.5 and Husband_education <= 2.5 | 1 | 0.007815 |
| Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Husband_occupation > 1.5 and Wife_age <= 20.5 | 1 | 0.014734 |
| Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Husband_occupation > 1.5 and Children > 2.5 and Standard-of-living <= 1.5 | 3 | 0.010495 |
| Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Standard-of-living <= 1.5 | 1 | 0.014868 |
| Wife_education <= 3.5 and Media_exposure <= 0.5 and Husband_occupation > 1.5 and Wife_religion > 0.5 and Wife_working > 0.5 and Husband_education > 2.5 and Wife_education <= 2.5 and Wife_age <= 24.5 | 1 | 0.006733 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Wife_working > 0.5 and Husband_occupation > 2.5 and Children > 3.5 and Standard-of-living > 2.5 and Standard-of-living <= 3.5 | 3 | 0.024315 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Media_exposure <= 0.5 and Wife_religion > 0.5 and Wife_working <= 0.5 and Husband_occupation <= 2.5 and Wife_education <= 2.5 | 3 | 0.010139 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Media_exposure > 0.5 and Wife_education > 2.5 and Wife_age <= 32.5 | 3 | 0.006095 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Media_exposure > 0.5 | 1 | 0.006231 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Wife_working > 0.5 and Husband_occupation > 2.5 and Husband_occupation <= 3.5 and Wife_religion <= 0.5 | 3 | 0.015543 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Wife_religion > 0.5 and Wife_working > 0.5 and Husband_education > 2.5 and Wife_education <= 2.5 and Husband_education > 3.5 and Wife_age <= 29.5 | 3 | 0.017449 |
| Husband_occupation > 1.5 and Wife_education <= 3.5 and Wife_religion > 0.5 and Wife_working <= 0.5 and Standard-of-living <= 2.5 and Husband_education <= 3.5 | 3 | 0.013315 |
| Children > 2.5 and Wife_education > 3.5 and Wife_age > 32.5 and Wife_age <= 47.5 and Husband_education > 3.5 and Wife_working <= 0.5 | 2 | 0.037739 |
| Wife_education <= 2.5 and Wife_religion > 0.5 and Husband_education > 2.5 and Wife_working <= 0.5 | 1 | 0.013064 |
| Husband_occupation > 1.5 and Wife_religion > 0.5 and Wife_education <= 3.5 and Husband_occupation > 2.5 and Husband_occupation <= 3.5 and Husband_education > 3.5 and Wife_education > 2.5 | 3 | 0.027220 |
| Wife_education <= 2.5 and Wife_religion > 0.5 and Husband_occupation <= 3.5 and Husband_education > 2.5 | 3 | 0.028770 |
| Children > 2.5 and Wife_working > 0.5 and Wife_religion <= 0.5 | 2 | 0.043769 |
| Husband_occupation > 1.5 and Children <= 2.5 and Husband_occupation > 2.5 and Wife_working > 0.5 and Children > 1.5 | 3 | 0.018115 |
| Children > 1.5 and Wife_religion > 0.5 and Husband_occupation > 2.5 and Husband_occupation <= 3.5 and Children <= 7.5 and Children <= 5.5 and Wife_working > 0.5 and Standard-of-living <= 3.5 | 3 | 0.006310 |
| Wife_age > 44.5 and Wife_religion > 0.5 and Standard-of-living > 3.5 and Children > 1.5 | 2 | 0.022146 |
| Wife_age > 43.5 and Children <= 3.5 | 1 | 0.020545 |
| Husband_occupation > 1.5 and Wife_working > 0.5 and Wife_religion > 0.5 and Husband_education > 3.5 and Standard-of-living > 2.5 and Standard-of-living > 3.5 and Husband_occupation > 2.5 and Children > 2.0 | 3 | 0.006823 |
| Husband_occupation > 1.5 and Wife_working > 0.5 and Wife_religion > 0.5 and Husband_education > 3.5 and Standard-of-living > 2.5 and Standard-of-living > 3.5 and Husband_occupation <= 2.5 and Wife_education > 3.5 and Children <= 3.5 | 3 | 0.015356 |
| Husband_occupation > 1.5 and Wife_age > 22.5 and Husband_occupation > 2.5 and Husband_occupation <= 3.5 and Wife_education > 2.5 and Husband_education > 2.5 and Wife_working > 0.5 | 3 | 0.011624 |
| Children <= 1.5 and Husband_education <= 3.5 | 3 | 0.018777 |
| Wife_religion > 0.5 and Wife_working > 0.5 and Children > 2.5 and Wife_age <= 44.5 and Standard-of-living > 2.5 and Standard-of-living <= 3.5 and Husband_occupation <= 1.5 | 2 | 0.025037 |
| Wife_religion > 0.5 and Standard-of-living > 3.5 and Children <= 5.5 and Wife_working > 0.5 and Wife_education > 3.5 | 2 | 0.068077 |
| Wife_age <= 43.5 and Standard-of-living > 3.5 and Children <= 5.5 and Children <= 4.5 and Husband_occupation <= 2.5 and Husband_education > 3.5 and Wife_age <= 36.5 | 3 | 0.092239 |
| Wife_age <= 43.5 and Husband_occupation > 2.5 and Wife_education > 3.5 | 3 | 0.012484 |
| Husband_occupation > 2.5 | 2 | 0.112113 |
| Wife_religion <= 0.5 and Standard-of-living > 3.5 | 1 | 0.064502 |
| Wife_working <= 0.5 and Husband_occupation <= 1.5 and Children > 1.5 | 2 | 0.016848 |
| Wife_working <= 0.5 | 1 | 0.116590 |
| Wife_religion <= 0.5 and Children <= 1.5 | 1 | 0.011905 |
| Wife_religion > 0.5 and Standard-of-living <= 2.5 | 2 | 0.030691 |
| Wife_religion > 0.5 and Standard-of-living > 3.5 and Wife_education <= 3.5 | 3 | 0.034372 |
| Standard-of-living > 3.5 and Husband_occupation <= 1.5 | 2 | 0.027881 |
| Wife_religion > 0.5 | 3 | 0.293076 |
|  | 2 | 0.203593 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

wife_age|wife_education|children|wife_working|contraceptive_method
---|---|---|---|---
(46.5-inf)|(3.5-inf)|(7.5-inf)|all|3
(37.5-46.5]|(3.5-inf)|(7.5-inf)|all|3
(37.5-46.5]|(2.5-3.5]|(7.5-inf)|all|1
(46.5-inf)|(2.5-3.5]|(7.5-inf)|all|1
(31.5-37.5]|(2.5-3.5]|(7.5-inf)|all|3
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|all|1
(31.5-37.5]|(-inf-2.5]|(7.5-inf)|all|1
(31.5-37.5]|(3.5-inf)|(2.5-7.5]|all|2
(46.5-inf)|(-inf-2.5]|(7.5-inf)|all|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|all|3
(37.5-46.5]|(-inf-2.5]|(7.5-inf)|all|1
(46.5-inf)|(3.5-inf)|(2.5-7.5]|all|1
(37.5-46.5]|(3.5-inf)|(2.5-7.5]|all|2
(46.5-inf)|(2.5-3.5]|(2.5-7.5]|all|1
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|all|3
(37.5-46.5]|(2.5-3.5]|(2.5-7.5]|all|1
(31.5-37.5]|(2.5-3.5]|(2.5-7.5]|all|2
(46.5-inf)|(3.5-inf)|(0.5-2.5]|all|1
(46.5-inf)|(-inf-2.5]|(2.5-7.5]|all|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|all|1
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|all|3
(31.5-37.5]|(-inf-2.5]|(2.5-7.5]|all|3
(37.5-46.5]|(-inf-2.5]|(2.5-7.5]|all|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|all|1
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|all|3
(46.5-inf)|(2.5-3.5]|(0.5-2.5]|all|1
(37.5-46.5]|(2.5-3.5]|(0.5-2.5]|all|1
(31.5-37.5]|(2.5-3.5]|(0.5-2.5]|all|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|all|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-2.5]|(0.5-2.5]|all|1
(46.5-inf)|(-inf-2.5]|(0.5-2.5]|all|1
(37.5-46.5]|(-inf-2.5]|(0.5-2.5]|all|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|all|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|all|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|all|1
(46.5-inf)|(-inf-2.5]|(-inf-0.5]|all|1
(37.5-46.5]|(-inf-2.5]|(-inf-0.5]|all|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|all|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|all|1

## PART

Decision list:

rules | predicted class
---|---
Children > 0.5 AND Wife_education <= 3.5 AND Wife_age > 37.5|1 (182.0/53.0)
Children <= 0.5|1 (77.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Wife_age > 30.5|1 (24.0/4.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Husband_education > 1.5 AND Wife_religion > 0.5 AND Children > 2.5 AND Media_exposure <= 0.5 AND Wife_age <= 29.5 AND Wife_age <= 27.5 AND Husband_education <= 3.5 AND Standard-of-living <= 3.5|3 (31.0/12.0)
Wife_education <= 3.5 AND Husband_education > 1.5 AND Children <= 2.5 AND Wife_religion > 0.5 AND Husband_occupation <= 3.5 AND Wife_working > 0.5 AND Media_exposure <= 0.5 AND Husband_education <= 3.5 AND Husband_occupation <= 2.5 AND Wife_age <= 27.0|3 (24.0/10.0)
Wife_education <= 3.5 AND Husband_education > 1.5 AND Children <= 2.5 AND Wife_religion > 0.5 AND Husband_occupation <= 3.5 AND Media_exposure <= 0.5 AND Standard-of-living <= 3.5 AND Husband_occupation <= 2.5|1 (24.0/7.0)
Wife_education <= 3.5 AND Husband_education > 1.5 AND Husband_occupation > 1.5 AND Wife_working > 0.5 AND Wife_education <= 1.5|3 (23.0/6.0)
Wife_education <= 3.5 AND Husband_education <= 1.5|1 (14.0/8.0)
Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Children > 2.5 AND Wife_working > 0.5 AND Standard-of-living > 1.5 AND Standard-of-living > 2.5 AND Husband_education > 3.5 AND Children <= 3.5 AND Wife_education <= 2.5|3 (11.0/1.0)
Wife_education <= 3.5 AND Husband_occupation > 1.5 AND Media_exposure > 0.5 AND Husband_occupation <= 3.5 AND Standard-of-living <= 2.5 AND Husband_education <= 2.5|1 (10.0/3.0)
Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Husband_occupation > 1.5 AND Wife_age <= 20.5|1 (18.0/6.0)
Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Husband_occupation > 1.5 AND Children > 2.5 AND Standard-of-living <= 1.5|3 (10.0/2.0)
Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Standard-of-living <= 1.5|1 (18.0/7.0)
Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Husband_occupation > 1.5 AND Wife_religion > 0.5 AND Wife_working > 0.5 AND Husband_education > 2.5 AND Wife_education <= 2.5 AND Wife_age <= 24.5|1 (8.0/2.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Wife_working > 0.5 AND Husband_occupation > 2.5 AND Children > 3.5 AND Standard-of-living > 2.5 AND Standard-of-living <= 3.5|3 (17.0/3.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Media_exposure <= 0.5 AND Wife_religion > 0.5 AND Wife_working <= 0.5 AND Husband_occupation <= 2.5 AND Wife_education <= 2.5|3 (7.0/2.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Media_exposure > 0.5 AND Wife_education > 2.5 AND Wife_age <= 32.5|3 (3.0/1.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Media_exposure > 0.5|1 (12.0/5.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Wife_working > 0.5 AND Husband_occupation > 2.5 AND Husband_occupation <= 3.5 AND Wife_religion <= 0.5|3 (10.0/3.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Wife_religion > 0.5 AND Wife_working > 0.5 AND Husband_education > 2.5 AND Wife_education <= 2.5 AND Husband_education > 3.5 AND Wife_age <= 29.5|3 (7.0)
Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Wife_religion > 0.5 AND Wife_working <= 0.5 AND Standard-of-living <= 2.5 AND Husband_education <= 3.5|3 (11.0/5.0)
Children > 2.5 AND Wife_education > 3.5 AND Wife_age > 32.5 AND Wife_age <= 47.5 AND Husband_education > 3.5 AND Wife_working <= 0.5|2 (40.0/12.0)
Wife_education <= 2.5 AND Wife_religion > 0.5 AND Husband_education > 2.5 AND Wife_working <= 0.5|1 (13.0/5.0)
Husband_occupation > 1.5 AND Wife_religion > 0.5 AND Wife_education <= 3.5 AND Husband_occupation > 2.5 AND Husband_occupation <= 3.5 AND Husband_education > 3.5 AND Wife_education > 2.5|3 (26.0/9.0)
Wife_education <= 2.5 AND Wife_religion > 0.5 AND Husband_occupation <= 3.5 AND Husband_education > 2.5|3 (36.0/18.0)
Children > 2.5 AND Wife_working > 0.5 AND Wife_religion <= 0.5|2 (47.0/20.0)
Husband_occupation > 1.5 AND Children <= 2.5 AND Husband_occupation > 2.5 AND Wife_working > 0.5 AND Children > 1.5|3 (22.0/9.0)
Children > 1.5 AND Wife_religion > 0.5 AND Husband_occupation > 2.5 AND Husband_occupation <= 3.5 AND Children <= 7.5 AND Children <= 5.5 AND Wife_working > 0.5 AND Standard-of-living <= 3.5|3 (16.0/7.0)
Wife_age > 44.5 AND Wife_religion > 0.5 AND Standard-of-living > 3.5 AND Children > 1.5|2 (18.0/8.0)
Wife_age > 43.5 AND Children <= 3.5|1 (8.0)
Husband_occupation > 1.5 AND Wife_working > 0.5 AND Wife_religion > 0.5 AND Husband_education > 3.5 AND Standard-of-living > 2.5 AND Standard-of-living > 3.5 AND Husband_occupation > 2.5 AND Children > 2.0|3 (12.0/6.0)
Husband_occupation > 1.5 AND Wife_working > 0.5 AND Wife_religion > 0.5 AND Husband_education > 3.5 AND Standard-of-living > 2.5 AND Standard-of-living > 3.5 AND Husband_occupation <= 2.5 AND Wife_education > 3.5 AND Children <= 3.5|3 (15.0/5.0)
Husband_occupation > 1.5 AND Wife_age > 22.5 AND Husband_occupation > 2.5 AND Husband_occupation <= 3.5 AND Wife_education > 2.5 AND Husband_education > 2.5 AND Wife_working > 0.5|3 (26.0/12.0)
Children <= 1.5 AND Husband_education <= 3.5|3 (19.0/7.0)
Wife_religion > 0.5 AND Wife_working > 0.5 AND Children > 2.5 AND Wife_age <= 44.5 AND Standard-of-living > 2.5 AND Standard-of-living <= 3.5 AND Husband_occupation <= 1.5|2 (14.0/3.0)
Wife_religion > 0.5 AND Standard-of-living > 3.5 AND Children <= 5.5 AND Wife_working > 0.5 AND Wife_education > 3.5|2 (88.0/52.0)
Wife_age <= 43.5 AND Standard-of-living > 3.5 AND Children <= 5.5 AND Children <= 4.5 AND Husband_occupation <= 2.5 AND Husband_education > 3.5 AND Wife_age <= 36.5|3 (59.0/30.0)
Wife_age <= 43.5 AND Husband_occupation > 2.5 AND Wife_education > 3.5|3 (24.0/13.0)
Husband_occupation > 2.5|2 (14.0/6.0)
Wife_religion <= 0.5 AND Standard-of-living > 3.5|1 (7.0/1.0)
Wife_working <= 0.5 AND Husband_occupation <= 1.5 AND Children > 1.5|2 (17.0/8.0)
Wife_working <= 0.5|1 (17.0/5.0)
Wife_religion <= 0.5 AND Children <= 1.5|1 (4.0/1.0)
Wife_religion > 0.5 AND Standard-of-living <= 2.5|2 (15.0/7.0)
Wife_religion > 0.5 AND Standard-of-living > 3.5 AND Wife_education <= 3.5|3 (6.0/2.0)
Standard-of-living > 3.5 AND Husband_occupation <= 1.5|2 (6.0/3.0)
Wife_religion > 0.5|3 (47.0/27.0)
|2 (3.0/1.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(86.0/1.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(123.0/113.0)
			* Children >= 2.5: 3(169.0/134.0)
		* Wife_age >= 37.5: 1(148.0/62.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Husband_occupation < 1.5: 1(51.0/66.0)
			* Husband_occupation >= 1.5: 3(53.0/43.0)
		* Children >= 2.5
			* Wife_age < 32.5: 3(32.0/31.0)
			* Wife_age >= 32.5: 2(116.0/97.0)


