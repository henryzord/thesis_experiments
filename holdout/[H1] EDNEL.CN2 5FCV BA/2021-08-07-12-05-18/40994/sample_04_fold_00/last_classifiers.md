# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 1 | 0.928571 |
| vconst_corr > 0.560713 and vconst_2 > 0.54087 and vconst_5 = all and bckgrnd_vdc1 <= 0.413724 and Prandtl = all | 0 | 0.037889 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 <= 0.54087 | 1 | 0.883117 |
| vconst_corr <= 0.558964 and vconst_2 <= 0.9721595000000001 | 1 | 0.761062 |
| vconst_4 > 0.1367345 and convect_corr <= 0.5114970000000001 and vconst_corr <= 0.888429 | 1 | 0.534483 |
| bckgrnd_vdc1 > 0.43972 and vconst_7 > 0.418209 | 1 | 0.357143 |
| bckgrnd_vdc_eq <= 0.5733415 and vconst_3 <= 0.4457875 | 0 | 0.464286 |
| vconst_corr <= 0.7176515 | 1 | 0.320000 |
| vconst_2 > 0.7144459999999999 | 0 | 0.555556 |
|  | 1 | 0.636364 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

vconst_corr|vconst_2|vconst_5|bckgrnd_vdc1|prandtl|target
---|---|---|---|---|---
(-inf-0.560713]|(0.54087-inf)|all|(0.413724-inf)|all|1
(0.560713-inf)|(0.54087-inf)|all|(0.413724-inf)|all|1
(0.560713-inf)|(-inf-0.54087]|all|(0.413724-inf)|all|1
(-inf-0.560713]|(-inf-0.54087]|all|(0.413724-inf)|all|1
(0.560713-inf)|(0.54087-inf)|all|(-inf-0.413724]|all|0
(-inf-0.560713]|(0.54087-inf)|all|(-inf-0.413724]|all|1
(0.560713-inf)|(-inf-0.54087]|all|(-inf-0.413724]|all|1
(-inf-0.560713]|(-inf-0.54087]|all|(-inf-0.413724]|all|1

## PART

Decision list:

rules | predicted class
---|---
vconst_2 <= 0.54087|1 (204.0)
vconst_corr <= 0.558964 AND vconst_2 <= 0.9721595000000001|1 (86.0)
vconst_4 > 0.1367345 AND convect_corr <= 0.5114970000000001 AND vconst_corr <= 0.888429|1 (31.0)
bckgrnd_vdc1 > 0.43972 AND vconst_7 > 0.418209|1 (15.0)
bckgrnd_vdc_eq <= 0.5733415 AND vconst_3 <= 0.4457875|0 (13.0)
vconst_corr <= 0.7176515|1 (10.0/2.0)
vconst_2 > 0.7144459999999999|0 (10.0/2.0)
|1 (9.0/4.0)


