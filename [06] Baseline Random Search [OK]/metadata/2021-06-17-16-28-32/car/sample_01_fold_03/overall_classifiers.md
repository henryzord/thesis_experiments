# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604958 |
| Persons != more | unacc | 0.600608 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot != med | acc | 0.045814 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint != med | acc | 0.036919 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot = med and Safety != med | acc | 0.024233 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint = high and Buying != vhigh | acc | 0.018936 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh and Lug_boot != small | acc | 0.018804 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Maint != high and Doors != 2 | acc | 0.019481 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot = small | acc | 0.013406 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Lug_boot = med and Safety = med and Doors != 2 | acc | 0.012615 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot != med | vgood | 0.015162 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Safety != med and Doors != 2 | acc | 0.013878 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint != high | good | 0.014091 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety = med | acc | 0.012265 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety = med and Lug_boot != small and Maint = high | acc | 0.011457 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint != high | good | 0.006843 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Doors != 2 | vgood | 0.007661 |
| Persons != 2 and Safety != low and Buying = low and Maint = vhigh and Lug_boot = small and Safety != med | acc | 0.005045 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot != small | vgood | 0.006839 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Maint = high and Buying != vhigh | acc | 0.004240 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot != small | good | 0.005758 |
| Buying = med and Maint = low and Persons = 4 and Safety = med | acc | 0.002707 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot = small and Safety = med and Maint = med | acc | 0.004240 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot = small and Maint = high | acc | 0.004240 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint != low and Lug_boot != small and Maint = med and Safety != med | vgood | 0.005125 |
| Persons != 2 and Safety != low and Buying != low and Buying != med and Maint != vhigh and Lug_boot = small and Safety != med and Maint != high and Doors = 2 and Persons = 4 | acc | 0.003300 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety != med and Lug_boot = small | good | 0.002783 |
| Persons != 2 and Safety != low and Buying != low and Buying = med and Maint = low and Safety = med and Lug_boot = small | acc | 0.004240 |
| Persons != 2 and Safety != low and Buying = low and Maint != vhigh and Safety != med and Lug_boot != small and Lug_boot = med and Doors = 2 | good | 0.001784 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Doors = 3 | acc | 0.000414 |
| Buying = med and Maint = high and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = med and Maint = vhigh and Persons = 4 and Safety = high | acc | 0.009024 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.001674 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.001674 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.528455 |
| Persons = 2 | unacc | 0.429975 |
| Buying = vhigh and Maint = vhigh | unacc | 0.086614 |
| Buying = high and Maint = vhigh | unacc | 0.081188 |
| Safety = med and Lug_boot = small and Buying = vhigh | unacc | 0.043299 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.041322 |
| Buying = high and Doors = 4 | acc | 0.120332 |
| Safety = med and Maint = high and Buying = vhigh | unacc | 0.026846 |
| Safety = med and Lug_boot = big and Buying = high | acc | 0.078341 |
| Safety = med and Lug_boot = big and Maint = vhigh | acc | 0.069767 |
| Safety = med and Lug_boot = big and Buying = vhigh | acc | 0.069767 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.034826 |
| Buying = high and Safety = high and Doors = 5more | acc | 0.088235 |
| Buying = high and Safety = high and Doors = 3 | acc | 0.079208 |
| Buying = vhigh and Maint = high | unacc | 0.056000 |
| Safety = med and Lug_boot = small and Maint = med and Doors = 4 | acc | 0.023669 |
| Safety = med and Lug_boot = small and Buying = low and Persons = 4 | acc | 0.057143 |
| Safety = med and Lug_boot = small and Maint = low and Persons = more | acc | 0.021259 |
| Safety = med and Lug_boot = small and Maint = high and Buying = med | unacc | 0.023324 |
| Safety = med and Lug_boot = small and Doors = 5more | acc | 0.030864 |
| Safety = med and Buying = vhigh and Doors = 2 | unacc | 0.011976 |
| Buying = vhigh and Doors = 4 | acc | 0.089286 |
| Buying = vhigh and Doors = 5more | acc | 0.083832 |
| Safety = med and Maint = high and Lug_boot = big | acc | 0.083832 |
| Safety = med and Lug_boot = big and Buying = low | good | 0.054348 |
| Maint = vhigh and Doors = 5more | acc | 0.098039 |
| Lug_boot = big and Safety = med and Maint = med | acc | 0.054795 |
| Lug_boot = big and Safety = high and Buying = low and Maint = high | vgood | 0.034483 |
| Maint = vhigh and Safety = high and Persons = 4 | acc | 0.121622 |
| Buying = vhigh and Lug_boot = big | acc | 0.051095 |
| Maint = vhigh and Doors = 3 | acc | 0.044118 |
| Lug_boot = big and Safety = high and Maint = high | acc | 0.064748 |
| Lug_boot = big and Safety = high and Buying = low and Maint = low | vgood | 0.041667 |
| Lug_boot = big and Safety = high and Buying = med and Maint = low | vgood | 0.036649 |
| Maint = vhigh and Doors = 2 and Buying = low | unacc | 0.009626 |
| Buying = vhigh and Doors = 3 and Persons = 4 | acc | 0.027826 |
| Maint = vhigh and Doors = 4 | acc | 0.042735 |
| Maint = high and Doors = 4 and Buying = low | acc | 0.031056 |
| Buying = vhigh and Lug_boot = med | acc | 0.051907 |
| Maint = high and Doors = 4 | acc | 0.031056 |
| Maint = high and Doors = 5more and Buying = med | acc | 0.042735 |
| Buying = high and Doors = 2 and Safety = high and Persons = 4 | acc | 0.066667 |
| Maint = high and Doors = 3 and Persons = 4 | acc | 0.031056 |
| Lug_boot = big and Safety = high and Buying = low | vgood | 0.042832 |
| Doors = 4 and Safety = med and Buying = med | good | 0.018735 |
| Doors = 4 and Lug_boot = small | good | 0.025407 |
| Doors = 4 and Safety = high | vgood | 0.067939 |
| Doors = 2 and Lug_boot = small and Persons = more | unacc | 0.128788 |
| Safety = med and Doors = 5more and Maint = low | good | 0.052478 |
| Safety = med and Doors = 4 | good | 0.024316 |
| Safety = med and Lug_boot = small | acc | 0.093750 |
| Safety = med and Buying = low and Maint = high | acc | 0.064516 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.059406 |
| Safety = med and Maint = high | acc | 0.038462 |
| Safety = med and Buying = med and Maint = low | acc | 0.028846 |
| Buying = high | acc | 0.087500 |
| Lug_boot = small and Buying = low and Maint = med | good | 0.073529 |
| Maint = high and Buying = med | acc | 0.063776 |
| Maint = high and Persons = 4 | acc | 0.027950 |
| Maint = low and Buying = med | good | 0.096970 |
| Buying = med and Safety = high and Lug_boot = med | acc | 0.043243 |
| Buying = med and Lug_boot = med | acc | 0.080065 |
| Buying = vhigh | acc | 0.076190 |
| Buying = med and Lug_boot = small | acc | 0.133333 |
| Safety = med | acc | 0.020737 |
| Maint = low and Lug_boot = med | vgood | 0.115385 |
| Maint = med and Persons = 4 | vgood | 0.076923 |
| Maint = high | acc | 0.018519 |
| Maint = med | vgood | 0.098814 |
|  | good | 0.481481 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more | vgood | 0.006387 |
| Safety = high and Buying = low and Persons = 4 and Lug_boot = big | vgood | 0.005374 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big | vgood | 0.002976 |
| Safety = high and Lug_boot = med and Buying = low and Persons = more | vgood | 0.003607 |
| Safety = high and Persons = 4 and Buying = high and Maint = med | acc | 0.010161 |
| Safety = high and Persons = 4 and Buying = med and Maint = vhigh | acc | 0.009322 |
| Safety = high and Persons = more and Buying = high and Maint = low | acc | 0.008552 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.009322 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med | acc | 0.008149 |
| Persons = 4 and Safety = med and Lug_boot = big and Maint = med | acc | 0.007647 |
| Safety = high and Persons = more and Maint = med and Buying = high | acc | 0.007717 |
| Persons = 4 and Safety = high and Maint = low and Buying = high | acc | 0.009322 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high | acc | 0.007647 |
| Persons = 4 and Safety = med and Buying = low and Maint = high | acc | 0.009322 |
| Safety = high and Persons = more and Maint = high and Buying = med | acc | 0.007717 |
| Persons = 4 and Safety = high and Maint = med and Buying = vhigh | acc | 0.010161 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 5more | acc | 0.006079 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.005106 |
| Persons = more and Safety = high and Doors = 5more | acc | 0.007794 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.003413 |
| Safety = med and Persons = more and Buying = low and Maint = high | acc | 0.006882 |
| Persons = 4 and Safety = high and Buying = med and Maint = high | acc | 0.009322 |
| Safety = med and Persons = 4 and Maint = low and Lug_boot = big | acc | 0.003904 |
| Persons = more and Safety = high and Maint = med and Buying = vhigh | acc | 0.005213 |
| Safety = med and Persons = more and Maint = med and Buying = med | acc | 0.004381 |
| Safety = med and Persons = 4 and Buying = low | acc | 0.005598 |
| Persons = more and Safety = high and Buying = med and Maint = vhigh | acc | 0.004381 |
| Persons = more and Safety = med and Maint = low and Buying = vhigh | acc | 0.002797 |
| Safety = high and Persons = 4 and Buying = low and Maint = vhigh | acc | 0.010161 |
|  | unacc | 0.862916 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|persons|safety|acceptability
---|---|---|---|---
low|low|more|high|vgood
high|low|more|high|acc
vhigh|low|more|high|acc
med|low|more|high|vgood
vhigh|med|more|high|acc
high|med|more|high|acc
med|med|more|high|vgood
low|med|more|high|vgood
low|low|4|high|good
med|low|4|high|vgood
low|high|more|high|vgood
high|low|4|high|acc
high|high|more|high|acc
vhigh|low|4|high|acc
vhigh|high|more|high|unacc
med|high|more|high|acc
low|med|4|high|good
med|med|4|high|vgood
med|vhigh|more|high|acc
vhigh|med|4|high|acc
low|vhigh|more|high|acc
high|med|4|high|acc
med|low|more|med|good
vhigh|vhigh|more|high|unacc
high|low|more|med|acc
high|vhigh|more|high|unacc
low|low|more|med|good
vhigh|low|more|med|acc
high|high|4|high|acc
med|high|4|high|acc
low|high|4|high|vgood
vhigh|med|more|med|acc
med|med|more|med|acc
low|med|more|med|good
high|med|more|med|acc
vhigh|low|2|high|unacc
med|low|2|high|unacc
low|low|2|high|unacc
high|low|2|high|unacc
vhigh|high|4|high|unacc
med|low|4|med|acc
low|vhigh|4|high|acc
low|low|4|med|good
med|vhigh|4|high|acc
low|high|more|med|acc
low|med|2|high|unacc
high|high|more|med|acc
vhigh|low|4|med|acc
high|vhigh|4|high|unacc
high|low|4|med|unacc
med|high|more|med|acc
med|med|2|high|unacc
vhigh|high|more|med|unacc
vhigh|med|2|high|unacc
high|med|2|high|unacc
vhigh|vhigh|4|high|unacc
med|med|4|med|acc
low|med|4|med|good
high|low|more|low|unacc
low|vhigh|more|med|acc
low|low|more|low|unacc
vhigh|med|4|med|acc
high|vhigh|more|med|unacc
high|med|4|med|acc
vhigh|high|2|high|unacc
vhigh|low|more|low|unacc
med|low|more|low|unacc
med|vhigh|more|med|acc
high|high|2|high|unacc
low|high|2|high|unacc
med|high|2|high|unacc
vhigh|vhigh|more|med|unacc
low|high|4|med|acc
low|vhigh|2|high|unacc
low|low|2|med|unacc
vhigh|low|2|med|unacc
med|vhigh|2|high|unacc
med|high|4|med|unacc
high|high|4|med|acc
high|med|more|low|unacc
vhigh|med|more|low|unacc
low|med|more|low|unacc
vhigh|vhigh|2|high|unacc
med|med|more|low|unacc
high|low|2|med|unacc
high|vhigh|2|high|unacc
med|low|2|med|unacc
vhigh|high|4|med|unacc
low|vhigh|4|med|acc
med|vhigh|4|med|acc
vhigh|med|2|med|unacc
vhigh|vhigh|4|med|unacc
high|high|more|low|unacc
vhigh|low|4|low|unacc
high|low|4|low|unacc
low|med|2|med|unacc
high|med|2|med|unacc
med|med|2|med|unacc
low|low|4|low|unacc
med|high|more|low|unacc
vhigh|high|more|low|unacc
low|high|more|low|unacc
high|vhigh|4|med|unacc
med|low|4|low|unacc
low|med|4|low|unacc
vhigh|vhigh|more|low|unacc
high|med|4|low|unacc
med|vhigh|more|low|unacc
vhigh|high|2|med|unacc
med|high|2|med|unacc
med|med|4|low|unacc
vhigh|med|4|low|unacc
low|high|2|med|unacc
high|high|2|med|unacc
low|vhigh|more|low|unacc
high|vhigh|more|low|unacc
low|high|4|low|unacc
med|high|4|low|unacc
med|low|2|low|unacc
vhigh|vhigh|2|med|unacc
high|high|4|low|unacc
med|vhigh|2|med|unacc
high|low|2|low|unacc
high|vhigh|2|med|unacc
vhigh|high|4|low|unacc
low|vhigh|2|med|unacc
vhigh|low|2|low|unacc
low|low|2|low|unacc
vhigh|vhigh|4|low|unacc
high|med|2|low|unacc
med|med|2|low|unacc
med|vhigh|4|low|unacc
vhigh|med|2|low|unacc
low|vhigh|4|low|unacc
low|med|2|low|unacc
high|vhigh|4|low|unacc
high|high|2|low|unacc
low|high|2|low|unacc
med|high|2|low|unacc
vhigh|high|2|low|unacc
high|vhigh|2|low|unacc
med|vhigh|2|low|unacc
low|vhigh|2|low|unacc
vhigh|vhigh|2|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more)|vgood (15.0/3.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Lug_boot = big)|vgood (15.0/4.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big)|vgood (11.0/4.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Persons = more)|vgood (15.0/6.0)
(Safety = high) and (Persons = 4) and (Buying = high) and (Maint = med)|acc (12.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med) and (Maint = vhigh)|acc (11.0/0.0)
(Safety = high) and (Persons = more) and (Buying = high) and (Maint = low)|acc (12.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (11.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = med)|acc (15.0/3.0)
(Persons = 4) and (Safety = med) and (Lug_boot = big) and (Maint = med)|acc (16.0/4.0)
(Safety = high) and (Persons = more) and (Maint = med) and (Buying = high)|acc (11.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = low) and (Buying = high)|acc (11.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = high)|acc (16.0/4.0)
(Persons = 4) and (Safety = med) and (Buying = low) and (Maint = high)|acc (11.0/0.0)
(Safety = high) and (Persons = more) and (Maint = high) and (Buying = med)|acc (11.0/1.0)
(Persons = 4) and (Safety = high) and (Maint = med) and (Buying = vhigh)|acc (12.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 5more)|acc (14.0/4.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Doors = 5more)|acc (26.0/12.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (9.0/3.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = high)|acc (10.0/1.0)
(Persons = 4) and (Safety = high) and (Buying = med) and (Maint = high)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = low) and (Lug_boot = big)|acc (11.0/3.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Buying = vhigh)|acc (8.0/1.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Buying = med)|acc (7.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = low)|acc (23.0/9.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Maint = vhigh)|acc (7.0/1.0)
(Persons = more) and (Safety = med) and (Maint = low) and (Buying = vhigh)|acc (11.0/5.0)
(Safety = high) and (Persons = 4) and (Buying = low) and (Maint = vhigh)|acc (8.0/0.0)
|unacc (1197.0/141.0)


## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (520.0)
Persons = 2|unacc (350.0)
Buying = vhigh AND Maint = vhigh|unacc (44.0)
Buying = high AND Maint = vhigh|unacc (41.0)
Safety = med AND Lug_boot = small AND Buying = vhigh|unacc (21.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (20.0)
Buying = high AND Doors = 4|acc (29.0)
Safety = med AND Maint = high AND Buying = vhigh|unacc (12.0)
Safety = med AND Lug_boot = big AND Buying = high|acc (17.0)
Safety = med AND Lug_boot = big AND Maint = vhigh|acc (15.0)
Safety = med AND Lug_boot = big AND Buying = vhigh|acc (15.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (14.0)
Buying = high AND Safety = high AND Doors = 5more|acc (18.0)
Buying = high AND Safety = high AND Doors = 3|acc (16.0)
Buying = vhigh AND Maint = high|unacc (21.0)
Safety = med AND Lug_boot = small AND Maint = med AND Doors = 4|acc (4.0)
Safety = med AND Lug_boot = small AND Buying = low AND Persons = 4|acc (10.0)
Safety = med AND Lug_boot = small AND Maint = low AND Persons = more|acc (7.0/2.0)
Safety = med AND Lug_boot = small AND Maint = high AND Buying = med|unacc (8.0)
Safety = med AND Lug_boot = small AND Doors = 5more|acc (5.0)
Safety = med AND Buying = vhigh AND Doors = 2|unacc (4.0)
Buying = vhigh AND Doors = 4|acc (15.0)
Buying = vhigh AND Doors = 5more|acc (14.0)
Safety = med AND Maint = high AND Lug_boot = big|acc (14.0)
Safety = med AND Lug_boot = big AND Buying = low|good (15.0)
Maint = vhigh AND Doors = 5more|acc (15.0)
Lug_boot = big AND Safety = med AND Maint = med|acc (8.0)
Lug_boot = big AND Safety = high AND Buying = low AND Maint = high|vgood (8.0)
Maint = vhigh AND Safety = high AND Persons = 4|acc (18.0)
Buying = vhigh AND Lug_boot = big|acc (7.0)
Maint = vhigh AND Doors = 3|acc (6.0)
Lug_boot = big AND Safety = high AND Maint = high|acc (9.0)
Lug_boot = big AND Safety = high AND Buying = low AND Maint = low|vgood (8.0)
Lug_boot = big AND Safety = high AND Buying = med AND Maint = low|vgood (7.0)
Maint = vhigh AND Doors = 2 AND Buying = low|unacc (5.0/2.0)
Buying = vhigh AND Doors = 3 AND Persons = 4|acc (5.0/1.0)
Maint = vhigh AND Doors = 4|acc (5.0)
Maint = high AND Doors = 4 AND Buying = low|acc (7.0/2.0)
Buying = vhigh AND Lug_boot = med|acc (7.0)
Maint = high AND Doors = 4|acc (5.0)
Maint = high AND Doors = 5more AND Buying = med|acc (5.0)
Buying = high AND Doors = 2 AND Safety = high AND Persons = 4|acc (8.0)
Maint = high AND Doors = 3 AND Persons = 4|acc (7.0/2.0)
Lug_boot = big AND Safety = high AND Buying = low|vgood (7.0)
Doors = 4 AND Safety = med AND Buying = med|good (7.0/3.0)
Doors = 4 AND Lug_boot = small|good (7.0/2.0)
Doors = 4 AND Safety = high|vgood (9.0)
Doors = 2 AND Lug_boot = small AND Persons = more|unacc (15.0)
Safety = med AND Doors = 5more AND Maint = low|good (7.0/1.0)
Safety = med AND Doors = 4|good (4.0)
Safety = med AND Lug_boot = small|acc (5.0)
Safety = med AND Buying = low AND Maint = high|acc (4.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = high|acc (6.0/2.0)
Safety = med AND Buying = med AND Maint = low|acc (6.0/3.0)
Buying = high|acc (8.0/2.0)
Lug_boot = small AND Buying = low AND Maint = med|good (5.0)
Maint = high AND Buying = med|acc (5.0)
Maint = high AND Persons = 4|acc (4.0/1.0)
Maint = low AND Buying = med|good (8.0/3.0)
Buying = med AND Safety = high AND Lug_boot = med|acc (7.0/3.0)
Buying = med AND Lug_boot = med|acc (6.0/1.0)
Buying = vhigh|acc (4.0)
Buying = med AND Lug_boot = small|acc (4.0)
Safety = med|acc (6.0/3.0)
Maint = low AND Lug_boot = med|vgood (6.0/3.0)
Maint = med AND Persons = 4|vgood (5.0/2.0)
Maint = high|acc (4.0/2.0)
Maint = med|vgood (4.0/1.0)
|good (5.0/1.0)


## J48 Decision Tree

* Persons = 2: unacc (522.0)
* Persons != 2
	* Safety = low: unacc (348.0)
	* Safety != low
		* Buying = low
			* Maint = vhigh
				* Lug_boot = small
					* Safety = med: unacc (7.0)
					* Safety != med: acc (8.0/1.0)
				* Lug_boot != small: acc (27.0/2.0)
			* Maint != vhigh
				* Safety = med
					* Lug_boot = small: acc (22.0/3.0)
					* Lug_boot != small
						* Maint = high: acc (14.0)
						* Maint != high: good (27.0/3.0)
				* Safety != med
					* Lug_boot = small
						* Maint = high: acc (7.0/1.0)
						* Maint != high: good (14.0/2.0)
					* Lug_boot != small
						* Lug_boot = med
							* Doors = 2: good (6.0/2.0)
							* Doors != 2: vgood (17.0/3.0)
						* Lug_boot != med: vgood (23.0)
		* Buying != low
			* Buying = med
				* Maint = low
					* Safety = med
						* Lug_boot = small: acc (7.0/1.0)
						* Lug_boot != small: good (14.0/3.0)
					* Safety != med
						* Lug_boot = small: good (6.0/1.0)
						* Lug_boot != small: vgood (14.0/2.0)
				* Maint != low
					* Lug_boot = small
						* Safety = med
							* Maint = med: acc (7.0/1.0)
							* Maint != med: unacc (15.0)
						* Safety != med
							* Doors = 2: unacc (5.0/2.0)
							* Doors != 2: acc (17.0)
					* Lug_boot != small
						* Maint = med
							* Safety = med: acc (15.0)
							* Safety != med: vgood (13.0/3.0)
						* Maint != med: acc (54.0/4.0)
			* Buying != med
				* Maint = vhigh: unacc (85.0)
				* Maint != vhigh
					* Lug_boot = small
						* Safety = med: unacc (41.0)
						* Safety != med
							* Maint = high
								* Buying = vhigh: unacc (6.0)
								* Buying != vhigh: acc (7.0/1.0)
							* Maint != high
								* Doors = 2
									* Persons = 4: acc (4.0)
									* Persons != 4: unacc (4.0)
								* Doors != 2: acc (24.0)
					* Lug_boot != small
						* Maint = high
							* Buying = vhigh: unacc (27.0)
							* Buying != vhigh: acc (29.0/3.0)
						* Maint != high
							* Lug_boot = med
								* Safety = med
									* Doors = 2: unacc (8.0)
									* Doors != 2: acc (21.0/3.0)
								* Safety != med: acc (30.0)
							* Lug_boot != med: acc (58.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med): vgood(46.0/11.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high): good(12.0/2.0)
								* Buying!=(low)|(vhigh)|(high)
							* Maint=(low): good(5.0/1.0)
							* Maint!=(low): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low): good(24.0/3.0)
						* Buying!=(low)
							* Maint=(low): good(11.0/3.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med): acc(24.0/4.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Maint=(high)|(med)|(low)
								* Buying=(low)|(vhigh)|(high)
								* Safety=(high)|(low): vgood(13.0/3.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Buying!=(low)|(vhigh)|(high): acc(25.0/3.0)
							* Maint!=(high)|(med)|(low): acc(50.0/3.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(26.0/4.0)
						* Safety!=(high)|(low)
								* Buying=(low)|(vhigh)|(high)
									* Maint=(high)|(med)|(low): acc(7.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
								* Buying!=(low)|(vhigh)|(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3): acc(84.0/3.0)
							* Doors!=(5more)|(4)|(3)
						* Lug_boot=(big): acc(14.0/0.0)
						* Lug_boot!=(big)
								* Safety=(high)|(low): acc(8.0/0.0)
								* Safety!=(high)|(low): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low): acc(28.0/4.0)
						* Safety!=(high)|(low): unacc(28.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med): acc(26.0/3.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low): acc(6.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(40.0/0.0)
				* Maint!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(348.0/0.0)
	* Persons!=(more)|(4): unacc(522.0/0.0)


