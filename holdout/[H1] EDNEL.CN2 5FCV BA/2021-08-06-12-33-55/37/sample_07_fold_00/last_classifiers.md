# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas >= 128 and mass >= 30.3 | 1 | 0.193922 |
| age >= 29 and insu >= 127 | 1 | 0.026525 |
|  | 0 | 0.852941 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(plas >= 128) and (mass >= 30.3)|1 (152.0/41.0)
(age >= 29) and (insu >= 127)|1 (27.0/9.0)
|0 (358.0/60.0)


