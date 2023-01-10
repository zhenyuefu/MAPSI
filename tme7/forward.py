def forward_probability(obs_seq, states, start_probs, trans_probs, emission_probs):
    T = len(obs_seq)
    N = len(states)

    forward = [[0 for _ in range(N)] for _ in range(T)]

    # Initialize the forward array.
    for i in range(N):
        forward[0][i] = start_probs[i] * emission_probs[i][obs_seq[0]]
        print(0, i, forward[0][i])
    # Calculate the forward probabilities for each time step.
    for t in range(1, T):
        for j in range(N):
            forward[t][j] = sum(
                forward[t - 1][i] * trans_probs[i][j] * emission_probs[j][obs_seq[t]]
                for i in range(N)
            )
            print(t, j, forward[t][j])

    # Calculate the probability of the entire sequence.
    probability = sum(forward[T - 1][i] for i in range(N))

    return probability


Pi = [0.99, 0.01]
A = [[0.99, 0.01], [0.01, 0.99]]
b = [[0.8, 0.2], [0.1, 0.9]]
print(forward_probability([0, 1, 0], [0, 1], Pi, A, b))
