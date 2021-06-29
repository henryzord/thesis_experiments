# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | unacc | 0.701675 |
| Buying = high and Persons = 4 and Safety = high | acc | 0.018967 |
| Buying = high and Persons = more and Safety = high | acc | 0.017100 |
| Buying = med and Persons = 4 and Safety = med | acc | 0.014005 |
| Buying = med and Persons = more and Safety = med | acc | 0.013864 |
| Buying = med and Persons = 4 and Safety = high | acc | 0.015319 |
| Buying = low and Persons = 4 and Safety = med | acc | 0.013225 |
| Buying = low and Persons = more and Safety = med | acc | 0.011710 |
| Buying = med and Persons = more and Safety = high | acc | 0.011459 |
| Buying = low and Persons = more and Safety = high | vgood | 0.005638 |
| Buying = low and Persons = 4 and Safety = high | vgood | 0.004107 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.528033 |
| Safety = low | unacc | 0.424845 |
| Buying = vhigh and Maint != high and Maint != vhigh and Lug_boot != small | acc | 0.120838 |
| Buying = vhigh | unacc | 0.198023 |
| Buying = high and Maint != vhigh and Lug_boot != small | acc | 0.227687 |
| Buying = high and Maint = vhigh | unacc | 0.118421 |
| Lug_boot = small and Safety = med and Buying != high and Maint != vhigh | acc | 0.106423 |
| Buying = high and Safety != med | acc | 0.083612 |
| Buying != high and Maint = low and Safety = med | good | 0.046232 |
| Buying != high and Maint = low and Lug_boot != small | vgood | 0.053467 |
| Buying != high and Maint != low and Maint != med and Lug_boot != small and Safety = med | acc | 0.228158 |
| Buying != high and Maint != low and Lug_boot != small and Safety = med | acc | 0.053868 |
| Safety != med and Maint != low and Maint != med | acc | 0.283585 |
| Safety = med | unacc | 0.335220 |
| Lug_boot = small | good | 0.138462 |
|  | vgood | 0.384615 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 and Maint = high | vgood | 0.002670 |
| Safety = high and Buying = low and Lug_boot = big and Persons = more and Maint = high | vgood | 0.002670 |
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 and Maint = med | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = med and Maint = high | vgood | 0.002004 |
| Safety = high and Maint = low and Buying = low and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Persons = more and Buying = low and Maint = low and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Persons = more and Maint = med and Buying = med and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more and Maint = low | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med and Persons = more | vgood | 0.001504 |
| Safety = high and Buying = low and Maint = med and Persons = more and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Lug_boot = med and Buying = low and Doors = 5more and Persons = 4 | vgood | 0.001504 |
| Safety = high and Buying = med and Maint = low and Persons = more and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Lug_boot = med and Doors = 4 and Buying = med and Maint = low | vgood | 0.000892 |
| Safety = high and Lug_boot = med and Maint = med and Buying = med and Persons = 4 | vgood | 0.000669 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more and Maint = med | vgood | 0.000892 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.004161 |
| Maint = low and Buying = low and Safety = high and Persons = 4 and Lug_boot = small | good | 0.002778 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.003470 |
| Buying = low and Safety = med and Lug_boot = big and Maint = low and Persons = more | good | 0.002778 |
| Buying = low and Maint = med and Safety = med and Lug_boot = big and Persons = 4 | good | 0.002778 |
| Maint = low and Buying = med and Safety = med and Lug_boot = big and Persons = 4 | good | 0.002778 |
| Buying = low and Persons = more and Maint = med and Safety = high | good | 0.002224 |
| Maint = low and Buying = low and Safety = high and Persons = more | good | 0.002778 |
| Maint = low and Buying = med and Persons = more and Safety = high and Lug_boot = small | good | 0.001565 |
| Safety = med and Buying = low and Maint = med and Persons = more and Lug_boot = big | good | 0.002085 |
| Maint = low and Safety = med and Buying = low and Lug_boot = big and Persons = 4 | good | 0.002085 |
| Maint = low and Lug_boot = med and Safety = med and Buying = med and Doors = 5more | good | 0.000928 |
| Lug_boot = med and Buying = low and Safety = med and Maint = med and Doors = 5more | good | 0.000928 |
| Maint = low and Lug_boot = med and Buying = low and Safety = med and Persons = more | good | 0.000928 |
| Maint = low and Buying = med and Persons = more and Safety = med and Lug_boot = big | good | 0.001391 |
| Lug_boot = med and Maint = low and Buying = low and Persons = 4 and Safety = high | good | 0.000928 |
| Lug_boot = med and Safety = med and Buying = low and Maint = med | good | 0.000399 |
| Maint = low and Lug_boot = med and Buying = med and Persons = more | good | 0.000349 |
| Maint = low and Doors = 4 and Lug_boot = med and Safety = med and Persons = 4 | good | 0.000696 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.025893 |
| Persons = more and Safety = high and Buying = med and Lug_boot = big | acc | 0.007279 |
| Persons = more and Safety = high and Maint = med and Lug_boot = med | acc | 0.008182 |
| Persons = more and Safety = high and Maint = low and Lug_boot = big | acc | 0.007279 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med | acc | 0.010879 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.018924 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.009982 |
| Persons = more and Safety = high and Buying = med and Lug_boot = med | acc | 0.005583 |
| Safety = med and Persons = more and Lug_boot = big and Buying = low | acc | 0.007279 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009083 |
| Persons = more and Safety = high and Maint = med and Lug_boot = big | acc | 0.007279 |
| Persons = more and Safety = high and Buying = low and Doors = 3 | acc | 0.003653 |
| Safety = med and Persons = more and Maint = med and Lug_boot = big | acc | 0.007279 |
| Safety = med and Persons = 4 and Maint = low and Lug_boot = big | acc | 0.006375 |
| Persons = more and Safety = high and Maint = low and Lug_boot = med | acc | 0.004692 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med and Buying = med | acc | 0.003653 |
| Persons = 4 and Safety = high and Maint = med | acc | 0.018885 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low and Maint = high | acc | 0.003653 |
| Safety = med and Persons = 4 and Maint = med and Buying = med | acc | 0.006375 |
| Persons = more and Safety = high and Buying = low and Doors = 4 | acc | 0.003653 |
| Safety = med and Persons = more and Maint = low and Lug_boot = big | acc | 0.007279 |
| Safety = med and Persons = 4 and Buying = low and Maint = low | acc | 0.005469 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 5more and Buying = high | acc | 0.002742 |
| Persons = more and Safety = high and Buying = med and Doors = 3 | acc | 0.002742 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 3 and Buying = med | acc | 0.001830 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med and Doors = 3 | acc | 0.001830 |
| Safety = med and Persons = 4 and Maint = med and Lug_boot = big | acc | 0.006375 |
| Persons = more and Safety = high and Doors = 4 and Lug_boot = small and Buying = high | acc | 0.002742 |
| Persons = more and Safety = med and Buying = low and Doors = 3 | acc | 0.002925 |
| Persons = more and Safety = high and Buying = med and Doors = 4 | acc | 0.002742 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 5more and Buying = med | acc | 0.001830 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.011836 |
| Safety = med and Persons = 4 and Buying = low and Maint = med | acc | 0.004562 |
| Persons = more and Safety = high and Doors = 5more and Lug_boot = small and Buying = med | acc | 0.002742 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low and Doors = 3 | acc | 0.001830 |
| Safety = med and Persons = more and Doors = 4 and Buying = low | acc | 0.002925 |
| Safety = med and Persons = 4 and Buying = med and Maint = low | acc | 0.005469 |
| Persons = more and Safety = high and Buying = low and Doors = 5more | acc | 0.002742 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 5more and Maint = med | acc | 0.001830 |
| Safety = med and Persons = more and Doors = 4 and Lug_boot = med and Maint = med | acc | 0.001830 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 and Buying = med | acc | 0.001830 |
| Buying = high and Maint = high and Safety = high and Persons = 4 | acc | 0.009083 |
| Persons = more and Safety = high and Buying = high and Maint = high and Lug_boot = big | acc | 0.003653 |
| Safety = med and Persons = more and Maint = low and Buying = med | acc | 0.002925 |
| Safety = med and Persons = 4 and Doors = 5more and Lug_boot = med and Buying = med | acc | 0.001830 |
| Safety = med and Persons = more and Maint = high and Buying = high and Lug_boot = big | acc | 0.003653 |
| Safety = med and Persons = 4 and Buying = low and Lug_boot = big | acc | 0.002742 |
| Persons = more and Safety = high and Maint = low and Doors = 3 | acc | 0.001830 |
| Safety = med and Lug_boot = med and Doors = 5more and Maint = low and Persons = 4 | acc | 0.001830 |
| Persons = more and Safety = high and Buying = low | acc | 0.000734 |
| Safety = med and Lug_boot = med and Doors = 4 and Persons = 4 and Maint = med | acc | 0.001830 |
| Persons = more and Safety = high and Maint = low | acc | 0.000612 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low and Doors = 5more | acc | 0.001830 |
| Safety = med and Maint = high and Buying = high and Persons = 4 and Lug_boot = big | acc | 0.002742 |
| Persons = more and Safety = med and Buying = low and Doors = 5more | acc | 0.002059 |
| Persons = more and Safety = high and Buying = high and Maint = high and Lug_boot = med | acc | 0.001830 |
| Safety = med and Lug_boot = med and Doors = 4 and Persons = 4 | acc | 0.002093 |
| Persons = more and Doors = 4 and Safety = med and Buying = med | acc | 0.000917 |
| Persons = more and Safety = high and Maint = med | acc | 0.000612 |
| Safety = med and Lug_boot = med and Doors = 5more and Persons = 4 | acc | 0.000734 |
| Persons = more and Doors = 3 and Maint = high and Buying = high | acc | 0.000612 |
|  | unacc | 0.995430 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

