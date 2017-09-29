from hmm import Model

states = ['rainy', 'sunny']
symbols = ['walk', 'shop', 'clean']

start_prob = {
    'rainy' : 0.5,
    'sunny' : 0.5
}

trans_prob = {
    'rainy': { 'rainy' : 0.7, 'sunny' : 0.3 },
    'sunny': { 'rainy' : 0.4, 'sunny' : 0.6 }
}

emit_prob = {
    'rainy': { 'walk' : 0.1, 'shop' : 0.4, 'clean' : 0.5 },
    'sunny': { 'walk' : 0.6, 'shop' : 0.3, 'clean' : 0.1 }
}

#sequence1 = ['walk', 'shop', 'clean', 'clean', 'walk', 'walk', 'walk', 'clean', 'shop', 'clean', 'clean', 'walk',]
#sequence2 = ['walk', 'shop', 'clean', 'clean', 'walk', 'walk', 'walk', 'clean', 'walk', 'walk', 'walk', 'clean', 'walk', 'walk', 'walk', 'clean']
sequence3 = ['walk', 'shop']

model = Model(states, symbols, start_prob, trans_prob, emit_prob)

#print model.evaluate(sequence1)
#print model.decode(sequence1)

#print model.evaluate(sequence2)
#print model.decode(sequence2)

print model.evaluate(sequence3)
print model.decode(sequence3)



