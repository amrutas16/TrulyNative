from sklearn.ensemble import RandomForestClassifier
import re
import glob
#from textblob import TextBlob

# values = []
# X = []
# Y = []
# X_test = []
# rfc = RandomForestClassifier(n_jobs=-1)

def extract_features(file_path):
    file = open(file_path, 'r')
    text = file.read()
    values = []
    values.append(text.count('\n'))
    values.append(text.count(' '))
    values.append(text.count('\t'))
    values.append(text.count('{'))
    values.append(text.count('['))
    values.append(len(re.split('\s+', text)))
    values.append(len(text))
    values.append(text.count('<'))
    values.append(text.count('('))
    values.append(len(re.split('\w+', text)))
    values.append(text.count('\n\t'))
    values.append(text.count('//'))
    values.append(text.count('/'))
    values.append(text.count('<!'))
    values.append(text.count('/>'))
    values.append(text.count('&'))
    values.append(text.count(';'))
    values.append(text.count('=='))
    values.append(text.count('==='))
    values.append(text.count('css'))
    values.append(text.count('#'))
    values.append(text.count('@'))
    values.append(text.count('$'))
    values.append(text.count('%'))
    values.append(text.count('^'))
    values.append(text.count('+'))
    values.append(text.count('?'))
    values.append(text.count('|'))
    values.append(text.count('\\'))
    values.append(text.count('*'))
    values.append(text.count('||'))
    values.append(text.count('\t\t'))
    values.append(text.count('\t\t\t'))

    return values

def build_train_data(train_directory, classes):
    train_data = []
    train_classes = []
    for each_class in classes.keys():
        print('Processing files of class '+each_class)
        train_files = glob.glob(train_directory + '/' + each_class + '/*.txt')
        for index, each_train_file in enumerate(train_files):
            train_data.append(extract_features(each_train_file))
            train_classes.append(classes[each_class])
            print(str(index)+' Extracted features from '+each_train_file)

    return train_data, train_classes

def build_test_data(test_directory):
    test_data = []
    test_files = glob.glob(test_directory + '/*.txt')
    for index, each_test_file in enumerate(test_files):
        test_data.append(extract_features(each_test_file))
        print(str(index)+' Extracted features from '+each_test_file)

    return test_data

def random_forest_classifier(train_directory, classes):
    print('RANDOM FOREST CLASSIFIER')
    X_train, Y_train = build_train_data(train_directory, classes)
    rfc = RandomForestClassifier(n_jobs=-1)
    rfc = rfc.fit(X_train, Y_train)
    return rfc