buying|persons|safety|acceptability
---|---|---|---
low|more|high|vgood
med|more|high|acc
high|more|high|acc
vhigh|more|high|unacc
low|4|high|vgood
med|4|high|acc
high|4|high|acc
vhigh|4|high|unacc
med|2|high|unacc
vhigh|more|med|unacc
med|more|med|acc
low|2|high|unacc
high|2|high|unacc
low|more|med|acc
vhigh|2|high|unacc
high|more|med|unacc
med|4|med|acc
low|4|med|acc
vhigh|4|med|unacc
high|4|med|unacc
low|2|med|unacc
med|more|low|unacc
high|more|low|unacc
vhigh|2|med|unacc
high|2|med|unacc
med|2|med|unacc
low|more|low|unacc
vhigh|more|low|unacc
high|4|low|unacc
med|4|low|unacc
low|4|low|unacc
vhigh|4|low|unacc
med|2|low|unacc
high|2|low|unacc
vhigh|2|low|unacc
low|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4) and (Maint = high)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more) and (Maint = high)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4) and (Maint = med)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = med) and (Maint = high)|vgood (3.0/0.0)
(Safety = high) and (Maint = low) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Maint = low) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Persons = more) and (Maint = med) and (Buying = med) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more) and (Maint = low)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med) and (Persons = more)|vgood (4.0/1.0)
(Safety = high) and (Buying = low) and (Maint = med) and (Persons = more) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Doors = 5more) and (Persons = 4)|vgood (4.0/1.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = more) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Lug_boot = med) and (Doors = 4) and (Buying = med) and (Maint = low)|vgood (3.0/1.0)
(Safety = high) and (Lug_boot = med) and (Maint = med) and (Buying = med) and (Persons = 4)|vgood (4.0/2.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more) and (Maint = med)|vgood (3.0/1.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (6.0/0.0)
(Maint = low) and (Buying = low) and (Safety = high) and (Persons = 4) and (Lug_boot = small)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (5.0/0.0)
(Buying = low) and (Safety = med) and (Lug_boot = big) and (Maint = low) and (Persons = more)|good (4.0/0.0)
(Buying = low) and (Maint = med) and (Safety = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Buying = low) and (Persons = more) and (Maint = med) and (Safety = high)|good (4.0/1.0)
(Maint = low) and (Buying = low) and (Safety = high) and (Persons = more)|good (3.0/0.0)
(Maint = low) and (Buying = med) and (Persons = more) and (Safety = high) and (Lug_boot = small)|good (4.0/1.0)
(Safety = med) and (Buying = low) and (Maint = med) and (Persons = more) and (Lug_boot = big)|good (3.0/0.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|good (3.0/0.0)
(Maint = low) and (Lug_boot = med) and (Safety = med) and (Buying = med) and (Doors = 5more)|good (3.0/1.0)
(Lug_boot = med) and (Buying = low) and (Safety = med) and (Maint = med) and (Doors = 5more)|good (3.0/1.0)
(Maint = low) and (Lug_boot = med) and (Buying = low) and (Safety = med) and (Persons = more)|good (3.0/1.0)
(Maint = low) and (Buying = med) and (Persons = more) and (Safety = med) and (Lug_boot = big)|good (2.0/0.0)
(Lug_boot = med) and (Maint = low) and (Buying = low) and (Persons = 4) and (Safety = high)|good (3.0/1.0)
(Lug_boot = med) and (Safety = med) and (Buying = low) and (Maint = med)|good (6.0/4.0)
(Maint = low) and (Lug_boot = med) and (Buying = med) and (Persons = more)|good (8.0/6.0)
(Maint = low) and (Doors = 4) and (Lug_boot = med) and (Safety = med) and (Persons = 4)|good (4.0/2.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (27.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = big)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Lug_boot = med)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = med)|acc (12.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (22.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (11.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = med)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = low)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (10.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Lug_boot = big)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Doors = 3)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = low) and (Lug_boot = big)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = med)|acc (6.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med) and (Buying = med)|acc (4.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = med)|acc (21.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Buying = low) and (Maint = high)|acc (4.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Buying = med)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Doors = 4)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Maint = low) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = low)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 5more) and (Buying = high)|acc (3.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 3)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 3) and (Buying = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med) and (Doors = 3)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Lug_boot = big)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Doors = 4) and (Lug_boot = small) and (Buying = high)|acc (3.0/0.0)
(Persons = more) and (Safety = med) and (Buying = low) and (Doors = 3)|acc (5.0/1.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 4)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 5more) and (Buying = med)|acc (2.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (13.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = med)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Doors = 5more) and (Lug_boot = small) and (Buying = med)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = low) and (Doors = 3)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Doors = 4) and (Buying = low)|acc (5.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = low)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Doors = 5more)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 5more) and (Maint = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Doors = 4) and (Lug_boot = med) and (Maint = med)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4) and (Buying = med)|acc (2.0/0.0)
(Buying = high) and (Maint = high) and (Safety = high) and (Persons = 4)|acc (10.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = high) and (Lug_boot = big)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Maint = low) and (Buying = med)|acc (4.0/1.0)
(Safety = med) and (Persons = 4) and (Doors = 5more) and (Lug_boot = med) and (Buying = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Maint = high) and (Buying = high) and (Lug_boot = big)|acc (4.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|acc (3.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Doors = 3)|acc (2.0/0.0)
(Safety = med) and (Lug_boot = med) and (Doors = 5more) and (Maint = low) and (Persons = 4)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low)|acc (4.0/2.0)
(Safety = med) and (Lug_boot = med) and (Doors = 4) and (Persons = 4) and (Maint = med)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (4.0/2.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = low) and (Doors = 5more)|acc (2.0/0.0)
(Safety = med) and (Maint = high) and (Buying = high) and (Persons = 4) and (Lug_boot = big)|acc (3.0/0.0)
(Persons = more) and (Safety = med) and (Buying = low) and (Doors = 5more)|acc (4.0/1.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = high) and (Lug_boot = med)|acc (2.0/0.0)
(Safety = med) and (Lug_boot = med) and (Doors = 4) and (Persons = 4)|acc (5.0/3.0)
(Persons = more) and (Doors = 4) and (Safety = med) and (Buying = med)|acc (4.0/2.0)
(Persons = more) and (Safety = high) and (Maint = med)|acc (5.0/3.0)
(Safety = med) and (Lug_boot = med) and (Doors = 5more) and (Persons = 4)|acc (5.0/3.0)
(Persons = more) and (Doors = 3) and (Maint = high) and (Buying = high)|acc (6.0/4.0)
|unacc (1056.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (457.0)
Safety = low|unacc (299.0)
Buying = vhigh AND Maint != high AND Maint != vhigh AND Lug_boot != small|acc (49.0/5.0)
Buying = vhigh|unacc (103.0/9.0)
Buying = high AND Maint != vhigh AND Lug_boot != small|acc (74.0/5.0)
Buying = high AND Maint = vhigh|unacc (37.0)
Lug_boot = small AND Safety = med AND Buying != high AND Maint != vhigh|acc (34.0/10.0)
Buying = high AND Safety != med|acc (20.0/3.0)
Buying != high AND Maint = low AND Safety = med|good (22.0/5.0)
Buying != high AND Maint = low AND Lug_boot != small|vgood (21.0/2.0)
Buying != high AND Maint != low AND Maint != med AND Lug_boot != small AND Safety = med|acc (56.0/8.0)
Buying != high AND Maint != low AND Lug_boot != small AND Safety = med|acc (26.0/11.0)
Safety != med AND Maint != low AND Maint != med|acc (78.0/15.0)
Safety = med|unacc (28.0)
Lug_boot = small|good (28.0/8.0)
|vgood (26.0/6.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(28.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small): vgood(3.0/3.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big): good(6.0/2.0)
						* Lug_boot!=(big)|(med)
						* Buying=(low): good(14.0/1.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high): good(7.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(7.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): good(13.0/0.0)
										* Doors!=(5more)|(4)|(2): good(5.0/1.0)
									* Doors!=(5more)|(4)|(3): acc(4.0/3.0)
						* Buying!=(low)
							* Maint=(low): good(10.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
						* Safety=(high)
									* Maint=(high)|(med)|(low)
									* Lug_boot=(big)|(small): vgood(8.0/0.0)
									* Lug_boot!=(big)|(small): vgood(4.0/2.0)
									* Maint!=(high)|(med)|(low): acc(13.0/0.0)
						* Safety!=(high)
									* Maint=(high)|(med)|(low): acc(15.0/0.0)
									* Maint!=(high)|(med)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4): acc(5.0/3.0)
					* Buying!=(low)
							* Lug_boot=(big)|(small): acc(31.0/0.0)
							* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2): acc(6.0/2.0)
									* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/3.0)
						* Safety!=(high)|(low)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high): acc(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(57.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Persons=(more)|(2): acc(15.0/0.0)
								* Persons!=(more)|(2)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low): unacc(3.0/3.0)
							* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big)|(small): acc(16.0/0.0)
							* Lug_boot!=(big)|(small)
							* Safety=(high): acc(7.0/0.0)
							* Safety!=(high): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3): unacc(4.0/4.0)
					* Safety!=(high): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3): acc(16.0/0.0)
									* Doors!=(5more)|(4)|(3): acc(6.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(7.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
					* Buying!=(high): unacc(44.0/0.0)
				* Maint!=(high): unacc(90.0/0.0)
		* Safety!=(high)|(med): unacc(342.0/0.0)
	* Persons!=(more)|(4): unacc(518.0/0.0)


