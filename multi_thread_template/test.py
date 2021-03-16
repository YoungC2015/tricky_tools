import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        save_name = "tmp.pkl"
    else:
        save_name = sys.argv[1]
    print(save_name)
