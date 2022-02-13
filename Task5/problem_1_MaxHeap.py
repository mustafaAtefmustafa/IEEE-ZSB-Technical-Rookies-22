def main():
    heap = list(map(int, input().split()))
    print(f"Before max heapify {heap}")
    build_max_heap(heap)
    print(f"After max heapify {heap}")

def build_max_heap(heap):
    heap_size = len(heap)
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(heap, i, heap_size)

def max_heapify(heap, i, n):
    left = 2 * i + 1
    right = (2 * i) + 2
    if left < n and heap[left] > heap[i]:
        largest = left
    else:
        largest = i
    if right < n and heap[right] > heap[largest]:
        largest = right
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, largest, n)
    
if __name__ == '__main__':
    main()
