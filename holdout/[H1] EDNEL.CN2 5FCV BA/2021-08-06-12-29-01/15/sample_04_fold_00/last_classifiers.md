# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli <= 2.0 and Bare_Nuclei <= 2.0 | 0 | 0.621622 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei > 5.5 | 1 | 0.220693 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity > 4.0 and Clump_Thickness > 6.0 | 1 | 0.184615 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli <= 2.0 and Bare_Nuclei > 2.0 and Bare_Nuclei <= 5.0 and Clump_Thickness <= 3.0 | 0 | 0.101604 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity > 4.0 and Clump_Thickness <= 6.0 and Marginal_Adhesion > 1.0 | 1 | 0.126593 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei > 2.0 and Cell_Size_Uniformity <= 2.0 | 1 | 0.018519 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity <= 4.0 and Marginal_Adhesion > 5.0 | 1 | 0.033435 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei <= 2.0 | 0 | 0.035201 |
| Cell_Shape_Uniformity > 4.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 5.5 | 1 | 0.062419 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity <= 4.0 and Marginal_Adhesion <= 5.0 and Clump_Thickness <= 6.0 | 0 | 0.034483 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei > 2.0 and Cell_Size_Uniformity > 2.0 and Cell_Shape_Uniformity <= 4.0 and Normal_Nucleoli <= 4.0 | 1 | 0.012422 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli <= 2.0 and Bare_Nuclei > 2.0 and Bare_Nuclei > 5.0 | 1 | 0.012422 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli <= 2.0 and Bare_Nuclei > 2.0 and Bare_Nuclei <= 5.0 and Clump_Thickness > 3.0 and Bland_Chromatin <= 1.0 | 0 | 0.011765 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli <= 2.0 and Bare_Nuclei > 2.0 and Bare_Nuclei <= 5.0 and Clump_Thickness > 3.0 and Bland_Chromatin > 1.0 | 1 | 0.006250 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity > 4.0 and Clump_Thickness <= 6.0 and Marginal_Adhesion <= 1.0 and Cell_Shape_Uniformity > 6.0 | 0 | 0.011765 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity <= 4.0 and Marginal_Adhesion <= 5.0 and Clump_Thickness > 6.0 | 1 | 0.028464 |
| Cell_Size_Uniformity <= 3.0 and Normal_Nucleoli > 2.0 and Bare_Nuclei > 2.0 and Cell_Size_Uniformity > 2.0 and Cell_Shape_Uniformity <= 4.0 and Normal_Nucleoli > 4.0 | 0 | 0.007890 |
| Cell_Size_Uniformity > 3.0 and Cell_Size_Uniformity > 4.0 and Clump_Thickness <= 6.0 and Marginal_Adhesion <= 1.0 and Cell_Shape_Uniformity <= 6.0 | 1 | 0.006250 |
| Cell_Shape_Uniformity > 3.5 and Cell_Shape_Uniformity <= 4.5 and Bare_Nuclei > 2.5 and Bare_Nuclei <= 5.5 | 1 | 0.006289 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 3 and Normal_Nucleoli <= 2 and Bare_Nuclei <= 2 | 0 | 0.621622 |
| Cell_Shape_Uniformity > 2 and Cell_Size_Uniformity > 4 and Marginal_Adhesion > 1 and Clump_Thickness > 6 | 1 | 0.603774 |
| Cell_Shape_Uniformity > 2 and Normal_Nucleoli > 8 | 1 | 0.408451 |
| Cell_Size_Uniformity <= 1 and Bare_Nuclei <= 4 | 0 | 0.202128 |
| Cell_Shape_Uniformity > 2 and Clump_Thickness <= 8 and Marginal_Adhesion > 5 and Bland_Chromatin <= 6 | 1 | 0.425000 |
| Clump_Thickness > 8 | 1 | 0.465116 |
| Cell_Shape_Uniformity <= 2 and Cell_Size_Uniformity <= 1 | 0 | 0.099206 |
| Cell_Shape_Uniformity > 2 and Bland_Chromatin > 4 and Bare_Nuclei > 7 and Marginal_Adhesion <= 5 | 1 | 0.357143 |
| Cell_Shape_Uniformity > 2 and Normal_Nucleoli <= 6 and Marginal_Adhesion <= 5 and Cell_Size_Uniformity > 3 and Normal_Nucleoli > 3 | 1 | 0.236715 |
| Marginal_Adhesion > 5 | 1 | 0.311538 |
| Normal_Nucleoli <= 2 | 0 | 0.281250 |
| Single_Epi_Cell_Size <= 4 and Cell_Shape_Uniformity > 3 | 0 | 0.175824 |
| Cell_Shape_Uniformity <= 3 | 0 | 0.166667 |
|  | 1 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity >= 4 and Cell_Size_Uniformity >= 5 and Bare_Nuclei >= 9 | 1 | 0.182519 |
| Cell_Size_Uniformity >= 3 and Clump_Thickness >= 9 | 1 | 0.099150 |
| Normal_Nucleoli >= 3 and Bare_Nuclei >= 3 and Marginal_Adhesion >= 6 | 1 | 0.042357 |
| Normal_Nucleoli >= 9 | 1 | 0.047904 |
| Bare_Nuclei >= 3 and Normal_Nucleoli >= 3 and Normal_Nucleoli <= 6 and Clump_Thickness >= 7 | 1 | 0.015480 |
| Cell_Shape_Uniformity >= 3 and Marginal_Adhesion >= 4 and Bare_Nuclei <= 6 and Normal_Nucleoli >= 4 | 1 | 0.024847 |
| Single_Epi_Cell_Size >= 3 and Cell_Shape_Uniformity >= 3 and Clump_Thickness <= 3 and Cell_Size_Uniformity >= 3 | 1 | 0.015480 |
| Bare_Nuclei >= 6 | 1 | 0.010259 |
|  | 0 | 0.981481 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cell_shape_uniformity|bare_nuclei|target
---|---|---
(2.5-3.5]|(5.5-inf)|1
(-inf-1.5]|(5.5-inf)|0
(1.5-2.5]|(5.5-inf)|1
(3.5-4.5]|(5.5-inf)|1
(4.5-inf)|(5.5-inf)|1
(2.5-3.5]|(2.5-5.5]|1
(3.5-4.5]|(2.5-5.5]|1
(4.5-inf)|(2.5-5.5]|1
(1.5-2.5]|(2.5-5.5]|0
(-inf-1.5]|(2.5-5.5]|0
(4.5-inf)|?|1
(3.5-4.5]|?|0
(2.5-3.5]|?|0
(-inf-1.5]|?|0
(2.5-3.5]|(1.5-2.5]|0
(3.5-4.5]|(1.5-2.5]|0
(4.5-inf)|(1.5-2.5]|1
(1.5-2.5]|(1.5-2.5]|0
(-inf-1.5]|(1.5-2.5]|0
(4.5-inf)|(-inf-1.5]|1
(3.5-4.5]|(-inf-1.5]|0
(2.5-3.5]|(-inf-1.5]|0
(1.5-2.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Shape_Uniformity >= 4) and (Cell_Size_Uniformity >= 5) and (Bare_Nuclei >= 9)|1 (71.0/0.0)
(Cell_Size_Uniformity >= 3) and (Clump_Thickness >= 9)|1 (35.0/0.0)
(Normal_Nucleoli >= 3) and (Bare_Nuclei >= 3) and (Marginal_Adhesion >= 6)|1 (15.0/0.0)
(Normal_Nucleoli >= 9)|1 (16.0/0.0)
(Bare_Nuclei >= 3) and (Normal_Nucleoli >= 3) and (Normal_Nucleoli <= 6) and (Clump_Thickness >= 7)|1 (5.0/0.0)
(Cell_Shape_Uniformity >= 3) and (Marginal_Adhesion >= 4) and (Bare_Nuclei <= 6) and (Normal_Nucleoli >= 4)|1 (9.0/0.0)
(Single_Epi_Cell_Size >= 3) and (Cell_Shape_Uniformity >= 3) and (Clump_Thickness <= 3) and (Cell_Size_Uniformity >= 3)|1 (5.0/0.0)
(Bare_Nuclei >= 6)|1 (11.0/5.0)
|0 (319.0/6.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Size_Uniformity <= 3 AND Normal_Nucleoli <= 2 AND Bare_Nuclei <= 2|0 (281.58)
Cell_Shape_Uniformity > 2 AND Cell_Size_Uniformity > 4 AND Marginal_Adhesion > 1 AND Clump_Thickness > 6|1 (64.0)
Cell_Shape_Uniformity > 2 AND Normal_Nucleoli > 8|1 (29.0)
Cell_Size_Uniformity <= 1 AND Bare_Nuclei <= 4|0 (13.26)
Cell_Shape_Uniformity > 2 AND Clump_Thickness <= 8 AND Marginal_Adhesion > 5 AND Bland_Chromatin <= 6|1 (17.0)
Clump_Thickness > 8|1 (20.0)
Cell_Shape_Uniformity <= 2 AND Cell_Size_Uniformity <= 1|0 (6.08/1.0)
Cell_Shape_Uniformity > 2 AND Bland_Chromatin > 4 AND Bare_Nuclei > 7 AND Marginal_Adhesion <= 5|1 (10.0)
Cell_Shape_Uniformity > 2 AND Normal_Nucleoli <= 6 AND Marginal_Adhesion <= 5 AND Cell_Size_Uniformity > 3 AND Normal_Nucleoli > 3|1 (9.0/2.0)
Marginal_Adhesion > 5|1 (10.0/1.0)
Normal_Nucleoli <= 2|0 (7.08/1.0)
Single_Epi_Cell_Size <= 4 AND Cell_Shape_Uniformity > 3|0 (7.0/3.0)
Cell_Shape_Uniformity <= 3|0 (6.0/2.0)
|1 (6.0/1.0)


## J48 Decision Tree

* Cell_Size_Uniformity <= 3.0
	* Normal_Nucleoli <= 2.0
		* Bare_Nuclei <= 2.0: 0 (281.58)
		* Bare_Nuclei > 2.0
			* Bare_Nuclei <= 5.0
				* Clump_Thickness <= 3.0: 0 (13.34)
				* Clump_Thickness > 3.0
					* Bland_Chromatin <= 1.0: 0 (2.0)
					* Bland_Chromatin > 1.0: 1 (2.0)
			* Bare_Nuclei > 5.0: 1 (4.08/0.08)
	* Normal_Nucleoli > 2.0
		* Bare_Nuclei <= 2.0: 0 (8.0/1.0)
		* Bare_Nuclei > 2.0
			* Cell_Size_Uniformity <= 2.0: 1 (6.0)
			* Cell_Size_Uniformity > 2.0
				* Cell_Shape_Uniformity <= 4.0
					* Normal_Nucleoli <= 4.0: 1 (4.0)
					* Normal_Nucleoli > 4.0: 0 (3.0/1.0)
				* Cell_Shape_Uniformity > 4.0: 1 (6.0)
* Cell_Size_Uniformity > 3.0
	* Cell_Size_Uniformity <= 4.0
		* Marginal_Adhesion <= 5.0
			* Clump_Thickness <= 6.0: 0 (6.0)
			* Clump_Thickness > 6.0: 1 (13.0/2.0)
		* Marginal_Adhesion > 5.0: 1 (11.0)
	* Cell_Size_Uniformity > 4.0
		* Clump_Thickness <= 6.0
			* Marginal_Adhesion <= 1.0
				* Cell_Shape_Uniformity <= 6.0: 1 (2.0)
				* Cell_Shape_Uniformity > 6.0: 0 (2.0)
			* Marginal_Adhesion > 1.0: 1 (50.0/2.0)
		* Clump_Thickness > 6.0: 1 (72.0)


