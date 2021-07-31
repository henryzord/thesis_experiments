# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.607497 |
| Persons != more | unacc | 0.600157 |
| Safety = med and Persons = more and Lug_boot = big | acc | 0.018005 |
| Safety = med and Persons = 4 and Buying = med | acc | 0.013919 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.013225 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.009844 |
| Buying = vhigh and Maint = low and Persons = 4 and Safety = high | acc | 0.009844 |
| Safety = high and Persons = 4 and Buying = high and Maint = high | acc | 0.009844 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.008285 |
| Buying = med and Maint = vhigh and Persons = more and Safety = high | acc | 0.008285 |
| Buying = vhigh and Maint = med and Persons = 4 and Safety = high | acc | 0.009031 |
| Buying = med and Maint = high and Persons = more and Safety = high | acc | 0.008285 |
| Safety = high and Persons = more and Buying = low and Maint = vhigh | acc | 0.007476 |
| Safety = high and Persons = more and Buying = high and Maint = high | acc | 0.007476 |
| Buying = high and Maint = med and Persons = more and Safety = high | acc | 0.007476 |
| Safety = med and Persons = 4 and Buying = high and Lug_boot = big | acc | 0.006859 |
| Buying = vhigh and Maint = low and Persons = more and Safety = high | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.008217 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.008217 |
| Safety = high and Persons = 4 and Buying = high and Maint = low | acc | 0.007401 |
| Buying = vhigh and Maint = med and Persons = more and Safety = high | acc | 0.006667 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 3 | acc | 0.005889 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 5more | acc | 0.004069 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 4 | acc | 0.003781 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | good | 0.001676 |
| Buying = med and Maint = med and Persons = more and Safety = high | vgood | 0.002730 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002733 |
| Safety = high and Persons = more and Buying = low and Maint = high | vgood | 0.002730 |
| Buying = med and Maint = low and Persons = more and Safety = med | good | 0.002733 |
| Buying = med and Maint = med and Persons = more and Safety = med | acc | 0.006667 |
| Safety = high and Persons = more and Buying = med and Maint = low | vgood | 0.002189 |
| Safety = high and Persons = more and Buying = low and Maint = low | vgood | 0.002089 |
| Safety = high and Persons = 4 and Buying = med and Maint = med | acc | 0.002486 |
| Buying = low and Maint = low and Persons = more and Safety = med | good | 0.001861 |
| Buying = low and Maint = high and Persons = more and Safety = med | acc | 0.004243 |
| Safety = high and Persons = 4 and Buying = low and Maint = low | vgood | 0.002189 |
| Buying = med and Maint = low and Persons = 4 and Safety = high | vgood | 0.002189 |
| Safety = high and Persons = 4 and Buying = med and Maint = low | good | 0.001524 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.001676 |
| Safety = high and Persons = 4 and Buying = low and Maint = med | vgood | 0.001673 |
| Buying = high and Maint = med and Persons = 4 and Safety = med | acc | 0.002709 |
| Buying = low and Maint = med and Persons = more and Safety = high | vgood | 0.001673 |
| Safety = high and Persons = more and Buying = low and Maint = med | good | 0.001074 |
| Safety = high and Persons = 4 and Buying = low and Maint = high | vgood | 0.001858 |
| Buying = high and Maint = high and Persons = 4 and Safety = med | acc | 0.002299 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 5more | acc | 0.001104 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 4 | acc | 0.001104 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.528993 |
| Persons = 2 | unacc | 0.430504 |
| Buying = vhigh and Maint = high | unacc | 0.090373 |
| Buying = high and Maint = vhigh | unacc | 0.081349 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.043388 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.041408 |
| Buying = high and Doors = 5more | acc | 0.121849 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.079295 |
| Safety = med and Maint = high and Buying = low | acc | 0.041701 |
| Safety = med and Maint = high and Lug_boot = small | unacc | 0.021687 |
| Maint = vhigh and Buying = vhigh | unacc | 0.073059 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.081967 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.081967 |
| Safety = high and Lug_boot = big and Buying = high | acc | 0.086957 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.037433 |
| Safety = med and Lug_boot = small and Doors = 4 | acc | 0.049383 |
| Safety = med and Lug_boot = small and Doors = 5more | acc | 0.049383 |
| Safety = med and Lug_boot = small and Doors = 3 | acc | 0.037500 |
| Safety = med and Lug_boot = small and Persons = more | unacc | 0.011696 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.046154 |
| Buying = vhigh and Safety = high | acc | 0.233087 |
| Maint = vhigh and Safety = high and Lug_boot = big | acc | 0.105960 |
| Safety = med and Doors = 4 and Buying = high | acc | 0.062500 |
| Lug_boot = big and Safety = high and Maint = low | vgood | 0.065041 |
| Maint = vhigh and Doors = 5more | acc | 0.091603 |
| Maint = vhigh and Safety = high and Persons = 4 | acc | 0.077519 |
| Buying = high and Safety = high and Lug_boot = med | acc | 0.125000 |
| Maint = vhigh and Doors = 4 | acc | 0.055556 |
| Maint = vhigh and Persons = more and Doors = 3 | acc | 0.048000 |
| Maint = vhigh and Safety = med | unacc | 0.025907 |
| Buying = high and Lug_boot = small and Persons = 4 | acc | 0.057851 |
| Safety = med and Buying = vhigh and Doors = 4 | acc | 0.033898 |
| Safety = med and Buying = high and Lug_boot = big | acc | 0.050000 |
| Buying = high and Doors = 2 | unacc | 0.039326 |
| Safety = med and Buying = vhigh and Doors = 5more | acc | 0.036036 |
| Safety = med and Buying = vhigh and Doors = 2 | unacc | 0.017647 |
| Safety = med and Maint = high and Doors = 2 | unacc | 0.011834 |
| Maint = vhigh and Lug_boot = small | unacc | 0.011834 |
| Safety = med and Buying = low and Doors = 2 | acc | 0.047619 |
| Maint = high and Buying = med | acc | 0.194700 |
| Safety = med and Buying = med and Maint = med | acc | 0.122807 |
| Lug_boot = big and Safety = high | vgood | 0.191304 |
| Lug_boot = small and Maint = high | acc | 0.076190 |
| Lug_boot = small and Buying = low and Persons = 4 | good | 0.104478 |
| Lug_boot = big | good | 0.104478 |
| Buying = high and Persons = more | acc | 0.085714 |
| Buying = high | unacc | 0.040000 |
| Lug_boot = small and Maint = low | good | 0.097222 |
| Safety = med and Doors = 4 | good | 0.105263 |
| Doors = 4 and Lug_boot = med | vgood | 0.140351 |
| Doors = 5more and Safety = high and Lug_boot = med | vgood | 0.155172 |
| Buying = vhigh and Persons = 4 | unacc | 0.045455 |
| Maint = low and Safety = high | good | 0.114286 |
| Doors = 5more and Lug_boot = med | good | 0.135135 |
| Persons = 4 | acc | 0.344729 |
| Buying = med | acc | 0.162896 |
| Lug_boot = med | acc | 0.095238 |
|  | good | 0.388889 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Lug_boot = big and Persons = 4 and Buying = med and Maint = med | vgood | 0.002670 |
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.005374 |
| Safety = high and Buying = med and Maint = med and Persons = more | vgood | 0.002730 |
| Safety = high and Maint = low and Buying = med and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Persons = more and Maint = low and Buying = med and Lug_boot = big | vgood | 0.002670 |
| Buying = low and Maint = med and Persons = more and Safety = med | good | 0.002810 |
| Maint = low and Persons = 4 and Buying = low and Safety = high | good | 0.002456 |
| Maint = low and Buying = med and Persons = more and Safety = med and Lug_boot = big | good | 0.002749 |
| Maint = low and Buying = med and Safety = high and Persons = 4 | good | 0.002456 |
| Buying = low and Maint = med and Safety = high and Lug_boot = small | good | 0.003064 |
| Maint = low and Buying = med and Persons = more and Safety = high | good | 0.001574 |
| Maint = low and Buying = low and Safety = med and Persons = more | good | 0.001913 |
| Safety = med and Maint = low and Persons = 4 and Buying = low and Lug_boot = big | good | 0.002749 |
| Persons = 4 and Safety = high and Buying = med | acc | 0.019645 |
| Safety = med and Persons = 4 and Maint = med and Buying = med | acc | 0.009683 |
| Persons = more and Safety = high and Buying = med | acc | 0.018450 |
| Persons = more and Safety = med and Lug_boot = big and Maint = med | acc | 0.010554 |
| Safety = high and Persons = more and Maint = low | acc | 0.013363 |
| Persons = 4 and Safety = high and Buying = high and Maint = high | acc | 0.010554 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.015447 |
| Safety = med and Persons = 4 and Lug_boot = big | acc | 0.018697 |
| Persons = more and Safety = med and Lug_boot = big and Buying = med | acc | 0.006184 |
| Persons = more and Safety = high and Maint = med | acc | 0.012212 |
| Safety = med and Persons = more and Lug_boot = med | acc | 0.016904 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.009549 |
| Persons = 4 and Safety = med and Maint = low and Buying = med | acc | 0.002222 |
| Persons = more and Safety = med and Maint = low and Lug_boot = big | acc | 0.007061 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.014866 |
| Buying = low and Safety = high and Persons = 4 | acc | 0.010252 |
| Persons = 4 and Safety = med and Lug_boot = med and Doors = 4 | acc | 0.002667 |
| Safety = high and Buying = high and Maint = high and Persons = more | acc | 0.008017 |
| Safety = med and Persons = more and Buying = low and Lug_boot = big | acc | 0.004425 |
| Safety = med and Persons = 4 and Doors = 5more and Lug_boot = med | acc | 0.004340 |
| Persons = more and Safety = med and Maint = high and Lug_boot = big and Buying = high | acc | 0.003543 |
| Persons = more and Buying = low and Safety = high | acc | 0.006447 |
| Persons = more and Safety = med and Buying = med and Maint = low | acc | 0.001144 |
| Buying = med and Persons = more and Maint = med and Safety = med | acc | 0.001996 |
|  | unacc | 0.962014 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
med|low|more|high|vgood
low|low|more|high|vgood
vhigh|low|more|high|acc
high|low|more|high|acc
low|med|more|high|vgood
high|med|more|high|acc
med|med|more|high|vgood
vhigh|med|more|high|acc
low|high|more|high|vgood
med|high|more|high|acc
low|low|4|high|vgood
high|high|more|high|acc
vhigh|low|4|high|acc
high|low|4|high|acc
med|low|4|high|vgood
vhigh|high|more|high|unacc
med|med|4|high|acc
low|low|more|med|good
vhigh|low|more|med|acc
med|vhigh|more|high|acc
high|vhigh|more|high|unacc
low|med|4|high|good
low|vhigh|more|high|acc
high|low|more|med|acc
high|med|4|high|acc
vhigh|med|4|high|acc
med|low|more|med|good
vhigh|vhigh|more|high|unacc
vhigh|med|more|med|acc
vhigh|low|2|high|unacc
low|low|2|high|unacc
med|med|more|med|acc
med|high|4|high|acc
high|high|4|high|acc
low|high|4|high|vgood
low|med|more|med|good
high|low|2|high|unacc
high|med|more|med|acc
vhigh|high|4|high|unacc
med|low|2|high|unacc
low|med|2|high|unacc
med|med|2|high|unacc
vhigh|vhigh|4|high|unacc
high|low|4|med|unacc
high|high|more|med|acc
low|high|more|med|acc
low|vhigh|4|high|acc
med|vhigh|4|high|acc
vhigh|low|4|med|unacc
med|low|4|med|good
med|high|more|med|unacc
low|low|4|med|acc
vhigh|med|2|high|unacc
high|vhigh|4|high|unacc
high|med|2|high|unacc
vhigh|high|more|med|unacc
low|med|4|med|acc
low|vhigh|more|med|acc
low|high|2|high|unacc
vhigh|med|4|med|unacc
high|med|4|med|acc
vhigh|vhigh|more|med|unacc
med|med|4|med|acc
high|low|more|low|unacc
high|vhigh|more|med|unacc
low|low|more|low|unacc
med|vhigh|more|med|acc
vhigh|low|more|low|unacc
high|high|2|high|unacc
vhigh|high|2|high|unacc
med|high|2|high|unacc
med|low|more|low|unacc
high|high|4|med|acc
vhigh|vhigh|2|high|unacc
med|high|4|med|unacc
vhigh|med|more|low|unacc
low|low|2|med|unacc
med|med|more|low|unacc
low|high|4|med|acc
low|vhigh|2|high|unacc
med|vhigh|2|high|unacc
high|vhigh|2|high|unacc
high|low|2|med|unacc
vhigh|high|4|med|unacc
low|med|more|low|unacc
vhigh|low|2|med|unacc
high|med|more|low|unacc
med|low|2|med|unacc
low|high|more|low|unacc
vhigh|vhigh|4|med|unacc
low|vhigh|4|med|acc
low|low|4|low|unacc
high|vhigh|4|med|unacc
med|vhigh|4|med|unacc
med|med|2|med|unacc
med|low|4|low|unacc
high|low|4|low|unacc
low|med|2|med|unacc
vhigh|med|2|med|unacc
vhigh|high|more|low|unacc
high|high|more|low|unacc
high|med|2|med|unacc
med|high|more|low|unacc
vhigh|low|4|low|unacc
high|high|2|med|unacc
vhigh|med|4|low|unacc
vhigh|high|2|med|unacc
med|med|4|low|unacc
med|vhigh|more|low|unacc
vhigh|vhigh|more|low|unacc
med|high|2|med|unacc
high|med|4|low|unacc
low|med|4|low|unacc
high|vhigh|more|low|unacc
low|high|2|med|unacc
low|vhigh|more|low|unacc
low|high|4|low|unacc
vhigh|low|2|low|unacc
med|high|4|low|unacc
low|low|2|low|unacc
vhigh|vhigh|2|med|unacc
med|low|2|low|unacc
low|vhigh|2|med|unacc
high|high|4|low|unacc
high|vhigh|2|med|unacc
high|low|2|low|unacc
med|vhigh|2|med|unacc
vhigh|high|4|low|unacc
high|vhigh|4|low|unacc
vhigh|med|2|low|unacc
med|med|2|low|unacc
vhigh|vhigh|4|low|unacc
low|vhigh|4|low|unacc
high|med|2|low|unacc
med|vhigh|4|low|unacc
low|med|2|low|unacc
low|high|2|low|unacc
vhigh|high|2|low|unacc
high|high|2|low|unacc
med|high|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc
low|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Lug_boot = big) and (Persons = 4) and (Buying = med) and (Maint = med)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Persons = more)|vgood (12.0/5.0)
(Safety = high) and (Maint = low) and (Buying = med) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Persons = more) and (Maint = low) and (Buying = med) and (Lug_boot = big)|vgood (4.0/0.0)
(Buying = low) and (Maint = med) and (Persons = more) and (Safety = med)|good (12.0/5.0)
(Maint = low) and (Persons = 4) and (Buying = low) and (Safety = high)|good (7.0/2.0)
(Maint = low) and (Buying = med) and (Persons = more) and (Safety = med) and (Lug_boot = big)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Persons = 4)|good (7.0/2.0)
(Buying = low) and (Maint = med) and (Safety = high) and (Lug_boot = small)|good (11.0/4.0)
(Maint = low) and (Buying = med) and (Persons = more) and (Safety = high)|good (7.0/3.0)
(Maint = low) and (Buying = low) and (Safety = med) and (Persons = more)|good (9.0/4.0)
(Safety = med) and (Maint = low) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|good (4.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = med)|acc (28.0/2.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Buying = med)|acc (11.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med)|acc (24.0/2.0)
(Persons = more) and (Safety = med) and (Lug_boot = big) and (Maint = med)|acc (12.0/0.0)
(Safety = high) and (Persons = more) and (Maint = low)|acc (26.0/5.0)
(Persons = 4) and (Safety = high) and (Buying = high) and (Maint = high)|acc (12.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (21.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big)|acc (48.0/16.0)
(Persons = more) and (Safety = med) and (Lug_boot = big) and (Buying = med)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (24.0/5.0)
(Safety = med) and (Persons = more) and (Lug_boot = med)|acc (48.0/19.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (26.0/8.0)
(Persons = 4) and (Safety = med) and (Maint = low) and (Buying = med)|acc (7.0/2.0)
(Persons = more) and (Safety = med) and (Maint = low) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (24.0/3.0)
(Buying = low) and (Safety = high) and (Persons = 4)|acc (13.0/1.0)
(Persons = 4) and (Safety = med) and (Lug_boot = med) and (Doors = 4)|acc (9.0/3.0)
(Safety = high) and (Buying = high) and (Maint = high) and (Persons = more)|acc (11.0/1.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Lug_boot = big)|acc (5.0/0.0)
(Safety = med) and (Persons = 4) and (Doors = 5more) and (Lug_boot = med)|acc (8.0/1.0)
(Persons = more) and (Safety = med) and (Maint = high) and (Lug_boot = big) and (Buying = high)|acc (4.0/0.0)
(Persons = more) and (Buying = low) and (Safety = high)|acc (15.0/5.0)
(Persons = more) and (Safety = med) and (Buying = med) and (Maint = low)|acc (4.0/1.0)
(Buying = med) and (Persons = more) and (Maint = med) and (Safety = med)|acc (4.0/1.0)
|unacc (1038.0/2.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (520.0)
Persons = 2|unacc (350.0)
Buying = vhigh AND Maint = high|unacc (46.0)
Buying = high AND Maint = vhigh|unacc (41.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (21.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (20.0)
Buying = high AND Doors = 5more|acc (29.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (18.0)
Safety = med AND Maint = high AND Buying = low|acc (11.0/1.0)
Safety = med AND Maint = high AND Lug_boot = small|unacc (8.0)
Maint = vhigh AND Buying = vhigh|unacc (32.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (15.0)
Safety = high AND Lug_boot = big AND Buying = high|acc (16.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (14.0)
Safety = med AND Lug_boot = small AND Doors = 4|acc (8.0)
Safety = med AND Lug_boot = small AND Doors = 5more|acc (8.0)
Safety = med AND Lug_boot = small AND Doors = 3|acc (6.0)
Safety = med AND Lug_boot = small AND Persons = more|unacc (4.0)
Safety = med AND Lug_boot = big AND Buying = low|good (15.0)
Buying = vhigh AND Safety = high|acc (43.0/1.0)
Maint = vhigh AND Safety = high AND Lug_boot = big|acc (16.0)
Safety = med AND Doors = 4 AND Buying = high|acc (9.0)
Lug_boot = big AND Safety = high AND Maint = low|vgood (16.0)
Maint = vhigh AND Doors = 5more|acc (12.0)
Maint = vhigh AND Safety = high AND Persons = 4|acc (10.0)
Buying = high AND Safety = high AND Lug_boot = med|acc (17.0)
Maint = vhigh AND Doors = 4|acc (7.0)
Maint = vhigh AND Persons = more AND Doors = 3|acc (6.0)
Maint = vhigh AND Safety = med|unacc (5.0)
Buying = high AND Lug_boot = small AND Persons = 4|acc (7.0)
Safety = med AND Buying = vhigh AND Doors = 4|acc (4.0)
Safety = med AND Buying = high AND Lug_boot = big|acc (6.0)
Buying = high AND Doors = 2|unacc (7.0)
Safety = med AND Buying = vhigh AND Doors = 5more|acc (4.0)
Safety = med AND Buying = vhigh AND Doors = 2|unacc (3.0)
Safety = med AND Maint = high AND Doors = 2|unacc (2.0)
Maint = vhigh AND Lug_boot = small|unacc (2.0)
Safety = med AND Buying = low AND Doors = 2|acc (5.0)
Maint = high AND Buying = med|acc (28.0/2.0)
Safety = med AND Buying = med AND Maint = med|acc (14.0)
Lug_boot = big AND Safety = high|vgood (22.0)
Lug_boot = small AND Maint = high|acc (9.0/1.0)
Lug_boot = small AND Buying = low AND Persons = 4|good (7.0)
Lug_boot = big|good (7.0)
Buying = high AND Persons = more|acc (6.0)
Buying = high|unacc (3.0)
Lug_boot = small AND Maint = low|good (9.0/2.0)
Safety = med AND Doors = 4|good (6.0)
Doors = 4 AND Lug_boot = med|vgood (8.0)
Doors = 5more AND Safety = high AND Lug_boot = med|vgood (9.0)
Buying = vhigh AND Persons = 4|unacc (2.0)
Maint = low AND Safety = high|good (7.0/1.0)
Doors = 5more AND Lug_boot = med|good (5.0)
Persons = 4|acc (12.0/1.0)
Buying = med|acc (9.0/3.0)
Lug_boot = med|acc (7.0/3.0)
|good (4.0/1.0)


## J48 Decision Tree

* Safety = low: unacc (259.0)
* Safety = med
	* Persons = 2: unacc (87.0)
	* Persons = 4
		* Buying = vhigh: unacc (24.0/6.0)
		* Buying = high
			* Lug_boot = small: unacc (7.0)
			* Lug_boot = med: unacc (4.0/2.0)
			* Lug_boot = big: acc (8.0/1.0)
		* Buying = med: acc (21.0/7.0)
		* Buying = low: acc (24.0/12.0)
	* Persons = more
		* Lug_boot = small: unacc (29.0/6.0)
		* Lug_boot = med
			* Doors = 2: unacc (8.0/3.0)
			* Doors = 3: acc (8.0/2.0)
			* Doors = 4: acc (7.0/2.0)
			* Doors = 5more: acc (4.0/2.0)
		* Lug_boot = big: acc (28.0/7.0)
* Safety = high
	* Persons = 2: unacc (88.0)
	* Persons = 4
		* Buying = vhigh
			* Maint = vhigh: unacc (6.0)
			* Maint = high: unacc (8.0)
			* Maint = med: acc (4.0)
			* Maint = low: acc (4.0)
		* Buying = high
			* Maint = vhigh: unacc (7.0)
			* Maint = high: acc (6.0)
			* Maint = med: acc (6.0)
			* Maint = low: acc (5.0)
		* Buying = med
			* Maint = vhigh: acc (8.0)
			* Maint = high: acc (3.0)
			* Maint = med: acc (7.0/3.0)
			* Maint = low: good (5.0/2.0)
		* Buying = low
			* Maint = vhigh: acc (5.0)
			* Maint = high: vgood (4.0/1.0)
			* Maint = med: vgood (7.0/3.0)
			* Maint = low: vgood (4.0/2.0)
	* Persons = more
		* Buying = vhigh
			* Maint = vhigh: unacc (4.0)
			* Maint = high: unacc (5.0)
			* Maint = med: acc (4.0)
			* Maint = low: acc (6.0)
		* Buying = high
			* Maint = vhigh: unacc (5.0)
			* Maint = high: acc (6.0/1.0)
			* Maint = med: acc (3.0)
			* Maint = low: acc (4.0)
		* Buying = med
			* Maint = vhigh: acc (8.0/1.0)
			* Maint = high: acc (5.0)
			* Maint = med: vgood (6.0/3.0)
			* Maint = low: vgood (8.0/2.0)
		* Buying = low
			* Maint = vhigh: acc (4.0)
			* Maint = high: vgood (5.0/2.0)
			* Maint = med: good (5.0/1.0)
			* Maint = low: vgood (3.0/1.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3): vgood(39.0/3.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low): good(11.0/2.0)
						* Buying!=(low)
							* Maint=(low): good(6.0/1.0)
							* Maint!=(low): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4): acc(6.0/1.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high): good(12.0/3.0)
									* Maint!=(low)|(vhigh)|(high): acc(13.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Maint=(high)
						* Buying=(low)
								* Safety=(high)|(low): vgood(12.0/2.0)
								* Safety!=(high)|(low): acc(11.0/0.0)
						* Buying!=(low): acc(26.0/3.0)
					* Maint!=(high): acc(55.0/5.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(25.0/4.0)
						* Safety!=(high)|(low): unacc(23.0/5.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Doors=(5more)|(4): acc(63.0/0.0)
						* Doors!=(5more)|(4)
							* Safety=(high)|(low): acc(28.0/0.0)
							* Safety!=(high)|(low)
							* Lug_boot=(big): acc(13.0/0.0)
							* Lug_boot!=(big): unacc(10.0/4.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high): acc(23.0/3.0)
					* Safety!=(high): unacc(27.0/0.0)
				* Maint!=(low)|(med)
						* Buying=(high)|(med)|(low)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(28.0/2.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(7.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
						* Buying!=(high)|(med)|(low): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(345.0/0.0)
	* Persons!=(more)|(4): unacc(525.0/0.0)


