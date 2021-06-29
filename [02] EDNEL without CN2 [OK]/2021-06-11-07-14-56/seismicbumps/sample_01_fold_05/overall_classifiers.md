# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1333 | 0 | 0.918771 |
| ghazard = a and nbumps <= 5 and seismic = a | 0 | 0.562900 |
| genergy <= 91210 | 0 | 0.411947 |
| nbumps4 > 0 | 0 | 0.173851 |
| seismoacoustic = b and maxenergy <= 1000 | 0 | 0.015293 |
| seismoacoustic = b and energy <= 6300 | 1 | 0.545552 |
| seismoacoustic = a and gpuls <= 1690 | 1 | 0.685850 |
| energy > 2500 | 0 | 0.349138 |
|  | 1 | 0.909091 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
=> class=0 (2320.0/150.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1 AND gpuls <= 1333|0 (1778.0/49.0)
ghazard = a AND nbumps <= 5 AND seismic = a|0 (264.0/39.0)
genergy <= 91210|0 (154.0/21.0)
nbumps4 > 0|0 (57.0/13.0)
seismoacoustic = b AND maxenergy <= 1000|0 (8.0)
seismoacoustic = b AND energy <= 6300|1 (8.0/2.0)
seismoacoustic = a AND gpuls <= 1690|1 (18.0/4.0)
energy > 2500|0 (25.0/3.0)
|1 (8.0/3.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


