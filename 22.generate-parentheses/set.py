@cache
def generateParenthesis(self, n: int) -> List[str]:
    par_l = set()
    if n == 0:
        par_l.add("")
    elif n == 1:
        par_l.add("()")
    else:
        for i in range(n):
            inside = self.generateParenthesis(i)
            outside = self.generateParenthesis(n-1-i)
            for _in in inside:
                for _out in outside:
                    par_l.add(f"({_in}){_out}")

    return par_l