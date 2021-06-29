# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Led2 >= 0.5 and Led5 < 0.5 and Led1 >= 0.5 and Led3 < 0.5 | 5 | 0.078079 |
| Led2 >= 0.5 and Led5 < 0.5 and Led1 < 0.5 | 4 | 0.073527 |
| Led2 < 0.5 and Led7 < 0.5 and Led1 >= 0.5 | 7 | 0.071241 |
| Led2 < 0.5 and Led7 >= 0.5 and Led6 < 0.5 | 2 | 0.059940 |
| Led2 < 0.5 and Led7 >= 0.5 and Led6 >= 0.5 | 3 | 0.055380 |
| Led2 >= 0.5 and Led5 >= 0.5 and Led3 < 0.5 | 6 | 0.053667 |
| Led2 >= 0.5 and Led5 >= 0.5 and Led3 >= 0.5 and Led4 < 0.5 | 0 | 0.050595 |
| Led2 >= 0.5 and Led5 >= 0.5 and Led3 >= 0.5 and Led4 >= 0.5 | 8 | 0.046668 |
| Led2 >= 0.5 and Led5 < 0.5 and Led1 >= 0.5 and Led3 >= 0.5 | 9 | 0.046091 |
| Led2 < 0.5 and Led7 < 0.5 and Led1 < 0.5 | 1 | 0.040460 |
| Led1 <= 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 <= 0.5 | 4 | 0.010263 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 <= 0.5 and Led7 > 0.5 | 2 | 0.003627 |
| Led1 > 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 <= 0.5 and Led6 <= 0.5 and Led7 > 0.5 | 3 | 0.004478 |
| Led1 > 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 <= 0.5 and Led7 <= 0.5 | 2 | 0.007371 |
| Led1 <= 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 <= 0.5 and Led6 > 0.5 and Led7 <= 0.5 | 4 | 0.007407 |
| Led1 <= 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 <= 0.5 and Led7 <= 0.5 | 2 | 0.004926 |
| Led1 <= 0.5 and Led2 <= 0.5 and Led4 <= 0.5 and Led5 <= 0.5 and Led6 > 0.5 and Led7 > 0.5 | 1 | 0.004773 |
| Led1 > 0.5 and Led2 <= 0.5 and Led4 <= 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 0 | 0.004380 |
| Led1 > 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 8 | 0.001990 |
| Led1 <= 0.5 and Led2 <= 0.5 and Led4 <= 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 0 | 0.002433 |
| Led1 > 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 <= 0.5 | 0 | 0.002433 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 <= 0.5 | 8 | 0.003722 |
| Led1 <= 0.5 and Led2 <= 0.5 and Led4 > 0.5 and Led5 <= 0.5 and Led6 <= 0.5 and Led7 <= 0.5 | 3 | 0.001256 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 8 | 0.028235 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 <= 0.5 and Led5 <= 0.5 and Led6 > 0.5 and Led7 <= 0.5 | 4 | 0.000625 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 <= 0.5 and Led6 > 0.5 and Led7 > 0.5 | 5 | 0.036038 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 <= 0.5 and Led5 <= 0.5 and Led6 > 0.5 and Led7 > 0.5 | 9 | 0.005626 |
| Led1 > 0.5 and Led2 > 0.5 and Led4 <= 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 0 | 0.037647 |
| Led1 <= 0.5 and Led2 > 0.5 and Led4 > 0.5 and Led5 > 0.5 and Led6 > 0.5 and Led7 > 0.5 | 6 | 0.005570 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Led2 <= 0.0 and Led7 <= 0.0 and Led4 <= 0.0 and Led1 > 0.0 | 7 | 0.075174 |
| Led5 > 0.0 and Led6 <= 0.0 and Led2 <= 0.0 | 2 | 0.077694 |
| Led5 > 0.0 and Led3 <= 0.0 | 6 | 0.066981 |
| Led3 <= 0.0 and Led1 > 0.0 and Led4 > 0.0 | 5 | 0.090612 |
| Led2 <= 0.0 and Led7 <= 0.0 and Led4 <= 0.0 | 1 | 0.073772 |
| Led5 > 0.0 and Led4 > 0.0 and Led7 > 0.0 and Led6 > 0.0 | 8 | 0.080848 |
| Led5 > 0.0 and Led4 <= 0.0 | 0 | 0.106258 |
| Led1 <= 0.0 and Led2 > 0.0 and Led7 <= 0.0 | 4 | 0.170616 |
| Led5 <= 0.0 and Led2 <= 0.0 and Led7 > 0.0 and Led6 > 0.0 and Led4 > 0.0 and Led1 > 0.0 | 3 | 0.138152 |
| Led5 <= 0.0 and Led2 > 0.0 and Led3 > 0.0 and Led4 > 0.0 and Led1 > 0.0 | 9 | 0.136773 |
| Led5 > 0.0 | 8 | 0.037736 |
| Led2 > 0.0 and Led3 <= 0.0 | 5 | 0.014468 |
| Led2 > 0.0 and Led1 <= 0.0 | 4 | 0.024725 |
| Led2 <= 0.0 and Led6 <= 0.0 | 2 | 0.028846 |
| Led7 > 0.0 and Led4 <= 0.0 | 9 | 0.025455 |
| Led7 <= 0.0 | 4 | 0.017527 |
|  | 3 | 0.290323 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

