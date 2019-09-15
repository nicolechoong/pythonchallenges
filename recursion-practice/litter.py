import os

def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def litter(path, prefix = ""):
    """ Print recursive listing of contents of path """
    if prefix == "":  # Detect outermost call, print a heading
        file = open(path+"/litter.txt","w")
        file.close()

    dirlist = get_dirlist(path)
    for f in dirlist:
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            litter(fullname, prefix + "| ")
            file = open(fullname+"/litter.txt","w")
            file.close()


litter("/Users/nicole/Downloads/test")
