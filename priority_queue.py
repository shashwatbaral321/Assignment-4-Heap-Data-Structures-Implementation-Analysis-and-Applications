class Task:
    """
    Represents a task with a priority.
    Lower priority number means higher urgency.
    """
    def __init__(self, task_id, description, priority):
        self.id = task_id
        self.description = description
        self.priority = priority

    def __repr__(self):
        return f"Task(id={self.id}, desc='{self.description}', priority={self.priority})"

class MinPriorityQueue:
    """
    Implements a Min-Heap Priority Queue using a Python list.
    Stores Task objects.
    """
    
    def __init__(self):
        # self.heap[0] will store the root
        self.heap = []

    def is_empty(self):
        """Returns True if the queue is empty, False otherwise."""
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    # --- Helper functions for index arithmetic ---
    def _get_parent(self, i):
        return (i - 1) // 2
    
    def _get_left_child(self, i):
        return 2 * i + 1
    
    def _get_right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # --- Core Heap Operations ---

    def _bubble_up(self, i):
        """
        Moves an element up the heap to its correct position.
        Used after insertion or decrease_key.
        """
        parent_index = self._get_parent(i)
        
        # While we haven't reached the root and child < parent
        while i > 0 and self.heap[i].priority < self.heap[parent_index].priority:
            self._swap(i, parent_index)
            i = parent_index
            parent_index = self._get_parent(i)

    def _bubble_down(self, i):
        """
        Moves an element down the heap to its correct position.
        Used after extraction or increase_key. (Min-Heapify)
        """
        n = len(self.heap)
        min_index = i
        
        while True:
            left_index = self._get_left_child(i)
            right_index = self._get_right_child(i)
            
            smallest = i # Assume current node is smallest

            # Check if left child exists and is smaller
            if left_index < n and self.heap[left_index].priority < self.heap[smallest].priority:
                smallest = left_index
            
            # Check if right child exists and is smaller
            if right_index < n and self.heap[right_index].priority < self.heap[smallest].priority:
                smallest = right_index

            # If the smallest is no longer the current node, swap
            if smallest != i:
                self._swap(i, smallest)
                i = smallest # Move down to the new index
            else:
                # The element is in its correct place
                break

    # --- Public API ---

    def insert(self, task):
        """
        Inserts a new task into the priority queue.
        Time Complexity: O(log n)
        """
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1) # Bubble up from the last element

    def extract_min(self):
        """
        Removes and returns the task with the highest priority (lowest number).
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("extract_min from an empty priority queue")
        
        n = len(self.heap)
        if n == 1:
            return self.heap.pop()

        # Save the root (min element)
        min_task = self.heap[0]
        
        # Move the last element to the root
        self.heap[0] = self.heap.pop()
        
        # Bubble down the new root to restore heap property
        self._bubble_down(0)
        
        return min_task

    def _find_task_index(self, task_id):
        """
        Finds the index of a task by its ID.
        Time Complexity: O(n)
        """
        for i, task in enumerate(self.heap):
            if task.id == task_id:
                return i
        return -1 # Not found

    def change_priority(self, task_id, new_priority):
        """
        Modifies the priority of an existing task.
        Time Complexity: O(n) due to search.
        (O(log n) if a hash map is used for lookups)
        """
        index = self._find_task_index(task_id)
        
        if index == -1:
            raise KeyError(f"Task ID {task_id} not found in queue")
            
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority
        
        if new_priority < old_priority:
            # New priority is higher (lower number), so bubble up
            self._bubble_up(index)
        elif new_priority > old_priority:
            # New priority is lower (higher number), so bubble down
            self._bubble_down(index)

# --- Demonstration ---
if __name__ == "__main__":
    
    pq = MinPriorityQueue()
    
    print("--- Inserting Tasks ---")
    pq.insert(Task("T1", "Fix critical bug", 2))
    pq.insert(Task("T2", "Implement feature X", 5))
    pq.insert(Task("T3", "Refactor database module", 3))
    pq.insert(Task("T4", "Write documentation", 10))
    pq.insert(Task("T5", "Attend team meeting", 8))
    
    print(f"Queue size: {len(pq)}")
    print([f"{t.id}({t.priority})" for t in pq.heap]) # Show internal heap
    
    print("\n--- Increasing Priority of 'Attend team meeting' (8 -> 1) ---")
    pq.change_priority("T5", 1)
    print([f"{t.id}({t.priority})" for t in pq.heap])
    
    print("\n--- Decreasing Priority of 'Refactor database' (3 -> 9) ---")
    pq.change_priority("T3", 9)
    print([f"{t.id}({t.priority})" for t in pq.heap])

    print("\n--- Extracting All Tasks (in priority order) ---")
    while not pq.is_empty():
        task = pq.extract_min()
        print(f"Extracted: {task}")
        
    print(f"\nFinal queue size: {len(pq)}")
