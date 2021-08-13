# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 <= 0.5397805 | 1 | 0.854851 |
| vconst_corr <= 0.4685555 | 1 | 0.698380 |
| convect_corr <= 0.39011 | 1 | 0.405451 |
| vconst_2 <= 0.8354865 and vconst_corr <= 0.9298095 | 1 | 0.290698 |
|  | 0 | 0.875000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
vconst_2 <= 0.5397805|1 (142.0/1.0)
vconst_corr <= 0.4685555|1 (60.0)
convect_corr <= 0.39011|1 (18.0/2.0)
vconst_2 <= 0.8354865 AND vconst_corr <= 0.9298095|1 (16.0/5.0)
|0 (16.0)


