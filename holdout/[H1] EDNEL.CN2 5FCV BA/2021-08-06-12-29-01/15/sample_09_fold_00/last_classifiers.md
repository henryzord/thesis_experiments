# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity < 2.5 and Bare_Nuclei < 5.5 | 0 | 0.630799 |
| Cell_Size_Uniformity >= 2.5 and Cell_Shape_Uniformity >= 2.5 and Cell_Size_Uniformity >= 4.5 and Clump_Thickness >= 6.5 | 1 | 0.179028 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 9.5 and Bare_Nuclei > 5.5 | 1 | 0.170866 |
| Cell_Size_Uniformity >= 2.5 and Cell_Shape_Uniformity >= 2.5 and Cell_Size_Uniformity >= 4.5 and Clump_Thickness < 6.5 and Bland_Chromatin >= 4.5 and Clump_Thickness < 5.5 | 1 | 0.080229 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 3.5 and Bare_Nuclei <= 2.5 | 0 | 0.091892 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 3.5 and Bare_Nuclei > 5.5 | 1 | 0.033364 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 3.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 5.5 | 1 | 0.015195 |
| Cell_Size_Uniformity <= 2.5 and Bare_Nuclei > 3.5 and Clump_Thickness > 3.5 and Bare_Nuclei > 5.5 | 1 | 0.018349 |
| Cell_Size_Uniformity > 9.5 and Bare_Nuclei > 5.5 | 1 | 0.090652 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity > 3.5 and Bare_Nuclei <= 8.5 and Clump_Thickness <= 8.5 and Cell_Size_Uniformity <= 9.5 and Normal_Nucleoli <= 9.5 and Single_Epi_Cell_Size <= 8.5 and Bland_Chromatin <= 7.5 and Clump_Thickness > 3.5 and Cell_Shape_Uniformity > 4.5 and Bland_Chromatin <= 5.5 and Clump_Thickness <= 6.5 | 0 | 0.023256 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity > 3.5 and Bare_Nuclei <= 8.5 and Clump_Thickness <= 8.5 and Cell_Size_Uniformity <= 9.5 and Normal_Nucleoli <= 9.5 and Single_Epi_Cell_Size <= 8.5 and Bland_Chromatin <= 7.5 and Clump_Thickness > 3.5 and Cell_Shape_Uniformity <= 4.5 | 0 | 0.023256 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 9.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 5.5 | 1 | 0.040541 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity > 3.5 and Bare_Nuclei <= 8.5 and Clump_Thickness <= 8.5 and Cell_Size_Uniformity > 9.5 | 1 | 0.036036 |
| Cell_Size_Uniformity >= 2.5 and Cell_Shape_Uniformity < 2.5 and Clump_Thickness < 5.5 | 0 | 0.067063 |
| Cell_Size_Uniformity <= 2.5 and Bare_Nuclei > 3.5 and Clump_Thickness > 3.5 and Bare_Nuclei <= 5.5 and Marginal_Adhesion <= 3.5 | 1 | 0.006192 |
| Cell_Size_Uniformity < 2.5 and Bare_Nuclei >= 5.5 and Clump_Thickness < 3.5 | 0 | 0.005917 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity <= 3.5 and Bare_Nuclei > 2.5 and Clump_Thickness <= 6.5 and Normal_Nucleoli > 4.5 and Cell_Shape_Uniformity <= 3.5 | 0 | 0.011765 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 9.5 and Bare_Nuclei <= 1.5 | 1 | 0.012821 |
| Cell_Size_Uniformity > 2.5 and Cell_Size_Uniformity > 3.5 and Bare_Nuclei <= 8.5 and Clump_Thickness <= 8.5 and Cell_Size_Uniformity <= 9.5 and Normal_Nucleoli <= 9.5 and Single_Epi_Cell_Size <= 8.5 and Bland_Chromatin <= 7.5 and Clump_Thickness > 3.5 and Cell_Shape_Uniformity > 4.5 and Bland_Chromatin <= 5.5 and Clump_Thickness > 6.5 | 0 | 0.002976 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 9.5 and Bare_Nuclei = ? | 0 | 0.013235 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity <= 2.5 and Bare_Nuclei <= 3.5 | 0 | 0.615561 |
| Cell_Shape_Uniformity > 2.5 and Bare_Nuclei > 8.5 and Clump_Thickness > 6.5 | 1 | 0.522936 |
| Bland_Chromatin > 2.5 and Cell_Shape_Uniformity > 4.5 and Bland_Chromatin > 4.5 | 1 | 0.518678 |
| Clump_Thickness <= 8.5 and Bland_Chromatin <= 2.5 and Marginal_Adhesion <= 2.5 | 0 | 0.325000 |
| Clump_Thickness <= 8.5 and Clump_Thickness > 1.5 and Single_Epi_Cell_Size <= 7.5 and Bare_Nuclei > 2.5 | 1 | 0.468900 |
| Clump_Thickness > 4.5 and Mitoses > 1.5 | 1 | 0.385714 |
| Cell_Size_Uniformity <= 5 and Bare_Nuclei <= 3.5 | 0 | 0.555556 |
| Cell_Size_Uniformity > 4.5 | 1 | 0.192513 |
|  | 0 | 0.888889 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity >= 3 and Bare_Nuclei >= 9 and Cell_Shape_Uniformity >= 4 | 1 | 0.207407 |
| Clump_Thickness >= 7 and Cell_Size_Uniformity >= 5 | 1 | 0.098315 |
| Bland_Chromatin >= 4 and Clump_Thickness >= 5 and Cell_Shape_Uniformity <= 3 | 1 | 0.041791 |
| Marginal_Adhesion >= 4 and Bare_Nuclei <= 6 and Cell_Shape_Uniformity >= 5 | 1 | 0.025329 |
| Bare_Nuclei >= 3 and Cell_Shape_Uniformity >= 3 and Normal_Nucleoli >= 9 | 1 | 0.015776 |
| Bare_Nuclei >= 3 and Cell_Shape_Uniformity >= 3 and Normal_Nucleoli <= 6 and Marginal_Adhesion >= 3 and Clump_Thickness <= 5 and Single_Epi_Cell_Size <= 5 | 1 | 0.021341 |
| Bare_Nuclei >= 3 and Clump_Thickness >= 7 and Marginal_Adhesion <= 4 | 1 | 0.018349 |
| Single_Epi_Cell_Size >= 6 and Bare_Nuclei >= 8 | 1 | 0.009259 |
|  | 0 | 0.990741 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cell_size_uniformity|bare_nuclei|target
---|---|---
(1.5-2.5]|(5.5-inf)|1
(-inf-1.5]|(5.5-inf)|0
(9.5-inf)|(5.5-inf)|1
(2.5-3.5]|(5.5-inf)|1
(3.5-9.5]|(5.5-inf)|1
(3.5-9.5]|?|0
(-inf-1.5]|?|0
(9.5-inf)|(1.5-5.5]|1
(1.5-2.5]|(1.5-5.5]|0
(2.5-3.5]|(1.5-5.5]|1
(3.5-9.5]|(1.5-5.5]|1
(-inf-1.5]|(1.5-5.5]|0
(9.5-inf)|(-inf-1.5]|1
(3.5-9.5]|(-inf-1.5]|1
(2.5-3.5]|(-inf-1.5]|0
(1.5-2.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Size_Uniformity >= 3) and (Bare_Nuclei >= 9) and (Cell_Shape_Uniformity >= 4)|1 (84.0/0.0)
(Clump_Thickness >= 7) and (Cell_Size_Uniformity >= 5)|1 (35.0/0.0)
(Bland_Chromatin >= 4) and (Clump_Thickness >= 5) and (Cell_Shape_Uniformity <= 3)|1 (14.0/0.0)
(Marginal_Adhesion >= 4) and (Bare_Nuclei <= 6) and (Cell_Shape_Uniformity >= 5)|1 (10.0/0.0)
(Bare_Nuclei >= 3) and (Cell_Shape_Uniformity >= 3) and (Normal_Nucleoli >= 9)|1 (6.0/0.0)
(Bare_Nuclei >= 3) and (Cell_Shape_Uniformity >= 3) and (Normal_Nucleoli <= 6) and (Marginal_Adhesion >= 3) and (Clump_Thickness <= 5) and (Single_Epi_Cell_Size <= 5)|1 (7.0/0.0)
(Bare_Nuclei >= 3) and (Clump_Thickness >= 7) and (Marginal_Adhesion <= 4)|1 (5.0/0.0)
(Single_Epi_Cell_Size >= 6) and (Bare_Nuclei >= 8)|1 (3.0/0.0)
|0 (325.0/4.0)


