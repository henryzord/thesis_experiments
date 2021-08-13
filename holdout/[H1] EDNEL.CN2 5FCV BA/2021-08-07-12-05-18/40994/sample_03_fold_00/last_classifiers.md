# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_corr <= 0.6229385000000001 | 1 | 0.868793 |
| vconst_corr > 0.6229385000000001 and vconst_2 <= 0.5779529999999999 | 1 | 0.685307 |
| vconst_corr > 0.6229385000000001 and vconst_2 > 0.5779529999999999 and convect_corr <= 0.5114970000000001 | 1 | 0.421554 |
| vconst_corr > 0.6229385000000001 and vconst_2 > 0.5779529999999999 and convect_corr > 0.5114970000000001 and efficiency_factor > 0.616654 | 0 | 0.036620 |
| vconst_corr > 0.6229385000000001 and vconst_2 > 0.5779529999999999 and convect_corr > 0.5114970000000001 and efficiency_factor <= 0.616654 and bckgrnd_vdc_psim <= 0.6344095000000001 | 0 | 0.021099 |
| vconst_corr > 0.6229385000000001 and vconst_2 > 0.5779529999999999 and convect_corr > 0.5114970000000001 and efficiency_factor <= 0.616654 and bckgrnd_vdc_psim > 0.6344095000000001 | 1 | 0.168750 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_corr <= 0.622939 | 1 | 0.868793 |
| vconst_2 <= 0.577953 | 1 | 0.682728 |
| convect_corr <= 0.511497 and vconst_corr <= 0.837943 | 1 | 0.333333 |
| bckgrnd_vdc1 <= 0.457998 and bckgrnd_vdc_psim <= 0.71565 | 0 | 0.478261 |
| vconst_2 <= 0.861251 and convect_corr <= 0.632057 | 1 | 0.555556 |
| vconst_corr > 0.840706 and vconst_corr <= 0.920574 | 0 | 0.290909 |
| vconst_corr <= 0.879751 | 1 | 0.447552 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
vconst_corr <= 0.622939|1 (229.0/2.0)
vconst_2 <= 0.577953|1 (76.0/1.0)
convect_corr <= 0.511497 AND vconst_corr <= 0.837943|1 (17.0)
bckgrnd_vdc1 <= 0.457998 AND bckgrnd_vdc_psim <= 0.71565|0 (21.0/1.0)
vconst_2 <= 0.861251 AND convect_corr <= 0.632057|1 (15.0)
vconst_corr > 0.840706 AND vconst_corr <= 0.920574|0 (5.0/1.0)
vconst_corr <= 0.879751|1 (8.0/2.0)
|0 (5.0)


## J48 Decision Tree

* vconst_corr <= 0.6229385000000001: 1 (229.0/2.0)
* vconst_corr > 0.6229385000000001
	* vconst_2 <= 0.5779529999999999: 1 (76.0/1.0)
	* vconst_2 > 0.5779529999999999
		* convect_corr <= 0.5114970000000001: 1 (35.0/6.0)
		* convect_corr > 0.5114970000000001
			* efficiency_factor <= 0.616654
				* bckgrnd_vdc_psim <= 0.6344095000000001: 0 (11.0/2.0)
				* bckgrnd_vdc_psim > 0.6344095000000001: 1 (12.0/3.0)
			* efficiency_factor > 0.616654: 0 (13.0)


