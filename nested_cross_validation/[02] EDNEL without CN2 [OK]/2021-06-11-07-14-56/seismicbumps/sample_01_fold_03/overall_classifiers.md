# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| nbumps <= 1 and gpuls <= 1421 | 0 | 0.919020 |
| nbumps > 1 | 0 | 0.697557 |
| nbumps <= 1 and gpuls > 1421 and nbumps3 <= 0 | 0 | 0.229191 |
| nbumps <= 1 and gpuls > 1421 and nbumps3 > 0 | 1 | 0.002195 |

## Ordered rules

# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

class
---
0

## J48 Decision Tree

* nbumps <= 1
	* gpuls <= 1421: 0 (1478.0/37.0)
	* gpuls > 1421
		* nbumps3 <= 0: 0 (43.0/4.0)
		* nbumps3 > 0: 1 (16.0/8.0)
* nbumps > 1: 0 (397.0/76.0)


## SimpleCart Decision Tree

* : 0(2170.0/150.0)


