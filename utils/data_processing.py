import random

def shuffle_data(file1, file2):
    # Open the input files in read mode
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        # Read the lines from both files
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Ensure that both files have the same number of lines
        assert len(lines1) == len(lines2), "Files must have the same number of lines"

        # Combine the lines from both files and shuffle them
        combined = list(zip(lines1, lines2))
        random.shuffle(combined)
        lines1[:], lines2[:] = zip(*combined)

    # Open the output files in write mode and write the shuffled lines back
    with open(file1, 'w', encoding='utf-8') as f:
        f.writelines(lines1)
    with open(file2, 'w', encoding='utf-8') as f:
        f.writelines(lines2)


def split_data(file1, file2, train_ratio=0.8, val_ratio=0.1):
    # Open the input files in read mode
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        # Read the lines from both files
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        # Ensure that both files have the same number of lines
        assert len(lines1) == len(lines2), "Files must have the same number of lines"

        # Calculate split indices based on the ratios
        split_index1 = int(len(lines1) * train_ratio)
        split_index2 = int(len(lines1) * (train_ratio + val_ratio))

        # Split the lines into train, validation, and test sets
        train_lines1 = lines1[:split_index1]
        val_lines1 = lines1[split_index1:split_index2]
        test_lines1 = lines1[split_index2:]
        train_lines2 = lines2[:split_index1]
        val_lines2 = lines2[split_index1:split_index2]
        test_lines2 = lines2[split_index2:]

    # Write the split lines to their respective output files
    with open('dialogue_text/train.prediction', 'w', encoding='utf-8') as f:
        f.writelines(train_lines1)
    with open('dialogue_text/val.prediction', 'w', encoding='utf-8') as f:
        f.writelines(val_lines1)
    with open('dialogue_text/test.prediction', 'w', encoding='utf-8') as f:
        f.writelines(test_lines1)
    with open('dialogue_text/train.learning', 'w', encoding='utf-8') as f:
        f.writelines(train_lines2)
    with open('dialogue_text/val.learning', 'w', encoding='utf-8') as f:
        f.writelines(val_lines2)
    with open('dialogue_text/test.learning', 'w', encoding='utf-8') as f:
        f.writelines(test_lines2)


if __name__ == '__main__':
    # Define the input file paths
    file1 = 'dialogue_text/prediction'
    file2 = 'dialogue_text/learning'

    # Shuffle and split the data
    shuffle_data(file1, file2)
    split_data(file1, file2)
