def isParenthesesBalanced(
    text: str,
    openParenthesesList: list[str] = ["[", "{", "("],
    closeParenthesesList: list[str] = ["]", "}", ")"],
) -> bool:
    """Returns whether the parentheses in the text are balanced.

    Args:
        text (str): A text for checking paranthesis balance.
        openParenthesesList (list[str], optional): A list of open paranthesis.. Defaults to ["[", "{", "("].
        closeParenthesesList (list[str], optional): A list of close paranthesis.. Defaults to ["]", "}", ")"].

    Returns:
        bool: Whether the parentheses in the text are balanced.
    """

    stack: list[str] = []

    if not text:
        raise ValueError("Text is empty.")

    for i in text:
        if i in openParenthesesList:
            stack.append(i)
        elif i in closeParenthesesList:
            pos = closeParenthesesList.index(i)
            if len(stack) > 0 and openParenthesesList[pos] == stack[-1]:
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
    text = input("Enter text: ")
    print("Is Parentheses Balanced?", isParenthesesBalanced(text))


if __name__ == "__main__":
    main()
