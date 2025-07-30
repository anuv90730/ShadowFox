justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Step 1: Original Justice League members:")
print(justice_league)
print("Number of members:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nStep 2: After adding Batgirl and Nightwing:")
print(justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("\nStep 3: After making Wonder Woman the leader:")
print(justice_league)

justice_league.remove("Green Lantern")

index_aqua = justice_league.index("Aquaman")
index_flash = justice_league.index("Flash")

insert_index = max(index_aqua, index_flash)
justice_league.insert(insert_index, "Green Lantern")
print("\nStep 4: After placing Green Lantern between Aquaman and Flash:")
print(justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nStep 5: After Superman assembles a new team:")
print(justice_league)

justice_league.sort()
print("\nStep 6: After sorting alphabetically:")
print(justice_league)
print("New leader is:", justice_league[0])