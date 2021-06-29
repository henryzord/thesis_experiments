# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 2 | 0.656051 |
| CellSize <= 3.5 and NormalNucleoli <= 2.5 and BareNuclei > 2.5 and CellShape > 2.5 | 4 | 0.009639 |
| CellShape > 3.5 and CellShape <= 4.5 and EpithelialSize > 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.001214 |
| CellShape > 7.5 and EpithelialSize > 3.5 and BareNuclei <= 1.5 | 4 | 0.016706 |
| CellSize >= 3.5 and CellSize >= 4.5 and ClumpThickness >= 6.5 | 4 | 0.187377 |
| CellShape > 3.5 and CellShape <= 4.5 and EpithelialSize > 2.5 and EpithelialSize <= 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.004831 |
| CellShape > 1.5 and CellShape <= 2.5 and EpithelialSize > 3.5 and BareNuclei > 5.5 | 4 | 0.007229 |
| CellShape > 2.5 and CellShape <= 3.5 and EpithelialSize > 2.5 and EpithelialSize <= 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.004831 |
| CellShape > 3.5 and CellShape <= 4.5 and EpithelialSize <= 2.5 and BareNuclei > 5.5 | 4 | 0.007229 |
| CellSize > 3.5 and CellSize <= 4.5 and ClumpThickness <= 8.5 and MarginalAdhesion > 6.0 | 4 | 0.016706 |
| CellSize > 3.5 and CellSize <= 4.5 and ClumpThickness > 8.5 | 4 | 0.030588 |
| CellShape > 4.5 and CellShape <= 7.5 and EpithelialSize > 3.5 and BareNuclei > 5.5 | 4 | 0.084500 |
| CellShape > 4.5 and CellShape <= 7.5 and EpithelialSize > 2.5 and EpithelialSize <= 3.5 and BareNuclei > 5.5 | 4 | 0.026005 |
| CellShape > 7.5 and EpithelialSize > 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.032864 |
| CellShape > 7.5 and EpithelialSize > 3.5 and BareNuclei > 1.5 and BareNuclei <= 2.5 | 4 | 0.009615 |
| CellSize >= 3.5 and CellSize >= 4.5 and ClumpThickness < 6.5 and BlandChromatin < 4.5 | 4 | 0.022109 |
| CellShape > 2.5 and CellShape <= 3.5 and EpithelialSize > 3.5 and BareNuclei > 5.5 | 4 | 0.016706 |
| CellShape > 4.5 and CellShape <= 7.5 and EpithelialSize > 2.5 and EpithelialSize <= 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.009615 |
| CellShape > 4.5 and CellShape <= 7.5 and EpithelialSize > 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.013952 |
| CellShape > 4.5 and CellShape <= 7.5 and EpithelialSize > 3.5 and BareNuclei <= 1.5 | 4 | 0.009615 |
| CellShape > 7.5 and EpithelialSize > 3.5 and BareNuclei > 5.5 | 4 | 0.110151 |
| CellShape > 2.5 and CellShape <= 3.5 and EpithelialSize > 3.5 and BareNuclei > 2.5 and BareNuclei <= 5.5 | 4 | 0.009615 |
| CellShape > 2.5 and CellShape <= 3.5 and EpithelialSize <= 2.5 and BareNuclei > 5.5 | 4 | 0.007229 |
| CellSize >= 3.5 and CellSize >= 4.5 and ClumpThickness < 6.5 and BlandChromatin >= 4.5 and CellSize < 6.5 | 4 | 0.028470 |
| CellShape > 2.5 and CellShape <= 3.5 and EpithelialSize > 2.5 and EpithelialSize <= 3.5 and BareNuclei > 5.5 | 4 | 0.005435 |
| CellSize < 3.5 and BareNuclei >= 4.5 and ClumpThickness >= 3.5 and ClumpThickness >= 6.5 | 4 | 0.030588 |
| CellSize >= 3.5 and CellSize >= 4.5 and ClumpThickness < 6.5 and BlandChromatin >= 4.5 and CellSize >= 6.5 | 4 | 0.082405 |
| CellSize >= 3.5 and CellSize < 4.5 | 4 | 0.053827 |
| CellSize < 3.5 and BareNuclei >= 4.5 and ClumpThickness >= 3.5 and ClumpThickness < 6.5 | 4 | 0.016148 |
| CellShape > 3.5 and CellShape <= 4.5 and EpithelialSize > 3.5 and BareNuclei <= 1.5 | 4 | 0.007711 |
| CellSize <= 3.5 and NormalNucleoli > 2.5 and BareNuclei > 2.5 | 4 | 0.040539 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize > 3 and CellSize > 4 and ClumpThickness > 6 | 4 | 0.187377 |
| BlandChromatin <= 3 and NormalNucleoli <= 2 and MarginalAdhesion <= 2 and BareNuclei <= 2 | 2 | 0.728090 |
| CellShape <= 2 and BareNuclei <= 5 and ClumpThickness <= 5 and EpithelialSize > 1 | 2 | 0.312500 |
| CellShape > 1 and BlandChromatin > 2 and CellShape > 7 | 4 | 0.492308 |
| CellSize > 1 and BareNuclei > 3 and ClumpThickness <= 8 and BlandChromatin > 4 and NormalNucleoli <= 7 | 4 | 0.410714 |
| ClumpThickness > 8 | 4 | 0.400000 |
| CellSize <= 1 and BareNuclei <= 4 | 2 | 0.254237 |
| NormalNucleoli > 9 | 4 | 0.400000 |
| MarginalAdhesion <= 9 and Mitoses <= 3 and BareNuclei > 3 and MarginalAdhesion <= 4 and ClumpThickness <= 5 and CellShape <= 4 and MarginalAdhesion <= 3 | 4 | 0.083333 |
| MarginalAdhesion <= 9 and Mitoses <= 3 and NormalNucleoli <= 2 and EpithelialSize <= 5 | 2 | 0.216216 |
| EpithelialSize <= 6 and ClumpThickness > 3 and NormalNucleoli <= 8 and CellSize > 2 and BareNuclei > 2 and BlandChromatin <= 5 and CellShape > 3 | 4 | 0.450000 |
| CellSize <= 6 and EpithelialSize <= 6 and ClumpThickness > 3 and MarginalAdhesion <= 4 and BareNuclei > 1 and ClumpThickness > 5 | 4 | 0.333333 |
| CellSize > 6 | 4 | 0.285714 |
| ClumpThickness <= 3 and CellShape <= 4 | 4 | 0.230769 |
| MarginalAdhesion > 4 and ClumpThickness <= 5 | 2 | 0.125000 |
| MarginalAdhesion <= 4 and MarginalAdhesion <= 3 and CellSize > 3 | 2 | 0.225000 |
| MarginalAdhesion <= 4 and MarginalAdhesion <= 2 | 4 | 0.321429 |
| MarginalAdhesion <= 4 | 4 | 0.300000 |
|  | 2 | 0.714286 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize >= 4 | 4 | 0.299000 |
| BareNuclei >= 3 and CellShape >= 3 | 4 | 0.034821 |
|  | 2 | 0.980952 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cellshape|epithelialsize|barenuclei|class
---|---|---|---
(1.5-2.5]|(3.5-inf)|(5.5-inf)|4
(3.5-4.5]|(3.5-inf)|(5.5-inf)|4
(4.5-7.5]|(3.5-inf)|(5.5-inf)|4
(2.5-3.5]|(3.5-inf)|(5.5-inf)|4
(7.5-inf)|(3.5-inf)|(5.5-inf)|4
(4.5-7.5]|(2.5-3.5]|(5.5-inf)|4
(3.5-4.5]|(2.5-3.5]|(5.5-inf)|4
(2.5-3.5]|(2.5-3.5]|(5.5-inf)|4
(7.5-inf)|(2.5-3.5]|(5.5-inf)|4
(-inf-1.5]|(3.5-inf)|(2.5-5.5]|2
(3.5-4.5]|(-inf-2.5]|(5.5-inf)|4
(3.5-4.5]|(3.5-inf)|(2.5-5.5]|4
(7.5-inf)|(-inf-2.5]|(5.5-inf)|2
(2.5-3.5]|(-inf-2.5]|(5.5-inf)|4
(2.5-3.5]|(3.5-inf)|(2.5-5.5]|4
(1.5-2.5]|(3.5-inf)|(2.5-5.5]|2
(1.5-2.5]|(-inf-2.5]|(5.5-inf)|2
(-inf-1.5]|(-inf-2.5]|(5.5-inf)|2
(4.5-7.5]|(3.5-inf)|(2.5-5.5]|4
(7.5-inf)|(3.5-inf)|(2.5-5.5]|4
(4.5-7.5]|(-inf-2.5]|(5.5-inf)|4
(4.5-7.5]|(3.5-inf)|?|2
(3.5-4.5]|(2.5-3.5]|(2.5-5.5]|4
(2.5-3.5]|(2.5-3.5]|(2.5-5.5]|4
(-inf-1.5]|(2.5-3.5]|(2.5-5.5]|2
(1.5-2.5]|(2.5-3.5]|(2.5-5.5]|2
(7.5-inf)|(2.5-3.5]|(2.5-5.5]|4
(4.5-7.5]|(2.5-3.5]|(2.5-5.5]|4
(1.5-2.5]|(2.5-3.5]|?|2
(2.5-3.5]|(-inf-2.5]|(2.5-5.5]|2
(1.5-2.5]|(3.5-inf)|(1.5-2.5]|2
(4.5-7.5]|(3.5-inf)|(1.5-2.5]|2
(7.5-inf)|(3.5-inf)|(1.5-2.5]|4
(7.5-inf)|(-inf-2.5]|(2.5-5.5]|2
(3.5-4.5]|(3.5-inf)|(1.5-2.5]|2
(3.5-4.5]|(-inf-2.5]|(2.5-5.5]|2
(1.5-2.5]|(-inf-2.5]|(2.5-5.5]|2
(-inf-1.5]|(-inf-2.5]|(2.5-5.5]|2
(4.5-7.5]|(-inf-2.5]|?|2
(7.5-inf)|(-inf-2.5]|?|2
(3.5-4.5]|(-inf-2.5]|?|2
(2.5-3.5]|(-inf-2.5]|?|2
(-inf-1.5]|(-inf-2.5]|?|2
(-inf-1.5]|(2.5-3.5]|(1.5-2.5]|2
(2.5-3.5]|(2.5-3.5]|(1.5-2.5]|2
(1.5-2.5]|(2.5-3.5]|(1.5-2.5]|2
(3.5-4.5]|(3.5-inf)|(-inf-1.5]|4
(3.5-4.5]|(-inf-2.5]|(1.5-2.5]|2
(4.5-7.5]|(3.5-inf)|(-inf-1.5]|4
(4.5-7.5]|(-inf-2.5]|(1.5-2.5]|2
(-inf-1.5]|(3.5-inf)|(-inf-1.5]|2
(7.5-inf)|(3.5-inf)|(-inf-1.5]|4
(-inf-1.5]|(-inf-2.5]|(1.5-2.5]|2
(2.5-3.5]|(-inf-2.5]|(1.5-2.5]|2
(1.5-2.5]|(-inf-2.5]|(1.5-2.5]|2
(2.5-3.5]|(2.5-3.5]|(-inf-1.5]|2
(-inf-1.5]|(2.5-3.5]|(-inf-1.5]|2
(1.5-2.5]|(2.5-3.5]|(-inf-1.5]|2
(4.5-7.5]|(2.5-3.5]|(-inf-1.5]|2
(3.5-4.5]|(-inf-2.5]|(-inf-1.5]|2
(4.5-7.5]|(-inf-2.5]|(-inf-1.5]|2
(1.5-2.5]|(-inf-2.5]|(-inf-1.5]|2
(2.5-3.5]|(-inf-2.5]|(-inf-1.5]|2
(-inf-1.5]|(-inf-2.5]|(-inf-1.5]|2

