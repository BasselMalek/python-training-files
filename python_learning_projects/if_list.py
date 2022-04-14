#1ist
pc_components =["ram","mb","gpu","cpu"]
for component in pc_components:
    if (component == "ram"):
        print("unneeded")
    else:
        print("buy 1x")

#2lists
avalible_parts=pc_components[:]
requested_parts=["ram","case","mouse","kb"]
for part in requested_parts:
    if (part in avalible_parts):
        print("avalible")
    else:
        print("unavalible")
