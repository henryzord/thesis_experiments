# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F21R <= 60.5 | 1 | 0.589744 |
| F21R > 60.5 and F2S <= 65.5 | 1 | 0.428571 |
| F3S > 64.5 and F5R = all and F6R = all and F7R = all and F19S = all and F20S > 61.5 and F20S <= 71.5 | 1 | 0.429936 |
| F3S > 64.5 and F5R = all and F6R = all and F7R = all and F19S = all and F20S > 71.5 | 0 | 0.083707 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S <= 71.5 and F11S <= 69.5 | 1 | 0.304348 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R <= 65.5 and F17R <= 64.5 and F11S <= 70.5 | 1 | 0.142857 |
| F3S <= 64.5 and F5R = all and F6R = all and F7R = all and F19S = all and F20S > 61.5 and F20S <= 71.5 | 1 | 0.431122 |
| F3S > 64.5 and F5R = all and F6R = all and F7R = all and F19S = all and F20S <= 61.5 | 1 | 0.294118 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S <= 71.5 and F11S > 69.5 and F8S > 60.5 and F18S <= 67.5 and F15S > 67.0 | 0 | 0.040404 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R <= 65.5 and F17R <= 64.5 and F11S > 70.5 and F1S <= 73.5 and F20R <= 71.5 | 1 | 0.111111 |
| F21R > 60.5 and F2S > 65.5 and F4R <= 64.5 | 1 | 0.186441 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R <= 65.5 and F17R <= 64.5 and F11S > 70.5 and F1S <= 73.5 and F20R > 71.5 and F21S <= 74.5 and F18S <= 63.5 | 1 | 0.094340 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S <= 71.5 and F11S > 69.5 and F8S > 60.5 and F18S <= 67.5 and F15S <= 67.0 and F21S > 72.5 | 0 | 0.020619 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S <= 71.5 and F11S > 69.5 and F8S > 60.5 and F18S <= 67.5 and F15S <= 67.0 and F21S <= 72.5 and F18S <= 64.5 | 0 | 0.009424 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R <= 65.5 and F17R <= 64.5 and F11S > 70.5 and F1S <= 73.5 and F20R > 71.5 and F21S <= 74.5 and F18S > 63.5 and F20S > 75.5 | 1 | 0.045000 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R > 65.5 | 0 | 0.040404 |
| F3S <= 64.5 and F5R = all and F6R = all and F7R = all and F19S = all and F20S <= 61.5 | 1 | 0.494737 |
| F21R > 60.5 and F2S > 65.5 and F4R > 64.5 and F20S > 71.5 and F22R <= 65.5 and F17R > 64.5 | 0 | 0.050417 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F21R <= 60 | 1 | 0.589744 |
| F2S <= 65 | 1 | 0.428571 |
| F4R > 64 and F20S <= 71 and F11S <= 69 | 1 | 0.304348 |
| F4R > 64 and F17R > 63 and F22S > 53 and F15S > 67 | 0 | 0.228916 |
| F4S <= 65 | 1 | 0.340909 |
| F22R > 64 and F16S > 74 | 0 | 0.040816 |
| F22R <= 64 and F14S <= 59 and F7S <= 70 | 1 | 0.285714 |
| F21R <= 74 and F10R > 70 and F12S > 68 | 1 | 0.404762 |
| F22S <= 63 and F11R > 73 and F17S <= 64 and F6S > 73 | 0 | 0.178182 |
| F22S > 63 | 0 | 0.241071 |
| F17S <= 64 and F17S > 60 | 1 | 0.590909 |
| F1R <= 65 | 1 | 0.388889 |
|  | 0 | 0.818182 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F20S >= 72 and F17R >= 63 and F3S >= 68 and F9S >= 64 | 0 | 0.068627 |
| F13S >= 58 and F7S >= 73 and F8S <= 66 and F6R >= 73 and F4S >= 66 | 0 | 0.054726 |
| F22R >= 56 and F11S >= 72 and F17R >= 65 and F3S >= 68 | 0 | 0.040404 |
| F20S >= 68 and F22R >= 66 and F19S >= 69 and F1S >= 58 | 0 | 0.025641 |
| F13S >= 61 and F19S >= 71 and F17S <= 60 and F1R >= 66 | 0 | 0.020619 |
| F12S >= 72 and F11S >= 80 and F8S >= 64 | 0 | 0.015544 |
| F13R >= 75 and F2S >= 70 and F1R <= 64 | 0 | 0.010417 |
|  | 1 | 0.994764 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

