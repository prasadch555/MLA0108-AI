monkey = "door"
box = "window"
on_box = False

print("Monkey moves from door to window")
monkey = "window"

print("Monkey pushes box to center")
box = "center"
monkey = "center"

print("Monkey climbs the box")
on_box = True

if on_box and box == "center":
    print("Monkey grabs the bananas!")
else:
    print("Monkey cannot reach the bananas.")
