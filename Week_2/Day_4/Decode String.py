class Solution:
    def decodeString(self, s):
        count_stack = []
        string_stack = []

        current_num = 0
        current_string = ""

        for ch in s:
            if ch.isdigit():
                current_num = current_num * 10 + int(ch)

            elif ch == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)

                current_num = 0
                current_string = ""

            elif ch == ']':
                repeat = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * repeat

            else:
                current_string += ch

        return current_string
