import os
if os.path.exists("thetext.mp3"):
  os.remove("thetext.mp3")
  print("deleted")
else:
  print("The file does not exist")