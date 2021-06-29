# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Deg-malig!=(3) | no-recurrence-events | 0.703125 |
| Node-caps = no and Deg-malig = 1 and Irradiated = yes | recurrence-events | 0.003745 |
| Inv-nodes = 3-5 and Deg-malig = 3 | recurrence-events | 0.033680 |
| Inv-nodes = 6-8 and Deg-malig = 3 | recurrence-events | 0.038027 |
| Node-caps = no and Deg-malig = 3 and Irradiated = yes | recurrence-events | 0.025118 |
| Node-caps = yes and Deg-malig = 3 and Irradiated = no | recurrence-events | 0.043137 |
| Inv-nodes = 24-26 | recurrence-events | 0.005525 |
| Inv-nodes = 12-14 | recurrence-events | 0.010989 |
| Node-caps = yes and Deg-malig = 3 and Irradiated = yes | recurrence-events | 0.049247 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Deg-malig = 2 | no-recurrence-events | 0.498051 |
| Node-caps = no and Irradiated = no | no-recurrence-events | 0.440831 |
|  | recurrence-events | 0.826087 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| Deg-malig = 3 and Node-caps = yes and Breast = left and Irradiated = yes | recurrence-events | 0.057592 |
| Deg-malig = 3 and Tumor-size = 30-34 and Breast = right | recurrence-events | 0.034409 |
| Deg-malig = 3 and Node-caps = yes and Menopause = premeno and Irradiated = no | recurrence-events | 0.032258 |
| Deg-malig = 3 and Inv-nodes = 3-5 | recurrence-events | 0.015347 |
|  | no-recurrence-events | 0.796460 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

node-caps|deg-malig|irradiated|class
---|---|---|---
no|3|no|no-recurrence-events
yes|3|no|recurrence-events
yes|2|no|no-recurrence-events
no|2|no|no-recurrence-events
?|3|yes|no-recurrence-events
?|1|no|recurrence-events
yes|3|yes|recurrence-events
no|3|yes|recurrence-events
no|1|no|no-recurrence-events
yes|2|yes|no-recurrence-events
?|2|yes|no-recurrence-events
no|2|yes|no-recurrence-events
?|1|yes|no-recurrence-events
no|1|yes|recurrence-events

## JRip

Decision list:

rules | predicted class
---|---
(Deg-malig = 3) and (Node-caps = yes) and (Breast = left) and (Irradiated = yes)|recurrence-events (11.0/0.0)
(Deg-malig = 3) and (Tumor-size = 30-34) and (Breast = right)|recurrence-events (10.0/2.0)
(Deg-malig = 3) and (Node-caps = yes) and (Menopause = premeno) and (Irradiated = no)|recurrence-events (6.0/0.0)
(Deg-malig = 3) and (Inv-nodes = 3-5)|recurrence-events (9.0/4.0)
|no-recurrence-events (220.0/46.0)


## PART

Decision list:

rules | predicted class
---|---
Deg-malig = 2|no-recurrence-events (101.0/21.0)
Node-caps = no AND Irradiated = no|no-recurrence-events (80.8/16.8)
|recurrence-events (42.2/13.0)


## J48 Decision Tree

* Inv-nodes = 0-2: no-recurrence-events (153.0/34.0)
* Inv-nodes = 3-5
	* Deg-malig = 1: no-recurrence-events (2.0)
	* Deg-malig = 2: no-recurrence-events (15.0/5.0)
	* Deg-malig = 3: recurrence-events (12.0/4.0)
* Inv-nodes = 6-8
	* Deg-malig = 1: recurrence-events (0.0)
	* Deg-malig = 2: no-recurrence-events (4.0/1.0)
	* Deg-malig = 3: recurrence-events (7.0)
* Inv-nodes = 9-11: no-recurrence-events (5.0/2.0)
* Inv-nodes = 12-14: recurrence-events (1.0)
* Inv-nodes = 15-17: no-recurrence-events (5.0/2.0)
* Inv-nodes = 18-20: no-recurrence-events (0.0)
* Inv-nodes = 21-23: no-recurrence-events (0.0)
* Inv-nodes = 24-26: recurrence-events (1.0)
* Inv-nodes = 27-29: no-recurrence-events (0.0)
* Inv-nodes = 30-32: no-recurrence-events (0.0)
* Inv-nodes = 33-35: no-recurrence-events (0.0)
* Inv-nodes = 36-39: no-recurrence-events (0.0)


## SimpleCart Decision Tree

* Deg-malig=(3)
						* Inv-nodes=(12-14)|(24-26)|(6-8)|(3-5)|(9-11)|(15-17): recurrence-events(26.0/9.0)
						* Inv-nodes!=(12-14)|(24-26)|(6-8)|(3-5)|(9-11)|(15-17): no-recurrence-events(26.0/16.0)
* Deg-malig!=(3): no-recurrence-events(145.0/34.0)


