import sys

def get_filename():

    if len(sys.argv) >=3:
        input1 = int(sys.argv[1])
        input2 = int(sys.argv[2])
        # name = sys.argv[1]
        # filename = sys.argv[1]
        # print(f"Hello {name}!!!! ")
        # return filename
        return input1 + input2
    else:
        print("[WARNING] you should run this program by calling: input1 input2")
        return -1

def read_from_file_to_list(filename):
    output
    with open("input.txt", "r") as file_to_read:
        file_to_read.readlines
        print(file_to_read.readlines())


def main():
    filename = get_filename()
    # if len(filename) == "":
    # if filename == "":
    #     return
    read_from_file_to_list("input.txt")
    # print(f"file to add: {filename}")



if __name__ == "__main__":
    main()