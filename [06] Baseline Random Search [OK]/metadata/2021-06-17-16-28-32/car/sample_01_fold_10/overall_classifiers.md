# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.700772 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.021010 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.011999 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.014605 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.012238 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.007401 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009836 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.009836 |
| Buying = low and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009836 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009024 |
| Safety = high and Persons = more and Buying = high and Maint = med | acc | 0.008279 |
| Buying = high and Maint = high and Persons = more and Safety = high | acc | 0.007470 |
| Safety = high and Persons = more and Buying = med and Maint = vhigh | acc | 0.007470 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.008210 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.007470 |
| Buying = high and Maint = med and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = high and Maint = low and Persons = 4 and Safety = high | acc | 0.008210 |
| Buying = low and Maint = vhigh and Persons = more and Safety = high | acc | 0.007470 |
| Safety = high and Persons = more and Buying = low | vgood | 0.005510 |
| Safety = high and Persons = more and Buying = med and Maint = high | acc | 0.006661 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.006661 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.007395 |
| Safety = high and Persons = more and Buying = vhigh and Maint = low | acc | 0.006661 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002976 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = low and Maint = low and Persons = 4 and Safety = med | good | 0.001673 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.002730 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002406 |
| Safety = high and Persons = more and Buying = med and Maint = med | vgood | 0.002728 |
| Buying = med and Maint = med and Persons = 4 and Safety = high | acc | 0.002707 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002188 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.008279 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.007470 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | vgood | 0.002188 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.002188 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | good | 0.001673 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | vgood | 0.001672 |
| Buying = high and Maint = med and Persons = 4 and Safety = med | acc | 0.002707 |
| Buying = high and Maint = low and Persons = 4 and Safety = med | acc | 0.002483 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | vgood | 0.001857 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.529828 |
| Persons = 2 | unacc | 0.421642 |
| Buying = vhigh and Maint = high | unacc | 0.086444 |
| Buying = high and Maint = vhigh | unacc | 0.086444 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045175 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.043210 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.093220 |
| Safety = med and Maint = vhigh and Lug_boot = small | unacc | 0.030635 |
| Buying = high and Doors = 4 | acc | 0.118943 |
| Buying = high and Safety = high and Doors = 3 | acc | 0.074074 |
| Safety = med and Maint = high and Buying = med | unacc | 0.021183 |
| Buying = high and Doors = 5more | acc | 0.116822 |
| Buying = high and Lug_boot = big | acc | 0.064356 |
| Buying = vhigh and Maint = vhigh | unacc | 0.083544 |
| Safety = med and Lug_boot = small and Doors = 2 | unacc | 0.007652 |
| Safety = med and Lug_boot = small | acc | 0.170330 |
| Safety = med and Buying = vhigh and Lug_boot = big | acc | 0.095808 |
| Safety = med and Buying = med and Maint = vhigh | acc | 0.054358 |
| Safety = med and Buying = med and Maint = med | acc | 0.084848 |
| Safety = med and Buying = low and Maint = med | good | 0.035424 |
| Maint = vhigh and Doors = 5more | acc | 0.103226 |
| Buying = vhigh and Safety = high and Lug_boot = big | acc | 0.097403 |
| Maint = vhigh and Safety = high and Persons = 4 | acc | 0.114650 |
| Lug_boot = big and Safety = high and Maint = med | vgood | 0.069124 |
| Buying = vhigh and Doors = 2 | unacc | 0.011682 |
| Buying = vhigh and Safety = high | acc | 0.161972 |
| Maint = vhigh and Doors = 2 | acc | 0.019260 |
| Maint = vhigh and Doors = 3 | acc | 0.051200 |
| Maint = high and Buying = med and Persons = 4 | acc | 0.091603 |
| Buying = high and Safety = med | unacc | 0.039244 |
| Lug_boot = big and Safety = med | good | 0.082770 |
| Lug_boot = big and Maint = low | vgood | 0.100000 |
| Lug_boot = small and Maint = high | acc | 0.086430 |
| Lug_boot = big | vgood | 0.036467 |
| Lug_boot = small and Doors = 2 | unacc | 0.060020 |
| Lug_boot = small and Maint = med | acc | 0.070330 |
| Lug_boot = med and Safety = med and Buying = low | acc | 0.133333 |
| Lug_boot = small | good | 0.186207 |
| Safety = med and Buying = vhigh | acc | 0.152830 |
| Doors = 2 | acc | 0.188127 |
| Maint = med | vgood | 0.122727 |
| Buying = med | good | 0.073463 |
|  | vgood | 0.276596 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.005750 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.005371 |
| Safety = high and Buying = med and Lug_boot = big and Maint = med | vgood | 0.003558 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.002852 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.003269 |
| Safety = high and Lug_boot = med and Buying = med | vgood | 0.001037 |
| Buying = low and Safety = high and Persons = 4 and Lug_boot = med | vgood | 0.001609 |
| Buying = low and Safety = med and Lug_boot = big and Maint = low | good | 0.003706 |
| Buying = low and Maint = med and Safety = med and Lug_boot = big | good | 0.003405 |
| Maint = low and Buying = med and Safety = high | good | 0.002826 |
| Buying = low and Safety = high and Persons = 4 | good | 0.002183 |
| Maint = low and Buying = med and Safety = med and Persons = more | good | 0.002505 |
| Buying = low and Persons = more and Safety = high | good | 0.001376 |
| Safety = med and Buying = low and Lug_boot = med and Persons = more | good | 0.001794 |
| Persons = 4 and Safety = med and Maint = low and Buying = med | good | 0.001585 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.022381 |
| Safety = med and Lug_boot = big and Persons = more and Buying = med | acc | 0.010870 |
| Safety = high and Persons = more and Maint = med and Lug_boot = big | acc | 0.007273 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = med | acc | 0.009973 |
| Safety = high and Persons = more and Maint = low and Lug_boot = med | acc | 0.007273 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009973 |
| Safety = high and Persons = 4 and Maint = low | acc | 0.018868 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.007273 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = low | acc | 0.007273 |
| Persons = more and Safety = high and Buying = med and Lug_boot = big | acc | 0.006369 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.007273 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.010105 |
| Persons = more and Safety = high and Maint = med and Lug_boot = med | acc | 0.007273 |
| Persons = more and Safety = high and Maint = low and Lug_boot = big | acc | 0.006369 |
| Safety = med and Persons = more and Buying = low and Lug_boot = big | acc | 0.006369 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med | acc | 0.008257 |
| Safety = high and Buying = med and Persons = 4 | acc | 0.019749 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.006369 |
| Persons = more and Safety = high and Buying = med | acc | 0.010736 |
| Buying = high and Maint = high and Safety = high and Persons = 4 | acc | 0.010870 |
| Safety = med and Persons = more and Buying = low | acc | 0.008493 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.005464 |
| Persons = more and Safety = high and Buying = high and Maint = high | acc | 0.008257 |
| Safety = med and Lug_boot = med and Persons = more and Maint = low | acc | 0.004106 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more | acc | 0.003732 |
| Safety = med and Persons = more and Buying = med | acc | 0.003093 |
| Buying = high and Maint = high and Safety = med and Lug_boot = big | acc | 0.005829 |
| Persons = more and Safety = high and Maint = med | acc | 0.002541 |
| Safety = med and Lug_boot = med and Doors = 4 and Persons = 4 | acc | 0.003653 |
|  | unacc | 0.958627 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
med|low|more|high|vgood
high|low|more|high|acc
vhigh|low|more|high|acc
med|med|more|high|vgood
low|med|more|high|vgood
high|med|more|high|acc
vhigh|med|more|high|acc
low|high|more|high|vgood
vhigh|low|4|high|acc
med|high|more|high|acc
high|low|4|high|acc
low|low|4|high|vgood
med|low|4|high|good
high|high|more|high|acc
vhigh|high|more|high|unacc
high|vhigh|more|high|unacc
med|low|more|med|good
vhigh|low|more|med|unacc
high|low|more|med|acc
med|med|4|high|acc
low|med|4|high|vgood
low|low|more|med|good
med|vhigh|more|high|acc
high|med|4|high|acc
low|vhigh|more|high|acc
vhigh|med|4|high|acc
vhigh|vhigh|more|high|unacc
med|high|4|high|acc
low|med|more|med|good
high|low|2|high|unacc
low|low|2|high|unacc
vhigh|low|2|high|unacc
high|high|4|high|acc
low|high|4|high|vgood
high|med|more|med|acc
med|low|2|high|unacc
med|med|more|med|acc
vhigh|med|more|med|acc
vhigh|high|4|high|unacc
med|low|4|med|acc
med|vhigh|4|high|acc
med|med|2|high|unacc
vhigh|low|4|med|unacc
low|vhigh|4|high|acc
low|low|4|med|good
high|high|more|med|acc
vhigh|vhigh|4|high|unacc
high|med|2|high|unacc
vhigh|high|more|med|unacc
high|vhigh|4|high|unacc
low|high|more|med|acc
high|low|4|med|acc
med|high|more|med|acc
low|med|2|high|unacc
vhigh|med|2|high|unacc
med|low|more|low|unacc
vhigh|low|more|low|unacc
low|vhigh|more|med|acc
med|med|4|med|acc
med|vhigh|more|med|acc
low|high|2|high|unacc
vhigh|med|4|med|acc
low|med|4|med|acc
med|high|2|high|unacc
high|low|more|low|unacc
low|low|more|low|unacc
high|med|4|med|acc
high|high|2|high|unacc
high|vhigh|more|med|unacc
vhigh|high|2|high|unacc
vhigh|vhigh|more|med|unacc
med|low|2|med|unacc
vhigh|high|4|med|unacc
high|vhigh|2|high|unacc
high|high|4|med|unacc
low|high|4|med|acc
med|med|more|low|unacc
low|low|2|med|unacc
low|vhigh|2|high|unacc
high|med|more|low|unacc
low|med|more|low|unacc
med|high|4|med|unacc
med|vhigh|2|high|unacc
high|low|2|med|unacc
vhigh|low|2|med|unacc
vhigh|vhigh|2|high|unacc
vhigh|med|more|low|unacc
low|med|2|med|unacc
high|med|2|med|unacc
vhigh|low|4|low|unacc
vhigh|vhigh|4|med|unacc
med|high|more|low|unacc
vhigh|med|2|med|unacc
vhigh|high|more|low|unacc
high|high|more|low|unacc
high|low|4|low|unacc
low|vhigh|4|med|acc
med|low|4|low|unacc
med|vhigh|4|med|unacc
high|vhigh|4|med|unacc
med|med|2|med|unacc
low|high|more|low|unacc
low|low|4|low|unacc
med|high|2|med|unacc
high|high|2|med|unacc
low|high|2|med|unacc
med|vhigh|more|low|unacc
vhigh|high|2|med|unacc
high|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
vhigh|med|4|low|unacc
low|med|4|low|unacc
low|vhigh|more|low|unacc
med|med|4|low|unacc
high|med|4|low|unacc
low|high|4|low|unacc
high|low|2|low|unacc
low|vhigh|2|med|unacc
med|low|2|low|unacc
vhigh|vhigh|2|med|unacc
high|vhigh|2|med|unacc
vhigh|low|2|low|unacc
high|high|4|low|unacc
vhigh|high|4|low|unacc
low|low|2|low|unacc
med|high|4|low|unacc
med|vhigh|2|med|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
vhigh|vhigh|4|low|unacc
low|med|2|low|unacc
vhigh|med|2|low|unacc
high|vhigh|4|low|unacc
med|vhigh|4|low|unacc
med|med|2|low|unacc
med|high|2|low|unacc
vhigh|high|2|low|unacc
low|high|2|low|unacc
high|high|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
low|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (14.0/3.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Lug_boot = big) and (Maint = med)|vgood (12.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (15.0/7.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (10.0/3.0)
(Safety = high) and (Lug_boot = med) and (Buying = med)|vgood (42.0/34.0)
(Buying = low) and (Safety = high) and (Persons = 4) and (Lug_boot = med)|vgood (15.0/9.0)
(Buying = low) and (Safety = med) and (Lug_boot = big) and (Maint = low)|good (12.0/4.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Lug_boot = big)|good (10.0/3.0)
(Maint = low) and (Buying = med) and (Safety = high)|good (12.0/5.0)
(Buying = low) and (Safety = high) and (Persons = 4)|good (13.0/7.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = more)|good (10.0/4.0)
(Buying = low) and (Persons = more) and (Safety = high)|good (15.0/10.0)
(Safety = med) and (Buying = low) and (Lug_boot = med) and (Persons = more)|good (14.0/8.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Buying = med)|good (11.0/6.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (23.0/0.0)
(Safety = med) and (Lug_boot = big) and (Persons = more) and (Buying = med)|acc (12.0/0.0)
(Safety = high) and (Persons = more) and (Maint = med) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Safety = high) and (Persons = more) and (Maint = low) and (Lug_boot = med)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (11.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = low)|acc (21.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (26.0/9.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Lug_boot = med)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med)|acc (10.0/1.0)
(Safety = high) and (Buying = med) and (Persons = 4)|acc (14.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (11.0/3.0)
(Buying = high) and (Maint = high) and (Safety = high) and (Persons = 4)|acc (12.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (14.0/6.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = high)|acc (11.0/1.0)
(Safety = med) and (Lug_boot = med) and (Persons = more) and (Maint = low)|acc (7.0/2.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 5more)|acc (10.0/3.0)
(Safety = med) and (Persons = more) and (Buying = med)|acc (16.0/10.0)
(Buying = high) and (Maint = high) and (Safety = med) and (Lug_boot = big)|acc (10.0/2.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (7.0/2.0)
(Safety = med) and (Lug_boot = med) and (Doors = 4) and (Persons = 4)|acc (8.0/2.0)
|unacc (1019.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (524.0)
Persons = 2|unacc (339.0)
Buying = vhigh AND Maint = high|unacc (44.0)
Buying = high AND Maint = vhigh|unacc (44.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (21.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (22.0)
Safety = med AND Maint = vhigh AND Lug_boot = small|unacc (14.0)
Buying = high AND Doors = 4|acc (27.0)
Buying = high AND Safety = high AND Doors = 3|acc (16.0)
Safety = med AND Maint = high AND Buying = med|unacc (14.0/3.0)
Buying = high AND Doors = 5more|acc (25.0)
Buying = high AND Lug_boot = big|acc (13.0)
Buying = vhigh AND Maint = vhigh|unacc (33.0)
Safety = med AND Lug_boot = small AND Doors = 2|unacc (9.0/4.0)
Safety = med AND Lug_boot = small|acc (27.0)
Safety = med AND Buying = vhigh AND Lug_boot = big|acc (16.0)
Safety = med AND Buying = med AND Maint = vhigh|acc (14.0/3.0)
Safety = med AND Buying = med AND Maint = med|acc (14.0)
Safety = med AND Buying = low AND Maint = med|good (15.0/3.0)
Maint = vhigh AND Doors = 5more|acc (16.0)
Buying = vhigh AND Safety = high AND Lug_boot = big|acc (15.0)
Maint = vhigh AND Safety = high AND Persons = 4|acc (18.0)
Lug_boot = big AND Safety = high AND Maint = med|vgood (15.0)
Buying = vhigh AND Doors = 2|unacc (10.0/5.0)
Buying = vhigh AND Safety = high|acc (18.0)
Maint = vhigh AND Doors = 2|acc (9.0/4.0)
Maint = vhigh AND Doors = 3|acc (9.0/1.0)
Maint = high AND Buying = med AND Persons = 4|acc (10.0)
Buying = high AND Safety = med|unacc (12.0/3.0)
Lug_boot = big AND Safety = med|good (16.0/2.0)
Lug_boot = big AND Maint = low|vgood (14.0)
Lug_boot = small AND Maint = high|acc (13.0/3.0)
Lug_boot = big|vgood (13.0/5.0)
Lug_boot = small AND Doors = 2|unacc (11.0/5.0)
Lug_boot = small AND Maint = med|acc (11.0/5.0)
Lug_boot = med AND Safety = med AND Buying = low|acc (15.0/4.0)
Lug_boot = small|good (12.0/1.0)
Safety = med AND Buying = vhigh|acc (10.0/1.0)
Doors = 2|acc (17.0/4.0)
Maint = med|vgood (11.0/2.0)
Buying = med|good (14.0/8.0)
|vgood (12.0/3.0)


## J48 Decision Tree

* Safety = low: unacc (418.0)
* Safety = med
	* Persons = 2: unacc (135.0)
	* Persons = 4
		* Buying = vhigh: unacc (37.0/9.0)
		* Buying = high
			* Lug_boot = small: unacc (13.0)
			* Lug_boot = med: unacc (13.0/4.0)
			* Lug_boot = big: acc (10.0/3.0)
		* Buying = med: acc (37.0/15.0)
		* Buying = low: acc (39.0/14.0)
	* Persons = more
		* Lug_boot = small: unacc (46.0/11.0)
		* Lug_boot = med: acc (44.0/20.0)
		* Lug_boot = big: acc (48.0/17.0)
* Safety = high
	* Persons = 2: unacc (130.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (8.0)
			* Maint = high: unacc (10.0)
			* Maint = med: acc (8.0)
			* Maint = low: acc (8.0)
		* Buying = high
			* Maint = vhigh: unacc (9.0)
			* Maint = high: acc (12.0)
			* Maint = med: acc (7.0)
			* Maint = low: acc (8.0)
		* Buying = med
			* Maint = vhigh: acc (10.0)
			* Maint = high: acc (8.0)
			* Maint = med: acc (9.0/3.0)
			* Maint = low: vgood (8.0/4.0)
		* Buying = low
			* Maint = vhigh: acc (8.0)
			* Maint = high: vgood (8.0/3.0)
			* Maint = med: vgood (8.0/3.0)
			* Maint = low: vgood (7.0/2.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (8.0)
			* Maint = high: unacc (8.0)
			* Maint = med: acc (9.0/1.0)
			* Maint = low: acc (8.0/1.0)
		* Buying = high
			* Maint = vhigh: unacc (10.0)
			* Maint = high: acc (9.0/1.0)
			* Maint = med: acc (7.0/1.0)
			* Maint = low: acc (8.0/1.0)
		* Buying = med
			* Maint = vhigh: acc (8.0/1.0)
			* Maint = high: acc (8.0)
			* Maint = med: vgood (10.0/4.0)
			* Maint = low: vgood (9.0/5.0)
		* Buying = low: vgood (36.0/20.0)


