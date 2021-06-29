# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| middle-middle-square != 0 and bottom-right-square!=(2) and top-left-square!=(2) | 0 | 0.252055 |
| top-left-square = 2 and middle-middle-square = 2 and bottom-right-square = 2 | 1 | 0.208995 |
| top-left-square = 1 and middle-middle-square = 2 and bottom-right-square = 1 | 1 | 0.113713 |
| top-left-square = 0 and middle-middle-square = 2 and bottom-right-square = 1 | 1 | 0.091483 |
| top-left-square = 1 and middle-middle-square = 2 and bottom-right-square = 0 | 1 | 0.082140 |
| top-left-square = 1 and middle-middle-square = 2 and bottom-right-square = 2 | 1 | 0.060449 |
| top-left-square = 2 and middle-middle-square = 2 and bottom-right-square = 1 | 1 | 0.057886 |
| top-left-square = 2 and middle-middle-square = 1 and bottom-right-square = 1 | 1 | 0.063694 |
| top-left-square = 1 and middle-middle-square = 1 and bottom-right-square = 2 | 1 | 0.066235 |
| top-left-square = 2 and middle-middle-square = 1 and bottom-right-square = 0 | 1 | 0.045682 |
| top-left-square = 0 and middle-middle-square = 1 and bottom-right-square = 2 | 1 | 0.048182 |
| top-left-square = 0 and middle-middle-square = 2 and bottom-right-square = 0 | 1 | 0.077160 |
| top-left-square = 2 and middle-middle-square = 0 and bottom-right-square = 1 | 1 | 0.058227 |
| top-left-square = 0 and middle-middle-square = 2 and bottom-right-square = 2 | 1 | 0.062696 |
| top-left-square = 1 and middle-middle-square = 0 and bottom-right-square = 2 | 1 | 0.056989 |
| top-left-square = 2 and middle-middle-square = 0 and bottom-right-square = 0 | 1 | 0.059748 |
| top-left-square = 2 and middle-middle-square = 2 and bottom-right-square = 0 | 1 | 0.056782 |
| top-left-square = 0 and middle-middle-square = 0 and bottom-right-square = 2 | 1 | 0.056782 |
| middle-middle-square = 0 and top-right-square != 2 and bottom-right-square != 0 and middle-right-square != 0 | 0 | 0.023046 |
| top-left-square = 2 and middle-middle-square = 0 and bottom-right-square = 2 | 1 | 0.047771 |
| middle-middle-square = 0 and top-right-square = 2 and bottom-left-square != 2 and top-left-square != 0 and middle-left-square != 0 | 0 | 0.003656 |
| top-left-square = 1 and middle-middle-square = 0 and bottom-right-square = 0 | 0 | 0.012281 |
| middle-middle-square = 0 and top-right-square = 2 and bottom-left-square != 2 and top-left-square = 0 and bottom-right-square != 2 and bottom-middle-square != 2 | 0 | 0.005300 |
| middle-middle-square = 0 and top-right-square != 2 and bottom-right-square != 0 and middle-right-square != 2 | 0 | 0.008768 |
| middle-middle-square = 0 and top-right-square = 2 and bottom-left-square != 2 and top-left-square != 0 and middle-left-square != 2 | 0 | 0.001808 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| middle-middle-square = 2 and bottom-right-square = 0 and top-left-square = 0 | 1 | 0.077160 |
| middle-middle-square = 2 and bottom-left-square = 0 and top-right-square = 0 | 1 | 0.077160 |
| middle-middle-square = 2 and bottom-right-square = 2 and top-left-square = 2 | 1 | 0.187500 |
| middle-middle-square = 2 and bottom-left-square = 2 and top-right-square = 2 | 1 | 0.194070 |
| middle-middle-square = 0 and top-right-square = 2 and bottom-left-square = 0 | 1 | 0.059748 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square = 1 and top-left-square = 2 | 1 | 0.046166 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square = 0 | 1 | 0.059748 |
| middle-middle-square = 2 and top-left-square = 0 and bottom-right-square = 1 and middle-right-square = 2 | 1 | 0.039389 |
| middle-middle-square = 2 and top-middle-square = 2 and bottom-middle-square = 2 | 1 | 0.135838 |
| bottom-right-square = 1 and top-left-square = 1 and middle-middle-square = 1 | 0 | 0.149502 |
| top-right-square = 1 and bottom-left-square = 1 and middle-middle-square = 1 | 0 | 0.143813 |
| top-right-square = 2 and bottom-middle-square = 0 and middle-left-square = 1 and top-left-square = 2 | 1 | 0.056054 |
| bottom-right-square = 2 and top-left-square = 0 and middle-middle-square = 1 and bottom-middle-square = 2 | 1 | 0.066632 |
| top-right-square = 2 and middle-left-square = 0 and bottom-middle-square = 1 and top-middle-square = 2 | 1 | 0.051934 |
| top-middle-square = 0 and bottom-right-square = 2 and middle-left-square = 0 | 1 | 0.062222 |
| top-right-square = 1 and top-middle-square = 2 and bottom-right-square = 1 and middle-right-square = 1 | 0 | 0.092166 |
| bottom-middle-square = 0 and middle-left-square = 2 and top-right-square = 2 | 1 | 0.068293 |
| bottom-left-square = 2 and top-left-square = 2 and middle-left-square = 2 | 1 | 0.180258 |
| bottom-right-square = 1 and bottom-middle-square = 1 and bottom-left-square = 1 | 0 | 0.189655 |
| middle-right-square = 1 and middle-middle-square = 1 and middle-left-square = 1 | 0 | 0.184971 |
| top-middle-square = 2 and top-left-square = 2 and top-right-square = 2 | 1 | 0.197452 |
| bottom-right-square = 0 and middle-middle-square = 1 | 0 | 0.105691 |
| middle-right-square = 0 and bottom-left-square = 2 and bottom-middle-square = 2 and bottom-right-square = 2 | 1 | 0.124031 |
| middle-right-square = 0 | 0 | 0.248000 |
| middle-right-square = 1 and bottom-right-square = 2 and bottom-left-square = 2 and bottom-middle-square = 2 | 1 | 0.163265 |
| middle-right-square = 2 and top-right-square = 2 and bottom-right-square = 2 | 1 | 0.316667 |
| middle-right-square = 1 | 0 | 0.420290 |
| middle-left-square = 1 and bottom-left-square = 1 | 0 | 0.298246 |
| middle-middle-square = 1 and bottom-middle-square = 1 | 0 | 0.245283 |
| middle-left-square = 2 and middle-middle-square = 2 | 1 | 0.603448 |
| top-right-square = 1 | 0 | 0.798913 |
| top-left-square = 1 | 1 | 0.666667 |
|  | 0 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| middle-middle-square = 1 and bottom-right-square = 1 and top-left-square = 1 | 0 | 0.074013 |
| middle-middle-square = 1 and bottom-left-square = 1 and top-right-square = 1 | 0 | 0.070957 |
| middle-middle-square = 1 and top-middle-square = 1 and bottom-middle-square = 1 | 0 | 0.056951 |
| bottom-right-square = 1 and top-right-square = 1 and middle-right-square = 1 | 0 | 0.058528 |
| bottom-left-square = 1 and top-left-square = 1 and middle-left-square = 1 | 0 | 0.052189 |
| middle-middle-square = 1 and middle-left-square = 1 and middle-right-square = 1 | 0 | 0.053782 |
| bottom-left-square = 1 and bottom-right-square = 1 and bottom-middle-square = 1 | 0 | 0.055369 |
| top-left-square = 1 and top-right-square = 1 and top-middle-square = 1 | 0 | 0.053782 |
|  | 1 | 0.975737 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

