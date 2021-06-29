# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.653132 |
| top-right-square = 1 and middle-middle-square = 0 and bottom-left-square = 1 | 0 | 0.007055 |
| top-right-square = 0 and middle-middle-square = 1 and bottom-left-square = 1 | 0 | 0.008803 |
| middle-middle-square = 0 and bottom-left-square != 2 and top-left-square != 2 and middle-left-square != 0 | 0 | 0.026401 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square != 2 and top-left-square != 0 and top-middle-square != 2 | 0 | 0.002281 |
| top-right-square = 0 and middle-middle-square = 0 and bottom-left-square = 1 | 0 | 0.014011 |
| top-right-square = 0 and middle-middle-square = 1 and bottom-left-square = 0 | 0 | 0.019164 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square != 2 and top-left-square = 0 and bottom-right-square != 2 and middle-right-square != 2 | 0 | 0.003540 |
| middle-middle-square = 0 and bottom-left-square != 2 and top-left-square = 2 and bottom-right-square != 2 and bottom-middle-square != 0 | 0 | 0.008473 |
| top-right-square = 2 and middle-middle-square = 1 and bottom-left-square = 2 | 0 | 0.035631 |
| middle-middle-square != 0 and top-right-square!=(2) and bottom-left-square!=(2) | 0 | 0.253461 |
| middle-middle-square = 0 and bottom-left-square != 2 and top-left-square != 2 and middle-left-square != 2 | 0 | 0.011545 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square != 2 and top-left-square != 0 and top-middle-square != 0 | 0 | 0.004355 |
| top-right-square = 1 and middle-middle-square = 0 and bottom-left-square = 0 | 0 | 0.014011 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| middle-middle-square = 2 and bottom-left-square = 0 and top-right-square = 0 | 1 | 0.082822 |
| middle-middle-square = 2 and top-left-square = 0 and bottom-right-square = 0 | 1 | 0.082822 |
| middle-middle-square = 2 and top-left-square = 2 and bottom-right-square = 2 | 1 | 0.187500 |
| middle-middle-square = 2 and bottom-left-square = 2 and top-right-square = 2 | 1 | 0.189702 |
| middle-middle-square = 0 and bottom-left-square = 2 and top-right-square = 0 | 1 | 0.062696 |
| middle-middle-square = 0 and top-right-square = 2 and bottom-left-square = 0 | 1 | 0.056782 |
| middle-middle-square = 2 and bottom-left-square = 0 and top-right-square = 2 | 1 | 0.044728 |
| middle-middle-square = 2 and top-right-square = 0 and bottom-left-square = 2 | 1 | 0.047771 |
| top-left-square = 1 and bottom-right-square = 1 and middle-middle-square = 1 | 0 | 0.126801 |
| bottom-left-square = 2 and top-middle-square = 0 and middle-right-square = 0 | 1 | 0.065934 |
| top-right-square = 2 and middle-left-square = 0 and bottom-middle-square = 0 | 1 | 0.062500 |
| bottom-left-square = 2 and middle-middle-square = 0 and top-right-square = 2 | 1 | 0.055556 |
| bottom-left-square = 2 and bottom-middle-square = 2 and bottom-right-square = 2 | 1 | 0.147157 |
| top-right-square = 1 and middle-middle-square = 1 and bottom-left-square = 1 | 0 | 0.180392 |
| middle-right-square = 1 and bottom-right-square = 1 and top-right-square = 1 | 0 | 0.129167 |
| top-middle-square = 2 and middle-left-square = 0 and bottom-middle-square = 2 | 1 | 0.096447 |
| top-left-square = 1 and middle-left-square = 1 and bottom-left-square = 1 | 0 | 0.147982 |
| top-middle-square = 0 and middle-right-square = 2 and bottom-right-square = 2 | 1 | 0.121212 |
| top-middle-square = 2 and middle-right-square = 0 and top-left-square = 2 and top-right-square = 2 | 1 | 0.110429 |
| middle-left-square = 0 and top-right-square = 1 | 0 | 0.078788 |
| bottom-middle-square = 0 and middle-left-square = 2 and top-left-square = 2 | 1 | 0.142857 |
| middle-middle-square = 2 and middle-left-square = 2 and middle-right-square = 2 | 1 | 0.223529 |
| top-middle-square = 0 and bottom-left-square = 1 | 0 | 0.123810 |
| top-middle-square = 1 and bottom-middle-square = 1 and middle-middle-square = 1 | 0 | 0.264000 |
| top-left-square = 1 and top-middle-square = 1 and top-right-square = 1 | 0 | 0.192982 |
| middle-right-square = 0 and bottom-middle-square = 2 | 1 | 0.168831 |
| middle-right-square = 2 and bottom-right-square = 2 and bottom-left-square = 1 | 1 | 0.209877 |
| bottom-right-square = 0 and middle-left-square = 2 | 1 | 0.189873 |
| middle-right-square = 1 and middle-middle-square = 1 and middle-left-square = 1 | 0 | 0.397436 |
| bottom-left-square = 0 | 1 | 0.282609 |
| bottom-middle-square = 2 and top-middle-square = 2 and middle-middle-square = 2 | 1 | 0.214286 |
| middle-middle-square = 2 and bottom-right-square = 1 | 0 | 0.342105 |
| top-left-square = 1 and middle-right-square = 1 | 0 | 0.166667 |
| top-left-square = 2 and top-middle-square = 2 and top-right-square = 2 | 1 | 0.444444 |
| bottom-left-square = 1 | 0 | 0.434783 |
| middle-left-square = 2 and bottom-right-square = 1 | 1 | 0.615385 |
| middle-left-square = 1 | 0 | 0.380952 |
|  | 1 | 0.833333 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| middle-middle-square = 1 and top-right-square = 1 and bottom-left-square = 1 | 0 | 0.075534 |
| middle-middle-square = 1 and top-left-square = 1 and bottom-right-square = 1 | 0 | 0.072488 |
| middle-middle-square = 1 and middle-right-square = 1 and middle-left-square = 1 | 0 | 0.053782 |
| bottom-left-square = 1 and top-left-square = 1 and middle-left-square = 1 | 0 | 0.055369 |
| middle-left-square = 2 and middle-middle-square = 0 and bottom-left-square = 1 and bottom-right-square = 1 | 0 | 0.017452 |
| top-right-square = 1 and top-left-square = 1 and top-middle-square = 1 | 0 | 0.055369 |
| bottom-right-square = 1 and top-right-square = 1 and middle-right-square = 1 | 0 | 0.050590 |
| bottom-middle-square = 1 and middle-middle-square = 1 and top-middle-square = 1 | 0 | 0.056951 |
| bottom-left-square = 1 and bottom-right-square = 1 and bottom-middle-square = 1 | 0 | 0.037607 |
|  | 1 | 0.974048 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

