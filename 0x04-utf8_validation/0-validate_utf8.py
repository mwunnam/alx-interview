#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Validation of a byte or list of byte to know if they comform to UTF-8
    """
    mask1 = 1 << 7
    mask2 = 1 << 6

    byte_num = 0

    for num in data:
        """ Getting the LSB of the last 8 bits """
        byte = num & 0xFF

        if byte_num == 0:
            mask = 1 << 7
            """
            check for the number of bytes in the current UTF-8 character
            """
            while mask & byte:
                byte_num += 1
                mask >>= 1

            """ If byte_number is 0 then it is an ASCII character """
            if byte_num == 0:
                continue

            """ This makes sure that the UTF-8 pattern is followed fo the first
            byte 11xxxxxx, 111xxxxx, 1111xxxx
            """
            if (byte_num == 1 or byte_num > 4):
                return False
        else:
            """ This check to makes sure that the subseqent bytes follow the
                pattern ie 01xxxxxx
            """
            if not (byte & mask1 and not (byte & mask2)):
                return False

        """
        Decreasing this will help to check the suseqent bytes
        """
        byte_num -= 1

    return byte_num == 0
