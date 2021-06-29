# Extracted rules

## Unordered rules

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty != 5 | 10 | 0.047761 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 != 1 | 11 | 0.014963 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance = 1 and Q27 != 5 | 6 | 0.009174 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 != 2 and Q16 != 3 | 6 | 0.006207 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance != 3 and Q15 != 4 and Q17 != 4 and Q9 != 2 | 3 | 0.005117 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance != 3 and difficulty != 4 and attendance != 4 and attendance = 0 and difficulty = 1 | 13 | 0.004881 |
| instr!=(3) and instr != 3 and difficulty = 4 | 7 | 0.003116 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty = 2 and Q25 != 5 | 6 | 0.004423 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty = 5 | 11 | 0.004289 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance = 2 and difficulty = 3 | 3 | 0.003822 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 != 5 and Q22 != 4 | 13 | 0.003701 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 = 2 and Q14 = 2 | 6 | 0.003306 |
| instr!=(3) and instr != 3 and difficulty = 5 | 7 | 0.002216 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 = 2 and Q9 != 3 and Q8 = 2 | 5 | 0.002737 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty != 5 and nb.repeat = 2 | 13 | 0.002559 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty = 5 and Q2 != 2 | 13 | 0.002422 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance != 3 and Q15 = 4 and Q22 != 3 | 3 | 0.002045 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and Q1 != 5 and Q17 != 5 and Q22 != 1 and Q28 != 4 | 10 | 0.001462 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 = 2 and Q1 != 1 | 11 | 0.001858 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 = 1 and attendance != 2 and Q28 = 4 | 5 | 0.001741 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 = 2 | 8 | 0.001712 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 != 4 and attendance = 2 | 3 | 0.001718 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 = 1 | 6 | 0.001764 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty != 3 and Q1 = 4 | 5 | 0.001670 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 != 5 and Q20 != 5 and Q12 != 2 and Q4 != 4 | 3 | 0.001642 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty = 2 | 13 | 0.001648 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and Q1 = 5 and attendance != 4 | 2 | 0.001308 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance = 0 and Q13 != 5 and Q2 = 3 | 6 | 0.001602 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance != 2 and difficulty != 1 and Q9 = 3 and attendance = 0 | 9 | 0.001450 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty = 5 | 13 | 0.001467 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance = 0 and Q13 = 5 | 6 | 0.001506 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty = 3 and Q25 = 3 | 13 | 0.001443 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 != 4 and Q25 != 4 and Q23 != 5 and attendance = 0 and Q19 != 1 | 11 | 0.001429 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 = 2 | 5 | 0.001353 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 != 4 and Q5 = 5 and Q1 = 5 and attendance != 0 | 3 | 0.001367 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty != 5 and Q6 = 2 | 8 | 0.001341 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance != 2 and difficulty != 1 and Q9 = 3 and attendance != 0 | 13 | 0.001296 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 != 1 | 13 | 0.001296 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 = 4 | 3 | 0.001280 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 != 5 and Q20 != 5 and Q12 != 2 and Q4 = 4 and Q8 = 4 | 5 | 0.001254 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 != 2 and Q16 = 3 and nb.repeat = 1 and attendance != 2 and Q1 = 3 | 6 | 0.001327 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 = 2 and Q7 != 2 | 6 | 0.001324 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 = 2 and Q13 != 2 | 3 | 0.001260 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 != 4 and Q25 != 4 and Q23 = 5 | 6 | 0.001307 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 = 4 and difficulty = 4 | 5 | 0.001200 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 != 5 and Q8 != 2 and Q1 != 2 and Q21 = 3 | 9 | 0.001169 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 = 2 and Q26 = 2 | 3 | 0.001194 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 = 1 and Q15 != 3 | 9 | 0.001156 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty != 3 and Q1 != 4 and Q24 = 3 and Q17 = 3 | 5 | 0.001157 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 = 4 and Q25 = 4 and attendance = 0 | 11 | 0.001207 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 = 1 and Q8 != 2 and Q21 != 3 and Q26 = 3 | 8 | 0.001141 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q21 != 4 and Q27 != 5 and attendance != 3 and Q6 != 1 and Q9 != 3 | 10 | 0.000830 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 = 4 | 8 | 0.001132 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty = 5 and Q14 != 3 | 8 | 0.001118 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 = 2 and Q13 = 2 and difficulty != 3 | 13 | 0.001131 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 != 2 and Q16 = 3 and nb.repeat = 1 and attendance = 2 | 11 | 0.001162 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 != 4 and attendance != 2 and Q9 != 5 and Q13 = 3 and attendance = 1 | 3 | 0.001117 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 = 2 and Q9 != 3 and Q8 != 2 | 3 | 0.001111 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 = 1 | 6 | 0.001144 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 != 4 and Q5 = 5 and Q1 = 5 and attendance = 0 and difficulty = 1 | 5 | 0.001070 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 != 4 and Q25 != 4 and Q23 != 5 and attendance = 0 and Q19 = 1 | 6 | 0.001113 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 = 2 and Q25 != 3 | 8 | 0.001027 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 = 5 | 13 | 0.001044 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 = 1 and attendance = 2 | 3 | 0.001037 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty = 5 and Q7 != 4 and Q12 = 3 | 3 | 0.001037 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 = 5 | 8 | 0.000999 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty = 3 | 13 | 0.001019 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 = 2 | 5 | 0.000983 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 = 2 | 6 | 0.001043 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 = 2 and Q1 = 1 | 6 | 0.001038 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 = 1 and Q8 != 2 and Q21 != 3 and Q26 != 3 | 9 | 0.000946 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 = 4 and difficulty != 4 | 13 | 0.000956 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 = 1 and attendance != 2 and Q28 != 4 and Q5 != 2 | 5 | 0.000922 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance != 3 and difficulty != 4 and attendance = 4 | 13 | 0.000935 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance = 2 and difficulty != 3 and Q1 = 3 | 3 | 0.000909 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty = 4 and Q12 != 4 and Q1 != 2 | 3 | 0.000907 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 = 2 | 6 | 0.000954 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty != 5 and Q6 != 2 and Q22 != 1 and difficulty != 1 and Q9 != 3 | 9 | 0.000867 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 = 5 | 5 | 0.000882 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty != 3 and Q1 != 4 and Q24 != 3 | 5 | 0.000864 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q21 = 4 | 10 | 0.000782 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 != 5 and Q20 = 5 | 8 | 0.000839 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 != 5 and Q20 != 5 and Q12 = 2 | 8 | 0.000839 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance = 2 and difficulty != 3 and Q1 != 3 | 5 | 0.000834 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty != 5 and nb.repeat != 2 and difficulty != 3 and difficulty != 1 | 9 | 0.000801 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 = 1 | 11 | 0.000847 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 != 2 and Q16 = 3 and nb.repeat != 1 | 11 | 0.000836 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance = 0 | 3 | 0.000807 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 = 2 | 11 | 0.000836 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance != 3 and difficulty != 4 and attendance != 4 and attendance != 0 | 3 | 0.000807 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 = 1 and Q2 = 2 | 13 | 0.000807 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 = 4 | 13 | 0.000807 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 != 4 and attendance != 2 and Q9 = 5 | 5 | 0.000778 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 = 2 and Q14 != 2 | 11 | 0.000788 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 = 1 and attendance != 2 and Q28 != 4 and Q5 = 2 | 3 | 0.000742 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 != 2 and Q4 != 2 and Q1 != 2 and attendance = 2 | 10 | 0.000727 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 = 4 and Q25 != 4 | 6 | 0.000763 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 != 4 and Q25 = 4 | 6 | 0.000763 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance = 1 and Q27 = 5 and Q9 = 5 | 11 | 0.000744 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty = 5 and Q7 != 4 and Q12 != 3 | 5 | 0.000707 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance != 3 and Q15 = 4 and Q22 = 3 | 5 | 0.000707 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 != 4 and attendance != 2 and Q9 != 5 and Q13 = 3 and attendance != 1 | 5 | 0.000692 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance != 1 and attendance != 4 and Q4 = 4 | 9 | 0.000651 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty = 2 and Q25 = 5 | 1 | 0.000648 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 = 5 and Q23 != 3 and attendance != 0 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 != 3 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 = 1 and Q18 = 1 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 = 5 and Q23 = 3 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty = 5 and Q7 = 4 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty != 3 and Q1 != 4 and Q24 = 3 and Q17 != 3 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 = 3 | 3 | 0.000630 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 != 2 and attendance != 0 and Q26 != 4 and attendance != 2 and Q9 != 5 and Q13 != 3 | 3 | 0.000629 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 = 2 and Q19 = 5 | 13 | 0.000623 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 = 2 and Q26 = 2 | 3 | 0.000629 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 != 1 | 13 | 0.000623 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 = 2 | 13 | 0.000623 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 = 3 and Q18 != 4 | 13 | 0.000623 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance != 2 and difficulty = 1 | 3 | 0.000618 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty = 3 and Q25 != 3 and attendance != 1 | 3 | 0.000614 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 != 4 and Q25 != 4 and Q23 != 5 and attendance != 0 | 11 | 0.000627 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance = 0 and Q13 != 5 and Q2 != 3 | 11 | 0.000627 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty = 4 and Q12 = 4 and nb.repeat != 2 | 5 | 0.000600 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 = 5 | 5 | 0.000600 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 = 4 | 5 | 0.000600 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty != 5 and nb.repeat != 2 and difficulty = 3 | 8 | 0.000581 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance != 1 and attendance != 4 and Q4 != 4 and nb.repeat = 2 | 8 | 0.000581 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 = 2 and Q13 = 2 and difficulty = 3 | 9 | 0.000568 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance = 1 and Q27 = 5 and Q9 != 5 | 6 | 0.000589 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty != 5 and Q6 != 2 and Q22 != 1 and difficulty = 1 | 8 | 0.000540 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 = 1 | 9 | 0.000531 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 != 5 and Q22 = 4 and Q16 = 3 | 9 | 0.000531 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 = 2 and attendance != 1 | 8 | 0.000540 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 = 3 | 9 | 0.000531 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 = 5 | 9 | 0.000531 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 = 5 and difficulty != 1 and difficulty = 3 | 13 | 0.000550 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance = 0 and Q13 != 3 | 5 | 0.000549 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 = 1 and Q18 != 1 | 5 | 0.000540 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance = 1 and Q7 != 4 | 8 | 0.000525 |
| instr = 1 and nb.repeat != 3 and difficulty != 4 and difficulty = 5 and Q21 != 4 and Q27 = 5 | 10 | 0.000400 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 = 2 | 8 | 0.000525 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 != 5 and Q20 != 5 and Q12 != 2 and Q4 = 4 and Q8 != 4 | 8 | 0.000525 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 = 2 | 8 | 0.000525 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance = 2 and difficulty != 4 | 9 | 0.000510 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 != 2 and attendance != 0 and Q1 != 2 and Q16 = 3 and nb.repeat = 1 and attendance != 2 and Q1 != 3 | 1 | 0.000505 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 = 5 | 5 | 0.000519 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 = 2 and Q26 != 2 | 4 | 0.000510 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance != 3 and Q15 != 4 and Q17 = 4 | 3 | 0.000516 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 != 4 and Q5 = 5 and Q1 != 5 | 13 | 0.000510 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 = 2 | 2 | 0.000491 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 = 2 | 1 | 0.000460 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 = 2 | 3 | 0.000473 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty = 4 and Q12 != 4 and Q1 = 2 | 9 | 0.000443 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 = 5 | 9 | 0.000443 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 != 5 and Q8 != 2 and Q1 != 2 and Q21 != 3 and difficulty != 4 | 3 | 0.000446 |
| instr = 1 and nb.repeat != 3 and difficulty = 4 and Q18 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and Q1 = 5 and attendance = 4 | 10 | 0.000369 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty != 5 and nb.repeat != 2 and difficulty != 3 and difficulty = 1 | 13 | 0.000431 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 = 3 | 3 | 0.000437 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance = 3 | 3 | 0.000437 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 = 2 and Q25 = 3 | 9 | 0.000409 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 = 5 | 9 | 0.000409 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 = 3 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 = 5 and Q23 != 3 and attendance = 0 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 = 1 and Q15 = 3 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 = 1 and Q2 != 2 | 3 | 0.000404 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 = 5 and Q14 != 4 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance = 2 and difficulty = 4 | 3 | 0.000404 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 = 4 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 != 4 and Q17 = 3 and attendance != 2 and difficulty != 1 and Q9 != 3 | 13 | 0.000399 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 = 3 | 9 | 0.000380 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 != 5 and Q8 != 2 and Q1 = 2 | 9 | 0.000378 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 != 5 and Q22 = 4 and Q16 != 3 and attendance != 3 and Q1 = 4 | 5 | 0.000386 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 = 2 and Q19 != 5 | 6 | 0.000408 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 = 5 and Q14 = 4 | 5 | 0.000384 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 = 2 | 8 | 0.000373 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 != 5 and Q22 = 4 and Q16 != 3 and attendance != 3 and Q1 != 4 | 8 | 0.000373 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 != 5 and Q8 = 2 | 8 | 0.000373 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty = 1 | 3 | 0.000379 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty = 1 and Q5 = 4 and Q25 = 4 and attendance != 0 | 1 | 0.000361 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 = 2 | 1 | 0.000361 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance = 1 | 5 | 0.000371 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 = 2 and Q7 = 2 | 1 | 0.000360 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty != 5 and Q6 != 2 and Q22 = 1 | 4 | 0.000354 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 = 1 | 11 | 0.000372 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 != 1 | 3 | 0.000363 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty = 2 and Q18 != 5 and Q25 != 5 and Q22 = 4 and Q16 != 3 and attendance = 3 | 13 | 0.000359 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 = 5 and difficulty = 1 | 3 | 0.000363 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance != 1 and attendance != 4 and Q4 != 4 and nb.repeat != 2 | 13 | 0.000359 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty != 5 and Q6 != 2 and Q22 != 1 and difficulty != 1 and Q9 = 3 | 4 | 0.000352 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 = 2 | 3 | 0.000363 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance != 3 and Q15 != 4 and Q17 != 4 and Q9 = 2 | 9 | 0.000340 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 != 4 and Q5 = 5 and Q1 = 5 and attendance = 0 and difficulty != 1 | 9 | 0.000340 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 = 2 | 9 | 0.000340 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 = 2 | 5 | 0.000346 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 = 1 and Q21 != 2 and Q2 != 4 and Q6 != 4 and Q22 != 2 and Q16 != 4 and difficulty = 5 and Q14 = 3 | 5 | 0.000346 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 = 2 | 8 | 0.000336 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 = 2 | 13 | 0.000326 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 != 2 and Q25 != 2 and Q23 != 2 and attendance = 3 | 9 | 0.000313 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance = 1 and Q7 = 4 | 9 | 0.000309 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance != 0 and difficulty = 3 and Q25 != 3 and attendance = 1 | 8 | 0.000309 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 = 1 and Q8 != 2 and Q21 = 3 | 3 | 0.000303 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 != 2 and difficulty != 5 and Q16 = 5 and difficulty != 1 and difficulty != 3 | 3 | 0.000303 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 = 3 and Q18 = 4 | 8 | 0.000280 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 != 2 and difficulty != 1 and attendance != 1 and attendance = 4 | 3 | 0.000280 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 = 2 | 4 | 0.000264 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty = 5 and Q8 = 2 and Q26 != 2 | 8 | 0.000259 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 != 2 and attendance != 2 and attendance = 0 and Q13 = 3 | 9 | 0.000243 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 = 1 and Q8 = 2 | 5 | 0.000247 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 != 2 and Q4 != 2 and Q1 = 2 | 5 | 0.000247 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 = 4 | 8 | 0.000240 |
| instr!=(3) and instr != 3 and difficulty != 5 | 10 | 0.020243 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty = 4 and Q12 = 4 and nb.repeat = 2 | 13 | 0.000224 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance = 2 | 3 | 0.000227 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 = 3 and Q22 = 4 | 9 | 0.000213 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 = 5 and Q4 != 4 and Q19 != 4 and Q7 != 3 and attendance != 1 and Q7 != 4 and Q5 != 5 | 5 | 0.000216 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance != 3 and difficulty != 4 and attendance != 4 and attendance = 0 and difficulty != 1 | 5 | 0.000216 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance = 3 and Q11 != 5 and Q8 != 2 and Q1 != 2 and Q21 != 3 and difficulty = 4 | 8 | 0.000210 |
| instr != 1 and instr = 2 and difficulty != 4 and difficulty != 5 and attendance != 1 and Q15 != 2 and Q23 != 2 and Q13 != 2 and Q11 != 2 and Q16 != 2 and Q24 != 2 and Q9 != 2 and Q3 != 2 and Q6 != 2 and difficulty != 1 and Q21 != 1 and Q2 != 1 and Q1 != 1 and difficulty != 2 and Q8 = 2 | 1 | 0.000202 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 = 1 | 13 | 0.000202 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty != 1 and Q20 != 2 and Q16 != 2 and Q17 != 5 and Q23 != 2 and Q26 != 2 and Q12 != 2 and Q5 != 2 and Q2 != 2 and Q8 = 2 | 5 | 0.000195 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty != 5 and Q21 != 3 and Q16 != 1 and Q22 != 3 and Q23 != 3 and Q3 != 3 and Q5 != 3 and difficulty != 4 and Q1 = 2 and attendance = 1 | 3 | 0.000186 |
| instr != 1 and instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 != 1 and Q10 != 1 and difficulty = 5 and Q2 = 2 | 4 | 0.000178 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 = 2 | 5 | 0.000177 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q8 != 2 and Q21 = 1 and Q2 = 1 and difficulty != 3 and attendance != 2 and attendance != 3 and difficulty = 4 | 3 | 0.000157 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 = 1 and Q9 = 5 | 3 | 0.000091 |
| instr != 1 and instr != 2 and nb.repeat = 1 and Q17 != 1 and difficulty != 2 and Q4 != 1 and Q5 != 1 and Q19 != 1 and Q11 != 1 and Q6 != 1 and attendance != 4 and Q26 != 1 and difficulty != 5 and Q20 != 5 and Q21 != 5 and Q22 != 5 and Q24 != 5 and Q3 != 5 and Q5 != 5 and Q11 != 5 and difficulty = 1 and Q27 = 2 and Q9 = 3 | 3 | 0.000091 |
| instr!=(3) and instr != 3 and difficulty != 4 | 10 | 0.019748 |
| instr = 1 and nb.repeat = 3 | 7 | 0.002726 |

