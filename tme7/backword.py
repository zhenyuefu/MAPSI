def backward_probability(obs_seq, states, start_probs, trans_probs, emission_probs):
    T = len(obs_seq)
    N = len(states)
    # Initialize the backward array.
    backward = [[0 for _ in range(N)] for _ in range(T)]
    for i in range(N):
        backward[T - 1][i] = 1
        print(T - 1, i, backward[T - 1][i])

    # Calculate the backward probabilities for each time step.
    for t in range(T - 2, -1, -1):
        for i in range(N):
            backward[t][i] = sum(
                backward[t + 1][j]
                * trans_probs[i][j]
                * emission_probs[j][obs_seq[t + 1]]
                for j in range(N)
            )
            print(t, i, backward[t][i])
    # Calculate the probability of the entire sequence.
    probability = sum(
        backward[0][i] * start_probs[i] * emission_probs[i][obs_seq[0]]
        for i in range(N)
    )

    return probability


Pi = [0.99, 0.01]
A = [[0.99, 0.01], [0.01, 0.99]]
b = [[0.8, 0.2], [0.1, 0.9]]
print(backward_probability([0, 1, 0], [0, 1], Pi, A, b))