## PART

Decision list:

rules | predicted class
---|---
Cell_Size_Uniformity <= 2.5 AND Bare_Nuclei <= 3.5|0 (278.34)
Cell_Shape_Uniformity > 2.5 AND Bare_Nuclei > 8.5 AND Clump_Thickness > 6.5|1 (57.54)
Bland_Chromatin > 2.5 AND Cell_Shape_Uniformity > 4.5 AND Bland_Chromatin > 4.5|1 (57.46/1.0)
Clump_Thickness <= 8.5 AND Bland_Chromatin <= 2.5 AND Marginal_Adhesion <= 2.5|0 (19.46)
Clump_Thickness <= 8.5 AND Clump_Thickness > 1.5 AND Single_Epi_Cell_Size <= 7.5 AND Bare_Nuclei > 2.5|1 (40.02/12.02)
Clump_Thickness > 4.5 AND Mitoses > 1.5|1 (18.0)
Cell_Size_Uniformity <= 5 AND Bare_Nuclei <= 3.5|0 (8.02)
Cell_Size_Uniformity > 4.5|1 (6.15/0.15)
|0 (4.01/2.0)


## J48 Decision Tree

* Cell_Size_Uniformity <= 2.5
	* Bare_Nuclei <= 3.5: 0 (278.34)
	* Bare_Nuclei > 3.5
		* Clump_Thickness <= 3.5: 0 (9.66)
		* Clump_Thickness > 3.5
			* Bare_Nuclei <= 5.5
				* Marginal_Adhesion <= 3.5: 1 (2.0)
				* Marginal_Adhesion > 3.5: 0 (2.0)
			* Bare_Nuclei > 5.5: 1 (6.0)
