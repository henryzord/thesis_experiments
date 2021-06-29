# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 2 | 0.656051 |
| CellShape > 4.5 and CellShape <= 7.5 and BareNuclei <= 1.5 | 4 | 0.006441 |
| CellShape > 2.5 and CellShape <= 3.5 and BareNuclei > 5.5 | 4 | 0.028470 |
| CellShape > 7.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.041860 |
| CellShape > 4.5 and CellShape <= 7.5 and BareNuclei > 1.5 and BareNuclei <= 2.5 | 4 | 0.004831 |
| CellShape > 4.5 and CellShape <= 7.5 and BareNuclei > 5.5 | 4 | 0.117811 |
| CellShape > 7.5 and BareNuclei <= 1.5 | 4 | 0.016706 |
| CellShape > 7.5 and BareNuclei > 1.5 and BareNuclei <= 2.5 | 4 | 0.009615 |
| CellSize <= 3 and NormalNucleoli > 2 and BareNuclei > 2 and ClumpThickness <= 6 | 4 | 0.016148 |
| CellSize <= 3 and NormalNucleoli > 2 and BareNuclei > 2 and ClumpThickness > 6 | 4 | 0.026005 |
| CellSize > 3 and CellSize <= 4 and ClumpThickness <= 8 and MarginalAdhesion > 6 | 4 | 0.016706 |
| CellShape > 4.5 and CellShape <= 7.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.025030 |
| CellShape > 2.5 and CellShape <= 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.011779 |
| CellSize > 3 and CellSize > 4 and ClumpThickness <= 6 and BlandChromatin > 4 and CellSize <= 6 and MarginalAdhesion <= 7 | 4 | 0.016706 |
| CellShape > 1.5 and CellShape <= 2.5 and BareNuclei > 5.5 | 4 | 0.009615 |
| CellSize > 3 and CellSize > 4 and ClumpThickness <= 6 and BlandChromatin > 4 and CellSize > 6 | 4 | 0.082405 |
| CellSize > 3 and CellSize > 4 and ClumpThickness <= 6 and BlandChromatin <= 4 | 4 | 0.022109 |
| CellSize > 3 and CellSize <= 4 and ClumpThickness > 8 | 4 | 0.030588 |
| CellSize > 3 and CellSize > 4 and ClumpThickness <= 6 and BlandChromatin > 4 and CellSize <= 6 and MarginalAdhesion > 7 | 4 | 0.012333 |
| CellSize <= 3 and NormalNucleoli <= 2 and BareNuclei > 2 and CellSize > 1 | 4 | 0.013952 |
| CellShape > 7.5 and BareNuclei > 5.5 | 4 | 0.125265 |
| CellSize > 3 and CellSize > 4 and ClumpThickness > 6 | 4 | 0.187377 |
| CellShape > 3.5 and CellShape <= 4.5 and BareNuclei > 5.5 | 4 | 0.033385 |
| CellShape > 3.5 and CellShape <= 4.5 and BareNuclei > 1.5 and BareNuclei <= 2.5 | 4 | 0.001214 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize > 3 and CellSize > 4 and ClumpThickness > 6 | 4 | 0.187377 |
| BlandChromatin <= 3 and NormalNucleoli <= 2 and MarginalAdhesion <= 2 and BareNuclei <= 2 | 2 | 0.728090 |
| CellShape <= 2 and Mitoses <= 1 and BareNuclei <= 4 | 2 | 0.324022 |
| BlandChromatin > 2 and CellShape > 7 | 4 | 0.516129 |
| CellShape > 1 and BlandChromatin > 2 and ClumpThickness > 8 | 4 | 0.387755 |
| CellSize > 1 and BareNuclei > 5 | 4 | 0.598753 |
| MarginalAdhesion > 3 | 4 | 0.216541 |
| ClumpThickness <= 4 and MarginalAdhesion <= 1 | 2 | 0.523810 |
| MarginalAdhesion > 1 | 2 | 0.631579 |
|  | 4 | 0.909091 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize >= 5 and BareNuclei >= 1 and NormalNucleoli >= 3 | 4 | 0.235678 |
| BareNuclei >= 3 and CellShape >= 3 and ClumpThickness >= 7 and NormalNucleoli <= 6 | 4 | 0.090508 |
| CellShape >= 3 and MarginalAdhesion <= 4 and BareNuclei >= 7 | 4 | 0.030588 |
| NormalNucleoli >= 3 and BareNuclei >= 4 | 4 | 0.029481 |
| CellSize >= 4 | 4 | 0.013951 |
|  | 2 | 0.983294 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cellshape|barenuclei|class
---|---|---
(-inf-1.5]|(5.5-inf)|2
(1.5-2.5]|(5.5-inf)|4
(2.5-3.5]|(5.5-inf)|4
(4.5-7.5]|(5.5-inf)|4
(3.5-4.5]|(5.5-inf)|4
(7.5-inf)|(5.5-inf)|4
(3.5-4.5]|(2.5-5.5]|4
(7.5-inf)|(2.5-5.5]|4
(4.5-7.5]|(2.5-5.5]|4
(2.5-3.5]|(2.5-5.5]|4
(1.5-2.5]|(2.5-5.5]|2
(-inf-1.5]|(2.5-5.5]|2
(7.5-inf)|?|2
(3.5-4.5]|?|2
(1.5-2.5]|?|2
(2.5-3.5]|?|2
(4.5-7.5]|?|2
(-inf-1.5]|?|2
(4.5-7.5]|(1.5-2.5]|4
(1.5-2.5]|(1.5-2.5]|2
(7.5-inf)|(1.5-2.5]|4
(-inf-1.5]|(1.5-2.5]|2
(2.5-3.5]|(1.5-2.5]|2
(3.5-4.5]|(1.5-2.5]|4
(7.5-inf)|(-inf-1.5]|4
(3.5-4.5]|(-inf-1.5]|2
(1.5-2.5]|(-inf-1.5]|2
(4.5-7.5]|(-inf-1.5]|4
(2.5-3.5]|(-inf-1.5]|2
(-inf-1.5]|(-inf-1.5]|2

