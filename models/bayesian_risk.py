def posterior(prior, likelihood):
    return (prior * likelihood) / (
        prior * likelihood + (1 - prior) * (1 - likelihood) + 1e-9
    )