import random

# Initialize arrays
N = [0] * 100
A = [""] * 100

# Data (equivalent to the DATA lines in BASIC)
data = [
    'hefLin-d', 'shelby-d', 'murkowski-r', 'stevens-r', 'deconcini-d',
    'mccain-r', 'bumpers-d', 'pryor-d', 'boxer-d', 'feinstein-d', 'campbell-d',
    'brown-r', 'dodd-d', 'Lieberman-d', 'biden-d', 'roth-r', 'graham-d', 'mack-r',
    'nunn-d', 'coverdell-r', 'akaka-d', 'inouye-d', 'craig-r', 'kempthorne-r',
    'mosley-brown-d', 'simon-d', 'coats-r', 'lugar-r', 'harkin-d', 'grassley-r',
    'dole-r', 'kasselbaum-r', 'ford-d', 'mcconnell-r', 'breaux-d', 'johnston-d',
    'mitchell-d', 'cohen-r', 'mikulski-d', 'sarbanes-d', 'kennedy-d', 'kerry-d',
    'levin-d', 'riegel-d', 'wellstone-d', 'durenburger-r', 'cochran-r',
    'Lott-r', 'bond-r', 'danforth-r', 'bacus-d', 'burns-r', 'exon-d', 'kerrey-d',
    'bryan-d', 'reid-d', 'gregg-r', 'smith-r', 'bradley-d', 'lautenberg-d',
    'bingaman-d', 'domenici-r', 'moynihan-d', 'damato-r', 'faircloth-r',
    'helms-r', 'conrad-d', 'dorgan-d', 'glenn-d', 'metzenbaum-d', 'boren-d',
    'nickles-r', 'hatfield-r', 'packwood-r', 'wofford-d', 'specter-r',
    'pell-d', 'chafee-r', 'hollings-d', 'thurmond-r', 'daschle-d', 'pressler-r',
    'matthews-d', 'sasser-d', 'gramm-r', 'hutchinson-r', 'bennett-r', 'hatch-r',
    'Leahy-d', 'jeffords-r', 'robb-d', 'warner-r', 'murray-d', 'gorton-r',
    'byrd-d', 'rockefeller-d', 'feingold-d', 'kohl-d', 'simpson-r', 'wallop-r'
]

# Load data into A
for i in range(100):
    A[i] = data[i]

# Initialize counters
R = 0
D = 0

# Main loop
for i in range(60):
    while True:
        k = random.randint(1, 100) - 1  # Generate random number between 1 and 100 (adjusted for 0-based index)
        if N[k] == 0:  # If not already selected
            N[k] = 1
            print(k + 1, A[k])  # Print index (adjusted to be 1-based) and name

            # Check the last character
            z = A[k][-1]
            if z == 'd':
                D += 1
            elif z == 'r':
                R += 1
            break  # Exit the while loop once a valid K is found

# Print results
print("Results: ")
for i in range(100):
    print(N[i], end=" ")
print("\nDemocrats:", D, "Republicans:", R)