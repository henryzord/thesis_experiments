# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 <= 0.587942 | 1 | 0.857215 |
| vconst_2 > 0.587942 and vconst_corr <= 0.515229 | 1 | 0.687064 |
| vconst_2 > 0.587942 and vconst_corr > 0.515229 and convect_corr <= 0.872487 | 1 | 0.484159 |
| vconst_2 > 0.587942 and vconst_corr > 0.515229 and convect_corr > 0.872487 | 0 | 0.029304 |

## Ordered rules

# Text representation of classifiers as-is

## J48 Decision Tree

* vconst_2 <= 0.587942: 1 (180.0/2.0)
* vconst_2 > 0.587942
	* vconst_corr <= 0.515229: 1 (71.0)
	* vconst_corr > 0.515229
		* convect_corr <= 0.872487: 1 (53.0/18.0)
		* convect_corr > 0.872487: 0 (11.0/1.0)