top-left-square|middle-middle-square|bottom-right-square|target
---|---|---|---
0|2|2|1
2|2|2|1
1|2|2|1
1|1|2|1
0|1|2|1
2|1|2|0
2|0|2|1
1|2|1|1
0|0|2|1
0|2|1|1
2|2|1|1
1|0|2|1
0|1|1|0
1|1|1|0
2|1|1|1
0|0|1|0
1|0|1|0
0|2|0|1
2|0|1|1
1|2|0|1
2|2|0|1
1|1|0|0
0|1|0|0
2|1|0|1
1|0|0|0
2|0|0|1

## JRip

Decision list:

rules | predicted class
---|---
(middle-middle-square = 1) and (bottom-right-square = 1) and (top-left-square = 1)|0 (45.0/0.0)
(middle-middle-square = 1) and (bottom-left-square = 1) and (top-right-square = 1)|0 (43.0/0.0)
(middle-middle-square = 1) and (top-middle-square = 1) and (bottom-middle-square = 1)|0 (34.0/0.0)
(bottom-right-square = 1) and (top-right-square = 1) and (middle-right-square = 1)|0 (35.0/0.0)
(bottom-left-square = 1) and (top-left-square = 1) and (middle-left-square = 1)|0 (31.0/0.0)
(middle-middle-square = 1) and (middle-left-square = 1) and (middle-right-square = 1)|0 (32.0/0.0)
(bottom-left-square = 1) and (bottom-right-square = 1) and (bottom-middle-square = 1)|0 (33.0/0.0)
(top-left-square = 1) and (top-right-square = 1) and (top-middle-square = 1)|0 (32.0/0.0)
|1 (577.0/14.0)


