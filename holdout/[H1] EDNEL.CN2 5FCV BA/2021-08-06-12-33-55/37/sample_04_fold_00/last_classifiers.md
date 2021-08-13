# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.633147 |
| plas > 154.5 and skin = all and mass <= 26.35 and age > 28.5 | 1 | 0.020493 |
| plas > 154.5 and skin = all and mass > 26.35 and age > 28.5 | 1 | 0.102128 |
| plas > 123.5 and plas <= 154.5 and skin = all and mass > 26.35 and age > 28.5 | 1 | 0.082043 |
| plas > 154.5 and skin = all and mass > 26.35 and age <= 28.5 | 1 | 0.041602 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 123 and mass > 26.4 and age <= 30 | 0 | 0.331060 |
| mass <= 26.3 and plas <= 156 | 0 | 0.334591 |
| plas > 106 and plas > 165 | 1 | 0.270677 |
| plas <= 106 | 0 | 0.161635 |
| preg > 7 | 1 | 0.237877 |
| pres > 80 and age <= 28 | 0 | 0.096970 |
|  | 1 | 0.614525 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

plas|skin|mass|age|target
---|---|---|---|---
(-inf-99.5]|all|(26.35-inf)|(28.5-inf)|0
(99.5-123.5]|all|(26.35-inf)|(28.5-inf)|0
(123.5-154.5]|all|(26.35-inf)|(28.5-inf)|1
(154.5-inf)|all|(26.35-inf)|(28.5-inf)|1
(123.5-154.5]|all|(-inf-26.35]|(28.5-inf)|0
(99.5-123.5]|all|(-inf-26.35]|(28.5-inf)|0
(-inf-99.5]|all|(-inf-26.35]|(28.5-inf)|0
(154.5-inf)|all|(-inf-26.35]|(28.5-inf)|1
(-inf-99.5]|all|(26.35-inf)|(-inf-28.5]|0
(123.5-154.5]|all|(26.35-inf)|(-inf-28.5]|0
(99.5-123.5]|all|(26.35-inf)|(-inf-28.5]|0
(154.5-inf)|all|(26.35-inf)|(-inf-28.5]|1
(154.5-inf)|all|(-inf-26.35]|(-inf-28.5]|0
(-inf-99.5]|all|(-inf-26.35]|(-inf-28.5]|0
(123.5-154.5]|all|(-inf-26.35]|(-inf-28.5]|0
(99.5-123.5]|all|(-inf-26.35]|(-inf-28.5]|0

## PART

Decision list:

rules | predicted class
---|---
plas <= 123 AND mass > 26.4 AND age <= 30|0 (133.0/20.0)
mass <= 26.3 AND plas <= 156|0 (103.0/2.0)
plas > 106 AND plas > 165|1 (63.0/9.0)
plas <= 106|0 (55.0/14.0)
preg > 7|1 (33.0/7.0)
pres > 80 AND age <= 28|0 (18.0/2.0)
|1 (132.0/53.0)


