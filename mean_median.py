""" Compute mean and median of a dataset without importing numpy"""


def mean(x):
      return sum(x) / len(x)

def median(x):
      z = len(x)
      if 2 & z == 0:
            return x[int(z/2)]
      else:
            return (x[int(z/2)]+x[int((z/2)+1)])/2


if __name__ == "__main__":
      x = [2.0,2.4 ,2.5 ,2.6, 2.6, 2.7, 2.7, 2.8 ,3.0, 3.1, 3.2 ,3.3 ,3.3, 3.4 ,3.4, 3.6, 3.6, 3.6, 3.6, 3.7 ,4.4, 4.6 ,4.7 ,4.8 ,5.3 ,10.1]
      print(f"Mean is: {round(mean(x),2)}",f"Median is: {median(x)}", sep = " | ")
      x.pop(0)
      x.pop(-1)
      trimmed_mean = x
      print(f"New mean is: {round(mean(trimmed_mean),2)}",f"New median is: {median(trimmed_mean)}", sep = " | ")
else:
      x = eval(input("Your dataset here: "))

