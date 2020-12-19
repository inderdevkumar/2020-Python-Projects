def check_symmetry(pth):
    symmtry_lines_list = []
    with open(pth, "r") as lines:
        new_lines = lines.readlines()
        print(new_lines)
check_symmetry("input.txt")          
