# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 0 | 0.555466 |
| variance > -0.279085 and variance <= 0.320165 and skewness > -2.3021 and skewness <= 5.21045 and curtosis > -4.42285 and curtosis <= 8.8457 and entropy = all | 1 | 0.040850 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis < -2.2525000000000004 | 1 | 0.027197 |
| variance < 0.320165 and skewness < 7.5653 and variance >= -0.458565 and curtosis < 4.84085 and skewness < 5.45355 | 1 | 0.079217 |
| variance > 0.31803 and curtosis <= -4.3882 and skewness <= 7.1907 | 1 | 0.039216 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis > 6.7156 and skewness <= -4.8069 | 1 | 0.136032 |
| variance >= 0.320165 and curtosis >= -4.38605 and variance < 1.5922 and curtosis >= -2.2525000000000004 and entropy >= 0.081882 and curtosis < 1.85305 | 1 | 0.020317 |
| variance <= 0.31803 and skewness <= 5.8561 and curtosis <= 6.7156 | 1 | 0.327463 |
| variance < 0.320165 and skewness >= 7.5653 and variance < -3.9402 | 1 | 0.025568 |
| variance <= 0.31803 and skewness > 5.8561 and variance <= -3.4605 | 1 | 0.048544 |
| variance > 0.31803 and curtosis > -4.3882 and variance <= 2.031 and curtosis <= -1.6488 and skewness <= 5.2808 | 1 | 0.043236 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance > 0.31803 and curtosis > -4.3882 and variance > 2.031 | 0 | 0.417197 |
| skewness > 5.2684 and variance > -3.3553 | 0 | 0.244842 |
| variance <= 0.31803 and curtosis <= 6.7156 | 1 | 0.762419 |
| variance <= -1.786 | 1 | 0.449811 |
| curtosis > 0.20278 and skewness > -6.4624 and curtosis > 1.8128 | 0 | 0.531073 |
| curtosis <= -1.3927 | 1 | 0.740741 |
| entropy <= 0.11162 and variance > -0.77995 | 0 | 0.477273 |
|  | 1 | 1.000000 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| variance <= 0.31803 and skewness <= 5.8333 and curtosis <= 6.7019 | 1 | 0.326803 |
| variance <= -1.5078 and skewness <= -4.9932 | 1 | 0.133838 |
| variance <= 1.7425 and skewness <= 7.259 and curtosis <= -2.2126 | 1 | 0.064120 |
| variance <= -4.1479 | 1 | 0.048544 |
| variance <= 2.3917 and skewness <= 4.78 and curtosis <= 0.18307 | 1 | 0.024453 |
| skewness <= -7.3191 | 1 | 0.005797 |
| entropy >= 0.74524 and variance <= 0.74428 and variance >= 0.37637 | 1 | 0.004354 |
|  | 0 | 1.000000 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

variance|skewness|curtosis|entropy|class
---|---|---|---|---
(1.74385-2.3943]|(9.61695-inf)|(-4.42285-8.8457]|all|0
(-0.279085-0.320165]|(9.61695-inf)|(-4.42285-8.8457]|all|0
(-2.7952--0.279085]|(9.61695-inf)|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(9.61695-inf)|(-4.42285-8.8457]|all|0
(2.3943-inf)|(9.61695-inf)|(-4.42285-8.8457]|all|0
(-0.279085-0.320165]|(5.21045-9.61695]|(-4.42285-8.8457]|all|0
(-2.7952--0.279085]|(5.21045-9.61695]|(-4.42285-8.8457]|all|0
(2.3943-inf)|(5.21045-9.61695]|(-4.42285-8.8457]|all|0
(1.74385-2.3943]|(5.21045-9.61695]|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(5.21045-9.61695]|(-4.42285-8.8457]|all|0
(-inf--2.7952]|(5.21045-9.61695]|(-4.42285-8.8457]|all|1
(2.3943-inf)|(9.61695-inf)|(-inf--4.42285]|all|0
(2.3943-inf)|(-2.3021-5.21045]|(-4.42285-8.8457]|all|0
(1.74385-2.3943]|(-2.3021-5.21045]|(-4.42285-8.8457]|all|0
(-inf--2.7952]|(-5.62225--4.9818]|(8.8457-inf)|all|1
(-0.279085-0.320165]|(-2.3021-5.21045]|(-4.42285-8.8457]|all|1
(-2.7952--0.279085]|(-2.3021-5.21045]|(-4.42285-8.8457]|all|1
(0.320165-1.74385]|(-2.3021-5.21045]|(-4.42285-8.8457]|all|0
(-inf--2.7952]|(-2.3021-5.21045]|(-4.42285-8.8457]|all|1
(-0.279085-0.320165]|(-4.9818--2.3021]|(-4.42285-8.8457]|all|1
(-2.7952--0.279085]|(-6.94555--5.62225]|(8.8457-inf)|all|1
(2.3943-inf)|(5.21045-9.61695]|(-inf--4.42285]|all|0
(1.74385-2.3943]|(-4.9818--2.3021]|(-4.42285-8.8457]|all|0
(2.3943-inf)|(-4.9818--2.3021]|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(-4.9818--2.3021]|(-4.42285-8.8457]|all|0
(-inf--2.7952]|(-6.94555--5.62225]|(8.8457-inf)|all|1
(-2.7952--0.279085]|(-4.9818--2.3021]|(-4.42285-8.8457]|all|1
(1.74385-2.3943]|(-5.62225--4.9818]|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(-5.62225--4.9818]|(-4.42285-8.8457]|all|0
(2.3943-inf)|(-5.62225--4.9818]|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-2.7952--0.279085]|(-5.62225--4.9818]|(-4.42285-8.8457]|all|1
(-inf--2.7952]|(-inf--6.94555]|(8.8457-inf)|all|1
(-2.7952--0.279085]|(-inf--6.94555]|(8.8457-inf)|all|1
(1.74385-2.3943]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(-0.279085-0.320165]|(-2.3021-5.21045]|(-inf--4.42285]|all|1
(2.3943-inf)|(-6.94555--5.62225]|(-4.42285-8.8457]|all|0
(-0.279085-0.320165]|(-6.94555--5.62225]|(-4.42285-8.8457]|all|0
(-inf--2.7952]|(-6.94555--5.62225]|(-4.42285-8.8457]|all|0
(0.320165-1.74385]|(-6.94555--5.62225]|(-4.42285-8.8457]|all|0
(1.74385-2.3943]|(-6.94555--5.62225]|(-4.42285-8.8457]|all|0
(-2.7952--0.279085]|(-6.94555--5.62225]|(-4.42285-8.8457]|all|1
(-inf--2.7952]|(-inf--6.94555]|(-4.42285-8.8457]|all|1
(-2.7952--0.279085]|(-inf--6.94555]|(-4.42285-8.8457]|all|1

