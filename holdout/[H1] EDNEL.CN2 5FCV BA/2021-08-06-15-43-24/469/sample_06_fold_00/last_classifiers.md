# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.185118 |
| Ethnic = 2 | 5 | 0.041050 |
| Ethnic = 1 | 1 | 0.031995 |
| Ethnic = 0 | 2 | 0.010557 |
| Ethnic = 1 and DMFT.Begin = 5 and DMFT.End = 3 | 4 | 0.005835 |
| Ethnic = 2 and DMFT.Begin = 5 and Gender = 0 | 1 | 0.003655 |
| Ethnic = 1 and DMFT.Begin = 2 and DMFT.End = 2 | 4 | 0.003532 |
| Ethnic = 1 and DMFT.Begin = 5 and DMFT.End = 2 | 2 | 0.002795 |
| Ethnic = 1 and DMFT.Begin = 6 and Gender = 0 | 4 | 0.002956 |
| Ethnic = 2 and DMFT.Begin = 3 and DMFT.End = 0 | 4 | 0.004396 |
| Ethnic = 2 and DMFT.Begin = 6 and Gender = 1 | 2 | 0.002512 |
| Ethnic = 1 and DMFT.Begin = 7 and Gender = 1 | 0 | 0.001965 |
| Ethnic = 2 and DMFT.Begin = 6 and Gender = 0 | 0 | 0.002693 |
| Ethnic = 1 and DMFT.Begin = 0 and DMFT.End = 1 | 0 | 0.003169 |
| Ethnic = 0 and DMFT.Begin = 8 | 4 | 0.003297 |
| Ethnic = 2 and DMFT.Begin = 2 and DMFT.End = 0 | 0 | 0.001965 |
| Ethnic = 0 and DMFT.Begin = 0 and Gender = 1 | 0 | 0.002344 |
| Ethnic = 1 and DMFT.Begin = 4 and DMFT.End = 0 | 2 | 0.002451 |
| Ethnic = 0 and DMFT.Begin = 7 | 4 | 0.002198 |
| Ethnic = 1 and DMFT.Begin = 4 and DMFT.End = 1 | 4 | 0.002924 |
| Ethnic = 0 and DMFT.Begin = 2 | 0 | 0.001449 |
| Ethnic = 2 and DMFT.Begin = 0 and DMFT.End = 2 | 0 | 0.002880 |
| Ethnic = 2 and DMFT.Begin = 7 and DMFT.End = 3 | 2 | 0.001452 |
| Ethnic = 2 and DMFT.Begin = 7 and DMFT.End = 5 | 2 | 0.002795 |
| Ethnic = 2 and DMFT.Begin = 8 and Gender = 1 | 2 | 0.002183 |
| Ethnic = 1 and DMFT.Begin = 3 and DMFT.End = 2 | 5 | 0.002141 |
| Ethnic = 2 and DMFT.Begin = 4 and DMFT.End = 3 | 2 | 0.001969 |
| Ethnic = 2 and DMFT.Begin = 4 and DMFT.End = 5 | 4 | 0.002193 |
| Ethnic = 2 and DMFT.Begin = 7 and DMFT.End = 6 | 4 | 0.001099 |
| Ethnic = 1 and DMFT.Begin = 1 and DMFT.End = 1 | 0 | 0.001449 |
| Ethnic = 1 and DMFT.Begin = 2 and DMFT.End = 1 | 0 | 0.001449 |
| Ethnic = 1 and DMFT.Begin = 0 and DMFT.End = 3 | 0 | 0.002160 |
| Ethnic = 1 and DMFT.Begin = 3 and DMFT.End = 4 | 0 | 0.002160 |
| Ethnic = 2 and DMFT.Begin = 4 and DMFT.End = 0 | 2 | 0.001739 |
| Ethnic = 2 and DMFT.Begin = 7 and DMFT.End = 0 | 2 | 0.001085 |
| Ethnic = 2 and DMFT.Begin = 2 and DMFT.End = 3 | 1 | 0.001739 |
| Ethnic = 2 and DMFT.Begin = 4 and DMFT.End = 1 | 1 | 0.001452 |
| Ethnic = 2 and DMFT.Begin = 0 and DMFT.End = 1 | 1 | 0.001452 |
| Ethnic = 2 and DMFT.Begin = 3 and DMFT.End = 2 | 1 | 0.001248 |
| Ethnic = 2 and DMFT.Begin = 2 and DMFT.End = 4 | 0 | 0.001735 |
| Ethnic = 1 and DMFT.Begin = 3 and DMFT.End = 1 | 0 | 0.001092 |
| Ethnic = 2 and DMFT.Begin = 8 and Gender = 0 | 0 | 0.001449 |
| Ethnic = 2 and DMFT.Begin = 3 and DMFT.End = 1 | 0 | 0.001449 |
| Ethnic = 1 and DMFT.Begin = 4 and DMFT.End = 4 | 4 | 0.001099 |
| Ethnic = 2 and DMFT.Begin = 0 and DMFT.End = 3 | 0 | 0.001082 |
| Ethnic = 1 and DMFT.Begin = 0 and DMFT.End = 2 | 0 | 0.000543 |
| Ethnic = 2 and DMFT.Begin = 3 and DMFT.End = 3 | 0 | 0.000543 |
| Ethnic = 1 and DMFT.Begin = 4 and DMFT.End = 2 | 0 | 0.000543 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| DMFT.End != 6 and DMFT.Begin != 8 and DMFT.End != 5 and DMFT.End = 3 and DMFT.Begin != 6 and Gender = 0 | 1 | 0.007391 |
| DMFT.End != 6 and DMFT.Begin != 8 and DMFT.End != 5 and DMFT.Begin = 5 | 3 | 0.012162 |
| DMFT.Begin = 8 | 1 | 0.004801 |
| DMFT.End != 6 and DMFT.End = 5 | 4 | 0.006601 |
| Ethnic = 2 and DMFT.End = 3 | 2 | 0.006579 |
| Ethnic = 2 and DMFT.Begin = 1 | 2 | 0.001018 |
| Ethnic = 2 and DMFT.Begin != 6 and DMFT.Begin = 2 and Gender != 0 | 5 | 0.010949 |
| DMFT.End != 6 and DMFT.End != 3 and DMFT.Begin = 6 | 0 | 0.006943 |
| DMFT.End != 6 and DMFT.End != 3 and DMFT.Begin != 2 and Ethnic = 0 and DMFT.End = 0 | 0 | 0.006804 |
| DMFT.End != 6 and DMFT.End != 3 and DMFT.Begin = 2 | 0 | 0.007900 |
| DMFT.End != 6 and Ethnic != 0 and DMFT.End != 4 and DMFT.Begin != 7 and DMFT.Begin != 1 and Ethnic != 1 and DMFT.End != 1 and DMFT.Begin != 3 and Gender = 0 | 5 | 0.014202 |
| DMFT.End != 6 and Ethnic != 0 and DMFT.End != 4 and DMFT.Begin != 7 and DMFT.Begin != 1 and DMFT.End = 1 | 1 | 0.005257 |
| DMFT.End != 6 and Ethnic = 0 | 2 | 0.016293 |
| DMFT.End != 6 and DMFT.End != 4 and DMFT.Begin != 7 and Ethnic != 1 and DMFT.Begin != 3 | 3 | 0.053908 |
| DMFT.End != 6 and DMFT.End != 4 and DMFT.Begin != 7 and Ethnic = 1 and Gender != 0 and DMFT.Begin != 0 | 1 | 0.012642 |
| DMFT.End != 6 and DMFT.End != 4 and Gender = 0 and DMFT.Begin != 0 and Ethnic = 1 | 3 | 0.010675 |
| DMFT.End != 6 and DMFT.End != 4 and Gender != 0 | 0 | 0.031590 |
| Gender = 0 and DMFT.Begin != 0 | 5 | 0.025064 |
| DMFT.Begin != 0 | 0 | 0.027075 |
|  | 1 | 0.183206 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Ethnic = 2 and DMFT.Begin = 2 and Gender = 1 and DMFT.End = 2 | 5 | 0.006383 |
| Ethnic = 2 and DMFT.Begin = 2 and DMFT.End = 1 | 5 | 0.005353 |
| Ethnic = 2 and DMFT.End = 2 and Gender = 1 and DMFT.Begin = 6 | 5 | 0.006383 |
| Ethnic = 2 and DMFT.End = 6 and Gender = 0 | 5 | 0.006809 |
| Ethnic = 2 and DMFT.Begin = 0 and DMFT.End = 1 and Gender = 1 | 5 | 0.004264 |
| Ethnic = 2 and Gender = 0 and DMFT.End = 0 and DMFT.Begin = 0 | 5 | 0.005072 |
| Ethnic = 2 and DMFT.End = 2 | 5 | 0.004192 |
| Ethnic = 2 and DMFT.Begin = 1 and DMFT.End = 0 and Gender = 0 | 5 | 0.002141 |
| DMFT.End = 0 and DMFT.Begin = 6 and Ethnic = 1 and Gender = 0 | 0 | 0.004651 |
| DMFT.End = 0 and Ethnic = 0 and Gender = 1 | 0 | 0.006097 |
| DMFT.Begin = 0 and Gender = 1 and Ethnic = 1 and DMFT.End = 1 | 0 | 0.005328 |
| DMFT.End = 0 and Ethnic = 2 and Gender = 0 and DMFT.Begin = 8 | 0 | 0.004651 |
| DMFT.End = 0 and Ethnic = 2 and DMFT.Begin = 3 and Gender = 1 | 0 | 0.002336 |
| DMFT.End = 0 and DMFT.Begin = 0 and Gender = 1 and Ethnic = 1 | 0 | 0.003940 |
| DMFT.End = 0 and Ethnic = 2 and Gender = 0 and DMFT.Begin = 2 | 0 | 0.001874 |
| DMFT.Begin = 0 and Gender = 1 and DMFT.End = 3 | 0 | 0.004651 |
| DMFT.End = 0 and DMFT.Begin = 0 and Gender = 1 | 0 | 0.001685 |
| Ethnic = 1 and DMFT.End = 3 and DMFT.Begin = 4 and Gender = 1 | 1 | 0.003359 |
| Ethnic = 1 and DMFT.End = 3 and DMFT.Begin = 8 | 1 | 0.003359 |
| Ethnic = 1 and DMFT.End = 3 and Gender = 0 | 1 | 0.005288 |
| DMFT.Begin = 5 and Ethnic = 2 and DMFT.End = 3 and Gender = 0 | 1 | 0.002525 |
| Ethnic = 1 and DMFT.Begin = 8 and DMFT.End = 2 and Gender = 1 | 1 | 0.005025 |
| DMFT.End = 5 and DMFT.Begin = 8 and Gender = 0 | 1 | 0.005653 |
| Ethnic = 1 and DMFT.End = 0 | 1 | 0.012401 |
| DMFT.Begin = 5 and Ethnic = 2 and DMFT.End = 3 | 1 | 0.001692 |
| DMFT.End = 4 and Ethnic = 0 | 1 | 0.002525 |
| Ethnic = 2 and DMFT.Begin = 8 and DMFT.End = 0 | 2 | 0.005510 |
| DMFT.End = 3 and Ethnic = 0 and DMFT.Begin = 4 | 2 | 0.003683 |
| Ethnic = 2 and DMFT.Begin = 7 and Gender = 0 and DMFT.End = 5 | 2 | 0.005510 |
| Gender = 1 and Ethnic = 0 and DMFT.Begin = 6 | 2 | 0.006198 |
| Ethnic = 2 and DMFT.End = 3 and Gender = 1 and DMFT.Begin = 4 | 2 | 0.004155 |
| Ethnic = 2 and DMFT.Begin = 6 and DMFT.End = 4 and Gender = 1 | 2 | 0.005510 |
| DMFT.End = 2 and DMFT.Begin = 5 and Gender = 1 | 2 | 0.002222 |
| Ethnic = 0 and Gender = 1 | 2 | 0.006728 |
| Ethnic = 2 and DMFT.End = 3 | 2 | 0.003826 |
| DMFT.End = 6 and DMFT.Begin = 8 | 4 | 0.015244 |
| DMFT.End = 5 and DMFT.Begin = 4 | 4 | 0.006154 |
| DMFT.Begin = 1 and Gender = 1 | 4 | 0.003175 |
| Ethnic = 1 and DMFT.Begin = 4 and DMFT.End = 1 | 4 | 0.004115 |
| DMFT.End = 5 and DMFT.Begin = 6 and Ethnic = 1 | 4 | 0.006923 |
| DMFT.Begin = 5 and DMFT.End = 3 and Gender = 1 | 4 | 0.009615 |
| DMFT.End = 2 and DMFT.Begin = 2 and Gender = 0 and Ethnic = 1 | 4 | 0.003096 |
| Ethnic = 0 | 4 | 0.012221 |
| DMFT.Begin = 1 | 4 | 0.003265 |
| DMFT.End = 6 | 4 | 0.003993 |
| DMFT.End = 2 and DMFT.Begin = 2 | 4 | 0.000913 |
| DMFT.Begin = 0 and DMFT.End = 1 | 4 | 0.003870 |
| DMFT.End = 0 and DMFT.Begin = 3 | 4 | 0.008573 |
|  | 3 | 0.281768 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

