# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 < 112.8 and Concave_points3 < 0.135 | B | 0.603022 |
| Perimeter3 > 106.1 and Texture1 > 15.745 | M | 0.327592 |
| Perimeter3 < 112.8 and Concave_points3 >= 0.135 and Texture1 < 20.299999999999997 | B | 0.061998 |
| Perimeter3 <= 106.1 and Concave_points3 > 0.1455 | M | 0.019231 |
| Perimeter3 >= 112.8 | M | 0.325202 |
| Concave_points1 > 0.0265 and Concave_points1 <= 0.0515 and Perimeter3 > 101.65 and Perimeter3 <= 117.45 | B | 0.100118 |
| Perimeter3 < 112.8 and Concave_points3 >= 0.135 and Texture1 >= 20.299999999999997 | M | 0.047478 |
| Perimeter3 > 106.1 and Texture1 <= 15.745 | B | 0.038668 |
| Concave_points1 > 0.0795 and Perimeter3 > 101.65 and Perimeter3 <= 117.45 | M | 0.021680 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 > 117.2 and Smoothness1 > 0.083 | M | 0.314103 |
| Concave_points3 <= 0.132 and Area1 <= 689.4 | B | 0.867162 |
| Texture1 > 20.25 | M | 0.467742 |
| Concave_points3 <= 0.179 and Area2 <= 21.91 | B | 0.516129 |
| Concavity3 > 0.21 and Perimeter2 <= 2.652 | M | 0.426036 |
| Fractal_dimension1 > 0.052 | B | 0.816667 |
|  | M | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 >= 113.1 and Concave_points3 >= 0.142 | M | 0.309677 |
| Concave_points1 >= 0.046 and Texture3 >= 23.75 and Concavity1 >= 0.108 | M | 0.061404 |
| Perimeter3 >= 104.4 and Area3 >= 967 and Concavity3 >= 0.193 | M | 0.033133 |
|  | B | 0.955357 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

concave_points1|perimeter3|class
---|---|---
(-inf-0.0265]|(117.45-inf)|m
(0.0515-0.0795]|(117.45-inf)|m
(0.0795-inf)|(117.45-inf)|m
(0.0265-0.0515]|(117.45-inf)|m
(0.0795-inf)|(101.65-117.45]|m
(0.0515-0.0795]|(101.65-117.45]|m
(-inf-0.0265]|(101.65-117.45]|b
(0.0265-0.0515]|(101.65-117.45]|b
(0.0795-inf)|(-inf-101.65]|m
(0.0515-0.0795]|(-inf-101.65]|b
(0.0265-0.0515]|(-inf-101.65]|b
(-inf-0.0265]|(-inf-101.65]|b

## JRip

Decision list:

rules | predicted class
---|---
(Perimeter3 >= 113.1) and (Concave_points3 >= 0.142)|M (144.0/0.0)
(Concave_points1 >= 0.046) and (Texture3 >= 23.75) and (Concavity1 >= 0.108)|M (21.0/0.0)
(Perimeter3 >= 104.4) and (Area3 >= 967) and (Concavity3 >= 0.193)|M (11.0/0.0)
|B (336.0/15.0)


## PART

Decision list:

rules | predicted class
---|---
Perimeter3 > 117.2 AND Smoothness1 > 0.083|M (147.0)
Concave_points3 <= 0.132 AND Area1 <= 689.4|B (293.0/3.0)
Texture1 > 20.25|M (29.0/2.0)
Concave_points3 <= 0.179 AND Area2 <= 21.91|B (16.0)
Concavity3 > 0.21 AND Perimeter2 <= 2.652|M (12.0)
Fractal_dimension1 > 0.052|B (12.0)
|M (3.0/1.0)


## J48 Decision Tree

* Perimeter3 <= 106.1
	* Concave_points3 <= 0.1455: B (148.0/2.0)
	* Concave_points3 > 0.1455: M (11.0/5.0)
* Perimeter3 > 106.1
	* Texture1 <= 15.745: B (9.0/3.0)
	* Texture1 > 15.745: M (88.0/3.0)


## SimpleCart Decision Tree

* Perimeter3 < 112.8
	* Concave_points3 < 0.135: B(294.0/4.0)
	* Concave_points3 >= 0.135
		* Texture1 < 20.299999999999997: B(18.0/8.0)
		* Texture1 >= 20.299999999999997: M(16.0/0.0)
* Perimeter3 >= 112.8: M(163.0/9.0)


