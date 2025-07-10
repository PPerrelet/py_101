# Alyssa was asked to write an implementation of a rolling buffer. 
# You can add and remove elements from a rolling buffer.
#  However, once the buffer becomes full,
#  any new elements will displace the oldest elements in the buffer.

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)  # .append modifies the original list as the original list.
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]   # creates a new list within this functions scope. global buffer remains unchanged.
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# What is the key difference between these implementations?