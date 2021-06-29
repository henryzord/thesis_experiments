# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.425982 |
| Children >= 0.5 and Wife_education < 3.5 and Wife_age < 37.5 and Children >= 2.5 | 3 | 0.104851 |
| Children >= 0.5 and Wife_education >= 3.5 and Children >= 2.5 | 2 | 0.062382 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 0.5 and Children <= 2.5 | 3 | 0.031674 |
| Wife_age <= 31.5 and Wife_education > 3.5 and Children > 2.5 and Children <= 7.5 | 3 | 0.013621 |
| Wife_age > 31.5 and Wife_age <= 37.5 and Wife_education > 2.5 and Wife_education <= 3.5 and Children > 2.5 and Children <= 7.5 | 2 | 0.007890 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation <= 1 and Wife_age > 24 and Children > 1 | 2 | 0.006393 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age > 30 and Standard-of-living > 2 and Wife_age <= 41 and Children <= 7 and Standard-of-living > 3 and Wife_age <= 32 | 3 | 0.012750 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation <= 1 and Wife_age <= 24 and Wife_age > 20 | 2 | 0.006677 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion > 0 and Wife_age > 17 and Wife_age > 19 and Husband_occupation <= 3 and Standard-of-living <= 3 and Standard-of-living > 1 and Wife_age <= 28 and Wife_working > 0 and Husband_education <= 3 and Wife_age <= 24 and Standard-of-living <= 2 | 3 | 0.005184 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion > 0 and Wife_age > 17 and Wife_age > 19 and Husband_occupation <= 3 and Standard-of-living <= 3 and Standard-of-living <= 1 | 3 | 0.003609 |
| Wife_age > 37.5 and Wife_age <= 46.5 and Wife_education > 3.5 and Children > 7.5 | 3 | 0.002315 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education > 3 and Husband_education > 3 and Wife_age > 22 and Wife_age <= 28 and Wife_age <= 26 and Wife_age <= 25 and Standard-of-living > 3 | 2 | 0.002930 |
| Children >= 0.5 and Wife_education >= 3.5 and Children < 2.5 and Husband_occupation >= 1.5 | 3 | 0.033479 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion > 0 and Wife_age <= 17 | 3 | 0.002598 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age <= 30 and Wife_age > 22 and Husband_education > 2 and Husband_occupation <= 1 and Wife_working > 0 and Wife_age > 26 | 2 | 0.003680 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age > 30 and Children > 1 and Media_exposure <= 0 and Husband_education > 3 and Wife_working <= 0 | 2 | 0.002531 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion > 0 and Wife_age > 17 and Wife_age > 19 and Husband_occupation <= 3 and Standard-of-living <= 3 and Standard-of-living > 1 and Wife_age <= 28 and Wife_working > 0 and Husband_education <= 3 and Wife_age <= 24 and Standard-of-living > 2 and Husband_occupation > 2 and Children <= 1 | 3 | 0.002309 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion > 0 and Wife_age > 17 and Wife_age > 19 and Husband_occupation <= 3 and Standard-of-living <= 3 and Standard-of-living > 1 and Wife_age > 28 | 3 | 0.002309 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age > 30 and Standard-of-living > 2 and Wife_age > 41 and Wife_education > 3 and Children > 11 | 3 | 0.002309 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education > 3 and Husband_education > 3 and Wife_age > 22 and Wife_age > 28 and Children <= 1 | 2 | 0.001301 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age <= 30 and Wife_age > 22 and Husband_education <= 2 | 2 | 0.000977 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age > 30 and Standard-of-living > 2 and Wife_age <= 41 and Children > 7 | 3 | 0.006265 |
| Children > 0 and Wife_education > 2 and Children <= 2 and Wife_age <= 30 and Husband_occupation > 1 and Wife_education <= 3 and Wife_religion <= 0 | 2 | 0.001101 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age > 30 and Standard-of-living > 2 and Wife_age <= 41 and Children <= 7 and Standard-of-living <= 3 and Wife_working > 0 | 2 | 0.012568 |
| Children > 0 and Wife_education > 2 and Children > 2 and Wife_age > 30 and Standard-of-living > 2 and Wife_age <= 41 and Children <= 7 and Standard-of-living > 3 and Wife_age > 32 | 2 | 0.037683 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Children <= 0.5 | 1 | 0.099540 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 1.5 and Media_exposure <= 0.5 and Children <= 9.5 and Wife_age > 46.5 | 1 | 0.035166 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Media_exposure > 0.5 | 1 | 0.041905 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children > 1.5 and Children > 9.5 | 1 | 0.011719 |
| Wife_education <= 3.5 and Wife_age > 37.5 and Children <= 1.5 | 1 | 0.016904 |
| Wife_education <= 3.5 and Wife_age > 41.5 and Wife_age <= 45.5 and Husband_education > 2.5 and Children <= 3.5 | 1 | 0.005999 |
| Wife_education <= 3.5 and Wife_age > 41.5 and Wife_age <= 45.5 and Wife_education <= 1.5 | 1 | 0.010029 |
| Wife_education <= 3.5 and Children <= 2.5 and Wife_age > 30.5 | 1 | 0.023002 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Husband_education > 1.5 and Husband_occupation > 1.5 and Children > 2.5 and Wife_age <= 32.5 and Wife_age <= 24.5 and Wife_age > 21.5 | 3 | 0.014426 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Husband_occupation > 1.5 and Husband_education > 1.5 and Children > 2.5 and Wife_age <= 32.5 and Wife_age > 23 and Standard-of-living <= 2.5 and Media_exposure <= 0.5 | 3 | 0.023320 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Wife_age <= 25.5 and Wife_working > 0.5 and Husband_education <= 3.5 and Wife_age <= 20.5 | 1 | 0.009458 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Children <= 2.5 and Husband_occupation <= 3.5 and Standard-of-living <= 2.5 and Wife_age > 23.5 | 1 | 0.024191 |
| Wife_age <= 37.5 and Wife_education <= 2.5 and Standard-of-living <= 1.5 and Children <= 4.5 | 1 | 0.012878 |
| Wife_age <= 37.5 and Wife_education <= 3.5 and Husband_education <= 1.5 and Wife_education <= 1.5 | 1 | 0.003161 |
| Wife_age <= 37.5 and Husband_occupation > 1.5 and Wife_education <= 3.5 and Wife_working > 0.5 and Wife_education <= 1.5 | 3 | 0.026801 |
| Wife_age <= 37.5 and Husband_occupation > 1.5 and Wife_education > 3.5 and Wife_age <= 28.5 and Children > 1.5 | 3 | 0.034386 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Wife_working > 0.5 and Wife_age <= 23.5 and Standard-of-living <= 3.5 and Children > 1.5 and Husband_education > 3.5 | 1 | 0.007866 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Wife_working > 0.5 and Husband_occupation > 1.5 and Wife_age > 20.5 and Husband_education > 2.5 and Wife_age <= 24.5 and Standard-of-living > 2.5 and Husband_education > 3.5 | 3 | 0.006555 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Wife_working > 0.5 and Wife_age > 20.5 and Children > 1.5 and Wife_age > 23.5 and Standard-of-living > 2.5 and Children <= 7.5 and Wife_religion > 0.5 and Husband_education > 2.5 and Husband_occupation > 1.5 and Wife_age <= 35.5 and Children > 2.5 and Wife_education <= 2.5 | 3 | 0.036649 |
| Wife_education <= 3.5 and Wife_age <= 37.5 and Wife_working > 0.5 and Wife_age <= 24.5 and Husband_education <= 3.5 and Husband_education > 2.5 and Children > 1.5 | 1 | 0.009889 |
| Children <= 1.5 and Wife_age <= 31.5 and Husband_education <= 3.5 and Wife_working > 0.5 | 3 | 0.035788 |
| Children <= 1.5 and Wife_age <= 31.5 and Husband_education > 3.5 and Wife_age > 24.5 and Wife_age <= 28.5 | 1 | 0.017101 |
| Wife_age > 41.5 and Children > 1.5 and Wife_age <= 48.5 and Husband_education > 2.5 and Wife_religion <= 0.5 | 2 | 0.016043 |
| Wife_age > 41.5 and Children > 1.5 and Wife_age <= 48.5 and Husband_education > 2.5 and Wife_education > 3.5 and Wife_working <= 0.5 | 2 | 0.014328 |
| Wife_age > 41.5 and Children > 1.5 and Wife_age <= 47.5 and Husband_education > 2.5 and Wife_education <= 3.5 and Children <= 6.5 | 1 | 0.004998 |
| Wife_age > 44.5 and Children > 2 and Wife_age > 45.5 and Children <= 7.5 | 1 | 0.010663 |
| Wife_education > 3.5 and Wife_age > 44.5 and Children > 2 | 2 | 0.007983 |
| Wife_age > 43.5 and Children <= 3.5 | 1 | 0.014444 |
| Wife_education > 3.5 and Children > 3.5 and Wife_age > 30.5 and Children <= 7.5 and Wife_religion <= 0.5 | 2 | 0.023424 |
| Wife_education <= 2.5 and Wife_age <= 41.5 and Standard-of-living > 1.5 and Children > 1.5 and Wife_age > 37.5 | 1 | 0.012158 |
| Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Husband_education > 3.5 and Children > 5.5 and Wife_age > 37.5 | 2 | 0.012160 |
| Wife_education > 3.5 and Children > 2.5 and Wife_age > 28.5 and Husband_education > 3.5 and Children <= 5.5 and Standard-of-living > 3.5 and Wife_age > 32.5 and Wife_working > 0.5 and Wife_age <= 39.5 | 2 | 0.030388 |
| Wife_education <= 2.5 and Wife_age <= 41.5 and Standard-of-living > 1.5 and Children > 1.5 and Husband_education > 2.5 and Media_exposure <= 0.5 and Wife_age > 26.5 and Wife_age > 34.5 | 3 | 0.020785 |
| Children > 1.5 and Children > 7.5 and Standard-of-living <= 3.5 | 1 | 0.010924 |
| Children > 2.5 and Wife_age <= 32.5 and Husband_occupation > 2.5 and Husband_education > 2.5 and Wife_education <= 3.5 | 3 | 0.036739 |
| Children > 4.5 and Children <= 7.5 and Children <= 5.5 and Standard-of-living <= 3.5 and Husband_occupation <= 1.5 | 2 | 0.011494 |
| Children > 4.5 and Children <= 7.5 and Wife_education > 3.5 | 3 | 0.033918 |
| Wife_age > 40.5 and Children > 3.5 | 2 | 0.027047 |
| Wife_age > 36.5 and Children > 1.5 and Husband_education > 3.5 | 3 | 0.060433 |
| Wife_age <= 36.5 and Children > 4.5 and Wife_age <= 33.5 | 3 | 0.019490 |
| Wife_age <= 36.5 and Wife_education <= 2.5 and Wife_working <= 0.5 and Wife_age <= 34.5 | 1 | 0.027162 |
| Wife_age > 36.5 | 1 | 0.040716 |
| Standard-of-living > 3.5 and Children <= 4.5 and Wife_age <= 35.5 and Children > 1.5 and Children > 3.5 and Wife_age > 30.5 | 3 | 0.021429 |
| Wife_age > 35.5 | 2 | 0.043901 |
| Children <= 3.5 and Wife_education <= 2.5 and Husband_occupation <= 2.5 | 3 | 0.029859 |
| Wife_age > 29.5 and Standard-of-living > 3.5 and Wife_age > 30.5 and Husband_occupation <= 2.5 and Children > 2.5 | 3 | 0.066980 |
| Children > 3.5 and Husband_occupation <= 2.5 | 1 | 0.053608 |
| Children > 3.5 | 2 | 0.063640 |
| Wife_education <= 2.5 | 1 | 0.030625 |
| Husband_occupation > 1.5 and Wife_age <= 22.5 and Wife_age <= 21.5 and Standard-of-living <= 3.5 and Wife_education <= 3.5 | 1 | 0.008370 |
| Wife_age <= 29.5 and Wife_age <= 22.5 and Husband_occupation > 1.5 and Wife_age > 20.5 | 3 | 0.056818 |
| Wife_age <= 29.5 and Wife_religion <= 0.5 | 2 | 0.021531 |
| Wife_age <= 29.5 and Wife_age <= 23.5 and Wife_age > 20.5 and Husband_occupation <= 2.5 and Wife_age <= 22.5 | 2 | 0.031395 |
| Wife_age <= 29.5 and Wife_age <= 28.5 and Wife_age <= 27.5 and Wife_working > 0.5 and Husband_occupation > 1.5 | 2 | 0.044702 |
| Wife_age <= 23.5 | 1 | 0.028718 |
| Wife_religion <= 0.5 and Wife_age > 32.5 | 1 | 0.021397 |
| Husband_occupation > 1.5 and Wife_age > 26.5 and Husband_education > 3.5 and Children <= 2.5 | 3 | 0.104403 |
| Children <= 1.5 | 1 | 0.014865 |
| Wife_religion > 0.5 and Wife_age <= 26.5 and Children <= 2.5 | 3 | 0.184154 |
| Wife_age > 26.5 and Wife_religion > 0.5 and Husband_education > 3.5 and Husband_occupation <= 2.5 and Wife_age <= 29.5 | 2 | 0.071190 |
| Wife_age > 27 and Wife_religion > 0.5 and Standard-of-living > 2.5 and Husband_occupation <= 2.5 | 1 | 0.040936 |
| Wife_age > 27 | 2 | 0.177794 |
|  | 1 | 0.225000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Wife_age >= 33 and Wife_education >= 4 and Children >= 3 and Wife_age <= 42 | 2 | 0.048532 |
| Husband_occupation <= 1 and Children >= 3 and Wife_age >= 41 and Wife_age <= 46 | 2 | 0.010373 |
| Wife_age <= 37 and Children >= 3 | 3 | 0.163064 |
| Wife_age <= 22 and Children >= 1 and Wife_age >= 21 and Husband_occupation >= 2 | 3 | 0.027537 |
|  | 1 | 0.594937 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

