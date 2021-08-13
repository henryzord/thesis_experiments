# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 <= 0.545086 | 1 | 0.867864 |
| vconst_corr <= 0.471976 | 1 | 0.743686 |
| bckgrnd_vdc1 > 0.4568175 and slm_corr > 0.202163 | 1 | 0.531684 |
| convect_corr <= 0.516374 and vconst_corr > 0.726325 | 1 | 0.127604 |
| convect_corr > 0.516374 and vertical_decay_scale > 0.6047705 | 0 | 0.400000 |
| convect_corr <= 0.5636365 | 1 | 0.315104 |
| ah_bolus > 0.498671 | 0 | 0.593137 |
|  | 1 | 0.500000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
vconst_2 <= 0.545086|1 (199.0/1.0)
vconst_corr <= 0.471976|1 (88.0)
bckgrnd_vdc1 > 0.4568175 AND slm_corr > 0.202163|1 (35.0)
convect_corr <= 0.516374 AND vconst_corr > 0.726325|1 (12.0/5.0)
convect_corr > 0.516374 AND vertical_decay_scale > 0.6047705|0 (12.0)
convect_corr <= 0.5636365|1 (11.0)
ah_bolus > 0.498671|0 (10.0/1.0)
|1 (9.0/3.0)


