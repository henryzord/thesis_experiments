# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
|  | 3 | 0.155479 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty != 5 | 10 | 0.047649 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 | 6 | 0.037553 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 != 1 | 11 | 0.014113 |
| instr != 1 and instr != 2 and nb.repeat != 1 and difficulty != 5 and Q28 != 1 and Q2 != 1 | 9 | 0.008422 |
| instr = 3 and nb.repeat = 1 and difficulty = 2 | 13 | 0.005158 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty != 3 and Q11 != 3 and Q18 != 3 and attendance != 4 | 5 | 0.004038 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 = 2 and Q26 != 4 | 5 | 0.003296 |
| instr != 1 and instr != 2 and nb.repeat != 1 and difficulty = 5 | 13 | 0.003412 |
| instr = 1 and nb.repeat = 1 and difficulty = 4 | 7 | 0.004461 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and nb.repeat = 1 and Q17 != 3 | 11 | 0.004069 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 = 1 and Q17 != 2 | 8 | 0.003110 |
| instr != 1 and instr != 2 and nb.repeat != 1 and difficulty != 5 and Q28 = 1 | 13 | 0.003031 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 != 2 and Q4 != 2 and Q16 != 2 and Q2 != 4 and Q11 != 4 | 2 | 0.002649 |
| instr!=(3) and instr != 3 and difficulty = 5 | 7 | 0.002391 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 = 5 | 5 | 0.002068 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance != 2 and Q10 != 4 and Q6 != 4 | 13 | 0.002058 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q13 != 2 and Q6 != 2 and Q1 != 1 | 13 | 0.002292 |
| instr = 1 and nb.repeat = 3 and difficulty = 4 | 7 | 0.002575 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance != 2 and Q10 = 4 and Q7 != 3 and attendance != 1 | 5 | 0.001478 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q13 != 2 and Q6 != 2 and Q1 = 1 and attendance = 4 | 13 | 0.001414 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 = 2 | 5 | 0.001819 |
| instr = 3 and nb.repeat = 3 and difficulty = 3 | 8 | 0.001102 |
| instr = 3 and nb.repeat = 2 and difficulty = 2 | 13 | 0.001722 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 = 1 and Q9 != 4 and attendance = 1 | 5 | 0.001722 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 = 1 and Q18 != 4 and Q24 != 4 and Q23 != 4 and difficulty != 5 | 13 | 0.001825 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 = 1 and Q18 = 4 | 13 | 0.001594 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 = 2 and Q2 != 2 | 8 | 0.001310 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 = 1 and Q13 != 2 and Q2 != 2 | 8 | 0.001465 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q1 != 1 and attendance = 4 and Q14 != 5 | 10 | 0.001325 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 = 1 and Q9 != 4 and attendance != 1 and Q27 != 3 and Q1 != 2 and Q17 != 4 | 5 | 0.001378 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 = 2 and Q13 = 4 | 5 | 0.001378 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 = 2 and Q2 = 2 | 9 | 0.001043 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 = 2 and Q18 = 3 | 8 | 0.001162 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q13 != 2 and Q6 = 2 | 13 | 0.001692 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 = 1 | 6 | 0.001426 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty != 3 and Q11 = 3 and Q1 != 3 | 5 | 0.000919 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 = 1 and Q9 != 4 and attendance != 1 and Q27 = 3 | 5 | 0.000985 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance != 2 and Q10 = 4 and Q7 = 3 | 8 | 0.000932 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q1 != 1 and attendance != 4 and Q12 != 3 and attendance != 3 | 2 | 0.000895 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and nb.repeat = 1 and Q17 = 3 | 6 | 0.001113 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance != 2 and Q10 != 4 and Q6 = 4 | 8 | 0.000837 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty = 2 and attendance = 4 | 8 | 0.000638 |
| instr != 1 and instr != 2 and nb.repeat != 1 and difficulty != 5 and Q28 != 1 and Q2 = 1 and Q20 != 3 | 13 | 0.000863 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance != 2 and Q10 = 4 and Q7 != 3 and attendance = 1 | 8 | 0.000732 |
| instr!=(3) and instr != 3 and difficulty != 5 | 10 | 0.020259 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 = 2 | 2 | 0.000490 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 = 5 | 13 | 0.000893 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 = 2 | 8 | 0.000892 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 = 1 and Q18 != 4 and Q24 != 4 and Q23 = 4 | 8 | 0.000654 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 = 1 and Q18 != 4 and Q24 = 4 | 8 | 0.000654 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 = 2 | 9 | 0.000781 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty != 3 and Q11 != 3 and Q18 = 3 | 8 | 0.000836 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 != 5 and Q2 != 5 and attendance != 3 and Q5 = 2 and Q11 = 2 | 13 | 0.000621 |
| instr = 3 and nb.repeat = 2 and difficulty = 1 | 13 | 0.001126 |
| instr = 1 and nb.repeat = 2 and difficulty = 4 | 7 | 0.000617 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q13 = 2 | 13 | 0.000731 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 != 5 and Q2 != 5 and attendance != 3 and Q5 = 2 and Q11 != 2 | 9 | 0.000545 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 and nb.repeat != 1 | 6 | 0.000761 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 = 2 | 5 | 0.000529 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q1 != 1 and attendance != 4 and Q12 != 3 and attendance = 3 | 10 | 0.000647 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 = 2 | 8 | 0.000471 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 != 5 and Q2 != 5 and attendance = 3 and Q7 = 3 | 13 | 0.000619 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 != 5 and Q2 = 5 | 13 | 0.000447 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 = 1 | 9 | 0.000509 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 != 2 and Q8 != 2 and Q12 != 2 and difficulty = 3 and Q1 != 2 and attendance = 2 and Q1 = 5 | 13 | 0.000508 |
| instr = 2 and nb.repeat = 3 and difficulty = 3 | 11 | 0.000417 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 = 1 and Q13 = 2 | 13 | 0.000397 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 = 1 and Q17 = 2 | 5 | 0.000431 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 = 2 and Q26 = 4 | 8 | 0.000372 |
| instr = 3 and nb.repeat = 3 and difficulty = 1 | 9 | 0.001125 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 = 1 and Q13 != 2 and Q2 = 2 | 4 | 0.000449 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 = 1 | 9 | 0.000377 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 != 2 and Q27 != 2 and Q11 != 2 and Q10 = 2 | 9 | 0.000377 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty = 1 and Q3 != 2 and Q9 != 5 and Q24 != 5 and Q2 != 5 and attendance = 3 and Q7 != 3 | 5 | 0.000243 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 != 1 and Q4 != 1 and difficulty != 2 and difficulty != 5 and Q24 != 1 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q23 != 2 and Q16 != 1 and Q3 != 2 and Q5 = 2 and Q18 != 3 | 9 | 0.000191 |
| instr = 2 and nb.repeat = 1 and difficulty = 5 | 11 | 0.003927 |
| instr != 1 and instr != 2 and nb.repeat != 1 and difficulty != 5 and Q28 != 1 and Q2 = 1 and Q20 = 3 | 4 | 0.000198 |
| instr = 1 and nb.repeat = 3 and difficulty = 1 | 2 | 0.000065 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and Q6 != 1 and Q5 != 1 and Q11 = 1 and Q9 = 4 | 13 | 0.000397 |
| instr = 3 and nb.repeat = 3 and difficulty = 2 | 9 | 0.000874 |
| instr!=(3) and instr != 3 and difficulty != 4 | 10 | 0.019807 |
| instr = 1 and nb.repeat = 3 and difficulty = 3 | 2 | 0.000049 |
| instr = 1 and nb.repeat = 3 | 7 | 0.002805 |
| instr = 3 and nb.repeat = 2 and difficulty = 4 | 9 | 0.001952 |
| instr = 3 and nb.repeat = 2 and difficulty = 3 | 9 | 0.002016 |
| instr = 2 and nb.repeat = 1 and difficulty = 4 | 11 | 0.012067 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty != 5 and Q13 != 5 | 10 | 0.036532 |
| instr = 1 and Q10 = 5 and nb.repeat != 3 and nb.repeat = 1 and Q6 = 4 and difficulty != 4 | 10 | 0.001268 |
| instr = 1 and Q1 = 5 and nb.repeat != 3 and nb.repeat = 1 and Q9 != 2 and Q13 = 5 and Q18 != 4 and difficulty != 1 and Q12 != 4 and difficulty != 4 and attendance != 0 | 10 | 0.006051 |
| instr = 1 and difficulty != 1 and nb.repeat = 3 | 7 | 0.003290 |
| instr = 1 and difficulty = 1 | 10 | 0.002249 |
| instr = 1 and difficulty = 3 and Q18 != 4 and Q8 != 4 | 2 | 0.003721 |
| instr = 1 and difficulty != 3 and Q10 = 5 and Q6 != 4 | 2 | 0.003386 |
| instr = 1 and difficulty = 3 | 10 | 0.001004 |
| instr = 1 and Q8 != 5 and Q1 != 5 and Q11 = 5 | 7 | 0.001424 |
| instr = 1 and Q8 = 5 | 7 | 0.003791 |
| instr = 1 and Q1 != 5 and nb.repeat != 1 | 7 | 0.001718 |
| instr = 1 and Q1 != 5 and Q18 = 2 and attendance != 0 and attendance != 4 | 2 | 0.000695 |
| instr = 1 and Q1 = 5 | 10 | 0.002396 |
| instr = 1 and Q25 = 2 and Q4 = 2 and Q9 = 2 | 10 | 0.000761 |
| instr = 1 and Q4 != 2 and Q3 != 2 and Q25 != 2 and Q16 != 2 and Q7 != 2 and Q12 != 2 and Q1 = 4 | 10 | 0.002500 |
| instr != 1 and instr = 2 and difficulty = 4 | 11 | 0.015190 |
| instr = 1 | 7 | 0.011147 |
| instr = 2 and difficulty = 5 and nb.repeat != 3 and Q1 != 2 and Q12 != 2 and Q3 != 2 and Q16 != 2 and nb.repeat = 1 and Q2 != 1 and attendance != 2 and Q8 != 4 | 6 | 0.001438 |
| instr = 2 and difficulty = 5 and nb.repeat != 3 and nb.repeat = 1 and Q11 != 4 | 11 | 0.004887 |
| instr = 2 and difficulty != 1 and difficulty = 2 and Q3 != 1 and Q7 != 1 and Q15 != 1 and Q6 != 1 and Q1 != 1 and Q24 != 2 and Q13 != 2 and Q26 != 2 and Q12 != 2 and Q1 != 2 and Q6 != 2 and Q27 != 2 and attendance = 2 | 6 | 0.002588 |
| instr = 2 and difficulty != 1 and difficulty != 2 and attendance = 0 and Q13 != 5 and Q22 != 5 | 6 | 0.003398 |
| instr = 2 and difficulty = 3 and attendance = 0 and Q13 != 4 | 6 | 0.001218 |
| instr = 2 and attendance = 1 and difficulty != 5 and nb.repeat != 3 and Q2 != 5 and Q14 != 5 and Q27 != 5 and Q20 != 5 and Q9 = 3 | 6 | 0.005268 |
| instr = 2 and difficulty = 3 and attendance != 0 and Q14 = 1 and Q1 = 1 and Q3 = 1 and attendance != 3 | 1 | 0.000365 |
| instr = 2 and difficulty = 3 and Q14 != 1 and attendance != 0 and Q26 != 1 and Q23 != 1 and Q7 != 1 and Q15 = 2 | 6 | 0.002053 |
| instr = 2 and attendance = 1 and difficulty != 5 and Q9 = 3 | 6 | 0.000387 |
| instr = 2 and difficulty = 2 and Q2 != 1 and Q3 != 1 and Q7 != 1 and Q4 != 1 and Q1 != 1 and Q27 = 3 | 6 | 0.002095 |
| instr = 2 and difficulty = 3 and Q16 = 1 | 11 | 0.002080 |
| instr = 2 and difficulty = 3 and Q11 != 1 and attendance != 0 and Q11 != 2 and Q10 != 1 and Q23 != 2 and Q16 != 2 and Q10 != 2 and Q12 = 2 | 11 | 0.001006 |
| instr = 2 and difficulty = 3 and Q11 != 1 and Q13 != 2 and Q28 != 2 and Q16 = 2 | 11 | 0.001097 |
| instr = 2 and difficulty = 3 and Q11 != 1 and Q13 != 2 and Q28 != 2 and Q12 != 2 and Q9 = 2 | 11 | 0.000359 |
| instr = 2 and attendance = 1 | 6 | 0.005920 |
| instr = 2 and difficulty = 3 and Q9 != 1 and Q10 = 2 | 1 | 0.000767 |
| instr = 2 and difficulty = 3 and Q9 != 1 and Q24 = 2 | 1 | 0.000350 |
| instr = 2 and difficulty = 3 and Q9 = 1 | 6 | 0.000452 |
| instr = 2 and difficulty = 3 and Q27 = 1 | 1 | 0.000447 |
| instr = 2 and difficulty = 3 and Q27 = 2 and Q8 = 3 | 11 | 0.000377 |
| instr = 2 and difficulty = 3 and Q27 != 2 and Q6 != 2 and Q12 != 1 and Q16 = 4 | 6 | 0.003597 |
| instr = 2 and nb.repeat = 2 and Q24 != 2 and Q2 != 3 | 6 | 0.000628 |
| instr = 2 and nb.repeat = 2 | 11 | 0.003067 |
| instr = 2 and difficulty = 2 and Q26 != 2 and Q13 != 2 and Q4 != 2 and Q27 != 2 and Q13 != 3 and Q7 != 3 and Q10 != 3 and Q7 != 1 and attendance = 3 and Q13 != 4 | 1 | 0.001154 |
| instr = 2 and difficulty = 2 | 6 | 0.002841 |
| instr = 2 and Q10 = 2 | 1 | 0.001256 |
| instr = 2 and Q18 != 2 and Q17 != 2 and Q19 = 2 | 11 | 0.001152 |
| instr = 2 and Q18 != 2 and Q17 != 2 and Q23 != 2 and Q13 != 2 and Q2 = 2 and Q9 != 4 | 6 | 0.000828 |
| instr = 2 and Q18 != 2 and Q2 != 2 and Q23 != 2 and Q27 != 2 and Q13 != 2 and Q3 != 2 and Q7 != 2 and Q4 != 2 and Q5 != 2 and difficulty != 5 and Q4 = 4 and Q13 != 5 and Q26 != 5 and Q5 != 3 and Q23 = 4 and attendance != 4 and attendance != 2 and attendance = 0 | 6 | 0.000935 |
| instr = 2 and Q18 != 2 and Q2 != 2 and Q23 != 2 and Q27 != 2 and Q13 != 2 and Q12 != 2 and Q4 != 2 and Q1 != 2 and Q3 != 2 and Q8 != 2 and Q7 != 2 and difficulty != 5 and Q4 = 4 and Q25 != 4 | 6 | 0.002198 |
| instr = 2 and Q18 != 2 and Q17 != 2 and Q2 != 2 and Q23 != 2 and Q27 != 2 and Q13 != 2 and Q12 != 2 and Q4 != 2 and Q1 != 2 and Q3 != 2 and Q8 != 2 and Q7 != 2 and difficulty != 5 and Q4 = 4 and Q20 = 4 and attendance != 2 | 11 | 0.005052 |
| instr = 2 and Q18 != 2 and Q17 != 2 and Q2 != 2 and Q23 != 2 and Q27 != 2 and Q20 = 4 and Q7 != 2 | 6 | 0.001577 |
| instr = 2 and Q23 != 4 and Q19 != 4 and Q28 != 4 and Q27 != 4 and Q13 != 4 and Q22 != 2 and Q8 != 2 and Q12 != 4 and Q3 != 4 and Q4 != 2 and Q11 != 4 and Q9 != 4 and Q1 != 4 and nb.repeat = 1 and attendance != 3 and attendance = 4 | 1 | 0.001673 |
| instr = 2 and Q23 != 4 and Q19 != 4 and Q28 != 4 and Q27 != 4 and Q13 != 4 and Q22 != 2 and Q8 != 2 and Q3 != 4 and Q4 != 2 and Q1 != 4 and Q10 != 4 and Q11 != 4 and attendance != 4 and difficulty != 1 and Q6 = 5 | 6 | 0.001904 |
| instr = 2 and Q23 != 4 and Q19 != 4 and Q28 != 4 and Q27 != 4 and Q13 != 4 and Q22 != 2 and Q8 != 2 and Q12 != 4 and Q3 != 4 and Q4 != 2 and Q11 != 4 and Q9 != 4 and Q1 != 4 and nb.repeat = 1 and attendance != 3 and difficulty = 1 | 1 | 0.003369 |
| instr = 2 and Q23 != 4 and Q21 != 4 and Q19 != 4 and Q27 != 4 and Q13 != 4 and Q22 != 1 and Q26 != 2 and attendance != 0 and nb.repeat = 1 and Q6 != 4 | 6 | 0.004078 |
| instr = 2 and Q22 != 2 and Q2 != 2 and Q25 != 4 and Q12 != 4 | 1 | 0.004054 |
| instr = 2 and Q25 = 4 | 11 | 0.003639 |
| instr = 2 | 6 | 0.004867 |
| difficulty = 2 and attendance = 4 and Q22 = 4 | 8 | 0.001266 |
| difficulty = 2 and Q11 = 2 and Q19 != 4 and Q22 != 2 | 13 | 0.003432 |
| nb.repeat != 1 and difficulty = 5 and Q9 != 2 and Q1 != 2 and Q19 != 4 and Q25 = 1 and nb.repeat != 2 | 13 | 0.001081 |
| nb.repeat != 1 and difficulty = 5 and Q25 != 1 and Q20 != 1 and Q11 != 1 and Q5 != 1 | 13 | 0.003785 |
| nb.repeat != 1 and Q28 = 1 and attendance != 2 and attendance != 3 and nb.repeat = 2 | 13 | 0.003224 |
| nb.repeat != 1 and Q1 = 1 and attendance = 3 | 8 | 0.000820 |
| nb.repeat != 1 and Q1 = 1 and Q16 != 4 and Q14 != 4 and Q4 != 3 and Q6 != 3 and Q16 != 5 and Q11 != 2 and Q8 != 2 and attendance != 2 and difficulty != 4 and difficulty != 5 and difficulty != 2 and Q15 != 3 and Q9 = 1 and difficulty = 1 | 9 | 0.000349 |
| nb.repeat != 1 and Q13 = 1 | 13 | 0.001117 |
| nb.repeat != 1 and Q14 != 1 and Q22 != 1 and Q9 != 1 and Q26 != 1 and Q12 != 1 and Q1 = 1 and Q5 != 3 | 9 | 0.001657 |
| nb.repeat != 1 and Q14 != 1 and Q9 = 1 | 13 | 0.001395 |
| nb.repeat != 1 and Q14 != 1 and Q22 != 1 and Q2 != 1 and Q1 != 1 and Q7 != 1 and Q2 != 4 and Q1 != 4 and Q7 != 4 and Q5 != 4 and Q10 != 4 and Q12 != 1 and Q27 != 1 and Q13 = 4 | 3 | 0.000766 |
| nb.repeat != 1 and Q14 != 1 and Q22 != 1 and Q2 != 1 and Q1 != 1 and Q7 != 1 and Q21 = 3 and Q24 != 2 and Q26 != 2 and Q16 != 2 and Q9 = 3 and Q3 = 3 and attendance != 3 and difficulty = 1 | 3 | 0.000698 |
| nb.repeat != 1 and Q14 != 1 and Q22 != 1 and Q2 != 1 and Q1 != 1 and Q7 != 1 and difficulty = 1 and Q16 != 4 and Q1 != 5 | 9 | 0.001905 |
| difficulty = 2 and Q11 = 2 | 13 | 0.001257 |
| difficulty = 2 and Q27 != 2 and Q25 != 2 and Q28 != 2 and Q12 = 2 | 8 | 0.000511 |
| difficulty = 2 and Q27 = 2 | 8 | 0.000600 |
| difficulty = 2 and Q25 != 2 and Q10 != 2 and Q16 != 2 and Q28 = 1 | 13 | 0.001432 |
| difficulty = 2 and Q23 != 2 and Q28 != 2 and Q10 != 1 and Q10 != 2 and Q1 = 1 | 13 | 0.000680 |
| nb.repeat = 2 and Q18 != 1 and Q7 != 1 and Q27 != 1 and Q10 = 2 | 9 | 0.000616 |
| nb.repeat = 2 and Q9 != 2 and Q3 != 1 and Q6 != 2 and Q11 != 1 and Q15 != 2 and attendance != 3 and Q1 != 2 and Q14 != 2 and difficulty != 1 and Q16 != 2 and difficulty = 4 and attendance != 2 and attendance != 0 | 3 | 0.000713 |
| nb.repeat = 2 and Q9 != 2 and Q3 != 1 and Q6 != 2 and attendance = 3 and Q4 != 5 and difficulty != 3 | 9 | 0.001400 |
| nb.repeat = 2 and Q9 != 2 and Q3 != 1 and Q6 != 2 and Q1 != 2 and Q15 != 2 and Q21 = 5 and Q25 != 4 and difficulty = 3 | 8 | 0.001321 |
| Q17 = 1 and nb.repeat = 1 and Q10 = 5 | 9 | 0.000448 |
| Q17 = 1 and nb.repeat = 1 and Q9 = 5 and Q3 = 1 | 3 | 0.000303 |
| Q17 = 1 and Q9 != 5 and nb.repeat = 1 and Q13 != 3 and Q8 != 4 and Q11 != 2 and Q12 != 3 and Q9 != 3 and Q7 != 3 and Q1 != 5 and Q9 = 1 and Q12 = 1 and Q3 = 1 and Q5 = 1 and Q6 = 1 | 3 | 0.011569 |
| Q17 = 1 and Q9 != 5 and Q8 != 4 and attendance != 2 and nb.repeat = 1 and difficulty != 4 and attendance != 3 and Q9 != 1 | 13 | 0.002666 |
| difficulty = 2 and Q23 != 2 and Q8 = 2 | 5 | 0.000550 |
| difficulty = 2 and Q16 != 2 and Q23 != 2 and attendance = 4 and Q1 = 3 | 13 | 0.000661 |
| difficulty = 2 | 13 | 0.005838 |
| Q15 = 1 and Q8 != 4 and Q28 != 5 and Q3 != 4 and attendance != 2 and Q21 != 2 and difficulty != 4 | 13 | 0.015838 |
| nb.repeat = 2 and Q9 != 2 and Q6 != 2 and Q3 != 1 and Q8 != 2 and Q4 != 2 and Q1 != 2 and Q27 != 1 and Q15 != 2 and Q11 != 5 and Q17 != 5 and attendance = 1 and Q17 = 3 | 13 | 0.001432 |
| Q5 = 1 and Q21 = 4 | 8 | 0.004572 |
| Q6 = 1 and Q4 != 5 and Q12 = 3 and Q8 != 2 | 9 | 0.001355 |
| Q6 = 1 and Q4 != 5 and Q12 = 3 | 13 | 0.002661 |
| nb.repeat = 2 and Q9 != 2 and Q6 != 2 and Q3 != 1 and Q8 != 2 and Q1 != 2 and Q27 != 1 and Q6 != 5 and Q17 != 5 and attendance != 1 and Q8 != 3 | 13 | 0.001720 |
| Q6 != 1 and Q5 = 1 and Q28 != 2 | 8 | 0.001625 |
| Q6 != 1 and Q11 = 1 and nb.repeat != 3 and Q12 != 4 and Q22 != 1 and Q19 != 1 and Q26 = 1 | 3 | 0.000630 |
| Q11 = 1 and Q12 = 4 | 4 | 0.000275 |
| Q11 = 1 and difficulty = 1 and Q4 != 2 and Q13 != 2 and Q24 != 5 and Q17 != 5 | 13 | 0.000126 |
| Q11 = 1 and nb.repeat != 3 and Q5 != 1 and Q20 != 1 and Q28 != 2 and Q7 != 4 and Q13 != 1 and Q4 != 4 and Q3 != 4 | 5 | 0.003729 |
| Q4 != 1 and Q11 = 1 | 5 | 0.002282 |
| nb.repeat = 2 and Q9 != 2 and Q6 != 2 and Q7 != 1 and Q10 != 5 and Q26 != 5 and Q25 != 4 and attendance != 2 and Q13 != 2 and Q14 = 3 and Q18 = 3 and attendance != 3 | 9 | 0.003160 |
| Q4 != 1 and difficulty = 5 and Q9 = 2 | 3 | 0.001791 |
| difficulty = 5 and Q25 != 1 and Q21 != 2 and Q15 != 2 and Q24 != 2 and Q4 != 1 and Q9 = 3 | 3 | 0.008094 |
| Q4 != 1 and Q27 = 1 and Q9 != 4 and Q2 != 4 and Q7 != 3 and Q28 != 2 | 5 | 0.000828 |
| Q27 = 1 and Q18 != 2 and Q28 != 3 and Q4 != 4 and Q20 != 3 and Q17 != 3 and Q9 != 4 | 3 | 0.002231 |
| Q27 = 1 and Q4 != 2 and Q9 != 1 and Q21 != 2 | 13 | 0.000704 |
| Q27 != 1 and Q24 = 1 | 4 | 0.000515 |
| Q27 = 1 | 4 | 0.001102 |
| Q21 != 1 and attendance = 4 and Q4 != 1 and Q14 = 2 and difficulty != 1 | 5 | 0.001584 |
| Q21 != 1 and attendance = 4 and Q6 != 1 and Q4 != 1 and Q15 != 2 and Q1 != 1 and Q27 != 2 and Q23 != 2 and Q9 != 2 and Q12 != 2 and Q11 != 2 and nb.repeat = 1 and difficulty != 5 and Q20 != 5 and Q28 != 5 and Q21 != 5 and Q12 != 5 and Q1 != 2 | 3 | 0.003135 |
| Q21 != 1 and attendance = 4 and Q3 = 2 | 3 | 0.001148 |
| Q21 != 1 and attendance = 4 and difficulty = 5 and Q4 = 4 | 3 | 0.000593 |
| Q21 != 1 and attendance = 4 and Q11 = 3 and Q5 != 3 | 8 | 0.001754 |
| Q21 = 1 | 5 | 0.006626 |
| attendance = 4 and Q11 = 3 and Q1 = 2 | 8 | 0.000962 |
| attendance = 4 and Q11 != 3 and Q24 != 3 and Q14 != 3 and Q18 != 3 and Q12 != 2 and Q2 != 3 and Q7 != 3 and Q3 != 3 and difficulty != 5 and difficulty != 4 | 13 | 0.001316 |
| attendance = 4 and Q11 != 3 and difficulty = 5 and Q12 = 5 | 5 | 0.000925 |
| attendance = 4 and Q11 != 3 and Q2 != 5 | 8 | 0.009146 |
| attendance != 4 and Q4 = 1 and Q11 != 5 and Q24 != 3 and Q1 != 2 and Q2 != 2 and Q19 != 5 | 3 | 0.000703 |
| Q4 = 1 and Q19 != 2 and Q24 != 4 and Q27 != 2 | 8 | 0.003279 |
| Q4 = 1 | 13 | 0.004246 |
| attendance != 4 and nb.repeat = 2 and Q9 != 2 and Q6 != 2 and Q7 != 5 and Q13 != 2 and Q15 != 4 and Q27 = 4 | 3 | 0.000662 |
| attendance != 4 and nb.repeat = 2 and Q9 != 2 and Q14 != 4 and Q13 != 3 | 9 | 0.002430 |
| attendance != 4 and Q21 = 5 and Q24 != 2 and Q28 != 3 and Q18 != 3 and Q3 != 2 and Q6 != 2 and Q27 != 2 and Q9 != 2 and Q8 != 2 and Q19 != 3 and Q26 != 3 and Q16 != 3 and Q14 != 3 and Q5 != 3 and Q20 = 5 and Q10 != 3 and Q1 != 2 and Q8 != 3 and Q2 != 1 and attendance != 1 and Q12 != 4 and Q16 != 4 and Q23 != 4 and Q19 != 4 and Q7 != 4 and nb.repeat = 1 and difficulty != 5 and difficulty != 3 | 5 | 0.003810 |
| attendance != 4 and nb.repeat = 2 and Q9 != 2 and Q6 != 2 and Q8 = 3 and attendance = 2 | 8 | 0.000446 |
| attendance != 4 and Q21 = 5 and Q24 != 2 and Q28 != 3 and Q18 != 3 and Q27 != 2 and Q9 != 3 and Q13 != 3 and Q9 != 2 and Q8 != 2 and Q26 != 3 and Q19 != 3 and Q24 != 3 and Q16 != 3 and Q4 != 3 and Q4 != 2 and Q3 != 3 and Q20 != 4 and nb.repeat = 1 and Q27 != 3 and difficulty != 1 and Q25 != 4 and Q12 != 4 and Q16 != 4 and attendance != 1 | 3 | 0.003529 |
| Q6 != 1 and Q26 != 1 and attendance != 4 and Q21 = 5 and Q28 != 3 and Q24 != 2 and Q18 != 3 and Q6 != 2 and Q27 != 2 and Q26 != 3 and Q9 != 2 and Q9 != 3 and difficulty = 1 | 13 | 0.006427 |
| Q6 != 1 and Q26 != 1 and Q3 != 1 and attendance != 4 and Q21 = 5 and Q28 != 3 and Q24 != 2 and Q27 != 2 and Q9 = 3 | 9 | 0.001018 |
| Q6 != 1 and Q26 != 1 and Q3 != 1 and attendance != 4 and Q21 = 5 and Q28 != 3 and Q7 != 2 and difficulty != 1 and Q16 != 3 and Q4 != 2 and Q16 != 2 and Q8 != 2 and Q6 != 3 and Q1 != 2 and Q5 != 3 and Q10 != 3 and Q20 = 5 and Q25 != 4 and Q27 = 5 and attendance = 1 | 5 | 0.001283 |
| Q6 != 1 and Q26 != 1 and Q3 = 1 | 5 | 0.001335 |
| Q6 != 1 and Q26 != 1 and attendance != 4 and Q21 = 5 and Q28 != 3 and Q7 != 2 and difficulty != 1 and Q16 = 3 | 8 | 0.002209 |
| Q6 != 1 and Q26 != 1 and attendance != 4 and Q23 = 5 and difficulty != 5 and Q9 != 3 and Q6 != 3 and Q10 != 3 and Q20 != 5 | 3 | 0.001540 |
| Q6 != 1 and Q26 != 1 and attendance != 4 and Q23 = 5 and difficulty != 5 | 8 | 0.004564 |
| Q6 != 1 and Q26 != 1 and Q23 = 5 | 3 | 0.009467 |
| attendance = 4 and Q11 = 3 | 9 | 0.000672 |
| attendance != 4 and Q6 != 1 and Q26 = 1 | 9 | 0.002100 |
| attendance != 4 and Q6 != 1 and Q7 = 1 and Q2 != 2 | 5 | 0.001395 |
| attendance != 4 and Q7 != 1 and Q8 != 1 and Q10 != 1 and Q2 != 1 and Q9 != 1 and Q18 != 1 and Q12 != 1 and Q24 != 5 and Q2 = 5 | 5 | 0.001608 |
| attendance != 4 and Q7 != 1 and Q6 != 1 and Q8 != 1 and Q2 != 1 and Q18 != 1 and Q16 != 1 and Q9 != 1 and Q3 != 5 and Q24 != 5 and Q12 != 5 and Q20 != 5 and Q10 != 5 and Q11 != 5 and Q22 != 5 and Q17 != 5 and Q27 != 5 and Q25 != 5 and Q28 != 5 and attendance != 1 and Q21 != 5 and Q1 != 5 and difficulty != 5 and Q17 = 2 and nb.repeat = 1 and Q7 != 4 and Q16 = 2 and Q13 != 3 and Q24 = 2 and difficulty = 1 | 5 | 0.004972 |
| attendance != 4 and Q7 != 1 and Q8 != 1 and Q2 != 1 and Q24 = 5 | 5 | 0.003106 |
| attendance != 4 and Q7 != 1 and Q8 != 1 and Q10 != 1 and Q2 != 1 and Q12 != 5 and Q9 != 1 and Q22 != 5 and Q7 != 5 and Q5 != 5 and Q10 != 5 and Q11 != 5 and Q21 != 5 and Q9 != 5 and Q27 != 5 and Q25 != 5 and Q28 != 5 and Q18 != 5 and Q17 != 5 and Q18 != 1 and nb.repeat != 1 and Q2 != 4 and Q7 != 4 and attendance != 1 | 3 | 0.006115 |
| attendance != 4 and Q7 != 1 and Q8 != 1 and Q2 != 1 and Q6 = 5 | 5 | 0.000197 |
| attendance != 4 and Q7 != 1 and Q8 != 1 and Q10 != 1 and Q2 = 1 | 8 | 0.001001 |
| attendance != 4 and Q6 != 1 and Q7 != 1 and Q8 != 1 and Q10 = 5 | 4 | 0.000133 |
| attendance = 4 | 8 | 0.000607 |
| Q6 = 1 | 13 | 0.000107 |
| Q7 = 1 | 4 | 0.000187 |
| Q11 = 5 and Q24 != 3 and difficulty = 3 | 9 | 0.003587 |
| Q11 != 5 and Q8 != 1 and Q27 != 5 and Q22 = 5 | 5 | 0.000576 |
| Q11 = 5 | 3 | 0.000650 |
| Q20 = 5 | 5 | 0.000839 |
| Q27 = 5 | 3 | 0.000136 |
| Q21 = 5 | 3 | 0.000325 |
| Q12 != 5 and Q9 != 5 and Q25 = 5 | 8 | 0.000812 |
| Q12 != 5 and Q9 != 5 and Q17 = 5 and Q13 != 3 and Q4 != 2 | 4 | 0.000484 |
| Q12 = 5 | 5 | 0.000109 |
| Q9 = 5 | 5 | 0.000241 |
| Q12 = 1 and Q15 = 4 | 5 | 0.000527 |
| Q12 = 1 and Q2 = 2 | 9 | 0.002797 |
| Q18 = 1 | 3 | 0.001252 |
| attendance != 1 and Q9 = 1 | 8 | 0.000143 |
| attendance != 1 and Q1 = 5 | 5 | 0.000044 |
| attendance != 1 and Q5 != 5 and Q28 = 5 | 5 | 0.000136 |
| attendance != 1 and Q5 != 5 and Q13 = 5 | 3 | 0.000120 |
| attendance != 1 and Q5 != 5 and difficulty = 5 and attendance != 0 and Q4 = 4 and Q1 != 3 and attendance = 2 | 5 | 0.000537 |
| attendance != 1 and Q5 != 5 and difficulty != 5 and Q10 != 2 and Q9 != 2 and Q16 != 2 and Q28 != 2 and Q11 != 2 and Q23 != 2 and Q12 != 2 and Q27 != 2 and Q5 != 2 and Q4 != 2 and Q1 != 2 and Q3 != 2 and attendance = 3 and difficulty != 1 | 5 | 0.004466 |
| attendance != 1 and difficulty != 5 and Q10 != 2 and Q9 != 2 and Q15 != 2 and Q16 != 2 and Q11 != 2 and Q18 != 2 and Q6 != 2 and Q28 != 2 and Q23 != 2 and Q12 != 2 and Q27 != 2 and Q5 != 2 and Q8 != 2 and Q1 != 2 and attendance != 3 and difficulty != 4 and Q20 = 3 and Q2 = 3 | 3 | 0.013927 |
| Q15 != 5 and Q5 != 5 and difficulty != 5 and Q25 = 2 and nb.repeat = 1 and Q2 != 4 and Q3 != 4 and Q14 != 4 | 13 | 0.004720 |
| Q10 = 2 and difficulty != 3 and difficulty != 5 and Q12 != 3 and Q6 != 4 and Q3 != 4 and nb.repeat = 1 and difficulty = 1 and Q16 = 3 | 9 | 0.002063 |
| Q10 = 2 | 3 | 0.012340 |
| Q9 = 2 | 5 | 0.006420 |
| nb.repeat != 2 and Q11 != 2 and Q16 = 2 | 9 | 0.005950 |
| Q17 != 2 and Q12 = 2 | 5 | 0.001389 |
| Q11 != 2 and Q18 != 2 and Q28 != 2 and Q25 != 2 and nb.repeat != 2 and Q23 != 2 and Q5 != 2 and Q7 = 2 | 9 | 0.001431 |
| Q11 != 2 and nb.repeat != 2 and Q18 != 2 and Q28 != 2 and Q25 != 2 and Q22 != 2 and Q23 != 2 and Q5 = 2 | 8 | 0.001172 |
| Q11 != 2 and nb.repeat != 2 and Q18 = 2 | 5 | 0.000672 |
| Q5 != 2 and Q20 != 2 and Q21 != 2 and Q27 != 2 and nb.repeat = 2 | 8 | 0.002850 |
| Q5 != 2 and Q20 != 2 and Q21 != 2 and Q27 = 2 | 3 | 0.001436 |
| Q8 != 2 and Q28 = 2 | 3 | 0.002716 |
| Q8 = 2 | 8 | 0.003483 |
| Q25 = 2 | 13 | 0.001134 |
| Q22 = 2 | 3 | 0.001090 |
| Q23 = 2 | 4 | 0.002730 |
| Q3 = 2 and Q13 = 4 | 5 | 0.001321 |
| Q3 = 2 and difficulty = 3 | 4 | 0.000086 |
| Q2 != 2 and attendance = 3 and difficulty != 3 and difficulty != 5 | 13 | 0.004378 |
| Q2 != 2 and difficulty = 5 | 3 | 0.001687 |
| Q2 = 2 | 3 | 0.000353 |
| nb.repeat != 1 and Q19 = 3 | 9 | 0.009561 |
| Q1 = 2 | 9 | 0.011431 |
| nb.repeat != 1 and difficulty != 3 and attendance = 0 | 3 | 0.000423 |
| difficulty = 1 | 3 | 0.006002 |
| attendance != 0 and difficulty != 3 and Q1 != 3 | 5 | 0.008397 |
| attendance = 1 | 5 | 0.003395 |
| attendance != 0 | 3 | 0.025478 |
|  | 5 | 0.087884 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and Q13 = 5 and difficulty = 4 and Q1 = 5 and attendance = 3 | 2 | 0.001139 |
| instr = 1 and Q21 = 5 and attendance = 1 | 2 | 0.000835 |
| instr = 1 and difficulty = 4 and attendance = 2 | 2 | 0.000784 |
| instr = 1 and Q5 = 5 | 2 | 0.001245 |
| instr = 1 and difficulty = 4 and nb.repeat = 3 | 7 | 0.002604 |
| instr = 1 and difficulty = 4 and Q4 = 2 and Q12 = 3 | 7 | 0.001596 |
| instr = 1 and difficulty = 5 and Q1 = 1 | 7 | 0.002768 |
| instr = 1 and difficulty = 4 and Q15 = 4 and Q12 = 2 | 7 | 0.001087 |
| instr = 1 and difficulty = 4 and Q28 = 4 and Q12 = 3 | 7 | 0.000899 |
| instr = 1 and difficulty = 4 and Q8 = 4 and attendance = 1 | 7 | 0.001065 |
| instr = 1 and difficulty = 5 and Q3 = 3 | 7 | 0.001826 |
| instr = 1 and difficulty = 4 | 7 | 0.002196 |
| instr = 1 and Q19 = 1 and difficulty = 3 | 7 | 0.000576 |
| instr = 1 and Q16 = 1 | 7 | 0.000288 |
| instr = 1 and attendance = 1 and Q10 = 3 | 7 | 0.000442 |
| instr = 3 and Q28 = 3 and Q2 = 2 and Q26 = 4 | 4 | 0.000569 |
| instr = 3 and Q20 = 3 and Q23 = 2 and Q17 = 4 and Q7 = 1 | 4 | 0.000822 |
| instr = 3 and Q9 = 3 and Q1 = 1 and Q11 = 2 | 4 | 0.000390 |
| instr = 2 and Q6 = 4 and difficulty = 3 and Q10 = 5 and Q13 = 5 | 1 | 0.001263 |
| instr = 2 and difficulty = 1 and Q4 = 3 | 1 | 0.001814 |
| instr = 2 and Q9 = 4 and difficulty = 3 and Q27 = 2 and Q24 = 2 | 1 | 0.001473 |
| instr = 2 and Q11 = 4 and difficulty = 3 and Q16 = 4 and Q3 = 3 | 1 | 0.000689 |
| instr = 2 and Q6 = 4 and difficulty = 3 and Q23 = 4 | 1 | 0.002635 |
| instr = 2 and Q12 = 5 and attendance = 0 | 1 | 0.001163 |
| instr = 2 and difficulty = 2 and Q5 = 4 and Q28 = 5 and Q13 = 5 | 1 | 0.001263 |
| instr = 1 and difficulty = 1 | 10 | 0.019698 |
| instr = 1 and Q26 = 3 and Q14 = 3 and attendance = 3 | 10 | 0.003367 |
| instr = 1 and difficulty = 2 and Q1 = 2 | 10 | 0.003099 |
| instr = 1 and Q7 = 4 and difficulty = 3 and attendance = 2 | 10 | 0.004212 |
| instr = 1 and Q6 = 4 and attendance = 3 and Q25 = 4 and Q3 = 4 and difficulty = 3 | 10 | 0.005412 |
| instr = 1 and Q26 = 3 and attendance = 0 | 10 | 0.001358 |
| instr = 1 and attendance = 4 and Q19 = 3 | 10 | 0.001796 |
| instr = 1 and Q5 = 4 | 10 | 0.009623 |
| instr = 1 and Q12 = 3 | 10 | 0.004654 |
| instr = 1 and Q2 = 2 | 10 | 0.001976 |
| instr = 2 and difficulty = 4 and Q13 = 4 and Q28 = 5 | 11 | 0.002399 |
| instr = 2 and difficulty = 4 and Q13 = 4 and attendance = 0 | 11 | 0.002159 |
| instr = 2 and difficulty = 4 and Q21 = 3 and Q2 = 4 | 11 | 0.001680 |
| instr = 2 and difficulty = 4 and Q23 = 4 and attendance = 3 | 11 | 0.003149 |
| instr = 2 and difficulty = 4 and Q22 = 3 and attendance = 1 and Q2 = 3 | 11 | 0.002135 |
| instr = 2 and difficulty = 5 and Q12 = 1 | 11 | 0.002348 |
| instr = 2 and difficulty = 4 and Q5 = 2 and Q13 = 2 | 11 | 0.001441 |
| instr = 2 and difficulty = 3 and Q18 = 4 and Q6 = 2 and Q1 = 2 | 11 | 0.001680 |
| instr = 2 and difficulty = 3 and attendance = 3 and Q27 = 4 and Q19 = 4 and Q9 = 3 | 11 | 0.001441 |
| instr = 2 and difficulty = 4 and Q27 = 4 | 11 | 0.002598 |
| instr = 2 and difficulty = 3 and attendance = 3 and Q17 = 5 and Q1 = 1 | 11 | 0.001308 |
| instr = 2 and difficulty = 3 and Q18 = 4 and Q3 = 4 | 11 | 0.004487 |
| instr = 2 and Q22 = 3 and difficulty = 4 | 11 | 0.001548 |
| instr = 2 and Q1 = 5 and Q16 = 4 | 11 | 0.001281 |
| instr = 2 and difficulty = 3 and attendance = 3 and Q14 = 1 | 11 | 0.001081 |
| instr = 2 and difficulty = 5 and Q17 = 4 | 11 | 0.000842 |
| instr = 2 and Q17 = 5 and Q3 = 3 | 11 | 0.001082 |
| instr = 2 and Q27 = 5 | 11 | 0.004213 |
| instr = 2 and difficulty = 1 and Q26 = 4 | 11 | 0.001754 |
| instr = 2 and Q22 = 3 and Q6 = 3 and attendance = 2 and Q1 = 3 | 11 | 0.002170 |
| Q21 = 5 and Q7 = 3 and Q17 = 5 and difficulty = 3 and Q28 = 4 | 8 | 0.001823 |
| attendance = 4 and instr = 3 and Q1 = 2 and Q24 = 3 and Q9 = 3 | 8 | 0.002170 |
| Q21 = 5 and Q5 = 3 and attendance = 4 and Q17 = 5 and Q8 = 3 | 8 | 0.002083 |
| Q21 = 4 and Q1 = 1 and Q16 = 1 and Q27 = 3 | 8 | 0.001340 |
| instr = 3 and Q21 = 4 and Q12 = 2 and attendance = 4 and Q9 = 4 | 8 | 0.002083 |
| Q11 = 5 and Q14 = 4 and Q18 = 2 | 8 | 0.001340 |
| instr = 3 and Q21 = 4 and Q1 = 1 and Q2 = 3 and Q6 = 4 | 8 | 0.001823 |
| instr = 3 and Q21 = 5 and attendance = 3 and Q5 = 1 | 8 | 0.001852 |
| instr = 3 and Q21 = 4 and Q1 = 2 and attendance = 4 | 8 | 0.001065 |
| instr = 3 and Q11 = 5 and Q1 = 1 and Q26 = 3 | 8 | 0.001173 |
| instr = 3 and Q17 = 4 and Q6 = 2 and Q11 = 4 and Q10 = 2 | 8 | 0.001563 |
| instr = 3 and Q17 = 4 and Q4 = 1 and attendance = 4 | 8 | 0.001284 |
| instr = 3 and Q11 = 5 and nb.repeat = 3 | 8 | 0.001370 |
| instr = 3 and Q22 = 4 and Q16 = 2 and difficulty = 5 | 8 | 0.001596 |
| instr = 3 and Q17 = 4 and Q21 = 5 and Q23 = 4 | 8 | 0.001088 |
| instr = 3 and Q21 = 4 and Q18 = 3 and Q24 = 4 and difficulty = 4 | 8 | 0.001192 |
| instr = 3 and difficulty = 3 and Q25 = 5 and nb.repeat = 2 | 8 | 0.001243 |
| instr = 3 and Q21 = 4 and Q5 = 1 and Q7 = 1 | 8 | 0.001408 |
| instr = 3 and difficulty = 3 and Q25 = 5 and Q7 = 3 | 8 | 0.000928 |
| instr = 2 and Q9 = 3 and Q17 = 4 and Q7 = 3 | 6 | 0.003925 |
| instr = 2 and Q12 = 4 and Q14 = 5 | 6 | 0.003905 |
| instr = 2 and Q3 = 4 and Q2 = 2 and Q15 = 4 | 6 | 0.002475 |
| instr = 2 and Q9 = 3 and Q27 = 2 | 6 | 0.002377 |
| instr = 2 and Q27 = 3 and Q14 = 2 | 6 | 0.002749 |
| instr = 2 and Q4 = 3 and Q14 = 4 and difficulty = 2 and Q18 = 4 | 6 | 0.002475 |
| instr = 2 and Q12 = 4 and Q20 = 3 | 6 | 0.002219 |
| instr = 2 and difficulty = 3 and Q1 = 3 and attendance = 1 | 6 | 0.003074 |
| instr = 2 and Q16 = 4 | 6 | 0.024511 |
| instr = 2 and Q21 = 2 and difficulty = 3 | 6 | 0.002024 |
| instr = 2 and Q9 = 3 | 6 | 0.009090 |
| instr = 2 and Q19 = 1 and difficulty = 4 | 6 | 0.001349 |
| instr = 2 and Q18 = 2 | 6 | 0.001755 |
| instr = 2 and Q2 = 1 | 6 | 0.003170 |
| instr = 2 and Q15 = 5 | 6 | 0.016024 |
| Q9 = 3 and nb.repeat = 2 and Q4 = 2 | 9 | 0.001706 |
| Q9 = 3 and nb.repeat = 2 and difficulty = 4 and attendance = 3 | 9 | 0.001152 |
| Q9 = 3 and nb.repeat = 3 and Q24 = 3 | 9 | 0.002812 |
| Q11 = 4 and Q7 = 2 and Q16 = 2 and Q19 = 3 | 9 | 0.001958 |
| Q7 = 3 and nb.repeat = 2 and difficulty = 4 | 9 | 0.001593 |
| Q11 = 4 and Q9 = 3 | 9 | 0.001730 |
| Q11 = 5 and Q1 = 2 | 9 | 0.001593 |
| attendance = 0 and Q14 = 3 and difficulty = 3 | 9 | 0.001188 |
| Q6 = 4 and Q7 = 3 | 9 | 0.001565 |
| Q11 = 4 and Q24 = 1 | 9 | 0.001140 |
| nb.repeat = 1 and difficulty = 4 and Q13 = 4 and attendance = 1 | 5 | 0.002574 |
| nb.repeat = 1 and attendance = 3 and Q6 = 4 and Q10 = 3 and Q3 = 4 | 5 | 0.001993 |
| nb.repeat = 1 and difficulty = 4 and Q1 = 4 and attendance = 2 | 5 | 0.003026 |
| nb.repeat = 1 and attendance = 3 and difficulty = 4 and Q2 = 3 and Q16 = 4 | 5 | 0.001542 |
| nb.repeat = 1 and Q24 = 2 and Q18 = 2 and attendance = 0 and Q2 = 2 and Q1 = 3 and Q3 = 2 | 5 | 0.001542 |
| nb.repeat = 1 and attendance = 3 and Q15 = 5 | 5 | 0.002108 |
| nb.repeat = 1 and Q24 = 2 and Q18 = 2 and difficulty = 1 and Q2 = 2 | 5 | 0.002886 |
| nb.repeat = 1 and Q13 = 4 and Q20 = 3 | 5 | 0.002615 |
| nb.repeat = 1 and Q6 = 4 and attendance = 3 | 5 | 0.002846 |
| nb.repeat = 1 and attendance = 4 and Q14 = 4 | 5 | 0.002916 |
| nb.repeat = 1 and Q4 = 5 and difficulty = 5 | 5 | 0.001269 |
| Q6 = 1 and Q28 = 4 and Q25 = 4 | 13 | 0.001677 |
| Q17 = 1 and difficulty = 2 and attendance = 1 and nb.repeat = 1 | 13 | 0.001767 |
| Q6 = 1 and Q22 = 2 and Q11 = 1 and Q20 = 1 | 13 | 0.002018 |
| Q4 = 1 and Q1 = 2 and Q3 = 2 and Q18 = 1 | 13 | 0.002354 |
| Q6 = 1 and Q24 = 2 | 13 | 0.002798 |
| Q17 = 1 and nb.repeat = 2 and attendance = 1 | 13 | 0.001677 |
| Q17 = 1 and attendance = 4 | 13 | 0.003476 |
| Q17 = 1 and Q1 = 3 | 13 | 0.001770 |
| Q1 = 1 and Q11 = 2 | 13 | 0.004777 |
| Q11 = 1 and attendance = 0 and nb.repeat = 3 | 13 | 0.001594 |
| Q17 = 1 and Q9 = 1 and difficulty = 3 | 13 | 0.001044 |
| difficulty = 2 and Q28 = 3 and nb.repeat = 1 and Q23 = 3 | 13 | 0.003838 |
| Q17 = 1 and difficulty = 1 | 13 | 0.008436 |
| Q19 = 5 and difficulty = 2 and attendance = 1 | 13 | 0.001286 |
| Q19 = 5 and Q3 = 4 | 13 | 0.004111 |
| Q21 = 5 and Q9 = 4 | 13 | 0.001517 |
| nb.repeat = 2 and Q10 = 5 | 13 | 0.002588 |
| nb.repeat = 2 and Q22 = 3 and attendance = 1 | 13 | 0.003096 |
| Q4 = 5 and Q7 = 4 | 13 | 0.000420 |
| attendance = 0 and Q14 = 2 | 13 | 0.001468 |
| Q9 = 5 and Q18 = 3 | 13 | 0.000966 |
| Q2 = 1 and nb.repeat = 3 | 13 | 0.000540 |
| Q10 = 5 and difficulty = 3 | 13 | 0.001413 |
|  | 3 | 0.278329 |


