# Copyright (c) [2023] [Edward Chalk]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import csv
import math

def read_lines_from_file(filename):
  with open(filename, 'r') as f:
    lines = f.readlines()
  # Append highest_sequence_len and pos_in_sequence columns to the lines in the text file
  return [{'line': line.strip(), 'highest_sequence_len': 0, 'pos_in_sequence': 0} for line in lines]

def write_lines_to_file(filename, lines):
  with open(filename, 'w') as f:
    f.write('\n'.join([entry['line'] for entry in lines if not entry.get('marked_for_deletion')]))

def print_csv_debug(lines):
  with open("debug.csv", "w", newline='') as csvfile:
    fieldnames = ['line', 'highest_sequence_len', 'pos_in_sequence', 'marked_for_deletion']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for line in lines:
      writer.writerow(line)

def find_and_mark_duplicates(lines):
    # Get the total number of lines in the input
    total_lines = len(lines)
    
    # Initialize a list to store deferred updates. This helps in identifying the longest sequence each line is part of.
    updates = []

    # Loop through possible sequence lengths, from 1 to half of the total number of lines
    for sequence_len in range(1, math.floor(total_lines // 2)):
        print ("\nLooking for sequences of length: ", sequence_len)

        # Initialize a dictionary to store sequences and their occurrences
        sequence_dict = {}
        
        # Find unique sequences and the indices at which they occur in the text file
        for i in range(0, total_lines - sequence_len + 1): #Loop through the lines in the text file, stop at the sequence length before the end of the file
            # Extract the current sequence from the lines
            find_sequence = tuple(lines[i:i + sequence_len])
            # Convert the sequence of dictionaries to a string representation
            sequence_str = " ".join([entry['line'] for entry in find_sequence])

            # If the sequence is not already in the dictionary, initialize its value as an empty list
            if sequence_str not in sequence_dict:
                sequence_dict[sequence_str] = []

            # Append the starting index of the current sequence to the list of its occurrences
            sequence_dict[sequence_str].append(i)

        for sequence, indices in sequence_dict.items(): # Identify sequences to be marked for deletion
            # If the sequence occurs more than once, process it
            if len(indices) > 1:
                # Iterate over the number of indices of the sequence occurrences
                num_contiguous_sequences = 0
                for j in range(len(indices)):
                    # If the next sequence is contiguous with the current one
                    # then mark the current sequence for deletion
                    # if it isn't the first contigious sequence identified
                    #if indices[j] + sequence_len == indices[j + 1]:
                    if (j + 1 < len(indices) and indices[j] + sequence_len == indices[j + 1]) or (indices[j] - sequence_len == indices[j - 1]):
                        #Increment the number of contiguous sequences
                        num_contiguous_sequences += 1                        
                        #Loop through each line
                        for k in range(indices[j], indices[j] + sequence_len):
                            #If this line has already been categorised for a sequence of the same length, then skip the sequence
                            #(I.e. if one line fits into 2 sequences of the same length then only process the first sequence.)
                            if lines[k]['highest_sequence_len'] == sequence_len:
                               break
                            lines[k]['highest_sequence_len'] = sequence_len
                            lines[k]['pos_in_sequence'] = num_contiguous_sequences
                            if j + 1 > len(indices):
                              lines[k + sequence_len]['highest_sequence_len'] = sequence_len
                              lines[k + sequence_len]['pos_in_sequence'] = num_contiguous_sequences + 1
                            if num_contiguous_sequences > 1:
                              lines[k]['marked_for_deletion'] = True
                              if j + 1 > len(indices):
                                  lines[k + sequence_len]['marked_for_deletion'] = True
                            else:
                              lines[k]['marked_for_deletion'] = False
                    else: #We break the series of contigious sequences
                      num_contiguous_sequences = 0

def main():
  input_filename = "input.txt"
  output_filename = "output.txt"
  lines = read_lines_from_file(input_filename)
  find_and_mark_duplicates(lines)
  print_csv_debug(lines)
  write_lines_to_file(output_filename, lines)

if __name__ == "__main__":
  main()
