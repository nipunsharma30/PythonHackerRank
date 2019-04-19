def split_and_join(line):
    # write your code here
    # l = line.replace(" ", "-")  
    l = line.split()
    l = "-".join(l)
    return l