ethnic|target
---|---
0|2
1|1
2|5

## JRip

Decision list:

rules | predicted class
---|---
(Ethnic = 2) and (DMFT.Begin = 2) and (Gender = 1) and (DMFT.End = 2)|5 (3.0/0.0)
(Ethnic = 2) and (DMFT.Begin = 2) and (DMFT.End = 1)|5 (10.0/5.0)
(Ethnic = 2) and (DMFT.End = 2) and (Gender = 1) and (DMFT.Begin = 6)|5 (3.0/0.0)
(Ethnic = 2) and (DMFT.End = 6) and (Gender = 0)|5 (5.0/1.0)
(Ethnic = 2) and (DMFT.Begin = 0) and (DMFT.End = 1) and (Gender = 1)|5 (2.0/0.0)
(Ethnic = 2) and (Gender = 0) and (DMFT.End = 0) and (DMFT.Begin = 0)|5 (21.0/14.0)
(Ethnic = 2) and (DMFT.End = 2)|5 (34.0/26.0)
(Ethnic = 2) and (DMFT.Begin = 1) and (DMFT.End = 0) and (Gender = 0)|5 (4.0/2.0)
(DMFT.End = 0) and (DMFT.Begin = 6) and (Ethnic = 1) and (Gender = 0)|0 (2.0/0.0)
(DMFT.End = 0) and (Ethnic = 0) and (Gender = 1)|0 (19.0/12.0)
(DMFT.Begin = 0) and (Gender = 1) and (Ethnic = 1) and (DMFT.End = 1)|0 (7.0/3.0)
(DMFT.End = 0) and (Ethnic = 2) and (Gender = 0) and (DMFT.Begin = 8)|0 (2.0/0.0)
(DMFT.End = 0) and (Ethnic = 2) and (DMFT.Begin = 3) and (Gender = 1)|0 (4.0/2.0)
(DMFT.End = 0) and (DMFT.Begin = 0) and (Gender = 1) and (Ethnic = 1)|0 (15.0/10.0)
(DMFT.End = 0) and (Ethnic = 2) and (Gender = 0) and (DMFT.Begin = 2)|0 (5.0/3.0)
(DMFT.Begin = 0) and (Gender = 1) and (DMFT.End = 3)|0 (2.0/0.0)
(DMFT.End = 0) and (DMFT.Begin = 0) and (Gender = 1)|0 (19.0/14.0)
(Ethnic = 1) and (DMFT.End = 3) and (DMFT.Begin = 4) and (Gender = 1)|1 (3.0/1.0)
(Ethnic = 1) and (DMFT.End = 3) and (DMFT.Begin = 8)|1 (3.0/1.0)
(Ethnic = 1) and (DMFT.End = 3) and (Gender = 0)|1 (12.0/7.0)
(DMFT.Begin = 5) and (Ethnic = 2) and (DMFT.End = 3) and (Gender = 0)|1 (4.0/2.0)
(Ethnic = 1) and (DMFT.Begin = 8) and (DMFT.End = 2) and (Gender = 1)|1 (2.0/0.0)
(DMFT.End = 5) and (DMFT.Begin = 8) and (Gender = 0)|1 (4.0/1.0)
(Ethnic = 1) and (DMFT.End = 0)|1 (38.0/29.0)
(DMFT.Begin = 5) and (Ethnic = 2) and (DMFT.End = 3)|1 (4.0/2.0)
(DMFT.End = 4) and (Ethnic = 0)|1 (4.0/2.0)
(Ethnic = 2) and (DMFT.Begin = 8) and (DMFT.End = 0)|2 (2.0/0.0)
(DMFT.End = 3) and (Ethnic = 0) and (DMFT.Begin = 4)|2 (3.0/1.0)
(Ethnic = 2) and (DMFT.Begin = 7) and (Gender = 0) and (DMFT.End = 5)|2 (2.0/0.0)
(Gender = 1) and (Ethnic = 0) and (DMFT.Begin = 6)|2 (3.0/1.0)
(Ethnic = 2) and (DMFT.End = 3) and (Gender = 1) and (DMFT.Begin = 4)|2 (6.0/3.0)
(Ethnic = 2) and (DMFT.Begin = 6) and (DMFT.End = 4) and (Gender = 1)|2 (2.0/0.0)
(DMFT.End = 2) and (DMFT.Begin = 5) and (Gender = 1)|2 (3.0/1.0)
(Ethnic = 0) and (Gender = 1)|2 (21.0/14.0)
(Ethnic = 2) and (DMFT.End = 3)|2 (31.0/24.0)
(DMFT.End = 6) and (DMFT.Begin = 8)|4 (4.0/0.0)
(DMFT.End = 5) and (DMFT.Begin = 4)|4 (2.0/0.0)
(DMFT.Begin = 1) and (Gender = 1)|4 (9.0/5.0)
(Ethnic = 1) and (DMFT.Begin = 4) and (DMFT.End = 1)|4 (3.0/1.0)
(DMFT.End = 5) and (DMFT.Begin = 6) and (Ethnic = 1)|4 (4.0/1.0)
(DMFT.Begin = 5) and (DMFT.End = 3) and (Gender = 1)|4 (5.0/2.0)
(DMFT.End = 2) and (DMFT.Begin = 2) and (Gender = 0) and (Ethnic = 1)|4 (4.0/2.0)
(Ethnic = 0)|4 (29.0/22.0)
(DMFT.Begin = 1)|4 (9.0/6.0)
(DMFT.End = 6)|4 (5.0/3.0)
(DMFT.End = 2) and (DMFT.Begin = 2)|4 (6.0/4.0)
(DMFT.Begin = 0) and (DMFT.End = 1)|4 (8.0/6.0)
(DMFT.End = 0) and (DMFT.Begin = 3)|4 (4.0/2.0)
|3 (155.0/120.0)


