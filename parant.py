oPL: list[str] = ["[", "{", "("]
cPL: list[str] = ["]", "}", ")"]
def isParenthesesBalanced(
    text: str,
    oPL: list[str] = ["[", "{", "("],
    cPL: list[str] = ["]", "}", ")"],
) -> bool:
    """Returns whether the parentheses in the text are balanced.

    Args:
        text (str): A text for checking paranthesis balance.
        oPL = openParenthesesList (list[str], optional): A list of open paranthesis.. Defaults to ["[", "{", "("].
        cPL = closeParenthesesList (list[str], optional): A list of close paranthesis.. Defaults to ["]", "}", ")"].

    Returns:
        bool: Whether the parentheses in the text are balanced.
    """

    stack: list[str] = []

    if not text:
        raise ValueError("Text is empty.")

    for i in text:
        if i in oPL:
            stack.append(i)
        elif i in cPL:
            pos = cPL.index(i)
            if len(stack) > 0 and oPL[pos] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            continue

    if not stack:
        return True
    else:
        return False


def main():
    
    while True:
        text = input("Enter text: ")
        if '()' in text or '[]' in text or '{}' in text:
            print("Is Parentheses Balanced?", isParenthesesBalanced(text))
        elif text=='exit':
            print('Shut down')
            break
        else:
            print('Not proper entry')

if __name__ == "__main__":
    main()
