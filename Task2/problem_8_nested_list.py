def main():
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest = sorted(list(set([score for name, score in students])), reverse=True)[-2]   #making a set to remove duplicates.
    lowest_students = [name for name, score in sorted(students) if score == second_lowest]

    for i in lowest_students:
        print(i)


if __name__ == "__main__":
    main()