## Ordered rules

### PART

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and nb.repeat = 3 and Q1 != 3 | 7 | 0.001002 |
| instr = 1 and nb.repeat = 3 | 7 | 0.001198 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 != 1 and Q8 != 5 and Q11 != 5 and nb.repeat = 1 and Q6 = 2 and Q1 = 2 and difficulty = 3 | 10 | 0.001333 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q16 != 1 and Q8 != 5 and Q11 != 5 and nb.repeat = 1 and Q26 != 2 and difficulty = 1 and Q27 != 3 | 10 | 0.006010 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q4 != 1 and difficulty = 1 and Q9 != 2 and Q1 != 3 | 10 | 0.003817 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q21 != 5 and Q16 != 1 and Q8 != 5 and Q11 != 5 and nb.repeat = 1 and Q1 != 2 and Q26 != 2 and difficulty != 1 and attendance != 4 and Q22 != 3 and Q9 = 4 and attendance != 1 and attendance != 2 | 10 | 0.005246 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q13 != 5 and Q8 != 5 and Q16 != 1 and difficulty = 1 and Q7 = 3 | 10 | 0.002924 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q13 = 5 and Q21 = 5 and Q4 = 5 and attendance = 3 | 10 | 0.002971 |
| instr = 1 and difficulty = 2 and Q5 != 5 and Q11 != 4 and Q3 != 2 | 10 | 0.004360 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q21 != 5 and Q16 != 1 and Q2 != 2 and Q26 != 2 and Q8 != 5 and Q1 = 4 and attendance = 2 | 10 | 0.003543 |
| instr = 1 and difficulty != 4 and difficulty != 5 and Q2 = 2 | 10 | 0.002536 |
| instr = 1 and difficulty = 3 and Q20 = 1 | 10 | 0.001468 |
| instr = 1 and difficulty = 3 and Q25 != 5 and Q13 != 5 and attendance != 4 and Q1 = 3 and attendance != 2 and attendance = 3 | 10 | 0.001666 |
| instr = 1 and difficulty = 3 and Q25 != 5 and Q13 != 5 and attendance = 4 | 10 | 0.001764 |
| instr = 1 and difficulty = 3 and Q12 = 3 and attendance = 1 | 10 | 0.001302 |
| instr = 1 and difficulty = 3 and Q12 != 3 and Q25 = 4 and attendance = 1 | 10 | 0.002129 |
| instr = 1 and difficulty = 3 and Q12 != 3 and Q25 != 4 and Q13 != 4 and attendance != 4 and Q2 != 4 | 2 | 0.002074 |
| instr = 1 and difficulty = 3 and Q14 = 3 | 10 | 0.000939 |
| instr = 1 and difficulty = 3 and Q3 = 4 and Q12 = 4 | 10 | 0.000328 |
| instr = 1 and difficulty = 3 and Q25 != 4 and Q9 = 5 | 10 | 0.002418 |
| instr = 1 and difficulty = 3 and Q25 = 4 | 10 | 0.000629 |
| instr = 1 and difficulty = 1 and attendance = 0 | 10 | 0.002324 |
| instr = 1 and difficulty != 1 and Q1 = 5 and attendance = 3 | 2 | 0.001309 |
| instr = 1 and difficulty != 1 and difficulty = 2 and Q17 != 4 | 2 | 0.000629 |
| instr = 1 and difficulty != 1 and difficulty != 2 and nb.repeat = 1 and Q25 = 2 | 10 | 0.000851 |
| instr = 1 and difficulty != 1 and Q27 = 2 | 7 | 0.002175 |
| instr = 1 and difficulty != 1 and difficulty != 2 and nb.repeat != 1 | 7 | 0.000784 |
| instr = 1 and difficulty != 1 and Q1 = 2 and Q8 != 3 | 7 | 0.000925 |
| instr = 1 and difficulty != 1 and Q5 != 2 and Q6 = 1 and difficulty != 4 | 7 | 0.003463 |
| instr = 1 and Q5 != 2 and difficulty != 1 and Q6 != 2 and Q12 != 2 and Q3 != 3 and Q21 != 3 and Q16 = 4 and attendance = 3 | 2 | 0.001169 |
| instr = 1 and Q5 != 2 and difficulty != 1 and Q8 = 4 and Q21 = 4 and attendance != 1 | 10 | 0.002641 |
| instr = 1 and difficulty != 1 and Q5 != 2 and Q9 = 4 and attendance != 1 | 10 | 0.000628 |
| instr = 1 and difficulty != 1 and Q5 != 2 and Q15 = 4 and Q6 = 4 | 7 | 0.002201 |
| instr = 1 and difficulty != 1 and Q5 != 2 and Q5 != 4 and Q1 = 5 | 2 | 0.000796 |
| instr = 1 and difficulty != 1 and Q17 != 5 and Q15 != 4 and attendance != 4 and Q9 = 3 and difficulty != 5 | 2 | 0.001827 |
| instr = 1 and Q20 != 4 and difficulty != 1 and Q17 != 5 and attendance != 3 and Q1 = 3 | 7 | 0.002110 |
| instr = 1 and Q20 != 4 and difficulty != 1 and Q17 = 5 | 7 | 0.002093 |
| instr = 1 and Q20 != 4 and attendance != 3 | 10 | 0.004558 |
| instr = 1 and Q20 != 4 | 2 | 0.003453 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 != 1 and nb.repeat != 2 and Q11 = 2 | 11 | 0.002035 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 != 1 and nb.repeat = 2 | 11 | 0.001817 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 != 1 and Q7 != 2 and Q13 != 5 and attendance = 0 | 11 | 0.001848 |
| instr != 1 and instr = 2 and difficulty = 4 and Q17 = 1 | 6 | 0.002050 |
| instr != 1 and instr = 2 and difficulty = 4 and Q7 = 2 | 11 | 0.001720 |
| instr != 1 and instr = 2 and difficulty = 4 and Q13 != 5 and Q1 != 2 and attendance != 2 and Q4 != 3 and Q18 = 4 and attendance = 3 | 11 | 0.001626 |
| instr != 1 and instr = 2 and difficulty = 4 and Q13 != 5 and Q1 != 2 and Q28 != 4 and Q2 != 4 and Q15 = 3 and attendance != 3 and attendance = 1 | 11 | 0.001418 |
| instr != 1 and instr = 2 and difficulty = 4 and attendance = 1 | 11 | 0.001008 |
| instr != 1 and instr = 2 and difficulty = 5 and Q19 != 5 and Q14 != 2 and attendance != 0 and Q14 = 3 | 11 | 0.001389 |
| instr != 1 and instr = 2 and difficulty = 4 and attendance != 3 and attendance = 2 and Q6 != 4 | 11 | 0.001102 |
| instr != 1 and instr = 2 and difficulty = 5 and Q27 != 2 and Q19 != 5 and attendance != 0 and Q25 = 4 | 1 | 0.000534 |
| instr != 1 and instr = 2 and difficulty = 5 and nb.repeat = 1 and Q13 != 1 and Q21 != 5 | 11 | 0.001436 |
| instr != 1 and instr = 2 and difficulty = 5 and nb.repeat = 1 and Q1 != 1 | 11 | 0.000554 |
| instr != 1 and instr = 2 and difficulty = 4 and attendance = 4 and Q12 = 4 | 11 | 0.001104 |
| instr != 1 and instr = 2 and difficulty = 4 and Q9 = 4 and attendance != 3 | 6 | 0.000590 |
| instr != 1 and instr = 2 and attendance = 1 and Q27 = 5 and Q9 = 5 | 11 | 0.000775 |
| instr != 1 and instr = 2 and attendance = 1 and Q14 != 5 and Q12 = 2 and Q10 = 2 | 6 | 0.000775 |
| instr != 1 and instr = 2 and attendance = 1 and Q14 != 5 and Q4 != 2 and Q8 != 2 and difficulty != 1 and difficulty != 2 and nb.repeat != 2 and Q6 != 1 and Q6 != 3 and Q1 = 4 | 6 | 0.002088 |
| instr != 1 and instr = 2 and Q28 = 2 and Q20 != 3 and nb.repeat = 1 and attendance != 0 and Q14 = 2 | 6 | 0.002020 |
| instr != 1 and instr = 2 and difficulty = 2 and Q22 != 2 and Q7 != 2 and Q4 != 5 and Q1 != 2 and Q23 != 5 and Q17 != 5 and attendance != 4 and attendance != 3 and Q27 != 1 and Q10 != 3 and attendance != 1 | 6 | 0.002138 |
| instr != 1 and instr = 2 and difficulty = 4 and Q9 != 4 and Q13 != 4 and attendance != 3 and Q2 != 5 | 11 | 0.000295 |
| instr != 1 and instr = 2 and attendance = 1 and Q18 != 5 and Q6 != 2 and difficulty != 2 and nb.repeat != 2 and Q3 != 4 and Q3 != 1 | 6 | 0.004164 |
| instr = 1 | 7 | 0.004165 |
| instr = 2 and difficulty = 2 and Q20 = 2 | 1 | 0.000985 |
| instr = 2 and nb.repeat = 2 and Q9 != 2 and attendance != 2 and Q13 != 4 and difficulty = 3 and Q7 = 3 | 6 | 0.000768 |
| instr = 2 and Q21 = 2 and attendance != 3 and difficulty = 1 and Q8 = 2 | 6 | 0.000401 |
| instr = 2 and Q21 = 2 and Q18 = 2 and difficulty = 3 | 6 | 0.000659 |
| instr = 2 and Q21 = 2 and Q16 != 2 | 6 | 0.000896 |
| instr = 2 and Q21 != 2 and Q28 = 2 | 6 | 0.001820 |
| instr = 2 and Q21 != 2 and Q26 = 2 | 11 | 0.001130 |
| instr = 2 and Q21 != 2 and Q23 != 2 and Q24 != 2 and Q9 = 2 and Q21 != 4 | 1 | 0.000641 |
| instr = 2 and Q21 != 2 and Q23 != 2 and Q9 != 2 and difficulty = 2 and attendance != 0 and Q4 != 5 and Q1 != 2 and Q2 != 3 and Q4 != 3 and Q4 != 1 and attendance != 3 | 6 | 0.000866 |
| instr = 2 and Q21 != 2 and Q23 != 2 and Q9 != 2 and difficulty = 2 and attendance = 0 | 1 | 0.000841 |
| instr = 2 and Q21 != 2 and Q23 != 2 and Q9 = 2 | 6 | 0.001612 |
| instr = 2 and Q21 != 2 and Q23 != 2 and difficulty = 2 and Q26 != 5 and Q1 != 2 and Q13 != 3 and Q7 != 4 and Q4 != 3 | 6 | 0.001608 |
| instr = 2 and Q21 != 2 and Q23 != 2 and Q24 != 2 and Q10 != 2 and Q27 = 2 | 6 | 0.001288 |
| instr = 2 and Q21 != 2 and Q13 != 2 and Q23 != 2 and Q24 != 2 and Q10 != 2 and Q12 != 2 and Q22 = 4 and Q18 != 5 and Q17 = 4 and Q16 = 4 and Q27 = 4 and difficulty != 2 and Q12 != 4 and Q8 = 3 | 6 | 0.001483 |
| instr = 2 and Q21 = 2 | 6 | 0.000867 |
| instr = 2 and Q13 = 2 | 11 | 0.002258 |
| instr = 2 and Q23 = 2 | 13 | 0.000570 |
| instr = 2 and Q12 = 2 and Q25 = 4 | 11 | 0.000487 |
| instr = 2 and Q12 != 2 and Q7 = 2 and Q15 = 4 | 11 | 0.001484 |
| instr = 2 and Q12 != 2 and Q4 = 2 and Q10 != 4 | 1 | 0.001346 |
| instr = 2 and Q12 != 2 and difficulty = 2 and Q13 = 4 and attendance != 3 | 6 | 0.001764 |
| instr = 2 and Q12 != 2 and difficulty = 3 and Q6 != 2 and Q8 != 2 and attendance = 0 and Q13 != 5 and Q13 = 3 | 6 | 0.001738 |
| instr = 2 and Q12 != 2 and Q23 = 4 and Q16 != 3 and Q15 != 5 and nb.repeat = 1 and Q1 != 2 and Q6 = 4 and difficulty != 1 and Q1 = 4 and attendance != 4 and attendance != 2 | 6 | 0.001809 |
| instr = 2 and Q12 != 2 and difficulty != 2 and difficulty != 1 and Q6 != 2 and Q24 = 4 and Q16 != 5 and Q7 = 4 and attendance != 1 and Q2 = 4 and attendance != 3 and attendance != 4 | 6 | 0.000835 |
| instr = 2 and Q12 != 2 and nb.repeat = 2 and Q6 != 4 and Q12 != 3 and Q20 = 1 | 6 | 0.001065 |
| instr = 2 and Q12 != 2 and difficulty != 5 and difficulty != 2 and difficulty != 1 and Q6 != 2 and attendance = 0 and Q28 = 5 | 6 | 0.001534 |
| instr = 2 and Q12 != 2 and difficulty != 5 and Q3 != 2 and Q2 != 2 and Q12 != 3 and Q11 != 3 and Q3 != 3 and nb.repeat != 1 | 6 | 0.000707 |
| instr = 2 and Q12 != 2 and nb.repeat = 2 | 11 | 0.002760 |
| instr = 2 and Q12 != 2 and Q3 = 2 | 6 | 0.000498 |
| instr = 2 and Q12 != 2 and attendance = 2 and Q11 != 3 and difficulty = 3 and Q1 != 4 and Q6 != 5 | 11 | 0.000677 |
| instr = 2 and Q12 != 2 and attendance = 2 and Q11 != 3 and Q16 = 5 | 6 | 0.003691 |
| instr = 2 and Q12 != 2 and Q23 = 4 and Q21 = 4 and Q26 = 4 and Q7 = 4 and Q4 = 4 and difficulty != 3 and attendance = 0 | 6 | 0.001223 |
| instr = 2 and Q12 = 2 | 11 | 0.000528 |
| instr = 2 and Q12 != 3 and Q8 = 3 and Q5 = 3 | 1 | 0.000932 |
| instr = 2 and Q12 != 3 and Q27 != 3 and difficulty != 2 and attendance != 1 and Q23 = 4 and Q6 = 4 and difficulty != 1 | 6 | 0.000550 |
| instr = 2 and Q21 = 3 and Q24 = 3 and Q6 = 3 and difficulty != 1 and Q1 = 3 and attendance != 4 and attendance = 2 | 11 | 0.000744 |
| instr = 2 and difficulty = 5 | 11 | 0.000204 |
| instr = 2 and Q1 != 2 and Q23 = 4 and Q6 != 4 and Q8 = 4 | 6 | 0.000471 |
| instr = 2 and Q1 != 2 and Q8 != 2 and Q23 = 4 and difficulty = 1 | 1 | 0.001084 |
| instr = 2 and Q23 = 4 and Q9 = 4 | 1 | 0.006443 |
| instr = 2 and Q23 != 4 and Q13 = 4 and difficulty != 3 | 6 | 0.000824 |
| instr = 2 and Q23 != 4 and Q19 != 4 and Q15 != 4 and Q6 = 4 | 1 | 0.000873 |
| instr = 2 and Q23 != 4 and Q19 != 4 and Q15 != 4 and Q11 != 4 and attendance != 2 and difficulty != 2 and attendance = 3 and Q2 = 3 and difficulty = 3 | 6 | 0.001502 |
| instr = 2 and Q23 != 4 and Q19 = 4 | 11 | 0.000890 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance != 2 and attendance = 3 and Q5 != 5 and difficulty = 4 | 11 | 0.000528 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance != 2 and attendance = 3 and Q5 = 5 and difficulty != 3 | 6 | 0.000829 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance = 3 and Q5 = 5 | 6 | 0.000339 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance != 3 and attendance != 2 and difficulty = 3 and Q4 != 3 and Q27 = 5 | 1 | 0.001584 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance = 3 | 11 | 0.003088 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance != 2 and difficulty = 3 and Q2 != 1 | 6 | 0.001285 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and attendance != 2 and difficulty != 3 and attendance != 4 and difficulty = 1 and Q27 != 5 and Q18 != 3 | 6 | 0.001200 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and Q27 != 1 and attendance != 4 and Q27 != 5 and Q1 = 3 and attendance = 0 | 11 | 0.001447 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and Q27 = 1 | 1 | 0.002983 |
| instr = 2 and Q23 != 4 and Q15 != 4 and Q11 != 4 and Q7 = 3 and attendance != 1 | 11 | 0.000401 |
| instr = 2 and Q23 != 4 and Q4 != 4 and Q4 != 1 and attendance != 4 and Q1 != 3 | 1 | 0.005702 |
| instr = 2 and Q24 != 4 and Q4 != 4 and Q1 = 5 | 6 | 0.002119 |
| instr = 2 and Q24 != 4 and Q24 = 3 | 6 | 0.007476 |
| instr = 2 and Q24 != 4 | 13 | 0.006922 |
| instr != 2 and nb.repeat != 1 and attendance != 3 and Q11 = 1 and difficulty = 5 and attendance != 0 | 13 | 0.000737 |
| instr != 2 and nb.repeat != 1 and Q11 = 1 and difficulty != 5 and difficulty != 4 and nb.repeat != 2 and attendance = 0 | 9 | 0.001187 |
| instr != 2 and difficulty = 2 and Q11 = 2 and Q22 = 2 and nb.repeat != 2 | 5 | 0.001053 |
| instr != 2 and difficulty = 2 and Q11 = 2 and Q22 != 2 | 13 | 0.003191 |
| instr != 2 and difficulty = 2 and Q9 = 2 and Q3 = 2 | 13 | 0.001871 |
| instr != 2 and difficulty = 2 and Q12 = 2 and Q10 != 3 | 8 | 0.001705 |
| instr != 2 and nb.repeat != 1 and Q11 = 1 and difficulty = 4 | 13 | 0.002229 |
| instr != 2 and difficulty = 2 and Q12 != 2 and Q19 != 4 and Q15 != 4 and nb.repeat = 3 | 9 | 0.001040 |
| instr != 2 and nb.repeat != 1 and Q11 = 1 and Q15 = 1 and attendance != 1 and difficulty != 1 | 13 | 0.001078 |
| instr != 2 and nb.repeat != 1 and Q14 = 1 and Q4 = 1 and attendance = 1 | 13 | 0.001147 |
| instr != 2 and nb.repeat != 1 and Q14 = 1 and Q4 = 1 | 3 | 0.001641 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q10 = 5 and attendance != 4 and attendance != 2 and difficulty != 2 and attendance != 0 | 8 | 0.001364 |
| instr != 2 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q18 != 2 and Q16 = 1 and Q8 != 2 and Q8 = 1 and Q1 = 1 and attendance = 4 and difficulty = 5 | 13 | 0.000652 |
| instr != 2 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q18 != 2 and Q16 = 1 and Q8 != 2 and attendance = 4 | 13 | 0.001169 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q8 != 1 and Q4 = 5 and attendance != 4 and difficulty != 2 and difficulty = 3 | 8 | 0.000678 |
| instr != 2 and difficulty = 2 and Q12 != 2 and Q17 != 1 and Q19 != 4 and Q15 != 4 and Q7 != 3 and Q3 = 5 | 13 | 0.001089 |
| instr != 2 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q18 != 2 and Q16 = 1 and Q8 != 2 and Q8 = 1 and Q1 = 1 and attendance = 2 | 13 | 0.001109 |
| instr != 2 and difficulty = 2 and Q12 != 2 and nb.repeat != 3 and Q17 != 1 and Q2 != 2 and Q28 = 3 and nb.repeat = 1 and attendance != 1 | 13 | 0.003247 |
| instr != 2 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q18 != 2 and Q16 = 1 and Q8 != 2 and Q8 = 1 and Q1 = 1 and attendance = 1 and difficulty = 5 | 3 | 0.001370 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q10 = 5 and nb.repeat = 2 | 13 | 0.001757 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q10 = 5 and attendance = 4 | 13 | 0.001112 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q4 = 5 | 8 | 0.000465 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q12 != 1 and Q8 != 1 and Q1 = 2 and Q5 != 4 and Q8 = 2 and nb.repeat = 2 and Q14 = 2 | 3 | 0.001208 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q12 != 1 and Q8 != 1 and Q1 = 2 and Q5 != 4 and attendance != 0 and Q8 = 2 | 8 | 0.001283 |
| instr != 2 and Q17 = 1 and Q9 != 5 and Q19 != 3 and difficulty != 2 and Q16 = 1 and Q13 = 1 and Q6 != 2 and Q1 != 3 and Q8 = 1 and attendance != 1 and difficulty != 4 and difficulty != 3 and attendance = 0 and difficulty = 1 | 3 | 0.008300 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q12 != 1 and Q8 != 1 and attendance = 3 and Q12 != 4 and difficulty != 3 | 9 | 0.001288 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q12 != 1 and Q8 != 1 and Q25 != 4 and attendance != 3 and Q18 != 4 and Q12 != 4 and Q1 != 1 and Q26 != 2 and Q2 != 2 and difficulty = 1 | 13 | 0.001086 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q12 != 1 and Q8 != 1 and Q25 != 4 and attendance != 3 and Q18 != 4 and Q12 != 4 and Q1 = 1 | 13 | 0.001317 |
| instr != 2 and difficulty = 2 and Q17 != 1 and Q26 != 5 and Q12 != 2 and Q28 != 3 and Q5 != 3 and Q23 = 4 and attendance != 0 and attendance != 3 | 5 | 0.000655 |
| instr != 2 and difficulty = 2 and Q17 != 1 and Q26 != 5 and Q12 != 2 and Q28 != 3 and Q5 != 3 and Q18 != 4 | 9 | 0.001240 |
| instr != 2 and difficulty = 2 and Q12 = 2 | 8 | 0.000360 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q8 != 1 and Q26 = 2 | 8 | 0.000238 |
| instr != 2 and difficulty = 2 and Q12 = 1 | 13 | 0.001539 |
| instr != 2 and nb.repeat != 1 and Q14 != 1 and Q11 != 1 and Q11 != 5 and Q8 != 1 and Q20 != 2 and Q6 != 2 and Q25 != 4 and attendance != 3 and Q10 = 4 | 3 | 0.000408 |
| instr != 2 and nb.repeat = 2 and Q19 != 1 and Q7 != 1 and Q20 != 5 and Q8 != 2 and attendance != 3 and attendance = 0 and Q1 != 4 and difficulty != 3 | 13 | 0.001061 |
| instr != 2 and nb.repeat = 2 and Q19 != 1 and Q1 = 1 | 9 | 0.001611 |
| instr != 2 and nb.repeat = 2 and Q19 != 1 and Q23 != 2 and Q1 = 2 | 9 | 0.002328 |
| instr != 2 and Q6 != 1 and Q5 = 1 and Q21 != 1 and Q11 = 1 | 3 | 0.001235 |
| instr != 2 and attendance = 4 and nb.repeat != 2 and Q4 = 1 and Q20 != 1 and Q21 != 3 | 8 | 0.002118 |
| instr != 2 and Q6 != 1 and Q5 = 1 and Q28 != 2 and Q20 != 1 and Q2 != 2 and Q20 != 3 | 8 | 0.001641 |
| instr != 2 and nb.repeat != 1 and Q10 != 1 and Q19 != 1 and Q27 != 2 and Q2 != 4 and Q19 != 4 and difficulty = 5 | 13 | 0.001386 |
| instr != 2 and Q6 != 1 and Q11 = 1 and Q23 != 4 and difficulty != 1 and Q19 != 2 and Q28 != 3 and Q17 != 5 and Q6 != 2 | 5 | 0.001600 |
| instr != 2 and nb.repeat = 2 and Q19 != 1 and Q23 != 2 and attendance != 3 and difficulty != 4 and attendance = 1 and Q12 != 3 | 8 | 0.000753 |
| instr != 2 and Q6 != 1 and Q17 = 1 and Q2 != 1 and Q6 != 2 | 13 | 0.001193 |
| instr != 2 and Q6 != 1 and Q17 = 1 and Q1 != 1 | 5 | 0.001026 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q5 = 1 and Q22 != 2 and Q11 != 3 | 8 | 0.001607 |
| instr != 2 and nb.repeat = 2 and difficulty != 5 and Q23 != 2 and attendance != 3 and difficulty != 4 and attendance = 1 | 9 | 0.001626 |
| instr != 2 and difficulty = 5 and Q2 != 2 and Q9 != 2 and Q24 != 2 and Q19 != 2 and Q12 != 2 and attendance != 0 and Q1 != 4 and Q18 != 1 and Q4 != 4 and attendance = 1 | 3 | 0.001187 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q21 = 1 and Q24 != 1 | 5 | 0.000913 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 = 1 and Q28 != 3 and Q1 != 2 and Q5 != 2 | 5 | 0.001038 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 = 1 and Q28 != 3 and Q1 = 2 | 3 | 0.001924 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 = 1 and Q28 = 3 | 13 | 0.001217 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 != 1 and Q23 = 1 and Q1 != 1 | 9 | 0.001189 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 != 1 and Q23 != 1 and Q4 = 1 and Q21 != 2 and Q24 = 3 | 9 | 0.001189 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 != 1 and Q23 != 1 and nb.repeat = 2 and Q23 != 2 and attendance != 3 and difficulty != 4 and attendance != 0 | 3 | 0.001419 |
| instr != 2 and Q6 != 1 and Q17 != 1 and Q11 = 1 | 5 | 0.003220 |
| instr != 2 and Q4 != 1 and Q21 = 1 | 13 | 0.001315 |
| instr != 2 and nb.repeat = 2 and Q23 != 2 and difficulty != 4 and Q13 = 3 | 3 | 0.001586 |
| instr != 2 and Q4 != 1 and Q23 = 1 and Q27 = 1 | 3 | 0.001227 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and nb.repeat != 3 and Q15 = 2 and Q1 = 2 | 5 | 0.001067 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and Q15 != 2 and Q23 != 2 and Q9 != 2 and Q1 = 2 and Q12 != 3 | 8 | 0.002281 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and Q6 = 1 and Q8 != 1 and Q10 = 3 | 13 | 0.001348 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and difficulty = 5 and Q2 != 2 and Q9 != 2 and attendance = 0 | 3 | 0.001769 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and difficulty = 5 and Q2 != 2 and Q9 != 2 and Q24 != 4 and attendance != 3 and attendance != 1 and Q12 != 3 | 3 | 0.002666 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and difficulty = 5 and Q8 != 2 and Q2 != 2 and Q25 = 3 and attendance != 3 and attendance = 4 | 3 | 0.001545 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and Q15 != 2 and Q1 = 2 and Q5 = 2 | 8 | 0.000486 |
| instr != 2 and Q4 != 1 and Q23 != 1 and Q27 = 1 and Q28 != 4 and Q23 != 2 | 8 | 0.001262 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and Q1 != 2 and Q15 != 2 and Q2 != 2 and Q12 != 2 and Q20 != 5 and Q4 = 4 and Q23 = 4 and Q12 != 3 and difficulty != 4 and difficulty = 3 | 3 | 0.000781 |
| instr != 2 and Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and Q1 != 2 and Q15 != 2 and Q2 != 2 and Q8 != 2 and Q20 != 5 and difficulty != 5 and Q4 = 4 and Q8 = 4 and difficulty = 4 | 3 | 0.000992 |
| instr != 2 and attendance = 4 and Q1 != 2 and Q27 != 1 and Q21 != 2 and Q27 != 2 and Q12 != 2 and difficulty = 1 and Q19 != 5 | 3 | 0.001553 |
| instr != 2 and attendance = 4 and Q1 != 2 and difficulty = 1 | 3 | 0.000810 |
| instr != 2 and attendance = 4 and Q1 != 2 and Q2 != 2 and Q23 != 2 and Q8 != 2 and Q17 != 5 and Q1 != 1 and difficulty != 5 and Q23 = 4 | 8 | 0.001775 |
| instr != 2 and attendance = 4 and Q1 != 2 and Q1 = 4 and Q20 = 4 | 5 | 0.003559 |
| instr != 2 and attendance = 4 and Q1 != 2 and Q12 != 4 and Q23 != 4 and Q10 != 2 and Q14 != 4 and difficulty != 3 and Q3 = 3 | 3 | 0.000303 |
| instr != 2 and attendance = 4 and Q1 != 2 and Q12 = 4 | 8 | 0.000883 |
| instr = 2 | 11 | 0.029229 |
| attendance = 4 and Q1 = 2 | 8 | 0.001073 |
| attendance = 4 and Q25 = 4 and difficulty = 3 | 8 | 0.000469 |
| Q4 != 1 and Q23 != 1 and difficulty != 2 and attendance = 4 and Q5 != 4 and Q15 != 3 and difficulty = 3 | 13 | 0.001454 |
| Q4 != 1 and Q23 != 1 and difficulty != 2 and Q8 = 1 and Q19 != 3 and Q16 != 2 | 5 | 0.001153 |
| Q4 != 1 and Q23 != 1 and difficulty != 2 and nb.repeat != 2 and nb.repeat != 1 and Q4 = 4 | 3 | 0.000933 |
| nb.repeat = 3 and Q11 != 3 | 13 | 0.003178 |
| nb.repeat = 3 and attendance != 0 and difficulty != 4 | 9 | 0.002606 |
| difficulty = 2 and Q20 != 4 and attendance = 1 | 13 | 0.003088 |
| Q4 != 1 and Q23 != 1 and Q26 = 1 | 3 | 0.000635 |
| Q4 != 1 and Q23 != 1 and nb.repeat = 3 and attendance = 0 | 9 | 0.002171 |
| difficulty = 2 and attendance = 3 | 13 | 0.002075 |
| difficulty = 2 | 9 | 0.001762 |
| Q4 != 1 and Q23 != 1 and Q8 = 1 | 9 | 0.001835 |
| Q4 != 1 and Q23 != 1 and difficulty = 5 and Q1 != 1 and Q21 = 2 | 3 | 0.001279 |
| difficulty = 5 and Q27 != 5 and Q16 != 3 and Q1 != 3 and Q20 != 3 and Q26 != 3 and Q22 != 1 and Q24 != 4 | 3 | 0.001288 |
| Q6 != 1 and Q23 != 1 and Q3 = 1 | 3 | 0.000918 |
| Q6 != 1 and Q23 != 1 and Q4 = 1 and Q3 != 2 | 8 | 0.001950 |
| Q4 != 1 and Q2 = 1 and Q18 != 3 | 8 | 0.000915 |
| Q4 != 1 and Q2 != 1 and Q18 = 1 | 3 | 0.002002 |
| Q4 != 1 and Q2 != 1 and difficulty = 5 and Q8 != 2 and Q2 != 2 and Q14 != 3 and Q25 != 5 and Q1 != 4 | 3 | 0.002370 |
| Q4 != 1 and Q2 != 1 and difficulty = 5 and Q8 != 2 and Q2 != 2 and Q22 != 4 and attendance = 3 and Q1 = 3 | 5 | 0.001208 |
| Q4 != 1 and Q2 != 1 and difficulty = 5 and Q8 != 2 and Q2 != 2 and Q8 != 4 and attendance != 3 | 3 | 0.000997 |
| Q4 = 1 and Q3 != 3 and Q11 != 5 and Q9 != 4 and Q9 = 3 | 5 | 0.000893 |
| Q4 = 1 and Q3 != 3 and Q11 != 5 and Q9 != 4 and Q17 != 3 and Q3 = 1 and attendance != 0 and difficulty != 3 and attendance = 1 | 3 | 0.001364 |
| Q4 = 1 and Q3 != 3 and Q11 != 5 and Q1 = 1 and Q3 != 1 | 13 | 0.001377 |
| Q4 = 1 and Q3 != 3 and Q11 != 5 and Q1 = 1 and Q12 = 1 and difficulty = 1 and Q13 != 1 | 13 | 0.001305 |
| Q4 != 1 and Q2 != 1 and Q28 = 2 and Q20 != 2 and Q14 != 2 | 5 | 0.002613 |
| Q28 = 2 and Q6 != 1 and difficulty != 3 and Q17 != 3 and Q9 != 3 and difficulty != 4 and Q1 != 2 and Q1 != 1 | 5 | 0.001771 |
| Q28 = 2 and Q6 != 1 and difficulty != 3 and Q17 != 3 and Q9 != 3 and difficulty != 4 and Q1 != 1 | 3 | 0.004442 |
| Q4 != 1 and Q2 != 1 and Q28 = 2 and attendance != 1 and Q13 = 2 and Q8 != 3 and attendance != 3 and Q1 != 1 | 13 | 0.002095 |
| Q4 != 1 and Q2 != 1 and Q28 = 2 and attendance != 1 and attendance != 3 and Q1 = 1 | 3 | 0.002103 |
| Q28 = 2 and Q1 != 1 and Q17 != 3 and difficulty != 3 and Q9 != 3 | 3 | 0.000676 |
| Q15 != 2 and Q2 != 2 and Q18 = 2 and Q2 != 3 | 3 | 0.001568 |
| Q28 = 2 and Q1 = 1 | 13 | 0.001739 |
| Q28 = 2 and Q17 = 2 and Q9 = 2 | 3 | 0.000846 |
| Q15 != 2 and Q17 = 2 and Q12 != 3 | 13 | 0.002466 |
| Q19 = 2 and Q7 = 3 and Q10 != 2 | 3 | 0.000997 |
| Q19 = 2 and Q7 != 3 and Q2 != 2 | 5 | 0.002928 |
| Q19 = 2 and Q7 != 3 | 9 | 0.003910 |
| Q19 != 2 and Q24 = 2 and Q20 = 4 | 5 | 0.001398 |
| Q19 = 2 | 9 | 0.000601 |
| Q2 != 2 and Q21 = 2 and Q14 = 3 | 5 | 0.001217 |
| Q18 != 2 and Q8 != 2 and Q13 != 2 and Q14 != 2 and Q23 != 2 and Q10 != 2 and Q12 = 2 and Q6 != 3 | 5 | 0.001522 |
| Q2 != 2 and Q21 != 2 and Q5 = 2 and Q4 != 2 and Q10 = 3 | 8 | 0.002493 |
| Q2 != 2 and Q21 != 2 and Q16 != 2 and Q25 != 2 and Q9 = 2 and Q16 != 3 | 5 | 0.000768 |
| Q2 != 2 and Q21 = 2 | 3 | 0.001770 |
| Q18 != 2 and Q16 != 2 and Q25 != 2 and Q23 = 2 | 3 | 0.001223 |
| Q21 != 2 and Q26 = 2 | 9 | 0.000702 |
| Q21 != 2 and Q18 = 2 and Q28 = 4 | 4 | 0.000303 |
| Q21 != 2 and Q18 != 2 and Q8 != 2 and Q10 != 2 and Q11 != 2 and Q27 != 2 and nb.repeat != 3 and Q7 != 2 and Q3 = 2 | 5 | 0.001560 |
| Q21 != 2 and Q18 != 2 and Q3 = 2 and Q4 = 2 and Q24 = 3 | 3 | 0.000779 |
| Q21 != 2 and Q18 = 2 | 9 | 0.001681 |
| Q21 != 2 and Q3 = 2 and Q4 != 2 | 4 | 0.001857 |
| Q21 != 2 and Q3 != 2 and Q16 != 2 and nb.repeat != 3 and Q5 != 2 and Q9 != 2 and Q2 = 2 and Q25 != 5 | 8 | 0.001801 |
| Q21 != 2 and Q3 != 2 and Q16 != 2 and nb.repeat != 3 and Q5 != 2 and Q9 != 2 and Q2 != 2 and Q11 != 2 and Q27 != 2 and Q8 != 2 and Q4 = 2 | 3 | 0.000564 |
| Q21 != 2 and Q3 != 2 and Q16 != 2 and nb.repeat != 3 and Q5 = 2 | 9 | 0.001385 |
| Q21 != 2 and Q5 != 2 and nb.repeat != 3 and Q7 != 2 and Q4 != 2 and Q12 != 2 and Q8 != 2 and Q27 != 2 and nb.repeat = 1 and Q1 = 2 and Q6 != 3 | 9 | 0.001296 |
| Q21 != 2 and Q5 != 2 and nb.repeat != 3 and Q7 = 2 and Q24 = 4 | 8 | 0.001431 |
| Q21 != 2 and Q5 != 2 and Q7 != 2 and Q4 != 2 and nb.repeat != 3 and Q12 != 2 and Q8 != 2 and Q1 != 2 and Q27 != 2 and nb.repeat = 1 and difficulty = 5 and Q21 != 4 and Q14 = 1 | 3 | 0.002546 |
| Q21 != 2 and Q5 != 2 and Q7 != 2 and Q4 != 2 and difficulty = 5 and Q7 = 4 | 3 | 0.002133 |
| Q21 != 2 and Q5 != 2 and difficulty != 5 and Q27 = 2 | 3 | 0.003228 |
| Q21 != 2 and Q5 != 2 and difficulty = 5 | 5 | 0.010642 |
| Q21 != 2 and Q5 != 2 and Q8 = 2 and Q10 != 3 | 13 | 0.001155 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q14 != 1 and difficulty = 1 and Q22 = 5 and Q8 = 5 and attendance = 0 | 5 | 0.003435 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty = 1 and Q10 != 1 and Q22 = 5 and attendance != 3 | 13 | 0.006351 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q1 = 2 | 3 | 0.001187 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q14 != 1 and nb.repeat = 2 and Q15 = 3 | 13 | 0.001315 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q14 != 1 and difficulty != 1 and nb.repeat != 3 and nb.repeat = 1 and attendance != 0 and difficulty != 3 and attendance != 4 and Q10 != 4 and Q24 != 4 and Q17 != 4 and attendance = 3 and Q18 != 5 | 5 | 0.001676 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q9 = 1 and difficulty = 4 | 9 | 0.002649 |
| Q21 != 2 and Q5 != 2 and Q8 != 2 and Q13 = 1 and difficulty != 1 | 3 | 0.000818 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty = 1 and Q1 != 5 and attendance != 3 and Q8 = 3 and attendance = 0 | 3 | 0.012637 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and attendance != 0 and difficulty = 4 and Q11 = 3 and Q24 = 3 and attendance != 1 | 3 | 0.004862 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and attendance != 0 and nb.repeat != 3 and nb.repeat = 1 and difficulty = 4 and attendance != 4 and Q8 = 5 and attendance != 3 | 5 | 0.002230 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and attendance != 0 and nb.repeat != 3 and nb.repeat = 1 and difficulty = 4 and attendance != 4 and Q8 != 5 and Q26 != 5 and Q6 = 3 and Q23 = 3 | 5 | 0.004386 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and attendance = 2 and Q16 != 5 and Q23 != 4 and difficulty = 3 | 3 | 0.004630 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty != 1 and nb.repeat != 3 and nb.repeat = 1 and Q25 = 4 and Q16 != 3 and Q11 != 3 and Q1 != 3 and Q22 = 4 and attendance = 2 and difficulty = 3 | 3 | 0.005493 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty != 1 and nb.repeat != 3 and nb.repeat = 1 and Q25 = 4 and Q16 != 3 and Q28 = 4 and Q3 != 3 and Q11 = 4 and attendance != 0 and attendance = 2 | 3 | 0.000875 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty != 1 and nb.repeat != 3 and nb.repeat = 1 and Q25 = 4 and Q16 != 3 and Q28 = 4 and Q11 != 3 and Q6 = 4 and attendance != 0 and attendance != 1 and difficulty != 3 | 5 | 0.004051 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and difficulty = 1 and Q1 != 5 and attendance != 3 and Q8 != 3 and Q9 = 4 | 3 | 0.006533 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q1 = 4 and Q17 != 3 and Q10 != 3 and Q12 != 3 and Q6 = 4 and Q27 = 4 and attendance = 3 | 5 | 0.001439 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and Q2 = 4 and Q11 = 3 | 3 | 0.001784 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and Q2 = 4 and Q12 != 3 and Q10 = 4 and Q26 = 4 and difficulty != 3 and attendance = 1 | 5 | 0.000957 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and Q2 = 4 and attendance != 2 and Q12 != 3 and Q10 = 4 and Q26 = 4 and difficulty != 3 | 5 | 0.003742 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q1 = 4 and Q24 != 3 and Q10 = 4 and Q6 = 4 and attendance != 1 | 13 | 0.011572 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q5 = 4 and Q27 = 4 and Q12 = 4 and attendance = 1 | 8 | 0.000576 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q2 = 4 and Q12 = 4 | 9 | 0.013227 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q2 != 4 and Q7 != 4 and Q4 != 4 and Q8 != 4 and Q16 != 4 and attendance = 3 and difficulty != 4 and Q1 != 5 and difficulty != 1 | 13 | 0.003027 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q2 != 4 and Q7 != 4 and Q4 != 4 and Q8 != 4 and Q16 != 4 and attendance = 1 and Q6 = 3 and difficulty = 3 | 13 | 0.001517 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and nb.repeat = 1 and Q2 = 4 | 5 | 0.004665 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and nb.repeat != 3 and Q2 != 4 and Q1 != 4 and Q4 != 4 and Q9 != 4 and Q16 = 4 | 5 | 0.002119 |
| Q13 != 1 and Q21 != 2 and Q5 != 2 and Q8 != 2 and attendance = 1 and Q1 = 3 | 3 | 0.005021 |
| attendance = 1 and Q11 = 5 | 9 | 0.001354 |
| attendance != 1 and Q16 != 1 and Q3 != 2 and Q8 != 2 and Q23 = 4 and nb.repeat != 1 | 9 | 0.001492 |
| attendance != 1 and Q16 != 1 and Q3 != 2 and Q5 != 4 and Q15 != 4 and Q28 != 4 and attendance = 2 | 3 | 0.002461 |
| attendance != 1 and Q16 != 1 and Q3 != 2 and Q5 = 4 | 8 | 0.015722 |
| attendance != 1 and Q16 != 1 and Q9 != 2 and Q9 != 4 and attendance != 0 and difficulty != 1 and Q6 = 5 and difficulty != 3 | 3 | 0.003894 |
| Q3 != 2 and Q15 != 4 and Q16 != 1 and Q28 != 4 and Q8 = 5 and attendance != 0 | 3 | 0.001796 |
| Q3 != 2 and Q15 != 4 and Q28 != 4 and Q16 != 1 and Q8 = 5 | 9 | 0.010630 |
| attendance != 1 and Q15 != 4 and Q16 != 1 and Q28 != 4 and Q24 = 3 and difficulty != 1 and attendance = 0 | 9 | 0.003630 |
| attendance != 1 and Q15 != 4 and Q19 != 5 and Q21 != 3 | 13 | 0.032601 |
| attendance != 0 and attendance != 1 and Q27 = 3 and difficulty != 1 | 5 | 0.005734 |
| attendance = 0 | 8 | 0.017245 |
| Q15 != 4 and Q4 = 3 | 13 | 0.020031 |
| Q15 = 4 | 9 | 0.005427 |
|  | 5 | 0.177778 |