top-right-square|middle-middle-square|bottom-left-square|target
---|---|---|---
2|2|2|1
0|2|2|1
1|2|2|1
2|1|2|0
0|1|2|1
1|1|2|1
0|0|2|1
1|2|1|1
2|0|2|1
2|2|1|1
1|0|2|1
0|2|1|1
0|1|1|0
2|1|1|1
1|1|1|0
1|0|1|0
2|2|0|1
0|2|0|1
2|0|1|1
1|2|0|1
0|0|1|0
0|1|0|0
1|1|0|0
2|1|0|1
2|0|0|1
1|0|0|0

## JRip

Decision list:

rules | predicted class
---|---
(middle-middle-square = 1) and (top-right-square = 1) and (bottom-left-square = 1)|0 (46.0/0.0)
(middle-middle-square = 1) and (top-left-square = 1) and (bottom-right-square = 1)|0 (44.0/0.0)
(middle-middle-square = 1) and (middle-right-square = 1) and (middle-left-square = 1)|0 (32.0/0.0)
(bottom-left-square = 1) and (top-left-square = 1) and (middle-left-square = 1)|0 (33.0/0.0)
(middle-left-square = 2) and (middle-middle-square = 0) and (bottom-left-square = 1) and (bottom-right-square = 1)|0 (10.0/0.0)
(top-right-square = 1) and (top-left-square = 1) and (top-middle-square = 1)|0 (33.0/0.0)
(bottom-right-square = 1) and (top-right-square = 1) and (middle-right-square = 1)|0 (30.0/0.0)
(bottom-middle-square = 1) and (middle-middle-square = 1) and (top-middle-square = 1)|0 (34.0/0.0)
(bottom-left-square = 1) and (bottom-right-square = 1) and (bottom-middle-square = 1)|0 (22.0/0.0)
|1 (578.0/15.0)


## PART

Decision list:

