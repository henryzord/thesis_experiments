# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Texture1 <= 18.635 and Smoothness1 > 0.0885 and Perimeter3 <= 101.55 | B | 0.373799 |
| Texture1 > 18.635 and Smoothness1 > 0.0885 and Perimeter3 > 116.05 | M | 0.253488 |
| Texture1 <= 18.635 and Smoothness1 <= 0.0885 and Perimeter3 <= 101.55 | B | 0.265385 |
| Texture1 > 18.635 and Smoothness1 <= 0.0885 and Perimeter3 <= 101.55 | B | 0.194093 |
| Texture1 > 18.635 and Smoothness1 > 0.0885 and Perimeter3 <= 101.55 | B | 0.169083 |
| Texture1 <= 18.635 and Smoothness1 > 0.0885 and Perimeter3 > 116.05 | M | 0.072361 |
| Texture1 > 18.635 and Smoothness1 > 0.0885 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | M | 0.058418 |
| Texture1 <= 18.635 and Smoothness1 > 0.0885 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.076192 |
| Texture1 > 18.635 and Smoothness1 <= 0.0885 and Perimeter3 > 116.05 | M | 0.036251 |
| Texture1 <= 18.635 and Smoothness1 <= 0.0885 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.045000 |
| Texture1 > 18.635 and Smoothness1 <= 0.0885 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.038388 |
| Texture1 <= 18.635 and Smoothness1 <= 0.0885 and Perimeter3 > 116.05 | M | 0.006966 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Perimeter3 > 115.9 and Concave_points1 > 0.05 | M | 0.309677 |
| Perimeter3 <= 101.4 and Smoothness1 <= 0.117 and Symmetry2 > 0.016 | B | 0.803347 |
| Concave_points3 <= 0.16 and Area3 <= 873.2 and Texture1 <= 21.26 and Fractal_dimension2 <= 0.002 | B | 0.500000 |
| Concave_points3 <= 0.16 and Area3 <= 767.3 and Texture2 <= 1.377 | B | 0.494624 |
| Texture3 > 19.9 and Symmetry3 > 0.319 | M | 0.368421 |
| Texture3 <= 20.61 | B | 0.365854 |
| Fractal_dimension2 > 0.003 | B | 0.244444 |
| Concavity3 > 0.196 and Texture1 <= 21.38 | M | 0.462963 |
| Concavity3 <= 0.196 | B | 0.266667 |
|  | M | 0.888889 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Area3 >= 869.3 and Concavity1 >= 0.074 | M | 0.315565 |
| Perimeter3 >= 101.7 and Texture3 >= 25.84 and Smoothness1 >= 0.091 | M | 0.064261 |
| Radius3 >= 15.79 and Texture1 >= 19.38 and Compactness1 <= 0.071 | M | 0.024620 |
| Concave_points3 >= 0.136 and Smoothness1 >= 0.119 | M | 0.015337 |
|  | B | 0.981651 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

texture1|smoothness1|perimeter3|class
---|---|---|---
(-inf-18.635]|(0.0885-inf)|(116.05-inf)|m
(18.635-inf)|(0.0885-inf)|(116.05-inf)|m
(-inf-18.635]|(-inf-0.0885]|(116.05-inf)|m
(18.635-inf)|(-inf-0.0885]|(116.05-inf)|m
(18.635-inf)|(0.0885-inf)|(101.55-116.05]|m
(-inf-18.635]|(0.0885-inf)|(101.55-116.05]|b
(-inf-18.635]|(-inf-0.0885]|(101.55-116.05]|b
(18.635-inf)|(-inf-0.0885]|(101.55-116.05]|b
(-inf-18.635]|(0.0885-inf)|(-inf-101.55]|b
(18.635-inf)|(0.0885-inf)|(-inf-101.55]|b
(-inf-18.635]|(-inf-0.0885]|(-inf-101.55]|b
(18.635-inf)|(-inf-0.0885]|(-inf-101.55]|b

## JRip

Decision list:

rules | predicted class
---|---
(Area3 >= 869.3) and (Concavity1 >= 0.074)|M (148.0/0.0)
(Perimeter3 >= 101.7) and (Texture3 >= 25.84) and (Smoothness1 >= 0.091)|M (24.0/1.0)
(Radius3 >= 15.79) and (Texture1 >= 19.38) and (Compactness1 <= 0.071)|M (10.0/1.0)
(Concave_points3 >= 0.136) and (Smoothness1 >= 0.119)|M (5.0/0.0)
|B (325.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Perimeter3 > 115.9 AND Concave_points1 > 0.05|M (144.0)
Perimeter3 <= 101.4 AND Smoothness1 <= 0.117 AND Symmetry2 > 0.016|B (192.0)
Concave_points3 <= 0.16 AND Area3 <= 873.2 AND Texture1 <= 21.26 AND Fractal_dimension2 <= 0.002|B (47.0)
Concave_points3 <= 0.16 AND Area3 <= 767.3 AND Texture2 <= 1.377|B (46.0)
Texture3 > 19.9 AND Symmetry3 > 0.319|M (21.0)
Texture3 <= 20.61|B (15.0)
Fractal_dimension2 > 0.003|B (15.0/4.0)
Concavity3 > 0.196 AND Texture1 <= 21.38|M (10.0/2.0)
Concavity3 <= 0.196|B (12.0/4.0)
|M (10.0)


