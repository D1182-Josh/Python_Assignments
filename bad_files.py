    #TASK

                        
Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.
Examplesi
remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"

remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files: antivirus.exe, cat.pdf"

remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")
Notes

Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
Return "PC Files: Empty" if there are no files left on the computer.       

    #SOLUTION

def remove_virus(files) :
  files = files.split()
  bad_files = ["virus", "malware"]
  bad = [j for i in bad_files for j in files if (i in j) and ("anti" not in j  and "not" not in j)]
  for k in bad :
    files.remove(k)
  return " ".join(files)

remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")
... 'PC Files: antivirus.exe, cat.pdf,'


