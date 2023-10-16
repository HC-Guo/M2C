def remove_short_texts(input_prediction_ori, input_learning_ori, output_prediction, output_learning):
    # Specify the character encoding for file operations
    encoding = "utf-8"

    # Open input files and output files using context managers
    with open(input_prediction_ori, 'r', encoding=encoding) as file1, \
         open(input_learning_ori, 'r', encoding=encoding) as file2, \
         open(output_prediction, 'w', encoding=encoding) as output1, \
         open(output_learning, 'w', encoding=encoding) as output2:

        # Iterate through corresponding lines in file1 and file2
        for line1, line2 in zip(file1, file2):
            # Check if the line in file1 has at least 3 words
            if len(line1.split()) >= 3:
                # Write the line to the output files
                output1.write(line1)
                output2.write(line2)

if __name__ == "__main__":
    input_prediction_ori = 'dialogue_text/prediction_ori'
    input_learning_ori = 'dialogue_text/learning_ori'
    output_prediction = 'dialogue_text/prediction'
    output_learning = 'dialogue_text/learning'

    # Call the function from the main function
    remove_short_texts(input_prediction_ori, input_learning_ori, output_prediction, output_learning)
