# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| A2 >= 3 and A4 >= 2 | 0 | 0.298969 |
| A5 >= 4 | 0 | 0.271429 |
| A2 >= 3 and A5 <= 2 | 0 | 0.089286 |
|  | 1 | 1.000000 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(A2 >= 3) and (A4 >= 2)|0 (87.0/0.0)
(A5 >= 4)|0 (76.0/0.0)
(A2 >= 3) and (A5 <= 2)|0 (20.0/0.0)
|1 (204.0/0.0)