### JRip

| Rule | Predicted class | Quality (precision * recall) |
|:----|----:|----:|
| instr = 1 and difficulty = 5 and Q3 = 3 | 7 | 0.002137 |
| instr = 1 and Q2 = 1 and difficulty = 5 | 7 | 0.002119 |
| instr = 1 and difficulty = 3 | 10 | 0.025794 |
| instr = 1 and difficulty = 1 | 10 | 0.016743 |
| instr = 1 and Q26 = 3 and nb.repeat = 1 and Q28 = 3 | 10 | 0.002676 |
| instr = 1 and difficulty = 2 | 10 | 0.005151 |
| instr = 2 and difficulty = 4 | 11 | 0.015599 |
| instr = 2 and difficulty = 5 | 11 | 0.004650 |
| instr = 3 and Q21 = 4 and Q1 = 1 and Q23 = 1 | 8 | 0.002432 |
| instr = 3 and Q28 = 4 and Q10 = 3 and attendance = 4 | 8 | 0.002305 |
| instr = 2 and difficulty = 2 and Q16 = 4 | 6 | 0.005798 |
| instr = 2 and Q23 = 2 and Q26 = 2 | 6 | 0.006254 |
| instr = 2 and Q12 = 4 and Q25 = 5 | 6 | 0.003115 |
|  | 3 | 0.178061 |


