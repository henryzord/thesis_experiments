# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2 and Single_Epi_Cell_Size <= 2 | 0 | 0.642210 |
| Cell_Size_Uniformity > 2 and Cell_Size_Uniformity > 4 | 1 | 0.255377 |
| Cell_Size_Uniformity > 2 and Cell_Size_Uniformity <= 4 and Bare_Nuclei > 2 | 1 | 0.064286 |
| Cell_Size_Uniformity > 2 and Cell_Size_Uniformity <= 4 and Bare_Nuclei <= 2 | 0 | 0.094186 |
| Cell_Size_Uniformity <= 2 and Single_Epi_Cell_Size > 2 and Cell_Shape_Uniformity <= 2 | 0 | 0.088063 |
| Cell_Size_Uniformity <= 2 and Single_Epi_Cell_Size > 2 and Cell_Shape_Uniformity > 2 | 1 | 0.012475 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2.5 and Single_Epi_Cell_Size <= 2.5 and Marginal_Adhesion <= 2.5 | 0 | 0.627685 |
| Cell_Shape_Uniformity <= 2.5 and Bland_Chromatin <= 3.5 and Single_Epi_Cell_Size > 1.5 | 0 | 0.212121 |
| Cell_Size_Uniformity > 4.5 and Clump_Thickness > 6.5 | 1 | 0.742268 |
| Bare_Nuclei > 3.5 and Cell_Shape_Uniformity > 7.5 | 1 | 0.418605 |
| Normal_Nucleoli > 9.5 | 1 | 0.390244 |
| Clump_Thickness > 8.5 | 1 | 0.342105 |
| Bare_Nuclei > 3.5 and Marginal_Adhesion > 6.5 and Clump_Thickness <= 5.5 | 1 | 0.218750 |
| Bare_Nuclei > 3.5 and Clump_Thickness > 2.5 and Cell_Shape_Uniformity > 2.5 and Cell_Shape_Uniformity > 4.5 and Cell_Size_Uniformity <= 5.5 | 1 | 0.242424 |
| Mitoses <= 3.5 and Bare_Nuclei <= 2.5 and Single_Epi_Cell_Size <= 4 | 0 | 0.312500 |
| Bland_Chromatin > 1.5 and Clump_Thickness > 2.5 and Mitoses <= 3.5 and Cell_Size_Uniformity <= 3.5 and Normal_Nucleoli <= 4.5 | 1 | 0.318182 |
| Cell_Size_Uniformity <= 1.5 | 0 | 0.166667 |
| Clump_Thickness <= 2.5 | 1 | 0.200000 |
| Mitoses > 3.5 | 1 | 0.200000 |
| Normal_Nucleoli <= 6.5 and Cell_Size_Uniformity <= 6.5 and Bare_Nuclei <= 9.5 and Marginal_Adhesion <= 4 and Clump_Thickness > 4.5 | 0 | 0.133333 |
| Single_Epi_Cell_Size <= 7.5 and Normal_Nucleoli <= 5.5 | 0 | 0.320513 |
| Cell_Size_Uniformity <= 6.5 and Marginal_Adhesion > 2 and Mitoses <= 2.5 and Normal_Nucleoli > 6.5 | 0 | 0.307692 |
| Clump_Thickness > 3.5 | 1 | 0.875000 |
|  | 1 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity >= 4 and Cell_Size_Uniformity >= 5 and Bare_Nuclei >= 9 | 1 | 0.175000 |
| Cell_Size_Uniformity >= 3 and Clump_Thickness >= 9 | 1 | 0.093407 |
| Normal_Nucleoli >= 3 and Bare_Nuclei >= 2 and Bland_Chromatin >= 5 and Cell_Size_Uniformity >= 5 | 1 | 0.049143 |
| Cell_Shape_Uniformity >= 3 and Bare_Nuclei >= 3 and Clump_Thickness >= 7 and Marginal_Adhesion <= 4 | 1 | 0.029412 |
| Normal_Nucleoli >= 9 and Clump_Thickness >= 5 | 1 | 0.026549 |
| Marginal_Adhesion >= 2 and Clump_Thickness <= 4 and Bare_Nuclei >= 5 | 1 | 0.017857 |
| Normal_Nucleoli >= 4 | 1 | 0.005866 |
|  | 0 | 0.990991 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Shape_Uniformity >= 4) and (Cell_Size_Uniformity >= 5) and (Bare_Nuclei >= 9)|1 (70.0/0.0)
(Cell_Size_Uniformity >= 3) and (Clump_Thickness >= 9)|1 (34.0/0.0)
(Normal_Nucleoli >= 3) and (Bare_Nuclei >= 2) and (Bland_Chromatin >= 5) and (Cell_Size_Uniformity >= 5)|1 (17.0/0.0)
(Cell_Shape_Uniformity >= 3) and (Bare_Nuclei >= 3) and (Clump_Thickness >= 7) and (Marginal_Adhesion <= 4)|1 (10.0/0.0)
(Normal_Nucleoli >= 9) and (Clump_Thickness >= 5)|1 (10.0/0.0)
(Marginal_Adhesion >= 2) and (Clump_Thickness <= 4) and (Bare_Nuclei >= 5)|1 (6.0/0.0)
(Normal_Nucleoli >= 4)|1 (19.0/13.0)
|0 (320.0/3.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Size_Uniformity <= 2.5 AND Single_Epi_Cell_Size <= 2.5 AND Marginal_Adhesion <= 2.5|0 (263.0)
Cell_Shape_Uniformity <= 2.5 AND Bland_Chromatin <= 3.5 AND Single_Epi_Cell_Size > 1.5|0 (42.0)
Cell_Size_Uniformity > 4.5 AND Clump_Thickness > 6.5|1 (72.0)
Bare_Nuclei > 3.5 AND Cell_Shape_Uniformity > 7.5|1 (18.0)
Normal_Nucleoli > 9.5|1 (16.0)
Clump_Thickness > 8.5|1 (13.0)
Bare_Nuclei > 3.5 AND Marginal_Adhesion > 6.5 AND Clump_Thickness <= 5.5|1 (7.0)
Bare_Nuclei > 3.5 AND Clump_Thickness > 2.5 AND Cell_Shape_Uniformity > 2.5 AND Cell_Shape_Uniformity > 4.5 AND Cell_Size_Uniformity <= 5.5|1 (8.0)
Mitoses <= 3.5 AND Bare_Nuclei <= 2.5 AND Single_Epi_Cell_Size <= 4|0 (10.34)
Bland_Chromatin > 1.5 AND Clump_Thickness > 2.5 AND Mitoses <= 3.5 AND Cell_Size_Uniformity <= 3.5 AND Normal_Nucleoli <= 4.5|1 (7.0)
Cell_Size_Uniformity <= 1.5|0 (3.0)
Clump_Thickness <= 2.5|1 (3.0)
Mitoses > 3.5|1 (3.0)
Normal_Nucleoli <= 6.5 AND Cell_Size_Uniformity <= 6.5 AND Bare_Nuclei <= 9.5 AND Marginal_Adhesion <= 4 AND Clump_Thickness > 4.5|0 (2.49/1.0)
Single_Epi_Cell_Size <= 7.5 AND Normal_Nucleoli <= 5.5|0 (5.16)
Cell_Size_Uniformity <= 6.5 AND Marginal_Adhesion > 2 AND Mitoses <= 2.5 AND Normal_Nucleoli > 6.5|0 (4.0)
Clump_Thickness > 3.5|1 (6.0)
|1 (3.0/1.0)


## J48 Decision Tree

* Cell_Size_Uniformity <= 2
	* Single_Epi_Cell_Size <= 2: 0 (211.0/1.0)
	* Single_Epi_Cell_Size > 2
		* Cell_Shape_Uniformity <= 2: 0 (13.0)
		* Cell_Shape_Uniformity > 2: 1 (3.0/1.0)
* Cell_Size_Uniformity > 2
	* Cell_Size_Uniformity <= 4
		* Bare_Nuclei <= 2: 0 (15.31/1.0)
		* Bare_Nuclei > 2: 1 (33.69/7.69)
	* Cell_Size_Uniformity > 4: 1 (89.0/2.0)