rules | predicted class
---|---
middle-middle-square = 2 AND bottom-left-square = 0 AND top-right-square = 0|1 (27.0)
middle-middle-square = 2 AND top-left-square = 0 AND bottom-right-square = 0|1 (27.0)
middle-middle-square = 2 AND top-left-square = 2 AND bottom-right-square = 2|1 (69.0)
middle-middle-square = 2 AND bottom-left-square = 2 AND top-right-square = 2|1 (70.0)
middle-middle-square = 0 AND bottom-left-square = 2 AND top-right-square = 0|1 (20.0)
middle-middle-square = 0 AND top-right-square = 2 AND bottom-left-square = 0|1 (18.0)
middle-middle-square = 2 AND bottom-left-square = 0 AND top-right-square = 2|1 (14.0)
middle-middle-square = 2 AND top-right-square = 0 AND bottom-left-square = 2|1 (15.0)
top-left-square = 1 AND bottom-right-square = 1 AND middle-middle-square = 1|0 (44.0)
bottom-left-square = 2 AND top-middle-square = 0 AND middle-right-square = 0|1 (18.0)
top-right-square = 2 AND middle-left-square = 0 AND bottom-middle-square = 0|1 (17.0)
bottom-left-square = 2 AND middle-middle-square = 0 AND top-right-square = 2|1 (15.0)
bottom-left-square = 2 AND bottom-middle-square = 2 AND bottom-right-square = 2|1 (44.0)
top-right-square = 1 AND middle-middle-square = 1 AND bottom-left-square = 1|0 (46.0)
middle-right-square = 1 AND bottom-right-square = 1 AND top-right-square = 1|0 (31.0)
top-middle-square = 2 AND middle-left-square = 0 AND bottom-middle-square = 2|1 (19.0)
top-left-square = 1 AND middle-left-square = 1 AND bottom-left-square = 1|0 (33.0)
top-middle-square = 0 AND middle-right-square = 2 AND bottom-right-square = 2|1 (20.0)
top-middle-square = 2 AND middle-right-square = 0 AND top-left-square = 2 AND top-right-square = 2|1 (18.0)
middle-left-square = 0 AND top-right-square = 1|0 (13.0)
bottom-middle-square = 0 AND middle-left-square = 2 AND top-left-square = 2|1 (22.0)
middle-middle-square = 2 AND middle-left-square = 2 AND middle-right-square = 2|1 (38.0)
top-middle-square = 0 AND bottom-left-square = 1|0 (13.0)
top-middle-square = 1 AND bottom-middle-square = 1 AND middle-middle-square = 1|0 (33.0)
top-left-square = 1 AND top-middle-square = 1 AND top-right-square = 1|0 (22.0)
middle-right-square = 0 AND bottom-middle-square = 2|1 (13.0)
middle-right-square = 2 AND bottom-right-square = 2 AND bottom-left-square = 1|1 (17.0)
bottom-right-square = 0 AND middle-left-square = 2|1 (15.0)
middle-right-square = 1 AND middle-middle-square = 1 AND middle-left-square = 1|0 (31.0)
bottom-left-square = 0|1 (13.0)
bottom-middle-square = 2 AND top-middle-square = 2 AND middle-middle-square = 2|1 (9.0)
middle-middle-square = 2 AND bottom-right-square = 1|0 (13.0)
top-left-square = 1 AND middle-right-square = 1|0 (5.0)
top-left-square = 2 AND top-middle-square = 2 AND top-right-square = 2|1 (12.0)
bottom-left-square = 1|0 (10.0)
middle-left-square = 2 AND bottom-right-square = 1|1 (8.0)
middle-left-square = 1|0 (6.0/2.0)
|1 (4.0/1.0)


## SimpleCart Decision Tree

	* middle-middle-square=(2)|(0)
		* bottom-left-square=(0)|(2)
			* top-right-square=(0)|(2): 1(197.0/0.0)
			* top-right-square!=(0)|(2)
				* top-left-square=(2)|(0)
					* bottom-right-square=(0)|(2): 1(54.0/0.0)
					* bottom-right-square!=(0)|(2)
						* middle-right-square=(0)|(2): 1(19.0/1.0)
						* middle-right-square!=(0)|(2): 0(22.0/0.0)
				* top-left-square!=(2)|(0)
					* top-middle-square=(0)|(2): 1(25.0/5.0)
					* top-middle-square!=(0)|(2): 0(28.0/0.0)
		* bottom-left-square!=(0)|(2)
			* top-left-square=(0)|(2)
				* bottom-right-square=(0)|(2): 1(81.0/0.0)
				* bottom-right-square!=(0)|(2)
					* bottom-middle-square=(0)|(2): 1(22.0/5.0)
					* bottom-middle-square!=(0)|(2): 0(27.0/0.0)
			* top-left-square!=(0)|(2)
				* middle-left-square=(0)|(2): 1(30.0/7.0)
				* middle-left-square!=(0)|(2): 0(30.0/0.0)
	* middle-middle-square!=(2)|(0)
	* top-right-square=(2)
		* top-left-square=(2)
			* top-middle-square=(2): 1(35.0/0.0)
			* top-middle-square!=(2): 0(23.0/12.0)
		* top-left-square!=(2)
			* bottom-right-square=(2)
				* middle-right-square=(2): 1(29.0/0.0)
				* middle-right-square!=(2): 0(13.0/6.0)
			* bottom-right-square!=(2): 0(36.0/0.0)
	* top-right-square!=(2)
		* bottom-left-square=(2)
				* middle-right-square=(0)|(1)
					* middle-left-square=(2)|(0): 1(36.0/8.0)
					* middle-left-square!=(2)|(0)
					* middle-right-square=(0): 1(5.0/0.0)
					* middle-right-square!=(0): 0(8.0/0.0)
				* middle-right-square!=(0)|(1)
					* top-left-square=(2)|(0)
						* bottom-middle-square=(0)|(2): 1(8.0/1.0)
						* bottom-middle-square!=(0)|(2): 0(7.0/3.0)
					* top-left-square!=(2)|(0): 0(11.0/1.0)
		* bottom-left-square!=(2): 0(67.0/0.0)


