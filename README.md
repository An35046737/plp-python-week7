# Week 7 Assignment: Shopping List Manager

This project demonstrates Python list operations, loops, membership checks, and list reporting.

## Files

- `list_warmup.py` — Demonstrates creating lists, accessing items by index, appending, removing, and counting items.
- `shopping_list.py` — Provides an interactive shopping list manager that allows users to add, remove, show, and finish.
- `list_report.py` — Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item name.
- `screenshots/` — Contains screenshots showing the output of each Python program.

## Why is it safer to check `in` before calling `.remove()`?

Checking whether an item is in a list before removing it prevents a `ValueError` when the item does not exist. It also allows the program to display a helpful message instead of stopping unexpectedly. This makes the program more reliable and user-friendly.
