# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity <= 1.5 and Bare_Nuclei <= 1.5 | 0 | 0.577836 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei > 7.5 | 1 | 0.189655 |
| Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Bare_Nuclei <= 1.5 | 0 | 0.162304 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 7.5 | 1 | 0.064198 |
| Cell_Shape_Uniformity <= 1.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 7.5 | 0 | 0.101404 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 7.5 | 1 | 0.062797 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei <= 1.5 | 0 | 0.088163 |
| Cell_Shape_Uniformity <= 1.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 0 | 0.075145 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 7.5 | 1 | 0.023069 |
| Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 7.5 | 0 | 0.036898 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei <= 1.5 | 1 | 0.019104 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei = ? | 0 | 0.024390 |
| Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 0 | 0.013889 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 1 | 0.009036 |
| Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 2.5 | 0 | 0.013889 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei = ? | 0 | 0.008282 |
| Cell_Shape_Uniformity > 1.5 and Cell_Shape_Uniformity <= 2.5 and Bare_Nuclei > 7.5 | 1 | 0.006042 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity <= 2.5 and Normal_Nucleoli <= 2.5 and Bare_Nuclei <= 2.5 | 0 | 0.615385 |
| Bland_Chromatin <= 2.5 and Cell_Size_Uniformity <= 2.5 and Marginal_Adhesion <= 1.5 | 0 | 0.153439 |
| Cell_Size_Uniformity > 4.5 and Clump_Thickness > 6.5 | 1 | 0.617391 |
| Bare_Nuclei > 7.5 and Bland_Chromatin > 3.5 | 1 | 0.526882 |
| Normal_Nucleoli <= 9.5 and Cell_Size_Uniformity <= 1.5 | 0 | 0.299169 |
| Mitoses <= 2.5 and Cell_Shape_Uniformity > 2.5 and Bare_Nuclei > 2.5 and Clump_Thickness > 6.5 | 1 | 0.299376 |
| Mitoses <= 2.5 and Cell_Size_Uniformity > 4.5 | 1 | 0.254202 |
| Mitoses <= 2.5 and Clump_Thickness <= 4.5 | 0 | 0.395604 |
| Mitoses > 2.0 | 1 | 0.416667 |
| Bare_Nuclei <= 2.5 | 0 | 0.471154 |
|  | 1 | 0.500000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cell_shape_uniformity|bare_nuclei|target
---|---|---
(-inf-1.5]|(7.5-inf)|0
(2.5-4.5]|(7.5-inf)|1
(1.5-2.5]|(7.5-inf)|1
(4.5-inf)|(7.5-inf)|1
(1.5-2.5]|(2.5-7.5]|0
(-inf-1.5]|(2.5-7.5]|0
(2.5-4.5]|(2.5-7.5]|1
(4.5-inf)|(2.5-7.5]|1
(1.5-2.5]|?|0
(4.5-inf)|?|0
(2.5-4.5]|?|0
(-inf-1.5]|?|0
(4.5-inf)|(1.5-2.5]|1
(1.5-2.5]|(1.5-2.5]|0
(2.5-4.5]|(1.5-2.5]|0
(-inf-1.5]|(1.5-2.5]|0
(4.5-inf)|(-inf-1.5]|1
(1.5-2.5]|(-inf-1.5]|0
(2.5-4.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0

## PART

Decision list:

rules | predicted class
---|---
Cell_Shape_Uniformity <= 2.5 AND Normal_Nucleoli <= 2.5 AND Bare_Nuclei <= 2.5|0 (262.49)
Bland_Chromatin <= 2.5 AND Cell_Size_Uniformity <= 2.5 AND Marginal_Adhesion <= 1.5|0 (25.29)
Cell_Size_Uniformity > 4.5 AND Clump_Thickness > 6.5|1 (71.0)
Bare_Nuclei > 7.5 AND Bland_Chromatin > 3.5|1 (49.95/0.95)
Normal_Nucleoli <= 9.5 AND Cell_Size_Uniformity <= 1.5|0 (16.22/1.0)
Mitoses <= 2.5 AND Cell_Shape_Uniformity > 2.5 AND Bare_Nuclei > 2.5 AND Clump_Thickness > 6.5|1 (13.0/1.0)
Mitoses <= 2.5 AND Cell_Size_Uniformity > 4.5|1 (13.05/2.05)
Mitoses <= 2.5 AND Clump_Thickness <= 4.5|0 (11.0)
Mitoses > 2.0|1 (10.0)
Bare_Nuclei <= 2.5|0 (8.5/1.0)
|1 (8.5/3.5)


