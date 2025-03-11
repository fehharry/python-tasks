import re
Matricule = r"^(UBA|UBa)+\d{2}[a-zA-z]{2,5}\d{2,4}$"
if re.fullmatch(Matricule,"UBa24PP0635"):
    print("valid")
else:
    print("invalid")
