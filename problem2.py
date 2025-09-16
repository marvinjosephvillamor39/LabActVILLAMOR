# ---------------- Tower of Hanoi ----------------
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)

print("=== Tower of Hanoi ===")
n = int(input("Enter number of disks: "))
print("Steps:")
tower_of_hanoi(n, 'A', 'C', 'B')

print("\n=== Bubble Sort ===")
arr = [5, 2, 6, 4, 1]   # you can change this list
print("Input values =", arr)

n = len(arr)
for i in range(n-1):
    for j in range(n-1-i):
        print(f"Items compared: [{arr[j]}, {arr[j+1]}]", end=" ")
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print("➔ swapped", arr)
        else:
            print("➔ not swapped")
    print(f"Iteration #{i+1}", arr)

print("Output values =", arr)

