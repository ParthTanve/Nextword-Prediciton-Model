from chain import MarkovChain

# Create 3rd-order chain => order = 2
mc = MarkovChain(2)

# Train using your dataset
mc.train("sampledata.txt")


# Save the model
mc.to_json("markov_chain_3rd_order.json")

print("3rd-order Markov Chain trained and saved.")
