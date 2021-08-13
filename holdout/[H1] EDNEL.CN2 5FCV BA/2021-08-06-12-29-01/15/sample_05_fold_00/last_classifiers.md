# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Clump_Thickness <= 1.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli <= 2.5 | 0 | 0.350195 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli <= 2.5 | 0 | 0.318367 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli <= 2.5 | 0 | 0.289422 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli > 8.5 | 1 | 0.063953 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.055718 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.047337 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli <= 2.5 | 0 | 0.097297 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.036142 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli > 8.5 | 1 | 0.027190 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli <= 2.5 | 1 | 0.027190 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli <= 2.5 | 0 | 0.062230 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli <= 2.5 | 1 | 0.024242 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli > 8.5 | 1 | 0.024242 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli <= 2.5 | 0 | 0.056497 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.023381 |
| Clump_Thickness <= 1.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli <= 2.5 | 0 | 0.056497 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli > 8.5 | 1 | 0.021277 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli <= 2.5 | 1 | 0.018293 |
| Clump_Thickness <= 1.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli <= 2.5 | 0 | 0.040230 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.018293 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli > 8.5 | 1 | 0.012270 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli > 8.5 | 1 | 0.012270 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli <= 2.5 | 0 | 0.018824 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.009231 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 0 | 0.017647 |
| Clump_Thickness <= 1.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 0 | 0.017647 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.006944 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.006211 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 0 | 0.011834 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 7.5 and Normal_Nucleoli <= 2.5 | 1 | 0.006173 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 0 | 0.011834 |
| Clump_Thickness > 1.5 and Clump_Thickness <= 3.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli <= 2.5 | 1 | 0.006173 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 1 | 0.006173 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 4.5 and Cell_Shape_Uniformity <= 7.5 and Normal_Nucleoli <= 2.5 | 1 | 0.005573 |
| Clump_Thickness > 3.5 and Clump_Thickness <= 6.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli > 2.5 and Normal_Nucleoli <= 8.5 | 0 | 0.005952 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity <= 1.5 and Normal_Nucleoli <= 2.5 | 0 | 0.005952 |
| Clump_Thickness > 6.5 and Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli <= 2.5 | 0 | 0.002994 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2 and Clump_Thickness <= 5 and Marginal_Adhesion <= 2 | 0 | 0.609813 |
| Cell_Shape_Uniformity <= 2 and Bare_Nuclei <= 4 | 0 | 0.193237 |
| Cell_Size_Uniformity > 4 and Clump_Thickness > 6 | 1 | 0.796117 |
| Bland_Chromatin > 2 and Bare_Nuclei > 8 and Single_Epi_Cell_Size <= 5 | 1 | 0.611111 |
| Normal_Nucleoli > 8 | 1 | 0.487805 |
| Mitoses > 2 | 1 | 0.275862 |
| Cell_Size_Uniformity <= 9 and Clump_Thickness > 6 and Marginal_Adhesion <= 4 | 1 | 0.250000 |
| Marginal_Adhesion <= 2 | 0 | 0.370370 |
| Cell_Shape_Uniformity <= 7 and Normal_Nucleoli > 3 and Normal_Nucleoli <= 5 | 1 | 0.388889 |
| Cell_Shape_Uniformity <= 7 and Bare_Nuclei <= 9 and Bland_Chromatin > 3 | 0 | 0.411765 |
| Cell_Shape_Uniformity > 4 and Cell_Shape_Uniformity > 6 | 1 | 0.555556 |
| Cell_Shape_Uniformity <= 4 | 0 | 0.380952 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Clump_Thickness >= 7 and Cell_Size_Uniformity >= 5 | 1 | 0.202970 |
| Bare_Nuclei >= 6 and Marginal_Adhesion >= 6 | 1 | 0.098039 |
| Cell_Shape_Uniformity >= 5 and Bland_Chromatin >= 5 and Marginal_Adhesion <= 8 | 1 | 0.061224 |
| Cell_Shape_Uniformity >= 3 and Bare_Nuclei >= 2 and Normal_Nucleoli >= 4 and Single_Epi_Cell_Size <= 3 | 1 | 0.024242 |
| Single_Epi_Cell_Size >= 4 and Bare_Nuclei >= 9 and Marginal_Adhesion <= 4 | 1 | 0.018293 |
| Single_Epi_Cell_Size >= 4 and Clump_Thickness >= 6 and Marginal_Adhesion <= 4 and Cell_Shape_Uniformity >= 3 | 1 | 0.018293 |
|  | 0 | 0.972810 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

