a = 1000
b = 1000
print(id(a))
print(id(b))

# Output:
# 4305789520
# 4305789520

# How are both the variables sharing the same ID even when both the values are greater than 256?

# Reasoning:
# While Python's **small integer cache** only applies to numbers from -5 to 256, integers greater than 256 can still share the same memory ID due to **code block optimization** (constant folding).

# **How Code Block Optimization Works**

# * **Single Code Block Compilation:** When Python compiles a block of code (such as a `.py` script file, a function, or a single multi-line execution in the REPL), it scans the code and groups constant values together.
# * **Literal Reuse (`co_consts`):** Because `1000` is an immutable literal and appears twice in the same code block, the compiler creates a single integer object in memory and points both `a` and `b` to it.

# **Small Integer Caching vs. Code Block Optimization**

# * **Small Integer Cache (-5 to 256):** Pre-allocated when Python starts up. Shared **globally** across all files, functions, and independent REPL prompts.
# * **Code Block Optimization (> 256):** Applied **locally** to identical constants within the same compiled code block.

# **When the IDs Will Differ**

# If you run those two assignments as separate commands in an interactive Python shell (REPL), each line is compiled as its own separate code block, resulting in two distinct objects:

# ```python
# >>> a = 1000  # Code block 1
# >>> b = 1000  # Code block 2
# >>> print(id(a) == id(b))
# False

# ```

# Running them together in a script file, inside a function, or pasted as a single block in the terminal forces Python to optimize the literal and reuse the same memory address.