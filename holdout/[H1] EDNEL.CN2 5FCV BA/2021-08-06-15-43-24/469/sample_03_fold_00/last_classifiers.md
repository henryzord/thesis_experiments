# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Ethnic!=(1) and DMFT.Begin != 1 and DMFT.End!=(0) and DMFT.Begin!=(0) and Ethnic != 1 and DMFT.End != 4 | 2 | 0.036271 |
| DMFT.Begin = 0 and Gender = 1 | 0 | 0.011946 |
| DMFT.Begin = 2 and Gender = 1 | 5 | 0.009293 |
| DMFT.Begin = 0 and Gender = 0 | 1 | 0.009163 |
| DMFT.Begin = 5 and Gender = 1 | 3 | 0.007623 |
| Ethnic!=(1) and DMFT.Begin = 1 and DMFT.End != 4 | 1 | 0.007151 |
| DMFT.Begin = 6 and Gender = 0 | 3 | 0.005885 |
| Ethnic!=(1) and DMFT.Begin != 1 and DMFT.End!=(0) and DMFT.Begin!=(0) and Ethnic = 1 and Gender!=(1) | 2 | 0.006634 |
| DMFT.Begin = 2 and Gender = 0 | 0 | 0.005271 |
| DMFT.Begin = 8 and Gender = 0 | 3 | 0.005114 |
| DMFT.Begin = 3 and Gender = 1 | 4 | 0.005185 |
| DMFT.Begin = 1 and Gender = 0 | 3 | 0.004812 |
| DMFT.Begin = 4 and Gender = 0 | 4 | 0.003950 |
| DMFT.Begin = 5 and Gender = 0 | 3 | 0.004211 |
| DMFT.Begin = 8 and Gender = 1 | 1 | 0.004258 |
| DMFT.Begin = 3 and Gender = 0 | 5 | 0.002734 |
| DMFT.Begin = 7 and Gender = 1 | 1 | 0.003051 |
| Ethnic!=(1) and DMFT.Begin != 1 and DMFT.End!=(0) and DMFT.Begin!=(0) and Ethnic != 1 and DMFT.End = 1 | 1 | 0.003340 |
| DMFT.Begin = 6 and Gender = 1 | 1 | 0.002854 |
| Ethnic!=(1) and DMFT.Begin != 1 and DMFT.End!=(0) and DMFT.Begin!=(0) and Ethnic != 1 and DMFT.End = 4 | 1 | 0.002854 |
| Ethnic!=(1) and DMFT.Begin = 1 and DMFT.End = 2 and Ethnic != 2 | 2 | 0.001068 |
| Ethnic!=(1) and DMFT.Begin != 1 and DMFT.End!=(0) and DMFT.Begin!=(0) and Ethnic != 1 and DMFT.End != 1 | 2 | 0.029400 |
| Ethnic!=(1) and DMFT.Begin = 1 and DMFT.End = 2 and Ethnic != 1 | 2 | 0.001078 |

## Ordered rules

# Text representation of classifiers as-is

## Decision Table

Non matches covered by IB1

dmft.begin|gender|target
---|---|---
1|1|1
8|1|1
7|1|1
3|1|4
5|1|3
4|1|2
6|1|1
0|1|0
2|1|5
5|0|3
1|0|3
4|0|4
7|0|2
8|0|3
3|0|5
6|0|3
0|0|1
2|0|0

## SimpleCart Decision Tree

* Ethnic=(1)
				* DMFT.End=(0)|(1)|(4)|(2)
						* DMFT.End=(2)|(1)|(3)|(5)|(6)
				* DMFT.Begin=(8)|(5): 1(4.0/11.0)
				* DMFT.Begin!=(8)|(5)
						* DMFT.Begin=(0)|(1)|(6): 0(11.0/20.0)
						* DMFT.Begin!=(0)|(1)|(6)
					* DMFT.Begin=(4): 4(5.0/4.0)
					* DMFT.Begin!=(4): 0(7.0/22.0)
						* DMFT.End!=(2)|(1)|(3)|(5)|(6)
							* DMFT.Begin=(5)|(1)|(0)|(6)|(8)
				* DMFT.Begin=(5): 3(4.0/5.0)
				* DMFT.Begin!=(5): 3(15.0/37.0)
							* DMFT.Begin!=(5)|(1)|(0)|(6)|(8): 3(6.0/17.0)
				* DMFT.End!=(0)|(1)|(4)|(2)
							* DMFT.Begin=(8)|(5)|(1)|(4)|(6)|(2): 4(11.0/18.0)
							* DMFT.Begin!=(8)|(5)|(1)|(4)|(6)|(2): 1(5.0/5.0)
* Ethnic!=(1)
			* DMFT.Begin=(8)|(5)|(1)
					* DMFT.End=(0)|(1)|(4)|(2)
				* Ethnic=(2)|(1)
					* DMFT.Begin=(8)|(5)
						* DMFT.End=(4)|(2): 3(6.0/6.0)
						* DMFT.End!=(4)|(2): 0(5.0/8.0)
					* DMFT.Begin!=(8)|(5): 3(9.0/17.0)
				* Ethnic!=(2)|(1): 2(5.0/8.0)
					* DMFT.End!=(0)|(1)|(4)|(2): 1(10.0/26.0)
			* DMFT.Begin!=(8)|(5)|(1)
		* DMFT.End=(0)
							* DMFT.Begin=(0)|(6)|(1)|(5)|(8)
				* Gender=(1): 3(10.0/14.0)
				* Gender!=(1): 2(7.0/24.0)
							* DMFT.Begin!=(0)|(6)|(1)|(5)|(8): 0(8.0/19.0)
		* DMFT.End!=(0)
			* DMFT.Begin=(0): 1(6.0/11.0)
			* DMFT.Begin!=(0)
					* Ethnic=(2)|(1)
					* Gender=(1)
							* DMFT.End=(5)|(3): 4(8.0/19.0)
							* DMFT.End!=(5)|(3)
								* DMFT.Begin=(2)|(6): 5(10.0/6.0)
								* DMFT.Begin!=(2)|(6): 5(7.0/16.0)
					* Gender!=(1): 2(16.0/40.0)
					* Ethnic!=(2)|(1)
						* DMFT.End=(1)|(4): 1(3.0/7.0)
						* DMFT.End!=(1)|(4): 2(8.0/6.0)


