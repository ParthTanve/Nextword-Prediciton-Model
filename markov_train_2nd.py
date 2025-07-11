from chain import MarkovChain

mc = MarkovChain(1)  # 2nd-order

# Use your dataset filename
mc.train("sampledata.txt")

# Save the trained model
mc.to_json("markov_chain_2nd_order.json")

print("Training complete. Model saved.")
