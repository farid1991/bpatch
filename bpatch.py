#!/usr/bin/env python

import sys
import struct

REPEATED = 20  # Number of repetitions of the pattern

def check_patched(data, patch):
    """
    Check if the binary file is already patched.

    :param data: Binary data to search
    :param patch: The patch data to compare
    :return: True if the patch is found in the binary, False otherwise
    """
    return patch in data


def check(data, what, a, s, count):
    """
    Check if a repeated pattern exists in the binary data.

    :param data: Binary data to search
    :param what: Byte to check for
    :param a: Start index
    :param s: Step size
    :param count: Number of repetitions
    :return: Length of the match (s * count) or 0 if no match
    """
    for i in range(count):
        index = a + s * i
        if index >= len(data) or data[index] != what:
            return 0
    return s * count



def find(data, what, paddr, count):
    """
    Find a repeated pattern in the binary data.

    :param data: Binary data to search
    :param what: Byte to check for
    :param paddr: Placeholder to store the start address (not used in this version)
    :param count: Number of repetitions
    :return: Tuple of start index and match length, or (0, 0) if not found
    """
    fs = len(data)

    # Determine possible step sizes based on data length and repetition count
    max_step = fs // count
    possible_steps = range(2, max_step + 1, 2)  # Check every 2 bytes

    for i in range(fs):
        for step in possible_steps:
            j = check(data, what, i, step, count)
            if j > 0:
                return i, j  # Return the start index and match length

    return 0, 0



def main():
    if len(sys.argv) < 2:
        print("Usage: bpatch.py jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b")
        return

    # Load the binary file
    file_path = sys.argv[1]
    try:
        with open(file_path, "rb") as f:
            data = bytearray(f.read())
    except FileNotFoundError:
        print("jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b not found.")
        return

    # Load the patch data
    try:
        with open("bpatchgo.bin", "rb") as patch_file:
            patch = patch_file.read()
    except FileNotFoundError:
        print("Patch file 'bpatchgo.bin' not found. use default patch data")
        patch = bytearray([0, 160, 0, 71, 122, 255, 23, 238, 253, 255, 255, 26, 0, 0, 160, 227, 154, 15, 7, 238, 0, 0, 160, 227, 21, 15, 7, 238, 1, 0, 143, 226, 16, 255, 47, 225, 40, 28, 16, 48, 49, 28, 16, 49, 136, 71, 192, 70])

    # Check if the file is already patched
    if check_patched(data, patch):
        print("The file is already patched.")
        return

    # Locate the pattern
    newcodestart, newcodeend = find(data, 0x55, 0, REPEATED)
    if newcodeend > 0:
        newcodeend += newcodestart
        print(f"Pattern found from {hex(newcodestart)} to {hex(newcodeend)}")

        ret = struct.unpack_from("<H", data, newcodeend)[0]

        # Verify the 'return' instruction (0x2000 in little-endian)
        if ret == 0x2000:
            print(f"Return instruction found: {bytearray(ret)}")
            # Replace the code with the patch
            data[newcodestart:newcodestart + len(patch)] = patch

            # Fill the remaining space with NOP instructions (0x46C0 in little-endian)
            for i in range(newcodestart + len(patch), newcodeend + 1, 2):
                data[i:i + 2] = b"\xC0\x46"  # 0x46C0 in little-endian

            # Save the modified binary
            with open(file_path, "wb") as out_file:
                out_file.write(data)

            print("Patch applied successfully.")
        else:
            print("Can't find 'return' instruction at the expected position.")
    else:
        print("Movefrom not found.")


if __name__ == "__main__":
    main()
