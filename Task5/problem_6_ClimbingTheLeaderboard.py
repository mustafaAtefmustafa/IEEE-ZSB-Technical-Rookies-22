from bisect import bisect, bisect_left, bisect_right


def main():
    n = int(input())
    ranked = sorted(set(map(int, input().split())))
    m = int(input())
    player = list(map(int, input().split()))
    for i in player:
        print(len(ranked)-bisect_right(ranked,i)+1)

    """This solution exceeds the time limit in some cases."""
   # for i in player:
   #     ranked.append(i)
    #    ranked = sorted(set(ranked), reverse=True)
     #   for j in range(len(ranked)):
      #      if i == ranked[j]:
       #         print(j + 1)
        #        break
        #ranked.remove(i)

if __name__ == '__main__':
    main()