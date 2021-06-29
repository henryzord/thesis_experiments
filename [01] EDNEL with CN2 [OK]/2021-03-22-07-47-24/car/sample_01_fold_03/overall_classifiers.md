# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.604958 |
| Persons != more | unacc | 0.600608 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors != 3 and Persons != 2 | acc | 0.004122 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot = med and Buying!=(low) and Maint!=(low) | acc | 0.002477 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors = 3 | acc | 0.001653 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Maint != low and Doors = 4 | acc | 0.001653 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Maint != low and Doors = 5more | acc | 0.001653 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.529412 |
| Safety = low | unacc | 0.428571 |
| Buying != low and Buying != med and Maint = vhigh | unacc | 0.154827 |
| Buying = vhigh and Maint != high and Lug_boot != small and Doors != 2 | acc | 0.136600 |
| Buying = vhigh and Maint = high | unacc | 0.086393 |
| Safety = med and Lug_boot = small and Buying != high and Buying != vhigh and Maint != vhigh and Doors != 2 and Maint != high | acc | 0.089744 |
| Lug_boot = small and Safety = med and Buying != low | unacc | 0.110662 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.260274 |
| Maint = vhigh and Lug_boot != small and Doors != 2 | acc | 0.190000 |
| Safety = med and Maint = vhigh and Lug_boot != big | unacc | 0.031546 |
| Buying = high and Lug_boot = big | acc | 0.126437 |
| Buying = high and Safety != med and Doors != 2 | acc | 0.067485 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.021429 |
| Safety = med and Maint = high and Lug_boot != big and Buying = low | acc | 0.082180 |
| Safety = med and Maint = high and Lug_boot != med | acc | 0.082180 |
| Safety = med and Buying = high and Persons = 4 | unacc | 0.012048 |
| Safety = med and Buying = vhigh and Lug_boot = med | unacc | 0.019920 |
| Lug_boot = small and Doors != 2 and Maint != low and Buying != low | acc | 0.142857 |
| Lug_boot = small and Doors != 2 and Buying != med and Maint != med and Maint != low | acc | 0.073826 |
| Lug_boot = small and Doors != 2 and Buying != vhigh | good | 0.080645 |
| Lug_boot = small and Persons != 4 and Doors = 2 | unacc | 0.075117 |
| Safety = med and Maint = high and Doors != 2 | acc | 0.037538 |
| Safety = med and Maint != high and Buying != vhigh and Maint != vhigh and Buying = low and Lug_boot != small and Lug_boot != med | good | 0.090909 |
| Safety = med and Maint != high and Maint != low and Buying != low | acc | 0.171171 |
| Safety = med and Maint != high and Doors != 2 and Doors != 3 | good | 0.096552 |
| Buying != vhigh and Maint != vhigh and Safety != med and Buying != high and Maint != high and Lug_boot != small and Lug_boot != med | vgood | 0.234783 |
| Doors = 2 and Maint != high and Maint = vhigh | acc | 0.190476 |
| Buying = vhigh | acc | 0.250000 |
| Doors != 2 and Safety = med and Buying = med | good | 0.013333 |
| Doors != 2 and Buying = low and Safety != med and Doors != 3 | vgood | 0.208333 |
| Maint = high and Safety != med and Buying != low | acc | 0.333333 |
| Buying != high and Safety = med and Maint != high and Lug_boot != big | acc | 0.192857 |
| Buying = high | acc | 0.170732 |
| Safety = med and Maint = high | unacc | 0.073171 |
| Doors != 2 and Persons != 4 | vgood | 0.303030 |
| Doors != 4 and Doors != 5more and Maint != high and Maint != med | good | 0.416667 |
| Lug_boot != big and Buying = med and Doors != 2 | vgood | 0.228571 |
| Lug_boot != big and Maint = high | acc | 0.363636 |
| Buying != med and Maint != high | good | 0.400000 |
| Buying != med | vgood | 0.500000 |
|  | acc | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = more and Maint = high | vgood | 0.002670 |
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 and Maint = high | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big and Maint = med | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = med | vgood | 0.003607 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002089 |
| Safety = high and Buying = low and Lug_boot = big and Maint = low and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = med and Maint = low and Persons = more | vgood | 0.002406 |
| Safety = high and Buying = low and Persons = 4 and Maint = med | vgood | 0.001673 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med | vgood | 0.001522 |
| Safety = high and Buying = low and Maint = low and Persons = more and Lug_boot = big | vgood | 0.002670 |
| Maint = low and Buying = low and Persons = 4 and Safety = high | good | 0.002888 |
| Maint = low and Safety = med and Buying = low and Lug_boot = big and Persons = more | good | 0.002772 |
| Maint = low and Buying = med and Safety = med and Lug_boot = big and Persons = 4 | good | 0.002772 |
| Buying = low and Safety = med and Maint = med and Lug_boot = big and Persons = 4 | good | 0.002772 |
| Maint = low and Buying = med and Persons = more and Safety = med | good | 0.002498 |
| Buying = low and Persons = more and Maint = med and Safety = med and Lug_boot = big | good | 0.002772 |
| Buying = low and Maint = low and Safety = med and Persons = 4 | good | 0.002169 |
| Buying = low and Persons = more and Safety = high | good | 0.001863 |
| Maint = low and Buying = med and Persons = 4 and Safety = high | good | 0.002477 |
| Buying = low and Lug_boot = med and Safety = med and Persons = more | good | 0.000929 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.021909 |
| Safety = high and Persons = 4 and Buying = med | acc | 0.017926 |
| Persons = more and Safety = high and Maint = low and Lug_boot = med | acc | 0.007188 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = med | acc | 0.010743 |
| Persons = more and Safety = high and Buying = med and Doors = 5more | acc | 0.005513 |
| Persons = more and Safety = high and Maint = med and Doors = 4 | acc | 0.006295 |
| Safety = med and Persons = more and Lug_boot = big and Buying = med | acc | 0.010743 |
| Persons = 4 and Safety = high and Maint = low | acc | 0.016362 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.009857 |
| Persons = more and Safety = high and Maint = low and Lug_boot = big | acc | 0.006295 |
| Safety = med and Persons = more and Lug_boot = big and Maint = low | acc | 0.007188 |
| Safety = med and Persons = more and Maint = med and Lug_boot = big | acc | 0.006295 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.005401 |
| Persons = more and Safety = high and Buying = med and Doors = 3 | acc | 0.004633 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = low | acc | 0.007188 |
| Persons = more and Safety = high and Maint = med and Doors = 3 | acc | 0.004505 |
| Safety = med and Persons = more and Buying = low and Lug_boot = big | acc | 0.006295 |
| Safety = med and Persons = 4 and Buying = med and Lug_boot = big | acc | 0.005401 |
| Persons = more and Safety = high and Buying = med and Doors = 4 | acc | 0.002888 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med and Buying = med | acc | 0.003607 |
| Persons = 4 and Safety = high and Buying = low and Maint = vhigh | acc | 0.010743 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 5more | acc | 0.006622 |
| Safety = med and Persons = 4 and Buying = low and Lug_boot = big | acc | 0.003607 |
| Persons = more and Safety = high and Buying = high and Maint = high | acc | 0.007278 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more | acc | 0.004418 |
| Safety = med and Persons = more and Buying = low | acc | 0.007606 |
| Persons = 4 and Safety = high and Maint = high and Buying = high | acc | 0.009857 |
| Safety = med and Persons = 4 and Buying = med and Maint = low and Lug_boot = small | acc | 0.003607 |
| Persons = more and Safety = high and Maint = med and Doors = 5more | acc | 0.004505 |
| Safety = med and Persons = more and Lug_boot = med and Doors = 4 | acc | 0.003610 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.004020 |
| Persons = more and Safety = high and Maint = low | acc | 0.002508 |
| Safety = med and Persons = more and Doors = 3 and Lug_boot = med | acc | 0.003223 |
| Safety = med and Persons = 4 and Buying = low and Maint = med | acc | 0.004058 |
| Maint = high and Persons = 4 and Buying = low and Safety = high and Lug_boot = small | acc | 0.003607 |
| Persons = more and Safety = high and Doors = 2 and Lug_boot = med | acc | 0.005513 |
| Safety = med and Persons = more and Lug_boot = big and Buying = high and Maint = high | acc | 0.003607 |
|  | unacc | 0.960317 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|doors|persons|lug_boot|safety|acceptability
---|---|---|---|---|---|---
vhigh|low|5more|more|big|high|unacc
med|low|5more|more|big|high|unacc
low|low|5more|more|big|high|unacc
high|low|5more|more|big|high|unacc
high|med|5more|more|big|high|unacc
low|med|5more|more|big|high|unacc
med|med|5more|more|big|high|unacc
low|high|5more|more|big|high|unacc
med|low|4|more|big|high|unacc
high|low|4|more|big|high|unacc
med|high|5more|more|big|high|unacc
low|low|4|more|big|high|unacc
high|high|5more|more|big|high|unacc
vhigh|high|5more|more|big|high|unacc
low|vhigh|5more|more|big|high|unacc
med|low|5more|4|big|high|unacc
vhigh|low|5more|4|big|high|unacc
med|vhigh|5more|more|big|high|unacc
high|low|5more|4|big|high|unacc
high|med|4|more|big|high|unacc
med|med|4|more|big|high|unacc
low|med|4|more|big|high|unacc
vhigh|med|4|more|big|high|unacc
low|low|5more|4|big|high|unacc
med|low|5more|more|med|high|unacc
low|high|4|more|big|high|unacc
med|low|3|more|big|high|unacc
vhigh|med|5more|4|big|high|unacc
low|low|5more|more|med|high|unacc
high|low|5more|more|med|high|unacc
vhigh|low|5more|more|med|high|unacc
med|high|4|more|big|high|unacc
vhigh|high|4|more|big|high|unacc
high|low|3|more|big|high|unacc
low|low|3|more|big|high|unacc
med|med|5more|4|big|high|unacc
vhigh|low|3|more|big|high|unacc
high|med|5more|4|big|high|unacc
low|high|5more|4|big|high|unacc
high|high|5more|4|big|high|unacc
low|low|4|4|big|high|unacc
low|med|3|more|big|high|unacc
high|med|5more|more|med|high|unacc
high|med|3|more|big|high|unacc
vhigh|high|5more|4|big|high|unacc
med|low|4|4|big|high|unacc
vhigh|med|3|more|big|high|unacc
med|med|5more|more|med|high|unacc
low|med|5more|more|med|high|unacc
low|low|5more|more|big|med|unacc
vhigh|med|5more|more|med|high|unacc
high|low|5more|more|big|med|unacc
vhigh|vhigh|4|more|big|high|unacc
high|low|4|4|big|high|unacc
med|high|5more|4|big|high|unacc
vhigh|low|4|4|big|high|unacc
med|low|5more|more|big|med|unacc
vhigh|low|5more|more|big|med|unacc
vhigh|med|4|4|big|high|unacc
med|vhigh|5more|4|big|high|unacc
high|med|5more|more|big|med|unacc
vhigh|low|2|more|big|high|unacc
med|low|4|more|med|high|unacc
high|med|4|4|big|high|unacc
high|low|5more|2|big|high|unacc
vhigh|low|5more|2|big|high|unacc
vhigh|high|3|more|big|high|unacc
high|low|4|more|med|high|unacc
vhigh|vhigh|5more|4|big|high|unacc
low|med|4|4|big|high|unacc
low|low|2|more|big|high|unacc
med|med|4|4|big|high|unacc
high|high|3|more|big|high|unacc
med|high|5more|more|med|high|unacc
high|high|5more|more|med|high|unacc
high|low|2|more|big|high|unacc
med|low|5more|2|big|high|unacc
low|high|3|more|big|high|unacc
low|high|5more|more|med|high|unacc
low|med|5more|more|big|med|unacc
med|med|5more|more|big|med|unacc
low|vhigh|5more|4|big|high|unacc
vhigh|low|4|more|med|high|unacc
vhigh|med|5more|more|big|med|unacc
high|vhigh|5more|4|big|high|unacc
vhigh|high|5more|more|med|high|unacc
low|low|4|more|med|high|unacc
low|low|5more|2|big|high|unacc
med|med|4|more|med|high|unacc
med|low|4|more|big|med|unacc
med|vhigh|5more|more|med|high|unacc
vhigh|vhigh|3|more|big|high|unacc
low|high|4|4|big|high|unacc
low|low|3|4|big|high|unacc
vhigh|low|3|4|big|high|unacc
high|med|4|more|med|high|unacc
high|low|5more|4|med|high|unacc
high|vhigh|5more|more|med|high|unacc
vhigh|high|4|4|big|high|unacc
low|med|5more|2|big|high|unacc
high|med|5more|2|big|high|unacc
med|low|3|4|big|high|unacc
low|low|4|more|big|med|unacc
med|high|4|4|big|high|unacc
vhigh|med|4|more|med|high|unacc
med|high|5more|more|big|med|unacc
high|vhigh|3|more|big|high|unacc
med|med|5more|2|big|high|unacc
vhigh|vhigh|5more|more|med|high|unacc
high|high|5more|more|big|med|unacc
low|vhigh|3|more|big|high|unacc
low|med|2|more|big|high|unacc
low|med|4|more|med|high|unacc
low|low|5more|4|med|high|unacc
med|vhigh|3|more|big|high|unacc
med|low|5more|4|med|high|unacc
low|vhigh|5more|more|med|high|unacc
high|low|4|more|big|med|unacc
high|high|4|4|big|high|unacc
vhigh|low|4|more|big|med|unacc
vhigh|med|2|more|big|high|unacc
vhigh|high|5more|more|big|med|unacc
low|med|5more|4|med|high|unacc
med|low|5more|more|small|high|unacc
med|vhigh|4|4|big|high|unacc
high|low|5more|more|small|high|unacc
low|low|4|2|big|high|unacc
med|low|4|2|big|high|unacc
med|low|5more|4|big|med|unacc
low|med|4|more|big|med|unacc
med|med|4|more|big|med|unacc
vhigh|low|5more|more|small|high|unacc
vhigh|vhigh|4|4|big|high|unacc
med|med|5more|4|med|high|unacc
high|low|3|more|med|high|unacc
med|vhigh|5more|more|big|med|unacc
high|high|4|more|med|high|unacc
low|vhigh|4|4|big|high|unacc
med|high|5more|2|big|high|unacc
vhigh|high|5more|2|big|high|unacc
low|high|4|more|med|high|unacc
high|med|3|4|big|high|unacc
high|high|2|more|big|high|unacc
vhigh|med|5more|4|med|high|unacc
high|low|5more|4|big|med|unacc
high|high|5more|2|big|high|unacc
high|vhigh|4|4|big|high|unacc
med|high|2|more|big|high|unacc
high|med|5more|4|med|high|unacc
med|high|4|more|med|high|unacc
vhigh|high|2|more|big|high|unacc
vhigh|high|4|more|med|high|unacc
low|high|5more|2|big|high|unacc
low|low|3|more|med|high|unacc
low|high|2|more|big|high|unacc
med|low|3|more|med|high|unacc
low|med|3|4|big|high|unacc
low|low|5more|more|small|high|unacc
vhigh|low|3|more|med|high|unacc
high|med|4|more|big|med|unacc
low|vhigh|5more|more|big|med|unacc
vhigh|low|5more|4|big|med|unacc
vhigh|med|3|4|big|high|unacc
high|vhigh|5more|more|big|med|unacc
vhigh|low|4|2|big|high|unacc
high|low|4|2|big|high|unacc
low|med|3|more|med|high|unacc
low|high|5more|4|med|high|unacc
low|low|3|more|big|med|unacc
med|med|5more|4|big|med|unacc
vhigh|low|5more|more|med|med|unacc
vhigh|med|5more|4|big|med|unacc
vhigh|med|5more|more|small|high|unacc
high|med|3|more|med|high|unacc
vhigh|med|4|2|big|high|unacc
low|high|3|4|big|high|unacc
med|low|2|4|big|high|unacc
med|high|4|more|big|med|unacc
high|high|4|more|big|med|unacc
med|vhigh|2|more|big|high|unacc
high|low|5more|more|med|med|unacc
high|med|5more|more|small|high|unacc
vhigh|vhigh|4|more|med|high|unacc
vhigh|high|3|4|big|high|unacc
med|med|3|more|med|high|unacc
low|low|5more|more|med|med|unacc
vhigh|low|4|4|med|high|unacc
high|med|5more|4|big|med|unacc
high|high|5more|4|med|high|unacc
vhigh|vhigh|2|more|big|high|unacc
low|med|5more|more|small|high|unacc
low|med|5more|4|big|med|unacc
high|low|2|4|big|high|unacc
low|high|4|more|big|med|unacc
med|med|5more|more|small|high|unacc
high|med|4|2|big|high|unacc
vhigh|high|5more|4|med|high|unacc
vhigh|vhigh|5more|2|big|high|unacc
med|low|5more|more|med|med|unacc
med|low|4|4|med|high|unacc
low|low|2|4|big|high|unacc
vhigh|low|3|more|big|med|unacc
med|high|3|4|big|high|unacc
high|high|3|4|big|high|unacc
high|low|4|4|med|high|unacc
high|low|3|more|big|med|unacc
low|vhigh|2|more|big|high|unacc
low|med|4|2|big|high|unacc
high|vhigh|4|more|med|high|unacc
high|vhigh|2|more|big|high|unacc
vhigh|high|4|more|big|med|unacc
med|med|2|4|big|high|unacc
low|high|3|more|med|high|unacc
low|high|5more|4|big|med|unacc
high|low|4|more|small|high|unacc
high|med|5more|more|med|med|unacc
high|high|3|more|med|high|unacc
high|low|5more|2|med|high|unacc
low|low|5more|2|med|high|unacc
med|low|3|2|big|high|unacc
vhigh|high|4|2|big|high|unacc
low|low|4|4|big|med|unacc
med|low|4|4|big|med|unacc
med|med|5more|more|med|med|unacc
med|vhigh|3|4|big|high|unacc
low|vhigh|3|4|big|high|unacc
med|vhigh|5more|4|med|high|unacc
vhigh|high|5more|4|big|med|unacc
vhigh|vhigh|3|4|big|high|unacc
high|high|4|2|big|high|unacc
low|med|4|4|med|high|unacc
low|med|3|more|big|med|unacc
med|low|4|more|small|high|unacc
high|med|4|4|med|high|unacc
high|med|2|4|big|high|unacc
vhigh|low|4|4|big|med|unacc
vhigh|low|4|more|small|high|unacc
med|vhigh|4|more|big|med|unacc
med|low|5more|2|med|high|unacc
med|low|5more|more|big|low|unacc
med|high|4|2|big|high|unacc
low|low|3|2|big|high|unacc
vhigh|low|3|2|big|high|unacc
low|high|4|2|big|high|unacc
med|med|4|4|med|high|unacc
low|low|2|more|med|high|unacc
high|low|4|4|big|med|unacc
med|high|5more|more|small|high|unacc
med|high|3|more|med|high|unacc
vhigh|vhigh|4|more|big|med|unacc
low|med|2|4|big|high|unacc
vhigh|low|2|more|med|high|unacc
low|vhigh|5more|4|med|high|unacc
high|low|2|more|med|high|unacc
low|vhigh|4|more|big|med|unacc
vhigh|med|5more|more|med|med|unacc
vhigh|med|4|4|med|high|unacc
med|med|3|more|big|med|unacc
vhigh|med|2|4|big|high|unacc
vhigh|high|3|more|med|high|unacc
high|vhigh|3|4|big|high|unacc
vhigh|low|5more|more|big|low|unacc
high|vhigh|5more|4|med|high|unacc
low|low|4|more|small|high|unacc
low|high|5more|more|small|high|unacc
vhigh|med|3|more|big|med|unacc
med|high|5more|4|big|med|unacc
high|high|5more|more|small|high|unacc
high|med|3|more|big|med|unacc
vhigh|low|5more|2|med|high|unacc
high|low|3|2|big|high|unacc
high|vhigh|4|more|big|med|unacc
high|low|5more|more|big|low|unacc
med|low|2|more|big|med|unacc
vhigh|low|3|4|med|high|unacc
high|low|2|more|big|med|unacc
med|high|2|4|big|high|unacc
high|high|2|4|big|high|unacc
vhigh|med|4|4|big|med|unacc
low|vhigh|3|more|med|high|unacc
med|med|3|2|big|high|unacc
vhigh|vhigh|5more|4|big|med|unacc
high|med|5more|2|med|high|unacc
low|vhigh|4|2|big|high|unacc
low|med|3|2|big|high|unacc
low|med|2|more|med|high|unacc
low|med|4|more|small|high|unacc
med|high|5more|more|med|med|unacc
low|vhigh|5more|more|small|high|unacc
low|high|3|more|big|med|unacc
med|vhigh|5more|more|small|high|unacc
med|med|4|more|small|high|unacc
med|med|4|4|big|med|unacc
high|high|3|more|big|med|unacc
vhigh|vhigh|5more|more|small|high|unacc
vhigh|high|5more|more|med|med|unacc
vhigh|high|3|more|big|med|unacc
low|high|2|4|big|high|unacc
low|low|4|more|med|med|unacc
med|low|3|4|med|high|unacc
low|med|4|4|big|med|unacc
vhigh|low|4|more|med|med|unacc
low|vhigh|5more|4|big|med|unacc
high|low|4|more|med|med|unacc
high|low|3|4|med|high|unacc
vhigh|low|2|more|big|med|unacc
high|high|5more|more|med|med|unacc
med|med|5more|more|big|low|unacc
low|med|5more|more|big|low|unacc
vhigh|med|3|2|big|high|unacc
high|vhigh|4|2|big|high|unacc
low|low|5more|2|big|med|unacc
vhigh|low|5more|2|big|med|unacc
med|med|5more|2|med|high|unacc
vhigh|vhigh|3|more|med|high|unacc
vhigh|med|5more|more|big|low|unacc
med|high|4|4|med|high|unacc
high|high|4|4|med|high|unacc
high|med|4|more|small|high|unacc
vhigh|med|2|more|med|high|unacc
high|vhigh|5more|more|small|high|unacc
high|vhigh|3|more|med|high|unacc
med|vhigh|4|2|big|high|unacc
high|med|3|2|big|high|unacc
med|low|4|more|med|med|unacc
low|low|2|more|big|med|unacc
med|med|2|more|med|high|unacc
high|low|5more|4|small|high|unacc
high|med|4|4|big|med|unacc
vhigh|low|5more|4|small|high|unacc
vhigh|med|4|more|small|high|unacc
vhigh|vhigh|4|2|big|high|unacc
vhigh|high|4|4|med|high|unacc
high|low|5more|2|big|med|unacc
low|high|4|4|med|high|unacc
low|low|3|4|med|high|unacc
med|low|5more|4|small|high|unacc
low|high|5more|more|med|med|unacc
med|vhigh|5more|4|big|med|unacc
med|high|3|more|big|med|unacc
high|med|2|more|med|high|unacc
med|vhigh|3|more|med|high|unacc
vhigh|med|5more|2|med|high|unacc
high|med|5more|more|big|low|unacc
high|vhigh|5more|4|big|med|unacc
vhigh|high|2|4|big|high|unacc
low|low|5more|4|med|med|unacc
low|med|3|4|med|high|unacc
low|low|3|more|small|high|unacc
med|med|2|more|big|med|unacc
vhigh|med|2|more|big|med|unacc
med|vhigh|2|4|big|high|unacc
low|high|2|more|med|high|unacc
high|high|4|more|small|high|unacc
med|high|3|2|big|high|unacc
vhigh|high|5more|2|med|high|unacc
vhigh|vhigh|5more|more|med|med|unacc
high|vhigh|3|more|big|med|unacc
high|low|4|2|med|high|unacc
vhigh|high|4|4|big|med|unacc
med|vhigh|5more|more|med|med|unacc
high|med|4|more|med|med|unacc
vhigh|low|3|4|big|med|unacc
high|vhigh|2|4|big|high|unacc
low|low|4|2|med|high|unacc
vhigh|med|5more|2|big|med|unacc
low|low|4|more|big|low|unacc
vhigh|vhigh|3|more|big|med|unacc
low|med|2|more|big|med|unacc
med|low|3|4|big|med|unacc
med|vhigh|4|4|med|high|unacc
vhigh|med|4|more|med|med|unacc
low|vhigh|3|more|big|med|unacc
high|low|3|4|big|med|unacc
high|high|4|4|big|med|unacc
vhigh|med|5more|4|small|high|unacc
med|med|5more|2|big|med|unacc
med|low|2|2|big|high|unacc
med|low|4|more|big|low|unacc
vhigh|high|4|more|small|high|unacc
med|high|5more|more|big|low|unacc
high|high|5more|2|med|high|unacc
low|med|5more|4|small|high|unacc
med|vhigh|3|more|big|med|unacc
high|med|5more|4|small|high|unacc
low|vhigh|4|4|med|high|unacc
med|high|2|more|med|high|unacc
vhigh|med|3|4|med|high|unacc
med|low|4|2|med|high|unacc
high|low|4|more|big|low|unacc
high|vhigh|4|4|med|high|unacc
vhigh|low|4|more|big|low|unacc
vhigh|low|4|2|med|high|unacc
vhigh|vhigh|2|4|big|high|unacc
low|low|3|4|big|med|unacc
med|low|3|more|small|high|unacc
low|med|4|more|med|med|unacc
high|med|3|4|med|high|unacc
low|high|4|more|small|high|unacc
med|med|5more|4|small|high|unacc
vhigh|low|3|more|small|high|unacc
med|med|4|more|med|med|unacc
low|high|3|2|big|high|unacc
low|high|5more|more|big|low|unacc
vhigh|high|5more|more|big|low|unacc
vhigh|low|2|2|big|high|unacc
vhigh|low|5more|4|med|med|unacc
low|vhigh|5more|more|med|med|unacc
high|med|2|more|big|med|unacc
low|vhigh|2|4|big|high|unacc
med|high|4|4|big|med|unacc
med|high|4|more|small|high|unacc
high|low|3|more|small|high|unacc
med|med|3|4|med|high|unacc
low|high|4|4|big|med|unacc
vhigh|high|3|2|big|high|unacc
high|high|5more|more|big|low|unacc
low|low|2|2|big|high|unacc
med|high|5more|2|med|high|unacc
high|high|3|2|big|high|unacc
vhigh|vhigh|4|4|med|high|unacc
low|high|5more|2|med|high|unacc
med|low|2|4|med|high|unacc
low|med|3|4|big|med|unacc
low|high|2|more|big|med|unacc
vhigh|low|2|4|med|high|unacc
high|low|5more|more|small|med|unacc
high|vhigh|4|4|big|med|unacc
high|med|2|2|big|high|unacc
med|low|3|more|med|med|unacc
high|med|5more|4|med|med|unacc
low|low|5more|more|small|med|unacc
high|med|3|4|big|med|unacc
high|high|3|4|med|high|unacc
vhigh|med|3|4|big|med|unacc
high|low|2|4|med|high|unacc
high|low|3|more|med|med|unacc
med|high|5more|4|small|high|unacc
low|high|4|more|med|med|unacc
low|vhigh|4|more|small|high|unacc
med|med|5more|4|med|med|unacc
vhigh|med|5more|4|med|med|unacc
high|vhigh|5more|2|med|high|unacc
vhigh|high|5more|4|small|high|unacc
med|low|5more|4|big|low|unacc
low|med|2|2|big|high|unacc
vhigh|vhigh|4|4|big|med|unacc
high|high|5more|2|big|med|unacc
low|med|4|more|big|low|unacc
med|med|4|more|big|low|unacc
vhigh|vhigh|5more|2|med|high|unacc
vhigh|low|5more|4|big|low|unacc
high|vhigh|4|more|small|high|unacc
vhigh|high|4|more|med|med|unacc
low|med|5more|4|med|med|unacc
med|vhigh|2|more|med|high|unacc
vhigh|med|3|more|small|high|unacc
high|high|4|more|med|med|unacc
vhigh|low|3|more|med|med|unacc
low|high|5more|4|small|high|unacc
vhigh|med|4|2|med|high|unacc
high|med|4|more|big|low|unacc
med|low|4|2|big|med|unacc
vhigh|high|3|4|med|high|unacc
med|med|4|2|med|high|unacc
vhigh|low|5more|more|small|med|unacc
med|vhigh|5more|more|big|low|unacc
med|high|5more|2|big|med|unacc
vhigh|vhigh|2|more|med|high|unacc
high|vhigh|5more|more|big|low|unacc
low|med|3|more|small|high|unacc
med|med|3|4|big|med|unacc
high|low|4|4|small|high|unacc
low|vhigh|2|more|med|high|unacc
low|vhigh|4|4|big|med|unacc
med|high|3|4|med|high|unacc
low|vhigh|5more|more|big|low|unacc
vhigh|low|4|2|big|med|unacc
med|vhigh|3|2|big|high|unacc
vhigh|vhigh|4|more|small|high|unacc
high|vhigh|3|2|big|high|unacc
low|low|5more|4|big|low|unacc
vhigh|med|2|2|big|high|unacc
med|vhigh|5more|2|med|high|unacc
med|med|2|2|big|high|unacc
low|low|3|more|med|med|unacc
med|low|4|4|small|high|unacc
high|high|2|more|big|med|unacc
high|high|5more|4|small|high|unacc
med|vhigh|4|more|small|high|unacc
high|med|3|more|small|high|unacc
med|med|3|more|small|high|unacc
low|high|5more|2|big|med|unacc
vhigh|high|5more|2|big|med|unacc
low|vhigh|3|2|big|high|unacc
low|low|4|2|big|med|unacc
vhigh|high|2|more|big|med|unacc
high|low|4|2|big|med|unacc
low|low|4|4|small|high|unacc
low|low|2|4|med|high|unacc
vhigh|low|4|4|small|high|unacc
med|high|2|more|big|med|unacc
low|high|3|4|med|high|unacc
high|low|5more|4|big|low|unacc
low|vhigh|5more|2|med|high|unacc
vhigh|med|4|more|big|low|unacc
low|med|4|2|med|high|unacc
vhigh|vhigh|5more|more|big|low|unacc
med|low|2|4|big|med|unacc
high|med|4|4|small|high|unacc
med|high|3|4|big|med|unacc
high|med|2|4|med|high|unacc
med|high|3|more|small|high|unacc
med|med|4|4|small|high|unacc
low|vhigh|3|4|med|high|unacc
low|med|5more|4|big|low|unacc
low|low|3|2|med|high|unacc
vhigh|low|2|more|small|high|unacc
med|low|3|2|med|high|unacc
low|med|2|4|med|high|unacc
low|low|2|4|big|med|unacc
high|high|3|4|big|med|unacc
low|high|3|4|big|med|unacc
high|high|5more|4|med|med|unacc
low|vhigh|2|more|big|med|unacc
high|vhigh|2|more|big|med|unacc
vhigh|vhigh|4|more|med|med|unacc
vhigh|low|5more|more|med|low|unacc
high|vhigh|5more|2|big|med|unacc
high|med|5more|4|big|low|unacc
med|high|4|more|big|low|unacc
high|vhigh|4|more|med|med|unacc
med|high|2|2|big|high|unacc
vhigh|med|4|2|big|med|unacc
med|med|2|4|med|high|unacc
med|vhigh|4|more|med|med|unacc
vhigh|med|3|more|med|med|unacc
high|low|4|4|med|med|unacc
low|vhigh|5more|4|small|high|unacc
high|low|2|more|small|high|unacc
vhigh|vhigh|3|4|med|high|unacc
vhigh|low|5more|2|small|high|unacc
high|low|5more|more|med|low|unacc
low|high|2|2|big|high|unacc
vhigh|high|4|2|med|high|unacc
vhigh|high|3|more|small|high|unacc
med|low|4|4|med|med|unacc
high|high|3|more|small|high|unacc
med|vhigh|3|4|med|high|unacc
low|med|5more|more|small|med|unacc
med|med|4|2|big|med|unacc
high|high|4|2|med|high|unacc
low|high|4|more|big|low|unacc
vhigh|med|5more|4|big|low|unacc
low|low|2|more|small|high|unacc
low|high|4|2|med|high|unacc
med|vhigh|5more|2|big|med|unacc
med|high|4|2|med|high|unacc
low|low|3|more|big|low|unacc
vhigh|low|3|more|big|low|unacc
vhigh|high|2|2|big|high|unacc
vhigh|low|3|2|med|high|unacc
high|high|2|2|big|high|unacc
vhigh|vhigh|5more|4|small|high|unacc
low|low|4|4|med|med|unacc
med|med|5more|more|small|med|unacc
med|med|3|more|med|med|unacc
vhigh|low|2|4|big|med|unacc
med|high|5more|4|med|med|unacc
vhigh|med|2|4|med|high|unacc
vhigh|low|4|4|med|med|unacc
med|vhigh|2|more|big|med|unacc
high|low|2|4|big|med|unacc
vhigh|med|4|4|small|high|unacc
low|med|4|2|big|med|unacc
med|low|2|more|small|high|unacc
high|med|5more|more|small|med|unacc
high|low|5more|2|small|high|unacc
high|low|3|2|med|high|unacc
high|vhigh|3|4|med|high|unacc
high|med|4|2|big|med|unacc
med|low|3|more|big|low|unacc
low|vhigh|4|more|med|med|unacc
high|low|3|more|big|low|unacc
low|low|5more|2|small|high|unacc
low|low|5more|more|med|low|unacc
low|vhigh|5more|2|big|med|unacc
med|med|5more|4|big|low|unacc
med|low|5more|2|small|high|unacc
vhigh|vhigh|5more|2|big|med|unacc
low|vhigh|5more|4|med|med|unacc
vhigh|low|3|4|small|high|unacc
high|high|3|more|med|med|unacc
high|med|2|4|big|med|unacc
med|high|4|4|small|high|unacc
med|vhigh|3|more|small|high|unacc
med|med|2|4|big|med|unacc
low|low|5more|2|med|med|unacc
vhigh|vhigh|3|4|big|med|unacc
vhigh|vhigh|4|more|big|low|unacc
high|vhigh|3|more|small|high|unacc
low|med|5more|more|med|low|unacc
med|vhigh|4|2|med|high|unacc
med|med|5more|more|med|low|unacc
vhigh|high|5more|4|big|low|unacc
med|high|5more|more|small|med|unacc
high|high|5more|more|small|med|unacc
med|high|4|2|big|med|unacc
vhigh|vhigh|4|2|med|high|unacc
low|med|5more|2|small|high|unacc
vhigh|low|4|more|small|med|unacc
vhigh|low|2|more|med|med|unacc
med|low|4|4|big|low|unacc
high|low|4|more|small|med|unacc
low|vhigh|3|more|small|high|unacc
high|high|2|4|med|high|unacc
high|high|4|4|small|high|unacc
low|high|5more|more|small|med|unacc
high|vhigh|4|more|big|low|unacc
high|low|2|more|med|med|unacc
high|high|5more|4|big|low|unacc
high|vhigh|2|2|big|high|unacc
high|high|4|2|big|med|unacc
med|med|2|more|small|high|unacc
low|vhigh|3|4|big|med|unacc
med|low|2|more|med|med|unacc
low|low|4|more|small|med|unacc
vhigh|low|3|2|big|med|unacc
vhigh|vhigh|5more|4|med|med|unacc
vhigh|low|4|4|big|low|unacc
vhigh|low|5more|2|med|med|unacc
low|med|2|4|big|med|unacc
vhigh|med|4|4|med|med|unacc
med|low|4|more|small|med|unacc
low|high|2|4|med|high|unacc
med|vhigh|3|4|big|med|unacc
med|med|4|4|med|med|unacc
med|vhigh|4|more|big|low|unacc
med|med|5more|2|small|high|unacc
med|low|5more|2|med|med|unacc
vhigh|med|5more|2|small|high|unacc
high|vhigh|3|4|big|med|unacc
low|high|5more|4|big|low|unacc
vhigh|high|5more|more|small|med|unacc
med|low|3|2|big|med|unacc
low|med|3|2|med|high|unacc
vhigh|med|2|4|big|med|unacc
med|vhigh|5more|4|med|med|unacc
low|low|2|more|med|med|unacc
vhigh|vhigh|2|2|big|high|unacc
vhigh|high|4|4|small|high|unacc
low|vhigh|2|2|big|high|unacc
high|med|2|more|small|high|unacc
vhigh|med|5more|more|med|low|unacc
low|vhigh|4|more|big|low|unacc
med|vhigh|2|2|big|high|unacc
vhigh|med|2|more|small|high|unacc
high|low|3|2|big|med|unacc
vhigh|high|2|4|med|high|unacc
vhigh|med|3|more|big|low|unacc
med|high|5more|4|big|low|unacc
high|med|5more|2|small|high|unacc
low|med|2|more|small|high|unacc
low|med|4|4|med|med|unacc
low|low|3|4|small|high|unacc
high|low|3|4|small|high|unacc
med|high|3|more|med|med|unacc
low|high|3|more|med|med|unacc
low|high|4|4|small|high|unacc
med|high|2|4|med|high|unacc
high|med|4|4|med|med|unacc
med|med|3|2|med|high|unacc
high|med|5more|more|med|low|unacc
med|med|3|more|big|low|unacc
high|vhigh|5more|4|med|med|unacc
high|med|3|2|med|high|unacc
vhigh|high|4|2|big|med|unacc
low|low|3|2|big|med|unacc
vhigh|vhigh|3|more|small|high|unacc
low|vhigh|2|4|med|high|unacc
low|low|2|more|big|low|unacc
high|vhigh|4|4|small|high|unacc
med|med|3|2|big|med|unacc
vhigh|low|4|more|med|low|unacc
med|med|4|4|big|low|unacc
high|high|5more|more|med|low|unacc
high|low|2|more|big|low|unacc
med|high|2|more|small|high|unacc
med|high|5more|more|med|low|unacc
low|high|5more|2|small|high|unacc
high|med|5more|2|med|med|unacc
med|high|3|2|med|high|unacc
high|low|5more|2|big|low|unacc
low|med|4|4|big|low|unacc
low|med|3|4|small|high|unacc
med|vhigh|2|4|med|high|unacc
low|high|4|4|med|med|unacc
low|vhigh|4|4|small|high|unacc
med|low|2|2|med|high|unacc
high|low|4|2|small|high|unacc
med|vhigh|5more|more|small|med|unacc
low|low|4|2|small|high|unacc
low|high|3|2|med|high|unacc
vhigh|vhigh|3|more|med|med|unacc
low|vhigh|5more|4|big|low|unacc
vhigh|low|4|2|small|high|unacc
med|vhigh|5more|4|big|low|unacc
med|vhigh|4|4|small|high|unacc
med|high|4|4|med|med|unacc
med|med|3|4|small|high|unacc
high|high|4|4|med|med|unacc
high|high|5more|2|small|high|unacc
med|low|2|more|big|low|unacc
high|vhigh|5more|4|big|low|unacc
low|vhigh|4|2|big|med|unacc
high|med|4|more|small|med|unacc
vhigh|low|5more|4|small|med|unacc
high|vhigh|3|more|med|med|unacc
high|med|3|2|big|med|unacc
med|vhigh|4|2|big|med|unacc
low|high|3|more|big|low|unacc
vhigh|high|5more|2|small|high|unacc
high|high|2|more|small|high|unacc
vhigh|low|2|more|big|low|unacc
vhigh|vhigh|5more|more|small|med|unacc
med|low|3|4|med|med|unacc
high|med|3|4|small|high|unacc
med|med|2|more|med|med|unacc
med|med|4|more|small|med|unacc
low|med|4|more|small|med|unacc
vhigh|high|3|2|med|high|unacc
low|med|5more|2|med|med|unacc
med|low|5more|2|big|low|unacc
med|low|4|more|med|low|unacc
vhigh|vhigh|2|4|med|high|unacc
low|vhigh|5more|more|small|med|unacc
high|low|2|2|med|high|unacc
high|low|4|more|med|low|unacc
high|high|2|4|big|med|unacc
med|low|5more|4|small|med|unacc
low|high|2|4|big|med|unacc
high|med|4|4|big|low|unacc
vhigh|low|2|2|med|high|unacc
low|high|5more|more|med|low|unacc
high|vhigh|4|2|big|med|unacc
vhigh|low|3|4|med|med|unacc
high|vhigh|5more|more|small|med|unacc
med|high|5more|2|small|high|unacc
vhigh|vhigh|4|2|big|med|unacc
high|high|3|more|big|low|unacc
vhigh|high|3|more|big|low|unacc
high|med|2|more|med|med|unacc
high|high|3|2|med|high|unacc
med|low|4|2|small|high|unacc
vhigh|high|2|4|big|med|unacc
low|low|2|2|med|high|unacc
vhigh|med|2|more|med|med|unacc
vhigh|med|5more|2|med|med|unacc
vhigh|low|5more|2|big|low|unacc
vhigh|med|3|4|small|high|unacc
low|high|2|more|small|high|unacc
high|low|5more|4|small|med|unacc
vhigh|med|4|4|big|low|unacc
vhigh|high|5more|more|med|low|unacc
high|low|3|4|med|med|unacc
low|low|5more|2|big|low|unacc
vhigh|vhigh|5more|4|big|low|unacc
vhigh|vhigh|4|4|small|high|unacc
med|med|5more|2|med|med|unacc
low|med|3|2|big|med|unacc
vhigh|med|3|2|big|med|unacc
med|high|3|4|small|high|unacc
low|med|3|4|med|med|unacc
low|vhigh|2|4|big|med|unacc
low|med|5more|4|small|med|unacc
low|low|2|2|big|med|unacc
med|low|3|4|big|low|unacc
high|med|4|more|med|low|unacc
high|vhigh|2|4|big|med|unacc
low|med|2|2|med|high|unacc
high|med|4|2|small|high|unacc
high|vhigh|5more|more|med|low|unacc
vhigh|low|4|2|med|med|unacc
med|vhigh|3|more|big|low|unacc
med|med|2|more|big|low|unacc
low|vhigh|2|more|small|high|unacc
high|low|4|2|med|med|unacc
high|high|3|2|big|med|unacc
vhigh|high|2|more|med|med|unacc
med|low|5more|4|med|low|unacc
vhigh|high|3|2|big|med|unacc
high|med|5more|4|small|med|unacc
high|vhigh|3|2|med|high|unacc
high|low|5more|4|med|low|unacc
vhigh|vhigh|2|4|big|med|unacc
high|med|2|2|med|high|unacc
high|med|3|4|med|med|unacc
high|vhigh|4|4|med|med|unacc
vhigh|low|2|4|small|high|unacc
med|vhigh|2|4|big|med|unacc
vhigh|high|5more|2|med|med|unacc
vhigh|low|3|4|big|low|unacc
med|high|4|more|small|med|unacc
high|high|2|more|med|med|unacc
low|med|2|more|big|low|unacc
med|vhigh|5more|more|med|low|unacc
vhigh|med|2|2|med|high|unacc
med|med|4|2|small|high|unacc
vhigh|vhigh|4|4|med|med|unacc
vhigh|low|3|more|small|med|unacc
med|high|3|2|big|med|unacc
low|low|3|4|big|low|unacc
vhigh|high|3|4|small|high|unacc
low|vhigh|5more|more|med|low|unacc
low|high|4|more|small|med|unacc
vhigh|med|4|2|small|high|unacc
vhigh|med|5more|2|big|low|unacc
low|vhigh|3|more|big|low|unacc
med|low|2|2|big|med|unacc
high|high|4|4|big|low|unacc
med|med|4|more|med|low|unacc
high|low|3|more|small|med|unacc
high|low|3|4|big|low|unacc
high|med|5more|2|big|low|unacc
med|low|2|4|small|high|unacc
med|low|3|more|small|med|unacc
high|low|2|4|small|high|unacc
low|high|3|4|small|high|unacc
med|med|5more|2|big|low|unacc
high|med|2|more|big|low|unacc
high|vhigh|5more|2|small|high|unacc
vhigh|high|4|more|small|med|unacc
vhigh|med|4|more|med|low|unacc
low|med|5more|2|big|low|unacc
med|vhigh|3|2|med|high|unacc
vhigh|vhigh|3|2|med|high|unacc
med|high|2|more|med|med|unacc
med|med|3|4|med|med|unacc
low|high|3|2|big|med|unacc
vhigh|vhigh|5more|2|small|high|unacc
high|low|2|2|big|med|unacc
med|low|4|2|med|med|unacc
low|high|5more|2|med|med|unacc
high|vhigh|2|more|small|high|unacc
low|low|4|2|med|med|unacc
med|vhigh|2|more|small|high|unacc
low|low|5more|4|med|low|unacc
vhigh|vhigh|3|more|big|low|unacc
high|high|4|more|small|med|unacc
med|high|5more|2|med|med|unacc
vhigh|med|2|more|big|low|unacc
low|high|4|4|big|low|unacc
low|low|2|4|small|high|unacc
med|med|5more|4|small|med|unacc
low|high|2|more|med|med|unacc
med|vhigh|4|4|med|med|unacc
low|low|3|more|small|med|unacc
high|vhigh|3|more|big|low|unacc
low|vhigh|5more|2|small|high|unacc
med|high|4|4|big|low|unacc
vhigh|low|5more|4|med|low|unacc
vhigh|med|5more|4|small|med|unacc
low|med|4|2|small|high|unacc
vhigh|high|4|4|big|low|unacc
vhigh|vhigh|2|more|small|high|unacc
low|med|4|more|med|low|unacc
high|high|5more|2|med|med|unacc
vhigh|low|3|2|small|high|unacc
vhigh|high|4|more|med|low|unacc
med|low|3|2|small|high|unacc
low|vhigh|5more|2|med|med|unacc
med|med|4|2|med|med|unacc
vhigh|high|4|2|small|high|unacc
vhigh|low|5more|more|small|low|unacc
low|low|4|2|big|low|unacc
low|low|3|2|small|high|unacc
vhigh|med|3|4|big|low|unacc
low|high|5more|4|small|med|unacc
vhigh|med|2|4|small|high|unacc
med|low|5more|more|small|low|unacc
high|vhigh|4|more|small|med|unacc
high|med|4|2|med|med|unacc
vhigh|med|3|more|small|med|unacc
vhigh|high|5more|2|big|low|unacc
high|low|2|4|med|med|unacc
vhigh|vhigh|2|more|med|med|unacc
high|high|2|2|med|high|unacc
high|vhigh|2|more|med|med|unacc
low|high|3|4|med|med|unacc
low|vhigh|4|4|big|low|unacc
med|high|2|2|med|high|unacc
high|high|2|more|big|low|unacc
high|low|3|more|med|low|unacc
low|high|2|more|big|low|unacc
high|high|5more|4|small|med|unacc
vhigh|low|4|4|small|med|unacc
high|low|4|4|small|med|unacc
med|high|3|4|med|med|unacc
low|high|2|2|med|high|unacc
med|high|4|2|small|high|unacc
med|med|5more|4|med|low|unacc
vhigh|med|2|2|big|med|unacc
low|med|2|4|small|high|unacc
med|med|3|more|small|med|unacc
med|low|4|4|small|med|unacc
vhigh|vhigh|3|2|big|med|unacc
low|med|4|2|med|med|unacc
med|vhigh|2|more|med|med|unacc
med|vhigh|3|2|big|med|unacc
high|med|2|2|big|med|unacc
low|med|2|2|big|med|unacc
high|high|5more|2|big|low|unacc
low|vhigh|2|more|med|med|unacc
vhigh|high|2|2|med|high|unacc
high|high|4|2|small|high|unacc
med|high|2|more|big|low|unacc
high|high|3|4|med|med|unacc
vhigh|med|4|2|med|med|unacc
low|low|5more|more|small|low|unacc
vhigh|vhigh|4|4|big|low|unacc
med|vhigh|3|4|small|high|unacc
low|low|4|4|small|med|unacc
low|vhigh|3|4|small|high|unacc
high|med|3|4|big|low|unacc
high|vhigh|3|4|small|high|unacc
high|low|3|2|small|high|unacc
high|low|4|2|big|low|unacc
low|high|4|2|small|high|unacc
vhigh|low|2|4|med|med|unacc
high|high|4|more|med|low|unacc
med|med|3|4|big|low|unacc
med|high|4|more|med|low|unacc
med|high|5more|4|small|med|unacc
high|vhigh|5more|2|med|med|unacc
low|vhigh|3|2|big|med|unacc
high|low|5more|more|small|low|unacc
vhigh|low|4|2|big|low|unacc
med|vhigh|4|4|big|low|unacc
med|low|2|4|med|med|unacc
high|med|2|4|small|high|unacc
low|low|3|more|med|low|unacc
med|med|2|2|big|med|unacc
med|low|4|2|big|low|unacc
med|vhigh|5more|2|med|med|unacc
high|vhigh|4|4|big|low|unacc
vhigh|vhigh|5more|2|med|med|unacc
vhigh|vhigh|3|4|small|high|unacc
high|med|5more|4|med|low|unacc
med|low|3|more|med|low|unacc
low|med|3|4|big|low|unacc
high|vhigh|3|2|big|med|unacc
low|high|5more|2|big|low|unacc
vhigh|low|3|more|med|low|unacc
vhigh|vhigh|4|more|small|med|unacc
low|high|4|more|med|low|unacc
vhigh|high|3|4|med|med|unacc
low|med|4|4|small|med|unacc
low|high|2|4|small|high|unacc
med|high|2|4|small|high|unacc
vhigh|med|5more|more|small|low|unacc
high|low|5more|2|small|med|unacc
low|low|3|2|med|med|unacc
vhigh|high|2|2|big|med|unacc
vhigh|med|3|2|small|high|unacc
med|low|4|4|med|low|unacc
low|vhigh|2|2|med|high|unacc
vhigh|vhigh|5more|4|small|med|unacc
high|high|3|more|small|med|unacc
high|med|4|2|big|low|unacc
med|med|5more|more|small|low|unacc
high|med|3|more|med|low|unacc
high|med|5more|more|small|low|unacc
vhigh|vhigh|4|2|small|high|unacc
high|med|2|4|med|med|unacc
vhigh|low|5more|2|small|med|unacc
vhigh|high|4|2|med|med|unacc
low|vhigh|4|more|med|low|unacc
low|med|3|more|med|low|unacc
med|med|3|more|med|low|unacc
high|low|4|4|med|low|unacc
med|high|4|2|med|med|unacc
low|low|5more|2|small|med|unacc
med|vhigh|4|more|med|low|unacc
high|high|2|4|small|high|unacc
med|high|3|4|big|low|unacc
low|high|2|2|big|med|unacc
high|vhigh|2|2|med|high|unacc
high|low|2|4|big|low|unacc
vhigh|vhigh|3|4|med|med|unacc
vhigh|high|3|4|big|low|unacc
vhigh|med|2|4|med|med|unacc
vhigh|vhigh|2|more|big|low|unacc
med|vhigh|5more|2|big|low|unacc
vhigh|low|3|2|med|med|unacc
vhigh|high|2|4|small|high|unacc
high|vhigh|3|4|med|med|unacc
vhigh|low|2|4|big|low|unacc
high|low|3|2|med|med|unacc
high|high|4|2|med|med|unacc
low|low|2|4|big|low|unacc
low|high|4|2|med|med|unacc
low|low|4|4|med|low|unacc
med|high|3|more|small|med|unacc
med|med|4|2|big|low|unacc
low|med|2|4|med|med|unacc
med|high|5more|4|med|low|unacc
high|med|4|4|small|med|unacc
low|med|4|2|big|low|unacc
high|high|2|2|big|med|unacc
low|vhigh|5more|2|big|low|unacc
vhigh|med|4|4|small|med|unacc
low|med|5more|more|small|low|unacc
vhigh|high|3|more|small|med|unacc
vhigh|high|5more|4|med|low|unacc
med|high|2|2|big|med|unacc
med|vhigh|4|2|small|high|unacc
med|vhigh|2|more|big|low|unacc
vhigh|low|2|more|small|med|unacc
high|vhigh|2|more|big|low|unacc
vhigh|med|3|more|med|low|unacc
low|vhigh|4|2|small|high|unacc
low|high|3|more|small|med|unacc
med|med|4|4|small|med|unacc
low|low|2|more|small|med|unacc
high|vhigh|5more|4|small|med|unacc
med|med|3|2|small|high|unacc
vhigh|vhigh|5more|2|big|low|unacc
vhigh|vhigh|4|more|med|low|unacc
high|high|3|4|big|low|unacc
med|low|2|more|small|med|unacc
high|vhigh|5more|2|big|low|unacc
med|low|5more|2|small|med|unacc
vhigh|vhigh|2|2|med|high|unacc
low|vhigh|2|more|big|low|unacc
med|low|3|2|med|med|unacc
vhigh|med|4|2|big|low|unacc
low|vhigh|5more|4|small|med|unacc
high|med|3|2|small|high|unacc
vhigh|low|4|4|med|low|unacc
low|high|3|4|big|low|unacc
low|med|3|2|small|high|unacc
med|low|2|4|big|low|unacc
med|vhigh|5more|4|small|med|unacc
med|vhigh|2|4|small|high|unacc
low|low|3|4|small|med|unacc
vhigh|low|2|more|med|low|unacc
low|low|2|more|med|low|unacc
high|med|2|more|small|med|unacc
high|med|2|4|big|low|unacc
high|low|3|2|big|low|unacc
high|high|4|2|big|low|unacc
med|vhigh|4|2|med|med|unacc
med|med|3|2|med|med|unacc
high|med|3|2|med|med|unacc
med|vhigh|3|more|small|med|unacc
high|low|2|more|med|low|unacc
vhigh|high|3|2|small|high|unacc
low|med|2|more|small|med|unacc
med|vhigh|5more|4|med|low|unacc
low|med|2|4|big|low|unacc
low|high|4|4|small|med|unacc
med|med|4|4|med|low|unacc
med|high|4|2|big|low|unacc
vhigh|vhigh|4|2|med|med|unacc
vhigh|high|4|2|big|low|unacc
high|low|2|2|small|high|unacc
med|high|5more|more|small|low|unacc
low|high|3|more|med|low|unacc
vhigh|vhigh|2|4|small|high|unacc
med|low|2|more|med|low|unacc
vhigh|low|2|2|small|high|unacc
high|high|5more|more|small|low|unacc
vhigh|vhigh|3|more|small|med|unacc
med|low|3|2|big|low|unacc
high|high|3|more|med|low|unacc
med|low|5more|2|med|low|unacc
high|vhigh|4|2|med|med|unacc
low|high|2|4|med|med|unacc
low|vhigh|5more|4|med|low|unacc
high|med|5more|2|small|med|unacc
vhigh|low|3|2|big|low|unacc
vhigh|med|4|4|med|low|unacc
low|high|5more|more|small|low|unacc
vhigh|med|3|2|med|med|unacc
med|med|5more|2|small|med|unacc
high|vhigh|3|more|small|med|unacc
med|med|2|more|small|med|unacc
high|vhigh|5more|4|med|low|unacc
vhigh|med|2|more|small|med|unacc
low|med|5more|2|small|med|unacc
low|high|3|2|small|high|unacc
vhigh|high|2|4|med|med|unacc
vhigh|high|4|4|small|med|unacc
low|vhigh|2|4|small|high|unacc
high|low|5more|2|med|low|unacc
vhigh|vhigh|5more|4|med|low|unacc
low|vhigh|3|more|small|med|unacc
low|vhigh|4|2|med|med|unacc
vhigh|high|5more|more|small|low|unacc
med|high|4|4|small|med|unacc
vhigh|low|4|more|small|low|unacc
high|vhigh|2|2|big|med|unacc
vhigh|low|5more|2|med|low|unacc
med|high|2|4|med|med|unacc
med|low|4|more|small|low|unacc
med|high|3|2|small|high|unacc
vhigh|low|3|4|small|med|unacc
vhigh|vhigh|3|4|big|low|unacc
vhigh|med|5more|2|small|med|unacc
low|low|2|2|small|high|unacc
vhigh|vhigh|2|2|big|med|unacc
high|high|3|2|small|high|unacc
high|high|2|4|med|med|unacc
low|med|3|2|med|med|unacc
low|med|4|4|med|low|unacc
low|low|4|more|small|low|unacc
vhigh|med|2|4|big|low|unacc
low|vhigh|2|2|big|med|unacc
high|low|3|4|small|med|unacc
med|low|2|2|small|high|unacc
med|low|3|4|small|med|unacc
low|high|4|2|big|low|unacc
med|high|3|more|med|low|unacc
high|vhigh|2|4|small|high|unacc
med|vhigh|3|4|big|low|unacc
high|low|4|more|small|low|unacc
med|vhigh|2|2|big|med|unacc
vhigh|high|3|more|med|low|unacc
low|vhigh|3|more|med|low|unacc
med|vhigh|4|4|small|med|unacc
high|med|5more|2|med|low|unacc
vhigh|vhigh|2|4|med|med|unacc
vhigh|vhigh|4|4|small|med|unacc
med|med|5more|2|med|low|unacc
vhigh|low|4|2|small|med|unacc
low|high|2|4|big|low|unacc
high|high|3|2|med|med|unacc
low|high|3|2|med|med|unacc
low|med|4|more|small|low|unacc
low|vhigh|3|2|small|high|unacc
high|high|5more|2|small|med|unacc
high|low|3|4|med|low|unacc
high|med|3|4|small|med|unacc
high|med|2|2|small|high|unacc
low|high|2|more|small|med|unacc
med|high|3|2|med|med|unacc
med|high|2|more|small|med|unacc
med|med|4|more|small|low|unacc
med|med|3|4|small|med|unacc
low|med|3|2|big|low|unacc
low|low|4|2|small|med|unacc
vhigh|low|2|2|med|med|unacc
med|med|3|2|big|low|unacc
high|high|2|more|small|med|unacc
high|low|4|2|small|med|unacc
vhigh|med|3|4|small|med|unacc
vhigh|med|5more|2|med|low|unacc
high|high|2|4|big|low|unacc
med|high|2|4|big|low|unacc
vhigh|high|2|4|big|low|unacc
med|low|3|4|med|low|unacc
high|vhigh|4|4|small|med|unacc
med|vhigh|5more|more|small|low|unacc
high|vhigh|5more|more|small|low|unacc
med|high|5more|2|small|med|unacc
low|high|4|4|med|low|unacc
vhigh|high|2|more|small|med|unacc
low|low|5more|4|small|low|unacc
med|high|4|4|med|low|unacc
low|vhigh|4|2|big|low|unacc
vhigh|med|3|2|big|low|unacc
low|low|2|2|med|med|unacc
vhigh|med|4|more|small|low|unacc
vhigh|low|5more|4|small|low|unacc
vhigh|vhigh|3|2|small|high|unacc
low|med|2|2|small|high|unacc
high|med|3|2|big|low|unacc
med|med|2|more|med|low|unacc
vhigh|high|3|2|med|med|unacc
high|vhigh|2|4|med|med|unacc
high|high|4|4|med|low|unacc
med|low|2|2|med|med|unacc
low|vhigh|2|4|med|med|unacc
high|vhigh|3|more|med|low|unacc
vhigh|low|3|4|med|low|unacc
low|med|3|4|small|med|unacc
high|low|5more|4|small|low|unacc
low|med|2|more|med|low|unacc
low|med|5more|2|med|low|unacc
med|low|5more|4|small|low|unacc
high|low|2|2|med|med|unacc
high|vhigh|3|2|small|high|unacc
vhigh|vhigh|5more|more|small|low|unacc
vhigh|med|2|more|med|low|unacc
vhigh|vhigh|3|more|med|low|unacc
med|vhigh|4|2|big|low|unacc
med|low|4|2|small|med|unacc
low|low|3|4|med|low|unacc
low|high|5more|2|small|med|unacc
low|vhigh|4|4|small|med|unacc
med|vhigh|3|more|med|low|unacc
low|vhigh|5more|more|small|low|unacc
high|med|4|more|small|low|unacc
vhigh|high|4|4|med|low|unacc
low|low|2|4|small|med|unacc
low|high|3|4|small|med|unacc
high|high|4|more|small|low|unacc
vhigh|vhigh|2|4|big|low|unacc
med|med|4|2|small|med|unacc
med|low|3|more|small|low|unacc
vhigh|med|4|2|small|med|unacc
med|high|4|more|small|low|unacc
med|vhigh|5more|2|small|med|unacc
low|med|2|2|med|med|unacc
vhigh|high|2|more|med|low|unacc
high|vhigh|3|2|med|med|unacc
low|high|4|more|small|low|unacc
low|low|3|more|small|low|unacc
med|vhigh|4|4|med|low|unacc
med|high|3|2|big|low|unacc
high|vhigh|2|4|big|low|unacc
vhigh|low|4|2|med|low|unacc
high|high|3|2|big|low|unacc
high|low|2|4|small|med|unacc
high|med|2|2|med|med|unacc
med|high|2|2|small|high|unacc
vhigh|med|5more|4|small|low|unacc
high|med|5more|4|small|low|unacc
high|high|2|2|small|high|unacc
high|low|3|more|small|low|unacc
low|high|2|more|med|low|unacc
low|vhigh|4|4|med|low|unacc
med|low|2|2|big|low|unacc
low|med|5more|4|small|low|unacc
low|low|2|2|big|low|unacc
vhigh|high|3|4|small|med|unacc
high|low|4|2|med|low|unacc
vhigh|med|3|4|med|low|unacc
low|vhigh|5more|2|small|med|unacc
low|high|2|2|small|high|unacc
low|high|5more|2|med|low|unacc
vhigh|low|3|more|small|low|unacc
med|high|5more|2|med|low|unacc
high|vhigh|4|4|med|low|unacc
low|vhigh|2|4|big|low|unacc
vhigh|vhigh|2|more|small|med|unacc
vhigh|med|2|2|med|med|unacc
med|high|2|more|med|low|unacc
high|high|5more|2|med|low|unacc
med|vhigh|3|2|med|med|unacc
high|vhigh|2|more|small|med|unacc
high|med|3|4|med|low|unacc
vhigh|vhigh|3|2|med|med|unacc
low|vhigh|2|more|small|med|unacc
vhigh|high|2|2|small|high|unacc
high|med|4|2|small|med|unacc
med|vhigh|2|4|big|low|unacc
low|med|4|2|small|med|unacc
med|high|3|4|small|med|unacc
vhigh|high|5more|2|med|low|unacc
vhigh|high|3|2|big|low|unacc
med|low|2|4|small|med|unacc
high|vhigh|5more|2|small|med|unacc
vhigh|high|4|more|small|low|unacc
vhigh|low|2|4|small|med|unacc
med|med|5more|4|small|low|unacc
med|low|4|2|med|low|unacc
vhigh|low|2|2|big|low|unacc
vhigh|vhigh|5more|2|small|med|unacc
low|med|3|4|med|low|unacc
med|vhigh|2|more|small|med|unacc
low|vhigh|3|2|med|med|unacc
high|vhigh|2|2|small|high|unacc
vhigh|vhigh|2|more|med|low|unacc
high|high|4|2|small|med|unacc
low|vhigh|2|2|small|high|unacc
med|low|3|2|small|med|unacc
vhigh|high|2|2|med|med|unacc
vhigh|high|3|4|med|low|unacc
high|med|4|2|med|low|unacc
high|high|3|4|med|low|unacc
vhigh|high|5more|4|small|low|unacc
med|low|4|4|small|low|unacc
vhigh|med|2|2|big|low|unacc
med|high|4|2|small|med|unacc
vhigh|low|3|2|small|med|unacc
low|high|2|2|med|med|unacc
med|vhigh|3|4|small|med|unacc
high|low|2|4|med|low|unacc
low|low|4|4|small|low|unacc
high|med|3|more|small|low|unacc
low|low|3|2|small|med|unacc
low|med|3|more|small|low|unacc
high|low|3|2|small|med|unacc
high|vhigh|2|more|med|low|unacc
vhigh|vhigh|2|2|small|high|unacc
vhigh|low|4|4|small|low|unacc
med|vhigh|2|2|small|high|unacc
vhigh|med|2|4|small|med|unacc
vhigh|low|2|4|med|low|unacc
high|high|5more|4|small|low|unacc
med|high|5more|4|small|low|unacc
low|vhigh|5more|2|med|low|unacc
med|med|4|2|med|low|unacc
low|med|4|2|med|low|unacc
low|med|2|4|small|med|unacc
low|vhigh|2|more|med|low|unacc
low|vhigh|3|2|big|low|unacc
vhigh|vhigh|3|2|big|low|unacc
med|med|3|more|small|low|unacc
high|vhigh|5more|2|med|low|unacc
med|vhigh|3|2|big|low|unacc
low|high|5more|4|small|low|unacc
med|vhigh|5more|2|med|low|unacc
med|low|2|4|med|low|unacc
vhigh|high|4|2|small|med|unacc
vhigh|med|3|more|small|low|unacc
low|high|3|4|med|low|unacc
med|vhigh|2|more|med|low|unacc
high|low|4|4|small|low|unacc
med|high|2|2|med|med|unacc
low|vhigh|3|4|small|med|unacc
med|vhigh|4|more|small|low|unacc
low|med|2|2|big|low|unacc
low|low|2|4|med|low|unacc
vhigh|vhigh|4|more|small|low|unacc
high|med|2|4|small|med|unacc
low|vhigh|4|more|small|low|unacc
high|vhigh|3|2|big|low|unacc
vhigh|vhigh|3|4|small|med|unacc
vhigh|med|4|2|med|low|unacc
med|high|3|4|med|low|unacc
med|med|2|2|big|low|unacc
vhigh|vhigh|5more|2|med|low|unacc
low|high|2|4|small|med|unacc
med|high|4|2|med|low|unacc
low|high|4|2|med|low|unacc
high|med|2|4|med|low|unacc
vhigh|vhigh|5more|4|small|low|unacc
high|low|5more|2|small|low|unacc
vhigh|high|3|more|small|low|unacc
vhigh|high|2|2|big|low|unacc
low|med|2|4|med|low|unacc
high|vhigh|5more|4|small|low|unacc
low|high|3|more|small|low|unacc
med|low|5more|2|small|low|unacc
med|med|4|4|small|low|unacc
low|med|4|4|small|low|unacc
vhigh|high|4|2|med|low|unacc
high|vhigh|2|2|med|med|unacc
high|med|3|2|small|med|unacc
med|low|3|2|med|low|unacc
high|high|3|more|small|low|unacc
high|high|4|2|med|low|unacc
low|med|3|2|small|med|unacc
med|vhigh|5more|4|small|low|unacc
med|low|2|more|small|low|unacc
med|vhigh|3|4|med|low|unacc
vhigh|med|2|4|med|low|unacc
med|med|3|2|small|med|unacc
low|low|5more|2|small|low|unacc
high|low|2|more|small|low|unacc
vhigh|low|2|more|small|low|unacc
vhigh|high|2|4|small|med|unacc
low|vhigh|4|2|small|med|unacc
vhigh|low|3|2|med|low|unacc
high|high|2|4|small|med|unacc
low|low|2|more|small|low|unacc
high|vhigh|4|2|small|med|unacc
med|vhigh|4|2|small|med|unacc
high|high|2|2|big|low|unacc
high|med|4|4|small|low|unacc
low|low|3|2|med|low|unacc
low|vhigh|2|2|med|med|unacc
low|vhigh|3|4|med|low|unacc
low|vhigh|5more|4|small|low|unacc
med|high|2|4|small|med|unacc
high|low|3|2|med|low|unacc
med|med|2|4|med|low|unacc
vhigh|vhigh|2|2|med|med|unacc
med|high|3|more|small|low|unacc
high|low|2|2|small|med|unacc
high|low|3|4|small|low|unacc
high|high|2|4|med|low|unacc
low|vhigh|2|4|small|med|unacc
high|vhigh|2|2|big|low|unacc
high|high|3|2|small|med|unacc
vhigh|vhigh|3|more|small|low|unacc
high|high|4|4|small|low|unacc
med|med|5more|2|small|low|unacc
high|vhigh|3|more|small|low|unacc
vhigh|med|3|2|med|low|unacc
low|vhigh|2|2|big|low|unacc
low|low|2|2|small|med|unacc
med|low|3|4|small|low|unacc
med|high|4|4|small|low|unacc
vhigh|high|2|4|med|low|unacc
low|high|3|2|small|med|unacc
low|vhigh|4|2|med|low|unacc
med|low|2|2|small|med|unacc
vhigh|vhigh|2|2|big|low|unacc
low|med|3|2|med|low|unacc
vhigh|high|4|4|small|low|unacc
high|vhigh|2|4|small|med|unacc
high|vhigh|4|2|med|low|unacc
low|med|5more|2|small|low|unacc
med|vhigh|3|more|small|low|unacc
high|med|3|2|med|low|unacc
med|high|3|2|small|med|unacc
low|med|2|more|small|low|unacc
vhigh|med|2|more|small|low|unacc
high|med|2|more|small|low|unacc
vhigh|med|5more|2|small|low|unacc
vhigh|low|2|2|small|med|unacc
med|high|2|4|med|low|unacc
low|vhigh|3|more|small|low|unacc
vhigh|vhigh|4|2|med|low|unacc
vhigh|vhigh|2|4|small|med|unacc
vhigh|high|3|2|small|med|unacc
high|med|5more|2|small|low|unacc
med|med|3|2|med|low|unacc
low|high|2|4|med|low|unacc
vhigh|low|3|4|small|low|unacc
med|vhigh|4|2|med|low|unacc
med|vhigh|2|4|small|med|unacc
vhigh|high|2|more|small|low|unacc
med|low|4|2|small|low|unacc
low|high|5more|2|small|low|unacc
vhigh|vhigh|4|4|small|low|unacc
low|high|2|more|small|low|unacc
low|vhigh|4|4|small|low|unacc
vhigh|high|3|2|med|low|unacc
low|vhigh|3|2|small|med|unacc
vhigh|vhigh|3|2|small|med|unacc
high|low|2|2|med|low|unacc
low|high|3|2|med|low|unacc
med|high|2|more|small|low|unacc
high|med|3|4|small|low|unacc
vhigh|high|5more|2|small|low|unacc
med|med|3|4|small|low|unacc
vhigh|low|2|2|med|low|unacc
med|med|2|2|small|med|unacc
high|high|3|2|med|low|unacc
high|vhigh|3|2|small|med|unacc
high|high|2|more|small|low|unacc
vhigh|med|2|2|small|med|unacc
med|vhigh|2|4|med|low|unacc
med|vhigh|3|2|small|med|unacc
med|high|3|2|med|low|unacc
vhigh|med|3|4|small|low|unacc
high|med|2|2|small|med|unacc
high|vhigh|4|4|small|low|unacc
high|vhigh|2|4|med|low|unacc
vhigh|vhigh|2|4|med|low|unacc
low|low|4|2|small|low|unacc
med|low|2|2|med|low|unacc
med|high|5more|2|small|low|unacc
med|vhigh|4|4|small|low|unacc
vhigh|low|4|2|small|low|unacc
high|low|4|2|small|low|unacc
low|med|2|2|small|med|unacc
high|vhigh|5more|2|small|low|unacc
med|vhigh|2|more|small|low|unacc
vhigh|med|2|2|med|low|unacc
low|high|3|4|small|low|unacc
vhigh|high|3|4|small|low|unacc
vhigh|high|2|2|small|med|unacc
low|med|4|2|small|low|unacc
vhigh|low|2|4|small|low|unacc
vhigh|vhigh|3|2|med|low|unacc
high|vhigh|2|more|small|low|unacc
med|vhigh|3|2|med|low|unacc
vhigh|vhigh|5more|2|small|low|unacc
low|vhigh|5more|2|small|low|unacc
high|med|2|2|med|low|unacc
low|high|2|2|small|med|unacc
high|high|3|4|small|low|unacc
high|high|2|2|small|med|unacc
med|med|2|2|med|low|unacc
high|med|4|2|small|low|unacc
high|vhigh|3|2|med|low|unacc
med|high|3|4|small|low|unacc
low|vhigh|2|more|small|low|unacc
low|vhigh|3|2|med|low|unacc
vhigh|vhigh|2|more|small|low|unacc
med|vhigh|5more|2|small|low|unacc
vhigh|med|4|2|small|low|unacc
med|high|2|2|small|med|unacc
high|low|2|4|small|low|unacc
low|low|2|4|small|low|unacc
vhigh|vhigh|3|4|small|low|unacc
low|vhigh|2|2|small|med|unacc
med|low|3|2|small|low|unacc
med|med|2|4|small|low|unacc
high|high|4|2|small|low|unacc
high|high|2|2|med|low|unacc
vhigh|high|4|2|small|low|unacc
low|vhigh|3|4|small|low|unacc
med|vhigh|2|2|small|med|unacc
med|high|4|2|small|low|unacc
low|med|2|4|small|low|unacc
vhigh|high|2|2|med|low|unacc
med|vhigh|3|4|small|low|unacc
vhigh|low|3|2|small|low|unacc
vhigh|vhigh|2|2|small|med|unacc
low|low|3|2|small|low|unacc
high|low|3|2|small|low|unacc
high|med|2|4|small|low|unacc
vhigh|med|2|4|small|low|unacc
med|high|2|2|med|low|unacc
low|high|4|2|small|low|unacc
low|high|2|2|med|low|unacc
high|vhigh|3|4|small|low|unacc
high|med|3|2|small|low|unacc
vhigh|vhigh|2|2|med|low|unacc
high|vhigh|2|2|med|low|unacc
high|vhigh|4|2|small|low|unacc
low|high|2|4|small|low|unacc
low|med|3|2|small|low|unacc
med|vhigh|4|2|small|low|unacc
vhigh|high|2|4|small|low|unacc
med|vhigh|2|2|med|low|unacc
vhigh|vhigh|4|2|small|low|unacc
med|med|3|2|small|low|unacc
low|vhigh|2|2|med|low|unacc
med|high|2|4|small|low|unacc
vhigh|med|3|2|small|low|unacc
med|high|3|2|small|low|unacc
low|high|3|2|small|low|unacc
low|vhigh|2|4|small|low|unacc
med|vhigh|2|4|small|low|unacc
low|low|2|2|small|low|unacc
high|vhigh|2|4|small|low|unacc
high|high|3|2|small|low|unacc
vhigh|low|2|2|small|low|unacc
vhigh|high|3|2|small|low|unacc
med|low|2|2|small|low|unacc
vhigh|vhigh|2|4|small|low|unacc
high|low|2|2|small|low|unacc
med|med|2|2|small|low|unacc
low|med|2|2|small|low|unacc
low|vhigh|3|2|small|low|unacc
vhigh|vhigh|3|2|small|low|unacc
vhigh|med|2|2|small|low|unacc
high|med|2|2|small|low|unacc
high|vhigh|3|2|small|low|unacc
med|vhigh|3|2|small|low|unacc
low|high|2|2|small|low|unacc
med|high|2|2|small|low|unacc
high|high|2|2|small|low|unacc
vhigh|high|2|2|small|low|unacc
med|vhigh|2|2|small|low|unacc
high|vhigh|2|2|small|low|unacc

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = more) and (Maint = high)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4) and (Maint = high)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big) and (Maint = med)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = med)|vgood (15.0/6.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (8.0/3.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Maint = low) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (10.0/4.0)
(Safety = high) and (Buying = low) and (Persons = 4) and (Maint = med)|vgood (10.0/5.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med)|vgood (11.0/6.0)
(Safety = high) and (Buying = low) and (Maint = low) and (Persons = more) and (Lug_boot = big)|vgood (4.0/0.0)
(Maint = low) and (Buying = low) and (Persons = 4) and (Safety = high)|good (6.0/1.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Lug_boot = big) and (Persons = more)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Persons = more) and (Safety = med)|good (10.0/4.0)
(Buying = low) and (Persons = more) and (Maint = med) and (Safety = med) and (Lug_boot = big)|good (4.0/0.0)
(Buying = low) and (Maint = low) and (Safety = med) and (Persons = 4)|good (8.0/3.0)
(Buying = low) and (Persons = more) and (Safety = high)|good (18.0/12.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high)|good (7.0/2.0)
(Buying = low) and (Lug_boot = med) and (Safety = med) and (Persons = more)|good (12.0/8.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (27.0/0.0)
(Safety = high) and (Persons = 4) and (Buying = med)|acc (22.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = med)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = med)|acc (12.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 5more)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Doors = 4)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = med)|acc (12.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = low)|acc (21.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (11.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 3)|acc (6.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Doors = 3)|acc (5.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Lug_boot = big)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 4)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med) and (Buying = med)|acc (4.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = low) and (Maint = vhigh)|acc (12.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 5more)|acc (9.0/2.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = high)|acc (10.0/1.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 5more)|acc (10.0/3.0)
(Safety = med) and (Persons = more) and (Buying = low)|acc (14.0/6.0)
(Persons = 4) and (Safety = high) and (Maint = high) and (Buying = high)|acc (11.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = low) and (Lug_boot = small)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Doors = 5more)|acc (5.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Doors = 4)|acc (9.0/3.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (11.0/4.0)
(Persons = more) and (Safety = high) and (Maint = low)|acc (8.0/2.0)
(Safety = med) and (Persons = more) and (Doors = 3) and (Lug_boot = med)|acc (7.0/2.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = med)|acc (6.0/0.0)
(Maint = high) and (Persons = 4) and (Buying = low) and (Safety = high) and (Lug_boot = small)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Doors = 2) and (Lug_boot = med)|acc (5.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Buying = high) and (Maint = high)|acc (4.0/0.0)
|unacc (1070.0/15.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (522.0)
Safety = low|unacc (348.0)
Buying != low AND Buying != med AND Maint = vhigh|unacc (85.0)
Buying = vhigh AND Maint != high AND Lug_boot != small AND Doors != 2|acc (42.0/1.0)
Buying = vhigh AND Maint = high|unacc (40.0)
Safety = med AND Lug_boot = small AND Buying != high AND Buying != vhigh AND Maint != vhigh AND Doors != 2 AND Maint != high|acc (21.0)
Lug_boot = small AND Safety = med AND Buying != low|unacc (52.0/1.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (57.0)
Maint = vhigh AND Lug_boot != small AND Doors != 2|acc (38.0)
Safety = med AND Maint = vhigh AND Lug_boot != big|unacc (10.0)
Buying = high AND Lug_boot = big|acc (22.0)
Buying = high AND Safety != med AND Doors != 2|acc (11.0)
Safety = med AND Buying = high AND Doors = 2|unacc (6.0)
Safety = med AND Maint = high AND Lug_boot != big AND Buying = low|acc (15.0/1.0)
Safety = med AND Maint = high AND Lug_boot != med|acc (14.0)
Safety = med AND Buying = high AND Persons = 4|unacc (3.0)
Safety = med AND Buying = vhigh AND Lug_boot = med|unacc (4.0)
Lug_boot = small AND Doors != 2 AND Maint != low AND Buying != low|acc (23.0)
Lug_boot = small AND Doors != 2 AND Buying != med AND Maint != med AND Maint != low|acc (11.0)
Lug_boot = small AND Doors != 2 AND Buying != vhigh|good (15.0)
Lug_boot = small AND Persons != 4 AND Doors = 2|unacc (15.0)
Safety = med AND Maint = high AND Doors != 2|acc (6.0/1.0)
Safety = med AND Maint != high AND Buying != vhigh AND Maint != vhigh AND Buying = low AND Lug_boot != small AND Lug_boot != med|good (15.0)
Safety = med AND Maint != high AND Maint != low AND Buying != low|acc (19.0)
Safety = med AND Maint != high AND Doors != 2 AND Doors != 3|good (14.0)
Buying != vhigh AND Maint != vhigh AND Safety != med AND Buying != high AND Maint != high AND Lug_boot != small AND Lug_boot != med|vgood (27.0)
Doors = 2 AND Maint != high AND Maint = vhigh|acc (12.0)
Buying = vhigh|acc (17.0)
Doors != 2 AND Safety = med AND Buying = med|good (3.0/1.0)
Doors != 2 AND Buying = low AND Safety != med AND Doors != 3|vgood (15.0)
Maint = high AND Safety != med AND Buying != low|acc (17.0)
Buying != high AND Safety = med AND Maint != high AND Lug_boot != big|acc (8.0/1.0)
Buying = high|acc (7.0)
Safety = med AND Maint = high|unacc (2.0)
Doors != 2 AND Persons != 4|vgood (10.0)
Doors != 4 AND Doors != 5more AND Maint != high AND Maint != med|good (9.0)
Lug_boot != big AND Buying = med AND Doors != 2|vgood (5.0/1.0)
Lug_boot != big AND Maint = high|acc (4.0)
Buying != med AND Maint != high|good (4.0)
Buying != med|vgood (3.0)
|acc (2.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(30.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): vgood(12.0/0.0)
							* Lug_boot!=(big)
								* Persons=(more)
											* Doors=(3)|(4)|(5more): vgood(4.0/0.0)
											* Doors!=(3)|(4)|(5more): good(2.0/1.0)
								* Persons!=(more)
											* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
											* Buying!=(low)|(vhigh)|(high)
												* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
												* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(10.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Persons=(more)|(2): unacc(2.0/0.0)
									* Persons!=(more)|(2): good(2.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): good(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(low)|(vhigh)|(high): acc(6.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Lug_boot=(big)|(small): good(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
											* Maint=(low)|(vhigh)|(high): acc(1.0/1.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Buying!=(low)
							* Maint=(low)
									* Doors=(5more)|(4): good(7.0/0.0)
									* Doors!=(5more)|(4)
									* Lug_boot=(big): good(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
							* Maint!=(low): acc(15.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(3.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
							* Maint=(high)|(med)|(low)
								* Buying=(low)|(vhigh)|(high)
								* Safety=(high)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): vgood(4.0/0.0)
										* Lug_boot!=(big)|(small)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
								* Safety!=(high)|(low): acc(14.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
									* Lug_boot=(big): acc(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Maint!=(high)|(med)|(low)
								* Doors=(5more)|(4)|(3): acc(38.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Lug_boot=(big)|(small): acc(8.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(4.0/0.0)
									* Safety!=(high)|(low): unacc(3.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
								* Buying=(low)|(vhigh)|(high)
									* Maint=(high)|(med)|(low)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Maint!=(high)|(med)|(low): unacc(7.0/0.0)
								* Buying!=(low)|(vhigh)|(high): unacc(15.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
							* Doors=(5more)|(4)|(3)
								* Doors=(5more)|(4)|(2): acc(59.0/0.0)
								* Doors!=(5more)|(4)|(2)
								* Lug_boot=(big)|(small): acc(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Safety=(high)|(low): acc(7.0/0.0)
									* Safety!=(high)|(low)
										* Persons=(more)|(2): acc(3.0/0.0)
										* Persons!=(more)|(2): unacc(3.0/0.0)
							* Doors!=(5more)|(4)|(3)
						* Lug_boot=(big): acc(14.0/0.0)
						* Lug_boot!=(big)
								* Safety=(high)|(low): acc(8.0/0.0)
								* Safety!=(high)|(low): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(24.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(28.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
							* Buying=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
									* Doors=(5more)|(4)|(3)
										* Doors=(5more)|(4)|(2): acc(14.0/0.0)
										* Doors!=(5more)|(4)|(2)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2)
											* Lug_boot=(big)|(small): acc(2.0/0.0)
											* Lug_boot!=(big)|(small): unacc(1.0/1.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(small): acc(4.0/0.0)
									* Lug_boot!=(big)|(small): unacc(2.0/1.0)
							* Lug_boot!=(big)|(med)
								* Safety=(high)|(low)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
								* Safety!=(high)|(low): unacc(6.0/0.0)
							* Buying!=(high)|(med)|(low): unacc(40.0/0.0)
				* Maint!=(high): unacc(85.0/0.0)
		* Safety!=(high)|(med): unacc(348.0/0.0)
	* Persons!=(more)|(4): unacc(522.0/0.0)


