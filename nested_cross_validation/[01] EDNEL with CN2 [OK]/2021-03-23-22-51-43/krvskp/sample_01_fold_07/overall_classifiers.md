# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| rimmx = f and bxqsq = t | nowin | 0.308437 |
| stlmt = f and rimmx = t | won | 0.426016 |
| wknck = t and wkovl = t | nowin | 0.219836 |
| wkna8 = t and bknwy = f | nowin | 0.087850 |
| wknck = f and hdchk = f and wkna8 = f and bkxbq = t | won | 0.616705 |
| mulch = f and bkon8 = f and wknck = f and wkpos = t and katri = n and rxmsq = f | won | 0.406059 |
| qxmsq = f and katri = w and bkxbq = f | won | 0.204276 |
| qxmsq = f and bkblk = f and bkxcr = t | nowin | 0.500000 |
| qxmsq = f and mulch = f and bkon8 = f and bkblk = f and wkovl = t | nowin | 0.355511 |
| mulch = t | nowin | 0.285714 |
| wkovl = t and katri = n | won | 0.304965 |
| skrxp = t | nowin | 0.336207 |
| reskr = f and bkon8 = f and bkona = t and bkxbq = t | nowin | 0.153846 |
| reskr = f and bkon8 = f and wkna8 = f and reskd = f and thrsk = f and rxmsq = f and wkovl = f and blxwp = f and cntxt = f | won | 0.407895 |
| reskr = f and bkon8 = f and wtoeg = n and cntxt = t and reskd = f and bknwy = f and rkxwp = f and wkpos = t | won | 0.187013 |
| reskr = f and bkon8 = f and wkpos = f and cntxt = t and reskd = f and bknwy = f and rkxwp = f and wkovl = f and wkcti = t | won | 0.147929 |
| katri = n and dwipd = l and wkcti = f | nowin | 0.400000 |
| reskr = f and bkon8 = f and cntxt = t and reskd = f | won | 0.366279 |
|  | nowin | 0.906250 |


# Text representation of classifiers as-is

## PART

Decision list:

rules | predicted class
---|---
rimmx = f AND bxqsq = t|nowin (669.0)
stlmt = f AND rimmx = t|won (524.0)
wknck = t AND wkovl = t|nowin (279.0/2.0)
wkna8 = t AND bknwy = f|nowin (94.0)
wknck = f AND hdchk = f AND wkna8 = f AND bkxbq = t|won (539.0)
mulch = f AND bkon8 = f AND wknck = f AND wkpos = t AND katri = n AND rxmsq = f|won (233.0/2.0)
qxmsq = f AND katri = w AND bkxbq = f|won (86.0)
qxmsq = f AND bkblk = f AND bkxcr = t|nowin (120.0)
qxmsq = f AND mulch = f AND bkon8 = f AND bkblk = f AND wkovl = t|nowin (68.0/1.0)
mulch = t|nowin (48.0)
wkovl = t AND katri = n|won (40.0)
skrxp = t|nowin (39.0)
reskr = f AND bkon8 = f AND bkona = t AND bkxbq = t|nowin (14.0)
reskr = f AND bkon8 = f AND wkna8 = f AND reskd = f AND thrsk = f AND rxmsq = f AND wkovl = f AND blxwp = f AND cntxt = f|won (31.0)
reskr = f AND bkon8 = f AND wtoeg = n AND cntxt = t AND reskd = f AND bknwy = f AND rkxwp = f AND wkpos = t|won (14.0/2.0)
reskr = f AND bkon8 = f AND wkpos = f AND cntxt = t AND reskd = f AND bknwy = f AND rkxwp = f AND wkovl = f AND wkcti = t|won (13.0/3.0)
katri = n AND dwipd = l AND wkcti = f|nowin (16.0)
reskr = f AND bkon8 = f AND cntxt = t AND reskd = f|won (23.0/2.0)
|nowin (25.0/3.0)


