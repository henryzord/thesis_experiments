# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize < 3.5 and BareNuclei < 3.5 | 2 | 0.632813 |
| CellSize > 2.5 | 4 | 0.298966 |
| CellSize <= 2.5 | 2 | 0.628226 |
| CellSize > 1.5 and CellSize <= 2.5 and BareNuclei > 5.5 | 4 | 0.011990 |
| CellSize > 3.5 and BareNuclei = ? | 2 | 0.006144 |
| CellSize < 3.5 and BareNuclei >= 3.5 and CellSize >= 1.5 | 4 | 0.049269 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize <= 2.5 | 2 | 0.628226 |
| CellShape > 2.5 | 4 | 0.846467 |
|  | 2 | 0.800000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| CellSize >= 5 and ClumpThickness >= 7 | 4 | 0.182540 |
| BlandChromatin >= 4 and BareNuclei >= 9 | 4 | 0.130802 |
| BareNuclei >= 3 and NormalNucleoli >= 8 | 4 | 0.033385 |
| NormalNucleoli >= 3 and CellShape >= 3 and BlandChromatin >= 5 and EpithelialSize <= 5 | 4 | 0.023697 |
| NormalNucleoli >= 3 and Mitoses >= 3 and CellSize >= 4 | 4 | 0.019048 |
| BareNuclei >= 3 and CellShape >= 3 and ClumpThickness >= 7 | 4 | 0.019048 |
| CellSize >= 3 and BareNuclei >= 3 and ClumpThickness <= 3 and CellShape >= 3 | 4 | 0.011990 |
| CellSize >= 3 and MarginalAdhesion >= 3 and NormalNucleoli <= 4 | 4 | 0.011042 |
| BareNuclei >= 2 and ClumpThickness >= 5 and CellSize >= 2 and CellSize <= 6 | 4 | 0.006272 |
|  | 2 | 0.997579 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cellsize|barenuclei|class
---|---|---
(-inf-1.5]|(5.5-inf)|2
(2.5-3.5]|(5.5-inf)|4
(1.5-2.5]|(5.5-inf)|4
(3.5-inf)|(5.5-inf)|4
(2.5-3.5]|(2.5-5.5]|4
(-inf-1.5]|(2.5-5.5]|2
(1.5-2.5]|(2.5-5.5]|2
(3.5-inf)|(2.5-5.5]|4
(3.5-inf)|?|2
(-inf-1.5]|?|2
(2.5-3.5]|(1.5-2.5]|2
(1.5-2.5]|(1.5-2.5]|2
(-inf-1.5]|(1.5-2.5]|2
(3.5-inf)|(1.5-2.5]|4
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
(CellSize >= 3) and (BareNuclei >= 3) and (ClumpThickness <= 3) and (CellShape >= 3)|4 (5.0/0.0)
(CellSize >= 3) and (MarginalAdhesion >= 3) and (NormalNucleoli <= 4)|4 (14.0/6.0)
(BareNuclei >= 2) and (ClumpThickness >= 5) and (CellSize >= 2) and (CellSize <= 6)|4 (11.0/5.0)
|2 (402.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
CellSize <= 2.5|2 (324.0/12.0)
CellShape > 2.5|4 (180.0/17.0)
|2 (20.0/5.0)


## J48 Decision Tree

* CellSize <= 2.5: 2 (337.0/10.0)
* CellSize > 2.5: 4 (213.0/34.0)


## SimpleCart Decision Tree

* CellSize < 3.5
	* BareNuclei < 3.5: 2(387.96/6.0)
	* BareNuclei >= 3.5
		* CellSize < 1.5: 2(10.03/4.0)
		* CellSize >= 1.5: 4(24.0/2.99)
* CellSize >= 3.5: 4(182.0/11.0)


