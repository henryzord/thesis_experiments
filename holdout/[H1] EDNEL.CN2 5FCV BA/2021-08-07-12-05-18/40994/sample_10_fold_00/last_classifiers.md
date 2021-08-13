# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| vconst_2 < 0.5941810000000001 | 1 | 0.878561 |
| vconst_2 >= 0.5941810000000001 and vconst_corr < 0.8368465 | 1 | 0.785686 |
| vconst_2 >= 0.5941810000000001 and vconst_corr >= 0.8368465 and bckgrnd_vdc1 < 0.4575495 | 0 | 0.033719 |
| vconst_2 >= 0.5941810000000001 and vconst_corr >= 0.8368465 and bckgrnd_vdc1 >= 0.4575495 | 1 | 0.219298 |

## Ordered rules

# Text representation of classifiers as-is

## SimpleCart Decision Tree

* vconst_2 < 0.5941810000000001: 1(218.0/1.0)
* vconst_2 >= 0.5941810000000001
	* vconst_corr < 0.8368465: 1(117.0/14.0)
	* vconst_corr >= 0.8368465
		* bckgrnd_vdc1 < 0.4575495: 0(13.0/1.0)
		* bckgrnd_vdc1 >= 0.4575495: 1(10.0/2.0)