# Text representation of classifiers as-is

## JRip

Decision list:

rules | predicted class
---|---
(instr = 1) and (difficulty = 5) and (Q3 = 3)|7 (30.0/12.0)
(instr = 1) and (Q2 = 1) and (difficulty = 5)|7 (21.0/6.0)
(instr = 1) and (difficulty = 3)|10 (260.0/79.0)
(instr = 1) and (difficulty = 1)|10 (118.0/20.0)
(instr = 1) and (Q26 = 3) and (nb.repeat = 1) and (Q28 = 3)|10 (35.0/11.0)
(instr = 1) and (difficulty = 2)|10 (44.0/11.0)
(instr = 2) and (difficulty = 4)|11 (215.0/93.0)
(instr = 2) and (difficulty = 5)|11 (78.0/38.0)
(instr = 3) and (Q21 = 4) and (Q1 = 1) and (Q23 = 1)|8 (19.0/5.0)
(instr = 3) and (Q28 = 4) and (Q10 = 3) and (attendance = 4)|8 (37.0/18.0)
(instr = 2) and (difficulty = 2) and (Q16 = 4)|6 (63.0/24.0)
(instr = 2) and (Q23 = 2) and (Q26 = 2)|6 (63.0/28.0)
(instr = 2) and (Q12 = 4) and (Q25 = 5)|6 (23.0/6.0)
|3 (4210.0/3409.0)


