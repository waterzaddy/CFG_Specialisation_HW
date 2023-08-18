from collections import deque


def reorder_queue(input_file):
    queue = deque()
    with open("hw3_q1.txt", "r") as source_file:
        for line in source_file:
            words = line.split()
            jump_or_join = words[0]
            name = words[1]

            if jump_or_join == "JUMP":
                queue.appendleft(name)
            elif jump_or_join == "JOIN":
                queue.append(name)

    return queue


def main():
    input_file = "hw3_q1.txt"
    final_queue_order = reorder_queue(input_file)
    for person in final_queue_order:
        print(person)


if __name__ == "__main__":
    main()

"""
Time and space complexity is O(n).
This is because the for loop is O(2n) which is just O(n)
"""