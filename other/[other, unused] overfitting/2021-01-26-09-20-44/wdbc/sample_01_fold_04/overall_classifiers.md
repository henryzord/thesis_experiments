# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Smoothness1 > 0.0885 and Radius3 <= 14.905 and Texture3 <= 24.87 and Perimeter3 <= 101.55 | B | 0.343676 |
| Smoothness1 > 0.0885 and Radius3 > 18.225 and Texture3 > 24.87 and Perimeter3 > 116.05 | M | 0.233890 |
| Smoothness1 <= 0.0885 and Radius3 <= 14.905 and Texture3 <= 24.87 and Perimeter3 <= 101.55 | B | 0.242063 |
| Smoothness1 > 0.0885 and Radius3 <= 14.905 and Texture3 > 24.87 and Perimeter3 <= 101.55 | B | 0.174007 |
| Smoothness1 <= 0.0885 and Radius3 <= 14.905 and Texture3 > 24.87 and Perimeter3 <= 101.55 | B | 0.169565 |
| Smoothness1 > 0.0885 and Radius3 > 18.225 and Texture3 <= 24.87 and Perimeter3 > 116.05 | M | 0.058651 |
| Smoothness1 <= 0.0885 and Radius3 > 18.225 and Texture3 > 24.87 and Perimeter3 > 116.05 | M | 0.036036 |
| Smoothness1 > 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 <= 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.052550 |
| Smoothness1 > 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 > 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | M | 0.033988 |
| Smoothness1 <= 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 <= 24.87 and Perimeter3 <= 101.55 | B | 0.045000 |
| Smoothness1 <= 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 > 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.041876 |
| Smoothness1 > 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 > 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | M | 0.030211 |
| Smoothness1 > 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 <= 24.87 and Perimeter3 <= 101.55 | B | 0.040201 |
| Smoothness1 > 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 > 24.87 and Perimeter3 > 116.05 | M | 0.024620 |
| Smoothness1 <= 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 <= 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.035354 |
| Smoothness1 <= 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 > 24.87 and Perimeter3 <= 101.55 | B | 0.030457 |
| Smoothness1 > 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 <= 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.030457 |
| Smoothness1 > 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 <= 24.87 and Perimeter3 > 116.05 | M | 0.015337 |
| Smoothness1 > 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 > 24.87 and Perimeter3 <= 101.55 | B | 0.025128 |
| Smoothness1 <= 0.0885 and Radius3 > 18.225 and Texture3 <= 24.87 and Perimeter3 > 116.05 | M | 0.009877 |
| Smoothness1 <= 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 > 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | M | 0.009259 |
| Smoothness1 > 0.0885 and Radius3 > 14.905 and Radius3 <= 16.805 and Texture3 > 24.87 and Perimeter3 > 116.05 | M | 0.009259 |
| Smoothness1 <= 0.0885 and Radius3 > 16.805 and Radius3 <= 18.225 and Texture3 <= 24.87 and Perimeter3 > 101.55 and Perimeter3 <= 116.05 | B | 0.010363 |

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
| Radius3 >= 16.84 and Concave_points3 >= 0.146 | M | 0.299127 |
| Perimeter3 >= 101.7 and Texture1 >= 19.77 and Concave_points1 >= 0.053 | M | 0.069565 |
| Area3 >= 967 and Concavity3 >= 0.208 | M | 0.030211 |
| Concave_points3 >= 0.111 and Smoothness3 >= 0.178 and Concavity1 >= 0.104 | M | 0.021341 |
| Radius3 >= 15.75 and Radius1 <= 13.96 and Radius1 >= 13.44 | M | 0.018349 |
| Area2 >= 38.87 and Texture1 >= 21.46 and Radius1 >= 14.48 | M | 0.015337 |
|  | B | 0.993808 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

smoothness1|radius3|texture3|perimeter3|class
---|---|---|---|---
(-inf-0.0885]|(18.225-inf)|(24.87-inf)|(116.05-inf)|m
(0.0885-inf)|(18.225-inf)|(24.87-inf)|(116.05-inf)|m
(-inf-0.0885]|(16.805-18.225]|(24.87-inf)|(116.05-inf)|m
(0.0885-inf)|(16.805-18.225]|(24.87-inf)|(116.05-inf)|m
(0.0885-inf)|(14.905-16.805]|(24.87-inf)|(116.05-inf)|m
(-inf-0.0885]|(18.225-inf)|(-inf-24.87]|(116.05-inf)|m
(0.0885-inf)|(18.225-inf)|(-inf-24.87]|(116.05-inf)|m
(0.0885-inf)|(16.805-18.225]|(-inf-24.87]|(116.05-inf)|m
(-inf-0.0885]|(16.805-18.225]|(24.87-inf)|(101.55-116.05]|m
(0.0885-inf)|(16.805-18.225]|(24.87-inf)|(101.55-116.05]|m
(-inf-0.0885]|(14.905-16.805]|(24.87-inf)|(101.55-116.05]|b
(0.0885-inf)|(14.905-16.805]|(24.87-inf)|(101.55-116.05]|m
(-inf-0.0885]|(16.805-18.225]|(-inf-24.87]|(101.55-116.05]|b
(0.0885-inf)|(16.805-18.225]|(-inf-24.87]|(101.55-116.05]|b
(-inf-0.0885]|(14.905-16.805]|(-inf-24.87]|(101.55-116.05]|b
(0.0885-inf)|(14.905-16.805]|(-inf-24.87]|(101.55-116.05]|b
(-inf-0.0885]|(-inf-14.905]|(-inf-24.87]|(101.55-116.05]|m
(-inf-0.0885]|(14.905-16.805]|(24.87-inf)|(-inf-101.55]|b
(0.0885-inf)|(14.905-16.805]|(24.87-inf)|(-inf-101.55]|b
(0.0885-inf)|(-inf-14.905]|(24.87-inf)|(-inf-101.55]|b
(-inf-0.0885]|(-inf-14.905]|(24.87-inf)|(-inf-101.55]|b
(-inf-0.0885]|(14.905-16.805]|(-inf-24.87]|(-inf-101.55]|b
(0.0885-inf)|(14.905-16.805]|(-inf-24.87]|(-inf-101.55]|b
(-inf-0.0885]|(-inf-14.905]|(-inf-24.87]|(-inf-101.55]|b
(0.0885-inf)|(-inf-14.905]|(-inf-24.87]|(-inf-101.55]|b

## JRip

Decision list:

rules | predicted class
---|---
(Radius3 >= 16.84) and (Concave_points3 >= 0.146)|M (137.0/0.0)
(Perimeter3 >= 101.7) and (Texture1 >= 19.77) and (Concave_points1 >= 0.053)|M (24.0/0.0)
(Area3 >= 967) and (Concavity3 >= 0.208)|M (10.0/0.0)
(Concave_points3 >= 0.111) and (Smoothness3 >= 0.178) and (Concavity1 >= 0.104)|M (7.0/0.0)
(Radius3 >= 15.75) and (Radius1 <= 13.96) and (Radius1 >= 13.44)|M (6.0/0.0)
(Area2 >= 38.87) and (Texture1 >= 21.46) and (Radius1 >= 14.48)|M (5.0/0.0)
|B (323.0/2.0)


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


