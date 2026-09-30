with open("app.log") as f:
    lines = f.readlines()
    for line in lines:
        print(line.rstrip())