# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F21R <= 60.0 | 1 | 0.589744 |
| F21R > 60.0 and F2S <= 65.0 | 1 | 0.428571 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S > 56.0 and F17R <= 64.0 and F11S > 70.0 and F17S <= 64.0 and F22R <= 64.0 | 1 | 0.270089 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S <= 63.0 | 1 | 0.261538 |
| F13S > 57.5 and F17R > 62.5 and F18R = all and F20S > 71.5 | 0 | 0.065032 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S <= 56.0 | 1 | 0.226815 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S > 56.0 and F17R <= 64.0 and F11S <= 70.0 | 1 | 0.186441 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S > 56.0 and F17R > 64.0 | 0 | 0.074198 |
| F21R > 60.0 and F2S > 65.0 and F4R <= 64.0 | 1 | 0.186441 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S > 56.0 and F17R <= 64.0 and F11S > 70.0 and F17S <= 64.0 and F22R > 64.0 | 0 | 0.025258 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S <= 77.0 and F20S > 63.0 and F14S > 56.0 and F17R <= 64.0 and F11S > 70.0 and F17S > 64.0 | 0 | 0.037379 |
| F13S > 57.5 and F17R > 62.5 and F18R = all and F20S > 61.5 and F20S <= 71.5 | 1 | 0.178896 |
| F21R > 60.0 and F2S > 65.0 and F4R > 64.0 and F16S > 77.0 | 0 | 0.032653 |
| F13S <= 57.5 and F17R > 62.5 and F18R = all and F20S > 61.5 and F20S <= 71.5 | 1 | 0.250000 |
| F13S <= 57.5 and F17R <= 62.5 and F18R = all and F20S > 71.5 | 1 | 0.226815 |
| F13S > 57.5 and F17R <= 62.5 and F18R = all and F20S > 71.5 | 1 | 0.191138 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F21R <= 60.5 | 1 | 0.589744 |
| F2S <= 65.5 | 1 | 0.428571 |
| F4R > 64.5 and F20S <= 71.5 and F11S <= 69.5 | 1 | 0.304348 |
| F4R > 64.5 and F17R > 63.5 and F22S > 53 and F15S > 67.5 | 0 | 0.228916 |
| F4S <= 65.5 | 1 | 0.340909 |
| F22R > 64.5 and F16S > 74.5 | 0 | 0.040816 |
| F22R <= 64.5 and F14S <= 59.5 and F7S <= 70 | 1 | 0.285714 |
| F21R <= 74.5 and F10R > 70.5 and F12S > 68.5 | 1 | 0.404762 |
| F22S <= 63.5 and F11R > 73.5 and F17S <= 64.5 and F6S > 73.5 | 0 | 0.178182 |
| F22S > 63.5 | 0 | 0.241071 |
| F17S <= 64 and F17S > 60 | 1 | 0.590909 |
| F1R <= 65.5 | 1 | 0.388889 |
|  | 0 | 0.818182 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| F20S >= 72 and F17R >= 63 and F3S >= 68 and F9S >= 64 | 0 | 0.068627 |
| F13S >= 58 and F7S >= 73 and F8S <= 66 and F6R >= 73 and F4S >= 66 | 0 | 0.054726 |
| F22R >= 56 and F11S >= 72 and F17R >= 65 and F3S >= 68 | 0 | 0.040404 |
|  | 1 | 0.926829 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

f13s|f17r|f18r|f20s|overall_diagnosis
---|---|---|---|---
(-inf-57.5]|(62.5-inf)|all|(71.5-inf)|0
(57.5-inf)|(62.5-inf)|all|(71.5-inf)|0
(57.5-inf)|(-inf-62.5]|all|(71.5-inf)|1
(-inf-57.5]|(-inf-62.5]|all|(71.5-inf)|1
(-inf-57.5]|(62.5-inf)|all|(61.5-71.5]|1
(57.5-inf)|(62.5-inf)|all|(61.5-71.5]|1
(-inf-57.5]|(-inf-62.5]|all|(61.5-71.5]|1
(57.5-inf)|(-inf-62.5]|all|(61.5-71.5]|1
(57.5-inf)|(62.5-inf)|all|(-inf-61.5]|1
(-inf-57.5]|(62.5-inf)|all|(-inf-61.5]|1
(57.5-inf)|(-inf-62.5]|all|(-inf-61.5]|1
(-inf-57.5]|(-inf-62.5]|all|(-inf-61.5]|1

## JRip

Decision list:

rules | predicted class
---|---
(F20S >= 72) and (F17R >= 63) and (F3S >= 68) and (F9S >= 64)|0 (14.0/0.0)
(F13S >= 58) and (F7S >= 73) and (F8S <= 66) and (F6R >= 73) and (F4S >= 66)|0 (11.0/0.0)
(F22R >= 56) and (F11S >= 72) and (F17R >= 65) and (F3S >= 68)|0 (8.0/0.0)
|1 (205.0/15.0)


## PART

Decision list:

rules | predicted class
---|---
F21R <= 60.5|1 (69.0)
F2S <= 65.5|1 (36.0)
F4R > 64.5 AND F20S <= 71.5 AND F11S <= 69.5|1 (21.0)
F4R > 64.5 AND F17R > 63.5 AND F22S > 53 AND F15S > 67.5|0 (19.0)
F4S <= 65.5|1 (15.0)
F22R > 64.5 AND F16S > 74.5|0 (8.0/4.0)
F22R <= 64.5 AND F14S <= 59.5 AND F7S <= 70|1 (10.0)
F21R <= 74.5 AND F10R > 70.5 AND F12S > 68.5|1 (17.0)
F22S <= 63.5 AND F11R > 73.5 AND F17S <= 64.5 AND F6S > 73.5|0 (10.0/3.0)
F22S > 63.5|0 (9.0)
F17S <= 64 AND F17S > 60|1 (8.0)
F1R <= 65.5|1 (8.0/2.0)
|0 (8.0/1.0)


## J48 Decision Tree

* F21R <= 60.0: 1 (69.0)
* F21R > 60.0
	* F2S <= 65.0: 1 (36.0)
	* F2S > 65.0
		* F4R <= 64.0: 1 (11.0)
		* F4R > 64.0
			* F16S <= 77.0
				* F20S <= 63.0: 1 (17.0)
				* F20S > 63.0
					* F14S <= 56.0: 1 (16.0/1.0)
					* F14S > 56.0
						* F17R <= 64.0
							* F11S <= 70.0: 1 (11.0)
							* F11S > 70.0
								* F17S <= 64.0
									* F22R <= 64.0: 1 (28.0/6.0)
									* F22R > 64.0: 0 (10.0/3.0)
								* F17S > 64.0: 0 (11.0/2.0)
						* F17R > 64.0: 0 (19.0/2.0)
			* F16S > 77.0: 0 (10.0/2.0)


## SimpleCart Decision Tree

* : 1(190.0/48.0)