## JRip

Decision list:

rules | predicted class
---|---
(CellSize >= 5) and (BareNuclei >= 1) and (NormalNucleoli >= 3)|4 (128.0/0.0)
(BareNuclei >= 3) and (CellShape >= 3) and (ClumpThickness >= 7) and (NormalNucleoli <= 6)|4 (40.0/0.0)
(CellShape >= 3) and (MarginalAdhesion <= 4) and (BareNuclei >= 7)|4 (13.0/0.0)
(NormalNucleoli >= 3) and (BareNuclei >= 4)|4 (18.0/3.0)
(CellSize >= 4)|4 (22.0/9.0)
|2 (407.0/7.0)


## PART

Decision list:

rules | predicted class
---|---
CellSize > 3 AND CellSize > 4 AND ClumpThickness > 6|4 (95.0)
BlandChromatin <= 3 AND NormalNucleoli <= 2 AND MarginalAdhesion <= 2 AND BareNuclei <= 2|2 (334.39)
CellShape <= 2 AND Mitoses <= 1 AND BareNuclei <= 4|2 (50.38)
BlandChromatin > 2 AND CellShape > 7|4 (32.0)
CellShape > 1 AND BlandChromatin > 2 AND ClumpThickness > 8|4 (19.0)
CellSize > 1 AND BareNuclei > 5|4 (54.6/5.95)
MarginalAdhesion > 3|4 (13.7/1.7)
ClumpThickness <= 4 AND MarginalAdhesion <= 1|2 (8.23)
MarginalAdhesion > 1|2 (12.0/1.0)
|4 (8.71/0.36)


## J48 Decision Tree

* CellSize <= 3
	* NormalNucleoli <= 2
		* BareNuclei <= 2: 2 (365.14)
		* BareNuclei > 2
			* CellSize <= 1
				* BlandChromatin <= 1: 2 (12.16)
				* BlandChromatin > 1: 2 (7.7/1.0)
			* CellSize > 1: 4 (11.0/3.0)
	* NormalNucleoli > 2
		* BareNuclei <= 2
			* ClumpThickness <= 3: 2 (7.0)
			* ClumpThickness > 3: 2 (7.0/2.0)
		* BareNuclei > 2
			* ClumpThickness <= 6: 4 (12.0/3.0)
			* ClumpThickness > 6: 4 (11.0)
* CellSize > 3
	* CellSize <= 4
		* ClumpThickness <= 8
			* MarginalAdhesion <= 6
				* CellShape <= 4: 2 (8.0/3.0)
				* CellShape > 4: 4 (8.0/2.0)
			* MarginalAdhesion > 6: 4 (7.0)
		* ClumpThickness > 8: 4 (13.0)
	* CellSize > 4
		* ClumpThickness <= 6
			* BlandChromatin <= 4: 4 (13.0/2.0)
			* BlandChromatin > 4
				* CellSize <= 6
					* MarginalAdhesion <= 7: 4 (7.0)
					* MarginalAdhesion > 7: 4 (7.0/1.0)
				* CellSize > 6: 4 (37.0)
		* ClumpThickness > 6: 4 (95.0)