## PART

Decision list:

rules | predicted class
---|---
instr = 1 AND nb.repeat = 3 AND Q1 != 3|7 (16.0/7.0)
instr = 1 AND nb.repeat = 3|7 (13.0/2.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q16 != 1 AND Q8 != 5 AND Q11 != 5 AND nb.repeat = 1 AND Q6 = 2 AND Q1 = 2 AND difficulty = 3|10 (10.0/2.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q16 != 1 AND Q8 != 5 AND Q11 != 5 AND nb.repeat = 1 AND Q26 != 2 AND difficulty = 1 AND Q27 != 3|10 (29.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q4 != 1 AND difficulty = 1 AND Q9 != 2 AND Q1 != 3|10 (23.0/3.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q21 != 5 AND Q16 != 1 AND Q8 != 5 AND Q11 != 5 AND nb.repeat = 1 AND Q1 != 2 AND Q26 != 2 AND difficulty != 1 AND attendance != 4 AND Q22 != 3 AND Q9 = 4 AND attendance != 1 AND attendance != 2|10 (31.0/3.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q13 != 5 AND Q8 != 5 AND Q16 != 1 AND difficulty = 1 AND Q7 = 3|10 (15.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q13 = 5 AND Q21 = 5 AND Q4 = 5 AND attendance = 3|10 (28.0/8.0)
instr = 1 AND difficulty = 2 AND Q5 != 5 AND Q11 != 4 AND Q3 != 2|10 (21.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q21 != 5 AND Q16 != 1 AND Q2 != 2 AND Q26 != 2 AND Q8 != 5 AND Q1 = 4 AND attendance = 2|10 (19.0/1.0)
instr = 1 AND difficulty != 4 AND difficulty != 5 AND Q2 = 2|10 (18.0/2.0)
instr = 1 AND difficulty = 3 AND Q20 = 1|10 (24.0/11.0)
instr = 1 AND difficulty = 3 AND Q25 != 5 AND Q13 != 5 AND attendance != 4 AND Q1 = 3 AND attendance != 2 AND attendance = 3|10 (18.0/6.0)
instr = 1 AND difficulty = 3 AND Q25 != 5 AND Q13 != 5 AND attendance = 4|10 (15.0/3.0)
instr = 1 AND difficulty = 3 AND Q12 = 3 AND attendance = 1|10 (15.0/5.0)
instr = 1 AND difficulty = 3 AND Q12 != 3 AND Q25 = 4 AND attendance = 1|10 (20.0/6.0)
instr = 1 AND difficulty = 3 AND Q12 != 3 AND Q25 != 4 AND Q13 != 4 AND attendance != 4 AND Q2 != 4|2 (16.0/6.0)
instr = 1 AND difficulty = 3 AND Q14 = 3|10 (16.0/5.0)
instr = 1 AND difficulty = 3 AND Q3 = 4 AND Q12 = 4|10 (11.0/5.0)
instr = 1 AND difficulty = 3 AND Q25 != 4 AND Q9 = 5|10 (18.0/6.0)
instr = 1 AND difficulty = 3 AND Q25 = 4|10 (10.0/1.0)
instr = 1 AND difficulty = 1 AND attendance = 0|10 (33.0/13.0)
instr = 1 AND difficulty != 1 AND Q1 = 5 AND attendance = 3|2 (15.0/6.0)
instr = 1 AND difficulty != 1 AND difficulty = 2 AND Q17 != 4|2 (12.0/6.0)
instr = 1 AND difficulty != 1 AND difficulty != 2 AND nb.repeat = 1 AND Q25 = 2|10 (18.0/9.0)
instr = 1 AND difficulty != 1 AND Q27 = 2|7 (12.0/2.0)
instr = 1 AND difficulty != 1 AND difficulty != 2 AND nb.repeat != 1|7 (12.0/4.0)
instr = 1 AND difficulty != 1 AND Q1 = 2 AND Q8 != 3|7 (12.0/3.0)
instr = 1 AND difficulty != 1 AND Q5 != 2 AND Q6 = 1 AND difficulty != 4|7 (19.0/6.0)
instr = 1 AND Q5 != 2 AND difficulty != 1 AND Q6 != 2 AND Q12 != 2 AND Q3 != 3 AND Q21 != 3 AND Q16 = 4 AND attendance = 3|2 (17.0/9.0)
instr = 1 AND Q5 != 2 AND difficulty != 1 AND Q8 = 4 AND Q21 = 4 AND attendance != 1|10 (21.0/8.0)
instr = 1 AND difficulty != 1 AND Q5 != 2 AND Q9 = 4 AND attendance != 1|10 (14.0/6.0)
instr = 1 AND difficulty != 1 AND Q5 != 2 AND Q15 = 4 AND Q6 = 4|7 (14.0/8.0)
instr = 1 AND difficulty != 1 AND Q5 != 2 AND Q5 != 4 AND Q1 = 5|2 (19.0/11.0)
instr = 1 AND difficulty != 1 AND Q17 != 5 AND Q15 != 4 AND attendance != 4 AND Q9 = 3 AND difficulty != 5|2 (20.0/11.0)
instr = 1 AND Q20 != 4 AND difficulty != 1 AND Q17 != 5 AND attendance != 3 AND Q1 = 3|7 (15.0/6.0)
instr = 1 AND Q20 != 4 AND difficulty != 1 AND Q17 = 5|7 (13.0/5.0)
instr = 1 AND Q20 != 4 AND attendance != 3|10 (18.0/6.0)
instr = 1 AND Q20 != 4|2 (14.0/9.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q17 != 1 AND nb.repeat != 2 AND Q11 = 2|11 (17.0/5.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q17 != 1 AND nb.repeat = 2|11 (16.0/5.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q17 != 1 AND Q7 != 2 AND Q13 != 5 AND attendance = 0|11 (13.0/3.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q17 = 1|6 (12.0/2.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q7 = 2|11 (12.0/2.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q13 != 5 AND Q1 != 2 AND attendance != 2 AND Q4 != 3 AND Q18 = 4 AND attendance = 3|11 (12.0/3.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q13 != 5 AND Q1 != 2 AND Q28 != 4 AND Q2 != 4 AND Q15 = 3 AND attendance != 3 AND attendance = 1|11 (16.0/6.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND attendance = 1|11 (16.0/6.0)
instr != 1 AND instr = 2 AND difficulty = 5 AND Q19 != 5 AND Q14 != 2 AND attendance != 0 AND Q14 = 3|11 (21.0/10.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND attendance != 3 AND attendance = 2 AND Q6 != 4|11 (11.0/3.0)
instr != 1 AND instr = 2 AND difficulty = 5 AND Q27 != 2 AND Q19 != 5 AND attendance != 0 AND Q25 = 4|1 (15.0/9.0)
instr != 1 AND instr = 2 AND difficulty = 5 AND nb.repeat = 1 AND Q13 != 1 AND Q21 != 5|11 (14.0/6.0)
instr != 1 AND instr = 2 AND difficulty = 5 AND nb.repeat = 1 AND Q1 != 1|11 (10.0/2.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND attendance = 4 AND Q12 = 4|11 (14.0/6.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q9 = 4 AND attendance != 3|6 (10.0/6.0)
instr != 1 AND instr = 2 AND attendance = 1 AND Q27 = 5 AND Q9 = 5|11 (18.0/10.0)
instr != 1 AND instr = 2 AND attendance = 1 AND Q14 != 5 AND Q12 = 2 AND Q10 = 2|6 (16.0/9.0)
instr != 1 AND instr = 2 AND attendance = 1 AND Q14 != 5 AND Q4 != 2 AND Q8 != 2 AND difficulty != 1 AND difficulty != 2 AND nb.repeat != 2 AND Q6 != 1 AND Q6 != 3 AND Q1 = 4|6 (31.0/14.0)
instr != 1 AND instr = 2 AND Q28 = 2 AND Q20 != 3 AND nb.repeat = 1 AND attendance != 0 AND Q14 = 2|6 (15.0/4.0)
instr != 1 AND instr = 2 AND difficulty = 2 AND Q22 != 2 AND Q7 != 2 AND Q4 != 5 AND Q1 != 2 AND Q23 != 5 AND Q17 != 5 AND attendance != 4 AND attendance != 3 AND Q27 != 1 AND Q10 != 3 AND attendance != 1|6 (17.0/5.0)
instr != 1 AND instr = 2 AND difficulty = 4 AND Q9 != 4 AND Q13 != 4 AND attendance != 3 AND Q2 != 5|11 (10.0/4.0)
instr != 1 AND instr = 2 AND attendance = 1 AND Q18 != 5 AND Q6 != 2 AND difficulty != 2 AND nb.repeat != 2 AND Q3 != 4 AND Q3 != 1|6 (30.0/13.0)
instr = 1|7 (9.0)
instr = 2 AND difficulty = 2 AND Q20 = 2|1 (9.0/4.0)
instr = 2 AND nb.repeat = 2 AND Q9 != 2 AND attendance != 2 AND Q13 != 4 AND difficulty = 3 AND Q7 = 3|6 (12.0/6.0)
instr = 2 AND Q21 = 2 AND attendance != 3 AND difficulty = 1 AND Q8 = 2|6 (16.0/11.0)
instr = 2 AND Q21 = 2 AND Q18 = 2 AND difficulty = 3|6 (10.0/4.0)
instr = 2 AND Q21 = 2 AND Q16 != 2|6 (12.0/5.0)
instr = 2 AND Q21 != 2 AND Q28 = 2|6 (15.0/5.0)
instr = 2 AND Q21 != 2 AND Q26 = 2|11 (14.0/5.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND Q24 != 2 AND Q9 = 2 AND Q21 != 4|1 (12.0/7.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND Q9 != 2 AND difficulty = 2 AND attendance != 0 AND Q4 != 5 AND Q1 != 2 AND Q2 != 3 AND Q4 != 3 AND Q4 != 1 AND attendance != 3|6 (17.0/9.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND Q9 != 2 AND difficulty = 2 AND attendance = 0|1 (16.0/8.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND Q9 = 2|6 (14.0/6.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND difficulty = 2 AND Q26 != 5 AND Q1 != 2 AND Q13 != 3 AND Q7 != 4 AND Q4 != 3|6 (14.0/5.0)
instr = 2 AND Q21 != 2 AND Q23 != 2 AND Q24 != 2 AND Q10 != 2 AND Q27 = 2|6 (16.0/6.0)
instr = 2 AND Q21 != 2 AND Q13 != 2 AND Q23 != 2 AND Q24 != 2 AND Q10 != 2 AND Q12 != 2 AND Q22 = 4 AND Q18 != 5 AND Q17 = 4 AND Q16 = 4 AND Q27 = 4 AND difficulty != 2 AND Q12 != 4 AND Q8 = 3|6 (18.0/7.0)
instr = 2 AND Q21 = 2|6 (11.0/1.0)
instr = 2 AND Q13 = 2|11 (11.0/6.0)
instr = 2 AND Q23 = 2|13 (11.0/6.0)
instr = 2 AND Q12 = 2 AND Q25 = 4|11 (11.0/6.0)
instr = 2 AND Q12 != 2 AND Q7 = 2 AND Q15 = 4|11 (11.0/3.0)
instr = 2 AND Q12 != 2 AND Q4 = 2 AND Q10 != 4|1 (12.0/6.0)
instr = 2 AND Q12 != 2 AND difficulty = 2 AND Q13 = 4 AND attendance != 3|6 (11.0)
instr = 2 AND Q12 != 2 AND difficulty = 3 AND Q6 != 2 AND Q8 != 2 AND attendance = 0 AND Q13 != 5 AND Q13 = 3|6 (14.0/4.0)
instr = 2 AND Q12 != 2 AND Q23 = 4 AND Q16 != 3 AND Q15 != 5 AND nb.repeat = 1 AND Q1 != 2 AND Q6 = 4 AND difficulty != 1 AND Q1 = 4 AND attendance != 4 AND attendance != 2|6 (40.0/23.0)
instr = 2 AND Q12 != 2 AND difficulty != 2 AND difficulty != 1 AND Q6 != 2 AND Q24 = 4 AND Q16 != 5 AND Q7 = 4 AND attendance != 1 AND Q2 = 4 AND attendance != 3 AND attendance != 4|6 (30.0/19.0)
instr = 2 AND Q12 != 2 AND nb.repeat = 2 AND Q6 != 4 AND Q12 != 3 AND Q20 = 1|6 (10.0/3.0)
instr = 2 AND Q12 != 2 AND difficulty != 5 AND difficulty != 2 AND difficulty != 1 AND Q6 != 2 AND attendance = 0 AND Q28 = 5|6 (16.0/6.0)
instr = 2 AND Q12 != 2 AND difficulty != 5 AND Q3 != 2 AND Q2 != 2 AND Q12 != 3 AND Q11 != 3 AND Q3 != 3 AND nb.repeat != 1|6 (15.0/7.0)
instr = 2 AND Q12 != 2 AND nb.repeat = 2|11 (13.0/7.0)
instr = 2 AND Q12 != 2 AND Q3 = 2|6 (10.0/5.0)
instr = 2 AND Q12 != 2 AND attendance = 2 AND Q11 != 3 AND difficulty = 3 AND Q1 != 4 AND Q6 != 5|11 (10.0/5.0)
instr = 2 AND Q12 != 2 AND attendance = 2 AND Q11 != 3 AND Q16 = 5|6 (19.0/3.0)
instr = 2 AND Q12 != 2 AND Q23 = 4 AND Q21 = 4 AND Q26 = 4 AND Q7 = 4 AND Q4 = 4 AND difficulty != 3 AND attendance = 0|6 (29.0/17.0)
instr = 2 AND Q12 = 2|11 (9.0/4.0)
instr = 2 AND Q12 != 3 AND Q8 = 3 AND Q5 = 3|1 (9.0/4.0)
instr = 2 AND Q12 != 3 AND Q27 != 3 AND difficulty != 2 AND attendance != 1 AND Q23 = 4 AND Q6 = 4 AND difficulty != 1|6 (24.0/15.0)
instr = 2 AND Q21 = 3 AND Q24 = 3 AND Q6 = 3 AND difficulty != 1 AND Q1 = 3 AND attendance != 4 AND attendance = 2|11 (17.0/9.0)
instr = 2 AND difficulty = 5|11 (9.0/5.0)
instr = 2 AND Q1 != 2 AND Q23 = 4 AND Q6 != 4 AND Q8 = 4|6 (9.0/5.0)
instr = 2 AND Q1 != 2 AND Q8 != 2 AND Q23 = 4 AND difficulty = 1|1 (22.0/15.0)
instr = 2 AND Q23 = 4 AND Q9 = 4|1 (11.0/7.0)
instr = 2 AND Q23 != 4 AND Q13 = 4 AND difficulty != 3|6 (13.0/6.0)
instr = 2 AND Q23 != 4 AND Q19 != 4 AND Q15 != 4 AND Q6 = 4|1 (17.0/10.0)
instr = 2 AND Q23 != 4 AND Q19 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 2 AND difficulty != 2 AND attendance = 3 AND Q2 = 3 AND difficulty = 3|6 (16.0/6.0)
instr = 2 AND Q23 != 4 AND Q19 = 4|11 (12.0/5.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 2 AND attendance = 3 AND Q5 != 5 AND difficulty = 4|11 (12.0/7.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 2 AND attendance = 3 AND Q5 = 5 AND difficulty != 3|6 (19.0/12.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance = 3 AND Q5 = 5|6 (16.0/10.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 3 AND attendance != 2 AND difficulty = 3 AND Q4 != 3 AND Q27 = 5|1 (24.0/13.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance = 3|11 (11.0/3.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 2 AND difficulty = 3 AND Q2 != 1|6 (11.0/5.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND attendance != 2 AND difficulty != 3 AND attendance != 4 AND difficulty = 1 AND Q27 != 5 AND Q18 != 3|6 (48.0/33.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND Q27 != 1 AND attendance != 4 AND Q27 != 5 AND Q1 = 3 AND attendance = 0|11 (43.0/29.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND Q27 = 1|1 (14.0/7.0)
instr = 2 AND Q23 != 4 AND Q15 != 4 AND Q11 != 4 AND Q7 = 3 AND attendance != 1|11 (13.0/5.0)
instr = 2 AND Q23 != 4 AND Q4 != 4 AND Q4 != 1 AND attendance != 4 AND Q1 != 3|1 (41.0/27.0)
instr = 2 AND Q24 != 4 AND Q4 != 4 AND Q1 = 5|6 (12.0/7.0)
instr = 2 AND Q24 != 4 AND Q24 = 3|6 (16.0/7.0)
instr = 2 AND Q24 != 4|13 (11.0/3.0)
instr != 2 AND nb.repeat != 1 AND attendance != 3 AND Q11 = 1 AND difficulty = 5 AND attendance != 0|13 (12.0/7.0)
instr != 2 AND nb.repeat != 1 AND Q11 = 1 AND difficulty != 5 AND difficulty != 4 AND nb.repeat != 2 AND attendance = 0|9 (18.0/10.0)
instr != 2 AND difficulty = 2 AND Q11 = 2 AND Q22 = 2 AND nb.repeat != 2|5 (16.0/9.0)
instr != 2 AND difficulty = 2 AND Q11 = 2 AND Q22 != 2|13 (16.0/4.0)
instr != 2 AND difficulty = 2 AND Q9 = 2 AND Q3 = 2|13 (10.0/6.0)
instr != 2 AND difficulty = 2 AND Q12 = 2 AND Q10 != 3|8 (17.0/9.0)
instr != 2 AND nb.repeat != 1 AND Q11 = 1 AND difficulty = 4|13 (16.0/6.0)
instr != 2 AND difficulty = 2 AND Q12 != 2 AND Q19 != 4 AND Q15 != 4 AND nb.repeat = 3|9 (16.0/9.0)
instr != 2 AND nb.repeat != 1 AND Q11 = 1 AND Q15 = 1 AND attendance != 1 AND difficulty != 1|13 (15.0/7.0)
instr != 2 AND nb.repeat != 1 AND Q14 = 1 AND Q4 = 1 AND attendance = 1|13 (17.0/10.0)
instr != 2 AND nb.repeat != 1 AND Q14 = 1 AND Q4 = 1|3 (13.0/8.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q10 = 5 AND attendance != 4 AND attendance != 2 AND difficulty != 2 AND attendance != 0|8 (19.0/10.0)
instr != 2 AND Q17 = 1 AND Q9 != 5 AND Q19 != 3 AND difficulty != 2 AND Q18 != 2 AND Q16 = 1 AND Q8 != 2 AND Q8 = 1 AND Q1 = 1 AND attendance = 4 AND difficulty = 5|13 (17.0/11.0)
instr != 2 AND Q17 = 1 AND Q9 != 5 AND Q19 != 3 AND difficulty != 2 AND Q18 != 2 AND Q16 = 1 AND Q8 != 2 AND attendance = 4|13 (16.0/6.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q8 != 1 AND Q4 = 5 AND attendance != 4 AND difficulty != 2 AND difficulty = 3|8 (14.0/8.0)
instr != 2 AND difficulty = 2 AND Q12 != 2 AND Q17 != 1 AND Q19 != 4 AND Q15 != 4 AND Q7 != 3 AND Q3 = 5|13 (27.0/18.0)
instr != 2 AND Q17 = 1 AND Q9 != 5 AND Q19 != 3 AND difficulty != 2 AND Q18 != 2 AND Q16 = 1 AND Q8 != 2 AND Q8 = 1 AND Q1 = 1 AND attendance = 2|13 (14.0/8.0)
instr != 2 AND difficulty = 2 AND Q12 != 2 AND nb.repeat != 3 AND Q17 != 1 AND Q2 != 2 AND Q28 = 3 AND nb.repeat = 1 AND attendance != 1|13 (16.0/4.0)
instr != 2 AND Q17 = 1 AND Q9 != 5 AND Q19 != 3 AND difficulty != 2 AND Q18 != 2 AND Q16 = 1 AND Q8 != 2 AND Q8 = 1 AND Q1 = 1 AND attendance = 1 AND difficulty = 5|3 (14.0/7.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q10 = 5 AND nb.repeat = 2|13 (18.0/10.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q10 = 5 AND attendance = 4|13 (13.0/6.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q4 = 5|8 (17.0/10.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q12 != 1 AND Q8 != 1 AND Q1 = 2 AND Q5 != 4 AND Q8 = 2 AND nb.repeat = 2 AND Q14 = 2|3 (16.0/10.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q12 != 1 AND Q8 != 1 AND Q1 = 2 AND Q5 != 4 AND attendance != 0 AND Q8 = 2|8 (15.0/7.0)
instr != 2 AND Q17 = 1 AND Q9 != 5 AND Q19 != 3 AND difficulty != 2 AND Q16 = 1 AND Q13 = 1 AND Q6 != 2 AND Q1 != 3 AND Q8 = 1 AND attendance != 1 AND difficulty != 4 AND difficulty != 3 AND attendance = 0 AND difficulty = 1|3 (194.0/130.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q12 != 1 AND Q8 != 1 AND attendance = 3 AND Q12 != 4 AND difficulty != 3|9 (21.0/13.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q12 != 1 AND Q8 != 1 AND Q25 != 4 AND attendance != 3 AND Q18 != 4 AND Q12 != 4 AND Q1 != 1 AND Q26 != 2 AND Q2 != 2 AND difficulty = 1|13 (17.0/10.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q12 != 1 AND Q8 != 1 AND Q25 != 4 AND attendance != 3 AND Q18 != 4 AND Q12 != 4 AND Q1 = 1|13 (13.0/7.0)
instr != 2 AND difficulty = 2 AND Q17 != 1 AND Q26 != 5 AND Q12 != 2 AND Q28 != 3 AND Q5 != 3 AND Q23 = 4 AND attendance != 0 AND attendance != 3|5 (18.0/12.0)
instr != 2 AND difficulty = 2 AND Q17 != 1 AND Q26 != 5 AND Q12 != 2 AND Q28 != 3 AND Q5 != 3 AND Q18 != 4|9 (13.0/5.0)
instr != 2 AND difficulty = 2 AND Q12 = 2|8 (11.0/6.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q8 != 1 AND Q26 = 2|8 (15.0/10.0)
instr != 2 AND difficulty = 2 AND Q12 = 1|13 (10.0/2.0)
instr != 2 AND nb.repeat != 1 AND Q14 != 1 AND Q11 != 1 AND Q11 != 5 AND Q8 != 1 AND Q20 != 2 AND Q6 != 2 AND Q25 != 4 AND attendance != 3 AND Q10 = 4|3 (12.0/8.0)
instr != 2 AND nb.repeat = 2 AND Q19 != 1 AND Q7 != 1 AND Q20 != 5 AND Q8 != 2 AND attendance != 3 AND attendance = 0 AND Q1 != 4 AND difficulty != 3|13 (17.0/10.0)
instr != 2 AND nb.repeat = 2 AND Q19 != 1 AND Q1 = 1|9 (14.0/8.0)
instr != 2 AND nb.repeat = 2 AND Q19 != 1 AND Q23 != 2 AND Q1 = 2|9 (14.0/6.0)
instr != 2 AND Q6 != 1 AND Q5 = 1 AND Q21 != 1 AND Q11 = 1|3 (10.0/4.0)
instr != 2 AND attendance = 4 AND nb.repeat != 2 AND Q4 = 1 AND Q20 != 1 AND Q21 != 3|8 (11.0/3.0)
instr != 2 AND Q6 != 1 AND Q5 = 1 AND Q28 != 2 AND Q20 != 1 AND Q2 != 2 AND Q20 != 3|8 (15.0/6.0)
instr != 2 AND nb.repeat != 1 AND Q10 != 1 AND Q19 != 1 AND Q27 != 2 AND Q2 != 4 AND Q19 != 4 AND difficulty = 5|13 (16.0/9.0)
instr != 2 AND Q6 != 1 AND Q11 = 1 AND Q23 != 4 AND difficulty != 1 AND Q19 != 2 AND Q28 != 3 AND Q17 != 5 AND Q6 != 2|5 (16.0/7.0)
instr != 2 AND nb.repeat = 2 AND Q19 != 1 AND Q23 != 2 AND attendance != 3 AND difficulty != 4 AND attendance = 1 AND Q12 != 3|8 (14.0/8.0)
instr != 2 AND Q6 != 1 AND Q17 = 1 AND Q2 != 1 AND Q6 != 2|13 (14.0/8.0)
instr != 2 AND Q6 != 1 AND Q17 = 1 AND Q1 != 1|5 (10.0/6.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q5 = 1 AND Q22 != 2 AND Q11 != 3|8 (14.0/8.0)
instr != 2 AND nb.repeat = 2 AND difficulty != 5 AND Q23 != 2 AND attendance != 3 AND difficulty != 4 AND attendance = 1|9 (11.0/7.0)
instr != 2 AND difficulty = 5 AND Q2 != 2 AND Q9 != 2 AND Q24 != 2 AND Q19 != 2 AND Q12 != 2 AND attendance != 0 AND Q1 != 4 AND Q18 != 1 AND Q4 != 4 AND attendance = 1|3 (18.0/10.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q21 = 1 AND Q24 != 1|5 (11.0/6.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 = 1 AND Q28 != 3 AND Q1 != 2 AND Q5 != 2|5 (13.0/7.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 = 1 AND Q28 != 3 AND Q1 = 2|3 (16.0/7.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 = 1 AND Q28 = 3|13 (17.0/11.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 != 1 AND Q23 = 1 AND Q1 != 1|9 (16.0/9.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 != 1 AND Q23 != 1 AND Q4 = 1 AND Q21 != 2 AND Q24 = 3|9 (15.0/8.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 != 1 AND Q23 != 1 AND nb.repeat = 2 AND Q23 != 2 AND attendance != 3 AND difficulty != 4 AND attendance != 0|3 (17.0/11.0)
instr != 2 AND Q6 != 1 AND Q17 != 1 AND Q11 = 1|5 (10.0/1.0)
instr != 2 AND Q4 != 1 AND Q21 = 1|13 (14.0/7.0)
instr != 2 AND nb.repeat = 2 AND Q23 != 2 AND difficulty != 4 AND Q13 = 3|3 (15.0/7.0)
instr != 2 AND Q4 != 1 AND Q23 = 1 AND Q27 = 1|3 (11.0/8.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND nb.repeat != 3 AND Q15 = 2 AND Q1 = 2|5 (14.0/8.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND Q15 != 2 AND Q23 != 2 AND Q9 != 2 AND Q1 = 2 AND Q12 != 3|8 (13.0/6.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND Q6 = 1 AND Q8 != 1 AND Q10 = 3|13 (11.0/5.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND difficulty = 5 AND Q2 != 2 AND Q9 != 2 AND attendance = 0|3 (20.0/11.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND difficulty = 5 AND Q2 != 2 AND Q9 != 2 AND Q24 != 4 AND attendance != 3 AND attendance != 1 AND Q12 != 3|3 (19.0/10.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND difficulty = 5 AND Q8 != 2 AND Q2 != 2 AND Q25 = 3 AND attendance != 3 AND attendance = 4|3 (13.0/6.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND Q15 != 2 AND Q1 = 2 AND Q5 = 2|8 (10.0/6.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND Q27 = 1 AND Q28 != 4 AND Q23 != 2|8 (11.0/5.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND Q1 != 2 AND Q15 != 2 AND Q2 != 2 AND Q12 != 2 AND Q20 != 5 AND Q4 = 4 AND Q23 = 4 AND Q12 != 3 AND difficulty != 4 AND difficulty = 3|3 (27.0/20.0)
instr != 2 AND Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND Q1 != 2 AND Q15 != 2 AND Q2 != 2 AND Q8 != 2 AND Q20 != 5 AND difficulty != 5 AND Q4 = 4 AND Q8 = 4 AND difficulty = 4|3 (19.0/12.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND Q27 != 1 AND Q21 != 2 AND Q27 != 2 AND Q12 != 2 AND difficulty = 1 AND Q19 != 5|3 (13.0/6.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND difficulty = 1|3 (17.0/11.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND Q2 != 2 AND Q23 != 2 AND Q8 != 2 AND Q17 != 5 AND Q1 != 1 AND difficulty != 5 AND Q23 = 4|8 (17.0/11.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND Q1 = 4 AND Q20 = 4|5 (12.0/6.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND Q12 != 4 AND Q23 != 4 AND Q10 != 2 AND Q14 != 4 AND difficulty != 3 AND Q3 = 3|3 (15.0/11.0)
instr != 2 AND attendance = 4 AND Q1 != 2 AND Q12 = 4|8 (14.0/6.0)
instr = 2|11 (9.0/1.0)
attendance = 4 AND Q1 = 2|8 (9.0/1.0)
attendance = 4 AND Q25 = 4 AND difficulty = 3|8 (9.0/3.0)
Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND attendance = 4 AND Q5 != 4 AND Q15 != 3 AND difficulty = 3|13 (21.0/13.0)
Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND Q8 = 1 AND Q19 != 3 AND Q16 != 2|5 (15.0/9.0)
Q4 != 1 AND Q23 != 1 AND difficulty != 2 AND nb.repeat != 2 AND nb.repeat != 1 AND Q4 = 4|3 (22.0/14.0)
nb.repeat = 3 AND Q11 != 3|13 (15.0/8.0)
nb.repeat = 3 AND attendance != 0 AND difficulty != 4|9 (12.0/5.0)
difficulty = 2 AND Q20 != 4 AND attendance = 1|13 (10.0/5.0)
Q4 != 1 AND Q23 != 1 AND Q26 = 1|3 (11.0/7.0)
Q4 != 1 AND Q23 != 1 AND nb.repeat = 3 AND attendance = 0|9 (10.0/6.0)
difficulty = 2 AND attendance = 3|13 (18.0/10.0)
difficulty = 2|9 (17.0/9.0)
Q4 != 1 AND Q23 != 1 AND Q8 = 1|9 (17.0/11.0)
Q4 != 1 AND Q23 != 1 AND difficulty = 5 AND Q1 != 1 AND Q21 = 2|3 (14.0/8.0)
difficulty = 5 AND Q27 != 5 AND Q16 != 3 AND Q1 != 3 AND Q20 != 3 AND Q26 != 3 AND Q22 != 1 AND Q24 != 4|3 (15.0/7.0)
Q6 != 1 AND Q23 != 1 AND Q3 = 1|3 (16.0/10.0)
Q6 != 1 AND Q23 != 1 AND Q4 = 1 AND Q3 != 2|8 (16.0/10.0)
Q4 != 1 AND Q2 = 1 AND Q18 != 3|8 (15.0/10.0)
Q4 != 1 AND Q2 != 1 AND Q18 = 1|3 (16.0/7.0)
Q4 != 1 AND Q2 != 1 AND difficulty = 5 AND Q8 != 2 AND Q2 != 2 AND Q14 != 3 AND Q25 != 5 AND Q1 != 4|3 (11.0/4.0)
Q4 != 1 AND Q2 != 1 AND difficulty = 5 AND Q8 != 2 AND Q2 != 2 AND Q22 != 4 AND attendance = 3 AND Q1 = 3|5 (17.0/10.0)
Q4 != 1 AND Q2 != 1 AND difficulty = 5 AND Q8 != 2 AND Q2 != 2 AND Q8 != 4 AND attendance != 3|3 (13.0/4.0)
Q4 = 1 AND Q3 != 3 AND Q11 != 5 AND Q9 != 4 AND Q9 = 3|5 (14.0/9.0)
Q4 = 1 AND Q3 != 3 AND Q11 != 5 AND Q9 != 4 AND Q17 != 3 AND Q3 = 1 AND attendance != 0 AND difficulty != 3 AND attendance = 1|3 (12.0/4.0)
Q4 = 1 AND Q3 != 3 AND Q11 != 5 AND Q1 = 1 AND Q3 != 1|13 (13.0/8.0)
Q4 = 1 AND Q3 != 3 AND Q11 != 5 AND Q1 = 1 AND Q12 = 1 AND difficulty = 1 AND Q13 != 1|13 (11.0/5.0)
Q4 != 1 AND Q2 != 1 AND Q28 = 2 AND Q20 != 2 AND Q14 != 2|5 (17.0/7.0)
Q28 = 2 AND Q6 != 1 AND difficulty != 3 AND Q17 != 3 AND Q9 != 3 AND difficulty != 4 AND Q1 != 2 AND Q1 != 1|5 (16.0/8.0)
Q28 = 2 AND Q6 != 1 AND difficulty != 3 AND Q17 != 3 AND Q9 != 3 AND difficulty != 4 AND Q1 != 1|3 (37.0/23.0)
Q4 != 1 AND Q2 != 1 AND Q28 = 2 AND attendance != 1 AND Q13 = 2 AND Q8 != 3 AND attendance != 3 AND Q1 != 1|13 (18.0/11.0)
Q4 != 1 AND Q2 != 1 AND Q28 = 2 AND attendance != 1 AND attendance != 3 AND Q1 = 1|3 (17.0/8.0)
Q28 = 2 AND Q1 != 1 AND Q17 != 3 AND difficulty != 3 AND Q9 != 3|3 (14.0/7.0)
Q15 != 2 AND Q2 != 2 AND Q18 = 2 AND Q2 != 3|3 (16.0/9.0)
Q28 = 2 AND Q1 = 1|13 (10.0/2.0)
Q28 = 2 AND Q17 = 2 AND Q9 = 2|3 (10.0/6.0)
Q15 != 2 AND Q17 = 2 AND Q12 != 3|13 (11.0/6.0)
Q19 = 2 AND Q7 = 3 AND Q10 != 2|3 (11.0/6.0)
Q19 = 2 AND Q7 != 3 AND Q2 != 2|5 (11.0/8.0)
Q19 = 2 AND Q7 != 3|9 (10.0/6.0)
Q19 != 2 AND Q24 = 2 AND Q20 = 4|5 (16.0/9.0)
Q19 = 2|9 (9.0/2.0)
Q2 != 2 AND Q21 = 2 AND Q14 = 3|5 (9.0/5.0)
Q18 != 2 AND Q8 != 2 AND Q13 != 2 AND Q14 != 2 AND Q23 != 2 AND Q10 != 2 AND Q12 = 2 AND Q6 != 3|5 (14.0/6.0)
Q2 != 2 AND Q21 != 2 AND Q5 = 2 AND Q4 != 2 AND Q10 = 3|8 (11.0/3.0)
Q2 != 2 AND Q21 != 2 AND Q16 != 2 AND Q25 != 2 AND Q9 = 2 AND Q16 != 3|5 (10.0/5.0)
Q2 != 2 AND Q21 = 2|3 (9.0/5.0)
Q18 != 2 AND Q16 != 2 AND Q25 != 2 AND Q23 = 2|3 (16.0/11.0)
Q21 != 2 AND Q26 = 2|9 (17.0/12.0)
Q21 != 2 AND Q18 = 2 AND Q28 = 4|4 (12.0/9.0)
Q21 != 2 AND Q18 != 2 AND Q8 != 2 AND Q10 != 2 AND Q11 != 2 AND Q27 != 2 AND nb.repeat != 3 AND Q7 != 2 AND Q3 = 2|5 (17.0/11.0)
Q21 != 2 AND Q18 != 2 AND Q3 = 2 AND Q4 = 2 AND Q24 = 3|3 (14.0/10.0)
Q21 != 2 AND Q18 = 2|9 (12.0/7.0)
Q21 != 2 AND Q3 = 2 AND Q4 != 2|4 (10.0/6.0)
Q21 != 2 AND Q3 != 2 AND Q16 != 2 AND nb.repeat != 3 AND Q5 != 2 AND Q9 != 2 AND Q2 = 2 AND Q25 != 5|8 (16.0/10.0)
Q21 != 2 AND Q3 != 2 AND Q16 != 2 AND nb.repeat != 3 AND Q5 != 2 AND Q9 != 2 AND Q2 != 2 AND Q11 != 2 AND Q27 != 2 AND Q8 != 2 AND Q4 = 2|3 (17.0/12.0)
Q21 != 2 AND Q3 != 2 AND Q16 != 2 AND nb.repeat != 3 AND Q5 = 2|9 (15.0/10.0)
Q21 != 2 AND Q5 != 2 AND nb.repeat != 3 AND Q7 != 2 AND Q4 != 2 AND Q12 != 2 AND Q8 != 2 AND Q27 != 2 AND nb.repeat = 1 AND Q1 = 2 AND Q6 != 3|9 (15.0/7.0)
Q21 != 2 AND Q5 != 2 AND nb.repeat != 3 AND Q7 = 2 AND Q24 = 4|8 (10.0/5.0)
Q21 != 2 AND Q5 != 2 AND Q7 != 2 AND Q4 != 2 AND nb.repeat != 3 AND Q12 != 2 AND Q8 != 2 AND Q1 != 2 AND Q27 != 2 AND nb.repeat = 1 AND difficulty = 5 AND Q21 != 4 AND Q14 = 1|3 (16.0/10.0)
Q21 != 2 AND Q5 != 2 AND Q7 != 2 AND Q4 != 2 AND difficulty = 5 AND Q7 = 4|3 (18.0/11.0)
Q21 != 2 AND Q5 != 2 AND difficulty != 5 AND Q27 = 2|3 (16.0/7.0)
Q21 != 2 AND Q5 != 2 AND difficulty = 5|5 (12.0/5.0)
Q21 != 2 AND Q5 != 2 AND Q8 = 2 AND Q10 != 3|13 (10.0/7.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q14 != 1 AND difficulty = 1 AND Q22 = 5 AND Q8 = 5 AND attendance = 0|5 (94.0/71.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty = 1 AND Q10 != 1 AND Q22 = 5 AND attendance != 3|13 (14.0/5.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q1 = 2|3 (15.0/9.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q14 != 1 AND nb.repeat = 2 AND Q15 = 3|13 (13.0/8.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q14 != 1 AND difficulty != 1 AND nb.repeat != 3 AND nb.repeat = 1 AND attendance != 0 AND difficulty != 3 AND attendance != 4 AND Q10 != 4 AND Q24 != 4 AND Q17 != 4 AND attendance = 3 AND Q18 != 5|5 (31.0/20.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q9 = 1 AND difficulty = 4|9 (13.0/8.0)
Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND Q13 = 1 AND difficulty != 1|3 (15.0/11.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty = 1 AND Q1 != 5 AND attendance != 3 AND Q8 = 3 AND attendance = 0|3 (153.0/99.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND attendance != 0 AND difficulty = 4 AND Q11 = 3 AND Q24 = 3 AND attendance != 1|3 (29.0/16.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND attendance != 0 AND nb.repeat != 3 AND nb.repeat = 1 AND difficulty = 4 AND attendance != 4 AND Q8 = 5 AND attendance != 3|5 (18.0/11.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND attendance != 0 AND nb.repeat != 3 AND nb.repeat = 1 AND difficulty = 4 AND attendance != 4 AND Q8 != 5 AND Q26 != 5 AND Q6 = 3 AND Q23 = 3|5 (22.0/12.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND attendance = 2 AND Q16 != 5 AND Q23 != 4 AND difficulty = 3|3 (28.0/13.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty != 1 AND nb.repeat != 3 AND nb.repeat = 1 AND Q25 = 4 AND Q16 != 3 AND Q11 != 3 AND Q1 != 3 AND Q22 = 4 AND attendance = 2 AND difficulty = 3|3 (27.0/12.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty != 1 AND nb.repeat != 3 AND nb.repeat = 1 AND Q25 = 4 AND Q16 != 3 AND Q28 = 4 AND Q3 != 3 AND Q11 = 4 AND attendance != 0 AND attendance = 2|3 (21.0/14.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty != 1 AND nb.repeat != 3 AND nb.repeat = 1 AND Q25 = 4 AND Q16 != 3 AND Q28 = 4 AND Q11 != 3 AND Q6 = 4 AND attendance != 0 AND attendance != 1 AND difficulty != 3|5 (27.0/17.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND difficulty = 1 AND Q1 != 5 AND attendance != 3 AND Q8 != 3 AND Q9 = 4|3 (106.0/74.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q1 = 4 AND Q17 != 3 AND Q10 != 3 AND Q12 != 3 AND Q6 = 4 AND Q27 = 4 AND attendance = 3|5 (29.0/19.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND Q2 = 4 AND Q11 = 3|3 (15.0/8.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND Q2 = 4 AND Q12 != 3 AND Q10 = 4 AND Q26 = 4 AND difficulty != 3 AND attendance = 1|5 (15.0/9.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND Q2 = 4 AND attendance != 2 AND Q12 != 3 AND Q10 = 4 AND Q26 = 4 AND difficulty != 3|5 (19.0/11.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q1 = 4 AND Q24 != 3 AND Q10 = 4 AND Q6 = 4 AND attendance != 1|13 (21.0/13.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q5 = 4 AND Q27 = 4 AND Q12 = 4 AND attendance = 1|8 (15.0/10.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q2 = 4 AND Q12 = 4|9 (16.0/10.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q2 != 4 AND Q7 != 4 AND Q4 != 4 AND Q8 != 4 AND Q16 != 4 AND attendance = 3 AND difficulty != 4 AND Q1 != 5 AND difficulty != 1|13 (22.0/11.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q2 != 4 AND Q7 != 4 AND Q4 != 4 AND Q8 != 4 AND Q16 != 4 AND attendance = 1 AND Q6 = 3 AND difficulty = 3|13 (22.0/15.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND nb.repeat = 1 AND Q2 = 4|5 (16.0/9.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND nb.repeat != 3 AND Q2 != 4 AND Q1 != 4 AND Q4 != 4 AND Q9 != 4 AND Q16 = 4|5 (17.0/10.0)
Q13 != 1 AND Q21 != 2 AND Q5 != 2 AND Q8 != 2 AND attendance = 1 AND Q1 = 3|3 (17.0/11.0)
attendance = 1 AND Q11 = 5|9 (10.0/5.0)
attendance != 1 AND Q16 != 1 AND Q3 != 2 AND Q8 != 2 AND Q23 = 4 AND nb.repeat != 1|9 (13.0/8.0)
attendance != 1 AND Q16 != 1 AND Q3 != 2 AND Q5 != 4 AND Q15 != 4 AND Q28 != 4 AND attendance = 2|3 (15.0/9.0)
attendance != 1 AND Q16 != 1 AND Q3 != 2 AND Q5 = 4|8 (13.0/6.0)
attendance != 1 AND Q16 != 1 AND Q9 != 2 AND Q9 != 4 AND attendance != 0 AND difficulty != 1 AND Q6 = 5 AND difficulty != 3|3 (22.0/14.0)
Q3 != 2 AND Q15 != 4 AND Q16 != 1 AND Q28 != 4 AND Q8 = 5 AND attendance != 0|3 (19.0/12.0)
Q3 != 2 AND Q15 != 4 AND Q28 != 4 AND Q16 != 1 AND Q8 = 5|9 (13.0/8.0)
attendance != 1 AND Q15 != 4 AND Q16 != 1 AND Q28 != 4 AND Q24 = 3 AND difficulty != 1 AND attendance = 0|9 (14.0/10.0)
attendance != 1 AND Q15 != 4 AND Q19 != 5 AND Q21 != 3|13 (17.0/6.0)
attendance != 0 AND attendance != 1 AND Q27 = 3 AND difficulty != 1|5 (15.0/9.0)
attendance = 0|8 (12.0/7.0)
Q15 != 4 AND Q4 = 3|13 (11.0/7.0)
Q15 = 4|9 (9.0/5.0)
|5 (9.0/7.0)


## J48 Decision Tree

* instr = 1
	* nb.repeat = 3: 7 (29.0/9.0)
	* nb.repeat != 3
		* difficulty = 4
			* Q18 = 2: 2 (10.0/5.0)
			* Q18 != 2
				* Q4 = 2: 7 (16.0)
				* Q4 != 2
					* Q1 = 2: 7 (11.0/3.0)
					* Q1 != 2
						* attendance = 2: 10 (14.0/7.0)
						* attendance != 2
							* Q1 = 5
								* attendance = 4: 10 (9.0/5.0)
								* attendance != 4: 2 (15.0/5.0)
							* Q1 != 5
								* Q17 = 5: 7 (10.0/2.0)
								* Q17 != 5
									* Q22 = 1: 7 (11.0/6.0)
									* Q22 != 1
										* Q28 = 4: 7 (36.0/22.0)
										* Q28 != 4: 10 (24.0/11.0)
		* difficulty != 4
			* difficulty = 5
				* Q21 = 4: 10 (13.0/6.0)
				* Q21 != 4
					* Q27 = 5: 10 (13.0/8.0)
					* Q27 != 5
						* attendance = 3: 7 (16.0/6.0)
						* attendance != 3
							* Q6 = 1: 7 (17.0/7.0)
							* Q6 != 1
								* Q9 = 3: 7 (11.0/3.0)
								* Q9 != 3: 10 (9.0/3.0)
			* difficulty != 5: 10 (429.0/108.0)
* instr != 1
	* instr = 2
		* difficulty = 4
			* Q17 = 1: 6 (12.0/2.0)
			* Q17 != 1: 11 (203.0/82.0)
		* difficulty != 4
			* difficulty = 5: 11 (78.0/38.0)
			* difficulty != 5
				* attendance = 1
					* Q27 = 5
						* Q9 = 5: 11 (18.0/10.0)
						* Q9 != 5: 6 (9.0/4.0)
					* Q27 != 5: 6 (159.0/76.0)
				* attendance != 1
					* Q15 = 2
						* Q14 = 2: 6 (40.0/15.0)
						* Q14 != 2: 11 (13.0/6.0)
					* Q15 != 2
						* Q23 = 2
							* Q7 = 2: 1 (9.0/5.0)
							* Q7 != 2: 6 (16.0/6.0)
						* Q23 != 2
							* Q13 = 2: 1 (14.0/9.0)
							* Q13 != 2
								* Q11 = 2: 1 (11.0/6.0)
								* Q11 != 2
									* Q16 = 2: 11 (9.0/3.0)
									* Q16 != 2
										* Q24 = 2: 13 (11.0/7.0)
										* Q24 != 2
											* Q9 = 2: 6 (13.0/5.0)
											* Q9 != 2
												* Q3 = 2
													* Q19 = 5: 13 (9.0/4.0)
													* Q19 != 5: 6 (13.0/8.0)
												* Q3 != 2
													* Q6 = 2
														* Q1 = 1: 6 (10.0/3.0)
														* Q1 != 1: 11 (19.0/6.0)
													* Q6 != 2
														* difficulty = 1
															* Q5 = 4
																* Q25 = 4
																	* attendance = 0: 11 (34.0/20.0)
																	* attendance != 0: 1 (14.0/9.0)
																* Q25 != 4: 6 (10.0/4.0)
															* Q5 != 4
																* Q25 = 4: 6 (10.0/4.0)
																* Q25 != 4
																	* Q23 = 5: 6 (47.0/30.0)
																	* Q23 != 5
																		* attendance = 0
																			* Q19 = 1: 6 (43.0/28.0)
																			* Q19 != 1: 11 (53.0/34.0)
																		* attendance != 0: 11 (12.0/6.0)
														* difficulty != 1
															* Q21 = 1: 11 (20.0/11.0)
															* Q21 != 1
																* Q2 = 1: 11 (9.0/5.0)
																* Q2 != 1
																	* Q1 = 1: 6 (15.0/6.0)
																	* Q1 != 1
																		* difficulty = 2
																			* Q25 = 5: 1 (20.0/12.0)
																			* Q25 != 5: 6 (62.0/26.0)
																		* difficulty != 2
																			* Q8 = 2: 1 (9.0/6.0)
																			* Q8 != 2
																				* attendance = 0
																					* Q13 = 5: 6 (9.0/1.0)
																					* Q13 != 5
																						* Q2 = 3: 6 (16.0/5.0)
																						* Q2 != 3: 11 (12.0/6.0)
																				* attendance != 0
																					* Q1 = 2: 6 (18.0/9.0)
																					* Q1 != 2
																						* Q16 = 3
																							* nb.repeat = 1
																								* attendance = 2: 11 (18.0/8.0)
																								* attendance != 2
																									* Q1 = 3: 6 (23.0/11.0)
																									* Q1 != 3: 1 (10.0/5.0)
																							* nb.repeat != 1: 11 (9.0/3.0)
																						* Q16 != 3: 6 (154.0/87.0)
	* instr != 2
		* nb.repeat = 1
			* Q17 = 1
				* Q9 = 5: 3 (10.0/8.0)
				* Q9 != 5
					* Q19 = 3: 13 (9.0/5.0)
					* Q19 != 3
						* difficulty = 2: 13 (11.0/2.0)
						* difficulty != 2
							* Q16 = 1
								* Q8 = 2: 5 (11.0/8.0)
								* Q8 != 2
									* Q21 = 1
										* Q2 = 1
											* difficulty = 3: 13 (22.0/12.0)
											* difficulty != 3
												* attendance = 2: 3 (9.0/6.0)
												* attendance != 2
													* attendance = 3: 3 (13.0/8.0)
													* attendance != 3
														* difficulty = 4: 3 (13.0/10.0)
														* difficulty != 4
															* attendance = 4: 13 (24.0/14.0)
															* attendance != 4
																* attendance = 0
																	* difficulty = 1: 13 (197.0/132.0)
																	* difficulty != 1: 5 (9.0/6.0)
																* attendance != 0: 3 (18.0/10.0)
										* Q2 != 1: 13 (14.0/5.0)
									* Q21 != 1: 3 (10.0/6.0)
							* Q16 != 1: 13 (9.0/4.0)
			* Q17 != 1
				* difficulty = 2
					* Q18 = 5: 13 (26.0/15.0)
					* Q18 != 5
						* Q25 = 5: 9 (12.0/7.0)
						* Q25 != 5
							* Q22 = 4
								* Q16 = 3: 9 (10.0/5.0)
								* Q16 != 3
									* attendance = 3: 13 (10.0/6.0)
									* attendance != 3
										* Q1 = 4: 5 (14.0/9.0)
										* Q1 != 4: 8 (9.0/5.0)
							* Q22 != 4: 13 (62.0/30.0)
				* difficulty != 2
					* Q4 = 1
						* Q21 = 2
							* Q26 = 2: 3 (13.0/7.0)
							* Q26 != 2: 4 (14.0/8.0)
						* Q21 != 2
							* Q2 = 4: 5 (9.0/4.0)
							* Q2 != 4
								* Q6 = 4: 8 (15.0/6.0)
								* Q6 != 4
									* Q22 = 2: 13 (9.0/4.0)
									* Q22 != 2
										* Q16 = 4: 13 (10.0/4.0)
										* Q16 != 4
											* difficulty = 5
												* Q14 = 3: 5 (10.0/6.0)
												* Q14 != 3: 8 (12.0/4.0)
											* difficulty != 5
												* Q6 = 2: 8 (10.0/2.0)
												* Q6 != 2
													* Q22 = 1: 4 (14.0/9.0)
													* Q22 != 1
														* difficulty = 1: 8 (14.0/8.0)
														* difficulty != 1
															* Q9 = 3: 4 (9.0/5.0)
															* Q9 != 3: 9 (12.0/5.0)
					* Q4 != 1
						* Q5 = 1
							* Q8 = 2: 5 (14.0/10.0)
							* Q8 != 2
								* Q21 = 3: 3 (12.0/8.0)
								* Q21 != 3
									* Q26 = 3: 8 (9.0/2.0)
									* Q26 != 3: 9 (11.0/4.0)
						* Q5 != 1
							* Q19 = 1
								* Q18 = 1: 3 (9.0/4.0)
								* Q18 != 1: 5 (10.0/5.0)
							* Q19 != 1
								* Q11 = 1
									* attendance = 2: 3 (14.0/6.0)
									* attendance != 2
										* Q28 = 4: 5 (15.0/4.0)
										* Q28 != 4
											* Q5 = 2: 3 (15.0/8.0)
											* Q5 != 2: 5 (15.0/7.0)
								* Q11 != 1
									* Q6 = 1
										* Q2 = 2: 13 (10.0/4.0)
										* Q2 != 2: 3 (9.0/5.0)
									* Q6 != 1
										* attendance = 4
											* Q15 = 2: 5 (22.0/12.0)
											* Q15 != 2
												* Q23 = 2: 8 (9.0/5.0)
												* Q23 != 2
													* Q9 = 2: 8 (10.0/5.0)
													* Q9 != 2
														* Q1 = 2: 8 (24.0/10.0)
														* Q1 != 2
															* difficulty = 5
																* Q7 = 4: 3 (9.0/4.0)
																* Q7 != 4
																	* Q12 = 3: 3 (14.0/6.0)
																	* Q12 != 3: 5 (11.0/5.0)
															* difficulty != 5
																* Q16 = 5
																	* difficulty = 1: 3 (10.0/6.0)
																	* difficulty != 1
																		* difficulty = 3: 13 (20.0/13.0)
																		* difficulty != 3: 3 (12.0/8.0)
																* Q16 != 5
																	* Q20 = 5: 8 (9.0/3.0)
																	* Q20 != 5
																		* Q12 = 2: 8 (9.0/3.0)
																		* Q12 != 2
																			* Q4 = 4
																				* Q8 = 4: 5 (50.0/33.0)
																				* Q8 != 4: 8 (10.0/5.0)
																			* Q4 != 4: 3 (40.0/23.0)
										* attendance != 4
											* Q26 = 1
												* Q15 = 3: 13 (9.0/5.0)
												* Q15 != 3: 9 (9.0/2.0)
											* Q26 != 1
												* difficulty = 5
													* Q8 = 2
														* Q26 = 2: 3 (19.0/9.0)
														* Q26 != 2: 8 (13.0/9.0)
													* Q8 != 2
														* attendance = 0: 3 (18.0/10.0)
														* attendance != 0
															* Q26 = 4: 3 (30.0/17.0)
															* Q26 != 4
																* attendance = 2: 3 (19.0/7.0)
																* attendance != 2
																	* Q9 = 5: 5 (10.0/4.0)
																	* Q9 != 5
																		* Q13 = 3
																			* attendance = 1: 3 (13.0/5.0)
																			* attendance != 1: 5 (20.0/12.0)
																		* Q13 != 3: 3 (13.0/7.0)
												* difficulty != 5
													* Q20 = 5
														* Q4 = 4
															* difficulty = 4: 5 (18.0/8.0)
															* difficulty != 4: 13 (19.0/10.0)
														* Q4 != 4
															* Q19 = 4: 8 (14.0/10.0)
															* Q19 != 4
																* Q7 = 3: 3 (13.0/8.0)
																* Q7 != 3
																	* attendance = 1: 5 (21.0/15.0)
																	* attendance != 1
																		* Q7 = 4: 13 (9.0/5.0)
																		* Q7 != 4
																			* Q5 = 5
																				* Q1 = 5
																					* attendance = 0
																						* difficulty = 1: 5 (90.0/69.0)
																						* difficulty != 1: 9 (10.0/6.0)
																					* attendance != 0: 3 (54.0/36.0)
																				* Q1 != 5: 13 (11.0/6.0)
																			* Q5 != 5: 5 (9.0/6.0)
													* Q20 != 5
														* Q21 = 5
															* Q23 = 3: 3 (9.0/4.0)
															* Q23 != 3
																* attendance = 0: 13 (9.0/5.0)
																* attendance != 0: 3 (9.0/4.0)
														* Q21 != 5
															* Q22 = 5: 5 (12.0/5.0)
															* Q22 != 5
																* Q24 = 5: 5 (9.0/4.0)
																* Q24 != 5
																	* Q3 = 5
																		* Q14 = 4: 5 (9.0/5.0)
																		* Q14 != 4: 13 (9.0/5.0)
																	* Q3 != 5
																		* Q5 = 5: 9 (10.0/5.0)
																		* Q5 != 5
																			* Q11 = 5: 9 (13.0/8.0)
																			* Q11 != 5
																				* difficulty = 1
																					* Q27 = 2
																						* Q9 = 3: 3 (10.0/8.0)
																						* Q9 != 3
																							* Q8 = 2: 5 (62.0/34.0)
																							* Q8 != 2: 3 (10.0/3.0)
																					* Q27 != 2
																						* Q25 = 2: 5 (10.0/6.0)
																						* Q25 != 2
																							* Q23 = 2: 8 (10.0/6.0)
																							* Q23 != 2
																								* attendance = 3: 9 (17.0/12.0)
																								* attendance != 3
																									* Q15 = 4
																										* Q22 = 3: 5 (11.0/5.0)
																										* Q22 != 3: 3 (115.0/83.0)
																									* Q15 != 4
																										* Q17 = 4: 3 (11.0/6.0)
																										* Q17 != 4
																											* Q9 = 2: 9 (10.0/6.0)
																											* Q9 != 2: 3 (184.0/120.0)
																				* difficulty != 1
																					* Q20 = 2
																						* Q13 = 2
																							* difficulty = 3: 9 (24.0/16.0)
																							* difficulty != 3: 13 (24.0/13.0)
																						* Q13 != 2: 3 (18.0/8.0)
																					* Q20 != 2
																						* Q16 = 2
																							* Q25 = 3: 9 (13.0/8.0)
																							* Q25 != 3: 8 (10.0/3.0)
																						* Q16 != 2
																							* Q17 = 5: 5 (15.0/9.0)
																							* Q17 != 5
																								* Q23 = 2: 3 (12.0/7.0)
																								* Q23 != 2
																									* Q26 = 2: 9 (10.0/6.0)
																									* Q26 != 2
																										* Q12 = 2: 5 (27.0/14.0)
																										* Q12 != 2
																											* Q5 = 2: 8 (10.0/5.0)
																											* Q5 != 2
																												* Q2 = 2: 4 (12.0/8.0)
																												* Q2 != 2
																													* Q8 = 2: 5 (10.0/7.0)
																													* Q8 != 2
																														* Q4 = 2: 3 (10.0/6.0)
																														* Q4 != 2
																															* Q1 = 2: 5 (14.0/10.0)
																															* Q1 != 2
																																* attendance = 2
																																	* difficulty = 3: 3 (57.0/26.0)
																																	* difficulty != 3
																																		* Q1 = 3: 3 (25.0/15.0)
																																		* Q1 != 3: 5 (21.0/12.0)
																																* attendance != 2
																																	* attendance = 0
																																		* Q13 = 3: 9 (14.0/10.0)
																																		* Q13 != 3: 5 (32.0/23.0)
																																	* attendance != 0
																																		* difficulty = 3
																																			* Q25 = 3: 13 (45.0/28.0)
																																			* Q25 != 3
																																				* attendance = 1: 8 (17.0/12.0)
																																				* attendance != 1: 3 (30.0/21.0)
																																		* difficulty != 3
																																			* Q1 = 4: 5 (42.0/24.0)
																																			* Q1 != 4
																																				* Q24 = 3
																																					* Q17 = 3: 5 (48.0/32.0)
																																					* Q17 != 3: 3 (9.0/4.0)
																																				* Q24 != 3: 5 (9.0/3.0)
		* nb.repeat != 1
			* attendance = 3
				* Q11 = 5: 8 (21.0/11.0)
				* Q11 != 5
					* Q8 = 2: 8 (9.0/5.0)
					* Q8 != 2
						* Q1 = 2: 9 (9.0/5.0)
						* Q1 != 2
							* Q21 = 3: 9 (22.0/11.0)
							* Q21 != 3
								* difficulty = 4: 8 (9.0/6.0)
								* difficulty != 4: 3 (25.0/18.0)
			* attendance != 3
				* Q11 = 1
					* difficulty = 5: 13 (22.0/10.0)
					* difficulty != 5
						* nb.repeat = 2: 13 (35.0/15.0)
						* nb.repeat != 2
							* difficulty = 3: 8 (13.0/7.0)
							* difficulty != 3
								* difficulty = 1: 13 (13.0/8.0)
								* difficulty != 1: 9 (13.0/6.0)
				* Q11 != 1
					* Q10 = 1: 13 (10.0/7.0)
					* Q10 != 1
						* difficulty = 5
							* Q2 = 2: 4 (10.0/7.0)
							* Q2 != 2: 13 (49.0/26.0)
						* difficulty != 5
							* Q21 = 3
								* Q22 = 4: 9 (9.0/6.0)
								* Q22 != 4
									* Q17 = 3
										* attendance = 2
											* difficulty = 4: 3 (9.0/5.0)
											* difficulty != 4: 9 (15.0/9.0)
										* attendance != 2
											* difficulty = 1: 3 (18.0/11.0)
											* difficulty != 1
												* Q9 = 3
													* attendance = 0: 9 (33.0/18.0)
													* attendance != 0: 13 (39.0/24.0)
												* Q9 != 3: 13 (9.0/5.0)
									* Q17 != 3: 3 (9.0/4.0)
							* Q21 != 3
								* Q16 = 1: 9 (10.0/5.0)
								* Q16 != 1
									* Q22 = 3: 9 (14.0/9.0)
									* Q22 != 3
										* Q23 = 3: 9 (10.0/5.0)
										* Q23 != 3
											* Q3 = 3
												* Q18 = 4: 8 (12.0/8.0)
												* Q18 != 4: 13 (9.0/4.0)
											* Q3 != 3
												* Q5 = 3: 3 (9.0/4.0)
												* Q5 != 3
													* difficulty = 4
														* Q12 = 4
															* nb.repeat = 2: 13 (9.0/6.0)
															* nb.repeat != 2: 5 (9.0/4.0)
														* Q12 != 4
															* Q1 = 2: 9 (12.0/7.0)
															* Q1 != 2: 3 (9.0/3.0)
													* difficulty != 4
														* Q1 = 2
															* attendance = 1: 3 (11.0/8.0)
															* attendance != 1: 8 (14.0/8.0)
														* Q1 != 2
															* difficulty = 1: 3 (15.0/10.0)
															* difficulty != 1
																* attendance = 1
																	* Q7 = 4: 9 (11.0/7.0)
																	* Q7 != 4: 8 (10.0/5.0)
																* attendance != 1
																	* attendance = 4: 3 (13.0/9.0)
																	* attendance != 4
																		* Q4 = 4: 9 (16.0/9.0)
																		* Q4 != 4
																			* nb.repeat = 2: 8 (13.0/7.0)
																			* nb.repeat != 2: 13 (10.0/6.0)


## SimpleCart Decision Tree

* instr=(3)
		* nb.repeat=(3)|(2): 13(167.0/450.0)
		* nb.repeat!=(3)|(2)
			* Q21=(5)|(4)
				* Q1=(5)|(4): 3(195.0/556.0)
				* Q1!=(5)|(4): 8(140.0/291.0)
			* Q21!=(5)|(4): 3(430.0/1001.0)
* instr!=(3)
		* instr=(2)|(3)
			* difficulty=(5)|(4): 11(162.0/131.0)
			* difficulty!=(5)|(4): 6(419.0/581.0)
		* instr!=(2)|(3)
			* difficulty=(5)|(4): 7(119.0/141.0)
			* difficulty!=(5)|(4): 10(323.0/110.0)