* Cell_Size_Uniformity > 2.5
	* Cell_Size_Uniformity <= 3.5
		* Bare_Nuclei <= 2.5: 0 (17.0)
		* Bare_Nuclei > 2.5
			* Clump_Thickness <= 6.5
				* Normal_Nucleoli <= 4.5
					* Cell_Shape_Uniformity <= 2.5: 1 (3.0/1.0)
					* Cell_Shape_Uniformity > 2.5: 1 (7.0)
				* Normal_Nucleoli > 4.5
					* Cell_Shape_Uniformity <= 3.5: 0 (2.0)
					* Cell_Shape_Uniformity > 3.5: 1 (3.0/1.0)
			* Clump_Thickness > 6.5: 1 (9.0)
	* Cell_Size_Uniformity > 3.5
		* Bare_Nuclei <= 8.5
			* Clump_Thickness <= 8.5
				* Cell_Size_Uniformity <= 9.5
					* Normal_Nucleoli <= 9.5
						* Single_Epi_Cell_Size <= 8.5
							* Bland_Chromatin <= 7.5
								* Clump_Thickness <= 3.5: 1 (2.0)
								* Clump_Thickness > 3.5
									* Cell_Shape_Uniformity <= 4.5: 0 (3.43)
									* Cell_Shape_Uniformity > 4.5
										* Bland_Chromatin <= 5.5
											* Clump_Thickness <= 6.5: 0 (3.43)
											* Clump_Thickness > 6.5: 0 (2.0/1.0)
										* Bland_Chromatin > 5.5
											* Cell_Size_Uniformity <= 5.5: 1 (2.43)
											* Cell_Size_Uniformity > 5.5: 1 (2.43/0.43)
							* Bland_Chromatin > 7.5: 1 (3.0)
						* Single_Epi_Cell_Size > 8.5: 1 (4.0)
					* Normal_Nucleoli > 9.5: 1 (7.0)
				* Cell_Size_Uniformity > 9.5: 1 (12.0)
			* Clump_Thickness > 8.5: 1 (23.0)
		* Bare_Nuclei > 8.5
			* Clump_Thickness <= 6.5
				* Cell_Shape_Uniformity <= 6.5
					* Single_Epi_Cell_Size <= 4.5
						* Cell_Size_Uniformity <= 4.5: 1 (2.57/0.57)
						* Cell_Size_Uniformity > 4.5: 1 (7.0)
					* Single_Epi_Cell_Size > 4.5: 0 (2.14/1.0)
				* Cell_Shape_Uniformity > 6.5: 1 (21.0)
			* Clump_Thickness > 6.5: 1 (52.57)


## SimpleCart Decision Tree

* Cell_Size_Uniformity < 2.5
	* Bare_Nuclei < 5.5: 0(288.75/2.0)
	* Bare_Nuclei >= 5.5
		* Clump_Thickness < 3.5: 0(1.24/0.0)
		* Clump_Thickness >= 3.5: 1(6.0/0.0)
* Cell_Size_Uniformity >= 2.5
	* Cell_Shape_Uniformity < 2.5
		* Clump_Thickness < 5.5: 0(13.0/1.0)
		* Clump_Thickness >= 5.5: 1(3.0/0.0)
	* Cell_Shape_Uniformity >= 2.5
		* Cell_Size_Uniformity < 4.5
			* Bare_Nuclei < 2.5: 0(7.15/1.15)
			* Bare_Nuclei >= 2.5
				* Cell_Shape_Uniformity < 4.5
					* Clump_Thickness < 6.5
						* Cell_Size_Uniformity < 3.5: 1(6.0/2.0)
						* Cell_Size_Uniformity >= 3.5: 0(2.84/0.0)
					* Clump_Thickness >= 6.5
						* Normal_Nucleoli < 7.0: 1(12.0/0.0)
						* Normal_Nucleoli >= 7.0: 0(1.0/1.0)
				* Cell_Shape_Uniformity >= 4.5: 1(21.84/0.0)
		* Cell_Size_Uniformity >= 4.5
			* Clump_Thickness < 6.5
				* Bland_Chromatin < 4.5
					* Marginal_Adhesion < 7.0
						* Clump_Thickness < 5.5
							* Single_Epi_Cell_Size < 4.5: 1(3.0/0.0)
							* Single_Epi_Cell_Size >= 4.5
								* Single_Epi_Cell_Size < 8.5: 0(2.0/0.0)
								* Single_Epi_Cell_Size >= 8.5: 1(2.0/0.0)
						* Clump_Thickness >= 5.5: 0(2.0/0.0)
					* Marginal_Adhesion >= 7.0: 1(4.0/0.0)
				* Bland_Chromatin >= 4.5
					* Clump_Thickness < 5.5: 1(28.0/0.0)
					* Clump_Thickness >= 5.5
						* Mitoses < 1.5: 0(1.0/1.0)
						* Mitoses >= 1.5: 1(6.0/0.0)
			* Clump_Thickness >= 6.5: 1(70.0/0.0)


