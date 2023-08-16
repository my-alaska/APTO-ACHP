def check(CNF, V):
    """Checks if V (dict indicating values of the solution) satisfies CNF"""
    for clause in CNF:
        check = [c in V and V[c] == 1 for c in clause]
        if not any(check):
            return False
    return True


def simplifyClause(clause, V):
    """helper function to simplify clause
    remove all false variables or return None if clause is positive"""
    res = []
    for v in clause:
        if v not in V:
            # variables that don't have assigned values yet
            res.append(v)
        elif V[v] == 1:
            # one positive makes the whole value of the clause True
            return None
    return res


def simplifyCNF(CNF, V):
    """Helper function that simplifies the full form
    Removes satisfied clauses and simplifies the rest of them
    """
    if CNF is None:
        return None
    res = []
    for clause in CNF:
        new_clause = simplifyClause(clause, V)
        if new_clause == []:
            return None
        elif new_clause:
            res.append(new_clause)
    return res


def test_solution(CNF, solution):
    for clause in CNF:
        check = [c in solution for c in clause]
        if not any(check):
            return False
    return True
