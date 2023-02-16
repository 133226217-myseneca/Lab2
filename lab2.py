import sys

def print_args():
    script_name = sys.argv[0]
    args = ' '.join(sys.argv[1:])
    print("Script name:", script_name)
    print("Script and variables:", script_name + ' ' + args)

print_args()

def helloWorld():
    print('Hello World')

helloWorld()

