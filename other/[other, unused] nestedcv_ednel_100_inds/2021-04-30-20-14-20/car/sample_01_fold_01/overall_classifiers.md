# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons != 4 | unacc | 0.603276 |
| Persons != more | unacc | 0.602607 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors != 3 and Persons!=(more) | acc | 0.004942 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot = med and Buying!=(low) and Maint != low | acc | 0.002477 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Safety != low and Lug_boot!=(big) and Doors = 5more | acc | 0.001653 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 4 | acc | 0.001103 |
| Persons = 4 and Safety = med and Buying != med and Maint = med and Lug_boot = med and Safety != low and Lug_boot!=(big) and Doors = 4 | acc | 0.001103 |
| Persons = 4 and Safety = med and Buying = med and Maint != med and Lug_boot = med and Safety!=(high) and Doors = 5more | acc | 0.001103 |
| Persons = 4 and Safety = med and Buying = med and Maint = med and Safety != low and Lug_boot != med and Doors = 3 | acc | 0.000827 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Persons = 2 | unacc | 0.529889 |
| Safety = low | unacc | 0.425031 |
| Buying = vhigh and Maint = vhigh | unacc | 0.093750 |
| Buying != low and Buying != med and Maint != vhigh and Lug_boot != small and Maint != high and Safety != med | acc | 0.167139 |
| Buying = vhigh and Maint = high | unacc | 0.095982 |
| Buying = high and Maint = vhigh | unacc | 0.091928 |
| Safety = med and Lug_boot = small and Buying = high | unacc | 0.051522 |
| Safety = med and Lug_boot = small and Buying != vhigh and Maint != vhigh and Doors != 2 and Maint != high | acc | 0.096154 |
| Safety = med and Lug_boot = small and Maint != high and Doors != 2 | unacc | 0.049383 |
| Safety = med and Lug_boot = small and Buying != low and Persons != 4 | unacc | 0.017857 |
| Safety = med and Lug_boot = big and Maint != low and Buying != low | acc | 0.210784 |
| Maint = vhigh and Doors != 2 | acc | 0.222609 |
| Buying = high and Doors != 2 and Doors != 3 | acc | 0.157068 |
| Safety = med and Lug_boot = big and Maint != high and Buying != vhigh and Buying != high and Maint != vhigh | good | 0.078652 |
| Lug_boot = big and Safety != med and Buying != high and Maint != vhigh and Maint != high | vgood | 0.113725 |
| Doors = 2 and Lug_boot = big | acc | 0.098142 |
| Doors = 2 and Safety = med and Buying != vhigh and Buying != high and Maint != vhigh and Maint != high | acc | 0.083333 |
| Doors = 2 and Safety = med and Buying != low | unacc | 0.073171 |
| Doors = 2 and Persons = 4 and Maint != low | acc | 0.107752 |
| Doors = 2 and Persons = 4 and Buying = med | good | 0.012048 |
| Doors = 2 and Lug_boot = small and Persons != 4 | unacc | 0.084211 |
| Safety = med and Maint = high | acc | 0.223214 |
| Buying != low and Buying != med and Lug_boot != med | acc | 0.257143 |
| Maint = high and Buying != low | acc | 0.191406 |
| Safety = med and Buying = vhigh and Doors != 3 | acc | 0.082353 |
| Safety = med and Doors != 3 and Maint = low | good | 0.093333 |
| Safety = med and Buying != low and Persons != 4 | acc | 0.079545 |
| Safety != med and Lug_boot = small and Maint != high and Buying != med | good | 0.175676 |
| Safety != med and Lug_boot = small and Maint != low | acc | 0.147059 |
| Safety != med and Lug_boot != small and Doors != 2 and Doors != 3 | vgood | 0.377049 |
| Safety != med and Lug_boot = small | good | 0.151515 |
| Safety = med and Buying != med and Buying = low and Maint = med | good | 0.103226 |
| Safety = med and Buying != med | unacc | 0.206452 |
| Maint = low | good | 0.142045 |
| Doors != 3 | acc | 0.198413 |
| Persons = 4 | acc | 0.189394 |
|  | vgood | 0.538462 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Safety = high and Buying = low and Lug_boot = big and Persons = 4 and Maint = med | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big and Maint = med | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = med and Doors = 3 | vgood | 0.002004 |
| Safety = high and Buying = med and Maint = med and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = low and Lug_boot = big and Maint = high and Persons = 4 | vgood | 0.002004 |
| Safety = high and Buying = med and Maint = low and Lug_boot = big and Persons = 4 | vgood | 0.002670 |
| Safety = high and Buying = low and Persons = more and Lug_boot = big and Maint = high | vgood | 0.002004 |
| Safety = high and Buying = low and Maint = low and Lug_boot = big and Persons = 4 | vgood | 0.002004 |
| Safety = high and Persons = more and Buying = med and Maint = med and Lug_boot = big | vgood | 0.002670 |
| Safety = high and Lug_boot = med and Buying = low and Doors = 4 and Persons = 4 | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med and Doors = 5more | vgood | 0.001337 |
| Safety = high and Persons = more and Maint = low and Buying = med and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Lug_boot = med and Persons = more and Buying = low and Doors = 4 | vgood | 0.001504 |
| Safety = high and Lug_boot = med and Buying = med and Maint = low and Persons = more | vgood | 0.001504 |
| Safety = high and Buying = low and Doors = 5more and Lug_boot = med and Persons = 4 | vgood | 0.001504 |
| Safety = high and Persons = more and Buying = low and Maint = low and Lug_boot = big | vgood | 0.002004 |
| Safety = high and Lug_boot = med and Buying = med and Maint = med and Doors = 4 | vgood | 0.000892 |
| Buying = low and Maint = med and Persons = 4 and Safety = high | good | 0.003463 |
| Maint = low and Buying = med and Persons = 4 and Safety = high and Lug_boot = small | good | 0.002772 |
| Buying = low and Maint = low and Persons = 4 and Safety = high | good | 0.004152 |
| Buying = low and Safety = med and Maint = med and Lug_boot = big and Persons = 4 | good | 0.002772 |
| Maint = low and Safety = med and Buying = med and Lug_boot = big and Persons = more | good | 0.002772 |
| Buying = low and Persons = more and Maint = med and Safety = med and Lug_boot = big | good | 0.002772 |
| Maint = low and Safety = med and Buying = low and Lug_boot = big and Persons = 4 | good | 0.002772 |
| Maint = low and Buying = med and Safety = med and Persons = 4 and Lug_boot = big | good | 0.002080 |
| Maint = low and Persons = more and Buying = low and Safety = high | good | 0.001561 |
| Maint = low and Buying = med and Lug_boot = med and Safety = med and Persons = more | good | 0.001561 |
| Buying = low and Persons = more and Maint = med and Safety = high and Lug_boot = small | good | 0.001561 |
| Maint = low and Buying = med and Safety = high and Persons = more | good | 0.001561 |
| Buying = low and Safety = med and Lug_boot = med and Maint = med and Persons = more | good | 0.001561 |
| Maint = low and Safety = med and Buying = low and Persons = more and Lug_boot = big | good | 0.001388 |
| Lug_boot = med and Maint = low and Persons = 4 and Buying = med and Safety = med | good | 0.000926 |
| Lug_boot = med and Buying = low and Safety = med and Doors = 4 and Maint = low | good | 0.000926 |
| Safety = high and Persons = 4 and Maint = med | acc | 0.023111 |
| Persons = more and Safety = high and Maint = low and Lug_boot = big | acc | 0.007227 |
| Persons = more and Safety = high and Buying = med and Lug_boot = big | acc | 0.007227 |
| Persons = more and Safety = high and Maint = med and Lug_boot = big | acc | 0.007227 |
| Safety = med and Persons = more and Lug_boot = big and Maint = med | acc | 0.009910 |
| Persons = 4 and Safety = high and Buying = low | acc | 0.014350 |
| Safety = med and Persons = 4 and Lug_boot = big and Buying = med | acc | 0.009910 |
| Persons = more and Safety = high and Maint = low and Lug_boot = med | acc | 0.006329 |
| Persons = more and Safety = high and Buying = med and Doors = 4 | acc | 0.004529 |
| Safety = med and Persons = more and Buying = low and Lug_boot = big | acc | 0.007227 |
| Safety = med and Persons = 4 and Buying = low and Maint = high | acc | 0.010801 |
| Persons = more and Safety = high and Maint = med and Buying = vhigh and Lug_boot = med | acc | 0.003626 |
| Persons = more and Safety = high and Buying = low and Maint = vhigh and Lug_boot = big | acc | 0.003626 |
| Safety = med and Persons = more and Lug_boot = med and Maint = low | acc | 0.006329 |
| Persons = 4 and Safety = high and Maint = low and Buying = high | acc | 0.009910 |
| Safety = med and Persons = more and Buying = med and Lug_boot = big | acc | 0.006329 |
| Safety = med and Persons = 4 and Lug_boot = big and Maint = low | acc | 0.007227 |
| Persons = more and Safety = high and Buying = high and Maint = high and Lug_boot = med | acc | 0.003626 |
| Persons = more and Safety = high and Buying = med and Lug_boot = med and Maint = vhigh | acc | 0.002722 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Maint = med | acc | 0.003626 |
| Safety = med and Persons = 4 and Buying = low and Lug_boot = big | acc | 0.003626 |
| Persons = more and Safety = high and Maint = med and Buying = high and Lug_boot = med | acc | 0.003626 |
| Safety = med and Persons = more and Buying = low and Maint = high and Lug_boot = med | acc | 0.003626 |
| Persons = 4 and Safety = high and Buying = med and Maint = high | acc | 0.009017 |
| Safety = med and Persons = 4 and Maint = med and Lug_boot = big | acc | 0.006329 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 3 and Maint = med | acc | 0.002722 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 5more and Buying = med | acc | 0.001817 |
| Safety = med and Persons = more and Lug_boot = med and Buying = med and Doors = 3 | acc | 0.001817 |
| Safety = med and Persons = more and Buying = low and Maint = low | acc | 0.002722 |
| Safety = med and Persons = more and Lug_boot = med and Maint = med and Doors = 3 | acc | 0.001817 |
| Safety = med and Persons = 4 and Buying = med and Maint = med | acc | 0.005430 |
| Persons = more and Safety = high and Buying = low and Maint = vhigh and Doors = 5more | acc | 0.001817 |
| Persons = more and Safety = high and Maint = low and Doors = 3 | acc | 0.001817 |
| Persons = more and Safety = med and Lug_boot = med and Doors = 5more and Buying = med | acc | 0.001817 |
| Persons = 4 and Safety = high and Maint = low and Buying = vhigh | acc | 0.009017 |
| Persons = more and Safety = high and Maint = high and Buying = high and Lug_boot = big | acc | 0.003626 |
| Safety = med and Persons = more and Buying = low and Maint = high | acc | 0.002044 |
| Safety = med and Persons = 4 and Buying = low and Maint = low and Lug_boot = small | acc | 0.003626 |
| Safety = med and Persons = more and Maint = med and Doors = 4 and Lug_boot = med | acc | 0.001817 |
| Safety = med and Persons = more and Buying = med and Doors = 4 and Lug_boot = med | acc | 0.001817 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more and Buying = med | acc | 0.001817 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 4 and Buying = low | acc | 0.001817 |
| Safety = med and Persons = more and Maint = low and Lug_boot = big | acc | 0.003626 |
| Persons = 4 and Safety = high and Buying = med and Maint = vhigh | acc | 0.008123 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 and Buying = med | acc | 0.001817 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 5more and Maint = med | acc | 0.001817 |
| Safety = med and Persons = 4 and Buying = low and Maint = med and Doors = 3 | acc | 0.001817 |
| Persons = more and Safety = high and Lug_boot = small and Doors = 4 and Maint = med | acc | 0.001817 |
| Safety = med and Persons = more and Maint = med and Doors = 5more and Lug_boot = med | acc | 0.001817 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 5more and Maint = med | acc | 0.001817 |
| Persons = more and Safety = high and Maint = high and Buying = med and Lug_boot = med | acc | 0.002722 |
| Safety = med and Persons = more and Buying = low and Maint = med | acc | 0.002904 |
| Safety = med and Persons = 4 and Maint = low and Buying = med | acc | 0.003626 |
| Persons = more and Safety = high and Lug_boot = small and Maint = low and Doors = 4 | acc | 0.001817 |
| Safety = med and Persons = more and Buying = med and Maint = med | acc | 0.002044 |
| Maint = high and Buying = high and Persons = 4 and Safety = high | acc | 0.008123 |
| Safety = med and Persons = 4 and Lug_boot = med and Doors = 4 | acc | 0.002525 |
| Persons = more and Safety = high and Buying = low and Doors = 3 | acc | 0.001817 |
| Persons = more and Safety = high and Maint = high and Buying = high | acc | 0.002044 |
| Safety = med and Persons = more and Lug_boot = med and Buying = low | acc | 0.002044 |
| Safety = med and Persons = 4 and Buying = low and Lug_boot = med | acc | 0.001365 |
| Safety = med and Buying = high and Maint = high and Lug_boot = big and Persons = 4 | acc | 0.003626 |
| Persons = more and Safety = med and Maint = high and Buying = high and Lug_boot = big | acc | 0.002722 |
|  | unacc | 0.974933 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Persons = 4) and (Maint = med)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big) and (Maint = med)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = med) and (Doors = 3)|vgood (3.0/0.0)
(Safety = high) and (Buying = med) and (Maint = med) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Lug_boot = big) and (Maint = high) and (Persons = 4)|vgood (3.0/0.0)
(Safety = high) and (Buying = med) and (Maint = low) and (Lug_boot = big) and (Persons = 4)|vgood (4.0/0.0)
(Safety = high) and (Buying = low) and (Persons = more) and (Lug_boot = big) and (Maint = high)|vgood (3.0/0.0)
(Safety = high) and (Buying = low) and (Maint = low) and (Lug_boot = big) and (Persons = 4)|vgood (3.0/0.0)
(Safety = high) and (Persons = more) and (Buying = med) and (Maint = med) and (Lug_boot = big)|vgood (4.0/0.0)
(Safety = high) and (Lug_boot = med) and (Buying = low) and (Doors = 4) and (Persons = 4)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med) and (Doors = 5more)|vgood (2.0/0.0)
(Safety = high) and (Persons = more) and (Maint = low) and (Buying = med) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Lug_boot = med) and (Persons = more) and (Buying = low) and (Doors = 4)|vgood (4.0/1.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = low) and (Persons = more)|vgood (4.0/1.0)
(Safety = high) and (Buying = low) and (Doors = 5more) and (Lug_boot = med) and (Persons = 4)|vgood (4.0/1.0)
(Safety = high) and (Persons = more) and (Buying = low) and (Maint = low) and (Lug_boot = big)|vgood (3.0/0.0)
(Safety = high) and (Lug_boot = med) and (Buying = med) and (Maint = med) and (Doors = 4)|vgood (3.0/1.0)
(Buying = low) and (Maint = med) and (Persons = 4) and (Safety = high)|good (5.0/0.0)
(Maint = low) and (Buying = med) and (Persons = 4) and (Safety = high) and (Lug_boot = small)|good (4.0/0.0)
(Buying = low) and (Maint = low) and (Persons = 4) and (Safety = high)|good (6.0/0.0)
(Buying = low) and (Safety = med) and (Maint = med) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Safety = med) and (Buying = med) and (Lug_boot = big) and (Persons = more)|good (4.0/0.0)
(Buying = low) and (Persons = more) and (Maint = med) and (Safety = med) and (Lug_boot = big)|good (4.0/0.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Lug_boot = big) and (Persons = 4)|good (4.0/0.0)
(Maint = low) and (Buying = med) and (Safety = med) and (Persons = 4) and (Lug_boot = big)|good (3.0/0.0)
(Maint = low) and (Persons = more) and (Buying = low) and (Safety = high)|good (4.0/1.0)
(Maint = low) and (Buying = med) and (Lug_boot = med) and (Safety = med) and (Persons = more)|good (4.0/1.0)
(Buying = low) and (Persons = more) and (Maint = med) and (Safety = high) and (Lug_boot = small)|good (4.0/1.0)
(Maint = low) and (Buying = med) and (Safety = high) and (Persons = more)|good (3.0/1.0)
(Buying = low) and (Safety = med) and (Lug_boot = med) and (Maint = med) and (Persons = more)|good (4.0/1.0)
(Maint = low) and (Safety = med) and (Buying = low) and (Persons = more) and (Lug_boot = big)|good (2.0/0.0)
(Lug_boot = med) and (Maint = low) and (Persons = 4) and (Buying = med) and (Safety = med)|good (3.0/1.0)
(Lug_boot = med) and (Buying = low) and (Safety = med) and (Doors = 4) and (Maint = low)|good (3.0/1.0)
(Safety = high) and (Persons = 4) and (Maint = med)|acc (26.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = big)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = big)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = big) and (Maint = med)|acc (11.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = low)|acc (14.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Buying = med)|acc (11.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Lug_boot = med)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Doors = 4)|acc (5.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Lug_boot = big)|acc (8.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = high)|acc (12.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Buying = vhigh) and (Lug_boot = med)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Maint = vhigh) and (Lug_boot = big)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = low)|acc (6.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = low) and (Buying = high)|acc (11.0/0.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Lug_boot = big)|acc (7.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = big) and (Maint = low)|acc (8.0/0.0)
(Persons = more) and (Safety = high) and (Buying = high) and (Maint = high) and (Lug_boot = med)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Buying = med) and (Lug_boot = med) and (Maint = vhigh)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Buying = med) and (Maint = med)|acc (4.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Lug_boot = big)|acc (4.0/0.0)
(Persons = more) and (Safety = high) and (Maint = med) and (Buying = high) and (Lug_boot = med)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = high) and (Lug_boot = med)|acc (4.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = med) and (Maint = high)|acc (10.0/0.0)
(Safety = med) and (Persons = 4) and (Maint = med) and (Lug_boot = big)|acc (7.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 3) and (Maint = med)|acc (3.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 5more) and (Buying = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Buying = med) and (Doors = 3)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = low)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Maint = med) and (Doors = 3)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = med) and (Maint = med)|acc (6.0/0.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Maint = vhigh) and (Doors = 5more)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Maint = low) and (Doors = 3)|acc (2.0/0.0)
(Persons = more) and (Safety = med) and (Lug_boot = med) and (Doors = 5more) and (Buying = med)|acc (2.0/0.0)
(Persons = 4) and (Safety = high) and (Maint = low) and (Buying = vhigh)|acc (10.0/0.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = high) and (Lug_boot = big)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = high)|acc (4.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = low) and (Lug_boot = small)|acc (4.0/0.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Doors = 4) and (Lug_boot = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Doors = 4) and (Lug_boot = med)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 5more) and (Buying = med)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 4) and (Buying = low)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Maint = low) and (Lug_boot = big)|acc (4.0/0.0)
(Persons = 4) and (Safety = high) and (Buying = med) and (Maint = vhigh)|acc (9.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4) and (Buying = med)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 5more) and (Maint = med)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Maint = med) and (Doors = 3)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Doors = 4) and (Maint = med)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Maint = med) and (Doors = 5more) and (Lug_boot = med)|acc (2.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 5more) and (Maint = med)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = med) and (Lug_boot = med)|acc (3.0/0.0)
(Safety = med) and (Persons = more) and (Buying = low) and (Maint = med)|acc (4.0/1.0)
(Safety = med) and (Persons = 4) and (Maint = low) and (Buying = med)|acc (3.0/0.0)
(Persons = more) and (Safety = high) and (Lug_boot = small) and (Maint = low) and (Doors = 4)|acc (2.0/0.0)
(Safety = med) and (Persons = more) and (Buying = med) and (Maint = med)|acc (4.0/1.0)
(Maint = high) and (Buying = high) and (Persons = 4) and (Safety = high)|acc (9.0/0.0)
(Safety = med) and (Persons = 4) and (Lug_boot = med) and (Doors = 4)|acc (9.0/4.0)
(Persons = more) and (Safety = high) and (Buying = low) and (Doors = 3)|acc (2.0/0.0)
(Persons = more) and (Safety = high) and (Maint = high) and (Buying = high)|acc (4.0/1.0)
(Safety = med) and (Persons = more) and (Lug_boot = med) and (Buying = low)|acc (4.0/1.0)
(Safety = med) and (Persons = 4) and (Buying = low) and (Lug_boot = med)|acc (5.0/2.0)
(Safety = med) and (Buying = high) and (Maint = high) and (Lug_boot = big) and (Persons = 4)|acc (4.0/0.0)
(Persons = more) and (Safety = med) and (Maint = high) and (Buying = high) and (Lug_boot = big)|acc (3.0/0.0)
|unacc (1100.0/25.0)


