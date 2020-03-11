from sklearn import tree

features = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]
classif =  tree.DecisionTreeClassifier()
classif = classif.fit(features, labels)

print classif.predict([150,0])