#
# def getFeatures(train_directory):
#     rowNum = 0
#     #print('Output dir is ' + outputDir)
#     #filepaths0 = glob.glob('D:/Amruta/NCSU/Fall_2015/ALDA/Project/Dataset/unsponsored/*.txt')
#     #filepaths1 = glob.glob('D:/Amruta/NCSU/Fall_2015/ALDA/Project/Dataset/sponsored/*.txt')
#
#     filepaths0 = glob.glob(train_directory + '/unsponsored/*.txt')
#     filepaths1 = glob.glob(train_directory + '/sponsored/*.txt')
#
#     global X, Y
#
#     for fp in filepaths0:
#         myfile = open(fp)
#         text = myfile.read()
#         values = []
#         values.append(text.count('\n'))
#         values.append(text.count(' '))
#         values.append(text.count('\t'))
#         values.append(text.count('{'))
#         values.append(text.count('['))
#         values.append(len(re.split('\s+', text)))
#         values.append(len(text))
#         values.append(text.count('<'))
#         values.append(text.count('('))
#         values.append(len(re.split('\w+', text)))
#         values.append(text.count('\n\t'))
#         values.append(text.count('//'))
#         values.append(text.count('/'))
#         values.append(text.count('<!'))
#         values.append(text.count('/>'))
#         values.append(text.count('&'))
#         values.append(text.count(';'))
#         values.append(text.count('=='))
#         values.append(text.count('==='))
#         values.append(text.count('css'))
#         values.append(text.count('#'))
#         values.append(text.count('@'))
#         values.append(text.count('$'))
#         values.append(text.count('%'))
#         values.append(text.count('^'))
#         values.append(text.count('+'))
#         values.append(text.count('?'))
#         values.append(text.count('|'))
#         values.append(text.count('\\'))
#         values.append(text.count('*'))
#         values.append(text.count('||'))
#         values.append(text.count('\t\t'))
#         values.append(text.count('\t\t\t'))
#         #X[rowNum] = values
#         X.append(values.copy())
#         #global Y
#         #Y[rowNum] = 0
#         Y.append(0)
#         ++rowNum
#
#     for fp in filepaths1:
#         #print('Filepath 1')
#         myfile = open(fp)
#         text = myfile.read()
#         values = []
#         values.append(text.count('\n'))
#         values.append(text.count(' '))
#         values.append(text.count('\t'))
#         values.append(text.count('{'))
#         values.append(text.count('['))
#         values.append(len(re.split('\s+', text)))
#         values.append(len(text))
#         values.append(text.count('<'))
#         values.append(text.count('('))
#         values.append(len(re.split('\w+', text)))
#         values.append(text.count('\n\t'))
#         values.append(text.count('//'))
#         values.append(text.count('/'))
#         values.append(text.count('<!'))
#         values.append(text.count('/>'))
#         values.append(text.count('&'))
#         values.append(text.count(';'))
#         values.append(text.count('=='))
#         values.append(text.count('==='))
#         values.append(text.count('css'))
#         values.append(text.count('#'))
#         values.append(text.count('@'))
#         values.append(text.count('$'))
#         values.append(text.count('%'))
#         values.append(text.count('^'))
#         values.append(text.count('+'))
#         values.append(text.count('?'))
#         values.append(text.count('|'))
#         values.append(text.count('\\'))
#         values.append(text.count('*'))
#         values.append(text.count('||'))
#         values.append(text.count('\t\t'))
#         values.append(text.count('\t\t\t'))
#         #X[rowNum] = values
#         #Y[rowNum] = 1
#         X.append(values.copy())
#         Y.append(1)
#         ++rowNum
#
# def getTestFeatures(test_directory, testfile):
#     filepaths0 = glob.glob(test_directory+'/'+testfile)
#     for fp in filepaths0:
#         rowNum = 0
#         myfile = open(fp)
#         text = myfile.read()
#         values = []
#         values.append(text.count('\n'))
#         values.append(text.count(' '))
#         values.append(text.count('\t'))
#         values.append(text.count('{'))
#         values.append(text.count('['))
#         values.append(len(re.split('\s+', text)))
#         values.append(len(text))
#         values.append(text.count('<'))
#         values.append(text.count('('))
#         values.append(len(re.split('\w+', text)))
#         values.append(text.count('\n\t'))
#         values.append(text.count('//'))
#         values.append(text.count('/'))
#         values.append(text.count('<!'))
#         values.append(text.count('/>'))
#         values.append(text.count('&'))
#         values.append(text.count(';'))
#         values.append(text.count('=='))
#         values.append(text.count('==='))
#         values.append(text.count('css'))
#         values.append(text.count('#'))
#         values.append(text.count('@'))
#         values.append(text.count('$'))
#         values.append(text.count('%'))
#         values.append(text.count('^'))
#         values.append(text.count('+'))
#         values.append(text.count('?'))
#         values.append(text.count('|'))
#         values.append(text.count('\\'))
#         values.append(text.count('*'))
#         values.append(text.count('||'))
#         values.append(text.count('\t\t'))
#         values.append(text.count('\t\t\t'))
#         global X_test
#         X_test = values
#         #print(rowNum)
#         ++rowNum
#
#         #Y.append(0)
#
# def classify():
#     global rfc
#     print(len(X))
#     print(len(X[0]))
#     #print(len(X_test))
#     #print(len(X_test[0]))
#     print('--------------------------------------------------------------------------------')
#     print('Number of 1s in Y'+str(sum(1 for y in Y if y==1)))
#     print(len(Y))
#     #global X
#     #global Y
#     rfc = rfc.fit(X,Y)
#     #Y_predict = rfc.predict(X_test)
#     #return Y_predict
#
# def predict():
#     print('Length of X_test = ' + str(len(X_test)))
#     Y_predict = rfc.predict(X_test)
#     return Y_predict


'''
def main():
    getFeatures()
    getTestFeatures()
    classify()

main()
'''