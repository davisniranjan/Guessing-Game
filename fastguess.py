def fguesser(resp,max):
  if not hasattr(fguesser, "left"):
    # Minimum value
    fguesser.left = 2
    # Maximum value
    fguesser.right = max
  else:
    if resp == "l" or resp == "L":
      fguesser.right = fguesser.mid - 1
    else:
      fguesser.left = fguesser.mid + 1
 
  fguesser.mid = (fguesser.left + fguesser.right) // 2
  return fguesser.mid
