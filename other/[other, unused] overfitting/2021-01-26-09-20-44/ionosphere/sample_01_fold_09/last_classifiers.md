# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | g | 0.642405 |
| Pulse5 > 0.041 and Pulse1 <= 0.0 | b | 0.081448 |
| Pulse5 <= 0.0515 and Pulse8 > -0.0005 and Pulse8 <= 0.001 | b | 0.113537 |
| Pulse5 <= 0.0515 and Pulse8 > 0.9945 | b | 0.042453 |
| Pulse5 > 0.9875 and Pulse8 > 0.9945 | b | 0.040961 |
| Pulse5 > 0.041 and Pulse1 > 0.0 and Pulse3 > 0.253 and Pulse8 > -0.673 and Pulse34 > 0.863 | b | 0.016043 |
| Pulse5 > 0.9875 and Pulse8 > -0.0005 and Pulse8 <= 0.001 | b | 0.037915 |
| Pulse5 <= 0.041 | b | 0.228137 |
| Pulse5 > 0.041 and Pulse1 > 0.0 and Pulse3 <= 0.253 | b | 0.039494 |
| Pulse5 > 0.041 and Pulse1 > 0.0 and Pulse3 > 0.253 and Pulse8 <= -0.673 and Pulse28 > -0.218 | b | 0.033333 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Pulse5 > 0.051500000000000004 and Pulse1 > 0.5 and Pulse3 > 0.2585 and Pulse8 > -0.6285000000000001 and Pulse34 <= 0.8825000000000001 and Pulse6 > -0.18 and Pulse3 > 0.6825000000000001 | g | 0.568728 |
| Pulse5 <= 0.051500000000000004 | b | 0.530973 |
| Pulse1 > 0.5 and Pulse3 > 0.1505 and Pulse24 > -0.9365 and Pulse6 > -0.8925000000000001 and Pulse8 > -0.9035 and Pulse14 <= 0.17099999999999999 | g | 0.432211 |
| Pulse27 > 0.866 and Pulse1 > 0.5 | b | 0.644643 |
| Pulse1 <= 0.5 | b | 0.642857 |
| Pulse14 <= 0.5435000000000001 and Pulse29 <= 0.1355 | b | 0.473684 |
| Pulse4 > 0.05450000000000001 | g | 0.500000 |
| Pulse26 > 0.1585 | b | 0.625000 |
|  | g | 0.600000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Pulse5 <= 0.23 | b | 0.237067 |
| Pulse27 >= 1 | b | 0.107997 |
|  | g | 0.935484 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

pulse5|pulse8|class
---|---|---
(0.0515-0.418]|(0.9945-inf)|g
(0.418-0.9875]|(0.9945-inf)|g
(0.9875-inf)|(0.9945-inf)|b
(-inf-0.0515]|(0.9945-inf)|b
(0.0515-0.418]|(0.001-0.9945]|g
(0.9875-inf)|(0.001-0.9945]|g
(0.418-0.9875]|(0.001-0.9945]|g
(-inf-0.0515]|(0.001-0.9945]|b
(0.0515-0.418]|(-0.0005-0.001]|g
(0.418-0.9875]|(-0.0005-0.001]|g
(-inf-0.0515]|(-0.0005-0.001]|b
(0.9875-inf)|(-0.0005-0.001]|b
(0.0515-0.418]|(-0.9835--0.0005]|b
(0.418-0.9875]|(-0.9835--0.0005]|g
(0.9875-inf)|(-0.9835--0.0005]|g
(-inf-0.0515]|(-0.9835--0.0005]|b
(-inf-0.0515]|(-inf--0.9835]|b
(0.9875-inf)|(-inf--0.9835]|b

## JRip

Decision list:

rules | predicted class
---|---
(Pulse5 <= 0.23)|b (67.0/2.0)
(Pulse27 >= 1)|b (48.0/14.0)
|g (201.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
Pulse5 > 0.051500000000000004 AND Pulse1 > 0.5 AND Pulse3 > 0.2585 AND Pulse8 > -0.6285000000000001 AND Pulse34 <= 0.8825000000000001 AND Pulse6 > -0.18 AND Pulse3 > 0.6825000000000001|g (151.0/1.0)
Pulse5 <= 0.051500000000000004|b (60.0)
Pulse1 > 0.5 AND Pulse3 > 0.1505 AND Pulse24 > -0.9365 AND Pulse6 > -0.8925000000000001 AND Pulse8 > -0.9035 AND Pulse14 <= 0.17099999999999999|g (45.0/2.0)
Pulse27 > 0.866 AND Pulse1 > 0.5|b (20.0/1.0)
Pulse1 <= 0.5|b (18.0)
Pulse14 <= 0.5435000000000001 AND Pulse29 <= 0.1355|b (9.0)
Pulse4 > 0.05450000000000001|g (6.0)
Pulse26 > 0.1585|b (4.0)
|g (3.0)


## J48 Decision Tree

* Pulse5 <= 0.041: b (60.0)
* Pulse5 > 0.041
	* Pulse1 <= 0.0: b (18.0)
	* Pulse1 > 0.0
		* Pulse3 <= 0.253: b (12.0/2.0)
		* Pulse3 > 0.253
			* Pulse8 <= -0.673
				* Pulse28 <= -0.218: g (6.0/2.0)
				* Pulse28 > -0.218: b (7.0)
			* Pulse8 > -0.673
				* Pulse34 <= 0.863: g (202.0/10.0)
				* Pulse34 > 0.863: b (11.0/5.0)


