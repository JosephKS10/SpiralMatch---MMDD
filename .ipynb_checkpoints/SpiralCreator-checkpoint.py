
def read_sequences(file_path):
    sequences = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line.startswith("-> "):
                    sequences.append(line[3:])  # Remove the "-> " prefix
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return sequences

# Specify the path to your input text file
file_path = "sequences.txt"

# Call the function to read the sequences
sequence_list = read_sequences(file_path)

# Print the extracted sequences
for i, sequence in enumerate(sequence_list, 1):
    print(f"Sequence {i}: {sequence}")