## JRip

Decision list:

rules | predicted class
---|---
(CellSize >= 4)|4 (195.0/10.0)
(BareNuclei >= 3) and (CellShape >= 3)|4 (25.0/2.0)
|2 (408.0/8.0)


## PART

Decision list:

rules | predicted class
---|---
CellSize > 3 AND CellSize > 4 AND ClumpThickness > 6|4 (95.0)
BlandChromatin <= 3 AND NormalNucleoli <= 2 AND MarginalAdhesion <= 2 AND BareNuclei <= 2|2 (334.39)
CellShape <= 2 AND BareNuclei <= 5 AND ClumpThickness <= 5 AND EpithelialSize > 1|2 (50.25)
CellShape > 1 AND BlandChromatin > 2 AND CellShape > 7|4 (32.0)
CellSize > 1 AND BareNuclei > 3 AND ClumpThickness <= 8 AND BlandChromatin > 4 AND NormalNucleoli <= 7|4 (22.76)
ClumpThickness > 8|4 (22.0)
CellSize <= 1 AND BareNuclei <= 4|2 (9.27)
NormalNucleoli > 9|4 (12.0)
MarginalAdhesion <= 9 AND Mitoses <= 3 AND BareNuclei > 3 AND MarginalAdhesion <= 4 AND ClumpThickness <= 5 AND CellShape <= 4 AND MarginalAdhesion <= 3|4 (5.71/2.71)
MarginalAdhesion <= 9 AND Mitoses <= 3 AND NormalNucleoli <= 2 AND EpithelialSize <= 5|2 (7.03)
EpithelialSize <= 6 AND ClumpThickness > 3 AND NormalNucleoli <= 8 AND CellSize > 2 AND BareNuclei > 2 AND BlandChromatin <= 5 AND CellShape > 3|4 (9.0)
CellSize <= 6 AND EpithelialSize <= 6 AND ClumpThickness > 3 AND MarginalAdhesion <= 4 AND BareNuclei > 1 AND ClumpThickness > 5|4 (5.16)
CellSize > 6|4 (4.0)
ClumpThickness <= 3 AND CellShape <= 4|4 (3.0)
MarginalAdhesion > 4 AND ClumpThickness <= 5|2 (4.0/2.0)
MarginalAdhesion <= 4 AND MarginalAdhesion <= 3 AND CellSize > 3|2 (3.43/1.08)
MarginalAdhesion <= 4 AND MarginalAdhesion <= 2|4 (3.0/1.0)
MarginalAdhesion <= 4|4 (3.0)
|2 (3.0)


