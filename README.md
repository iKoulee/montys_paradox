# Does Montys paradox really works?

Usage: ./paradox.py [True|False] [<integer>]

 * First argument tell if you want to change option
   after revealing one doors
 * Second argument is number of repetition

## Some test results

$ ./paradox.py false 10000
 ('Do we change a pick?', False)
 We will play 10000 times
 Wictory rate: 33.18% 
 Lose rate: 66.82%

$ ./paradox.py true 10000
('Do we change a pick?', True)
We will play 10000 times
Wictory rate: 66.65%
Lose rate: 33.35%

