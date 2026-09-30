with open   ("app.log") as f:
     lines = f.readlines()
     level_counts = {}
     for line in lines:
        counts = line.split()
        level = counts[2]
        level_counts[level] = level_counts.get(level, 0) + 1
for key, value in level_counts.items():
    print(f"{key}: {value}")

     