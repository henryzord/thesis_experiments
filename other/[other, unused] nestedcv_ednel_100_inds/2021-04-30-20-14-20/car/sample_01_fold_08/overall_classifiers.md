# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety != high | unacc | 0.617873 |
| Safety != med | unacc | 0.591646 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors != 3 and Persons != 2 | acc | 0.004946 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety != low and Lug_boot = med and Buying != high and Maint != low | acc | 0.003303 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 4 | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying != med and Maint = med and Lug_boot = med and Lug_boot!=(big) and Safety != low and Doors = 5more | acc | 0.001104 |
| Safety = med and Persons = 4 and Buying = med and Maint != med and Lug_boot = med and Buying!=(low) and Doors = 3 and Doors != 2 and Lug_boot != small and Maint != high | acc | 0.000414 |
| Safety = med and Persons = 4 and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors = 3 | acc | 0.000828 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = low | unacc | 0.532795 |
| Persons = 2 | unacc | 0.422693 |
| Maint = vhigh and Buying = high | unacc | 0.086785 |
| Buying = vhigh and Maint = vhigh | unacc | 0.083168 |
| Buying = vhigh and Maint = high | unacc | 0.083168 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.045361 |
| Safety = med and Lug_boot = small and Maint != vhigh and Buying != vhigh and Maint != high and Doors != 2 | acc | 0.099526 |
| Safety = med and Lug_boot = small and Maint = vhigh | unacc | 0.034934 |
| Safety = med and Lug_boot = small and Buying != low and Doors != 2 | unacc | 0.032823 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.246445 |
| Safety = med and Lug_boot = big and Buying != vhigh and Maint != low and Maint != med | acc | 0.145161 |
| Safety = med and Lug_boot = big and Buying != low and Buying != med | acc | 0.126374 |
| Safety != med and Lug_boot != small and Buying != vhigh and Maint != vhigh and Buying != high and Maint != high and Doors != 2 and Doors != 3 | vgood | 0.087571 |
| Safety != med and Lug_boot != small and Buying != low and Buying != med | acc | 0.292818 |
| Maint = vhigh and Doors != 2 and Safety != med | acc | 0.200000 |
| Lug_boot != big and Doors = 2 and Persons != 4 and Lug_boot = small | unacc | 0.074380 |
| Safety != med and Lug_boot = big and Maint != low and Maint != med and Buying = med | acc | 0.075630 |
| Lug_boot != big and Safety != med and Maint = high and Buying != low | acc | 0.126984 |
| Safety = med and Buying = high and Doors = 2 | unacc | 0.024510 |
| Lug_boot != big and Safety = med and Doors = 2 and Buying != vhigh and Maint = low | acc | 0.054054 |
| Safety = med and Lug_boot = big and Buying != med | good | 0.079268 |
| Lug_boot = big and Safety != med and Doors != 2 | vgood | 0.055249 |
| Safety = med and Maint != low and Doors != 2 and Doors != 3 and Buying != low | acc | 0.196078 |
| Safety != med and Lug_boot = big and Maint != low | vgood | 0.017429 |
| Buying = vhigh and Safety != med | acc | 0.152174 |
| Buying = vhigh and Doors != 2 | acc | 0.044092 |
| Maint = low and Buying != high and Safety != med and Lug_boot != big and Doors != 3 | good | 0.125000 |
| Buying != vhigh and Maint != low and Maint != med and Buying = low and Safety = med and Maint != vhigh | acc | 0.179487 |
| Buying != vhigh and Maint = vhigh and Safety = med and Persons = 4 | unacc | 0.026403 |
| Buying != vhigh and Buying = high and Lug_boot = small | acc | 0.090909 |
| Buying != vhigh and Buying != high and Maint = low and Safety = med and Doors != 3 | good | 0.129412 |
| Buying = vhigh | unacc | 0.078652 |
| Safety = med and Maint = high | unacc | 0.037647 |
| Maint = vhigh and Buying != med | acc | 0.208333 |
| Buying != high and Maint != vhigh and Maint = high and Lug_boot = small | acc | 0.136364 |
| Maint = high and Persons = 4 | acc | 0.026316 |
| Buying != high and Buying = med and Maint != low and Maint != vhigh and Doors != 3 | acc | 0.208333 |
| Buying != high and Maint != vhigh and Safety = med and Persons != 4 | good | 0.105263 |
| Safety = med and Buying != high and Doors = 3 | acc | 0.182336 |
| Buying != high and Maint != vhigh and Lug_boot != big and Maint != high and Lug_boot = small and Maint = med | good | 0.145161 |
| Buying != high and Maint != vhigh and Lug_boot != small and Maint != med and Maint != high | vgood | 0.177340 |
| Maint != high and Buying != high and Maint != vhigh and Persons = 4 | good | 0.196000 |
| Safety != med and Doors != 2 | vgood | 0.222727 |
| Safety = med | unacc | 0.093750 |
|  | acc | 0.785714 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