clump_thickness|cell_shape_uniformity|normal_nucleoli|target
---|---|---|---
(1.5-3.5]|(7.5-inf)|(8.5-inf)|0
(3.5-6.5]|(7.5-inf)|(8.5-inf)|1
(6.5-inf)|(7.5-inf)|(8.5-inf)|1
(6.5-inf)|(4.5-7.5]|(8.5-inf)|1
(3.5-6.5]|(4.5-7.5]|(8.5-inf)|1
(-inf-1.5]|(7.5-inf)|(2.5-8.5]|0
(6.5-inf)|(2.5-4.5]|(8.5-inf)|1
(3.5-6.5]|(2.5-4.5]|(8.5-inf)|1
(3.5-6.5]|(7.5-inf)|(2.5-8.5]|1
(6.5-inf)|(7.5-inf)|(2.5-8.5]|1
(1.5-3.5]|(4.5-7.5]|(2.5-8.5]|1
(6.5-inf)|(4.5-7.5]|(2.5-8.5]|1
(3.5-6.5]|(4.5-7.5]|(2.5-8.5]|1
(-inf-1.5]|(2.5-4.5]|(2.5-8.5]|0
(1.5-3.5]|(2.5-4.5]|(2.5-8.5]|1
(3.5-6.5]|(7.5-inf)|(-inf-2.5]|1
(6.5-inf)|(7.5-inf)|(-inf-2.5]|1
(6.5-inf)|(2.5-4.5]|(2.5-8.5]|1
(3.5-6.5]|(2.5-4.5]|(2.5-8.5]|1
(3.5-6.5]|(1.5-2.5]|(2.5-8.5]|0
(3.5-6.5]|(4.5-7.5]|(-inf-2.5]|1
(6.5-inf)|(1.5-2.5]|(2.5-8.5]|1
(1.5-3.5]|(4.5-7.5]|(-inf-2.5]|1
(6.5-inf)|(4.5-7.5]|(-inf-2.5]|1
(1.5-3.5]|(1.5-2.5]|(2.5-8.5]|0
(-inf-1.5]|(-inf-1.5]|(2.5-8.5]|0
(1.5-3.5]|(-inf-1.5]|(2.5-8.5]|0
(6.5-inf)|(2.5-4.5]|(-inf-2.5]|1
(3.5-6.5]|(-inf-1.5]|(2.5-8.5]|0
(3.5-6.5]|(2.5-4.5]|(-inf-2.5]|0
(-inf-1.5]|(2.5-4.5]|(-inf-2.5]|0
(1.5-3.5]|(2.5-4.5]|(-inf-2.5]|0
(6.5-inf)|(1.5-2.5]|(-inf-2.5]|0
(-inf-1.5]|(1.5-2.5]|(-inf-2.5]|0
(1.5-3.5]|(1.5-2.5]|(-inf-2.5]|0
(3.5-6.5]|(1.5-2.5]|(-inf-2.5]|0
(6.5-inf)|(-inf-1.5]|(-inf-2.5]|0
(1.5-3.5]|(-inf-1.5]|(-inf-2.5]|0
(3.5-6.5]|(-inf-1.5]|(-inf-2.5]|0
(-inf-1.5]|(-inf-1.5]|(-inf-2.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Clump_Thickness >= 7) and (Cell_Size_Uniformity >= 5)|1 (82.0/0.0)
(Bare_Nuclei >= 6) and (Marginal_Adhesion >= 6)|1 (35.0/0.0)
(Cell_Shape_Uniformity >= 5) and (Bland_Chromatin >= 5) and (Marginal_Adhesion <= 8)|1 (21.0/0.0)
(Cell_Shape_Uniformity >= 3) and (Bare_Nuclei >= 2) and (Normal_Nucleoli >= 4) and (Single_Epi_Cell_Size <= 3)|1 (8.0/0.0)
(Single_Epi_Cell_Size >= 4) and (Bare_Nuclei >= 9) and (Marginal_Adhesion <= 4)|1 (6.0/0.0)
(Single_Epi_Cell_Size >= 4) and (Clump_Thickness >= 6) and (Marginal_Adhesion <= 4) and (Cell_Shape_Uniformity >= 3)|1 (6.0/0.0)
|0 (331.0/9.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Size_Uniformity <= 2 AND Clump_Thickness <= 5 AND Marginal_Adhesion <= 2|0 (261.0)
Cell_Shape_Uniformity <= 2 AND Bare_Nuclei <= 4|0 (40.0)
Cell_Size_Uniformity > 4 AND Clump_Thickness > 6|1 (82.0)
Bland_Chromatin > 2 AND Bare_Nuclei > 8 AND Single_Epi_Cell_Size <= 5|1 (33.53)
Normal_Nucleoli > 8|1 (20.0)
Mitoses > 2|1 (8.0)
Cell_Size_Uniformity <= 9 AND Clump_Thickness > 6 AND Marginal_Adhesion <= 4|1 (6.47)
Marginal_Adhesion <= 2|0 (10.0)
Cell_Shape_Uniformity <= 7 AND Normal_Nucleoli > 3 AND Normal_Nucleoli <= 5|1 (7.0)
Cell_Shape_Uniformity <= 7 AND Bare_Nuclei <= 9 AND Bland_Chromatin > 3|0 (6.69)
Cell_Shape_Uniformity > 4 AND Cell_Shape_Uniformity > 6|1 (5.0)
Cell_Shape_Uniformity <= 4|0 (6.0/2.0)
|1 (3.31/0.31)