led1|led2|led4|led5|led6|led7|number
---|---|---|---|---|---|---
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|6
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|8
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|8
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|0
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|0
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|4
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|0
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|5
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|3
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|3
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|8
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|9
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|0
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|0
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|2
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|0
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|5
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|0
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|7
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|9
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|3
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|0
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|7
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|4
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|2
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|7
(0.5-inf)|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|0
(-inf-0.5]|(0.5-inf)|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|0
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|7
(0.5-inf)|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|0
(-inf-0.5]|(-inf-0.5]|(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|3
(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|1
(0.5-inf)|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|(-inf-0.5]|7

## PART

Decision list:

rules | predicted class
---|---
Led2 <= 0.0 AND Led7 <= 0.0 AND Led4 <= 0.0 AND Led1 > 0.0|7 (40.0/4.0)
Led5 > 0.0 AND Led6 <= 0.0 AND Led2 <= 0.0|2 (30.0)
Led5 > 0.0 AND Led3 <= 0.0|6 (42.0/10.0)
Led3 <= 0.0 AND Led1 > 0.0 AND Led4 > 0.0|5 (43.0/6.0)
Led2 <= 0.0 AND Led7 <= 0.0 AND Led4 <= 0.0|1 (35.0/8.0)
Led5 > 0.0 AND Led4 > 0.0 AND Led7 > 0.0 AND Led6 > 0.0|8 (40.0/14.0)
Led5 > 0.0 AND Led4 <= 0.0|0 (35.0/6.0)
Led1 <= 0.0 AND Led2 > 0.0 AND Led7 <= 0.0|4 (36.0)
Led5 <= 0.0 AND Led2 <= 0.0 AND Led7 > 0.0 AND Led6 > 0.0 AND Led4 > 0.0 AND Led1 > 0.0|3 (28.0/3.0)
Led5 <= 0.0 AND Led2 > 0.0 AND Led3 > 0.0 AND Led4 > 0.0 AND Led1 > 0.0|9 (41.0/14.0)
Led5 > 0.0|8 (13.0/5.0)
Led2 > 0.0 AND Led3 <= 0.0|5 (9.0/4.0)
Led2 > 0.0 AND Led1 <= 0.0|4 (9.0/5.0)
Led2 <= 0.0 AND Led6 <= 0.0|2 (12.0/6.0)
Led7 > 0.0 AND Led4 <= 0.0|9 (19.0/14.0)
Led7 <= 0.0|4 (10.0/6.0)
|3 (8.0/1.0)


## SimpleCart Decision Tree

* Led2 < 0.5
	* Led7 < 0.5
		* Led1 < 0.5: 1(27.0/15.0)
		* Led1 >= 0.5: 7(39.0/11.0)
	* Led7 >= 0.5
		* Led6 < 0.5: 2(30.0/5.0)
		* Led6 >= 0.5: 3(37.0/23.0)
* Led2 >= 0.5
	* Led5 < 0.5
		* Led1 < 0.5: 4(37.0/6.0)
		* Led1 >= 0.5
			* Led3 < 0.5: 5(40.0/7.0)
			* Led3 >= 0.5: 9(31.0/19.0)
	* Led5 >= 0.5
		* Led3 < 0.5: 6(30.0/9.0)
		* Led3 >= 0.5
			* Led4 < 0.5: 0(26.0/5.0)
			* Led4 >= 0.5: 8(32.0/21.0)


