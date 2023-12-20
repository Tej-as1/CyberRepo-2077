import os

def list_hidden_files(directory):
    hidden_files = [f for f in os.listdir(directory) if f.startswith('.')]
    return hidden_files

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")

    hidden_files = list_hidden_files(directory_path)

    if hidden_files:
        print("Hidden files in the directory:")
        for file in hidden_files:
            print(file)
    else:
        print("No hidden files found in the directory.")
