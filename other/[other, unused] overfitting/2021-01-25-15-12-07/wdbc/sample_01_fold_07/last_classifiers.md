# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | B | 0.626953 |
| Perimeter3 >= 112.8 and Concave_points1 < 0.05 | M | 0.015673 |
| Concave_points1 > 0.0265 and Concave_points1 <= 0.0515 and Area3 > 696.05 and Area3 <= 880.75 and Smoothness3 > 0.1375 | M | 0.004673 |
| Perimeter3 <= 106.1 and Concave_points3 > 0.1455 | M | 0.019231 |
| Concave_points1 > 0.0795 and Area3 > 1214 and Smoothness3 > 0.1375 | M | 0.146277 |
| Concave_points1 > 0.0515 and Concave_points1 <= 0.0795 and Area3 > 880.75 and Area3 <= 1214 and Smoothness3 <= 0.1375 | M | 0.006966 |
| Concave_points1 > 0.0795 and Area3 > 1214 and Smoothness3 <= 0.1375 | M | 0.088068 |
| Perimeter3 > 106.1 and Texture1 > 15.745 | M | 0.327592 |
| Concave_points1 > 0.0515 and Concave_points1 <= 0.0795 and Area3 > 880.75 and Area3 <= 1214 and Smoothness3 > 0.1375 | M | 0.030211 |
| Concave_points1 > 0.0515 and Concave_points1 <= 0.0795 and Area3 > 696.05 and Area3 <= 880.75 and Smoothness3 > 0.1375 | M | 0.033364 |
| Perimeter3 > 106.1 and Texture1 <= 15.745 and Concavity1 > 0.1715 | M | 0.015337 |
| Perimeter3 < 112.8 and Concave_points3 >= 0.135 and Texture1 >= 20.299999999999997 | M | 0.047478 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 > 117.45 and Smoothness1 > 0.0835 | M | 0.314103 |
| Concave_points3 <= 0.1325 and Area1 <= 689.45 and Area2 <= 36.730000000000004 and Texture3 <= 33.269999999999996 | B | 0.854305 |
| Concave_points3 > 0.1605 and Texture3 > 23.47 | M | 0.231707 |
| Texture3 > 20.355 and Area3 <= 724.05 and Area2 <= 47.035 and Smoothness3 <= 0.1415 | B | 0.489796 |
| Texture3 <= 20.355 | B | 0.431818 |
| Area2 > 16.805 and Fractal_dimension2 <= 0.0075 and Symmetry1 > 0.152 and Concavity1 > 0.103 | M | 0.354839 |
| Perimeter3 <= 122.05 and Area2 > 19.56 and Compactness2 > 0.0175 and Smoothness3 <= 0.1375 | B | 0.440000 |
| Area2 > 19.56 and Radius1 > 13.024999999999999 | M | 0.571429 |
| Area2 <= 19.58 | B | 0.800000 |
|  | M | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 >= 113.1 and Concave_points3 >= 0.142 | M | 0.309677 |
| Concave_points1 >= 0.046 and Texture3 >= 23.75 and Concavity1 >= 0.108 | M | 0.061404 |
| Perimeter3 >= 104.4 and Area3 >= 967 and Concavity3 >= 0.193 | M | 0.033133 |
|  | B | 0.955357 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

concave_points1|area3|smoothness3|class
---|---|---|---
(0.0515-0.0795]|(1214-inf)|(0.1375-inf)|m
(0.0795-inf)|(1214-inf)|(0.1375-inf)|m
(0.0515-0.0795]|(880.75-1214]|(0.1375-inf)|m
(0.0265-0.0515]|(880.75-1214]|(0.1375-inf)|m
(0.0795-inf)|(880.75-1214]|(0.1375-inf)|m
(0.0265-0.0515]|(696.05-880.75]|(0.1375-inf)|m
(0.0265-0.0515]|(1214-inf)|(-inf-0.1375]|m
(0.0795-inf)|(696.05-880.75]|(0.1375-inf)|m
(0.0515-0.0795]|(696.05-880.75]|(0.1375-inf)|m
(0.0515-0.0795]|(1214-inf)|(-inf-0.1375]|m
(0.0795-inf)|(1214-inf)|(-inf-0.1375]|m
(-inf-0.0265]|(880.75-1214]|(-inf-0.1375]|m
(0.0795-inf)|(-inf-696.05]|(0.1375-inf)|m
(0.0795-inf)|(880.75-1214]|(-inf-0.1375]|m
(0.0515-0.0795]|(880.75-1214]|(-inf-0.1375]|m
(0.0265-0.0515]|(880.75-1214]|(-inf-0.1375]|b
(0.0265-0.0515]|(-inf-696.05]|(0.1375-inf)|b
(-inf-0.0265]|(-inf-696.05]|(0.1375-inf)|b
(0.0515-0.0795]|(-inf-696.05]|(0.1375-inf)|b
(0.0795-inf)|(696.05-880.75]|(-inf-0.1375]|m
(-inf-0.0265]|(696.05-880.75]|(-inf-0.1375]|b
(0.0265-0.0515]|(696.05-880.75]|(-inf-0.1375]|b
(0.0515-0.0795]|(696.05-880.75]|(-inf-0.1375]|b
(0.0515-0.0795]|(-inf-696.05]|(-inf-0.1375]|b
(0.0265-0.0515]|(-inf-696.05]|(-inf-0.1375]|b
(-inf-0.0265]|(-inf-696.05]|(-inf-0.1375]|b

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
Perimeter3 > 117.45 AND Smoothness1 > 0.0835|M (147.0)
Concave_points3 <= 0.1325 AND Area1 <= 689.45 AND Area2 <= 36.730000000000004 AND Texture3 <= 33.269999999999996|B (258.0)
Concave_points3 > 0.1605 AND Texture3 > 23.47|M (19.0)
Texture3 > 20.355 AND Area3 <= 724.05 AND Area2 <= 47.035 AND Smoothness3 <= 0.1415|B (24.0)
Texture3 <= 20.355|B (19.0)
Area2 > 16.805 AND Fractal_dimension2 <= 0.0075 AND Symmetry1 > 0.152 AND Concavity1 > 0.103|M (11.0)
Perimeter3 <= 122.05 AND Area2 > 19.56 AND Compactness2 > 0.0175 AND Smoothness3 <= 0.1375|B (11.0)
Area2 > 19.56 AND Radius1 > 13.024999999999999|M (12.0)
Area2 <= 19.58|B (8.0)
|M (3.0/1.0)


## J48 Decision Tree

* Perimeter3 <= 106.1
	* Concave_points3 <= 0.1455: B (148.0/2.0)
	* Concave_points3 > 0.1455: M (11.0/5.0)
* Perimeter3 > 106.1
	* Texture1 <= 15.745
		* Concavity1 <= 0.1715: B (6.0)
		* Concavity1 > 0.1715: M (3.0)
	* Texture1 > 15.745: M (88.0/3.0)


## SimpleCart Decision Tree

* Perimeter3 < 112.8
	* Concave_points3 < 0.135: B(294.0/4.0)
	* Concave_points3 >= 0.135
		* Texture1 < 20.299999999999997: B(18.0/8.0)
		* Texture1 >= 20.299999999999997: M(16.0/0.0)
* Perimeter3 >= 112.8
	* Concave_points1 < 0.05: M(9.0/7.0)
	* Concave_points1 >= 0.05: M(154.0/2.0)


