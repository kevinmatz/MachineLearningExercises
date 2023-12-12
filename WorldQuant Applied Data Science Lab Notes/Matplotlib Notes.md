# Notes on Matplotlib (PyPlot)

* Import
  * `import matplotlib.pyplot as plt`

* Line chart (with superimposed scatter plots):

```
my_X = [1, 2, 4, 7, 10]
my_Y = [1, 3, 6, 6, 14]
plt.plot(my_X, my_Y)
plt.scatter(
    my_X,
    my_Y,
    color="gray",
    marker="*",
    s=150   # size
)
plt.xlabel("Number of Cats in Household")
plt.ylabel("Number of Mice Caught in Week")
plt.title("Mice Caught Per Household");
```

![Graph image](images/Mice%20caught%20per%20household%20graph.png)
