# split_data.py

def split_data(file1, file2, train_ratio=0.8, val_ratio=0.1):
    # Initialize the variables outside the 'with' block
    lines1 = None
    lines2 = None

    # Open and read the two input files
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Ensure both files have the same number of lines
        assert len(lines1) == len(lines2), "Files must have the same number of lines"

        # Calculate the split indices based on ratios
        split_index1 = int(len(lines1) * train_ratio)
        split_index2 = int(len(lines1) * (train_ratio + val_ratio))

        # Split the lines into training, validation, and test sets
        train_lines1 = lines1[:split_index1]
        val_lines1 = lines1[split_index1:split_index2]
        test_lines1 = lines1[split_index2:]
        train_lines2 = lines2[:split_index1]
        val_lines2 = lines2[split_index1:split_index2]
        test_lines2 = lines2[split_index2:]

    # Write the split data to separate output files
    with open('.../train_prediction1.txt', 'w', encoding='utf-8') as f:
        f.writelines(train_lines1)
    with open('.../val_prediction1.txt', 'w', encoding='utf-8') as f:
        f.writelines(val_lines1)
    with open('.../test_prediction1.txt', 'w', encoding='utf-8') as f:
        f.writelines(test_lines1)
    with open('.../train_learning.txt', 'w', encoding='utf-8') as f:
        f.writelines(train_lines2)
    with open('.../val_learning.txt', 'w', encoding='utf-8') as f:
        f.writelines(val_lines2)
    with open('.../test_learning.txt', 'w', encoding='utf-8') as f:
        f.writelines(test_lines2)

if __name__ == '__main':
    file1 = '.../prediction.txt'
    file2 = '.../learning.txt'
    split_data(file1, file2)
