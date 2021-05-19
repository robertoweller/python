from sklearn import tree

x = [[140, 1], [130, 1], [150, 0], [170, 0]]
y = [5, 5, 10, 10]

c = tree.DecisionTreeClassifier()
c = c.fit(x, y)

print(c.predict([[150, 1]]))