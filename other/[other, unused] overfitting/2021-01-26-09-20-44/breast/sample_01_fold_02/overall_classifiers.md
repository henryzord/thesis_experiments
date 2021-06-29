# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | no-recurrence-events | 0.703125 |
| Deg-malig = 3 and Node-caps = no and Inv-nodes = 6-8 | recurrence-events | 0.005525 |
| Node-caps = no and Deg-malig = 3 and Irradiated = yes | recurrence-events | 0.025118 |
| Node-caps = yes and Deg-malig = 3 and Irradiated = no | recurrence-events | 0.043137 |
| Node-caps = yes and Deg-malig = 3 and Irradiated = yes | recurrence-events | 0.049247 |
| Deg-malig = 3 and Node-caps = no and Inv-nodes = 3-5 | recurrence-events | 0.022645 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Tumor-size = 20-24 and Menopause = ge40 | no-recurrence-events | 0.096023 |
| Tumor-size = 25-29 | no-recurrence-events | 0.212374 |
| Tumor-size = 15-19 | no-recurrence-events | 0.153409 |
| Tumor-size = 20-24 | no-recurrence-events | 0.115785 |
| Tumor-size = 40-44 | no-recurrence-events | 0.135307 |
| Tumor-size = 10-14 | no-recurrence-events | 0.247891 |
| Tumor-size = 30-34 and Breast-quad = left_up | recurrence-events | 0.068644 |
|  | no-recurrence-events | 0.476563 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Deg-malig = 3 and Node-caps = yes | recurrence-events | 0.088192 |
| Inv-nodes = 3-5 and Breast = left | recurrence-events | 0.022436 |
|  | no-recurrence-events | 0.792952 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

node-caps|deg-malig|irradiated|class
---|---|---|---
no|3|no|no-recurrence-events
yes|3|no|recurrence-events
yes|2|no|no-recurrence-events
no|2|no|no-recurrence-events
?|1|no|recurrence-events
?|3|yes|no-recurrence-events
no|3|yes|recurrence-events
no|1|no|no-recurrence-events
yes|3|yes|recurrence-events
?|2|yes|no-recurrence-events
no|2|yes|no-recurrence-events
yes|2|yes|no-recurrence-events
no|1|yes|no-recurrence-events
?|1|yes|no-recurrence-events

## JRip

Decision list:

rules | predicted class
---|---
(Deg-malig = 3) and (Node-caps = yes)|recurrence-events (28.0/6.0)
(Inv-nodes = 3-5) and (Breast = left)|recurrence-events (11.0/4.0)
|no-recurrence-events (217.0/47.0)


## PART

Decision list:

rules | predicted class
---|---
Tumor-size = 20-24 AND Menopause = ge40|no-recurrence-events (15.0/6.0)
Tumor-size = 25-29|no-recurrence-events (24.0/9.0)
Tumor-size = 15-19|no-recurrence-events (13.0/1.0)
Tumor-size = 20-24|no-recurrence-events (13.0/3.0)
Tumor-size = 40-44|no-recurrence-events (12.0/3.0)
Tumor-size = 10-14|no-recurrence-events (11.0)
Tumor-size = 30-34 AND Breast-quad = left_up|recurrence-events (8.4/3.0)
|no-recurrence-events (31.6/10.6)


## J48 Decision Tree

* Deg-malig = 1: no-recurrence-events (67.0/11.0)
* Deg-malig = 2: no-recurrence-events (112.0/23.0)
* Deg-malig = 3
	* Node-caps = yes: recurrence-events (28.75/6.75)
	* Node-caps = no
		* Inv-nodes = 0-2: no-recurrence-events (39.0/14.0)
		* Inv-nodes = 3-5: recurrence-events (6.0/1.0)
		* Inv-nodes = 6-8: recurrence-events (1.0)
		* Inv-nodes = 9-11: no-recurrence-events (1.25)
		* Inv-nodes = 12-14: no-recurrence-events (0.0)
		* Inv-nodes = 15-17: no-recurrence-events (1.0)
		* Inv-nodes = 18-20: no-recurrence-events (0.0)
		* Inv-nodes = 21-23: no-recurrence-events (0.0)
		* Inv-nodes = 24-26: no-recurrence-events (0.0)
		* Inv-nodes = 27-29: no-recurrence-events (0.0)
		* Inv-nodes = 30-32: no-recurrence-events (0.0)
		* Inv-nodes = 33-35: no-recurrence-events (0.0)
		* Inv-nodes = 36-39: no-recurrence-events (0.0)


## SimpleCart Decision Tree

* Deg-malig=(3)
						* Inv-nodes=(12-14)|(24-26)|(6-8)|(3-5)|(9-11)|(15-17): recurrence-events(26.0/9.0)
						* Inv-nodes!=(12-14)|(24-26)|(6-8)|(3-5)|(9-11)|(15-17): no-recurrence-events(26.0/16.0)
* Deg-malig!=(3): no-recurrence-events(145.0/34.0)


