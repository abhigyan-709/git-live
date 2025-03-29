import fibo

def demo_dir(s):
    """
    This is the demo of the importing the custom python file or module, 
    so that we can demonstrate the dir function for the custom python file, by making an import
    """

    print(dir(s))

def main():
    demo_dir(s = fibo)
    print(demo_dir.__doc__)

if __name__ == "__main__":
    main()