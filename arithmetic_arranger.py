def arithmetic_arranger(problems, solve=False):
  
  if len(problems) > 5:
    return "Error: Too many problems."

  # A helper dict that makes handling string-form operations easier
  ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y)}

  # Create the lines that we will output
  line1, line2, line3, line4 = "", "", "", ""
  
  # Parse each problem
  for problem in problems:
    n1, op, n2 = problem.split(" ")

    # Error catching
    try:
      int(n1)
      int(n2)
    except ValueError:
      return "Error: Numbers must only contain digits."

    if len(n1) > 4 or len(n2) > 4:
      return "Error: Numbers cannot be more than four digits."

    if op not in ops.keys():
      return "Error: Operator must be '+' or '-'."

    # Figure out the whitespace needed for the top and middle cells
    t_pad = " " * (len(n2) - len(n1) + 2) if len(n2) > len(n1) else "  "
    m_pad = " " * (len(n1) - len(n2) + 1) if len(n1) > len(n2) else " "
    
    # Construct the cells needed
    top = f"{t_pad}{n1}"
    mid = f"{op}{m_pad}{n2}"
    bot = "-" * max(len(top), len(mid))
    
    # Add cells to their respective lines
    line1 += top + "    "
    line2 += mid + "    "
    line3 += bot + "    "
  
    # Do the same for the answers if we need them
    if solve:
      n3 = ops[op](int(n1), int(n2)) 
      ans = " " * (len(bot)-len(str(n3))) + str(n3)
      line4 += ans + "    "

  # Strip off trailing whitespace, 
  # not using .strip() because we want to keep some leading whitespace
  line1 = line1[:-4]
  line2 = line2[:-4]
  line3 = line3[:-4]

  # Combine the lines into a single string
  arranged_problems = line1 + "\n" + line2 + "\n" + line3

  # Add the answer line if needed
  if solve:
    line4 = line4[:-4]
    arranged_problems += "\n" + line4
  
  return arranged_problems