wife_age|wife_education|children|contraceptive_method
---|---|---|---
(37.5-46.5]|(3.5-inf)|(7.5-inf)|3
(46.5-inf)|(3.5-inf)|(7.5-inf)|2
(37.5-46.5]|(2.5-3.5]|(7.5-inf)|1
(46.5-inf)|(2.5-3.5]|(7.5-inf)|1
(31.5-37.5]|(2.5-3.5]|(7.5-inf)|3
(-inf-31.5]|(-inf-2.5]|(7.5-inf)|1
(37.5-46.5]|(-inf-2.5]|(7.5-inf)|1
(46.5-inf)|(3.5-inf)|(2.5-7.5]|1
(31.5-37.5]|(-inf-2.5]|(7.5-inf)|1
(37.5-46.5]|(3.5-inf)|(2.5-7.5]|2
(46.5-inf)|(-inf-2.5]|(7.5-inf)|1
(-inf-31.5]|(3.5-inf)|(2.5-7.5]|3
(31.5-37.5]|(3.5-inf)|(2.5-7.5]|2
(46.5-inf)|(2.5-3.5]|(2.5-7.5]|1
(37.5-46.5]|(2.5-3.5]|(2.5-7.5]|1
(-inf-31.5]|(2.5-3.5]|(2.5-7.5]|3
(31.5-37.5]|(2.5-3.5]|(2.5-7.5]|2
(46.5-inf)|(3.5-inf)|(0.5-2.5]|1
(46.5-inf)|(-inf-2.5]|(2.5-7.5]|1
(37.5-46.5]|(3.5-inf)|(0.5-2.5]|1
(31.5-37.5]|(-inf-2.5]|(2.5-7.5]|3
(37.5-46.5]|(-inf-2.5]|(2.5-7.5]|1
(31.5-37.5]|(3.5-inf)|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(2.5-7.5]|3
(-inf-31.5]|(3.5-inf)|(0.5-2.5]|3
(46.5-inf)|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(2.5-3.5]|(0.5-2.5]|1
(31.5-37.5]|(2.5-3.5]|(0.5-2.5]|1
(-inf-31.5]|(2.5-3.5]|(0.5-2.5]|1
(37.5-46.5]|(3.5-inf)|(-inf-0.5]|1
(31.5-37.5]|(3.5-inf)|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(3.5-inf)|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(-inf-2.5]|(0.5-2.5]|1
(-inf-31.5]|(-inf-2.5]|(0.5-2.5]|1
(31.5-37.5]|(2.5-3.5]|(-inf-0.5]|1
(-inf-31.5]|(2.5-3.5]|(-inf-0.5]|1
(37.5-46.5]|(-inf-2.5]|(-inf-0.5]|1
(46.5-inf)|(-inf-2.5]|(-inf-0.5]|1
(31.5-37.5]|(-inf-2.5]|(-inf-0.5]|1
(-inf-31.5]|(-inf-2.5]|(-inf-0.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(Wife_age >= 33) and (Wife_education >= 4) and (Children >= 3) and (Wife_age <= 42)|2 (145.0/59.0)
(Husband_occupation <= 1) and (Children >= 3) and (Wife_age >= 41) and (Wife_age <= 46)|2 (44.0/21.0)
(Wife_age <= 37) and (Children >= 3)|3 (366.0/165.0)
(Wife_age <= 22) and (Children >= 1) and (Wife_age >= 21) and (Husband_occupation >= 2)|3 (56.0/21.0)
|1 (713.0/290.0)


## PART

Decision list:

rules | predicted class
---|---
Children <= 0.5|1 (86.0/1.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 1.5 AND Media_exposure <= 0.5 AND Children <= 9.5 AND Wife_age > 46.5|1 (37.0/5.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Media_exposure > 0.5|1 (39.0/3.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children > 1.5 AND Children > 9.5|1 (16.0/4.0)
Wife_education <= 3.5 AND Wife_age > 37.5 AND Children <= 1.5|1 (15.0/1.0)
Wife_education <= 3.5 AND Wife_age > 41.5 AND Wife_age <= 45.5 AND Husband_education > 2.5 AND Children <= 3.5|1 (13.0/5.0)
Wife_education <= 3.5 AND Wife_age > 41.5 AND Wife_age <= 45.5 AND Wife_education <= 1.5|1 (11.0/1.0)
Wife_education <= 3.5 AND Children <= 2.5 AND Wife_age > 30.5|1 (36.0/9.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Husband_education > 1.5 AND Husband_occupation > 1.5 AND Children > 2.5 AND Wife_age <= 32.5 AND Wife_age <= 24.5 AND Wife_age > 21.5|3 (21.0/7.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Husband_occupation > 1.5 AND Husband_education > 1.5 AND Children > 2.5 AND Wife_age <= 32.5 AND Wife_age > 23 AND Standard-of-living <= 2.5 AND Media_exposure <= 0.5|3 (37.0/13.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Children <= 2.5 AND Husband_occupation <= 3.5 AND Wife_age <= 25.5 AND Wife_working > 0.5 AND Husband_education <= 3.5 AND Wife_age <= 20.5|1 (21.0/9.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Children <= 2.5 AND Husband_occupation <= 3.5 AND Standard-of-living <= 2.5 AND Wife_age > 23.5|1 (41.0/14.0)
Wife_age <= 37.5 AND Wife_education <= 2.5 AND Standard-of-living <= 1.5 AND Children <= 4.5|1 (13.0/3.0)
Wife_age <= 37.5 AND Wife_education <= 3.5 AND Husband_education <= 1.5 AND Wife_education <= 1.5|1 (7.0/3.0)
Wife_age <= 37.5 AND Husband_occupation > 1.5 AND Wife_education <= 3.5 AND Wife_working > 0.5 AND Wife_education <= 1.5|3 (21.0/4.0)
Wife_age <= 37.5 AND Husband_occupation > 1.5 AND Wife_education > 3.5 AND Wife_age <= 28.5 AND Children > 1.5|3 (38.0/10.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Wife_working > 0.5 AND Wife_age <= 23.5 AND Standard-of-living <= 3.5 AND Children > 1.5 AND Husband_education > 3.5|1 (10.0/4.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Wife_working > 0.5 AND Husband_occupation > 1.5 AND Wife_age > 20.5 AND Husband_education > 2.5 AND Wife_age <= 24.5 AND Standard-of-living > 2.5 AND Husband_education > 3.5|3 (12.0/6.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Wife_working > 0.5 AND Wife_age > 20.5 AND Children > 1.5 AND Wife_age > 23.5 AND Standard-of-living > 2.5 AND Children <= 7.5 AND Wife_religion > 0.5 AND Husband_education > 2.5 AND Husband_occupation > 1.5 AND Wife_age <= 35.5 AND Children > 2.5 AND Wife_education <= 2.5|3 (30.0/4.0)
Wife_education <= 3.5 AND Wife_age <= 37.5 AND Wife_working > 0.5 AND Wife_age <= 24.5 AND Husband_education <= 3.5 AND Husband_education > 2.5 AND Children > 1.5|1 (12.0/4.0)
Children <= 1.5 AND Wife_age <= 31.5 AND Husband_education <= 3.5 AND Wife_working > 0.5|3 (23.0/6.0)
Children <= 1.5 AND Wife_age <= 31.5 AND Husband_education > 3.5 AND Wife_age > 24.5 AND Wife_age <= 28.5|1 (42.0/21.0)
Wife_age > 41.5 AND Children > 1.5 AND Wife_age <= 48.5 AND Husband_education > 2.5 AND Wife_religion <= 0.5|2 (23.0/8.0)
Wife_age > 41.5 AND Children > 1.5 AND Wife_age <= 48.5 AND Husband_education > 2.5 AND Wife_education > 3.5 AND Wife_working <= 0.5|2 (15.0/4.0)
Wife_age > 41.5 AND Children > 1.5 AND Wife_age <= 47.5 AND Husband_education > 2.5 AND Wife_education <= 3.5 AND Children <= 6.5|1 (14.0/6.0)
Wife_age > 44.5 AND Children > 2 AND Wife_age > 45.5 AND Children <= 7.5|1 (20.0/8.0)
Wife_education > 3.5 AND Wife_age > 44.5 AND Children > 2|2 (11.0/5.0)
Wife_age > 43.5 AND Children <= 3.5|1 (13.0/1.0)
Wife_education > 3.5 AND Children > 3.5 AND Wife_age > 30.5 AND Children <= 7.5 AND Wife_religion <= 0.5|2 (22.0/4.0)
Wife_education <= 2.5 AND Wife_age <= 41.5 AND Standard-of-living > 1.5 AND Children > 1.5 AND Wife_age > 37.5|1 (20.0/8.0)
Wife_education > 3.5 AND Children > 2.5 AND Wife_age > 28.5 AND Husband_education > 3.5 AND Children > 5.5 AND Wife_age > 37.5|2 (14.0/4.0)
Wife_education > 3.5 AND Children > 2.5 AND Wife_age > 28.5 AND Husband_education > 3.5 AND Children <= 5.5 AND Standard-of-living > 3.5 AND Wife_age > 32.5 AND Wife_working > 0.5 AND Wife_age <= 39.5|2 (49.0/21.0)
Wife_education <= 2.5 AND Wife_age <= 41.5 AND Standard-of-living > 1.5 AND Children > 1.5 AND Husband_education > 2.5 AND Media_exposure <= 0.5 AND Wife_age > 26.5 AND Wife_age > 34.5|3 (18.0/7.0)
Children > 1.5 AND Children > 7.5 AND Standard-of-living <= 3.5|1 (19.0/9.0)
Children > 2.5 AND Wife_age <= 32.5 AND Husband_occupation > 2.5 AND Husband_education > 2.5 AND Wife_education <= 3.5|3 (28.0/5.0)
Children > 4.5 AND Children <= 7.5 AND Children <= 5.5 AND Standard-of-living <= 3.5 AND Husband_occupation <= 1.5|2 (11.0/3.0)
Children > 4.5 AND Children <= 7.5 AND Wife_education > 3.5|3 (20.0/7.0)
Wife_age > 40.5 AND Children > 3.5|2 (13.0/4.0)
Wife_age > 36.5 AND Children > 1.5 AND Husband_education > 3.5|3 (44.0/25.0)
Wife_age <= 36.5 AND Children > 4.5 AND Wife_age <= 33.5|3 (25.0/11.0)
Wife_age <= 36.5 AND Wife_education <= 2.5 AND Wife_working <= 0.5 AND Wife_age <= 34.5|1 (21.0/6.0)
Wife_age > 36.5|1 (16.0/5.0)
Standard-of-living > 3.5 AND Children <= 4.5 AND Wife_age <= 35.5 AND Children > 1.5 AND Children > 3.5 AND Wife_age > 30.5|3 (9.0/3.0)
Wife_age > 35.5|2 (21.0/11.0)
Children <= 3.5 AND Wife_education <= 2.5 AND Husband_occupation <= 2.5|3 (13.0/4.0)
Wife_age > 29.5 AND Standard-of-living > 3.5 AND Wife_age > 30.5 AND Husband_occupation <= 2.5 AND Children > 2.5|3 (19.0/5.0)
Children > 3.5 AND Husband_occupation <= 2.5|1 (24.0/10.0)
Children > 3.5|2 (18.0/7.0)
Wife_education <= 2.5|1 (10.0/5.0)
Husband_occupation > 1.5 AND Wife_age <= 22.5 AND Wife_age <= 21.5 AND Standard-of-living <= 3.5 AND Wife_education <= 3.5|1 (9.0/4.0)
Wife_age <= 29.5 AND Wife_age <= 22.5 AND Husband_occupation > 1.5 AND Wife_age > 20.5|3 (13.0/3.0)
Wife_age <= 29.5 AND Wife_religion <= 0.5|2 (12.0/4.0)
Wife_age <= 29.5 AND Wife_age <= 23.5 AND Wife_age > 20.5 AND Husband_occupation <= 2.5 AND Wife_age <= 22.5|2 (9.0/2.0)
Wife_age <= 29.5 AND Wife_age <= 28.5 AND Wife_age <= 27.5 AND Wife_working > 0.5 AND Husband_occupation > 1.5|2 (23.0/11.0)
Wife_age <= 23.5|1 (14.0/7.0)
Wife_religion <= 0.5 AND Wife_age > 32.5|1 (14.0/6.0)
Husband_occupation > 1.5 AND Wife_age > 26.5 AND Husband_education > 3.5 AND Children <= 2.5|3 (18.0/6.0)
Children <= 1.5|1 (19.0/10.0)
Wife_religion > 0.5 AND Wife_age <= 26.5 AND Children <= 2.5|3 (12.0/5.0)
Wife_age > 26.5 AND Wife_religion > 0.5 AND Husband_education > 3.5 AND Husband_occupation <= 2.5 AND Wife_age <= 29.5|2 (24.0/10.0)
Wife_age > 27 AND Wife_religion > 0.5 AND Standard-of-living > 2.5 AND Husband_occupation <= 2.5|1 (21.0/12.0)
Wife_age > 27|2 (19.0/8.0)
|1 (6.0/2.0)


## J48 Decision Tree

* Children <= 0: 1 (57.0/1.0)
* Children > 0
	* Wife_education <= 2
		* Wife_age <= 37
			* Children <= 2: 1 (74.0/28.0)
			* Children > 2
				* Husband_education <= 3
					* Wife_age <= 30
						* Wife_age <= 20: 1 (3.0)
						* Wife_age > 20
							* Husband_education <= 1: 1 (4.0/1.0)
							* Husband_education > 1: 3 (35.0/13.0)
					* Wife_age > 30: 3 (52.0/28.0)
				* Husband_education > 3: 3 (27.0/6.0)
		* Wife_age > 37: 1 (81.0/14.0)
	* Wife_education > 2
		* Children <= 2
			* Wife_age <= 30
				* Husband_occupation <= 1
					* Wife_age <= 24
						* Wife_age <= 20: 1 (2.0/1.0)
						* Wife_age > 20: 2 (13.0/4.0)
					* Wife_age > 24
						* Children <= 1: 1 (16.0/7.0)
						* Children > 1: 2 (17.0/9.0)
				* Husband_occupation > 1
					* Wife_education <= 3
						* Wife_religion <= 0: 2 (4.0/2.0)
						* Wife_religion > 0
							* Wife_age <= 17: 3 (2.0)
							* Wife_age > 17
								* Wife_age <= 19: 1 (5.0/1.0)
								* Wife_age > 19
									* Husband_occupation <= 3
										* Standard-of-living <= 3
											* Standard-of-living <= 1: 3 (6.0/3.0)
											* Standard-of-living > 1
												* Wife_age <= 28
													* Wife_working <= 0: 1 (4.0/1.0)
													* Wife_working > 0
														* Husband_education <= 3
															* Wife_age <= 24
																* Standard-of-living <= 2: 3 (4.0)
																* Standard-of-living > 2
																	* Husband_occupation <= 2: 1 (2.0/1.0)
																	* Husband_occupation > 2
																		* Children <= 1: 3 (2.0)
																		* Children > 1: 1 (2.0/1.0)
															* Wife_age > 24: 1 (4.0/1.0)
														* Husband_education > 3: 1 (9.0/4.0)
												* Wife_age > 28: 3 (2.0)
										* Standard-of-living > 3: 1 (16.0/9.0)
									* Husband_occupation > 3: 1 (2.0/1.0)
					* Wife_education > 3
						* Husband_education <= 3: 3 (5.0)
						* Husband_education > 3
							* Wife_age <= 22: 3 (14.0/4.0)
							* Wife_age > 22
								* Wife_age <= 28
									* Wife_age <= 26
										* Wife_age <= 25
											* Standard-of-living <= 3: 1 (13.0/7.0)
											* Standard-of-living > 3: 2 (10.0/6.0)
										* Wife_age > 25: 3 (5.0/1.0)
									* Wife_age > 26
										* Wife_age <= 27: 1 (3.0/1.0)
										* Wife_age > 27: 3 (3.0/1.0)
								* Wife_age > 28
									* Children <= 1: 2 (2.0/1.0)
									* Children > 1: 3 (2.0)
			* Wife_age > 30
				* Children <= 1: 1 (27.0/5.0)
				* Children > 1
					* Media_exposure <= 0
						* Husband_education <= 3: 1 (4.0/2.0)
						* Husband_education > 3
							* Wife_working <= 0: 2 (9.0/5.0)
							* Wife_working > 0: 1 (20.0/9.0)
					* Media_exposure > 0: 1 (2.0)
		* Children > 2
			* Wife_age <= 30
				* Wife_age <= 22: 3 (4.0)
				* Wife_age > 22
					* Husband_education <= 2: 2 (3.0/1.0)
					* Husband_education > 2
						* Husband_occupation <= 1
							* Wife_working <= 0: 1 (2.0/1.0)
							* Wife_working > 0
								* Wife_age <= 26: 1 (6.0/3.0)
								* Wife_age > 26: 2 (13.0/6.0)
						* Husband_occupation > 1: 3 (50.0/16.0)
			* Wife_age > 30
				* Standard-of-living <= 2: 1 (29.0/15.0)
				* Standard-of-living > 2
					* Wife_age <= 41
						* Children <= 7
							* Standard-of-living <= 3
								* Wife_working <= 0
									* Wife_religion <= 0: 1 (2.0)
									* Wife_religion > 0
										* Wife_age <= 33: 1 (4.0/2.0)
										* Wife_age > 33: 2 (4.0)
								* Wife_working > 0: 2 (23.0/10.0)
							* Standard-of-living > 3
								* Wife_age <= 32: 3 (18.0/6.0)
								* Wife_age > 32: 2 (80.0/36.0)
						* Children > 7: 3 (8.0/2.0)
					* Wife_age > 41
						* Wife_education <= 3: 1 (22.0/10.0)
						* Wife_education > 3
							* Children <= 11
								* Wife_age <= 47: 2 (38.0/21.0)
								* Wife_age > 47
									* Wife_age <= 48: 2 (7.0/1.0)
									* Wife_age > 48: 1 (4.0/1.0)
							* Children > 11: 3 (2.0)


## SimpleCart Decision Tree

* Children < 0.5: 1(85.0/1.0)
* Children >= 0.5
	* Wife_education < 3.5
		* Wife_age < 37.5
			* Children < 2.5: 1(122.0/113.0)
			* Children >= 2.5: 3(169.0/134.0)
		* Wife_age >= 37.5: 1(149.0/62.0)
	* Wife_education >= 3.5
		* Children < 2.5
			* Husband_occupation < 1.5: 1(51.0/66.0)
			* Husband_occupation >= 1.5: 3(53.0/43.0)
		* Children >= 2.5: 2(132.0/144.0)


