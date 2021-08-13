# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| plas <= 129 | 0 | 0.581675 |
| plas >= 127.5 | 1 | 0.177405 |
| plas > 129 and mass <= 29.9 | 0 | 0.122500 |
| plas > 127.5 and plas <= 166.5 and mass > 27.85 and age <= 24.5 | 0 | 0.043501 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| mass >= 30 and plas >= 156 and pedi >= 0.345 | 1 | 0.085271 |
| plas >= 128 and age >= 29 and mass >= 35.2 and pedi <= 0.278 | 1 | 0.030137 |
| plas >= 113 and mass >= 30 and skin <= 0 and mass <= 32.9 and preg <= 9 and age >= 22 | 1 | 0.040650 |
| plas >= 128 and mass >= 33.3 and pedi >= 0.314 and age >= 31 and insu <= 325 and pedi <= 1.353 | 1 | 0.053476 |
| plas >= 107 and age >= 25 and pedi >= 0.319 and pedi <= 0.38 and age <= 33 | 1 | 0.027473 |
| age <= 55 and preg >= 8 and plas >= 143 and pedi >= 0.212 | 1 | 0.022099 |
| plas >= 107 and mass >= 42.1 | 1 | 0.016994 |
| plas >= 100 and age >= 25 and pedi >= 0.403 and mass >= 29.9 and pres <= 74 | 1 | 0.029658 |
|  | 0 | 0.869779 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

plas|mass|age|target
---|---|---|---
(166.5-inf)|(27.85-inf)|(24.5-inf)|1
(127.5-166.5]|(27.85-inf)|(24.5-inf)|1
(-inf-99.5]|(27.85-inf)|(24.5-inf)|0
(99.5-127.5]|(27.85-inf)|(24.5-inf)|0
(166.5-inf)|(-inf-27.85]|(24.5-inf)|1
(-inf-99.5]|(-inf-27.85]|(24.5-inf)|0
(99.5-127.5]|(-inf-27.85]|(24.5-inf)|0
(127.5-166.5]|(-inf-27.85]|(24.5-inf)|0
(166.5-inf)|(27.85-inf)|(-inf-24.5]|1
(127.5-166.5]|(27.85-inf)|(-inf-24.5]|0
(99.5-127.5]|(27.85-inf)|(-inf-24.5]|0
(-inf-99.5]|(27.85-inf)|(-inf-24.5]|0
(166.5-inf)|(-inf-27.85]|(-inf-24.5]|0
(127.5-166.5]|(-inf-27.85]|(-inf-24.5]|0
(99.5-127.5]|(-inf-27.85]|(-inf-24.5]|0
(-inf-99.5]|(-inf-27.85]|(-inf-24.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(mass >= 30) and (plas >= 156) and (pedi >= 0.345)|1 (33.0/0.0)
(plas >= 128) and (age >= 29) and (mass >= 35.2) and (pedi <= 0.278)|1 (11.0/0.0)
(plas >= 113) and (mass >= 30) and (skin <= 0) and (mass <= 32.9) and (preg <= 9) and (age >= 22)|1 (15.0/0.0)
(plas >= 128) and (mass >= 33.3) and (pedi >= 0.314) and (age >= 31) and (insu <= 325) and (pedi <= 1.353)|1 (20.0/0.0)
(plas >= 107) and (age >= 25) and (pedi >= 0.319) and (pedi <= 0.38) and (age <= 33)|1 (10.0/0.0)
(age <= 55) and (preg >= 8) and (plas >= 143) and (pedi >= 0.212)|1 (8.0/0.0)
(plas >= 107) and (mass >= 42.1)|1 (20.0/9.0)
(plas >= 100) and (age >= 25) and (pedi >= 0.403) and (mass >= 29.9) and (pres <= 74)|1 (32.0/13.0)
|0 (385.0/53.0)


## J48 Decision Tree

* plas <= 129: 0 (240.0/48.0)
* plas > 129
	* mass <= 29.9: 0 (30.0/10.0)
	* mass > 29.9: 1 (86.0/24.0)


## SimpleCart Decision Tree

* plas < 127.5: 0(277.0/64.0)
* plas >= 127.5: 1(116.0/77.0)