## PART

Decision list:

rules | predicted class
---|---
Persons = 2|unacc (523.0)
Safety = low|unacc (343.0)
Buying = vhigh AND Maint = vhigh|unacc (48.0)
Buying != low AND Buying != med AND Maint != vhigh AND Lug_boot != small AND Maint != high AND Safety != med|acc (59.0)
Buying = vhigh AND Maint = high|unacc (43.0)
Buying = high AND Maint = vhigh|unacc (41.0)
Safety = med AND Lug_boot = small AND Buying = high|unacc (22.0)
Safety = med AND Lug_boot = small AND Buying != vhigh AND Maint != vhigh AND Doors != 2 AND Maint != high|acc (20.0)
Safety = med AND Lug_boot = small AND Maint != high AND Doors != 2|unacc (20.0)
Safety = med AND Lug_boot = small AND Buying != low AND Persons != 4|unacc (7.0)
Safety = med AND Lug_boot = big AND Maint != low AND Buying != low|acc (43.0)
Maint = vhigh AND Doors != 2|acc (50.0/2.0)
Buying = high AND Doors != 2 AND Doors != 3|acc (30.0)
Safety = med AND Lug_boot = big AND Maint != high AND Buying != vhigh AND Buying != high AND Maint != vhigh|good (21.0)
Lug_boot = big AND Safety != med AND Buying != high AND Maint != vhigh AND Maint != high|vgood (29.0)
Doors = 2 AND Lug_boot = big|acc (14.0/1.0)
Doors = 2 AND Safety = med AND Buying != vhigh AND Buying != high AND Maint != vhigh AND Maint != high|acc (12.0/1.0)
Doors = 2 AND Safety = med AND Buying != low|unacc (15.0)
Doors = 2 AND Persons = 4 AND Maint != low|acc (16.0/2.0)
Doors = 2 AND Persons = 4 AND Buying = med|good (2.0)
Doors = 2 AND Lug_boot = small AND Persons != 4|unacc (15.0)
Safety = med AND Maint = high|acc (28.0/3.0)
Buying != low AND Buying != med AND Lug_boot != med|acc (27.0)
Maint = high AND Buying != low|acc (21.0)
Safety = med AND Buying = vhigh AND Doors != 3|acc (7.0)
Safety = med AND Doors != 3 AND Maint = low|good (7.0)
Safety = med AND Buying != low AND Persons != 4|acc (8.0/1.0)
Safety != med AND Lug_boot = small AND Maint != high AND Buying != med|good (13.0)
Safety != med AND Lug_boot = small AND Maint != low|acc (10.0)
Safety != med AND Lug_boot != small AND Doors != 2 AND Doors != 3|vgood (23.0)
Safety != med AND Lug_boot = small|good (5.0)
Safety = med AND Buying != med AND Buying = low AND Maint = med|good (5.0/1.0)
Safety = med AND Buying != med|unacc (6.0/1.0)
Maint = low|good (6.0/2.0)
Doors != 3|acc (6.0/1.0)
Persons = 4|acc (4.0/1.0)
|vgood (4.0)


