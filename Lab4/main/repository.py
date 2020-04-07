class Repository:
    def readNet(self, fileName):
        f = open(fileName, "r")
        net = {}
        n = int(f.readline())
        net['noNodes'] = n
        mat = []
        for i in range(n):
            mat.append([])
            line = f.readline()
            elems = line.split(" ")
            for j in range(n):
                mat[-1].append(int(elems[j]))
        net["mat"] = mat
        degrees = []
        noEdges = 0
        for i in range(n):
            d = 0
            for j in range(n):
                if (mat[i][j] == 1):
                    d += 1
                if (j > i):
                    noEdges += mat[i][j]
            degrees.append(d)
        net["noEdges"] = noEdges
        net["degrees"] = degrees
        f.close()
        return n, net