## PART

Decision list:

rules | predicted class
---|---
DMFT.End != 6 AND DMFT.Begin != 8 AND DMFT.End != 5 AND DMFT.End = 3 AND DMFT.Begin != 6 AND Gender = 0|1 (20.0/11.0)
DMFT.End != 6 AND DMFT.Begin != 8 AND DMFT.End != 5 AND DMFT.Begin = 5|3 (23.0/16.0)
DMFT.Begin = 8|1 (16.0/10.0)
DMFT.End != 6 AND DMFT.End = 5|4 (16.0/9.0)
Ethnic = 2 AND DMFT.End = 3|2 (10.0/7.0)
Ethnic = 2 AND DMFT.Begin = 1|2 (9.0/6.0)
Ethnic = 2 AND DMFT.Begin != 6 AND DMFT.Begin = 2 AND Gender != 0|5 (9.0/4.0)
DMFT.End != 6 AND DMFT.End != 3 AND DMFT.Begin = 6|0 (17.0/10.0)
DMFT.End != 6 AND DMFT.End != 3 AND DMFT.Begin != 2 AND Ethnic = 0 AND DMFT.End = 0|0 (16.0/9.0)
DMFT.End != 6 AND DMFT.End != 3 AND DMFT.Begin = 2|0 (15.0/11.0)
DMFT.End != 6 AND Ethnic != 0 AND DMFT.End != 4 AND DMFT.Begin != 7 AND DMFT.Begin != 1 AND Ethnic != 1 AND DMFT.End != 1 AND DMFT.Begin != 3 AND Gender = 0|5 (15.0/8.0)
DMFT.End != 6 AND Ethnic != 0 AND DMFT.End != 4 AND DMFT.Begin != 7 AND DMFT.Begin != 1 AND DMFT.End = 1|1 (19.0/14.0)
DMFT.End != 6 AND Ethnic = 0|2 (14.0/10.0)
DMFT.End != 6 AND DMFT.End != 4 AND DMFT.Begin != 7 AND Ethnic != 1 AND DMFT.Begin != 3|3 (13.0/8.0)
DMFT.End != 6 AND DMFT.End != 4 AND DMFT.Begin != 7 AND Ethnic = 1 AND Gender != 0 AND DMFT.Begin != 0|1 (13.0/10.0)
DMFT.End != 6 AND DMFT.End != 4 AND Gender = 0 AND DMFT.Begin != 0 AND Ethnic = 1|3 (14.0/9.0)
DMFT.End != 6 AND DMFT.End != 4 AND Gender != 0|0 (14.0/8.0)
Gender = 0 AND DMFT.Begin != 0|5 (10.0/5.0)
DMFT.Begin != 0|0 (8.0/6.0)
|1 (5.0/3.0)


