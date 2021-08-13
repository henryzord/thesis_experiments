# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_corr <= 0.560713 and vconst_2 <= 0.956662 | 1 | 0.875536 |
| vconst_2 <= 0.475691 | 1 | 0.718447 |
| convect_corr <= 0.445535 and slm_corr <= 0.894022 and vconst_5 <= 0.88201 | 1 | 0.539683 |
| efficiency_factor <= 0.944002 and convect_corr <= 0.985364 and bckgrnd_vdc1 > 0.450643 and vconst_3 > 0.186172 and vconst_2 <= 0.891708 | 1 | 0.420000 |
| vconst_7 <= 0.27174 | 0 | 0.500000 |
| convect_corr <= 0.8073 and vertical_decay_scale <= 0.4194 and vconst_corr <= 0.738848 | 1 | 0.363636 |
| ah_corr > 0.706929 | 0 | 0.500000 |
| vconst_3 > 0.221943 and efficiency_factor > 0.287928 | 0 | 0.461538 |
| vconst_corr <= 0.795247 | 1 | 0.800000 |
|  | 1 | 0.750000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_corr >= 0.84282 and vconst_2 >= 0.584058 and convect_corr >= 0.448845 and vconst_5 <= 0.852842 | 0 | 0.036011 |
| vconst_2 >= 0.721159 and vconst_corr >= 0.561778 and bckgrnd_vdc1 <= 0.412961 and convect_corr >= 0.479588 | 0 | 0.019718 |
| vconst_corr >= 0.728289 and bckgrnd_vdc_eq <= 0.257976 and vconst_2 >= 0.482306 and vconst_7 <= 0.612793 | 0 | 0.011364 |
| vconst_4 <= 0.095428 and vconst_2 >= 0.783255 and vconst_corr >= 0.728289 | 0 | 0.005714 |
| vconst_4 <= 0.04975 and convect_corr >= 0.83934 and vconst_corr >= 0.473099 | 0 | 0.005714 |
|  | 1 | 0.997135 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(vconst_corr >= 0.84282) and (vconst_2 >= 0.584058) and (convect_corr >= 0.448845) and (vconst_5 <= 0.852842)|0 (13.0/0.0)
(vconst_2 >= 0.721159) and (vconst_corr >= 0.561778) and (bckgrnd_vdc1 <= 0.412961) and (convect_corr >= 0.479588)|0 (7.0/0.0)
(vconst_corr >= 0.728289) and (bckgrnd_vdc_eq <= 0.257976) and (vconst_2 >= 0.482306) and (vconst_7 <= 0.612793)|0 (4.0/0.0)
(vconst_4 <= 0.095428) and (vconst_2 >= 0.783255) and (vconst_corr >= 0.728289)|0 (2.0/0.0)
(vconst_4 <= 0.04975) and (convect_corr >= 0.83934) and (vconst_corr >= 0.473099)|0 (2.0/0.0)
|1 (349.0/1.0)


## PART

Decision list:

rules | predicted class
---|---
vconst_corr <= 0.560713 AND vconst_2 <= 0.956662|1 (204.0)
vconst_2 <= 0.475691|1 (74.0)
convect_corr <= 0.445535 AND slm_corr <= 0.894022 AND vconst_5 <= 0.88201|1 (34.0)
efficiency_factor <= 0.944002 AND convect_corr <= 0.985364 AND bckgrnd_vdc1 > 0.450643 AND vconst_3 > 0.186172 AND vconst_2 <= 0.891708|1 (21.0)
vconst_7 <= 0.27174|0 (15.0)
convect_corr <= 0.8073 AND vertical_decay_scale <= 0.4194 AND vconst_corr <= 0.738848|1 (8.0)
ah_corr > 0.706929|0 (7.0)
vconst_3 > 0.221943 AND efficiency_factor > 0.287928|0 (6.0)
vconst_corr <= 0.795247|1 (4.0)
|1 (4.0/1.0)


