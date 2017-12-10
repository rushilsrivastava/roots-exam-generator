import random

def createExam(prefixes, roots, suffixes):
    exam = []
    solution = []
    i = 25
    while i > 0:
        prefix = random.choice(prefixes).replace("\n", "")
        root = random.choice(roots).replace("\n", "")
        suffix = random.choice(suffixes).replace("\n", "")
        word = str(prefix + root + suffix).replace(" ", "")
        exam.append(word)
        solution.append("{} + {} + {}".format(prefix, root, suffix))
        i = i - 1

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

prefix = open('prefix.txt', 'r')
prefixes = [line.lower() for line in prefix]

root = open('root.txt', 'r')
roots = [line.lower() for line in root]

suffix = open('suffix.txt', 'r')
suffixes = [line.lower() for line in suffix]

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
createExam(prefixes, roots, suffixes)
print("Done! Exam and solutions saved to directory. Good luck!")
