# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 <= 0.6102175 and vconst_7 > 0.169706 | 1 | 0.850000 |
| vconst_corr <= 0.5601465 and vconst_4 > 0.1493075 | 1 | 0.713043 |
| vconst_corr <= 0.8379435 and convect_corr <= 0.5751515 and vconst_4 > 0.0745265 | 1 | 0.507463 |
| bckgrnd_vdc1 > 0.45230950000000003 and vconst_7 <= 0.479905 and bckgrnd_vdc_psim > 0.599043 | 1 | 0.251748 |
| vconst_2 > 0.861251 | 0 | 0.264063 |
| bckgrnd_vdc1 > 0.3598475 and vconst_5 > 0.6197395 | 1 | 0.375000 |
| convect_corr <= 0.8646475 and vertical_decay_scale <= 0.45907450000000005 | 1 | 0.342857 |
| vconst_4 <= 0.3012935 | 0 | 0.547009 |
|  | 0 | 0.666667 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 >= 0.610852 and vconst_corr >= 0.845014 | 0 | 0.033920 |
| vconst_2 >= 0.621174 and vconst_corr >= 0.561778 and convect_corr >= 0.582027 | 0 | 0.015942 |
|  | 1 | 0.985714 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(vconst_2 >= 0.610852) and (vconst_corr >= 0.845014)|0 (24.0/7.0)
(vconst_2 >= 0.621174) and (vconst_corr >= 0.561778) and (convect_corr >= 0.582027)|0 (21.0/10.0)
|1 (333.0/5.0)


## PART

Decision list:

rules | predicted class
---|---
vconst_2 <= 0.6102175 AND vconst_7 > 0.169706|1 (187.0)
vconst_corr <= 0.5601465 AND vconst_4 > 0.1493075|1 (82.0)
vconst_corr <= 0.8379435 AND convect_corr <= 0.5751515 AND vconst_4 > 0.0745265|1 (34.0)
bckgrnd_vdc1 > 0.45230950000000003 AND vconst_7 <= 0.479905 AND bckgrnd_vdc_psim > 0.599043|1 (13.0/1.0)
vconst_2 > 0.861251|0 (16.0/3.0)
bckgrnd_vdc1 > 0.3598475 AND vconst_5 > 0.6197395|1 (11.0)
convect_corr <= 0.8646475 AND vertical_decay_scale <= 0.45907450000000005|1 (13.0/2.0)
vconst_4 <= 0.3012935|0 (11.0/5.0)
|0 (11.0)


