# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.642458 |
| plas > 103.5 and plas <= 129.5 and skin <= 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.044718 |
| plas > 129.5 and plas <= 166 and skin > 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.042477 |
| plas > 166 and skin <= 31.5 and mass > 26.45 and age <= 28.5 | 1 | 0.011461 |
| plas > 103.5 and plas <= 129.5 and skin > 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.018863 |
| plas > 166 and skin <= 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.044875 |
| plas > 166 and skin > 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.031648 |
| plas > 129.5 and plas <= 166 and skin <= 31.5 and mass > 26.45 and age > 28.5 | 1 | 0.061394 |
| plas > 166 and skin > 31.5 and mass > 26.45 and age <= 28.5 | 1 | 0.028169 |
| plas > 166 and skin <= 31.5 and mass <= 26.45 and age > 28.5 | 1 | 0.009195 |

## Ordered rules

# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

plas|skin|mass|age|target
---|---|---|---|---
(-inf-103.5]|(31.5-inf)|(26.45-inf)|(28.5-inf)|0
(166-inf)|(31.5-inf)|(26.45-inf)|(28.5-inf)|1
(103.5-129.5]|(31.5-inf)|(26.45-inf)|(28.5-inf)|1
(129.5-166]|(31.5-inf)|(26.45-inf)|(28.5-inf)|1
(166-inf)|(-inf-31.5]|(26.45-inf)|(28.5-inf)|1
(103.5-129.5]|(-inf-31.5]|(26.45-inf)|(28.5-inf)|1
(129.5-166]|(-inf-31.5]|(26.45-inf)|(28.5-inf)|1
(-inf-103.5]|(-inf-31.5]|(26.45-inf)|(28.5-inf)|0
(129.5-166]|(31.5-inf)|(-inf-26.45]|(28.5-inf)|0
(166-inf)|(31.5-inf)|(-inf-26.45]|(28.5-inf)|0
(103.5-129.5]|(31.5-inf)|(-inf-26.45]|(28.5-inf)|0
(-inf-103.5]|(31.5-inf)|(-inf-26.45]|(28.5-inf)|0
(129.5-166]|(-inf-31.5]|(-inf-26.45]|(28.5-inf)|0
(166-inf)|(-inf-31.5]|(-inf-26.45]|(28.5-inf)|1
(166-inf)|(31.5-inf)|(26.45-inf)|(-inf-28.5]|1
(-inf-103.5]|(-inf-31.5]|(-inf-26.45]|(28.5-inf)|0
(129.5-166]|(31.5-inf)|(26.45-inf)|(-inf-28.5]|0
(103.5-129.5]|(31.5-inf)|(26.45-inf)|(-inf-28.5]|0
(-inf-103.5]|(31.5-inf)|(26.45-inf)|(-inf-28.5]|0
(103.5-129.5]|(-inf-31.5]|(-inf-26.45]|(28.5-inf)|0
(166-inf)|(-inf-31.5]|(26.45-inf)|(-inf-28.5]|1
(103.5-129.5]|(-inf-31.5]|(26.45-inf)|(-inf-28.5]|0
(129.5-166]|(-inf-31.5]|(26.45-inf)|(-inf-28.5]|0
(-inf-103.5]|(-inf-31.5]|(26.45-inf)|(-inf-28.5]|0
(-inf-103.5]|(31.5-inf)|(-inf-26.45]|(-inf-28.5]|0
(166-inf)|(-inf-31.5]|(-inf-26.45]|(-inf-28.5]|0
(129.5-166]|(-inf-31.5]|(-inf-26.45]|(-inf-28.5]|0
(103.5-129.5]|(-inf-31.5]|(-inf-26.45]|(-inf-28.5]|0
(-inf-103.5]|(-inf-31.5]|(-inf-26.45]|(-inf-28.5]|0

