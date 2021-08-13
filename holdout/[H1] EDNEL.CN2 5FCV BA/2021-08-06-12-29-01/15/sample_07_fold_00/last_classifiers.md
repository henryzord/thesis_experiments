# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.654321 |
| Cell_Shape_Uniformity > 3.5 and Cell_Shape_Uniformity <= 4.5 and Marginal_Adhesion > 3.5 | 1 | 0.042838 |
| Cell_Shape_Uniformity > 3.5 and Cell_Shape_Uniformity <= 4.5 and Marginal_Adhesion > 2.5 and Marginal_Adhesion <= 3.5 | 1 | 0.004180 |
| Cell_Shape_Uniformity > 3.5 and Cell_Shape_Uniformity <= 4.5 and Marginal_Adhesion <= 1.5 | 1 | 0.012461 |
| Cell_Shape_Uniformity > 4.5 and Marginal_Adhesion > 1.5 and Marginal_Adhesion <= 2.5 | 1 | 0.036364 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 3.5 and Marginal_Adhesion > 3.5 | 1 | 0.021880 |
| Cell_Shape_Uniformity > 4.5 and Marginal_Adhesion > 2.5 and Marginal_Adhesion <= 3.5 | 1 | 0.045045 |
| Cell_Shape_Uniformity > 4.5 and Marginal_Adhesion > 3.5 | 1 | 0.220615 |
| Cell_Shape_Uniformity > 4.5 and Marginal_Adhesion <= 1.5 | 1 | 0.019290 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity <= 3.5 and Bland_Chromatin <= 3.5 and Bare_Nuclei <= 2.5 | 0 | 0.619910 |
| Cell_Shape_Uniformity > 2.5 and Clump_Thickness > 6.5 | 1 | 0.710526 |
| Single_Epi_Cell_Size <= 2.5 and Marginal_Adhesion <= 2.5 and Cell_Size_Uniformity <= 1.5 | 0 | 0.259259 |
| Single_Epi_Cell_Size > 2.5 and Bland_Chromatin > 3.5 and Cell_Size_Uniformity > 6.5 | 1 | 0.566038 |
| Marginal_Adhesion > 5.5 and Marginal_Adhesion > 8.5 | 1 | 0.220690 |
| Marginal_Adhesion <= 5.5 and Clump_Thickness <= 3.5 | 0 | 0.266667 |
| Marginal_Adhesion <= 5.5 and Mitoses > 1.5 | 1 | 0.236842 |
| Marginal_Adhesion > 5.5 | 1 | 0.304762 |
| Cell_Shape_Uniformity > 3.5 and Cell_Shape_Uniformity <= 4.5 | 0 | 0.347222 |
| Marginal_Adhesion <= 1.5 | 0 | 0.363636 |
|  | 1 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity >= 3 and Clump_Thickness >= 6 | 1 | 0.270933 |
| Cell_Shape_Uniformity >= 3 and Bland_Chromatin >= 4 | 1 | 0.092105 |
|  | 0 | 0.966565 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

cell_shape_uniformity|marginal_adhesion|target
---|---|---
(1.5-2.5]|(3.5-inf)|0
(-inf-1.5]|(3.5-inf)|0
(3.5-4.5]|(3.5-inf)|1
(4.5-inf)|(3.5-inf)|1
(2.5-3.5]|(3.5-inf)|1
(3.5-4.5]|(2.5-3.5]|1
(2.5-3.5]|(2.5-3.5]|0
(4.5-inf)|(2.5-3.5]|1
(1.5-2.5]|(2.5-3.5]|0
(-inf-1.5]|(2.5-3.5]|0
(3.5-4.5]|(1.5-2.5]|0
(2.5-3.5]|(1.5-2.5]|0
(4.5-inf)|(1.5-2.5]|1
(1.5-2.5]|(1.5-2.5]|0
(-inf-1.5]|(1.5-2.5]|0
(3.5-4.5]|(-inf-1.5]|1
(2.5-3.5]|(-inf-1.5]|0
(4.5-inf)|(-inf-1.5]|1
(1.5-2.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Size_Uniformity >= 3) and (Clump_Thickness >= 6)|1 (126.0/4.0)
(Cell_Shape_Uniformity >= 3) and (Bland_Chromatin >= 4)|1 (37.0/2.0)
|0 (323.0/11.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Shape_Uniformity <= 3.5 AND Bland_Chromatin <= 3.5 AND Bare_Nuclei <= 2.5|0 (279.5)
Cell_Shape_Uniformity > 2.5 AND Clump_Thickness > 6.5|1 (108.0)
Single_Epi_Cell_Size <= 2.5 AND Marginal_Adhesion <= 2.5 AND Cell_Size_Uniformity <= 1.5|0 (15.5)
Single_Epi_Cell_Size > 2.5 AND Bland_Chromatin > 3.5 AND Cell_Size_Uniformity > 6.5|1 (30.0)
Marginal_Adhesion > 5.5 AND Marginal_Adhesion > 8.5|1 (10.0/2.0)
Marginal_Adhesion <= 5.5 AND Clump_Thickness <= 3.5|0 (8.0)
Marginal_Adhesion <= 5.5 AND Mitoses > 1.5|1 (8.0/2.0)
Marginal_Adhesion > 5.5|1 (8.0)
Cell_Shape_Uniformity > 3.5 AND Cell_Shape_Uniformity <= 4.5|0 (6.0/1.0)
Marginal_Adhesion <= 1.5|0 (7.0/2.0)
|1 (6.0/1.0)


