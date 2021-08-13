# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.192793 |
| Ethnic = 2 | 5 | 0.042571 |
| Ethnic = 1 | 1 | 0.035138 |
| Ethnic = 0 | 2 | 0.008718 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Ethnic = 1 and DMFT.End != 4 and DMFT.Begin != 8 and DMFT.Begin != 7 and DMFT.End != 5 and DMFT.End != 3 and DMFT.Begin != 5 and DMFT.End != 2 | 0 | 0.015176 |
| Ethnic = 1 and DMFT.Begin != 7 and DMFT.Begin != 2 and DMFT.End != 5 and DMFT.End != 4 and DMFT.End != 3 | 4 | 0.014551 |
| Ethnic = 1 | 1 | 0.045266 |
| DMFT.End = 0 and Gender != 0 and DMFT.Begin = 0 | 3 | 0.015894 |
| DMFT.Begin = 4 and DMFT.End = 3 | 2 | 0.007066 |
| DMFT.End = 4 and DMFT.Begin != 5 | 0 | 0.007319 |
| DMFT.End != 4 and DMFT.Begin != 8 and DMFT.Begin = 1 and DMFT.End != 2 | 5 | 0.011599 |
| DMFT.Begin != 1 and DMFT.End != 4 and DMFT.Begin != 8 and Ethnic = 0 | 2 | 0.010547 |
| DMFT.Begin != 1 and DMFT.End != 4 and DMFT.Begin != 5 and DMFT.Begin != 8 and DMFT.Begin != 3 and DMFT.End != 3 and Gender != 0 and DMFT.End != 5 | 5 | 0.044053 |
| DMFT.Begin != 1 and DMFT.End != 4 and Gender != 0 | 4 | 0.039112 |
| DMFT.Begin != 1 and DMFT.End != 4 and DMFT.Begin != 8 and DMFT.Begin != 7 and DMFT.End != 3 and DMFT.Begin != 3 and DMFT.End != 2 and DMFT.Begin = 0 | 3 | 0.010717 |
| DMFT.Begin != 1 and DMFT.End != 4 and DMFT.End != 0 and DMFT.End = 1 | 3 | 0.014762 |
| DMFT.End != 0 and DMFT.Begin != 1 and DMFT.End != 4 and DMFT.Begin != 7 and DMFT.End = 2 | 5 | 0.004091 |
| DMFT.End != 0 | 1 | 0.076281 |
|  | 0 | 0.215385 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

ethnic|target
---|---
0|2
1|1
2|5

## PART

Decision list:

rules | predicted class
---|---
Ethnic = 1 AND DMFT.End != 4 AND DMFT.Begin != 8 AND DMFT.Begin != 7 AND DMFT.End != 5 AND DMFT.End != 3 AND DMFT.Begin != 5 AND DMFT.End != 2|0 (91.0/68.0)
Ethnic = 1 AND DMFT.Begin != 7 AND DMFT.Begin != 2 AND DMFT.End != 5 AND DMFT.End != 4 AND DMFT.End != 3|4 (37.0/28.0)
Ethnic = 1|1 (72.0/53.0)
DMFT.End = 0 AND Gender != 0 AND DMFT.Begin = 0|3 (20.0/13.0)
DMFT.Begin = 4 AND DMFT.End = 3|2 (12.0/6.0)
DMFT.End = 4 AND DMFT.Begin != 5|0 (20.0/14.0)
DMFT.End != 4 AND DMFT.Begin != 8 AND DMFT.Begin = 1 AND DMFT.End != 2|5 (22.0/15.0)
DMFT.Begin != 1 AND DMFT.End != 4 AND DMFT.Begin != 8 AND Ethnic = 0|2 (39.0/28.0)
DMFT.Begin != 1 AND DMFT.End != 4 AND DMFT.Begin != 5 AND DMFT.Begin != 8 AND DMFT.Begin != 3 AND DMFT.End != 3 AND Gender != 0 AND DMFT.End != 5|5 (29.0/11.0)
DMFT.Begin != 1 AND DMFT.End != 4 AND Gender != 0|4 (48.0/36.0)
DMFT.Begin != 1 AND DMFT.End != 4 AND DMFT.Begin != 8 AND DMFT.Begin != 7 AND DMFT.End != 3 AND DMFT.Begin != 3 AND DMFT.End != 2 AND DMFT.Begin = 0|3 (24.0/18.0)
DMFT.Begin != 1 AND DMFT.End != 4 AND DMFT.End != 0 AND DMFT.End = 1|3 (16.0/11.0)
DMFT.End != 0 AND DMFT.Begin != 1 AND DMFT.End != 4 AND DMFT.Begin != 7 AND DMFT.End = 2|5 (16.0/11.0)
DMFT.End != 0|1 (41.0/31.0)
|0 (13.0/7.0)


## SimpleCart Decision Tree

* : 3(107.0/448.0)


