# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.935345 |
| seismoacoustic = a and shift = W and genergy > 31245 and gpuls > 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy <= 550 and maxenergy > 350 | 1 | 0.000230 |
| seismoacoustic = c and shift = W and genergy > 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = b and nbumps > 1.5 and nbumps2 <= 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000461 |
| seismoacoustic = a and shift = N and genergy <= 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy <= 550 and maxenergy <= 350 | 1 | 0.000461 |
| seismoacoustic = b and shift = W and genergy <= 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = b and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000154 |
| seismoacoustic = b and shift = W and genergy > 31245 and gpuls > 1253.5 and gdenergy = all and gdpuls = all and ghazard = b and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 > 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000614 |
| seismoacoustic = a and shift = W and genergy > 31245 and gpuls > 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.001506 |
| seismoacoustic = c and shift = W and genergy > 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = b and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000461 |
| seismoacoustic = c and shift = W and genergy > 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000461 |
| seismoacoustic = a and shift = N and genergy > 31245 and gpuls <= 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 1.5 and nbumps2 > 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000230 |
| seismoacoustic = b and shift = W and genergy > 31245 and gpuls > 1253.5 and gdenergy = all and gdpuls = all and ghazard = a and nbumps > 0.5 and nbumps <= 1.5 and nbumps2 <= 0.5 and nbumps4 <= 0.5 and nbumps5 = all and nbumps6 = all and nbumps7 = all and nbumps89 = all and energy > 550 and maxenergy > 350 | 1 | 0.000829 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1.5 and gpuls <= 1342.5 | 0 | 0.919026 |
| ghazard = a and shift = W and seismic = a | 0 | 0.557604 |
| shift = W and nbumps4 > 0.5 and nbumps2 <= 0.5 | 0 | 0.162688 |
| seismic = b and genergy <= 117615 and nbumps3 <= 1.5 | 0 | 0.254836 |
| seismic = a | 0 | 0.085536 |
| ghazard = a and nbumps3 > 1.5 and nbumps2 <= 3.5 and nbumps4 > 0.5 | 0 | 0.089800 |
| ghazard = a and seismoacoustic = b and genergy > 41045 | 0 | 0.072466 |
| seismoacoustic = a and genergy > 38175 and nbumps4 <= 0.5 and gdpuls > 22.5 | 0 | 0.037422 |
| seismoacoustic = a and genergy > 38175 and nbumps4 <= 0.5 and gdenergy > -10.5 | 1 | 0.500408 |
| seismoacoustic = a and genergy > 83990 and gpuls <= 1868 | 1 | 0.352667 |
| seismoacoustic = a | 0 | 0.167626 |
|  | 1 | 0.968421 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps >= 2 and gdenergy <= -5 and gpuls >= 362 and nbumps4 <= 0 | 1 | 0.005388 |
|  | 0 | 0.948012 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

seismoacoustic|shift|genergy|gpuls|gdenergy|gdpuls|ghazard|nbumps|nbumps2|nbumps4|nbumps5|nbumps6|nbumps7|nbumps89|energy|maxenergy|class
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|c|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(31245-inf)|(1253.5-inf)|all|all|b|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
b|n|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|n|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
c|w|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(0.5-inf)|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
c|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(-inf-350]|1
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(550-inf)|(-inf-350]|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(550-inf)|(350-inf)|0
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(350-inf)|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(1.5-inf)|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(-inf-31245]|(1253.5-inf)|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(31245-inf)|(1253.5-inf)|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(0.5-inf)|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
c|w|(31245-inf)|(-inf-1253.5]|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(-inf-31245]|(-inf-1253.5]|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
c|w|(-inf-31245]|(-inf-1253.5]|all|all|c|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(1253.5-inf)|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|n|(31245-inf)|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(31245-inf)|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(0.5-1.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
a|w|(31245-inf)|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
c|w|(31245-inf)|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|n|(-inf-31245]|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
c|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
a|n|(31245-inf)|(1253.5-inf)|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|w|(-inf-31245]|(-inf-1253.5]|all|all|b|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(1253.5-inf)|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(31245-inf)|(1253.5-inf)|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(-inf-31245]|(1253.5-inf)|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(31245-inf)|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(31245-inf)|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(31245-inf)|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(31245-inf)|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
c|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|1
b|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|n|(-inf-31245]|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
a|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0
b|w|(-inf-31245]|(-inf-1253.5]|all|all|a|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|all|all|all|all|(-inf-550]|(-inf-350]|0

## JRip

Decision list:

rules | predicted class
---|---
(nbumps >= 2) and (gdenergy <= -5) and (gpuls >= 362) and (nbumps4 <= 0)|1 (83.0/52.0)
|0 (2237.0/119.0)


## PART

Decision list:

rules | predicted class
---|---
nbumps <= 1.5 AND gpuls <= 1342.5|0 (1777.0/44.0)
ghazard = a AND shift = W AND seismic = a|0 (264.0/44.0)
shift = W AND nbumps4 > 0.5 AND nbumps2 <= 0.5|0 (33.0/2.0)
seismic = b AND genergy <= 117615 AND nbumps3 <= 1.5|0 (76.0/8.0)
seismic = a|0 (35.0/4.0)
ghazard = a AND nbumps3 > 1.5 AND nbumps2 <= 3.5 AND nbumps4 > 0.5|0 (21.0/3.0)
ghazard = a AND seismoacoustic = b AND genergy > 41045|0 (30.0/7.0)
seismoacoustic = a AND genergy > 38175 AND nbumps4 <= 0.5 AND gdpuls > 22.5|0 (15.0/3.0)
seismoacoustic = a AND genergy > 38175 AND nbumps4 <= 0.5 AND gdenergy > -10.5|1 (13.0/1.0)
seismoacoustic = a AND genergy > 83990 AND gpuls <= 1868|1 (18.0/6.0)
seismoacoustic = a|0 (26.0/2.0)
|1 (12.0/3.0)


## J48 Decision Tree

* : 0 (2320.0/150.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


