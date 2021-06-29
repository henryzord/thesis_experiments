# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.75896 and curtosis > -1.8785 | 0 | 0.403261 |
| skewness <= 5.1401 and variance <= -1.786 | 1 | 0.434242 |
| skewness > 5.2022 and variance > -3.4605 | 0 | 0.454707 |
| curtosis <= 0.7126 and variance <= 1.581 | 1 | 0.785978 |
| skewness <= -0.94981 and variance <= -0.46651 | 1 | 0.536000 |
| curtosis > 2.1624 | 0 | 0.609025 |
| variance > 0.32444 and curtosis > -2.1835 | 0 | 0.314103 |
|  | 1 | 0.964286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.1401 and curtosis <= 6.7019 | 1 | 0.326477 |
| variance <= -1.3968 and skewness <= -4.9932 | 1 | 0.136192 |
| variance <= 1.7875 and skewness <= 5.2022 and curtosis <= 0.18307 | 1 | 0.084225 |
| variance <= -4.1479 | 1 | 0.048649 |
|  | 0 | 0.989884 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.1401) and (curtosis <= 6.7019)|1 (338.0/3.0)
(variance <= -1.3968) and (skewness <= -4.9932)|1 (108.0/0.0)
(variance <= 1.7875) and (skewness <= 5.2022) and (curtosis <= 0.18307)|1 (63.0/0.0)
(variance <= -4.1479)|1 (37.0/1.0)
|0 (688.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.75896 AND curtosis > -1.8785|0 (371.0)
skewness <= 5.1401 AND variance <= -1.786|1 (243.0/1.0)
skewness > 5.2022 AND variance > -3.4605|0 (256.0)
curtosis <= 0.7126 AND variance <= 1.581|1 (213.0)
skewness <= -0.94981 AND variance <= -0.46651|1 (67.0)
curtosis > 2.1624|0 (43.0/1.0)
variance > 0.32444 AND curtosis > -2.1835|0 (16.0/2.0)
|1 (25.0/1.0)