## SimpleCart Decision Tree

	* Persons=(more)|(4)
		* Safety=(high)|(med)
			* Buying=(low)|(med)
				* Maint=(low)|(med)
					* Safety=(high)|(low)
						* Lug_boot=(big)|(med)
							* Doors=(5more)|(4): vgood(29.0/0.0)
							* Doors!=(5more)|(4)
								* Lug_boot=(big)|(small): vgood(15.0/0.0)
								* Lug_boot!=(big)|(small)
									* Persons=(more)|(2)
											* Doors=(3)|(4)|(5more): vgood(4.0/0.0)
											* Doors!=(3)|(4)|(5more): good(2.0/1.0)
									* Persons!=(more)|(2)
											* Buying=(low)|(vhigh)|(high): good(4.0/0.0)
											* Buying!=(low)|(vhigh)|(high): good(2.0/1.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3)
									* Buying=(low)|(vhigh)|(high): good(12.0/0.0)
									* Buying!=(low)|(vhigh)|(high)
										* Maint=(low)|(vhigh)|(high): good(5.0/0.0)
										* Maint!=(low)|(vhigh)|(high): acc(5.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): good(2.0/1.0)
					* Safety!=(high)|(low)
						* Lug_boot=(big)|(med)
						* Buying=(low)
								* Lug_boot=(big)|(small): good(14.0/0.0)
								* Lug_boot!=(big)|(small)
									* Doors=(5more)|(4): good(6.0/0.0)
									* Doors!=(5more)|(4)
											* Maint=(low)|(vhigh)|(high): acc(3.0/0.0)
											* Maint!=(low)|(vhigh)|(high): acc(2.0/1.0)
						* Buying!=(low)
									* Maint=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): good(10.0/0.0)
										* Doors!=(5more)|(4)|(3)
										* Lug_boot=(big)|(small): good(2.0/0.0)
										* Lug_boot!=(big)|(small): acc(2.0/0.0)
									* Maint!=(low)|(vhigh)|(high): acc(14.0/0.0)
						* Lug_boot!=(big)|(med)
								* Doors=(5more)|(4)|(3): acc(20.0/0.0)
								* Doors!=(5more)|(4)|(3)
							* Persons=(more): unacc(3.0/0.0)
							* Persons!=(more): acc(4.0/0.0)
				* Maint!=(low)|(med)
					* Lug_boot=(big)|(med)
					* Safety=(high)
						* Buying=(low)
									* Maint=(high)|(med)|(low)
									* Doors=(5more)|(4): vgood(8.0/0.0)
									* Doors!=(5more)|(4)
									* Lug_boot=(big): vgood(2.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): acc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): acc(2.0/0.0)
									* Maint!=(high)|(med)|(low): acc(14.0/0.0)
						* Buying!=(low): acc(30.0/0.0)
					* Safety!=(high)
							* Doors=(5more)|(4): acc(32.0/0.0)
							* Doors!=(5more)|(4)
							* Lug_boot=(big): acc(14.0/0.0)
							* Lug_boot!=(big)
								* Buying=(low)
											* Maint=(high)|(med)|(low): acc(4.0/0.0)
											* Maint!=(high)|(med)|(low): unacc(2.0/1.0)
								* Buying!=(low)
											* Doors=(3)|(4)|(5more)
											* Persons=(more)|(2): acc(2.0/0.0)
											* Persons!=(more)|(2): unacc(2.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(4.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(19.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low)
								* Maint=(high)|(med)|(low)
									* Buying=(low)|(vhigh)|(high)
										* Doors=(5more)|(4)|(3): acc(6.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
									* Buying!=(low)|(vhigh)|(high): unacc(4.0/0.0)
								* Maint!=(high)|(med)|(low): unacc(12.0/0.0)
			* Buying!=(low)|(med)
				* Maint=(low)|(med)
					* Lug_boot=(big)|(med)
						* Safety=(high)|(low): acc(59.0/0.0)
						* Safety!=(high)|(low)
						* Lug_boot=(big): acc(27.0/0.0)
						* Lug_boot!=(big)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
								* Persons=(more)
											* Doors=(3)|(4)|(5more): acc(4.0/0.0)
											* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
								* Persons!=(more): unacc(8.0/0.0)
					* Lug_boot!=(big)|(med)
						* Safety=(high)|(low)
								* Doors=(5more)|(4)|(3): acc(22.0/0.0)
								* Doors!=(5more)|(4)|(3)
								* Persons=(more)|(2): unacc(4.0/0.0)
								* Persons!=(more)|(2): acc(4.0/0.0)
						* Safety!=(high)|(low): unacc(29.0/0.0)
				* Maint!=(low)|(med)
				* Buying=(high)
							* Maint=(high)|(med)|(low)
							* Lug_boot=(big)|(med)
								* Doors=(5more)|(4): acc(14.0/0.0)
								* Doors!=(5more)|(4)
									* Safety=(high)|(low): acc(8.0/0.0)
									* Safety!=(high)|(low)
									* Lug_boot=(big): acc(3.0/0.0)
									* Lug_boot!=(big)
												* Doors=(3)|(4)|(5more): unacc(1.0/1.0)
												* Doors!=(3)|(4)|(5more): unacc(2.0/0.0)
							* Lug_boot!=(big)|(med)
							* Safety=(high)
										* Doors=(5more)|(4)|(3): acc(5.0/0.0)
										* Doors!=(5more)|(4)|(3): unacc(1.0/1.0)
							* Safety!=(high): unacc(8.0/0.0)
							* Maint!=(high)|(med)|(low): unacc(41.0/0.0)
				* Buying!=(high): unacc(91.0/0.0)
		* Safety!=(high)|(med): unacc(343.0/0.0)
	* Persons!=(more)|(4): unacc(523.0/0.0)


