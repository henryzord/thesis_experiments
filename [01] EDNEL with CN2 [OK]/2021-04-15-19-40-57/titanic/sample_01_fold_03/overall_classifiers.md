# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 | -1.0 | 0.623067 |
| Sex <= -1.92 and Class <= -0.923 | 1.0 | 0.127122 |
| Sex <= -1.92 and Class > -0.923 and Class <= 0.0214 | -1.0 | 0.077220 |
| Sex >= -0.6995 and Age >= 2.076 and Class < -0.45080000000000003 | 1.0 | 0.011070 |
| Sex < -0.6995 and Class >= -0.45080000000000003 and Class >= 0.49319999999999997 | 1.0 | 0.009246 |
| Sex >= -0.6995 and Age >= 2.076 and Class >= -0.45080000000000003 | -1.0 | 0.033310 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class <= 0.0214 and Class > -0.923 | -1.0 | 0.318982 |
| Sex > -1.92 and Age <= -0.228 and Class > -1.87 and Class > -0.923 | -1.0 | 0.428101 |
| Sex > -1.92 and Age <= -0.228 and Class <= -1.87 | -1.0 | 0.103107 |
| Class > -1.87 and Sex > -1.92 and Age <= -0.228 | -1.0 | 0.095216 |
| Class <= -0.923 and Age <= -0.228 and Class <= -1.87 | 1.0 | 0.545453 |
| Class <= -0.923 and Age <= -0.228 | 1.0 | 0.351329 |
| Class > -0.923 and Class <= 0.0214 and Sex <= -1.92 and Age <= -0.228 | -1.0 | 0.109021 |
| Class > -0.923 and Class <= 0.0214 and Sex > -1.92 | -1.0 | 0.025176 |
| Class <= -0.923 | 1.0 | 0.406673 |
| Class <= 0.0214 | -1.0 | 0.021601 |
|  | 1.0 | 0.991501 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class <= 0.0214 AND Class > -0.923|-1.0 (418.0/67.0)
Sex > -1.92 AND Age <= -0.228 AND Class > -1.87 AND Class > -0.923|-1.0 (779.0/179.0)
Sex > -1.92 AND Age <= -0.228 AND Class <= -1.87|-1.0 (160.0/53.0)
Class > -1.87 AND Sex > -1.92 AND Age <= -0.228|-1.0 (154.0/13.0)
Class <= -0.923 AND Age <= -0.228 AND Class <= -1.87|1.0 (124.0/4.0)
Class <= -0.923 AND Age <= -0.228|1.0 (86.0/11.0)
Class > -0.923 AND Class <= 0.0214 AND Sex <= -1.92 AND Age <= -0.228|-1.0 (142.0/64.0)
Class > -0.923 AND Class <= 0.0214 AND Sex > -1.92|-1.0 (41.0/11.0)
Class <= -0.923|1.0 (29.0)
Class <= 0.0214|-1.0 (29.0/14.0)
|1.0 (18.0/3.0)


## J48 Decision Tree

* Sex <= -1.92
	* Class <= -0.923: 1.0 (224.0/15.0)
	* Class > -0.923
		* Class <= 0.0214: -1.0 (171.0/78.0)
		* Class > 0.0214: 1.0 (18.0/3.0)
* Sex > -1.92
	* Age <= -0.228: -1.0 (1511.0/312.0)
	* Age > -0.228
		* Class <= -0.923: 1.0 (15.0)
		* Class > -0.923: -1.0 (41.0/11.0)


## SimpleCart Decision Tree

* Sex < -0.6995
	* Class < -0.45080000000000003
		* Class < -1.3965: 1.0(121.0/4.0)
		* Class >= -1.3965
			* Age < 2.076: 1.0(75.0/11.0)
			* Age >= 2.076: 1.0(13.0/0.0)
	* Class >= -0.45080000000000003
		* Class < 0.49319999999999997
			* Age < 2.076: -1.0(78.0/64.0)
			* Age >= 2.076: -1.0(15.0/14.0)
		* Class >= 0.49319999999999997: 1.0(15.0/3.0)
* Sex >= -0.6995
	* Age < 2.076
		* Class < -1.3965: -1.0(107.0/53.0)
		* Class >= -1.3965
			* Class < 0.49319999999999997
				* Class < -0.45080000000000003: -1.0(141.0/13.0)
				* Class >= -0.45080000000000003: -1.0(351.0/67.0)
			* Class >= 0.49319999999999997: -1.0(600.0/179.0)
	* Age >= 2.076
		* Class < -0.45080000000000003: 1.0(15.0/0.0)
		* Class >= -0.45080000000000003: -1.0(30.0/11.0)