f3s|f5r|f6r|f7r|f19s|f20s|overall_diagnosis
---|---|---|---|---|---|---
(64.5-inf)|all|all|all|all|(71.5-inf)|0
(-inf-64.5]|all|all|all|all|(71.5-inf)|1
(64.5-inf)|all|all|all|all|(61.5-71.5]|1
(-inf-64.5]|all|all|all|all|(61.5-71.5]|1
(-inf-64.5]|all|all|all|all|(-inf-61.5]|1
(64.5-inf)|all|all|all|all|(-inf-61.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(F20S >= 72) and (F17R >= 63) and (F3S >= 68) and (F9S >= 64)|0 (14.0/0.0)
(F13S >= 58) and (F7S >= 73) and (F8S <= 66) and (F6R >= 73) and (F4S >= 66)|0 (11.0/0.0)
(F22R >= 56) and (F11S >= 72) and (F17R >= 65) and (F3S >= 68)|0 (8.0/0.0)
(F20S >= 68) and (F22R >= 66) and (F19S >= 69) and (F1S >= 58)|0 (5.0/0.0)
(F13S >= 61) and (F19S >= 71) and (F17S <= 60) and (F1R >= 66)|0 (4.0/0.0)
(F12S >= 72) and (F11S >= 80) and (F8S >= 64)|0 (3.0/0.0)
(F13R >= 75) and (F2S >= 70) and (F1R <= 64)|0 (2.0/0.0)
|1 (191.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
F21R <= 60|1 (69.0)
F2S <= 65|1 (36.0)
F4R > 64 AND F20S <= 71 AND F11S <= 69|1 (21.0)
F4R > 64 AND F17R > 63 AND F22S > 53 AND F15S > 67|0 (19.0)
F4S <= 65|1 (15.0)
F22R > 64 AND F16S > 74|0 (8.0/4.0)
F22R <= 64 AND F14S <= 59 AND F7S <= 70|1 (10.0)
F21R <= 74 AND F10R > 70 AND F12S > 68|1 (17.0)
F22S <= 63 AND F11R > 73 AND F17S <= 64 AND F6S > 73|0 (10.0/3.0)
F22S > 63|0 (9.0)
F17S <= 64 AND F17S > 60|1 (8.0)
F1R <= 65|1 (8.0/2.0)
|0 (8.0/1.0)


## J48 Decision Tree

* F21R <= 60.5: 1 (69.0)
* F21R > 60.5
	* F2S <= 65.5: 1 (36.0)
	* F2S > 65.5
		* F4R <= 64.5: 1 (11.0)
		* F4R > 64.5
			* F20S <= 71.5
				* F11S <= 69.5: 1 (21.0)
				* F11S > 69.5
					* F8S <= 60.5: 1 (9.0)
					* F8S > 60.5
						* F18S <= 67.5
							* F15S <= 67.0
								* F21S <= 72.5
									* F18S <= 64.5: 0 (5.0/2.0)
									* F18S > 64.5: 1 (8.0)
								* F21S > 72.5: 0 (4.0)
							* F15S > 67.0: 0 (8.0)
						* F18S > 67.5: 1 (12.0/1.0)
			* F20S > 71.5
				* F22R <= 65.5
					* F17R <= 64.5
						* F11S <= 70.5: 1 (8.0)
						* F11S > 70.5
							* F1S <= 73.5
								* F20R <= 71.5: 1 (6.0)
								* F20R > 71.5
									* F21S <= 74.5
										* F18S <= 63.5: 1 (5.0)
										* F18S > 63.5
											* F20S <= 75.5: 0 (4.0)
											* F20S > 75.5: 1 (4.0/1.0)
									* F21S > 74.5: 0 (3.0)
							* F1S > 73.5: 0 (5.0)
					* F17R > 64.5: 0 (12.0/1.0)
				* F22R > 65.5: 0 (8.0)


## SimpleCart Decision Tree

* : 1(190.0/48.0)


