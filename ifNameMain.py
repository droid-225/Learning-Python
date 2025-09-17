# if __name__ == '__main__'
# 1. Module can be run as standalone program
# 2. Module can be imported and used by other modules
# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it's the initial module being run

#import ifNameMain2

#print(__name__) # __main__
#print(ifNameMain2.__name__) # imported module name is the name of the module

def main():
    print("Hello!")

if __name__ == '__main__': # tests if this module is being run directly or indirectly
    #print("running this module directly")
    main()
#else:
#    print("running this other module indirectly")