buying|maint|doors|persons|lug_boot|safety|acceptability
---|---|---|---|---|---|---
vhigh|low|5more|more|big|high|unacc
high|low|5more|more|big|high|unacc
low|low|5more|more|big|high|unacc
med|low|5more|more|big|high|unacc
low|med|5more|more|big|high|unacc
med|med|5more|more|big|high|unacc
vhigh|med|5more|more|big|high|unacc
high|med|5more|more|big|high|unacc
vhigh|high|5more|more|big|high|unacc
med|low|4|more|big|high|unacc
high|high|5more|more|big|high|unacc
low|high|5more|more|big|high|unacc
low|low|4|more|big|high|unacc
vhigh|low|4|more|big|high|unacc
med|high|5more|more|big|high|unacc
high|low|4|more|big|high|unacc
med|med|4|more|big|high|unacc
low|low|5more|4|big|high|unacc
low|med|4|more|big|high|unacc
vhigh|low|5more|4|big|high|unacc
high|med|4|more|big|high|unacc
high|vhigh|5more|more|big|high|unacc
vhigh|vhigh|5more|more|big|high|unacc
high|low|5more|4|big|high|unacc
med|vhigh|5more|more|big|high|unacc
vhigh|med|5more|4|big|high|unacc
low|low|3|more|big|high|unacc
high|high|4|more|big|high|unacc
low|high|4|more|big|high|unacc
vhigh|high|4|more|big|high|unacc
high|med|5more|4|big|high|unacc
low|low|5more|more|med|high|unacc
med|med|5more|4|big|high|unacc
med|low|5more|more|med|high|unacc
high|low|3|more|big|high|unacc
low|med|5more|4|big|high|unacc
vhigh|low|5more|more|med|high|unacc
vhigh|low|3|more|big|high|unacc
med|high|4|more|big|high|unacc
low|med|3|more|big|high|unacc
med|med|5more|more|med|high|unacc
high|vhigh|4|more|big|high|unacc
high|high|5more|4|big|high|unacc
high|med|3|more|big|high|unacc
high|med|5more|more|med|high|unacc
vhigh|high|5more|4|big|high|unacc
vhigh|low|4|4|big|high|unacc
med|high|5more|4|big|high|unacc
vhigh|low|5more|more|big|med|unacc
low|low|4|4|big|high|unacc
low|vhigh|4|more|big|high|unacc
high|low|5more|more|big|med|unacc
med|med|3|more|big|high|unacc
med|low|5more|more|big|med|unacc
low|low|5more|more|big|med|unacc
vhigh|vhigh|4|more|big|high|unacc
med|vhigh|4|more|big|high|unacc
vhigh|med|5more|more|med|high|unacc
med|low|4|4|big|high|unacc
low|med|5more|more|med|high|unacc
med|low|2|more|big|high|unacc
high|med|5more|more|big|med|unacc
high|low|4|more|med|high|unacc
low|low|5more|2|big|high|unacc
high|low|5more|2|big|high|unacc
vhigh|high|5more|more|med|high|unacc
med|low|5more|2|big|high|unacc
vhigh|low|2|more|big|high|unacc
vhigh|med|4|4|big|high|unacc
med|low|4|more|med|high|unacc
vhigh|med|5more|more|big|med|unacc
low|high|3|more|big|high|unacc
low|med|4|4|big|high|unacc
low|low|4|more|med|high|unacc
low|med|5more|more|big|med|unacc
high|vhigh|5more|4|big|high|unacc
med|vhigh|5more|4|big|high|unacc
high|low|2|more|big|high|unacc
high|high|5more|more|med|high|unacc
med|high|5more|more|med|high|unacc
vhigh|low|4|more|med|high|unacc
low|vhigh|5more|4|big|high|unacc
vhigh|low|5more|2|big|high|unacc
high|med|4|4|big|high|unacc
med|high|3|more|big|high|unacc
med|med|4|4|big|high|unacc
vhigh|high|3|more|big|high|unacc
med|med|5more|more|big|med|unacc
low|high|5more|more|med|high|unacc
low|low|2|more|big|high|unacc
med|med|4|more|med|high|unacc
vhigh|vhigh|3|more|big|high|unacc
low|vhigh|3|more|big|high|unacc
med|vhigh|5more|more|med|high|unacc
high|low|4|more|big|med|unacc
med|med|2|more|big|high|unacc
low|med|2|more|big|high|unacc
low|low|3|4|big|high|unacc
low|low|4|more|big|med|unacc
vhigh|high|5more|more|big|med|unacc
high|vhigh|3|more|big|high|unacc
high|low|3|4|big|high|unacc
vhigh|med|4|more|med|high|unacc
low|low|5more|4|med|high|unacc
high|med|5more|2|big|high|unacc
med|high|4|4|big|high|unacc
vhigh|low|4|more|big|med|unacc
high|med|2|more|big|high|unacc
vhigh|vhigh|5more|more|med|high|unacc
high|vhigh|5more|more|med|high|unacc
vhigh|med|2|more|big|high|unacc
vhigh|low|3|4|big|high|unacc
vhigh|low|5more|4|med|high|unacc
vhigh|high|4|4|big|high|unacc
low|med|4|more|med|high|unacc
vhigh|med|5more|2|big|high|unacc
low|high|5more|more|big|med|unacc
med|vhigh|3|more|big|high|unacc
med|low|3|4|big|high|unacc
med|low|5more|4|med|high|unacc
low|med|5more|2|big|high|unacc
med|med|5more|2|big|high|unacc
low|vhigh|5more|more|med|high|unacc
high|low|5more|4|med|high|unacc
med|high|5more|more|big|med|unacc
low|med|5more|4|med|high|unacc
med|low|5more|more|small|high|unacc
med|low|5more|4|big|med|unacc
low|low|5more|4|big|med|unacc
vhigh|med|3|4|big|high|unacc
med|high|2|more|big|high|unacc
high|low|5more|4|big|med|unacc
vhigh|med|4|more|big|med|unacc
low|vhigh|4|4|big|high|unacc
med|low|3|more|med|high|unacc
med|low|4|2|big|high|unacc
vhigh|vhigh|5more|more|big|med|unacc
high|med|5more|4|med|high|unacc
high|high|4|more|med|high|unacc
low|high|4|more|med|high|unacc
low|low|3|more|med|high|unacc
med|med|5more|4|med|high|unacc
vhigh|high|5more|2|big|high|unacc
vhigh|vhigh|4|4|big|high|unacc
vhigh|high|4|more|med|high|unacc
high|vhigh|5more|more|big|med|unacc
med|vhigh|4|4|big|high|unacc
high|low|3|more|med|high|unacc
med|med|4|more|big|med|unacc
vhigh|high|2|more|big|high|unacc
med|high|5more|2|big|high|unacc
low|high|2|more|big|high|unacc
low|med|4|more|big|med|unacc
high|high|5more|2|big|high|unacc
high|med|4|more|big|med|unacc
med|vhigh|5more|more|big|med|unacc
low|vhigh|5more|more|big|med|unacc
vhigh|med|5more|4|med|high|unacc
vhigh|low|5more|4|big|med|unacc
med|med|3|4|big|high|unacc
low|low|5more|more|small|high|unacc
high|low|4|2|big|high|unacc
low|high|5more|2|big|high|unacc
vhigh|low|5more|more|small|high|unacc
high|med|3|4|big|high|unacc
med|high|4|more|med|high|unacc
high|low|5more|more|small|high|unacc
high|vhigh|4|4|big|high|unacc
vhigh|low|3|more|med|high|unacc
high|high|2|more|big|high|unacc
low|low|4|4|med|high|unacc
med|med|3|more|med|high|unacc
low|low|5more|more|med|med|unacc
med|med|4|2|big|high|unacc
high|high|5more|4|med|high|unacc
low|med|3|more|med|high|unacc
med|low|2|4|big|high|unacc
low|low|3|more|big|med|unacc
high|low|5more|more|med|med|unacc
vhigh|low|3|more|big|med|unacc
high|med|3|more|med|high|unacc
low|low|2|4|big|high|unacc
med|low|3|more|big|med|unacc
low|med|5more|more|small|high|unacc
low|med|4|2|big|high|unacc
vhigh|high|3|4|big|high|unacc
low|vhigh|5more|2|big|high|unacc
vhigh|med|5more|4|big|med|unacc
med|high|5more|4|med|high|unacc
high|med|5more|more|small|high|unacc
med|med|5more|4|big|med|unacc
high|low|2|4|big|high|unacc
med|low|4|4|med|high|unacc
low|high|3|4|big|high|unacc
high|vhigh|4|more|med|high|unacc
vhigh|high|4|more|big|med|unacc
vhigh|med|4|2|big|high|unacc
vhigh|vhigh|4|more|med|high|unacc
high|med|5more|4|big|med|unacc
vhigh|low|2|4|big|high|unacc
med|high|3|4|big|high|unacc
low|high|5more|4|med|high|unacc
med|vhigh|5more|2|big|high|unacc
high|vhigh|5more|2|big|high|unacc
vhigh|high|5more|4|med|high|unacc
vhigh|med|5more|more|small|high|unacc
low|vhigh|4|more|med|high|unacc
vhigh|low|5more|more|med|med|unacc
high|high|4|more|big|med|unacc
high|low|3|more|big|med|unacc
high|med|4|2|big|high|unacc
vhigh|vhigh|2|more|big|high|unacc
high|vhigh|2|more|big|high|unacc
med|med|5more|more|small|high|unacc
vhigh|med|3|more|med|high|unacc
vhigh|low|4|4|med|high|unacc
med|vhigh|4|more|med|high|unacc
med|low|5more|more|med|med|unacc
high|high|3|4|big|high|unacc
high|low|4|4|med|high|unacc
low|vhigh|2|more|big|high|unacc
low|low|4|more|small|high|unacc
high|low|3|2|big|high|unacc
high|med|3|more|big|med|unacc
high|high|3|more|med|high|unacc
med|med|5more|more|med|med|unacc
vhigh|med|5more|more|med|med|unacc
vhigh|med|4|4|med|high|unacc
med|low|4|4|big|med|unacc
high|vhigh|5more|4|med|high|unacc
low|low|3|2|big|high|unacc
med|low|5more|2|med|high|unacc
low|low|4|4|big|med|unacc
low|low|5more|2|med|high|unacc
med|low|3|2|big|high|unacc
vhigh|high|4|2|big|high|unacc
high|vhigh|3|4|big|high|unacc
med|high|5more|more|small|high|unacc
high|high|5more|more|small|high|unacc
vhigh|low|4|4|big|med|unacc
low|high|5more|more|small|high|unacc
med|low|4|more|small|high|unacc
low|low|5more|more|big|low|unacc
high|med|5more|more|med|med|unacc
high|med|2|4|big|high|unacc
high|high|5more|4|big|med|unacc
vhigh|low|4|more|small|high|unacc
low|vhigh|5more|4|med|high|unacc
low|high|5more|4|big|med|unacc
med|med|4|4|med|high|unacc
low|high|4|2|big|high|unacc
vhigh|vhigh|5more|4|med|high|unacc
vhigh|high|5more|4|big|med|unacc
vhigh|low|3|2|big|high|unacc
vhigh|high|5more|more|small|high|unacc
med|med|3|more|big|med|unacc
high|low|2|more|med|high|unacc
vhigh|low|2|more|med|high|unacc
low|med|4|4|med|high|unacc
low|med|2|4|big|high|unacc
low|med|5more|more|med|med|unacc
low|med|3|more|big|med|unacc
high|low|5more|2|med|high|unacc
vhigh|low|5more|2|med|high|unacc
med|low|5more|more|big|low|unacc
med|high|5more|4|big|med|unacc
high|med|4|4|med|high|unacc
low|vhigh|3|4|big|high|unacc
vhigh|med|2|4|big|high|unacc
low|high|3|more|med|high|unacc
low|low|2|more|med|high|unacc
med|low|2|more|med|high|unacc
vhigh|low|5more|more|big|low|unacc
vhigh|vhigh|3|4|big|high|unacc
med|high|4|2|big|high|unacc
vhigh|vhigh|4|more|big|med|unacc
vhigh|med|3|more|big|med|unacc
med|high|3|more|med|high|unacc
med|vhigh|5more|4|med|high|unacc
med|vhigh|3|4|big|high|unacc
high|low|4|more|small|high|unacc
vhigh|vhigh|5more|more|small|high|unacc
vhigh|med|4|4|big|med|unacc
vhigh|med|2|more|med|high|unacc
vhigh|low|3|4|med|high|unacc
med|med|4|more|small|high|unacc
med|low|4|more|med|med|unacc
med|med|3|2|big|high|unacc
med|low|5more|2|big|med|unacc
high|vhigh|4|2|big|high|unacc
high|vhigh|5more|4|big|med|unacc
high|low|5more|2|big|med|unacc
vhigh|low|5more|2|big|med|unacc
med|med|2|more|med|high|unacc
low|med|2|more|med|high|unacc
low|med|5more|2|med|high|unacc
vhigh|med|5more|more|big|low|unacc
med|high|5more|more|med|med|unacc
low|high|3|more|big|med|unacc
high|med|4|4|big|med|unacc
med|med|4|4|big|med|unacc
high|low|3|4|med|high|unacc
med|low|5more|4|small|high|unacc
high|med|3|2|big|high|unacc
vhigh|med|5more|2|med|high|unacc
med|high|4|4|med|high|unacc
low|vhigh|5more|more|small|high|unacc
high|low|4|more|med|med|unacc
low|med|4|4|big|med|unacc
med|vhigh|4|2|big|high|unacc
low|med|3|2|big|high|unacc
vhigh|high|3|more|big|med|unacc
high|med|5more|more|big|low|unacc
med|med|5more|more|big|low|unacc
low|vhigh|4|2|big|high|unacc
vhigh|high|4|4|med|high|unacc
low|med|5more|more|big|low|unacc
high|vhigh|3|more|med|high|unacc
med|high|3|more|big|med|unacc
high|high|3|more|big|med|unacc
high|high|2|4|big|high|unacc
high|low|2|more|big|med|unacc
low|vhigh|5more|4|big|med|unacc
high|med|2|more|med|high|unacc
high|low|5more|4|small|high|unacc
low|low|4|more|med|med|unacc
high|vhigh|5more|more|small|high|unacc
vhigh|med|3|2|big|high|unacc
vhigh|vhigh|3|more|med|high|unacc
high|high|5more|more|med|med|unacc
vhigh|low|5more|4|small|high|unacc
low|high|4|4|med|high|unacc
low|low|5more|4|small|high|unacc
low|med|4|more|small|high|unacc
med|low|2|more|big|med|unacc
vhigh|high|5more|more|med|med|unacc
low|low|5more|2|big|med|unacc
vhigh|high|2|4|big|high|unacc
med|med|5more|2|med|high|unacc
med|vhigh|5more|4|big|med|unacc
low|vhigh|3|more|med|high|unacc
vhigh|low|2|more|big|med|unacc
med|high|2|4|big|high|unacc
vhigh|med|4|more|small|high|unacc
low|high|5more|more|med|med|unacc
low|med|3|4|med|high|unacc
med|low|3|4|big|med|unacc
high|vhigh|4|4|med|high|unacc
med|low|2|2|big|high|unacc
high|vhigh|3|more|big|med|unacc
vhigh|med|5more|2|big|med|unacc
vhigh|low|2|2|big|high|unacc
low|high|3|2|big|high|unacc
high|low|5more|4|med|med|unacc
low|high|4|4|big|med|unacc
high|low|3|more|small|high|unacc
med|med|4|more|med|med|unacc
low|vhigh|2|4|big|high|unacc
high|high|5more|2|med|high|unacc
med|low|4|more|big|low|unacc
high|vhigh|2|4|big|high|unacc
med|high|3|2|big|high|unacc
vhigh|low|3|more|small|high|unacc
med|vhigh|2|4|big|high|unacc
med|vhigh|3|more|big|med|unacc
low|low|2|2|big|high|unacc
vhigh|vhigh|3|more|big|med|unacc
high|high|3|2|big|high|unacc
vhigh|high|4|more|small|high|unacc
med|vhigh|5more|more|med|med|unacc
vhigh|low|5more|4|med|med|unacc
low|vhigh|4|4|med|high|unacc
high|med|5more|4|small|high|unacc
vhigh|vhigh|5more|more|med|med|unacc
high|med|5more|2|big|med|unacc
high|low|4|2|med|high|unacc
vhigh|low|4|more|big|low|unacc
high|high|4|4|big|med|unacc
med|med|3|4|med|high|unacc
med|med|5more|4|small|high|unacc
low|vhigh|5more|more|med|med|unacc
low|med|5more|4|small|high|unacc
vhigh|high|5more|more|big|low|unacc
vhigh|vhigh|4|4|med|high|unacc
low|high|5more|2|med|high|unacc
low|high|5more|more|big|low|unacc
vhigh|high|2|more|med|high|unacc
low|low|4|2|med|high|unacc
low|high|2|more|med|high|unacc
high|high|4|more|small|high|unacc
low|vhigh|3|more|big|med|unacc
high|med|4|more|med|med|unacc
high|low|3|4|big|med|unacc
vhigh|med|5more|4|small|high|unacc
low|med|4|more|med|med|unacc
med|low|3|more|small|high|unacc
low|med|2|more|big|med|unacc
high|low|4|more|big|low|unacc
vhigh|high|4|4|big|med|unacc
high|low|2|2|big|high|unacc
med|high|5more|2|med|high|unacc
high|vhigh|5more|more|med|med|unacc
med|med|5more|2|big|med|unacc
low|med|5more|2|big|med|unacc
low|low|4|more|big|low|unacc
vhigh|high|5more|2|med|high|unacc
med|high|4|4|big|med|unacc
vhigh|med|4|more|med|med|unacc
med|vhigh|4|4|med|high|unacc
vhigh|low|3|4|big|med|unacc
low|low|3|more|small|high|unacc
vhigh|high|3|2|big|high|unacc
vhigh|vhigh|2|4|big|high|unacc
high|high|5more|more|big|low|unacc
med|med|2|more|big|med|unacc
high|high|2|more|med|high|unacc
vhigh|med|3|4|med|high|unacc
high|med|3|4|med|high|unacc
high|med|2|more|big|med|unacc
med|low|2|4|med|high|unacc
med|low|3|more|med|med|unacc
high|med|4|2|med|high|unacc
low|low|4|2|big|med|unacc
vhigh|vhigh|3|2|big|high|unacc
high|vhigh|4|4|big|med|unacc
med|vhigh|5more|more|big|low|unacc
high|vhigh|5more|2|med|high|unacc
vhigh|low|5more|4|big|low|unacc
vhigh|low|3|more|med|med|unacc
vhigh|low|4|4|small|high|unacc
low|low|5more|more|small|med|unacc
high|high|4|more|med|med|unacc
low|med|3|more|small|high|unacc
low|vhigh|5more|more|big|low|unacc
med|low|5more|4|big|low|unacc
low|vhigh|2|more|med|high|unacc
high|med|3|4|big|med|unacc
med|high|4|more|med|med|unacc
med|med|3|4|big|med|unacc
med|high|2|more|big|med|unacc
low|high|2|more|big|med|unacc
med|med|3|more|small|high|unacc
vhigh|med|3|4|big|med|unacc
low|low|2|4|med|high|unacc
vhigh|vhigh|4|more|small|high|unacc
low|vhigh|5more|2|med|high|unacc
vhigh|low|5more|more|small|med|unacc
vhigh|vhigh|4|4|big|med|unacc
vhigh|med|2|2|big|high|unacc
vhigh|high|2|more|big|med|unacc
low|med|2|2|big|high|unacc
low|high|3|4|med|high|unacc
med|low|5more|more|small|med|unacc
vhigh|med|3|more|small|high|unacc
high|low|2|4|med|high|unacc
low|vhigh|4|more|small|high|unacc
med|low|4|4|small|high|unacc
vhigh|med|4|more|big|low|unacc
low|low|5more|4|big|low|unacc
vhigh|vhigh|5more|more|big|low|unacc
vhigh|high|5more|2|big|med|unacc
high|low|4|2|big|med|unacc
vhigh|high|4|more|med|med|unacc
med|vhigh|4|more|small|high|unacc
high|high|5more|4|small|high|unacc
vhigh|med|5more|4|med|med|unacc
low|high|5more|4|small|high|unacc
low|low|3|more|med|med|unacc
low|low|4|4|small|high|unacc
high|vhigh|5more|more|big|low|unacc
low|vhigh|3|2|big|high|unacc
high|low|4|4|small|high|unacc
high|med|3|more|small|high|unacc
low|med|5more|4|med|med|unacc
high|vhigh|4|more|small|high|unacc
med|vhigh|5more|2|med|high|unacc
vhigh|med|4|2|med|high|unacc
low|med|4|more|big|low|unacc
high|med|4|more|big|low|unacc
high|med|5more|4|med|med|unacc
low|high|4|more|med|med|unacc
high|high|3|4|med|high|unacc
vhigh|low|2|4|med|high|unacc
med|vhigh|2|more|med|high|unacc
med|med|5more|4|med|med|unacc
med|high|3|4|med|high|unacc
low|med|3|4|big|med|unacc
low|med|4|2|med|high|unacc
med|med|4|more|big|low|unacc
high|vhigh|2|more|med|high|unacc
med|high|5more|2|big|med|unacc
high|low|5more|more|small|med|unacc
med|vhigh|3|2|big|high|unacc
low|high|5more|2|big|med|unacc
vhigh|low|4|2|big|med|unacc
med|med|4|2|med|high|unacc
vhigh|vhigh|5more|2|med|high|unacc
med|low|4|2|big|med|unacc
vhigh|high|3|4|med|high|unacc
low|vhigh|4|4|big|med|unacc
med|high|5more|4|small|high|unacc
high|low|3|more|med|med|unacc
med|vhigh|4|4|big|med|unacc
high|vhigh|5more|4|small|high|unacc
vhigh|low|2|more|small|high|unacc
med|low|5more|more|med|low|unacc
med|high|4|2|med|high|unacc
vhigh|vhigh|5more|4|small|high|unacc
med|vhigh|5more|2|big|med|unacc
vhigh|high|2|2|big|high|unacc
vhigh|low|3|more|big|low|unacc
vhigh|high|5more|4|med|med|unacc
med|vhigh|3|4|med|high|unacc
high|low|4|4|med|med|unacc
high|high|3|more|small|high|unacc
high|high|5more|4|med|med|unacc
low|high|3|more|small|high|unacc
low|med|2|4|med|high|unacc
low|low|4|4|med|med|unacc
low|low|2|4|big|med|unacc
low|low|3|more|big|low|unacc
low|low|5more|more|med|low|unacc
high|vhigh|3|4|med|high|unacc
high|low|3|more|big|low|unacc
vhigh|low|5more|2|small|high|unacc
high|low|3|2|med|high|unacc
low|high|4|2|med|high|unacc
low|vhigh|2|more|big|med|unacc
med|med|2|4|med|high|unacc
vhigh|low|2|4|big|med|unacc
med|vhigh|4|more|med|med|unacc
low|med|5more|more|small|med|unacc
high|low|2|4|big|med|unacc
low|med|4|4|small|high|unacc
med|low|3|more|big|low|unacc
vhigh|med|5more|more|small|med|unacc
vhigh|vhigh|2|more|big|med|unacc
high|low|2|more|small|high|unacc
low|vhigh|5more|2|big|med|unacc
low|med|5more|4|big|low|unacc
low|low|3|2|med|high|unacc
vhigh|high|3|more|small|high|unacc
high|med|4|2|big|med|unacc
low|med|4|2|big|med|unacc
vhigh|med|2|4|med|high|unacc
med|high|3|more|small|high|unacc
high|low|5more|more|med|low|unacc
med|low|5more|2|small|high|unacc
vhigh|low|3|2|med|high|unacc
vhigh|med|5more|4|big|low|unacc
low|high|4|more|big|low|unacc
med|low|3|2|med|high|unacc
high|low|5more|2|small|high|unacc
vhigh|med|4|4|small|high|unacc
vhigh|med|3|more|med|med|unacc
high|med|3|more|med|med|unacc
low|high|5more|4|med|med|unacc
med|low|2|4|big|med|unacc
med|high|4|more|big|low|unacc
low|high|2|2|big|high|unacc
med|med|5more|4|big|low|unacc
vhigh|high|4|more|big|low|unacc
high|med|5more|4|big|low|unacc
vhigh|vhigh|3|4|med|high|unacc
med|high|5more|4|med|med|unacc
med|med|5more|more|small|med|unacc
high|med|4|4|small|high|unacc
med|high|3|4|big|med|unacc
med|low|4|4|med|med|unacc
low|low|5more|2|small|high|unacc
vhigh|high|3|4|big|med|unacc
vhigh|vhigh|4|more|med|med|unacc
vhigh|high|4|2|med|high|unacc
high|high|4|2|med|high|unacc
high|med|2|4|med|high|unacc
low|vhigh|5more|4|small|high|unacc
low|vhigh|4|more|med|med|unacc
vhigh|low|4|4|med|med|unacc
low|med|3|more|med|med|unacc
low|low|2|more|small|high|unacc
vhigh|vhigh|5more|2|big|med|unacc
high|high|4|more|big|low|unacc
high|vhigh|2|more|big|med|unacc
high|high|2|2|big|high|unacc
med|vhigh|5more|4|small|high|unacc
low|vhigh|3|4|med|high|unacc
high|low|5more|2|med|med|unacc
med|vhigh|4|more|big|low|unacc
low|med|2|more|small|high|unacc
vhigh|low|4|4|big|low|unacc
high|vhigh|4|2|med|high|unacc
low|vhigh|4|more|big|low|unacc
high|high|5more|4|big|low|unacc
vhigh|high|2|4|med|high|unacc
vhigh|med|4|4|med|med|unacc
vhigh|high|5more|4|big|low|unacc
med|med|2|more|small|high|unacc
vhigh|med|3|2|med|high|unacc
med|low|5more|2|med|med|unacc
high|low|4|more|small|med|unacc
med|med|5more|2|small|high|unacc
low|med|3|2|med|high|unacc
vhigh|vhigh|4|more|big|low|unacc
high|low|4|4|big|low|unacc
low|vhigh|5more|4|med|med|unacc
low|high|2|4|med|high|unacc
med|vhigh|3|more|small|high|unacc
high|med|2|4|big|med|unacc
low|high|5more|more|small|med|unacc
med|low|3|4|small|high|unacc
vhigh|vhigh|3|more|small|high|unacc
high|vhigh|3|more|small|high|unacc
high|vhigh|4|more|big|low|unacc
low|med|3|more|big|low|unacc
high|vhigh|5more|4|med|med|unacc
vhigh|vhigh|2|2|big|high|unacc
med|high|5more|more|small|med|unacc
vhigh|vhigh|4|2|med|high|unacc
high|med|3|more|big|low|unacc
vhigh|vhigh|5more|4|med|med|unacc
low|high|3|more|med|med|unacc
low|high|4|4|small|high|unacc
med|high|4|4|small|high|unacc
med|vhigh|3|4|big|med|unacc
low|low|4|more|small|med|unacc
low|med|4|4|med|med|unacc
low|med|2|4|big|med|unacc
med|vhigh|2|2|big|high|unacc
low|med|5more|more|med|low|unacc
med|med|3|2|med|high|unacc
vhigh|high|4|4|small|high|unacc
low|low|4|4|big|low|unacc
high|vhigh|3|4|big|med|unacc
vhigh|med|5more|2|small|high|unacc
vhigh|high|3|more|med|med|unacc
high|med|5more|more|med|low|unacc
high|high|4|2|big|med|unacc
high|high|2|4|med|high|unacc
high|low|3|4|small|high|unacc
med|low|2|more|med|med|unacc
high|med|4|4|med|med|unacc
low|low|3|4|small|high|unacc
med|med|3|more|big|low|unacc
vhigh|low|2|more|med|med|unacc
low|vhigh|4|2|med|high|unacc
high|vhigh|2|2|big|high|unacc
high|med|2|more|small|high|unacc
med|high|4|2|big|med|unacc
vhigh|med|2|4|big|med|unacc
high|med|3|2|med|high|unacc
high|low|2|more|med|med|unacc
low|high|5more|4|big|low|unacc
med|med|5more|more|med|low|unacc
low|low|5more|2|med|med|unacc
med|low|4|4|big|low|unacc
med|low|3|2|big|med|unacc
vhigh|vhigh|3|4|big|med|unacc
vhigh|high|4|2|big|med|unacc
med|low|4|more|small|med|unacc
med|vhigh|5more|4|med|med|unacc
low|vhigh|3|4|big|med|unacc
low|low|2|more|med|med|unacc
med|high|3|more|med|med|unacc
med|med|2|4|big|med|unacc
vhigh|low|3|2|big|med|unacc
low|high|4|2|big|med|unacc
vhigh|low|5more|2|med|med|unacc
high|med|5more|2|small|high|unacc
high|low|3|2|big|med|unacc
low|low|3|2|big|med|unacc
med|med|4|4|med|med|unacc
vhigh|low|3|4|small|high|unacc
high|high|4|4|small|high|unacc
med|high|2|4|med|high|unacc
vhigh|high|3|more|big|low|unacc
med|med|5more|2|med|med|unacc
low|low|5more|2|big|low|unacc
high|vhigh|5more|4|big|low|unacc
vhigh|vhigh|5more|4|big|low|unacc
vhigh|low|2|more|big|low|unacc
vhigh|high|3|2|med|high|unacc
med|med|4|more|small|med|unacc
vhigh|med|3|4|small|high|unacc
med|high|4|4|med|med|unacc
high|high|4|4|med|med|unacc
low|med|2|more|med|med|unacc
med|high|3|more|big|low|unacc
vhigh|low|3|4|med|med|unacc
low|low|4|more|med|low|unacc
vhigh|high|2|4|big|med|unacc
vhigh|vhigh|3|more|med|med|unacc
high|high|5more|more|med|low|unacc
low|med|5more|2|med|med|unacc
med|high|2|more|small|high|unacc
vhigh|low|5more|2|big|low|unacc
high|med|5more|2|med|med|unacc
high|high|3|more|big|low|unacc
low|high|3|2|med|high|unacc
med|low|3|4|med|med|unacc
med|vhigh|3|more|med|med|unacc
med|vhigh|4|4|small|high|unacc
low|low|3|4|med|med|unacc
med|vhigh|2|4|med|high|unacc
vhigh|med|4|more|small|med|unacc
high|high|3|2|med|high|unacc
vhigh|vhigh|4|4|small|high|unacc
high|med|4|more|small|med|unacc
high|vhigh|2|4|med|high|unacc
med|low|5more|4|small|med|unacc
low|med|3|4|small|high|unacc
med|vhigh|5more|more|small|med|unacc
med|med|4|4|big|low|unacc
vhigh|low|4|more|med|low|unacc
low|high|5more|more|med|low|unacc
vhigh|med|2|more|med|med|unacc
high|low|2|more|big|low|unacc
low|high|2|more|small|high|unacc
vhigh|vhigh|5more|more|small|med|unacc
vhigh|med|5more|2|med|med|unacc
vhigh|med|3|2|big|med|unacc
med|vhigh|5more|4|big|low|unacc
low|high|3|more|big|low|unacc
vhigh|vhigh|4|2|big|med|unacc
high|med|3|4|small|high|unacc
vhigh|high|2|more|small|high|unacc
med|low|2|more|big|low|unacc
med|low|5more|2|big|low|unacc
high|high|5more|2|small|high|unacc
high|vhigh|3|more|med|med|unacc
low|low|4|2|small|high|unacc
high|low|3|4|med|med|unacc
high|low|5more|2|big|low|unacc
vhigh|med|4|4|big|low|unacc
low|med|3|2|big|med|unacc
vhigh|vhigh|2|4|med|high|unacc
med|high|3|2|med|high|unacc
low|low|2|more|big|low|unacc
med|vhigh|4|2|big|med|unacc
med|high|2|4|big|med|unacc
med|high|5more|more|med|low|unacc
med|med|3|2|big|med|unacc
high|low|2|2|med|high|unacc
vhigh|high|4|4|med|med|unacc
med|low|4|more|med|low|unacc
vhigh|low|2|2|med|high|unacc
low|low|2|2|med|high|unacc
vhigh|high|5more|more|med|low|unacc
med|low|2|2|med|high|unacc
high|med|2|more|med|med|unacc
low|vhigh|5more|4|big|low|unacc
high|low|5more|4|small|med|unacc
low|med|4|4|big|low|unacc
low|vhigh|4|2|big|med|unacc
med|high|5more|2|small|high|unacc
high|vhigh|5more|more|small|med|unacc
low|vhigh|5more|more|small|med|unacc
high|vhigh|4|2|big|med|unacc
vhigh|high|5more|2|small|high|unacc
low|high|5more|2|small|high|unacc
high|high|2|more|small|high|unacc
low|low|5more|4|small|med|unacc
low|vhigh|4|4|small|high|unacc
low|high|2|4|big|med|unacc
low|vhigh|2|4|med|high|unacc
low|high|4|4|med|med|unacc
low|vhigh|3|more|med|med|unacc
high|med|4|2|small|high|unacc
vhigh|med|4|2|small|high|unacc
vhigh|low|4|2|med|med|unacc
low|low|3|4|big|low|unacc
low|med|4|2|small|high|unacc
med|low|2|2|big|med|unacc
vhigh|med|2|more|big|low|unacc
low|vhigh|4|4|med|med|unacc
low|med|4|more|med|low|unacc
high|med|5more|2|big|low|unacc
high|high|5more|2|med|med|unacc
med|high|4|4|big|low|unacc
vhigh|vhigh|3|2|med|high|unacc
low|low|2|2|big|med|unacc
vhigh|med|2|2|med|high|unacc
vhigh|med|5more|4|small|med|unacc
med|high|2|more|med|med|unacc
vhigh|low|5more|4|med|low|unacc
med|low|3|more|small|med|unacc
low|high|2|more|med|med|unacc
low|high|3|4|small|high|unacc
low|low|2|4|small|high|unacc
med|high|5more|2|med|med|unacc
low|med|5more|2|big|low|unacc
med|med|2|more|big|low|unacc
high|med|3|4|med|med|unacc
med|low|5more|4|med|low|unacc
med|med|5more|2|big|low|unacc
vhigh|vhigh|5more|more|med|low|unacc
high|vhigh|2|more|small|high|unacc
low|med|3|4|med|med|unacc
vhigh|low|2|4|small|high|unacc
low|low|3|more|small|med|unacc
med|low|2|4|small|high|unacc
high|low|4|2|med|med|unacc
low|high|3|2|big|med|unacc
vhigh|high|4|4|big|low|unacc
med|vhigh|3|2|med|high|unacc
high|med|2|2|med|high|unacc
low|vhigh|5more|more|med|low|unacc
med|med|2|2|med|high|unacc
high|med|2|more|big|low|unacc
low|high|4|4|big|low|unacc
vhigh|vhigh|5more|2|small|high|unacc
high|vhigh|3|more|big|low|unacc
high|low|3|4|big|low|unacc
high|high|4|more|small|med|unacc
high|med|5more|4|small|med|unacc
high|low|3|more|small|med|unacc
high|high|3|4|small|high|unacc
low|vhigh|2|4|big|med|unacc
med|vhigh|2|4|big|med|unacc
high|low|2|4|small|high|unacc
vhigh|low|2|2|big|med|unacc
med|low|3|4|big|low|unacc
low|vhigh|3|more|big|low|unacc
high|vhigh|5more|more|med|low|unacc
high|vhigh|4|4|med|med|unacc
low|vhigh|2|more|small|high|unacc
low|med|2|more|big|low|unacc
med|high|3|2|big|med|unacc
vhigh|high|4|more|small|med|unacc
med|med|4|2|small|high|unacc
vhigh|med|3|4|med|med|unacc
vhigh|vhigh|3|more|big|low|unacc
med|vhigh|3|more|big|low|unacc
med|med|5more|4|small|med|unacc
vhigh|high|3|2|big|med|unacc
med|vhigh|5more|more|med|low|unacc
high|high|4|4|big|low|unacc
med|vhigh|2|more|small|high|unacc
high|high|3|2|big|med|unacc
high|vhigh|3|2|med|high|unacc
high|high|2|more|med|med|unacc
vhigh|low|3|4|big|low|unacc
vhigh|high|5more|2|med|med|unacc
vhigh|low|3|more|small|med|unacc
vhigh|med|4|more|med|low|unacc
high|low|2|2|big|med|unacc
low|vhigh|3|2|med|high|unacc
low|med|5more|4|small|med|unacc
med|med|3|4|med|med|unacc
med|high|3|4|small|high|unacc
med|high|4|more|small|med|unacc
med|low|4|2|med|med|unacc
vhigh|vhigh|4|4|med|med|unacc
high|vhigh|5more|2|small|high|unacc
low|low|4|2|med|med|unacc
high|vhigh|2|4|big|med|unacc
vhigh|high|3|4|small|high|unacc
med|med|4|more|med|low|unacc
low|low|5more|4|med|low|unacc
med|vhigh|5more|2|small|high|unacc
high|med|4|more|med|low|unacc
high|low|5more|4|med|low|unacc
vhigh|vhigh|2|4|big|med|unacc
med|vhigh|4|4|med|med|unacc
low|vhigh|3|2|big|med|unacc
med|high|2|2|med|high|unacc
high|high|2|2|med|high|unacc
high|low|3|more|med|low|unacc
med|low|3|2|small|high|unacc
high|high|5more|4|small|med|unacc
vhigh|low|3|more|med|low|unacc
vhigh|high|5more|2|big|low|unacc
vhigh|low|4|2|big|low|unacc
high|med|3|more|small|med|unacc
med|vhigh|3|2|big|med|unacc
med|high|5more|2|big|low|unacc
med|vhigh|4|4|big|low|unacc
med|med|2|4|small|high|unacc
med|vhigh|4|more|small|med|unacc
low|low|3|more|med|low|unacc
med|high|4|2|small|high|unacc
high|high|3|4|med|med|unacc
high|low|2|4|med|med|unacc
med|low|4|2|big|low|unacc
med|high|4|more|med|low|unacc
high|low|4|2|big|low|unacc
low|high|4|more|med|low|unacc
vhigh|high|5more|4|small|med|unacc
low|high|5more|2|big|low|unacc
low|med|4|2|med|med|unacc
low|low|3|2|small|high|unacc
low|med|3|more|small|med|unacc
med|low|4|4|small|med|unacc
vhigh|high|3|4|med|med|unacc
low|med|5more|4|med|low|unacc
high|vhigh|5more|2|med|med|unacc
vhigh|vhigh|2|more|med|med|unacc
med|vhigh|2|more|med|med|unacc
med|med|4|2|med|med|unacc
med|low|5more|more|small|low|unacc
vhigh|low|2|4|med|med|unacc
low|med|3|4|big|low|unacc
high|med|5more|4|med|low|unacc
low|low|4|4|small|med|unacc
vhigh|med|2|4|small|high|unacc
low|low|2|4|med|med|unacc
high|high|4|more|med|low|unacc
vhigh|vhigh|4|4|big|low|unacc
vhigh|high|2|more|big|low|unacc
high|med|3|4|big|low|unacc
vhigh|low|5more|more|small|low|unacc
low|vhigh|4|more|small|med|unacc
low|high|4|2|small|high|unacc
med|low|2|4|med|med|unacc
low|high|3|4|med|med|unacc
low|vhigh|3|4|small|high|unacc
low|high|2|more|big|low|unacc
med|med|2|2|big|med|unacc
vhigh|low|4|4|small|med|unacc
high|high|4|2|small|high|unacc
vhigh|vhigh|4|more|small|med|unacc
low|low|5more|more|small|low|unacc
high|low|3|2|small|high|unacc
vhigh|med|4|2|med|med|unacc
high|high|5more|2|big|low|unacc
high|high|2|more|big|low|unacc
vhigh|med|3|more|small|med|unacc
vhigh|med|2|2|big|med|unacc
med|vhigh|5more|2|med|med|unacc
high|low|4|4|small|med|unacc
med|vhigh|3|4|small|high|unacc
low|high|5more|4|small|med|unacc
high|vhigh|2|more|med|med|unacc
low|high|2|2|med|high|unacc
high|low|5more|more|small|low|unacc
low|med|2|2|big|med|unacc
high|vhigh|4|more|small|med|unacc
med|med|5more|4|med|low|unacc
high|med|4|2|med|med|unacc
med|med|3|4|big|low|unacc
low|vhigh|5more|2|med|med|unacc
vhigh|high|4|2|small|high|unacc
low|low|4|2|big|low|unacc
med|high|5more|4|small|med|unacc
vhigh|vhigh|3|4|small|high|unacc
vhigh|high|2|2|med|high|unacc
high|vhigh|3|4|small|high|unacc
vhigh|med|3|4|big|low|unacc
high|vhigh|3|2|big|med|unacc
vhigh|med|5more|4|med|low|unacc
med|med|3|more|small|med|unacc
high|med|2|4|small|high|unacc
med|high|2|2|big|med|unacc
high|vhigh|5more|4|small|med|unacc
vhigh|vhigh|4|2|small|high|unacc
med|vhigh|2|2|med|high|unacc
med|high|3|4|big|low|unacc
high|high|3|more|small|med|unacc
med|vhigh|3|4|med|med|unacc
med|low|2|4|big|low|unacc
low|med|5more|more|small|low|unacc
vhigh|med|3|more|med|low|unacc
high|high|2|4|small|high|unacc
high|med|4|2|big|low|unacc
vhigh|high|5more|4|med|low|unacc
med|high|4|2|med|med|unacc
med|high|5more|4|med|low|unacc
low|low|3|2|med|med|unacc
low|vhigh|3|4|med|med|unacc
low|vhigh|5more|4|small|med|unacc
high|med|5more|more|small|low|unacc
vhigh|low|2|more|small|med|unacc
high|low|2|4|big|low|unacc
med|high|3|more|small|med|unacc
vhigh|high|2|4|small|high|unacc
high|low|5more|2|small|med|unacc
med|low|4|4|med|low|unacc
vhigh|vhigh|2|2|med|high|unacc
low|vhigh|2|more|big|low|unacc
high|high|3|4|big|low|unacc
low|med|4|4|small|med|unacc
med|high|2|4|small|high|unacc
low|med|4|2|big|low|unacc
low|vhigh|2|2|med|high|unacc
high|med|3|more|med|low|unacc
low|med|3|more|med|low|unacc
high|med|3|2|small|high|unacc
vhigh|vhigh|3|4|med|med|unacc
med|vhigh|2|more|big|low|unacc
low|low|5more|2|small|med|unacc
vhigh|vhigh|2|more|big|low|unacc
high|vhigh|4|more|med|low|unacc
med|vhigh|5more|4|small|med|unacc
med|vhigh|4|2|small|high|unacc
med|low|2|more|small|med|unacc
high|low|3|2|med|med|unacc
low|med|3|2|small|high|unacc
med|med|4|2|big|low|unacc
low|high|2|2|big|med|unacc
vhigh|med|4|2|big|low|unacc
low|low|4|4|med|low|unacc
low|vhigh|4|more|med|low|unacc
vhigh|med|5more|more|small|low|unacc
high|vhigh|4|2|small|high|unacc
vhigh|med|2|4|med|med|unacc
low|low|2|4|big|low|unacc
vhigh|med|4|4|small|med|unacc
low|vhigh|5more|2|big|low|unacc
vhigh|vhigh|5more|4|small|med|unacc
low|high|3|4|big|low|unacc
vhigh|low|2|4|big|low|unacc
med|low|3|2|med|med|unacc
med|med|5more|more|small|low|unacc
vhigh|high|4|2|med|med|unacc
high|med|4|4|small|med|unacc
low|high|4|2|med|med|unacc
high|high|2|2|big|med|unacc
low|high|2|4|small|high|unacc
high|vhigh|3|4|med|med|unacc
vhigh|high|3|4|big|low|unacc
high|high|4|2|med|med|unacc
med|vhigh|4|more|med|low|unacc
high|high|5more|4|med|low|unacc
vhigh|high|2|2|big|med|unacc
low|high|5more|4|med|low|unacc
low|high|3|more|small|med|unacc
med|med|2|4|med|med|unacc
low|med|2|4|med|med|unacc
vhigh|low|5more|2|small|med|unacc
med|low|5more|2|small|med|unacc
high|vhigh|2|more|big|low|unacc
low|low|2|more|small|med|unacc
vhigh|low|3|2|med|med|unacc
vhigh|med|3|2|small|high|unacc
vhigh|low|4|4|med|low|unacc
high|low|4|4|med|low|unacc
high|vhigh|5more|2|big|low|unacc
med|med|3|2|small|high|unacc
high|low|2|more|small|med|unacc
med|vhigh|5more|2|big|low|unacc
vhigh|vhigh|5more|2|big|low|unacc
med|med|4|4|small|med|unacc
vhigh|low|5more|2|med|low|unacc
vhigh|low|2|2|small|high|unacc
low|low|2|2|small|high|unacc
high|high|5more|more|small|low|unacc
vhigh|high|3|2|small|high|unacc
vhigh|med|3|2|med|med|unacc
high|low|2|more|med|low|unacc
high|vhigh|3|4|big|low|unacc
high|vhigh|3|more|small|med|unacc
med|high|2|4|med|med|unacc
high|high|4|4|small|med|unacc
low|high|3|more|med|low|unacc
low|low|4|more|small|low|unacc
med|vhigh|2|2|big|med|unacc
vhigh|vhigh|3|more|small|med|unacc
low|vhigh|2|2|big|med|unacc
vhigh|high|4|4|small|med|unacc
high|low|3|2|big|low|unacc
high|low|5more|2|med|low|unacc
med|low|4|more|small|low|unacc
high|low|4|more|small|low|unacc
med|vhigh|3|more|small|med|unacc
high|med|2|more|small|med|unacc
med|high|5more|more|small|low|unacc
high|low|3|4|small|med|unacc
med|vhigh|3|4|big|low|unacc
low|high|3|2|small|high|unacc
low|vhigh|4|2|med|med|unacc
vhigh|low|3|4|small|med|unacc
med|med|2|4|big|low|unacc
med|med|3|2|med|med|unacc
low|med|3|2|med|med|unacc
vhigh|vhigh|2|2|big|med|unacc
med|high|4|2|big|low|unacc
vhigh|low|4|more|small|low|unacc
high|med|5more|2|small|med|unacc
low|med|2|4|big|low|unacc
vhigh|high|2|4|med|med|unacc
vhigh|high|3|more|med|low|unacc
med|vhigh|4|2|med|med|unacc
med|high|3|2|small|high|unacc
low|low|3|2|big|low|unacc
med|vhigh|5more|4|med|low|unacc
med|high|3|more|med|low|unacc
vhigh|low|2|more|med|low|unacc
low|med|2|more|small|med|unacc
high|vhigh|2|4|small|high|unacc
low|med|5more|2|small|med|unacc
high|vhigh|2|2|big|med|unacc
med|med|5more|2|small|med|unacc
high|low|2|2|small|high|unacc
med|low|2|2|small|high|unacc
vhigh|med|2|4|big|low|unacc
high|high|4|2|big|low|unacc
vhigh|vhigh|5more|4|med|low|unacc
vhigh|vhigh|4|2|med|med|unacc
med|low|5more|2|med|low|unacc
low|vhigh|3|more|small|med|unacc
low|high|5more|more|small|low|unacc
high|vhigh|5more|4|med|low|unacc
med|vhigh|2|4|small|high|unacc
med|low|3|4|small|med|unacc
low|high|2|4|med|med|unacc
low|low|3|4|small|med|unacc
low|med|4|4|med|low|unacc
med|low|3|2|big|low|unacc
low|low|5more|2|med|low|unacc
low|vhigh|3|4|big|low|unacc
high|med|4|4|med|low|unacc
vhigh|high|4|2|big|low|unacc
vhigh|med|4|4|med|low|unacc
low|high|4|2|big|low|unacc
low|vhigh|5more|4|med|low|unacc
med|med|2|more|small|med|unacc
high|high|3|2|small|high|unacc
low|vhigh|2|4|small|high|unacc
med|low|2|more|med|low|unacc
high|med|3|2|med|med|unacc
med|med|4|4|med|low|unacc
high|high|3|more|med|low|unacc
high|high|2|4|med|med|unacc
vhigh|high|5more|more|small|low|unacc
high|vhigh|4|2|med|med|unacc
low|high|4|4|small|med|unacc
vhigh|low|5more|4|small|low|unacc
vhigh|high|2|4|big|low|unacc
low|high|5more|2|small|med|unacc
low|vhigh|5more|more|small|low|unacc
low|med|3|2|big|low|unacc
vhigh|vhigh|5more|more|small|low|unacc
med|med|2|more|med|low|unacc
low|low|3|4|med|low|unacc
high|high|2|4|big|low|unacc
low|vhigh|4|2|big|low|unacc
high|low|4|2|small|med|unacc
vhigh|low|2|2|med|med|unacc
med|vhigh|4|4|small|med|unacc
vhigh|low|3|4|med|low|unacc
vhigh|vhigh|4|2|big|low|unacc
vhigh|vhigh|2|4|med|med|unacc
vhigh|med|4|more|small|low|unacc
med|vhigh|4|2|big|low|unacc
high|high|4|4|med|low|unacc
med|vhigh|5more|more|small|low|unacc
high|high|5more|2|small|med|unacc
med|low|4|2|small|med|unacc
low|low|2|2|med|med|unacc
vhigh|vhigh|4|4|small|med|unacc
vhigh|med|5more|2|med|low|unacc
vhigh|low|4|2|small|med|unacc
high|low|5more|4|small|low|unacc
low|med|2|more|med|low|unacc
med|vhigh|3|2|small|high|unacc
high|high|2|more|small|med|unacc
high|med|3|4|small|med|unacc
low|med|4|more|small|low|unacc
high|med|4|more|small|low|unacc
med|med|4|more|small|low|unacc
vhigh|vhigh|3|2|small|high|unacc
vhigh|vhigh|3|more|med|low|unacc
med|med|2|2|small|high|unacc
low|med|2|2|small|high|unacc
low|high|2|4|big|low|unacc
med|med|5more|2|med|low|unacc
high|low|3|4|med|low|unacc
low|vhigh|2|4|med|med|unacc
vhigh|high|3|2|med|med|unacc
low|med|5more|2|med|low|unacc
low|low|5more|4|small|low|unacc
low|low|4|2|small|med|unacc
vhigh|high|4|4|med|low|unacc
low|vhigh|4|4|small|med|unacc
med|med|3|2|big|low|unacc
high|high|3|2|med|med|unacc
vhigh|med|3|4|small|med|unacc
med|vhigh|2|4|med|med|unacc
high|vhigh|4|4|small|med|unacc
vhigh|med|2|more|med|low|unacc
high|vhigh|2|4|med|med|unacc
low|vhigh|3|more|med|low|unacc
high|vhigh|4|2|big|low|unacc
high|low|2|2|med|med|unacc
vhigh|med|2|2|small|high|unacc
low|vhigh|3|2|small|high|unacc
high|med|2|more|med|low|unacc
med|low|5more|4|small|low|unacc
vhigh|high|5more|2|small|med|unacc
low|high|3|2|med|med|unacc
low|high|2|more|small|med|unacc
med|low|3|4|med|low|unacc
high|med|3|2|big|low|unacc
high|med|5more|2|med|low|unacc
low|high|4|4|med|low|unacc
med|high|2|more|small|med|unacc
high|vhigh|3|more|med|low|unacc
med|low|2|2|med|med|unacc
med|high|5more|2|small|med|unacc
vhigh|med|3|2|big|low|unacc
med|high|2|4|big|low|unacc
low|vhigh|5more|2|small|med|unacc
high|high|3|2|big|low|unacc
med|med|4|2|small|med|unacc
high|med|2|2|med|med|unacc
med|vhigh|3|2|med|med|unacc
high|low|2|2|big|low|unacc
high|med|3|4|med|low|unacc
med|high|3|2|big|low|unacc
high|med|4|2|small|med|unacc
high|high|3|4|small|med|unacc
low|low|2|4|small|med|unacc
med|low|2|4|small|med|unacc
med|high|3|4|small|med|unacc
low|low|3|more|small|low|unacc
low|low|4|2|med|low|unacc
vhigh|vhigh|5more|2|small|med|unacc
vhigh|low|2|2|big|low|unacc
med|med|2|2|med|med|unacc
low|high|2|more|med|low|unacc
low|med|2|2|med|med|unacc
vhigh|high|2|more|med|low|unacc
vhigh|med|4|2|small|med|unacc
high|high|2|more|med|low|unacc
med|med|3|4|med|low|unacc
vhigh|high|3|2|big|low|unacc
med|vhigh|4|4|med|low|unacc
vhigh|med|5more|4|small|low|unacc
med|high|5more|2|med|low|unacc
low|vhigh|2|more|small|med|unacc
high|low|3|more|small|low|unacc
low|vhigh|4|4|med|low|unacc
med|high|2|more|med|low|unacc
vhigh|low|4|2|med|low|unacc
low|med|5more|4|small|low|unacc
vhigh|high|3|4|small|med|unacc
vhigh|vhigh|3|2|med|med|unacc
vhigh|low|3|more|small|low|unacc
vhigh|vhigh|4|4|med|low|unacc
vhigh|med|3|4|med|low|unacc
vhigh|high|5more|2|med|low|unacc
low|med|4|2|small|med|unacc
med|high|4|more|small|low|unacc
med|low|3|more|small|low|unacc
low|high|2|2|small|high|unacc
vhigh|high|2|2|small|high|unacc
med|vhigh|2|more|small|med|unacc
high|med|5more|4|small|low|unacc
low|vhigh|2|4|big|low|unacc
vhigh|high|4|more|small|low|unacc
med|high|2|2|small|high|unacc
low|high|3|4|small|med|unacc
med|low|4|2|med|low|unacc
high|high|5more|2|med|low|unacc
high|high|4|more|small|low|unacc
high|vhigh|2|4|big|low|unacc
low|med|3|4|med|low|unacc
med|vhigh|5more|2|small|med|unacc
high|low|4|2|med|low|unacc
high|vhigh|4|4|med|low|unacc
high|low|2|4|small|med|unacc
high|vhigh|5more|2|small|med|unacc
high|vhigh|3|2|med|med|unacc
med|med|5more|4|small|low|unacc
low|high|3|2|big|low|unacc
low|low|2|2|big|low|unacc
low|high|5more|2|med|low|unacc
med|low|2|2|big|low|unacc
vhigh|vhigh|2|4|big|low|unacc
vhigh|med|2|2|med|med|unacc
vhigh|high|2|2|med|med|unacc
low|vhigh|4|more|small|low|unacc
vhigh|vhigh|5more|2|med|low|unacc
med|vhigh|3|4|small|med|unacc
high|low|4|4|small|low|unacc
med|high|3|4|med|low|unacc
low|high|5more|4|small|low|unacc
vhigh|vhigh|3|2|big|low|unacc
med|low|2|4|med|low|unacc
high|med|3|more|small|low|unacc
med|high|4|2|small|med|unacc
med|vhigh|2|more|med|low|unacc
low|low|3|2|small|med|unacc
vhigh|med|3|more|small|low|unacc
med|vhigh|4|more|small|low|unacc
high|vhigh|2|2|small|high|unacc
vhigh|vhigh|2|more|med|low|unacc
vhigh|high|4|2|small|med|unacc
low|med|2|4|small|med|unacc
vhigh|med|2|2|big|low|unacc
high|high|3|4|med|low|unacc
high|med|2|4|small|med|unacc
vhigh|high|3|4|med|low|unacc
vhigh|vhigh|4|more|small|low|unacc
med|med|2|4|small|med|unacc
high|high|2|2|med|med|unacc
low|vhigh|3|4|small|med|unacc
vhigh|vhigh|3|4|small|med|unacc
high|low|2|4|med|low|unacc
low|high|2|2|med|med|unacc
high|med|2|2|big|low|unacc
high|high|5more|4|small|low|unacc
med|med|4|2|med|low|unacc
vhigh|vhigh|2|2|small|high|unacc
high|vhigh|4|more|small|low|unacc
med|low|3|2|small|med|unacc
high|med|4|2|med|low|unacc
med|vhigh|5more|2|med|low|unacc
low|high|4|2|small|med|unacc
high|high|4|2|small|med|unacc
vhigh|med|4|2|med|low|unacc
high|vhigh|3|2|big|low|unacc
med|vhigh|3|2|big|low|unacc
high|vhigh|2|more|med|low|unacc
vhigh|low|2|4|med|low|unacc
low|vhigh|2|2|small|high|unacc
vhigh|med|2|4|small|med|unacc
low|vhigh|2|more|med|low|unacc
vhigh|low|3|2|small|med|unacc
vhigh|high|5more|4|small|low|unacc
low|med|2|2|big|low|unacc
low|med|3|more|small|low|unacc
med|high|5more|4|small|low|unacc
med|med|3|more|small|low|unacc
med|med|2|2|big|low|unacc
vhigh|low|4|4|small|low|unacc
low|med|4|2|med|low|unacc
high|vhigh|3|4|small|med|unacc
low|low|4|4|small|low|unacc
high|low|3|2|small|med|unacc
med|low|4|4|small|low|unacc
med|high|2|2|med|med|unacc
low|low|2|4|med|low|unacc
low|vhigh|3|2|big|low|unacc
med|med|3|2|small|med|unacc
low|low|5more|2|small|low|unacc
med|high|2|2|big|low|unacc
vhigh|high|4|2|med|low|unacc
vhigh|vhigh|2|2|med|med|unacc
vhigh|med|3|2|small|med|unacc
low|high|2|2|big|low|unacc
med|vhigh|4|2|small|med|unacc
vhigh|vhigh|5more|4|small|low|unacc
high|vhigh|4|2|small|med|unacc
med|med|2|4|med|low|unacc
low|vhigh|3|4|med|low|unacc
high|low|5more|2|small|low|unacc
med|vhigh|5more|4|small|low|unacc
high|high|3|more|small|low|unacc
med|vhigh|2|2|med|med|unacc
vhigh|low|5more|2|small|low|unacc
vhigh|med|2|4|med|low|unacc
low|med|2|4|med|low|unacc
med|med|4|4|small|low|unacc
low|low|3|2|med|low|unacc
high|low|2|more|small|low|unacc
high|med|2|4|med|low|unacc
high|vhigh|5more|4|small|low|unacc
vhigh|low|3|2|med|low|unacc
vhigh|vhigh|4|2|small|med|unacc
vhigh|med|4|4|small|low|unacc
high|low|3|2|med|low|unacc
med|high|3|more|small|low|unacc
med|low|5more|2|small|low|unacc
low|high|4|2|med|low|unacc
low|high|2|4|small|med|unacc
low|low|2|more|small|low|unacc
low|vhigh|4|2|small|med|unacc
med|high|4|2|med|low|unacc
vhigh|high|2|2|big|low|unacc
low|vhigh|5more|4|small|low|unacc
vhigh|high|2|4|small|med|unacc
vhigh|low|2|more|small|low|unacc
low|high|3|more|small|low|unacc
high|vhigh|3|4|med|low|unacc
med|high|2|4|small|med|unacc
vhigh|vhigh|3|4|med|low|unacc
high|high|2|4|small|med|unacc
high|med|3|2|small|med|unacc
high|high|2|2|big|low|unacc
med|high|2|4|med|low|unacc
low|vhigh|2|4|small|med|unacc
high|med|2|more|small|low|unacc
med|med|5more|2|small|low|unacc
med|low|3|4|small|low|unacc
low|med|2|more|small|low|unacc
vhigh|vhigh|4|2|med|low|unacc
med|med|2|more|small|low|unacc
high|vhigh|4|2|med|low|unacc
low|med|3|2|med|low|unacc
low|high|3|2|small|med|unacc
high|med|5more|2|small|low|unacc
high|high|2|4|med|low|unacc
low|low|3|4|small|low|unacc
vhigh|med|5more|2|small|low|unacc
vhigh|med|2|more|small|low|unacc
high|high|3|2|small|med|unacc
med|vhigh|3|more|small|low|unacc
med|vhigh|2|2|big|low|unacc
high|vhigh|2|2|big|low|unacc
vhigh|vhigh|2|2|big|low|unacc
med|low|2|2|small|med|unacc
high|low|2|2|small|med|unacc
high|vhigh|2|4|small|med|unacc
vhigh|med|3|2|med|low|unacc
high|med|3|2|med|low|unacc
vhigh|high|4|4|small|low|unacc
low|low|2|2|small|med|unacc
med|vhigh|2|4|small|med|unacc
vhigh|low|2|2|small|med|unacc
high|vhigh|3|more|small|low|unacc
high|high|4|4|small|low|unacc
low|vhigh|3|more|small|low|unacc
vhigh|vhigh|3|more|small|low|unacc
low|med|5more|2|small|low|unacc
low|vhigh|2|2|big|low|unacc
vhigh|vhigh|2|4|small|med|unacc
vhigh|low|3|4|small|low|unacc
low|high|2|4|med|low|unacc
high|low|3|4|small|low|unacc
med|high|4|4|small|low|unacc
med|med|3|2|med|low|unacc
vhigh|high|2|4|med|low|unacc
low|high|4|4|small|low|unacc
low|vhigh|4|2|med|low|unacc
med|high|3|2|small|med|unacc
vhigh|low|4|2|small|low|unacc
med|high|2|more|small|low|unacc
vhigh|med|3|4|small|low|unacc
high|high|2|more|small|low|unacc
low|high|2|more|small|low|unacc
med|high|3|2|med|low|unacc
vhigh|high|2|more|small|low|unacc
low|vhigh|2|4|med|low|unacc
med|high|5more|2|small|low|unacc
vhigh|high|3|2|med|low|unacc
med|low|4|2|small|low|unacc
vhigh|vhigh|3|2|small|med|unacc
med|low|2|2|med|low|unacc
low|vhigh|4|4|small|low|unacc
high|med|2|2|small|med|unacc
high|vhigh|2|4|med|low|unacc
high|low|4|2|small|low|unacc
high|med|3|4|small|low|unacc
med|med|2|2|small|med|unacc
low|med|3|4|small|low|unacc
low|vhigh|3|2|small|med|unacc
low|low|4|2|small|low|unacc
low|low|2|2|med|low|unacc
vhigh|med|2|2|small|med|unacc
vhigh|high|5more|2|small|low|unacc
low|med|2|2|small|med|unacc
vhigh|vhigh|2|4|med|low|unacc
high|high|5more|2|small|low|unacc
vhigh|low|2|2|med|low|unacc
med|med|3|4|small|low|unacc
med|vhigh|4|4|small|low|unacc
vhigh|vhigh|4|4|small|low|unacc
high|vhigh|3|2|small|med|unacc
med|vhigh|2|4|med|low|unacc
low|high|3|2|med|low|unacc
high|vhigh|4|4|small|low|unacc
med|low|2|4|small|low|unacc
high|med|4|2|small|low|unacc
high|low|2|4|small|low|unacc
high|vhigh|5more|2|small|low|unacc
vhigh|vhigh|3|2|med|low|unacc
vhigh|low|2|4|small|low|unacc
low|low|2|4|small|low|unacc
med|med|2|2|med|low|unacc
low|high|2|2|small|med|unacc
vhigh|high|2|2|small|med|unacc
vhigh|vhigh|5more|2|small|low|unacc
low|vhigh|3|2|med|low|unacc
high|vhigh|3|2|med|low|unacc
low|med|2|2|med|low|unacc
low|med|4|2|small|low|unacc
high|high|2|2|small|med|unacc
med|vhigh|3|2|med|low|unacc
high|high|3|4|small|low|unacc
vhigh|high|3|4|small|low|unacc
high|med|2|2|med|low|unacc
vhigh|med|4|2|small|low|unacc
low|vhigh|2|more|small|low|unacc
high|vhigh|2|more|small|low|unacc
low|vhigh|5more|2|small|low|unacc
med|vhigh|2|more|small|low|unacc
low|high|3|4|small|low|unacc
med|vhigh|5more|2|small|low|unacc
vhigh|vhigh|2|more|small|low|unacc
med|med|4|2|small|low|unacc
vhigh|med|2|2|med|low|unacc
med|high|2|2|small|med|unacc
med|high|3|4|small|low|unacc
high|med|2|4|small|low|unacc
med|high|2|2|med|low|unacc
low|low|3|2|small|low|unacc
high|vhigh|3|4|small|low|unacc
med|vhigh|3|4|small|low|unacc
high|high|4|2|small|low|unacc
low|vhigh|2|2|small|med|unacc
high|vhigh|2|2|small|med|unacc
low|med|2|4|small|low|unacc
med|low|3|2|small|low|unacc
med|high|4|2|small|low|unacc
high|low|3|2|small|low|unacc
vhigh|low|3|2|small|low|unacc
vhigh|vhigh|2|2|small|med|unacc
vhigh|vhigh|3|4|small|low|unacc
low|high|2|2|med|low|unacc
low|high|4|2|small|low|unacc
vhigh|high|2|2|med|low|unacc
vhigh|high|4|2|small|low|unacc
low|vhigh|4|2|small|low|unacc
low|high|2|4|small|low|unacc
vhigh|vhigh|2|2|med|low|unacc
vhigh|med|3|2|small|low|unacc
med|high|2|4|small|low|unacc
high|high|2|4|small|low|unacc
low|vhigh|2|2|med|low|unacc
med|vhigh|2|2|med|low|unacc
med|vhigh|4|2|small|low|unacc
vhigh|vhigh|4|2|small|low|unacc
high|vhigh|2|2|med|low|unacc
vhigh|high|2|4|small|low|unacc
med|med|3|2|small|low|unacc
low|med|3|2|small|low|unacc
high|med|3|2|small|low|unacc
med|low|2|2|small|low|unacc
low|vhigh|2|4|small|low|unacc
vhigh|low|2|2|small|low|unacc
high|high|3|2|small|low|unacc
low|high|3|2|small|low|unacc
vhigh|high|3|2|small|low|unacc
low|low|2|2|small|low|unacc
high|low|2|2|small|low|unacc
med|vhigh|2|4|small|low|unacc
high|vhigh|2|4|small|low|unacc
vhigh|vhigh|2|4|small|low|unacc
low|med|2|2|small|low|unacc
high|vhigh|3|2|small|low|unacc
vhigh|med|2|2|small|low|unacc
med|med|2|2|small|low|unacc
high|med|2|2|small|low|unacc
low|vhigh|3|2|small|low|unacc
vhigh|vhigh|3|2|small|low|unacc
low|high|2|2|small|low|unacc
med|high|2|2|small|low|unacc
high|high|2|2|small|low|unacc
vhigh|high|2|2|small|low|unacc
low|vhigh|2|2|small|low|unacc
vhigh|vhigh|2|2|small|low|unacc
med|vhigh|2|2|small|low|unacc