## J48 Decision Tree

* Ethnic = 0
	* DMFT.Begin = 0
		* Gender = 0: 3 (10.0/7.0)
		* Gender = 1: 0 (15.0/11.0)
	* DMFT.Begin = 1: 2 (10.0/7.0)
	* DMFT.Begin = 2: 0 (6.0/4.0)
	* DMFT.Begin = 3: 2 (7.0/5.0)
	* DMFT.Begin = 4: 2 (10.0/6.0)
	* DMFT.Begin = 5: 2 (8.0/5.0)
	* DMFT.Begin = 6: 2 (6.0/3.0)
	* DMFT.Begin = 7: 4 (4.0/2.0)
	* DMFT.Begin = 8: 4 (6.0/3.0)
* Ethnic = 1
	* DMFT.Begin = 0
		* DMFT.End = 0
			* Gender = 0: 1 (13.0/9.0)
			* Gender = 1: 1 (15.0/9.0)
		* DMFT.End = 1: 0 (11.0/7.0)
		* DMFT.End = 2: 0 (4.0/3.0)
		* DMFT.End = 3: 0 (1.0)
		* DMFT.End = 4: 1 (1.0)
		* DMFT.End = 5: 1 (1.0)
		* DMFT.End = 6: 0 (0.0)
	* DMFT.Begin = 1
		* DMFT.End = 0: 3 (10.0/7.0)
		* DMFT.End = 1: 0 (6.0/4.0)
		* DMFT.End = 2: 4 (0.0)
		* DMFT.End = 3: 1 (2.0/1.0)
		* DMFT.End = 4: 4 (0.0)
		* DMFT.End = 5: 4 (0.0)
		* DMFT.End = 6: 4 (0.0)
	* DMFT.Begin = 2
		* DMFT.End = 0: 1 (2.0/1.0)
		* DMFT.End = 1: 0 (6.0/4.0)
		* DMFT.End = 2: 4 (10.0/6.0)
		* DMFT.End = 3: 4 (0.0)
		* DMFT.End = 4: 3 (1.0)
		* DMFT.End = 5: 4 (0.0)
		* DMFT.End = 6: 4 (0.0)
	* DMFT.Begin = 3
		* DMFT.End = 0: 1 (3.0/2.0)
		* DMFT.End = 1: 0 (8.0/6.0)
		* DMFT.End = 2: 5 (4.0/2.0)
		* DMFT.End = 3: 1 (6.0/4.0)
		* DMFT.End = 4: 0 (1.0)
		* DMFT.End = 5: 1 (0.0)
		* DMFT.End = 6: 1 (0.0)
	* DMFT.Begin = 4
		* DMFT.End = 0: 2 (8.0/5.0)
		* DMFT.End = 1: 4 (3.0/1.0)
		* DMFT.End = 2: 0 (4.0/3.0)
		* DMFT.End = 3: 1 (8.0/4.0)
		* DMFT.End = 4: 4 (2.0/1.0)
		* DMFT.End = 5: 1 (0.0)
		* DMFT.End = 6: 1 (0.0)
	* DMFT.Begin = 5
		* DMFT.End = 0: 1 (1.0)
		* DMFT.End = 1: 1 (4.0/3.0)
		* DMFT.End = 2: 2 (7.0/4.0)
		* DMFT.End = 3: 4 (6.0/2.0)
		* DMFT.End = 4: 3 (4.0/2.0)
		* DMFT.End = 5: 1 (1.0)
		* DMFT.End = 6: 4 (0.0)
	* DMFT.Begin = 6
		* Gender = 0: 4 (12.0/8.0)
		* Gender = 1: 1 (12.0/9.0)
	* DMFT.Begin = 7
		* Gender = 0: 3 (7.0/4.0)
		* Gender = 1: 0 (10.0/7.0)
	* DMFT.Begin = 8: 1 (10.0/5.0)