## J48 Decision Tree

* CellSize <= 3.5
	* NormalNucleoli <= 2.5
		* BareNuclei <= 2.5: 2 (365.14)
		* BareNuclei > 2.5
			* CellShape <= 2.5: 2 (24.62/3.0)
			* CellShape > 2.5: 4 (6.23/0.23)
	* NormalNucleoli > 2.5
		* BareNuclei <= 2.5: 2 (14.0/2.0)
		* BareNuclei > 2.5: 4 (23.0/3.0)
* CellSize > 3.5
	* CellSize <= 4.5
		* ClumpThickness <= 8.5
			* MarginalAdhesion <= 6.0
				* ClumpThickness <= 6.0: 2 (6.0/1.0)
				* ClumpThickness > 6.0: 4 (10.0/2.0)
			* MarginalAdhesion > 6.0: 4 (7.0)
		* ClumpThickness > 8.5: 4 (13.0)
	* CellSize > 4.5: 4 (159.0/3.0)


## SimpleCart Decision Tree

* CellSize < 3.5
	* BareNuclei < 4.5: 2(392.13/7.0)
	* BareNuclei >= 4.5
		* ClumpThickness < 3.5: 2(6.78/2.0)
		* ClumpThickness >= 3.5
			* ClumpThickness < 6.5: 4(9.0/3.07)
			* ClumpThickness >= 6.5: 4(13.0/0.0)
* CellSize >= 3.5
	* CellSize < 4.5: 4(29.0/7.0)
	* CellSize >= 4.5
		* ClumpThickness < 6.5
			* BlandChromatin < 4.5: 4(11.0/2.0)
			* BlandChromatin >= 4.5
				* CellSize < 6.5: 4(13.0/1.0)
				* CellSize >= 6.5: 4(37.0/0.0)
		* ClumpThickness >= 6.5: 4(95.0/0.0)


