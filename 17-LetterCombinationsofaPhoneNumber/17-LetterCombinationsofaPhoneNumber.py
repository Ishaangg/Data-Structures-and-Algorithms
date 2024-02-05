        }

        def solve(combinations, next_digit):
            if not next_digit:
                result.append(combinations)
            
                return result


            for letter in digit_letters[current_digit]:
                new_combination = combinations + letter
                solve(new_combination, next_digit[1:])
        solve('', digits)
            current_digit = next_digit[0]
        return result
"
