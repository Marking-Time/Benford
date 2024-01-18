# Benford.py
### Code to explore the Benfords law paradox
- Code creates 1000 random numbers and then calculates the occurance of each digit "1", "2", or "3"
- According to Benford the results should be something like 30.1%, 16.7% and 12.5%
- Code is expected to calculate to an average of 602.2.  The code calculated with randint varies with the run, but is usually in the low 300s.  This does not confirm Benfords law.
- Possible Inconsistency:
  The calculated code doesn't approach 300 (the theoretical prediction) and hovers in the 320-350 range. This may be because the first number can never be 0, while the remaining numbers can include 0.