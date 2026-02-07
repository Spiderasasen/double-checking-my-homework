# DFA String Checker (a/b Language)

This is a small Python program I wrote to help double‑check my DFA (Deterministic Finite Automaton) homework. It takes a string made of a and b, validates it, and then runs it through several different language checks based on the DFAs I sketched on paper.
What It Does

# The program asks the user for a string and then checks:

  -  Format Check  
    Makes sure the input only contains the letters a and b.

  -  Even/Odd Check  
    True if the string has an even number of a’s and an odd number of b’s.

  -  Minimum Length + Even A’s  
    True if the string has at least 3 characters and an even number of a’s.

  -  Every Second Symbol Is a  
    True if the string is at least length 2 and every second character is a.

  -  Symbol Has Appeared Before  
    True if both a and b appear at least once, and then a repeated symbol appears afterward.

  -  Ends With abab  
    Checks whether the string ends with the exact pattern abab.
