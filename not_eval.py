class Test():
    def execute(self, method_name):
        method = eval(method_name)
        methodrun = method(' World!')    

    def send_method(self):
        for version in xrange(1,5): 
            version = str(version) #test each version of the algorithm, version = 1, 2, 3, 4
            method = 'self.'+'p'+version
            self.execute(method)

    def p1(self,n):
        print "Hello"+n
    def p2(self,n):
        print "Hello2"+n
    def p3(self, n):
        print "Hello3"+n
    def p4(self,n):
        print "Hello4"+n
    def p5(self,n):
        print "Hello5"+n


if __name__ == '__main__':
    test = Test()
    test.send_method()