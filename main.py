from linked_list import LinkedList

if __name__ == "__main__":
    print("=== Linked List Recursive Operations Demo ===\n")

    # 1. Initialize and create the linked list with integer IDs
    my_list = LinkedList()
    initial_ids = [10, 25, 42, 7, 19]
    
    print(f"Loading initial IDs into the list: {initial_ids}")
    for item in initial_ids:
        my_list.insert_at_end(item)

    print(f"Current Linked List: {my_list.display()}\n")

    # 2. Sum all node data using recursion
    total_sum = my_list.recursive_sum()
    print(f"-> Sum of all ID data: {total_sum}\n")

    # 3. Search for IDs using recursion
    search_target_yes = 42
    search_target_no = 99
    
    found_yes = my_list.recursive_search(search_target_yes)
    found_no = my_list.recursive_search(search_target_no)
    
    print(f"-> Searching for ID {search_target_yes}: {'Found!' if found_yes else 'Not Found.'}")
    print(f"-> Searching for ID {search_target_no}: {'Found!' if found_no else 'Not Found.'}\n")

    # 4. Reverse the list in-place using recursion
    print("Reversing the linked list in-place...")
    my_list.recursive_reverse()
    print(f"-> Reversed Linked List: {my_list.display()}")
    


# 