## PART

Decision list:

rules | predicted class
---|---
Safety = low|unacc (528.0)
Persons = 2|unacc (339.0)
Maint = vhigh AND Buying = high|unacc (44.0)
Buying = vhigh AND Maint = vhigh|unacc (42.0)
Buying = vhigh AND Maint = high|unacc (42.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Maint != vhigh AND Buying != vhigh AND Maint != high AND Doors != 2|acc (21.0)
Safety = med AND Lug_boot = small AND Maint = vhigh|unacc (16.0)
Safety = med AND Lug_boot = small AND Buying != low AND Doors != 2|unacc (15.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (52.0)
Safety = med AND Lug_boot = big AND Buying != vhigh AND Maint != low AND Maint != med|acc (27.0)
Safety = med AND Lug_boot = big AND Buying != low AND Buying != med|acc (23.0)
Safety != med AND Lug_boot != small AND Buying != vhigh AND Maint != vhigh AND Buying != high AND Maint != high AND Doors != 2 AND Doors != 3|vgood (31.0)
Safety != med AND Lug_boot != small AND Buying != low AND Buying != med|acc (53.0)
Maint = vhigh AND Doors != 2 AND Safety != med|acc (32.0)
Lug_boot != big AND Doors = 2 AND Persons != 4 AND Lug_boot = small|unacc (18.0)
Safety != med AND Lug_boot = big AND Maint != low AND Maint != med AND Buying = med|acc (9.0)
Lug_boot != big AND Safety != med AND Maint = high AND Buying != low|acc (16.0)
Safety = med AND Buying = high AND Doors = 2|unacc (5.0)
Lug_boot != big AND Safety = med AND Doors = 2 AND Buying != vhigh AND Maint = low|acc (6.0)
Safety = med AND Lug_boot = big AND Buying != med|good (13.0)
Lug_boot = big AND Safety != med AND Doors != 2|vgood (10.0)
Safety = med AND Maint != low AND Doors != 2 AND Doors != 3 AND Buying != low|acc (20.0)
Safety != med AND Lug_boot = big AND Maint != low|vgood (6.0/2.0)
Buying = vhigh AND Safety != med|acc (14.0)
Buying = vhigh AND Doors != 2|acc (7.0/2.0)
Maint = low AND Buying != high AND Safety != med AND Lug_boot != big AND Doors != 3|good (14.0)
Buying != vhigh AND Maint != low AND Maint != med AND Buying = low AND Safety = med AND Maint != vhigh|acc (14.0)
Buying != vhigh AND Maint = vhigh AND Safety = med AND Persons = 4|unacc (6.0/2.0)
Buying != vhigh AND Buying = high AND Lug_boot = small|acc (6.0)
Buying != vhigh AND Buying != high AND Maint = low AND Safety = med AND Doors != 3|good (11.0)
Buying = vhigh|unacc (5.0)
Safety = med AND Maint = high|unacc (5.0/1.0)
Maint = vhigh AND Buying != med|acc (6.0)
Buying != high AND Maint != vhigh AND Maint = high AND Lug_boot = small|acc (6.0)
Maint = high AND Persons = 4|acc (4.0/2.0)
Buying != high AND Buying = med AND Maint != low AND Maint != vhigh AND Doors != 3|acc (10.0)
Buying != high AND Maint != vhigh AND Safety = med AND Persons != 4|good (8.0/2.0)
Safety = med AND Buying != high AND Doors = 3|acc (7.0/1.0)
Buying != high AND Maint != vhigh AND Lug_boot != big AND Maint != high AND Lug_boot = small AND Maint = med|good (8.0/2.0)
Buying != high AND Maint != vhigh AND Lug_boot != small AND Maint != med AND Maint != high|vgood (6.0)
Maint != high AND Buying != high AND Maint != vhigh AND Persons = 4|good (8.0/2.0)
Safety != med AND Doors != 2|vgood (7.0/2.0)
Safety = med|unacc (5.0/2.0)
|acc (5.0/1.0)


## SimpleCart Decision Tree

	* Safety=(high)|(med)
		* Persons=(more)|(4)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): vgood(31.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Persons=(more)|(2): vgood(7.0/0.0)
									* Persons!=(more)|(2)
										* Lug_boot=(big)|(small): vgood(3.0/0.0)
										* Lug_boot!=(big)|(small): acc(1.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): vgood(7.0/0.0)
							* Lug_boot!=(big)
										* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
										* Buying!=(low)|(vhigh)|(high)
											* Maint=(low)|(vhigh)|(high): good(2.0/0.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/0.0)
						* Lug_boot!=(big)|(med)
								* Maint=(low)|(vhigh)|(high)
									* Doors=(5more)|(4)|(3): good(12.0/0.0)
									* Doors!=(5more)|(4)|(3): good(2.0/1.0)
								* Maint!=(low)|(vhigh)|(high)
									* Buying=(low)|(vhigh)|(high): good(6.0/1.0)
									* Buying!=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(4.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
								* Buying=(low)|(vhigh)|(high)
								* Doors=(5more)|(4): good(14.0/0.0)
								* Doors!=(5more)|(4)
								* Lug_boot=(big): good(6.0/0.0)
								* Lug_boot!=(big)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): good(2.0/0.0)
											* Persons!=(more)|(2): acc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): acc(4.0/0.0)
								* Buying!=(low)|(vhigh)|(high)
									* Maint=(low)|(vhigh)|(high)
									* Lug_boot=(big)|(small): good(7.0/0.0)
									* Lug_boot!=(big)|(small)
										* Doors=(5more)|(4): good(3.0/0.0)
										* Doors!=(5more)|(4)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(21.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Buying=(low)
						* Maint=(high)
							* Safety=(high)
										* Doors=(5more)|(4)|(3)
											* Doors=(5more)|(4)|(2): vgood(6.0/0.0)
											* Doors!=(5more)|(4)|(2)
											* Persons=(more)|(2): vgood(2.0/0.0)
											* Persons!=(more)|(2): acc(1.0/1.0)
										* Doors!=(5more)|(4)|(3): acc(2.0/1.0)
							* Safety!=(high): acc(14.0/0.0)
						* Maint!=(high)
								* Safety=(high)|(low): acc(15.0/0.0)
								* Safety!=(high)|(low)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4)
										* Lug_boot=(big)|(small): acc(4.0/0.0)
										* Lug_boot!=(big)|(small): unacc(2.0/1.0)
					* Buying!=(low)
								* Doors=(5more)|(4)|(3)
									* Doors=(5more)|(4)|(2): acc(30.0/0.0)
									* Doors!=(5more)|(4)|(2)
									* Lug_boot=(big)|(small): acc(8.0/0.0)
									* Lug_boot!=(big)|(small)
											* Maint=(high)|(med)|(low): acc(3.0/0.0)
											* Maint!=(high)|(med)|(low): acc(2.0/1.0)
								* Doors!=(5more)|(4)|(3)
							* Lug_boot=(big): acc(6.0/0.0)
							* Lug_boot!=(big)
								* Safety=(high): acc(3.0/0.0)
								* Safety!=(high): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
					* Safety=(high)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
					* Safety!=(high)
						* Maint=(high)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(7.0/0.0)
						* Maint!=(high): unacc(16.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
					* Lug_boot=(big): acc(59.0/0.0)
					* Lug_boot!=(big)
							* Safety=(high)|(low): acc(30.0/0.0)
							* Safety!=(high)|(low)
								* Doors=(5more)|(4): acc(15.0/0.0)
								* Doors!=(5more)|(4)
										* Doors=(3)|(4)|(5more)
										* Persons=(more)|(2): acc(4.0/0.0)
										* Persons!=(more)|(2): unacc(4.0/0.0)
										* Doors!=(3)|(4)|(5more): unacc(7.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(23.0/0.0)
								* Doors!=(5more)|(4)|(3)
							* Persons=(more): unacc(3.0/0.0)
							* Persons!=(more): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(27.0/0.0)
				* Maint!=(low)|(med)
				* Maint=(high)
					* Buying=(high)
							* Safety=(high)|(low)
									* Doors=(5more)|(4)|(3): acc(15.0/0.0)
									* Doors!=(5more)|(4)|(3)
									* Lug_boot=(big)|(med): acc(4.0/0.0)
									* Lug_boot!=(big)|(med): unacc(1.0/1.0)
							* Safety!=(high)|(low)
								* Lug_boot=(big)|(med)
									* Doors=(5more)|(4): acc(7.0/0.0)
									* Doors!=(5more)|(4): unacc(3.0/1.0)
								* Lug_boot!=(big)|(med): unacc(7.0/0.0)
					* Buying!=(high): unacc(42.0/0.0)
				* Maint!=(high): unacc(86.0/0.0)
		* Persons!=(more)|(4): unacc(339.0/0.0)
	* Safety!=(high)|(med): unacc(528.0/0.0)