* Ethnic = 2
	* DMFT.Begin = 0
		* DMFT.End = 0
			* Gender = 0: 5 (21.0/14.0)
			* Gender = 1: 3 (19.0/11.0)
		* DMFT.End = 1: 1 (6.0/4.0)
		* DMFT.End = 2: 0 (3.0/1.0)
		* DMFT.End = 3: 0 (2.0/1.0)
		* DMFT.End = 4: 3 (0.0)
		* DMFT.End = 5: 3 (0.0)
		* DMFT.End = 6: 3 (0.0)
	* DMFT.Begin = 1
		* Gender = 0: 5 (14.0/10.0)
		* Gender = 1: 3 (8.0/5.0)
	* DMFT.Begin = 2
		* DMFT.End = 0: 0 (10.0/7.0)
		* DMFT.End = 1: 5 (10.0/5.0)
		* DMFT.End = 2: 5 (9.0/4.0)
		* DMFT.End = 3: 1 (5.0/3.0)
		* DMFT.End = 4: 0 (5.0/3.0)
		* DMFT.End = 5: 5 (0.0)
		* DMFT.End = 6: 5 (0.0)
	* DMFT.Begin = 3
		* DMFT.End = 0: 4 (8.0/4.0)
		* DMFT.End = 1: 0 (6.0/4.0)
		* DMFT.End = 2: 1 (7.0/5.0)
		* DMFT.End = 3: 0 (4.0/3.0)
		* DMFT.End = 4: 5 (3.0/1.0)
		* DMFT.End = 5: 5 (1.0)
		* DMFT.End = 6: 0 (0.0)
	* DMFT.Begin = 4
		* DMFT.End = 0: 2 (5.0/3.0)
		* DMFT.End = 1: 1 (6.0/4.0)
		* DMFT.End = 2: 3 (6.0/4.0)
		* DMFT.End = 3: 2 (10.0/7.0)
		* DMFT.End = 4: 3 (5.0/3.0)
		* DMFT.End = 5: 4 (1.0)
		* DMFT.End = 6: 2 (0.0)
	* DMFT.Begin = 5
		* Gender = 0: 1 (15.0/10.0)
		* Gender = 1: 3 (13.0/9.0)
	* DMFT.Begin = 6
		* Gender = 0: 0 (13.0/9.0)
		* Gender = 1: 2 (14.0/10.0)
	* DMFT.Begin = 7
		* DMFT.End = 0: 2 (2.0/1.0)
		* DMFT.End = 1: 3 (3.0/2.0)
		* DMFT.End = 2: 5 (1.0)
		* DMFT.End = 3: 2 (6.0/4.0)
		* DMFT.End = 4: 2 (0.0)
		* DMFT.End = 5: 2 (7.0/4.0)
		* DMFT.End = 6: 4 (2.0/1.0)
	* DMFT.Begin = 8
		* Gender = 0: 0 (6.0/4.0)
		* Gender = 1: 2 (9.0/6.0)


