Assignment 4: Heap Data Structures and Applications

Author: Shashwat Baral
Course: Algorithms and Data Structures (MSCS-532-B01)

Overview

This repository contains the Python implementation and analysis for an assignment on heap data structures. The project covers two main applications:

Heapsort: An efficient, in-place $O(n \log n)$ sorting algorithm. This implementation includes an empirical benchmark comparing it against Randomized Quicksort and Mergesort.

Priority Queue: A Min-Heap-based Priority Queue designed for task scheduling. It supports $O(\log n)$ insertion and extraction, and $O(n)$ priority updates.

A detailed theoretical analysis of all algorithms and data structures is available in the report/Assignment_4_Report.md file.

Repository Contents

report/Assignment_4_Report.md: The formal write-up, analysis, and discussion for the assignment.

src/heapsort_analysis.py: Python code for Heapsort, Mergesort, Randomized Quicksort, and the empirical comparison test script.

src/priority_queue.py: Python implementation of a Task class and a MinPriorityQueue class, with a demonstration.

README.md: This file.

How to Run the Code

Prerequisites

Python 3.x

Part 1: Heapsort Empirical Analysis

To run the comparison script that benchmarks Heapsort, Randomized Quicksort, and Mergesort:

python heapsort_analysis.py


This script will:

Generate three different types of arrays (Random, Sorted, Reverse-Sorted) of size n=100,000.

Run all three sorting algorithms on copies of these arrays.

Print the time taken for each experiment to the console.

Part 2: Priority Queue Demonstration

To run the demonstration of the MinPriorityQueue:

python priority_queue.py


This script will:

Initialize a new MinPriorityQueue.

Insert several Task objects with different priorities.

Demonstrate the change_priority function to both increase and decrease a task's priority.

Extract all tasks from the queue in priority order (lowest number to highest) until the queue is empty.

Summary of Findings

Heapsort: Proves to be a highly reliable sorting algorithm. Its $O(n \log n)$ performance is consistent across all data distributions (random, sorted, reverse-sorted), and it has the significant advantage of being an $O(1)$ space (in-place) sort.

Priority Queue: A heap is the ideal data structure for a priority queue, providing efficient $O(\log n)$ insert and extract_min operations. The primary performance bottleneck is updating an arbitrary task's priority (change_priority), which requires an $O(n)$ scan to locate the task. This can be optimized to $O(\log n)$ by using an auxiliary hash map to track task indices.
