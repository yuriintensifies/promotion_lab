import regression_tree
import sys
import csv


def main(col_names=None):
    # parse command-line arguments to read the name of the input csv file
    # and optional 'draw tree' parameter
    if len(sys.argv) < 2:  # input file name should be specified
        print ("Please specify input csv file name")
        return

    csv_file_name = sys.argv[1]
    test_set = sys.argv[2]

    train = []
    test = []
    with open(csv_file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            train.append(list(row))
    with open(test_set) as csvfile:
        readtest = csv.reader(csvfile, delimiter=',')
        for row in readtest:
            test.append(list(row))

    print("Total number of records = ",len(train))
    tree = regression_tree.buildtree(train, min_gain=0.005, min_samples=5)

    #max_tree_depth = regression_tree.max_depth(tree)
    #print("max number of questions=" + str(max_tree_depth))

    if len(sys.argv) > 2: # draw option specified
        import dtree_draw
        dtree_draw.drawtree(tree, jpeg=csv_file_name+'.jpg')

    predictions = []
    actual = []
    for problem in test:
        predictions.append(regression_tree.classify(problem, tree))
        actual.append(problem[-1])
    for n, prediction in enumerate(predictions):
        if prediction < 0.6:
            predictions[n] = 0
        else:
            predictions[n] = 1

    with open('predictions.csv', 'w', newline='') as out:
        dwriter = csv.writer(out)
        dwriter.writerow(predictions)
        dwriter.writerow(actual)

if __name__ == "__main__":
    col_names = ['rank',
                 'ethnicity',
                 'gender',
                 'language',
                 'age',
                 'class_size',
                 'cls_level',
                 'bty_avg',
                 'prof_eval']
    main(col_names)





