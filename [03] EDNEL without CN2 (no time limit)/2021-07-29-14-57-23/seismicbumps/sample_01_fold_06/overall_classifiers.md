# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 | 0 | 0.918683 |
| ghazard = a and seismic = a | 0 | 0.584071 |
| genergy <= 82760 and seismoacoustic = a | 0 | 0.205140 |
| seismoacoustic = b | 0 | 0.292431 |
| ghazard = a and nbumps4 > 0.5 and nbumps2 <= 0.5 | 0 | 0.081198 |
|  | 0 | 0.202128 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

gpuls|nbumps|nbumps2|class
---|---|---|---
(-inf-54.5]|(1.5-inf)|(0.5-inf)|0
(1142.5-inf)|(1.5-inf)|(0.5-inf)|0
(54.5-1142.5]|(1.5-inf)|(0.5-inf)|0
(-inf-54.5]|(-inf-1.5]|(0.5-inf)|0
(1142.5-inf)|(-inf-1.5]|(0.5-inf)|0
(54.5-1142.5]|(-inf-1.5]|(0.5-inf)|0
(1142.5-inf)|(1.5-inf)|(-inf-0.5]|0
(54.5-1142.5]|(1.5-inf)|(-inf-0.5]|0
(-inf-54.5]|(-inf-1.5]|(-inf-0.5]|0
(1142.5-inf)|(-inf-1.5]|(-inf-0.5]|0
(54.5-1142.5]|(-inf-1.5]|(-inf-0.5]|0

## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5|0 (1596.0/42.0)
ghazard = a AND seismic = a|0 (258.0/39.0)
genergy <= 82760 AND seismoacoustic = a|0 (63.0/5.0)
seismoacoustic = b|0 (100.0/22.0)
ghazard = a AND nbumps4 > 0.5 AND nbumps2 <= 0.5|0 (12.0)
|0 (59.0/27.0)


## J48 Decision Tree

* : 0 (1547.0/100.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


