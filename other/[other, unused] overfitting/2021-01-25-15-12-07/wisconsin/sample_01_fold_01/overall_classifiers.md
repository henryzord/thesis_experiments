# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 2 | 0.656051 |
| CellSize < 3.5 and BareNuclei >= 3.5 and CellSize >= 1.5 | 4 | 0.049269 |
| CellSize > 2.5 and CellSize > 3.5 and BlandChromatin <= 4.5 and ClumpThickness <= 6.5 and ClumpThickness <= 3.5 | 4 | 0.011990 |
| CellSize > 2.5 and CellSize > 3.5 and BlandChromatin > 4.5 | 4 | 0.242701 |
| CellSize > 2.5 and CellSize <= 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.013952 |
| CellSize > 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.059435 |
| CellSize > 3.5 and BareNuclei > 1.5 and BareNuclei <= 2.5 | 4 | 0.019048 |
| CellSize > 3.5 and BareNuclei > 5.5 | 4 | 0.238571 |
| CellSize <= 2.5 and ClumpThickness > 5.5 and BareNuclei > 2 | 4 | 0.016706 |
| CellSize > 2.5 and CellSize > 3.5 and BlandChromatin <= 4.5 and ClumpThickness > 6.5 | 4 | 0.072138 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize <= 2 and ClumpThickness <= 5 and BareNuclei <= 2 | 2 | 0.607273 |
| CellShape > 2 and BareNuclei > 2 and ClumpThickness > 6 | 4 | 0.585106 |
| BlandChromatin > 3 and BareNuclei > 8 | 4 | 0.390625 |
| NormalNucleoli <= 2 and CellSize <= 3 and BareNuclei <= 3 | 2 | 0.416667 |
| CellShape > 2 and BlandChromatin > 4 and BlandChromatin > 7 | 4 | 0.283019 |
| BlandChromatin > 1 and NormalNucleoli > 9 | 4 | 0.208333 |
| CellSize > 1 and Mitoses <= 2 and ClumpThickness <= 6 and MarginalAdhesion > 1 and NormalNucleoli > 3 | 4 | 0.179259 |
| Mitoses <= 2 and ClumpThickness <= 6 and BlandChromatin > 1 and NormalNucleoli > 1 | 2 | 0.363441 |
| EpithelialSize > 4 | 4 | 0.324324 |
| ClumpThickness <= 3 | 2 | 0.692308 |
| ClumpThickness > 5 | 4 | 0.357143 |
|  | 2 | 0.700000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize >= 5 and ClumpThickness >= 7 | 4 | 0.182540 |
| BlandChromatin >= 4 and BareNuclei >= 9 | 4 | 0.130802 |
| BareNuclei >= 3 and NormalNucleoli >= 8 | 4 | 0.033385 |
| NormalNucleoli >= 3 and CellShape >= 3 and BlandChromatin >= 5 and EpithelialSize <= 5 | 4 | 0.023697 |
| NormalNucleoli >= 3 and Mitoses >= 3 and CellSize >= 4 | 4 | 0.019048 |
| BareNuclei >= 3 and CellShape >= 3 and ClumpThickness >= 7 | 4 | 0.019048 |
| CellSize >= 3 and BareNuclei >= 3 | 4 | 0.015777 |
|  | 2 | 0.983294 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cellsize|barenuclei|class
---|---|---
(1.5-2.5]|(5.5-inf)|4
(2.5-3.5]|(5.5-inf)|4
(-inf-1.5]|(5.5-inf)|2
(3.5-inf)|(5.5-inf)|4
(-inf-1.5]|(2.5-5.5]|2
(2.5-3.5]|(2.5-5.5]|4
(3.5-inf)|(2.5-5.5]|4
(1.5-2.5]|(2.5-5.5]|2
(3.5-inf)|?|2
(-inf-1.5]|?|2
(2.5-3.5]|(1.5-2.5]|2
(3.5-inf)|(1.5-2.5]|4
(1.5-2.5]|(1.5-2.5]|2
(-inf-1.5]|(1.5-2.5]|2
(2.5-3.5]|(-inf-1.5]|2
(1.5-2.5]|(-inf-1.5]|2
(-inf-1.5]|(-inf-1.5]|2
(3.5-inf)|(-inf-1.5]|4

