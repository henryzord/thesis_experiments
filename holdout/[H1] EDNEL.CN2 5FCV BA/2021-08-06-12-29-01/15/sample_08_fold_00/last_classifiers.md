# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Shape_Uniformity < 3.5 and Bare_Nuclei < 5.5 | 0 | 0.648930 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion >= 1.5 and Cell_Shape_Uniformity >= 4.5 and Bare_Nuclei >= 1.5 and Clump_Thickness >= 4.5 | 1 | 0.230404 |
| Cell_Size_Uniformity > 4.5 and Bare_Nuclei > 5.5 | 1 | 0.202000 |
| Cell_Shape_Uniformity < 3.5 and Bare_Nuclei >= 5.5 and Clump_Thickness >= 3.5 | 1 | 0.035927 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion < 1.5 and Clump_Thickness >= 7.0 | 1 | 0.024096 |
| Cell_Size_Uniformity > 4.5 and Bare_Nuclei <= 1.5 | 1 | 0.015198 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion >= 1.5 and Cell_Shape_Uniformity < 4.5 and Cell_Size_Uniformity < 5.0 and Marginal_Adhesion >= 5.5 | 1 | 0.015198 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity < 2.5 | 0 | 0.025100 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion < 1.5 and Clump_Thickness < 7.0 | 0 | 0.025100 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion >= 1.5 and Cell_Shape_Uniformity >= 4.5 and Bare_Nuclei >= 1.5 and Clump_Thickness < 4.5 | 1 | 0.044421 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion >= 1.5 and Cell_Shape_Uniformity < 4.5 and Cell_Size_Uniformity < 5.0 and Marginal_Adhesion < 5.5 | 0 | 0.024096 |
| Cell_Size_Uniformity > 4.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 5.5 | 1 | 0.066709 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 4.5 and Bare_Nuclei > 1.5 and Bare_Nuclei <= 5.5 | 1 | 0.005538 |
| Cell_Shape_Uniformity >= 3.5 and Cell_Size_Uniformity >= 2.5 and Marginal_Adhesion >= 1.5 and Cell_Shape_Uniformity >= 4.5 and Bare_Nuclei < 1.5 | 1 | 0.012703 |
| Cell_Size_Uniformity <= 1.5 and Bare_Nuclei > 5.5 | 0 | 0.002070 |
| Cell_Size_Uniformity > 4.5 and Bare_Nuclei = ? | 0 | 0.003086 |
| Cell_Size_Uniformity > 3.5 and Cell_Size_Uniformity <= 4.5 and Bare_Nuclei <= 1.5 | 0 | 0.006173 |

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Cell_Size_Uniformity >= 4 | 1 | 0.279658 |
| Bare_Nuclei >= 4 and Cell_Size_Uniformity >= 2 | 1 | 0.042517 |
| Normal_Nucleoli >= 4 and Clump_Thickness >= 5 | 1 | 0.011598 |
|  | 0 | 0.996923 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

cell_size_uniformity|bare_nuclei|target
---|---|---
(1.5-2.5]|(5.5-inf)|1
(-inf-1.5]|(5.5-inf)|0
(3.5-4.5]|(5.5-inf)|1
(2.5-3.5]|(5.5-inf)|1
(4.5-inf)|(5.5-inf)|1
(3.5-4.5]|?|0
(-inf-1.5]|?|0
(4.5-inf)|?|0
(1.5-2.5]|(1.5-5.5]|0
(-inf-1.5]|(1.5-5.5]|0
(3.5-4.5]|(1.5-5.5]|1
(4.5-inf)|(1.5-5.5]|1
(2.5-3.5]|(1.5-5.5]|0
(1.5-2.5]|(-inf-1.5]|0
(2.5-3.5]|(-inf-1.5]|0
(-inf-1.5]|(-inf-1.5]|0
(4.5-inf)|(-inf-1.5]|1
(3.5-4.5]|(-inf-1.5]|0

## JRip

Decision list:

rules | predicted class
---|---
(Cell_Size_Uniformity >= 4)|1 (143.0/9.0)
(Bare_Nuclei >= 4) and (Cell_Size_Uniformity >= 2)|1 (23.0/3.0)
(Normal_Nucleoli >= 4) and (Clump_Thickness >= 5)|1 (7.0/0.0)
|0 (313.0/1.0)


## SimpleCart Decision Tree

* Cell_Shape_Uniformity < 3.5
	* Bare_Nuclei < 5.5: 0(305.62/7.0)
	* Bare_Nuclei >= 5.5
		* Clump_Thickness < 3.5: 0(1.28/0.0)
		* Clump_Thickness >= 3.5: 1(13.0/1.09)
* Cell_Shape_Uniformity >= 3.5
	* Cell_Size_Uniformity < 2.5: 0(5.0/1.0)
	* Cell_Size_Uniformity >= 2.5
		* Marginal_Adhesion < 1.5
			* Clump_Thickness < 7.0: 0(5.0/1.0)
			* Clump_Thickness >= 7.0: 1(8.0/0.0)
		* Marginal_Adhesion >= 1.5
			* Cell_Shape_Uniformity < 4.5
				* Cell_Size_Uniformity < 5.0
					* Marginal_Adhesion < 5.5: 0(4.0/0.0)
					* Marginal_Adhesion >= 5.5: 1(5.0/0.0)
				* Cell_Size_Uniformity >= 5.0: 1(9.0/0.0)
			* Cell_Shape_Uniformity >= 4.5
				* Bare_Nuclei < 1.5: 1(5.0/1.05)
				* Bare_Nuclei >= 1.5
					* Clump_Thickness < 4.5: 1(16.0/0.94)
					* Clump_Thickness >= 4.5: 1(97.0/0.0)


