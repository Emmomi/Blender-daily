import sys
with open("Blender-diary.md",mode='a') as f:
    text=sys.argv[1]
    f.write("\n"+str(text))

print("Done!")