import time

# Simulate a very basic LLM inference function
# In a real scenario, this would involve complex neural network computations.
# The 'prompt' is the input text, and 'tokens' is the number of tokens to generate.
class MockLLM:
    def __init__(self):
        self.cache = {}
        self.inference_count = 0

    def infer(self, prompt, tokens=1):
        self.inference_count += 1
        # Simulate a cache key based on prompt and requested tokens
        cache_key = (prompt, tokens)

        if cache_key in self.cache:
            print(f"[CACHE HIT] Returning cached result for prompt: '{prompt[:20]}...' and {tokens} tokens.")
            return self.cache[cache_key]

        print(f"[CACHE MISS] Performing full inference for prompt: '{prompt[:20]}...' and {tokens} tokens.")
        # Simulate computation time
        time.sleep(0.1) # Simulate 100ms of computation
        result = f"Generated text for '{prompt[:20]}...'"
        # In a real LLM, subsequent tokens would depend on previous ones.
        # For simplicity, we're just generating a placeholder.
        for _ in range(tokens - 1):
            result += "+" # Simulate adding more tokens

        # Store the result in the cache
        self.cache[cache_key] = result
        return result

# --- Demonstration ---

llm = MockLLM()

# First inference - cache miss
print("--- First Inference ---")
start_time = time.time()
output1 = llm.infer("What is the capital of France?", tokens=5)
end_time = time.time()
print(f"Output: {output1}")
print(f"Time taken: {end_time - start_time:.4f} seconds\n")

# Second inference with the exact same prompt and tokens - cache hit
print("--- Second Inference (Same Prompt) ---")
start_time = time.time()
output2 = llm.infer("What is the capital of France?", tokens=5)
end_time = time.time()
print(f"Output: {output2}")
print(f"Time taken: {end_time - start_time:.4f} seconds\n")

# Third inference with a slightly different prompt - cache miss
print("--- Third Inference (Different Prompt) ---")
start_time = time.time()
output3 = llm.infer("What is the capital of Germany?", tokens=3)
end_time = time.time()
print(f"Output: {output3}")
print(f"Time taken: {end_time - start_time:.4f} seconds\n")

# Fourth inference, re-using the second prompt, but requesting fewer tokens - cache miss (in this simplified model)
# In advanced KV caching, this might still leverage parts of the KV cache.
print("--- Fourth Inference (Same Prompt, Fewer Tokens) ---")
start_time = time.time()
output4 = llm.infer("What is the capital of France?", tokens=3)
end_time = time.time()
print(f"Output: {output4}")
print(f"Time taken: {end_time - start_time:.4f} seconds\n")

print(f"Total inferences performed: {llm.inference_count}")
print(f"Cache size: {len(llm.cache)}")
