# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | negative | 0.555556 |
| A3 = all and A4 = u and A5 = g and A9 = t and A10 = t and A11 > 2.5 and A15 <= 492 | positive | 0.126340 |
| A3 = all and A4 = l and A5 = gg and A9 = f and A10 = f and A11 <= 0.5 and A15 > 492 | positive | 0.002890 |
| A9 = t and A10 = t and A6 != k | positive | 0.329981 |
| A3 = all and A4 = u and A5 = g and A9 = t and A10 = t and A11 > 2.5 and A15 > 492 | positive | 0.168708 |
| A9 != t and A13 = p | positive | 0.009006 |
| A3 = all and A4 = l and A5 = gg and A9 = f and A10 = f and A11 <= 0.5 and A15 <= 492 | positive | 0.002890 |
| A9 = t and A10 = t and A6 = k and A15 > 142.0 | positive | 0.011461 |
| A3 = all and A4 = y and A5 = p and A9 = t and A10 = f and A11 <= 0.5 and A15 > 492 | positive | 0.008621 |
| A9 = t and A10 != t and A15 <= 450.0 and A6 != q and A7 != h and A6 != d and A4 = u and A14 <= 115.0 and A15 <= 13.5 | positive | 0.036499 |
| A9 = t and A10 != t and A15 <= 450.0 and A6 != q and A7 != h and A6 != d and A4 = u and A14 > 115.0 and A15 > 12.0 | positive | 0.008621 |
| A3 = all and A4 = u and A5 = g and A9 = t and A10 = f and A11 <= 0.5 and A15 <= 492 | positive | 0.065083 |
| A3 = all and A4 = u and A5 = g and A9 = t and A10 = t and A11 > 0.5 and A11 <= 2.5 and A15 <= 492 | positive | 0.049519 |
| A3 = all and A4 = u and A5 = g and A9 = t and A10 = f and A11 <= 0.5 and A15 > 492 | positive | 0.041830 |
| A9 = t and A10 != t and A15 <= 450.0 and A6 != q and A7 = h | positive | 0.024074 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A9 = f and A13 = g and A3 <= 1225 and A8 > 0 and A3 <= 79 and A14 > 154 | negative | 0.168675 |
| A9 = f and A13 = g and A3 > 1225 | negative | 0.153374 |
| A9 = f and A13 = g and A8 <= 0 | negative | 0.098039 |
| A9 = f and A8 > 0 and A7 = v and A2 <= 3358 and A2 > 2392 | negative | 0.103896 |
| A9 = f and A8 > 0 and A6 = c and A2 <= 2158 | negative | 0.051749 |
| A9 = f and A8 > 0 and A6 = i | negative | 0.054795 |
| A9 = f and A8 > 0 and A6 = k | negative | 0.035256 |
| A9 = t and A15 > 228 and A15 > 501 and A8 > 1 and A2 > 235 | positive | 0.404444 |
| A9 = f and A8 > 0 and A2 > 3775 | negative | 0.070666 |
| A11 > 3 and A3 > 155 | positive | 0.222222 |
| A9 = f and A3 > 4 and A4 = u and A2 <= 1975 | negative | 0.101504 |
| A14 <= 52 and A11 > 2 | positive | 0.178862 |
| A3 > 3625 | positive | 0.106827 |
| A15 > 228 and A2 <= 215 | positive | 0.106195 |
| A4 = y and A14 <= 208 and A8 <= 175 and A3 > 20 | negative | 0.118644 |
| A10 = t and A6 = q | positive | 0.059809 |
| A15 > 228 | positive | 0.107456 |
| A10 = t and A11 > 1 and A2 <= 2867 | positive | 0.057471 |
| A8 <= 1165 and A3 > 0 and A10 = t | positive | 0.059259 |
| A8 > 1165 | positive | 0.077366 |
| A2 > 4425 | positive | 0.051364 |
| A3 > 3 and A14 > 102 and A14 <= 212 and A2 > 2292 | negative | 0.315789 |
| A6 = c | positive | 0.084706 |
| A4 = y | negative | 0.344048 |
| A14 > 303 | negative | 0.366870 |
| A13 = g and A8 <= 35 | negative | 0.205782 |
| A13 = g | positive | 0.459201 |
|  | negative | 0.846154 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