## JRip

Decision list:

rules | predicted class
---|---
(variance <= 0.31803) and (skewness <= 5.8333) and (curtosis <= 6.7019)|1 (337.0/2.0)
(variance <= -1.5078) and (skewness <= -4.9932)|1 (106.0/0.0)
(variance <= 1.7425) and (skewness <= 7.259) and (curtosis <= -2.2126)|1 (47.0/0.0)
(variance <= -4.1479)|1 (35.0/0.0)
(variance <= 2.3917) and (skewness <= 4.78) and (curtosis <= 0.18307)|1 (21.0/2.0)
(skewness <= -7.3191)|1 (4.0/0.0)
(entropy >= 0.74524) and (variance <= 0.74428) and (variance >= 0.37637)|1 (3.0/0.0)
|0 (682.0/0.0)


## PART

Decision list:

rules | predicted class
---|---
variance > 0.31803 AND curtosis > -4.3882 AND variance > 2.031|0 (393.0)
skewness > 5.2684 AND variance > -3.3553|0 (178.0)
variance <= 0.31803 AND curtosis <= 6.7156|1 (373.0/2.0)
variance <= -1.786|1 (96.0/1.0)
curtosis > 0.20278 AND skewness > -6.4624 AND curtosis > 1.8128|0 (91.0)
curtosis <= -1.3927|1 (60.0)
entropy <= 0.11162 AND variance > -0.77995|0 (21.0)
|1 (23.0)


## J48 Decision Tree

* variance <= 0.31803
	* skewness <= 5.8561
		* curtosis <= 6.7156: 1 (338.0/2.0)
		* curtosis > 6.7156
			* skewness <= -4.8069: 1 (110.0/1.0)
			* skewness > -4.8069: 0 (22.0)
	* skewness > 5.8561
		* variance <= -3.4605: 1 (35.0)
		* variance > -3.4605: 0 (85.0)
* variance > 0.31803
	* curtosis <= -4.3882
		* skewness <= 7.1907: 1 (28.0)
		* skewness > 7.1907: 0 (10.0)
	* curtosis > -4.3882
		* variance <= 2.031
			* curtosis <= -1.6488
				* skewness <= 5.2808: 1 (31.0)
				* skewness > 5.2808: 0 (15.0)
			* curtosis > -1.6488
				* variance <= 0.74521
					* entropy <= -0.021566: 0 (42.0/1.0)
					* entropy > -0.021566
						* curtosis <= 1.949: 1 (9.0)
						* curtosis > 1.949: 0 (6.0)
				* variance > 0.74521: 0 (111.0)
		* variance > 2.031: 0 (393.0)


## SimpleCart Decision Tree

* variance < 0.320165
	* skewness < 7.5653
		* variance < -0.458565
			* curtosis < 6.7456: 1(293.0/1.0)
			* curtosis >= 6.7456
				* skewness < -4.7997: 1(109.0/0.0)
				* skewness >= -4.7997: 0(14.0/0.0)
		* variance >= -0.458565
			* curtosis < 4.84085
				* skewness < 5.45355: 1(60.0/1.0)
				* skewness >= 5.45355: 0(9.0/0.0)
			* curtosis >= 4.84085: 0(10.0/0.0)
	* skewness >= 7.5653
		* variance < -3.9402: 1(18.0/0.0)
		* variance >= -3.9402: 0(75.0/0.0)
* variance >= 0.320165
	* curtosis < -4.38605
		* variance < 3.30405: 1(28.0/0.0)
		* variance >= 3.30405: 0(10.0/0.0)
	* curtosis >= -4.38605
		* variance < 1.5922
			* curtosis < -2.2525000000000004: 1(21.0/2.0)
			* curtosis >= -2.2525000000000004
				* entropy < 0.081882: 0(109.0/1.0)
				* entropy >= 0.081882
					* curtosis < 1.85305: 1(16.0/2.0)
					* curtosis >= 1.85305: 0(16.0/0.0)
		* variance >= 1.5922: 0(437.0/3.0)


