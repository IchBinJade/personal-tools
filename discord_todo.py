#!/usr/bin/env python3
# 14 Jun 22 - Ich_bin_Jade
# Script to convert task list into formatted list for KOA accountability-station channel

import os
import datetime

"""
I like to use the moon phase emojis to track progress
of my tasks. Feel free to amend and find one at:

https://www.webfx.com/tools/emoji-cheat-sheet/
"""

EMOJI_MARKER = ":new_moon:"

tasks = []


def clear_screen():
    if os.name in ("nt", "dos"):
        command = "cls"
    else:
        command = "clear"
    os.system(command)


def get_date():
    # Format today's date as MON MM/DD/YY
    raw_date = datetime.datetime.now()
    out_date = raw_date.strftime("%a %x")
    return out_date


def get_list(user_tasks):
    task_in = ""

    # Get the tasks and build up list
    while task_in.lower() != "q":
        task_in = input("Enter a task (or 'q' to quit): ")
        if task_in != "q":
            user_tasks.append(task_in)

    return user_tasks


def display_list(task_list, marker):
    clear_screen()
    print(f"**{get_date()}**")
    print(f"*Not Started: {len(task_list)}; In Progress: 0; Completed: 0*")
    print("")

    for task in task_list:
        print(f"{marker} {task}")


if __name__ == "__main__":
    get_list(tasks)
    display_list(tasks, EMOJI_MARKER)
