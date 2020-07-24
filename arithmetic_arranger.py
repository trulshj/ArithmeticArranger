def arithmetic_arranger(problems):
  
  line1, line2, line3 = "", "", ""
  
  for problem in problems:
    n1, op, n2 = problem.split(" ")
    top = " " * (6-len(n1)) + n1
    top = op + " " * (5-len(n2)) + n2
    bot = "-" * len(max(len(top), len(mid)))

    line1 += top + "    "
    line2 += mid + "    "
    line3 += bot + "    "

    print("apple")

  arranged_problems = line1 + "\n" + line2 + "\n" + line3
  return arranged_problems