# Text representation of classifiers as-is

## Decision Table

Non matches covered by Majority class

instr|nb.repeat|difficulty|class
---|---|---|---
2|3|5|6
1|3|5|7
3|3|5|13
2|2|5|6
1|2|5|7
3|2|5|3
2|3|4|11
1|3|4|7
2|1|5|11
3|3|4|3
3|1|5|3
1|1|5|7
1|2|4|7
2|2|4|11
3|2|4|9
1|3|3|2
2|3|3|11
2|1|4|11
3|3|3|8
3|1|4|3
1|1|4|7
2|2|3|6
1|2|3|10
3|2|3|9
2|3|2|6
3|3|2|9
2|1|3|6
3|1|3|3
1|1|3|10
1|2|2|10
2|2|2|6
3|2|2|13
2|3|1|6
2|1|2|6
3|3|1|9
3|1|2|13
1|3|1|2
1|1|2|10
2|2|1|6
3|2|1|13
2|1|1|6
3|1|1|3
1|1|1|10

## JRip

Decision list:

rules | predicted class
---|---
(instr = 1) and (Q13 = 5) and (difficulty = 4) and (Q1 = 5) and (attendance = 3)|2 (11.0/3.0)
(instr = 1) and (Q21 = 5) and (attendance = 1)|2 (19.0/10.0)
(instr = 1) and (difficulty = 4) and (attendance = 2)|2 (25.0/15.0)
(instr = 1) and (Q5 = 5)|2 (130.0/100.0)
(instr = 1) and (difficulty = 4) and (nb.repeat = 3)|7 (10.0/0.0)
(instr = 1) and (difficulty = 4) and (Q4 = 2) and (Q12 = 3)|7 (8.0/0.0)
(instr = 1) and (difficulty = 5) and (Q1 = 1)|7 (24.0/7.0)
(instr = 1) and (difficulty = 4) and (Q15 = 4) and (Q12 = 2)|7 (7.0/0.0)
(instr = 1) and (difficulty = 4) and (Q28 = 4) and (Q12 = 3)|7 (7.0/1.0)
(instr = 1) and (difficulty = 4) and (Q8 = 4) and (attendance = 1)|7 (12.0/4.0)
(instr = 1) and (difficulty = 5) and (Q3 = 3)|7 (28.0/12.0)
(instr = 1) and (difficulty = 4)|7 (70.0/50.0)
(instr = 1) and (Q19 = 1) and (difficulty = 3)|7 (16.0/9.0)
(instr = 1) and (Q16 = 1)|7 (47.0/37.0)
(instr = 1) and (attendance = 1) and (Q10 = 3)|7 (25.0/18.0)
(instr = 3) and (Q28 = 3) and (Q2 = 2) and (Q26 = 4)|4 (13.0/7.0)
(instr = 3) and (Q20 = 3) and (Q23 = 2) and (Q17 = 4) and (Q7 = 1)|4 (9.0/3.0)
(instr = 3) and (Q9 = 3) and (Q1 = 1) and (Q11 = 2)|4 (18.0/12.0)
(instr = 2) and (Q6 = 4) and (difficulty = 3) and (Q10 = 5) and (Q13 = 5)|1 (6.0/0.0)
(instr = 2) and (difficulty = 1) and (Q4 = 3)|1 (79.0/53.0)
(instr = 2) and (Q9 = 4) and (difficulty = 3) and (Q27 = 2) and (Q24 = 2)|1 (7.0/0.0)
(instr = 2) and (Q11 = 4) and (difficulty = 3) and (Q16 = 4) and (Q3 = 3)|1 (15.0/8.0)
(instr = 2) and (Q6 = 4) and (difficulty = 3) and (Q23 = 4)|1 (133.0/92.0)
(instr = 2) and (Q12 = 5) and (attendance = 0)|1 (59.0/41.0)
(instr = 2) and (difficulty = 2) and (Q5 = 4) and (Q28 = 5) and (Q13 = 5)|1 (6.0/0.0)
(instr = 1) and (difficulty = 1)|10 (56.0/0.0)
(instr = 1) and (Q26 = 3) and (Q14 = 3) and (attendance = 3)|10 (14.0/0.0)
(instr = 1) and (difficulty = 2) and (Q1 = 2)|10 (12.0/0.0)
(instr = 1) and (Q7 = 4) and (difficulty = 3) and (attendance = 2)|10 (20.0/1.0)
(instr = 1) and (Q6 = 4) and (attendance = 3) and (Q25 = 4) and (Q3 = 4) and (difficulty = 3)|10 (32.0/4.0)
(instr = 1) and (Q26 = 3) and (attendance = 0)|10 (6.0/0.0)
(instr = 1) and (attendance = 4) and (Q19 = 3)|10 (6.0/0.0)
(instr = 1) and (Q5 = 4)|10 (70.0/22.0)
(instr = 1) and (Q12 = 3)|10 (15.0/4.0)
(instr = 1) and (Q2 = 2)|10 (17.0/7.0)
(instr = 2) and (difficulty = 4) and (Q13 = 4) and (Q28 = 5)|11 (10.0/0.0)
(instr = 2) and (difficulty = 4) and (Q13 = 4) and (attendance = 0)|11 (9.0/0.0)
(instr = 2) and (difficulty = 4) and (Q21 = 3) and (Q2 = 4)|11 (7.0/0.0)
(instr = 2) and (difficulty = 4) and (Q23 = 4) and (attendance = 3)|11 (22.0/5.0)
(instr = 2) and (difficulty = 4) and (Q22 = 3) and (attendance = 1) and (Q2 = 3)|11 (19.0/6.0)
(instr = 2) and (difficulty = 5) and (Q12 = 1)|11 (23.0/8.0)
(instr = 2) and (difficulty = 4) and (Q5 = 2) and (Q13 = 2)|11 (6.0/0.0)
(instr = 2) and (difficulty = 3) and (Q18 = 4) and (Q6 = 2) and (Q1 = 2)|11 (7.0/0.0)
(instr = 2) and (difficulty = 3) and (attendance = 3) and (Q27 = 4) and (Q19 = 4) and (Q9 = 3)|11 (6.0/0.0)
(instr = 2) and (difficulty = 4) and (Q27 = 4)|11 (45.0/22.0)
(instr = 2) and (difficulty = 3) and (attendance = 3) and (Q17 = 5) and (Q1 = 1)|11 (9.0/2.0)
(instr = 2) and (difficulty = 3) and (Q18 = 4) and (Q3 = 4)|11 (26.0/11.0)
(instr = 2) and (Q22 = 3) and (difficulty = 4)|11 (39.0/22.0)
(instr = 2) and (Q1 = 5) and (Q16 = 4)|11 (8.0/2.0)
(instr = 2) and (difficulty = 3) and (attendance = 3) and (Q14 = 1)|11 (8.0/2.0)
(instr = 2) and (difficulty = 5) and (Q17 = 4)|11 (13.0/6.0)
(instr = 2) and (Q17 = 5) and (Q3 = 3)|11 (14.0/6.0)
(instr = 2) and (Q27 = 5)|11 (165.0/114.0)
(instr = 2) and (difficulty = 1) and (Q26 = 4)|11 (61.0/39.0)
(instr = 2) and (Q22 = 3) and (Q6 = 3) and (attendance = 2) and (Q1 = 3)|11 (26.0/11.0)
(Q21 = 5) and (Q7 = 3) and (Q17 = 5) and (difficulty = 3) and (Q28 = 4)|8 (7.0/0.0)
(attendance = 4) and (instr = 3) and (Q1 = 2) and (Q24 = 3) and (Q9 = 3)|8 (12.0/2.0)
(Q21 = 5) and (Q5 = 3) and (attendance = 4) and (Q17 = 5) and (Q8 = 3)|8 (8.0/0.0)
(Q21 = 4) and (Q1 = 1) and (Q16 = 1) and (Q27 = 3)|8 (7.0/1.0)
(instr = 3) and (Q21 = 4) and (Q12 = 2) and (attendance = 4) and (Q9 = 4)|8 (8.0/0.0)
(Q11 = 5) and (Q14 = 4) and (Q18 = 2)|8 (7.0/1.0)
(instr = 3) and (Q21 = 4) and (Q1 = 1) and (Q2 = 3) and (Q6 = 4)|8 (7.0/0.0)
(instr = 3) and (Q21 = 5) and (attendance = 3) and (Q5 = 1)|8 (9.0/1.0)
(instr = 3) and (Q21 = 4) and (Q1 = 2) and (attendance = 4)|8 (12.0/5.0)
(instr = 3) and (Q11 = 5) and (Q1 = 1) and (Q26 = 3)|8 (8.0/2.0)
(instr = 3) and (Q17 = 4) and (Q6 = 2) and (Q11 = 4) and (Q10 = 2)|8 (6.0/0.0)
(instr = 3) and (Q17 = 4) and (Q4 = 1) and (attendance = 4)|8 (12.0/5.0)
(instr = 3) and (Q11 = 5) and (nb.repeat = 3)|8 (42.0/27.0)
(instr = 3) and (Q22 = 4) and (Q16 = 2) and (difficulty = 5)|8 (7.0/1.0)
(instr = 3) and (Q17 = 4) and (Q21 = 5) and (Q23 = 4)|8 (24.0/14.0)
(instr = 3) and (Q21 = 4) and (Q18 = 3) and (Q24 = 4) and (difficulty = 4)|8 (13.0/5.0)
(instr = 3) and (difficulty = 3) and (Q25 = 5) and (nb.repeat = 2)|8 (21.0/11.0)
(instr = 3) and (Q21 = 4) and (Q5 = 1) and (Q7 = 1)|8 (12.0/4.0)
(instr = 3) and (difficulty = 3) and (Q25 = 5) and (Q7 = 3)|8 (17.0/9.0)
(instr = 2) and (Q9 = 3) and (Q17 = 4) and (Q7 = 3)|6 (17.0/1.0)
(instr = 2) and (Q12 = 4) and (Q14 = 5)|6 (7.0/0.0)
(instr = 2) and (Q3 = 4) and (Q2 = 2) and (Q15 = 4)|6 (7.0/0.0)
(instr = 2) and (Q9 = 3) and (Q27 = 2)|6 (12.0/2.0)
(instr = 2) and (Q27 = 3) and (Q14 = 2)|6 (9.0/0.0)
(instr = 2) and (Q4 = 3) and (Q14 = 4) and (difficulty = 2) and (Q18 = 4)|6 (8.0/0.0)
(instr = 2) and (Q12 = 4) and (Q20 = 3)|6 (12.0/3.0)
(instr = 2) and (difficulty = 3) and (Q1 = 3) and (attendance = 1)|6 (26.0/10.0)
(instr = 2) and (Q16 = 4)|6 (69.0/35.0)
(instr = 2) and (Q21 = 2) and (difficulty = 3)|6 (20.0/7.0)
(instr = 2) and (Q9 = 3)|6 (94.0/53.0)
(instr = 2) and (Q19 = 1) and (difficulty = 4)|6 (10.0/3.0)
(instr = 2) and (Q18 = 2)|6 (47.0/28.0)
(instr = 2) and (Q2 = 1)|6 (86.0/58.0)
(instr = 2) and (Q15 = 5)|6 (12.0/6.0)
(Q9 = 3) and (nb.repeat = 2) and (Q4 = 2)|9 (9.0/2.0)
(Q9 = 3) and (nb.repeat = 2) and (difficulty = 4) and (attendance = 3)|9 (10.0/4.0)
(Q9 = 3) and (nb.repeat = 3) and (Q24 = 3)|9 (60.0/36.0)
(Q11 = 4) and (Q7 = 2) and (Q16 = 2) and (Q19 = 3)|9 (6.0/0.0)
(Q7 = 3) and (nb.repeat = 2) and (difficulty = 4)|9 (19.0/10.0)
(Q11 = 4) and (Q9 = 3)|9 (72.0/51.0)
(Q11 = 5) and (Q1 = 2)|9 (23.0/11.0)
(attendance = 0) and (Q14 = 3) and (difficulty = 3)|9 (27.0/16.0)
(Q6 = 4) and (Q7 = 3)|9 (60.0/43.0)
(Q11 = 4) and (Q24 = 1)|9 (14.0/7.0)
(nb.repeat = 1) and (difficulty = 4) and (Q13 = 4) and (attendance = 1)|5 (21.0/7.0)
(nb.repeat = 1) and (attendance = 3) and (Q6 = 4) and (Q10 = 3) and (Q3 = 4)|5 (6.0/0.0)
(nb.repeat = 1) and (difficulty = 4) and (Q1 = 4) and (attendance = 2)|5 (24.0/11.0)
(nb.repeat = 1) and (attendance = 3) and (difficulty = 4) and (Q2 = 3) and (Q16 = 4)|5 (8.0/2.0)
(nb.repeat = 1) and (Q24 = 2) and (Q18 = 2) and (attendance = 0) and (Q2 = 2) and (Q1 = 3) and (Q3 = 2)|5 (8.0/2.0)
(nb.repeat = 1) and (attendance = 3) and (Q15 = 5)|5 (74.0/48.0)
(nb.repeat = 1) and (Q24 = 2) and (Q18 = 2) and (difficulty = 1) and (Q2 = 2)|5 (55.0/32.0)
(nb.repeat = 1) and (Q13 = 4) and (Q20 = 3)|5 (46.0/25.0)
(nb.repeat = 1) and (Q6 = 4) and (attendance = 3)|5 (93.0/65.0)
(nb.repeat = 1) and (attendance = 4) and (Q14 = 4)|5 (85.0/56.0)
(nb.repeat = 1) and (Q4 = 5) and (difficulty = 5)|5 (34.0/21.0)
(Q6 = 1) and (Q28 = 4) and (Q25 = 4)|13 (7.0/0.0)
(Q17 = 1) and (difficulty = 2) and (attendance = 1) and (nb.repeat = 1)|13 (7.0/1.0)
(Q6 = 1) and (Q22 = 2) and (Q11 = 1) and (Q20 = 1)|13 (7.0/1.0)
(Q4 = 1) and (Q1 = 2) and (Q3 = 2) and (Q18 = 1)|13 (6.0/0.0)
(Q6 = 1) and (Q24 = 2)|13 (39.0/21.0)
(Q17 = 1) and (nb.repeat = 2) and (attendance = 1)|13 (13.0/5.0)
(Q17 = 1) and (attendance = 4)|13 (46.0/26.0)
(Q17 = 1) and (Q1 = 3)|13 (16.0/8.0)
(Q1 = 1) and (Q11 = 2)|13 (51.0/26.0)
(Q11 = 1) and (attendance = 0) and (nb.repeat = 3)|13 (18.0/9.0)
(Q17 = 1) and (Q9 = 1) and (difficulty = 3)|13 (24.0/13.0)
(difficulty = 2) and (Q28 = 3) and (nb.repeat = 1) and (Q23 = 3)|13 (27.0/8.0)
(Q17 = 1) and (difficulty = 1)|13 (222.0/153.0)
(Q19 = 5) and (difficulty = 2) and (attendance = 1)|13 (6.0/0.0)
(Q19 = 5) and (Q3 = 4)|13 (27.0/14.0)
(Q21 = 5) and (Q9 = 4)|13 (21.0/11.0)
(nb.repeat = 2) and (Q10 = 5)|13 (26.0/13.0)
(nb.repeat = 2) and (Q22 = 3) and (attendance = 1)|13 (32.0/18.0)
(Q4 = 5) and (Q7 = 4)|13 (13.0/7.0)
(attendance = 0) and (Q14 = 2)|13 (56.0/41.0)
(Q9 = 5) and (Q18 = 3)|13 (12.0/6.0)
(Q2 = 1) and (nb.repeat = 3)|13 (11.0/4.0)
(Q10 = 5) and (difficulty = 3)|13 (39.0/27.0)
|3 (1519.0/1052.0)


