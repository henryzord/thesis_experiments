# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.666667 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 5.5 | 1 | 0.055901 |
| Cell_Size_Uniformity < 3.5 and Bare_Nuclei >= 6.0 | 1 | 0.035927 |
| Cell_Shape_Uniformity > 7.5 and Bare_Nuclei <= 1.5 | 1 | 0.021148 |
| Cell_Shape_Uniformity > 7.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 5.5 | 1 | 0.038576 |
| Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 1 | 0.006135 |
| Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 5.5 | 1 | 0.023240 |
| Cell_Size_Uniformity >= 3.5 | 1 | 0.290916 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 5.5 | 1 | 0.015529 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2.0 and Bare_Nuclei <= 2.0 | 0 | 0.623256 |
| Cell_Shape_Uniformity > 2.0 and Cell_Size_Uniformity > 4.0 and Cell_Size_Uniformity > 7.0 | 1 | 0.559055 |
| Cell_Shape_Uniformity <= 2.0 and Clump_Thickness <= 4.0 | 0 | 0.266129 |
| Bland_Chromatin > 2.0 and Clump_Thickness > 6.0 | 1 | 0.685195 |
| Bare_Nuclei > 5.0 and Mitoses <= 1.0 and Bland_Chromatin > 4.0 | 1 | 0.361111 |
| Mitoses > 1.0 | 1 | 0.344898 |
| Bland_Chromatin > 2.0 and Single_Epi_Cell_Size <= 4.0 | 1 | 0.207692 |
| Bland_Chromatin <= 2.0 | 0 | 0.672222 |
|  | 0 | 0.705882 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity >= 5 and Bare_Nuclei >= 1 and Marginal_Adhesion >= 2 | 1 | 0.265381 |
| Cell_Shape_Uniformity >= 3 and Bare_Nuclei >= 9 and Single_Epi_Cell_Size <= 6 | 1 | 0.055394 |
| Normal_Nucleoli >= 3 and Clump_Thickness >= 7 and Marginal_Adhesion <= 4 | 1 | 0.035714 |
| Bare_Nuclei >= 3 and Bland_Chromatin >= 4 and Marginal_Adhesion <= 2 | 1 | 0.012195 |
| Normal_Nucleoli >= 3 and Bare_Nuclei >= 3 and Single_Epi_Cell_Size <= 3 and Cell_Shape_Uniformity >= 3 | 1 | 0.012703 |
|  | 0 | 0.990826 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cell_shape_uniformity|bare_nuclei|target
---|---|---
(1.5-2.5]|(5.5-inf)|0
(2.5-4.5]|(5.5-inf)|1
(7.5-inf)|(5.5-inf)|1
(4.5-7.5]|(5.5-inf)|1
(-inf-1.5]|(5.5-inf)|1
(2.5-4.5]|(2.5-5.5]|1
(7.5-inf)|(2.5-5.5]|1
(4.5-7.5]|(2.5-5.5]|1
(1.5-2.5]|(2.5-5.5]|0
(-inf-1.5]|(2.5-5.5]|0
(7.5-inf)|?|0
(2.5-4.5]|?|0
(1.5-2.5]|?|0
(-inf-1.5]|?|0
(4.5-7.5]|?|0
(2.5-4.5]|(1.5-2.5]|0
(7.5-inf)|(1.5-2.5]|1
(1.5-2.5]|(1.5-2.5]|0
(4.5-7.5]|(1.5-2.5]|1
(-inf-1.5]|(1.5-2.5]|0
(4.5-7.5]|(-inf-1.5]|1
(7.5-inf)|(-inf-1.5]|1
(2.5-4.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0
(1.5-2.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Size_Uniformity >= 5) and (Bare_Nuclei >= 1) and (Marginal_Adhesion >= 2)|1 (119.0/0.0)
(Cell_Shape_Uniformity >= 3) and (Bare_Nuclei >= 9) and (Single_Epi_Cell_Size <= 6)|1 (19.0/0.0)
(Normal_Nucleoli >= 3) and (Clump_Thickness >= 7) and (Marginal_Adhesion <= 4)|1 (12.0/0.0)
(Bare_Nuclei >= 3) and (Bland_Chromatin >= 4) and (Marginal_Adhesion <= 2)|1 (4.0/0.0)
(Normal_Nucleoli >= 3) and (Bare_Nuclei >= 3) and (Single_Epi_Cell_Size <= 3) and (Cell_Shape_Uniformity >= 3)|1 (5.0/0.0)
|0 (327.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Size_Uniformity <= 2.0 AND Bare_Nuclei <= 2.0|0 (278.2)
Cell_Shape_Uniformity > 2.0 AND Cell_Size_Uniformity > 4.0 AND Cell_Size_Uniformity > 7.0|1 (71.0)
Cell_Shape_Uniformity <= 2.0 AND Clump_Thickness <= 4.0|0 (26.51)
Bland_Chromatin > 2.0 AND Clump_Thickness > 6.0|1 (52.0/1.0)
Bare_Nuclei > 5.0 AND Mitoses <= 1.0 AND Bland_Chromatin > 4.0|1 (13.62/0.62)
Mitoses > 1.0|1 (13.0)
Bland_Chromatin > 2.0 AND Single_Epi_Cell_Size <= 4.0|1 (12.15/3.15)
Bland_Chromatin <= 2.0|0 (10.15/1.0)
|0 (9.38/4.0)


## SimpleCart Decision Tree

* Cell_Size_Uniformity < 3.5
	* Bare_Nuclei < 6.0: 0(312.52/7.0)
	* Bare_Nuclei >= 6.0: 1(13.0/1.47)
* Cell_Size_Uniformity >= 3.5: 1(142.0/10.0)


