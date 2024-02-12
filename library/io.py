
def reader(path):
    with open(path) as f:
        contents = f.read()
        contents = contents.split("matrix\n")
        matrix = "".join(contents).split("vector\n")[0]
        vector = "".join(contents).split("vector\n")[1]
        matrix = "".join(matrix)
        vector = "".join(vector)
        matrix = transform_matrix(matrix)
        vector = transform_vector(vector)
        return matrix, vector
def transform_matrix(matrix):
    l = matrix.splitlines()
    for i in range(len(l)):
        l[i] = l[i].split()
    for i in range(len(l)):
        for j in range(len(l[0])):
            l[i][j] = float(l[i][j])
    return l


def transform_vector(vector):
    l = vector.split()
    for i in range(len(l)):
        l[i] = float(l[i])
    return l

def read_sequential_data(path, separator = "   "):
    """
    read_sequential_data: Function to read sequential data from a file
    
    args:
    path: The path to the file
    separator: The gap between each column
    """
    with open(path) as f:
        content = f.read().strip("\n").strip("\t").strip()
        content = content.split("\n")
        content = list(map(lambda x:list(map(lambda y:float(y), x.split(separator))), content))
        count = len(content[0])
        value =[]
        for i in range(count):
            temp =[]
            for j in range(len(content)):
                temp.append(content[j][i])
            value.append(temp)
        return value