## PART

Decision list:

rules | predicted class
---|---
instr = 1 AND nb.repeat != 3 AND difficulty != 4 AND difficulty != 5 AND Q13 != 5|10 (244.0/58.0)
instr = 1 AND Q10 = 5 AND nb.repeat != 3 AND nb.repeat = 1 AND Q6 = 4 AND difficulty != 4|10 (6.0)
instr = 1 AND Q1 = 5 AND nb.repeat != 3 AND nb.repeat = 1 AND Q9 != 2 AND Q13 = 5 AND Q18 != 4 AND difficulty != 1 AND Q12 != 4 AND difficulty != 4 AND attendance != 0|10 (49.0/17.0)
instr = 1 AND difficulty != 1 AND nb.repeat = 3|7 (22.0/6.0)
instr = 1 AND difficulty = 1|10 (20.0/3.0)
instr = 1 AND difficulty = 3 AND Q18 != 4 AND Q8 != 4|2 (7.0/3.0)
instr = 1 AND difficulty != 3 AND Q10 = 5 AND Q6 != 4|2 (30.0/11.0)
instr = 1 AND difficulty = 3|10 (11.0/1.0)
instr = 1 AND Q8 != 5 AND Q1 != 5 AND Q11 = 5|7 (10.0/4.0)
instr = 1 AND Q8 = 5|7 (9.0)
instr = 1 AND Q1 != 5 AND nb.repeat != 1|7 (9.0/2.0)
instr = 1 AND Q1 != 5 AND Q18 = 2 AND attendance != 0 AND attendance != 4|2 (7.0/3.0)
instr = 1 AND Q1 = 5|10 (5.0/1.0)
instr = 1 AND Q25 = 2 AND Q4 = 2 AND Q9 = 2|10 (3.0/1.0)
instr = 1 AND Q4 != 2 AND Q3 != 2 AND Q25 != 2 AND Q16 != 2 AND Q7 != 2 AND Q12 != 2 AND Q1 = 4|10 (39.0/20.0)
instr != 1 AND instr = 2 AND difficulty = 4|11 (176.0/83.0)
instr = 1|7 (86.0/42.0)
instr = 2 AND difficulty = 5 AND nb.repeat != 3 AND Q1 != 2 AND Q12 != 2 AND Q3 != 2 AND Q16 != 2 AND nb.repeat = 1 AND Q2 != 1 AND attendance != 2 AND Q8 != 4|6 (13.0/5.0)
instr = 2 AND difficulty = 5 AND nb.repeat != 3 AND nb.repeat = 1 AND Q11 != 4|11 (26.0/5.0)
instr = 2 AND difficulty != 1 AND difficulty = 2 AND Q3 != 1 AND Q7 != 1 AND Q15 != 1 AND Q6 != 1 AND Q1 != 1 AND Q24 != 2 AND Q13 != 2 AND Q26 != 2 AND Q12 != 2 AND Q1 != 2 AND Q6 != 2 AND Q27 != 2 AND attendance = 2|6 (15.0/3.0)
instr = 2 AND difficulty != 1 AND difficulty != 2 AND attendance = 0 AND Q13 != 5 AND Q22 != 5|6 (40.0/20.0)
instr = 2 AND difficulty = 3 AND attendance = 0 AND Q13 != 4|6 (9.0)
instr = 2 AND attendance = 1 AND difficulty != 5 AND nb.repeat != 3 AND Q2 != 5 AND Q14 != 5 AND Q27 != 5 AND Q20 != 5 AND Q9 = 3|6 (38.0/15.0)
instr = 2 AND difficulty = 3 AND attendance != 0 AND Q14 = 1 AND Q1 = 1 AND Q3 = 1 AND attendance != 3|1 (5.0/3.0)
instr = 2 AND difficulty = 3 AND Q14 != 1 AND attendance != 0 AND Q26 != 1 AND Q23 != 1 AND Q7 != 1 AND Q15 = 2|6 (18.0/9.0)
instr = 2 AND attendance = 1 AND difficulty != 5 AND Q9 = 3|6 (10.0/3.0)
instr = 2 AND difficulty = 2 AND Q2 != 1 AND Q3 != 1 AND Q7 != 1 AND Q4 != 1 AND Q1 != 1 AND Q27 = 3|6 (16.0/4.0)
instr = 2 AND difficulty = 3 AND Q16 = 1|11 (8.0/2.0)
instr = 2 AND difficulty = 3 AND Q11 != 1 AND attendance != 0 AND Q11 != 2 AND Q10 != 1 AND Q23 != 2 AND Q16 != 2 AND Q10 != 2 AND Q12 = 2|11 (8.0/4.0)
instr = 2 AND difficulty = 3 AND Q11 != 1 AND Q13 != 2 AND Q28 != 2 AND Q16 = 2|11 (7.0/3.0)
instr = 2 AND difficulty = 3 AND Q11 != 1 AND Q13 != 2 AND Q28 != 2 AND Q12 != 2 AND Q9 = 2|11 (6.0/3.0)
instr = 2 AND attendance = 1|6 (98.0/52.0)
instr = 2 AND difficulty = 3 AND Q9 != 1 AND Q10 = 2|1 (6.0/3.0)
instr = 2 AND difficulty = 3 AND Q9 != 1 AND Q24 = 2|1 (5.0/3.0)
instr = 2 AND difficulty = 3 AND Q9 = 1|6 (3.0/1.0)
instr = 2 AND difficulty = 3 AND Q27 = 1|1 (3.0/1.0)
instr = 2 AND difficulty = 3 AND Q27 = 2 AND Q8 = 3|11 (3.0)
instr = 2 AND difficulty = 3 AND Q27 != 2 AND Q6 != 2 AND Q12 != 1 AND Q16 = 4|6 (82.0/47.0)
instr = 2 AND nb.repeat = 2 AND Q24 != 2 AND Q2 != 3|6 (17.0/10.0)
instr = 2 AND nb.repeat = 2|11 (13.0/6.0)
instr = 2 AND difficulty = 2 AND Q26 != 2 AND Q13 != 2 AND Q4 != 2 AND Q27 != 2 AND Q13 != 3 AND Q7 != 3 AND Q10 != 3 AND Q7 != 1 AND attendance = 3 AND Q13 != 4|1 (7.0/2.0)
instr = 2 AND difficulty = 2|6 (54.0/26.0)
instr = 2 AND Q10 = 2|1 (18.0/12.0)
instr = 2 AND Q18 != 2 AND Q17 != 2 AND Q19 = 2|11 (6.0/1.0)
instr = 2 AND Q18 != 2 AND Q17 != 2 AND Q23 != 2 AND Q13 != 2 AND Q2 = 2 AND Q9 != 4|6 (6.0/2.0)
instr = 2 AND Q18 != 2 AND Q2 != 2 AND Q23 != 2 AND Q27 != 2 AND Q13 != 2 AND Q3 != 2 AND Q7 != 2 AND Q4 != 2 AND Q5 != 2 AND difficulty != 5 AND Q4 = 4 AND Q13 != 5 AND Q26 != 5 AND Q5 != 3 AND Q23 = 4 AND attendance != 4 AND attendance != 2 AND attendance = 0|6 (26.0/15.0)
instr = 2 AND Q18 != 2 AND Q2 != 2 AND Q23 != 2 AND Q27 != 2 AND Q13 != 2 AND Q12 != 2 AND Q4 != 2 AND Q1 != 2 AND Q3 != 2 AND Q8 != 2 AND Q7 != 2 AND difficulty != 5 AND Q4 = 4 AND Q25 != 4|6 (19.0/9.0)
instr = 2 AND Q18 != 2 AND Q17 != 2 AND Q2 != 2 AND Q23 != 2 AND Q27 != 2 AND Q13 != 2 AND Q12 != 2 AND Q4 != 2 AND Q1 != 2 AND Q3 != 2 AND Q8 != 2 AND Q7 != 2 AND difficulty != 5 AND Q4 = 4 AND Q20 = 4 AND attendance != 2|11 (9.0/5.0)
instr = 2 AND Q18 != 2 AND Q17 != 2 AND Q2 != 2 AND Q23 != 2 AND Q27 != 2 AND Q20 = 4 AND Q7 != 2|6 (25.0/13.0)
instr = 2 AND Q23 != 4 AND Q19 != 4 AND Q28 != 4 AND Q27 != 4 AND Q13 != 4 AND Q22 != 2 AND Q8 != 2 AND Q12 != 4 AND Q3 != 4 AND Q4 != 2 AND Q11 != 4 AND Q9 != 4 AND Q1 != 4 AND nb.repeat = 1 AND attendance != 3 AND attendance = 4|1 (28.0/17.0)
instr = 2 AND Q23 != 4 AND Q19 != 4 AND Q28 != 4 AND Q27 != 4 AND Q13 != 4 AND Q22 != 2 AND Q8 != 2 AND Q3 != 4 AND Q4 != 2 AND Q1 != 4 AND Q10 != 4 AND Q11 != 4 AND attendance != 4 AND difficulty != 1 AND Q6 = 5|6 (22.0/12.0)
instr = 2 AND Q23 != 4 AND Q19 != 4 AND Q28 != 4 AND Q27 != 4 AND Q13 != 4 AND Q22 != 2 AND Q8 != 2 AND Q12 != 4 AND Q3 != 4 AND Q4 != 2 AND Q11 != 4 AND Q9 != 4 AND Q1 != 4 AND nb.repeat = 1 AND attendance != 3 AND difficulty = 1|1 (110.0/78.0)
instr = 2 AND Q23 != 4 AND Q21 != 4 AND Q19 != 4 AND Q27 != 4 AND Q13 != 4 AND Q22 != 1 AND Q26 != 2 AND attendance != 0 AND nb.repeat = 1 AND Q6 != 4|6 (33.0/17.0)
instr = 2 AND Q22 != 2 AND Q2 != 2 AND Q25 != 4 AND Q12 != 4|1 (23.0/15.0)
instr = 2 AND Q25 = 4|11 (17.0/6.0)
instr = 2|6 (12.0/4.0)
difficulty = 2 AND attendance = 4 AND Q22 = 4|8 (12.0/4.0)
difficulty = 2 AND Q11 = 2 AND Q19 != 4 AND Q22 != 2|13 (13.0/1.0)
nb.repeat != 1 AND difficulty = 5 AND Q9 != 2 AND Q1 != 2 AND Q19 != 4 AND Q25 = 1 AND nb.repeat != 2|13 (7.0/3.0)
nb.repeat != 1 AND difficulty = 5 AND Q25 != 1 AND Q20 != 1 AND Q11 != 1 AND Q5 != 1|13 (51.0/30.0)
nb.repeat != 1 AND Q28 = 1 AND attendance != 2 AND attendance != 3 AND nb.repeat = 2|13 (37.0/19.0)
nb.repeat != 1 AND Q1 = 1 AND attendance = 3|8 (13.0/7.0)
nb.repeat != 1 AND Q1 = 1 AND Q16 != 4 AND Q14 != 4 AND Q4 != 3 AND Q6 != 3 AND Q16 != 5 AND Q11 != 2 AND Q8 != 2 AND attendance != 2 AND difficulty != 4 AND difficulty != 5 AND difficulty != 2 AND Q15 != 3 AND Q9 = 1 AND difficulty = 1|9 (7.0/4.0)
nb.repeat != 1 AND Q13 = 1|13 (30.0/18.0)
nb.repeat != 1 AND Q14 != 1 AND Q22 != 1 AND Q9 != 1 AND Q26 != 1 AND Q12 != 1 AND Q1 = 1 AND Q5 != 3|9 (16.0/5.0)
nb.repeat != 1 AND Q14 != 1 AND Q9 = 1|13 (11.0/4.0)
nb.repeat != 1 AND Q14 != 1 AND Q22 != 1 AND Q2 != 1 AND Q1 != 1 AND Q7 != 1 AND Q2 != 4 AND Q1 != 4 AND Q7 != 4 AND Q5 != 4 AND Q10 != 4 AND Q12 != 1 AND Q27 != 1 AND Q13 = 4|3 (11.0/6.0)
nb.repeat != 1 AND Q14 != 1 AND Q22 != 1 AND Q2 != 1 AND Q1 != 1 AND Q7 != 1 AND Q21 = 3 AND Q24 != 2 AND Q26 != 2 AND Q16 != 2 AND Q9 = 3 AND Q3 = 3 AND attendance != 3 AND difficulty = 1|3 (17.0/11.0)
nb.repeat != 1 AND Q14 != 1 AND Q22 != 1 AND Q2 != 1 AND Q1 != 1 AND Q7 != 1 AND difficulty = 1 AND Q16 != 4 AND Q1 != 5|9 (10.0/4.0)
difficulty = 2 AND Q11 = 2|13 (24.0/15.0)
difficulty = 2 AND Q27 != 2 AND Q25 != 2 AND Q28 != 2 AND Q12 = 2|8 (10.0/6.0)
difficulty = 2 AND Q27 = 2|8 (9.0/5.0)
difficulty = 2 AND Q25 != 2 AND Q10 != 2 AND Q16 != 2 AND Q28 = 1|13 (7.0/2.0)
difficulty = 2 AND Q23 != 2 AND Q28 != 2 AND Q10 != 1 AND Q10 != 2 AND Q1 = 1|13 (6.0/1.0)
nb.repeat = 2 AND Q18 != 1 AND Q7 != 1 AND Q27 != 1 AND Q10 = 2|9 (18.0/11.0)
nb.repeat = 2 AND Q9 != 2 AND Q3 != 1 AND Q6 != 2 AND Q11 != 1 AND Q15 != 2 AND attendance != 3 AND Q1 != 2 AND Q14 != 2 AND difficulty != 1 AND Q16 != 2 AND difficulty = 4 AND attendance != 2 AND attendance != 0|3 (10.0/7.0)
nb.repeat = 2 AND Q9 != 2 AND Q3 != 1 AND Q6 != 2 AND attendance = 3 AND Q4 != 5 AND difficulty != 3|9 (13.0/5.0)
nb.repeat = 2 AND Q9 != 2 AND Q3 != 1 AND Q6 != 2 AND Q1 != 2 AND Q15 != 2 AND Q21 = 5 AND Q25 != 4 AND difficulty = 3|8 (11.0/5.0)
Q17 = 1 AND nb.repeat = 1 AND Q10 = 5|9 (3.0/1.0)
Q17 = 1 AND nb.repeat = 1 AND Q9 = 5 AND Q3 = 1|3 (3.0/2.0)
Q17 = 1 AND Q9 != 5 AND nb.repeat = 1 AND Q13 != 3 AND Q8 != 4 AND Q11 != 2 AND Q12 != 3 AND Q9 != 3 AND Q7 != 3 AND Q1 != 5 AND Q9 = 1 AND Q12 = 1 AND Q3 = 1 AND Q5 = 1 AND Q6 = 1|3 (223.0/145.0)
Q17 = 1 AND Q9 != 5 AND Q8 != 4 AND attendance != 2 AND nb.repeat = 1 AND difficulty != 4 AND attendance != 3 AND Q9 != 1|13 (14.0/5.0)
difficulty = 2 AND Q23 != 2 AND Q8 = 2|5 (6.0/2.0)
difficulty = 2 AND Q16 != 2 AND Q23 != 2 AND attendance = 4 AND Q1 = 3|13 (4.0/1.0)
difficulty = 2|13 (90.0/59.0)
Q15 = 1 AND Q8 != 4 AND Q28 != 5 AND Q3 != 4 AND attendance != 2 AND Q21 != 2 AND difficulty != 4|13 (34.0/12.0)
nb.repeat = 2 AND Q9 != 2 AND Q6 != 2 AND Q3 != 1 AND Q8 != 2 AND Q4 != 2 AND Q1 != 2 AND Q27 != 1 AND Q15 != 2 AND Q11 != 5 AND Q17 != 5 AND attendance = 1 AND Q17 = 3|13 (9.0/5.0)
Q5 = 1 AND Q21 = 4|8 (21.0/8.0)
Q6 = 1 AND Q4 != 5 AND Q12 = 3 AND Q8 != 2|9 (6.0/3.0)
Q6 = 1 AND Q4 != 5 AND Q12 = 3|13 (5.0)
nb.repeat = 2 AND Q9 != 2 AND Q6 != 2 AND Q3 != 1 AND Q8 != 2 AND Q1 != 2 AND Q27 != 1 AND Q6 != 5 AND Q17 != 5 AND attendance != 1 AND Q8 != 3|13 (23.0/10.0)
Q6 != 1 AND Q5 = 1 AND Q28 != 2|8 (24.0/15.0)
Q6 != 1 AND Q11 = 1 AND nb.repeat != 3 AND Q12 != 4 AND Q22 != 1 AND Q19 != 1 AND Q26 = 1|3 (6.0/3.0)
Q11 = 1 AND Q12 = 4|4 (5.0/3.0)
Q11 = 1 AND difficulty = 1 AND Q4 != 2 AND Q13 != 2 AND Q24 != 5 AND Q17 != 5|13 (5.0/1.0)
Q11 = 1 AND nb.repeat != 3 AND Q5 != 1 AND Q20 != 1 AND Q28 != 2 AND Q7 != 4 AND Q13 != 1 AND Q4 != 4 AND Q3 != 4|5 (27.0/13.0)
Q4 != 1 AND Q11 = 1|5 (35.0/20.0)
nb.repeat = 2 AND Q9 != 2 AND Q6 != 2 AND Q7 != 1 AND Q10 != 5 AND Q26 != 5 AND Q25 != 4 AND attendance != 2 AND Q13 != 2 AND Q14 = 3 AND Q18 = 3 AND attendance != 3|9 (11.0/4.0)
Q4 != 1 AND difficulty = 5 AND Q9 = 2|3 (23.0/15.0)
difficulty = 5 AND Q25 != 1 AND Q21 != 2 AND Q15 != 2 AND Q24 != 2 AND Q4 != 1 AND Q9 = 3|3 (56.0/25.0)
Q4 != 1 AND Q27 = 1 AND Q9 != 4 AND Q2 != 4 AND Q7 != 3 AND Q28 != 2|5 (18.0/11.0)
Q27 = 1 AND Q18 != 2 AND Q28 != 3 AND Q4 != 4 AND Q20 != 3 AND Q17 != 3 AND Q9 != 4|3 (21.0/11.0)
Q27 = 1 AND Q4 != 2 AND Q9 != 1 AND Q21 != 2|13 (12.0/6.0)
Q27 != 1 AND Q24 = 1|4 (19.0/15.0)
Q27 = 1|4 (12.0/7.0)
Q21 != 1 AND attendance = 4 AND Q4 != 1 AND Q14 = 2 AND difficulty != 1|5 (11.0/4.0)
Q21 != 1 AND attendance = 4 AND Q6 != 1 AND Q4 != 1 AND Q15 != 2 AND Q1 != 1 AND Q27 != 2 AND Q23 != 2 AND Q9 != 2 AND Q12 != 2 AND Q11 != 2 AND nb.repeat = 1 AND difficulty != 5 AND Q20 != 5 AND Q28 != 5 AND Q21 != 5 AND Q12 != 5 AND Q1 != 2|3 (68.0/45.0)
Q21 != 1 AND attendance = 4 AND Q3 = 2|3 (12.0/7.0)
Q21 != 1 AND attendance = 4 AND difficulty = 5 AND Q4 = 4|3 (8.0/4.0)
Q21 != 1 AND attendance = 4 AND Q11 = 3 AND Q5 != 3|8 (6.0)
Q21 = 1|5 (5.0/1.0)
attendance = 4 AND Q11 = 3 AND Q1 = 2|8 (5.0/1.0)
attendance = 4 AND Q11 != 3 AND Q24 != 3 AND Q14 != 3 AND Q18 != 3 AND Q12 != 2 AND Q2 != 3 AND Q7 != 3 AND Q3 != 3 AND difficulty != 5 AND difficulty != 4|13 (33.0/23.0)
attendance = 4 AND Q11 != 3 AND difficulty = 5 AND Q12 = 5|5 (7.0/4.0)
attendance = 4 AND Q11 != 3 AND Q2 != 5|8 (41.0/17.0)
attendance != 4 AND Q4 = 1 AND Q11 != 5 AND Q24 != 3 AND Q1 != 2 AND Q2 != 2 AND Q19 != 5|3 (17.0/10.0)
Q4 = 1 AND Q19 != 2 AND Q24 != 4 AND Q27 != 2|8 (16.0/10.0)
Q4 = 1|13 (9.0/4.0)
attendance != 4 AND nb.repeat = 2 AND Q9 != 2 AND Q6 != 2 AND Q7 != 5 AND Q13 != 2 AND Q15 != 4 AND Q27 = 4|3 (7.0/3.0)
attendance != 4 AND nb.repeat = 2 AND Q9 != 2 AND Q14 != 4 AND Q13 != 3|9 (10.0/5.0)
attendance != 4 AND Q21 = 5 AND Q24 != 2 AND Q28 != 3 AND Q18 != 3 AND Q3 != 2 AND Q6 != 2 AND Q27 != 2 AND Q9 != 2 AND Q8 != 2 AND Q19 != 3 AND Q26 != 3 AND Q16 != 3 AND Q14 != 3 AND Q5 != 3 AND Q20 = 5 AND Q10 != 3 AND Q1 != 2 AND Q8 != 3 AND Q2 != 1 AND attendance != 1 AND Q12 != 4 AND Q16 != 4 AND Q23 != 4 AND Q19 != 4 AND Q7 != 4 AND nb.repeat = 1 AND difficulty != 5 AND difficulty != 3|5 (106.0/80.0)
attendance != 4 AND nb.repeat = 2 AND Q9 != 2 AND Q6 != 2 AND Q8 = 3 AND attendance = 2|8 (6.0/4.0)
attendance != 4 AND Q21 = 5 AND Q24 != 2 AND Q28 != 3 AND Q18 != 3 AND Q27 != 2 AND Q9 != 3 AND Q13 != 3 AND Q9 != 2 AND Q8 != 2 AND Q26 != 3 AND Q19 != 3 AND Q24 != 3 AND Q16 != 3 AND Q4 != 3 AND Q4 != 2 AND Q3 != 3 AND Q20 != 4 AND nb.repeat = 1 AND Q27 != 3 AND difficulty != 1 AND Q25 != 4 AND Q12 != 4 AND Q16 != 4 AND attendance != 1|3 (36.0/25.0)
Q6 != 1 AND Q26 != 1 AND attendance != 4 AND Q21 = 5 AND Q28 != 3 AND Q24 != 2 AND Q18 != 3 AND Q6 != 2 AND Q27 != 2 AND Q26 != 3 AND Q9 != 2 AND Q9 != 3 AND difficulty = 1|13 (19.0/7.0)
Q6 != 1 AND Q26 != 1 AND Q3 != 1 AND attendance != 4 AND Q21 = 5 AND Q28 != 3 AND Q24 != 2 AND Q27 != 2 AND Q9 = 3|9 (11.0/6.0)
Q6 != 1 AND Q26 != 1 AND Q3 != 1 AND attendance != 4 AND Q21 = 5 AND Q28 != 3 AND Q7 != 2 AND difficulty != 1 AND Q16 != 3 AND Q4 != 2 AND Q16 != 2 AND Q8 != 2 AND Q6 != 3 AND Q1 != 2 AND Q5 != 3 AND Q10 != 3 AND Q20 = 5 AND Q25 != 4 AND Q27 = 5 AND attendance = 1|5 (13.0/6.0)
Q6 != 1 AND Q26 != 1 AND Q3 = 1|5 (9.0/5.0)
Q6 != 1 AND Q26 != 1 AND attendance != 4 AND Q21 = 5 AND Q28 != 3 AND Q7 != 2 AND difficulty != 1 AND Q16 = 3|8 (7.0/2.0)
Q6 != 1 AND Q26 != 1 AND attendance != 4 AND Q23 = 5 AND difficulty != 5 AND Q9 != 3 AND Q6 != 3 AND Q10 != 3 AND Q20 != 5|3 (10.0/3.0)
Q6 != 1 AND Q26 != 1 AND attendance != 4 AND Q23 = 5 AND difficulty != 5|8 (36.0/26.0)
Q6 != 1 AND Q26 != 1 AND Q23 = 5|3 (11.0/4.0)
attendance = 4 AND Q11 = 3|9 (5.0/3.0)
attendance != 4 AND Q6 != 1 AND Q26 = 1|9 (5.0/2.0)
attendance != 4 AND Q6 != 1 AND Q7 = 1 AND Q2 != 2|5 (5.0/2.0)
attendance != 4 AND Q7 != 1 AND Q8 != 1 AND Q10 != 1 AND Q2 != 1 AND Q9 != 1 AND Q18 != 1 AND Q12 != 1 AND Q24 != 5 AND Q2 = 5|5 (20.0/12.0)
attendance != 4 AND Q7 != 1 AND Q6 != 1 AND Q8 != 1 AND Q2 != 1 AND Q18 != 1 AND Q16 != 1 AND Q9 != 1 AND Q3 != 5 AND Q24 != 5 AND Q12 != 5 AND Q20 != 5 AND Q10 != 5 AND Q11 != 5 AND Q22 != 5 AND Q17 != 5 AND Q27 != 5 AND Q25 != 5 AND Q28 != 5 AND attendance != 1 AND Q21 != 5 AND Q1 != 5 AND difficulty != 5 AND Q17 = 2 AND nb.repeat = 1 AND Q7 != 4 AND Q16 = 2 AND Q13 != 3 AND Q24 = 2 AND difficulty = 1|5 (45.0/24.0)
attendance != 4 AND Q7 != 1 AND Q8 != 1 AND Q2 != 1 AND Q24 = 5|5 (17.0/10.0)
attendance != 4 AND Q7 != 1 AND Q8 != 1 AND Q10 != 1 AND Q2 != 1 AND Q12 != 5 AND Q9 != 1 AND Q22 != 5 AND Q7 != 5 AND Q5 != 5 AND Q10 != 5 AND Q11 != 5 AND Q21 != 5 AND Q9 != 5 AND Q27 != 5 AND Q25 != 5 AND Q28 != 5 AND Q18 != 5 AND Q17 != 5 AND Q18 != 1 AND nb.repeat != 1 AND Q2 != 4 AND Q7 != 4 AND attendance != 1|3 (31.0/18.0)
attendance != 4 AND Q7 != 1 AND Q8 != 1 AND Q2 != 1 AND Q6 = 5|5 (13.0/9.0)
attendance != 4 AND Q7 != 1 AND Q8 != 1 AND Q10 != 1 AND Q2 = 1|8 (10.0/6.0)
attendance != 4 AND Q6 != 1 AND Q7 != 1 AND Q8 != 1 AND Q10 = 5|4 (7.0/5.0)
attendance = 4|8 (3.0/1.0)
Q6 = 1|13 (3.0/1.0)
Q7 = 1|4 (3.0/1.0)
Q11 = 5 AND Q24 != 3 AND difficulty = 3|9 (3.0)
Q11 != 5 AND Q8 != 1 AND Q27 != 5 AND Q22 = 5|5 (9.0/4.0)
Q11 = 5|3 (7.0/5.0)
Q20 = 5|5 (7.0/3.0)
Q27 = 5|3 (7.0/4.0)
Q21 = 5|3 (7.0/3.0)
Q12 != 5 AND Q9 != 5 AND Q25 = 5|8 (7.0/4.0)
Q12 != 5 AND Q9 != 5 AND Q17 = 5 AND Q13 != 3 AND Q4 != 2|4 (6.0/1.0)
Q12 = 5|5 (5.0/2.0)
Q9 = 5|5 (5.0/3.0)
Q12 = 1 AND Q15 = 4|5 (3.0)
Q12 = 1 AND Q2 = 2|9 (3.0/1.0)
Q18 = 1|3 (9.0/3.0)
attendance != 1 AND Q9 = 1|8 (4.0/2.0)
attendance != 1 AND Q1 = 5|5 (4.0/2.0)
attendance != 1 AND Q5 != 5 AND Q28 = 5|5 (4.0/2.0)
attendance != 1 AND Q5 != 5 AND Q13 = 5|3 (4.0/1.0)
attendance != 1 AND Q5 != 5 AND difficulty = 5 AND attendance != 0 AND Q4 = 4 AND Q1 != 3 AND attendance = 2|5 (4.0/1.0)
attendance != 1 AND Q5 != 5 AND difficulty != 5 AND Q10 != 2 AND Q9 != 2 AND Q16 != 2 AND Q28 != 2 AND Q11 != 2 AND Q23 != 2 AND Q12 != 2 AND Q27 != 2 AND Q5 != 2 AND Q4 != 2 AND Q1 != 2 AND Q3 != 2 AND attendance = 3 AND difficulty != 1|5 (86.0/61.0)
attendance != 1 AND difficulty != 5 AND Q10 != 2 AND Q9 != 2 AND Q15 != 2 AND Q16 != 2 AND Q11 != 2 AND Q18 != 2 AND Q6 != 2 AND Q28 != 2 AND Q23 != 2 AND Q12 != 2 AND Q27 != 2 AND Q5 != 2 AND Q8 != 2 AND Q1 != 2 AND attendance != 3 AND difficulty != 4 AND Q20 = 3 AND Q2 = 3|3 (152.0/93.0)
Q15 != 5 AND Q5 != 5 AND difficulty != 5 AND Q25 = 2 AND nb.repeat = 1 AND Q2 != 4 AND Q3 != 4 AND Q14 != 4|13 (38.0/25.0)
Q10 = 2 AND difficulty != 3 AND difficulty != 5 AND Q12 != 3 AND Q6 != 4 AND Q3 != 4 AND nb.repeat = 1 AND difficulty = 1 AND Q16 = 3|9 (9.0/5.0)
Q10 = 2|3 (40.0/28.0)
Q9 = 2|5 (23.0/11.0)
nb.repeat != 2 AND Q11 != 2 AND Q16 = 2|9 (7.0/4.0)
Q17 != 2 AND Q12 = 2|5 (14.0/6.0)
Q11 != 2 AND Q18 != 2 AND Q28 != 2 AND Q25 != 2 AND nb.repeat != 2 AND Q23 != 2 AND Q5 != 2 AND Q7 = 2|9 (8.0/5.0)
Q11 != 2 AND nb.repeat != 2 AND Q18 != 2 AND Q28 != 2 AND Q25 != 2 AND Q22 != 2 AND Q23 != 2 AND Q5 = 2|8 (7.0/4.0)
Q11 != 2 AND nb.repeat != 2 AND Q18 = 2|5 (6.0/3.0)
Q5 != 2 AND Q20 != 2 AND Q21 != 2 AND Q27 != 2 AND nb.repeat = 2|8 (6.0/4.0)
Q5 != 2 AND Q20 != 2 AND Q21 != 2 AND Q27 = 2|3 (5.0/1.0)
Q8 != 2 AND Q28 = 2|3 (5.0)
Q8 = 2|8 (4.0/1.0)
Q25 = 2|13 (3.0/1.0)
Q22 = 2|3 (3.0)
Q23 = 2|4 (3.0/1.0)
Q3 = 2 AND Q13 = 4|5 (3.0)
Q3 = 2 AND difficulty = 3|4 (3.0/1.0)
Q2 != 2 AND attendance = 3 AND difficulty != 3 AND difficulty != 5|13 (16.0/9.0)
Q2 != 2 AND difficulty = 5|3 (10.0/5.0)
Q2 = 2|3 (6.0/4.0)
nb.repeat != 1 AND Q19 = 3|9 (6.0/2.0)
Q1 = 2|9 (15.0/9.0)
nb.repeat != 1 AND difficulty != 3 AND attendance = 0|3 (6.0/3.0)
difficulty = 1|3 (98.0/63.0)
attendance != 0 AND difficulty != 3 AND Q1 != 3|5 (29.0/14.0)
attendance = 1|5 (59.0/43.0)
attendance != 0|3 (46.0/26.0)
|5 (29.0/22.0)


