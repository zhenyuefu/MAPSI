def viterbi(obs_seq, states, start_probs, trans_probs, emission_probs):
    T = len(obs_seq)
    N = len(states)

    V = [[0 for _ in range(N)] for _ in range(T)]
    backpointer = [[0 for _ in range(N)] for _ in range(T)]
    # Initialize the Viterbi array.
    for i in range(N):
        V[0][i] = start_probs[i] * emission_probs[i][obs_seq[0]]
        backpointer[0][i] = -1
        print(0, i, V[0][i], backpointer[0][i])

    # Calculate the Viterbi probabilities for each time step.
    for t in range(1, T):
        for j in range(N):
            V[t][j], backpointer[t][j] = max(
                (V[t - 1][i] * trans_probs[i][j] * emission_probs[j][obs_seq[t]], i)
                for i in range(N)
            )
            print(t, j, V[t][j], backpointer[t][j])

    # Trace the backpointers to find the optimal hidden state sequence.
    hidden_seq = []
    j = max(range(N), key=lambda i: V[T - 1][i])
    hidden_seq.append(j)
    for t in range(T - 1, 0, -1):
        j = backpointer[t][j]
        hidden_seq.append(j)

    hidden_seq.reverse()

    return hidden_seq


Pi = [0.99, 0.01]
A = [[0.99, 0.01], [0.01, 0.99]]
b = [[0.8, 0.2], [0.1, 0.9]]
print(viterbi([0, 1, 0], [0, 1], Pi, A, b))
