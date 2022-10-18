import time

from matplotlib.pyplot import bar

def progress_bar(part, total, lenght=30):
    frac=part/total
    completed=int(frac*lenght)
    missing=lenght-completed
    bar=f"[{'#'*completed}{'-'*missing}]{frac:.2%}"
    return bar
n=30
for i in range(n+1):
    time.sleep(2)
    print(progress_bar(i,n),end='\r')