## J48 Decision Tree

* instr = 1
	* nb.repeat = 3: 7 (31.0/10.0)
	* nb.repeat != 3
		* difficulty = 4
			* Q18 = 2: 2 (10.0/5.0)
			* Q18 != 2
				* Q4 = 2: 7 (15.0)
				* Q4 != 2
					* Q16 = 2: 7 (8.0/1.0)
					* Q16 != 2
						* Q2 = 4: 7 (52.0/31.0)
						* Q2 != 4
							* Q11 = 4: 7 (15.0/7.0)
							* Q11 != 4: 2 (58.0/30.0)
		* difficulty != 4
			* difficulty = 5
				* Q1 = 1: 7 (25.0/7.0)
				* Q1 != 1
					* attendance = 4
						* Q14 = 5: 7 (9.0/4.0)
						* Q14 != 5: 10 (10.0/2.0)
					* attendance != 4
						* Q12 = 3: 7 (20.0/9.0)
						* Q12 != 3
							* attendance = 3: 10 (8.0/3.0)
							* attendance != 3: 2 (14.0/6.0)
			* difficulty != 5: 10 (421.0/103.0)
* instr != 1
	* instr = 2
		* difficulty = 4
			* Q17 = 1: 6 (12.0/3.0)
			* Q17 != 1: 11 (208.0/89.0)
		* difficulty != 4
			* difficulty = 5
				* nb.repeat = 1
					* Q17 = 3: 6 (19.0/9.0)
					* Q17 != 3: 11 (46.0/16.0)
				* nb.repeat != 1: 6 (10.0/4.0)
			* difficulty != 5: 6 (1002.0/588.0)
	* instr != 2
		* nb.repeat = 1
			* Q17 = 1
				* Q13 = 2: 13 (11.0/5.0)
				* Q13 != 2
					* Q6 = 2: 13 (19.0/7.0)
					* Q6 != 2
						* Q1 = 1
							* attendance = 4: 13 (31.0/17.0)
							* attendance != 4: 3 (274.0/178.0)
						* Q1 != 1: 13 (39.0/19.0)
			* Q17 != 1
				* Q6 = 1
					* Q18 = 4: 13 (14.0/4.0)
					* Q18 != 4
						* Q24 = 4: 8 (8.0/3.0)
						* Q24 != 4
							* Q23 = 4: 8 (8.0/3.0)
							* Q23 != 4
								* difficulty = 5: 3 (22.0/15.0)
								* difficulty != 5: 13 (77.0/52.0)
				* Q6 != 1
					* Q5 = 1
						* Q17 = 2: 5 (8.0/4.0)
						* Q17 != 2: 8 (49.0/22.0)
					* Q5 != 1
						* Q11 = 1
							* Q9 = 4: 13 (9.0/5.0)
							* Q9 != 4
								* attendance = 1: 5 (8.0)
								* attendance != 1
									* Q27 = 3: 5 (14.0/6.0)
									* Q27 != 3
										* Q1 = 2: 3 (12.0/4.0)
										* Q1 != 2
											* Q17 = 4: 3 (12.0/6.0)
											* Q17 != 4: 5 (10.0/2.0)
						* Q11 != 1
							* Q4 = 1
								* Q13 = 2: 13 (9.0/5.0)
								* Q13 != 2
									* Q2 = 2: 4 (11.0/6.0)
									* Q2 != 2: 8 (28.0/14.0)
							* Q4 != 1
								* difficulty = 2
									* attendance = 4: 8 (21.0/13.0)
									* attendance != 4: 13 (101.0/63.0)
								* difficulty != 2
									* difficulty = 5: 3 (204.0/118.0)
									* difficulty != 5
										* Q24 = 1: 9 (15.0/9.0)
										* Q24 != 1
											* difficulty = 1
												* Q3 = 2
													* Q26 = 4: 8 (9.0/5.0)
													* Q26 != 4: 5 (85.0/49.0)
												* Q3 != 2
													* Q9 = 5: 5 (137.0/101.0)
													* Q9 != 5
														* Q24 = 5: 13 (9.0/3.0)
														* Q24 != 5
															* Q2 = 5: 13 (8.0/4.0)
															* Q2 != 5
																* attendance = 3
																	* Q7 = 3: 13 (13.0/7.0)
																	* Q7 != 3: 5 (8.0/5.0)
																* attendance != 3
																	* Q5 = 2
																		* Q11 = 2: 13 (9.0/4.0)
																		* Q11 != 2: 9 (14.0/8.0)
																	* Q5 != 2: 3 (359.0/239.0)
											* difficulty != 1
												* Q20 = 2: 3 (85.0/57.0)
												* Q20 != 2
													* Q16 = 2
														* Q2 = 2: 9 (13.0/5.0)
														* Q2 != 2: 8 (27.0/14.0)
													* Q16 != 2
														* Q23 = 2: 5 (20.0/13.0)
														* Q23 != 2
															* Q16 = 1: 9 (9.0/5.0)
															* Q16 != 1
																* Q3 = 2
																	* Q13 = 4: 5 (10.0/2.0)
																	* Q13 != 4: 3 (20.0/11.0)
																* Q3 != 2
																	* Q5 = 2
																		* Q18 = 3: 8 (18.0/8.0)
																		* Q18 != 3: 9 (10.0/7.0)
																	* Q5 != 2
																		* Q27 = 2: 3 (22.0/10.0)
																		* Q27 != 2
																			* Q11 = 2: 5 (20.0/7.0)
																			* Q11 != 2
																				* Q10 = 2: 9 (9.0/5.0)
																				* Q10 != 2
																					* Q8 = 2: 8 (19.0/10.0)
																					* Q8 != 2
																						* Q12 = 2: 8 (16.0/10.0)
																						* Q12 != 2
																							* difficulty = 3
																								* Q1 = 2: 9 (22.0/13.0)
																								* Q1 != 2
																									* attendance = 2
																										* Q1 = 5: 13 (11.0/6.0)
																										* Q1 != 5: 3 (66.0/33.0)
																									* attendance != 2
																										* Q10 = 4
																											* Q7 = 3: 8 (11.0/4.0)
																											* Q7 != 3
																												* attendance = 1: 8 (14.0/7.0)
																												* attendance != 1: 5 (71.0/49.0)
																										* Q10 != 4
																											* Q6 = 4: 8 (16.0/8.0)
																											* Q6 != 4: 13 (135.0/100.0)
																							* difficulty != 3
																								* Q11 = 3
																									* Q1 = 3: 3 (104.0/65.0)
																									* Q1 != 3: 5 (19.0/10.0)
																								* Q11 != 3
																									* Q18 = 3: 8 (9.0/3.0)
																									* Q18 != 3
																										* attendance = 4: 3 (38.0/26.0)
																										* attendance != 4: 5 (140.0/89.0)
		* nb.repeat != 1
			* difficulty = 5: 13 (95.0/57.0)
			* difficulty != 5
				* Q28 = 1: 13 (71.0/40.0)
				* Q28 != 1
					* Q2 = 1
						* Q20 = 3: 4 (9.0/6.0)
						* Q20 != 3: 13 (21.0/12.0)
					* Q2 != 1: 9 (421.0/294.0)


## SimpleCart Decision Tree

* instr=(3)
		* nb.repeat=(3)|(2)
				* Q10=(4)|(3)|(2): 9(126.0/305.0)
				* Q10!=(4)|(3)|(2): 13(76.0/110.0)
		* nb.repeat!=(3)|(2)
			* Q21=(5)|(4)
				* Q1=(5)|(4): 5(198.0/569.0)
				* Q1!=(5)|(4): 8(138.0/299.0)
			* Q21!=(5)|(4)
						* Q17=(5)|(4)|(3)|(2)
				* difficulty=(2): 13(25.0/28.0)
				* difficulty!=(2): 3(314.0/686.0)
						* Q17!=(5)|(4)|(3)|(2): 13(125.0/237.0)
* instr!=(3)
		* instr=(2)|(3)
			* difficulty=(5)|(4): 11(158.0/137.0)
			* difficulty!=(5)|(4): 6(414.0/588.0)
		* instr!=(2)|(3)
			* difficulty=(5)|(4): 7(122.0/146.0)
			* difficulty!=(5)|(4): 10(322.0/106.0)


