# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2.0 and Normal_Nucleoli <= 2.0 | 0 | 0.637615 |
| Cell_Size_Uniformity > 2.0 | 1 | 0.285562 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 4.5 and Bare_Nuclei <= 1.5 | 0 | 0.070402 |
| Cell_Size_Uniformity <= 2.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei <= 4.0 | 0 | 0.038095 |
| Cell_Size_Uniformity <= 2.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei > 4.0 | 1 | 0.018182 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 4.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 0 | 0.013720 |
| Cell_Size_Uniformity > 4.5 and Bare_Nuclei = ? | 0 | 0.008180 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 4.5 and Bare_Nuclei = ? | 0 | 0.003086 |
| Cell_Size_Uniformity > 1.5 and Cell_Size_Uniformity <= 2.5 and Bare_Nuclei > 5.5 | 1 | 0.012195 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity <= 2.0 | 0 | 0.635328 |
| Bland_Chromatin > 2.0 and Bare_Nuclei > 2.0 | 1 | 0.787348 |
| Single_Epi_Cell_Size <= 3.0 | 0 | 0.579201 |
|  | 1 | 0.703704 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity >= 5 | 1 | 0.260445 |
| Bare_Nuclei >= 3 and Clump_Thickness >= 5 | 1 | 0.085381 |
| Bare_Nuclei >= 7 | 1 | 0.006173 |
|  | 0 | 0.984802 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cell_size_uniformity|bare_nuclei|target
---|---|---
(1.5-2.5]|(5.5-inf)|1
(-inf-1.5]|(5.5-inf)|1
(2.5-4.5]|(5.5-inf)|1
(4.5-inf)|(5.5-inf)|1
(1.5-2.5]|(2.5-5.5]|0
(4.5-inf)|(2.5-5.5]|1
(-inf-1.5]|(2.5-5.5]|0
(2.5-4.5]|(2.5-5.5]|1
(4.5-inf)|?|0
(2.5-4.5]|?|0
(-inf-1.5]|?|0
(1.5-2.5]|(1.5-2.5]|0
(2.5-4.5]|(1.5-2.5]|0
(4.5-inf)|(1.5-2.5]|1
(-inf-1.5]|(1.5-2.5]|0
(4.5-inf)|(-inf-1.5]|1
(2.5-4.5]|(-inf-1.5]|0
(1.5-2.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Size_Uniformity >= 5)|1 (120.0/3.0)
(Bare_Nuclei >= 3) and (Clump_Thickness >= 5)|1 (39.0/4.0)
(Bare_Nuclei >= 7)|1 (5.0/1.0)
|0 (322.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Shape_Uniformity <= 2.0|0 (292.0/5.0)
Bland_Chromatin > 2.0 AND Bare_Nuclei > 2.0|1 (147.49/7.75)
Single_Epi_Cell_Size <= 3.0|0 (31.25/3.25)
|1 (15.25/1.25)


## J48 Decision Tree

* Cell_Size_Uniformity <= 2.0
	* Normal_Nucleoli <= 2.0: 0 (258.0/2.0)
	* Normal_Nucleoli > 2.0
		* Bare_Nuclei <= 4.0: 0 (9.0/1.0)
		* Bare_Nuclei > 4.0: 1 (5.0)
* Cell_Size_Uniformity > 2.0: 1 (166.0/28.0)