## PART

Decision list:

rules | predicted class
---|---
middle-middle-square = 2 AND bottom-right-square = 0 AND top-left-square = 0|1 (25.0)
middle-middle-square = 2 AND bottom-left-square = 0 AND top-right-square = 0|1 (25.0)
middle-middle-square = 2 AND bottom-right-square = 2 AND top-left-square = 2|1 (69.0)
middle-middle-square = 2 AND bottom-left-square = 2 AND top-right-square = 2|1 (72.0)
middle-middle-square = 0 AND top-right-square = 2 AND bottom-left-square = 0|1 (19.0)
middle-middle-square = 0 AND bottom-left-square = 2 AND top-right-square = 1 AND top-left-square = 2|1 (20.0/3.0)
middle-middle-square = 0 AND bottom-left-square = 2 AND top-right-square = 0|1 (19.0)
middle-middle-square = 2 AND top-left-square = 0 AND bottom-right-square = 1 AND middle-right-square = 2|1 (16.0/2.0)
middle-middle-square = 2 AND top-middle-square = 2 AND bottom-middle-square = 2|1 (47.0)
bottom-right-square = 1 AND top-left-square = 1 AND middle-middle-square = 1|0 (45.0)
top-right-square = 1 AND bottom-left-square = 1 AND middle-middle-square = 1|0 (43.0)
top-right-square = 2 AND bottom-middle-square = 0 AND middle-left-square = 1 AND top-left-square = 2|1 (18.0/3.0)
bottom-right-square = 2 AND top-left-square = 0 AND middle-middle-square = 1 AND bottom-middle-square = 2|1 (17.0/1.0)
top-right-square = 2 AND middle-left-square = 0 AND bottom-middle-square = 1 AND top-middle-square = 2|1 (17.0/3.0)
top-middle-square = 0 AND bottom-right-square = 2 AND middle-left-square = 0|1 (14.0)
top-right-square = 1 AND top-middle-square = 2 AND bottom-right-square = 1 AND middle-right-square = 1|0 (18.0)
bottom-middle-square = 0 AND middle-left-square = 2 AND top-right-square = 2|1 (14.0)
bottom-left-square = 2 AND top-left-square = 2 AND middle-left-square = 2|1 (42.0)
bottom-right-square = 1 AND bottom-middle-square = 1 AND bottom-left-square = 1|0 (28.0)
middle-right-square = 1 AND middle-middle-square = 1 AND middle-left-square = 1|0 (28.0)
top-middle-square = 2 AND top-left-square = 2 AND top-right-square = 2|1 (31.0)
bottom-right-square = 0 AND middle-middle-square = 1|0 (13.0)
middle-right-square = 0 AND bottom-left-square = 2 AND bottom-middle-square = 2 AND bottom-right-square = 2|1 (16.0)
middle-right-square = 0|0 (31.0)
middle-right-square = 1 AND bottom-right-square = 2 AND bottom-left-square = 2 AND bottom-middle-square = 2|1 (16.0)
middle-right-square = 2 AND top-right-square = 2 AND bottom-right-square = 2|1 (38.0)
middle-right-square = 1|0 (28.0)
middle-left-square = 1 AND bottom-left-square = 1|0 (17.0)
middle-middle-square = 1 AND bottom-middle-square = 1|0 (13.0)
middle-left-square = 2 AND middle-middle-square = 2|1 (35.0)
top-right-square = 1|0 (24.0/3.0)
top-left-square = 1|1 (2.0)
|0 (2.0)


