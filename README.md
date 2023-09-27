# remove_duplicate_lines_and_sequences_from_text_file
You can use this Python script to remove duplicate lines and sequences from a text file.

## Input file
The script looks for an input file called input.txt, this can be changed in the main function, if required.

## Example output
The following table shows a sample input file on the left hand side, and the output file on the right hand side. Lines in original file that are kept are coloured green, lines that are discarded because they form parts of duplicate sequences are coloured red.

![image](https://github.com/edwardchalk/remove_duplicate_lines_and_sequences_from_text_file/assets/144559018/cc9ce630-eca2-4c18-b26a-27551a3a58ff)

## Debug file
In addition to an output file, the script also generates a debug file so you can see why each line was kept or removed.

![image](https://github.com/edwardchalk/remove_duplicate_lines_and_sequences_from_text_file/assets/144559018/4c16a108-ae17-4606-8fd2-cc6dd983e47a)

highest_sequence_len is the longest sequence of which this line is a part.
pos_in_sequence is the position of the line in that sequence.

For example, here we have a sequence 4 lines long that occurs twice.

line	highest_sequence_len	pos_in_sequence	marked_for_deletion

![image](https://github.com/edwardchalk/remove_duplicate_lines_and_sequences_from_text_file/assets/144559018/144c01fc-0be1-4ba2-8c1e-ac591dc1ed23)

And here we have a sequence 1 line long that occurs 8 times.

![image](https://github.com/edwardchalk/remove_duplicate_lines_and_sequences_from_text_file/assets/144559018/9f89ba99-8506-4a57-8204-6466b27ffac1)
