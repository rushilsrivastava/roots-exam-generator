import random
import argparse

def createExam(prefixes, roots, suffixes, iterations):
    exam = []
    solution = []
    while iterations > 0:
        prefix = random.choice(prefixes).replace("\n", "")
        root = random.choice(roots).replace("\n", "")
        suffix = random.choice(suffixes).replace("\n", "")
        word = str(prefix + root + suffix).replace(" ", "")
        exam.append(word)
        solution.append("{} + {} + {}".format(prefix, root, suffix))
        iterations = iterations - 1

    examFile = open('exams/exam.txt', 'w')
    e = 0
    solutionFile = open('solutions/solution.txt', 'w')
    s = 0

    for word in exam:
        e = e + 1
        examFile.write("{}. {}\n".format(e, word))

    for answers in solution:
        s = s + 1
        solutionFile.write("{}. {}\n".format(s, answers))

if __name__ == "__main__":
    # parse command line options
    parser = argparse.ArgumentParser()
    parser.add_argument("words", help="Number of words to generate.", type=int)
    parser.add_argument("--hush", help="Prevent output. 0=false. 1=true.", nargs='?', const=0, type=int)
    args = parser.parse_args()

    # open datasets
    prefix = open('prefix.txt', 'r')
    prefixes = [line.lower() for line in prefix]

    root = open('root.txt', 'r')
    roots = [line.lower() for line in root]

    suffix = open('suffix.txt', 'r')
    suffixes = [line.lower() for line in suffix]

    # handle datasets
    if args.hush == 1:
        createExam(prefixes, roots, suffixes, args.words)
    else:
        print("Prefixes: {}".format(len(prefixes)))
        for prefix in prefixes:
            print("    {}".format(prefix))

        print("\n\n")

        print("Roots: {}".format(len(roots)))
        for root in roots:
            print("    {}".format(root))

        print("\n\n")

        print("Suffixes: {}".format(len(suffixes)))
        for suffix in suffixes:
            print("    {}".format(suffix))

        print("\n\n---------------------------------------------\n")

        print("Creating Exam...")
        createExam(prefixes, roots, suffixes, args.words)
        print("Done! Exam and solutions saved to directory. Good luck!")
