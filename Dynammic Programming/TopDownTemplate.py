def solve(state):
    if state in memo:
        return memo[state]

    if base_case:
        return base_value

    memo[state] = best_choice(
        solve(smaller_state_1),
        solve(smaller_state_2)
    )

    return memo[state]