## JRip

Decision list:

rules | predicted class
---|---
(CellSize >= 5) and (ClumpThickness >= 7)|4 (92.0/0.0)
(BlandChromatin >= 4) and (BareNuclei >= 9)|4 (62.0/0.0)
(BareNuclei >= 3) and (NormalNucleoli >= 8)|4 (16.0/0.0)
(NormalNucleoli >= 3) and (CellShape >= 3) and (BlandChromatin >= 5) and (EpithelialSize <= 5)|4 (10.0/0.0)
(NormalNucleoli >= 3) and (Mitoses >= 3) and (CellSize >= 4)|4 (8.0/0.0)
(BareNuclei >= 3) and (CellShape >= 3) and (ClumpThickness >= 7)|4 (8.0/0.0)
(CellSize >= 3) and (BareNuclei >= 3)|4 (24.0/11.0)
|2 (408.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
CellSize <= 2 AND ClumpThickness <= 5 AND BareNuclei <= 2|2 (344.29)
CellShape > 2 AND BareNuclei > 2 AND ClumpThickness > 6|4 (109.86)
BlandChromatin > 3 AND BareNuclei > 8|4 (51.08/1.01)
NormalNucleoli <= 2 AND CellSize <= 3 AND BareNuclei <= 3|2 (40.52)
CellShape > 2 AND BlandChromatin > 4 AND BlandChromatin > 7|4 (15.0)
BlandChromatin > 1 AND NormalNucleoli > 9|4 (10.0)
CellSize > 1 AND Mitoses <= 2 AND ClumpThickness <= 6 AND MarginalAdhesion > 1 AND NormalNucleoli > 3|4 (13.99/2.99)
Mitoses <= 2 AND ClumpThickness <= 6 AND BlandChromatin > 1 AND NormalNucleoli > 1|2 (11.0/2.0)
EpithelialSize > 4|4 (10.0)
ClumpThickness <= 3|2 (8.17)
ClumpThickness > 5|4 (7.07/2.0)
|2 (7.02/3.0)


## J48 Decision Tree

* CellSize <= 2.5
	* ClumpThickness <= 5.5
		* BareNuclei <= 2.5: 2 (344.29)
		* BareNuclei > 2.5
			* CellShape <= 2.5: 2 (19.52/1.0)
			* CellShape > 2.5: 4 (4.19/1.19)
	* ClumpThickness > 5.5
		* BareNuclei <= 2: 2 (13.0/1.0)
		* BareNuclei > 2: 4 (7.0)
* CellSize > 2.5
	* CellSize <= 3.5
		* BareNuclei <= 2.5: 2 (22.0/1.0)
		* BareNuclei > 2.5: 4 (25.0/4.0)
	* CellSize > 3.5
		* BlandChromatin <= 4.5
			* ClumpThickness <= 6.5
				* ClumpThickness <= 3.5: 4 (5.0)
				* ClumpThickness > 3.5
					* ClumpThickness <= 4.5: 2 (3.0)
					* ClumpThickness > 4.5
						* Mitoses <= 2
							* MarginalAdhesion <= 1.5: 2 (3.0)
							* MarginalAdhesion > 1.5
								* EpithelialSize <= 4.5: 4 (5.0)
								* EpithelialSize > 4.5: 2 (3.0/1.0)
						* Mitoses > 2: 4 (4.0)
			* ClumpThickness > 6.5: 4 (34.0/1.0)
		* BlandChromatin > 4.5: 4 (136.0/2.0)


## SimpleCart Decision Tree

* CellSize < 3.5
	* BareNuclei < 3.5: 2(387.96/6.0)
	* BareNuclei >= 3.5
		* CellSize < 1.5: 2(10.03/4.0)
		* CellSize >= 1.5: 4(24.0/2.99)
* CellSize >= 3.5: 4(182.0/11.0)