a3|a4|a5|a9|a10|a11|a15|class
---|---|---|---|---|---|---|---
all|u|g|f|t|(2.5-inf)|(492-inf)|negative
all|l|gg|f|f|(-inf-0.5]|(492-inf)|positive
all|y|p|t|t|(2.5-inf)|(492-inf)|positive
all|y|p|f|t|(2.5-inf)|(-inf-492]|positive
all|y|p|f|f|(-inf-0.5]|(492-inf)|negative
all|u|g|t|t|(2.5-inf)|(492-inf)|positive
all|u|g|f|t|(0.5-2.5]|(492-inf)|negative
all|y|p|t|t|(0.5-2.5]|(492-inf)|positive
all|l|gg|f|f|(-inf-0.5]|(-inf-492]|positive
all|y|p|t|f|(-inf-0.5]|(492-inf)|positive
all|u|g|f|t|(2.5-inf)|(-inf-492]|negative
all|u|g|f|f|(-inf-0.5]|(492-inf)|negative
all|y|p|t|t|(2.5-inf)|(-inf-492]|positive
all|?|?|f|f|(-inf-0.5]|(-inf-492]|positive
all|y|p|f|t|(0.5-2.5]|(-inf-492]|negative
all|u|g|t|t|(0.5-2.5]|(492-inf)|positive
all|y|p|f|f|(-inf-0.5]|(-inf-492]|negative
all|u|g|t|f|(-inf-0.5]|(492-inf)|positive
all|u|g|t|t|(2.5-inf)|(-inf-492]|positive
all|u|g|f|t|(0.5-2.5]|(-inf-492]|negative
all|y|p|t|t|(0.5-2.5]|(-inf-492]|positive
all|u|g|f|f|(-inf-0.5]|(-inf-492]|negative
all|y|p|t|f|(-inf-0.5]|(-inf-492]|negative
all|u|g|t|t|(0.5-2.5]|(-inf-492]|positive
all|u|g|t|f|(-inf-0.5]|(-inf-492]|positive

## PART

Decision list:

rules | predicted class
---|---
A9 = f AND A13 = g AND A3 <= 1225 AND A8 > 0 AND A3 <= 79 AND A14 > 154|negative (56.0)
A9 = f AND A13 = g AND A3 > 1225|negative (50.0)
A9 = f AND A13 = g AND A8 <= 0|negative (30.0)
A9 = f AND A8 > 0 AND A7 = v AND A2 <= 3358 AND A2 > 2392|negative (31.3)
A9 = f AND A8 > 0 AND A6 = c AND A2 <= 2158|negative (16.24/1.0)
A9 = f AND A8 > 0 AND A6 = i|negative (16.12)
A9 = f AND A8 > 0 AND A6 = k|negative (12.8/1.0)
A9 = t AND A15 > 228 AND A15 > 501 AND A8 > 1 AND A2 > 235|positive (90.9)
A9 = f AND A8 > 0 AND A2 > 3775|negative (15.0)
A11 > 3 AND A3 > 155|positive (34.0)
A9 = f AND A3 > 4 AND A4 = u AND A2 <= 1975|negative (19.0/1.0)
A14 <= 52 AND A11 > 2|positive (22.0)
A3 > 3625|positive (14.0/1.0)
A15 > 228 AND A2 <= 215|positive (12.04)
A4 = y AND A14 <= 208 AND A8 <= 175 AND A3 > 20|negative (13.54)
A10 = t AND A6 = q|positive (19.0/9.0)
A15 > 228|positive (16.06/3.0)
A10 = t AND A11 > 1 AND A2 <= 2867|positive (14.0/4.0)
A8 <= 1165 AND A3 > 0 AND A10 = t|positive (19.0/7.0)
A8 > 1165|positive (14.0/3.0)
A2 > 4425|positive (10.5/2.4)
A3 > 3 AND A14 > 102 AND A14 <= 212 AND A2 > 2292|negative (10.25)
A6 = c|positive (14.77/6.25)
A4 = y|negative (17.95/4.63)
A14 > 303|negative (13.92/2.49)
A13 = g AND A8 <= 35|negative (13.9/6.0)
A13 = g|positive (12.45/1.55)
|negative (12.26/4.36)


## J48 Decision Tree

* A9 = t
	* A10 = t
		* A6 = k
			* A15 <= 142.0: negative (5.0/1.0)
			* A15 > 142.0: positive (4.0)
		* A6 != k: positive (200.0/16.0)
	* A10 != t
		* A15 <= 450.0
			* A6 = q
				* A1 = b: positive (7.0)
				* A1 != b: negative (3.0/1.0)
			* A6 != q
				* A7 = h: positive (20.0/7.0)
				* A7 != h
					* A6 = d: negative (4.0)
					* A6 != d
						* A4 = u
							* A14 <= 115.0
								* A15 <= 13.5: positive (15.0/1.0)
								* A15 > 13.5: negative (4.0/1.0)
							* A14 > 115.0
								* A15 <= 12.0: negative (30.0/7.0)
								* A15 > 12.0: positive (3.0)
						* A4 != u: negative (11.0/1.0)
		* A15 > 450.0: positive (20.0/1.0)
* A9 != t
	* A13 = p: positive (8.0/3.0)
	* A13 != p: negative (287.0/16.0)