## SimpleCart Decision Tree

	* middle-middle-square=(2)|(0)
		* top-right-square=(0)|(2)
			* bottom-left-square=(0)|(2): 1(196.0/0.0)
			* bottom-left-square!=(0)|(2)
				* top-left-square=(2)|(0)
					* bottom-right-square=(0)|(2): 1(52.0/0.0)
					* bottom-right-square!=(0)|(2)
						* bottom-middle-square=(0)|(2): 1(19.0/2.0)
						* bottom-middle-square!=(0)|(2): 0(24.0/0.0)
				* top-left-square!=(2)|(0)
					* middle-left-square=(0)|(2): 1(25.0/5.0)
					* middle-left-square!=(0)|(2): 0(26.0/0.0)
		* top-right-square!=(0)|(2)
			* bottom-right-square=(2)|(0)
				* top-left-square=(0)|(2): 1(82.0/0.0)
				* top-left-square!=(0)|(2)
					* top-middle-square=(0)|(2): 1(24.0/4.0)
					* top-middle-square!=(0)|(2): 0(27.0/0.0)
			* bottom-right-square!=(2)|(0)
				* middle-right-square=(0)|(2): 1(34.0/7.0)
				* middle-right-square!=(0)|(2): 0(32.0/0.0)
	* middle-middle-square!=(2)|(0)
	* bottom-right-square=(2)
			* top-left-square=(1)|(0)
				* bottom-left-square=(2)|(0)
				* bottom-middle-square=(2): 1(31.0/1.0)
				* bottom-middle-square!=(2)
					* middle-right-square=(2): 1(14.0/5.0)
					* middle-right-square!=(2): 0(10.0/0.0)
				* bottom-left-square!=(2)|(0)
				* top-right-square=(2): 1(11.0/3.0)
				* top-right-square!=(2): 0(14.0/0.0)
			* top-left-square!=(1)|(0)
			* top-right-square=(2): 0(9.0/9.0)
			* top-right-square!=(2)
				* bottom-left-square=(2): 1(10.0/7.0)
				* bottom-left-square!=(2): 0(18.0/0.0)
	* bottom-right-square!=(2)
		* top-left-square=(2)
				* bottom-middle-square=(0)|(1)
					* top-middle-square=(2)|(0): 1(37.0/9.0)
					* top-middle-square!=(2)|(0): 0(8.0/5.0)
				* bottom-middle-square!=(0)|(1)
					* middle-right-square=(0)|(1)
						* middle-left-square=(2)|(0): 1(11.0/6.0)
						* middle-left-square!=(2)|(0): 0(7.0/2.0)
					* middle-right-square!=(0)|(1): 0(8.0/1.0)
		* top-left-square!=(2): 0(67.0/0.0)


