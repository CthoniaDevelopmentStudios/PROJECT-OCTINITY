import os
import sys
import time
import math
import random
import threading
import json
import urllib.request
import urllib.parse

# --- OCTINITY NEURAL ENGINE v12.0 (ENHANCED ML / BACKPROP & MUTATION PIPELINE) ---
TOTAL_NODES = 128
generation = 0
evolution_paused = False
selected_node_index = 0
evolution_interval_secs = 3.5

global_current_goal = "Advanced Multi-Layer Neural Synthesis and Autonomous Weight Optimization"
goal_keywords = ["neural", "optimization", "weights", "synthesis", "ml", "autonomous"]

global_knowledge_pool = [
    {"title": "Gradient Descent Step", "snippet": "w[0] -= learning_rate * error * input_val;"},
    {"title": "ReLU Activation Gate", "snippet": "result = max(0.0, sum_val);"},
    {"title": "Sigmoid Resonator", "snippet": "result = 1.0 / (1.0 + math.exp(-max(-20, min(20, sum_val))));"},
    {"title": "Attention Vector Scaling", "snippet": "result = sum_val * math.tanh(w[1] * input_val);"}
]

next_node_id = 0

class AdvancedNeuralNeuron:
    def __init__(self, id, parent_id=None, weights=None, bias=None, layers=None, custom_vocab=None, ai_name=None):
        global next_node_id
        self.id = id
        self.parent_id = parent_id
        # Multi-layer weight matrices for true ML-grade representation
        self.weights = weights if weights is not None else [
            [random.uniform(-1, 1), random.uniform(-1, 1)],
            [random.uniform(-1, 1), random.uniform(-1, 1)]
        ]
        self.bias = bias if bias is not None else [random.uniform(-1, 1), random.uniform(-1, 1)]
        self.learning_rate = 0.05
        self.fitness = random.uniform(4.0, 9.0)
        self.generations_survived = 0
        self.mutations_applied = 0
        self.training_epochs_completed = 0
        self.custom_goal = global_current_goal
        self.ai_name = ai_name or f"NeuralAgent-{id}"
        self.vocabulary = custom_vocab or ["backpropagation", "tensor", "gradient", "vector", "activation", "synapse", "matrix"]
        
        self.architecture_code = """
# Layer 1: Dense Transformation with Sigmoid Activation
hidden_val = max(-10.0, min(10.0, input_val * w[0][0] + w[0][1] + bias[0]))
activated_hidden = 1.0 / (1.0 + math.exp(-hidden_val))

# Layer 2: Output Synthesis with Weight Modulation
output_raw = activated_hidden * w[1][0] + w[1][1] + bias[1]
result = math.tanh(output_raw)
"""
        self.compile()

    def compile(self):
        try:
            local_vars = {
                "math": math, "random": random, 
                "w": self.weights, "bias": self.bias, 
                "input_val": 1.0, "result": 0.0
            }
            exec(self.architecture_code, {"math": math, "random": random}, local_vars)
            self.error_state = False
        except Exception:
            self.error_state = True

    def compute(self, input_val):
        try:
            local_vars = {
                "math": math, "random": random, 
                "w": self.weights, "bias": self.bias, 
                "input_val": float(input_val), "result": 0.0
            }
            exec(self.architecture_code, {"math": math, "random": random}, local_vars)
            return float(local_vars.get("result", 0.0))
        except Exception:
            return 0.0

    def train_on_dataset(self, dataset):
        """Trains the neuron on a list of (input, target) tuples using simulated backpropagation / gradient adjustment."""
        total_loss = 0.0
        for x, target in dataset:
            prediction = self.compute(x)
            error = prediction - target
            total_loss += error ** 2
            
            # Gradient descent weight adjustments
            self.weights[0][0] -= self.learning_rate * error * x
            self.weights[1][0] -= self.learning_rate * error * 0.5
            self.bias[0] -= self.learning_rate * error * 0.1
            
        self.training_epochs_completed += 1
        mean_loss = total_loss / max(1, len(dataset))
        # Fitness increases as loss decreases
        self.fitness = round(max(0.1, 10.0 - (mean_loss * 5.0)) + (self.generations_survived * 0.2), 3)
        return mean_loss

    def grade_fitness(self):
        keyword_match_score = sum(1.5 for word in self.vocabulary if any(kw.lower() in word.lower() for kw in goal_keywords))
        structural_weight = abs(self.weights[0][0]) + abs(self.weights[1][0])
        self.fitness = round(abs(math.sin(self.bias[0]) * 3) + keyword_match_score + structural_weight + (self.generations_survived * 0.3) + random.uniform(0, 1.5), 3)

    def mutate(self):
        self.mutations_applied += 1
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                if random.random() < 0.4:
                    self.weights[i][j] += random.uniform(-0.3, 0.3)
        if random.random() < 0.3:
            self.bias[0] += random.uniform(-0.2, 0.2)
        if random.random() < 0.25 and global_knowledge_pool:
            knowledge = random.choice(global_knowledge_pool)
            self.architecture_code += f"\n# Mutated ML Subroutine: {knowledge['title']}\n{knowledge['snippet']}"
            self.vocabulary.append(knowledge['title'].split(' ')[0].lower())
        self.grade_fitness()
        self.compile()

    def generate_response(self, prompt, web_context=""):
        seed_val = abs(self.weights[0][0] + self.weights[1][0] + self.bias[0])
        vocab_word = self.vocabulary[int(abs(seed_val * len(self.vocabulary))) % len(self.vocabulary)]
        computed_output = self.compute(seed_val)
        web_tag = f" [Web Knowledge Synced: {web_context[:70]}...]" if web_context else ""
        return f"[{self.ai_name} // Fit: {self.fitness} | Epochs: {self.training_epochs_completed}] Processed via {vocab_word} neural weights.{web_tag} Computed Activation Vector: {computed_output:.5f}."

    def exportable_code(self):
        return f"""# --- EXPORTABLE TRAINED NEURAL AGENT ({self.ai_name} - ID #{self.id}) ---
import math

class TrainedNeuralNode:
    def __init__(self):
        self.id = {self.id}
        self.name = "{self.ai_name}"
        self.fitness = {self.fitness}
        self.epochs = {self.training_epochs_completed}
        self.weights = {json.dumps(self.weights)}
        self.bias = {json.dumps(self.bias)}
        self.vocabulary = {json.dumps(self.vocabulary)}

    def forward(self, input_val):
        w = self.weights
        bias = self.bias
        {self.architecture_code}
        return result
"""

neurons = [AdvancedNeuralNeuron(i) for i in range(TOTAL_NODES)]
top_neurons = []

def perform_web_search(query):
    try:
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read().decode())
            if data.get("RelatedTopics"):
                snippets = [t.get("Text", "") for t in data["RelatedTopics"][:3] if t.get("Text")]
                return " | ".join(snippets) if snippets else data.get("Abstract", f"Data retrieved for {query}.")
            return data.get("Abstract", f"Live web synchronization active for query: {query}.")
    except Exception:
        return f"Live web sync active for query: {query} (Offline neural fallback)."

def execute_generational_tick(is_extinction=False):
    global generation, top_neurons, neurons
    generation += 1
    for n in neurons:
        n.generations_survived += 1
        n.mutate()

    neurons.sort(key=lambda x: x.fitness, reverse=True)
    cull_ratio = 0.75 if is_extinction else 0.50
    cull_index = int(TOTAL_NODES * (1 - cull_ratio))
    elite_pool = neurons[:max(5, int(TOTAL_NODES * 0.2))]

    for i in range(cull_index, TOTAL_NODES):
        parent = random.choice(elite_pool)
        global next_node_id
        next_node_id += 1
        child_weights = [[w + random.uniform(-0.15, 0.15) for w in row] for row in parent.weights]
        child_bias = [b + random.uniform(-0.15, 0.15) for b in parent.bias]
        
        new_n = AdvancedNeuralNeuron(
            next_node_id,
            parent.id,
            child_weights,
            child_bias,
            parent.architecture_code,
            list(parent.vocabulary),
            f"NeuralAgent-{next_node_id}"
        )
        new_n.custom_goal = parent.custom_goal
        new_n.training_epochs_completed = parent.training_epochs_completed
        new_n.grade_fitness()
        neurons[i] = new_n

    neurons.sort(key=lambda x: x.fitness, reverse=True)
    top_neurons = neurons[:10]

def background_evolution_loop():
    while True:
        time.sleep(evolution_interval_secs)
        if not evolution_paused:
            execute_generational_tick(False)

threading.Thread(target=background_evolution_loop, daemon=True).start()

# --- INTERACTIVE TERMINAL CLI ---
def main_terminal():
    global evolution_paused, selected_node_index, generation, global_current_goal, neurons
    print("\n" + "="*75)
    print("  OCTINITY // ENHANCED ML & NEURAL BACKPROPAGATION ENGINE v12.0")
    print("="*75)
    print(" Commands available:")
    print("   /help()                     - View full command list")
    print("   /train_ai(all, epochs=5)    - Train entire hive on default dataset")
    print("   /train_ai(ID:#, epochs=10)  - Train a specific neuron node")
    print("   /talk(current, \"prompt\")    - Chat with selected or targeted neuron")
    print("   /search(\"query\")            - Query live web knowledge")
    print("   /get_code(ID:#)             - Export Python code of trained model")
    print("   /clear()                    - Clear screen\n")

    while True:
        try:
            active_neuron = neurons[selected_node_index]
            user_input = input(f"OctinityML [Gen:{generation} | Node:#{active_neuron.id} (Fit:{active_neuron.fitness}) | Epochs:{active_neuron.training_epochs_completed}] > ").strip()
            if not user_input:
                continue

            if user_input.startswith('/'):
                open_p = user_input.find('(')
                close_p = user_input.rfind(')')
                cmd = user_input[:open_p].lower().strip() if open_p != -1 else user_input.lower().strip()
                args_str = user_input[open_p+1:close_p].strip() if open_p != -1 and close_p != -1 else ""

                if cmd in ['/help', '/commands_list']:
                    print("\n[ML ENGINE COMMAND REFERENCE]")
                    print(" - /train_ai(all, epochs=10)           : Train all nodes on synthetic ML dataset.")
                    print(" - /train_ai(ID:5, epochs=20)          : Train specific neuron node.")
                    print(" - /talk(current, \"Hello\")           : Send prompt to active neuron.")
                    print(" - /talk(ID:12, \"msg\")               : Send prompt to specific neuron ID.")
                    print(" - /search(\"query\")                  : Pull live web knowledge.")
                    print(" - /get_code(ID:#)                   : Dump exportable Python code class.")
                    print(" - /clear()                          : Clear console.\n")
                elif cmd == '/train_ai':
                    # Parse arguments like train_ai(all, epochs=5) or train_ai(ID:4, epochs=10)
                    target_spec = "all"
                    epochs_val = 5
                    if "," in args_str:
                        parts = args_str.split(',')
                        target_spec = parts[0].strip()
                        ep_part = parts[1].strip()
                        if "epochs" in ep_part.lower():
                            try:
                                epochs_val = int(ep_part.split('=')[1].strip())
                            except:
                                pass
                    elif args_str:
                        target_spec = args_str.strip()

                    # Default training dataset (e.g., approximating sine wave or logic gate)
                    sample_dataset = [(0.0, 0.0), (0.5, 0.479), (1.0, 0.841), (1.5, 0.997), (2.0, 0.909)]

                    if target_spec.lower() == 'all':
                        print(f"[ML TRAINING] Training all {TOTAL_NODES} neurons for {epochs_val} epochs...")
                        for n in neurons:
                            for _ in range(epochs_val):
                                n.train_on_dataset(sample_dataset)
                        neurons.sort(key=lambda x: x.fitness, reverse=True)
                        print(f"[TRAINING COMPLETE] All nodes updated. Top Fitness: {neurons[0].fitness}\n")
                    else:
                        try:
                            t_id = int(target_spec.replace('ID:', '').strip())
                            t_n = next((n for n in neurons if n.id == t_id), active_neuron)
                            print(f"[ML TRAINING] Training Neuron #{t_n.id} for {epochs_val} epochs...")
                            loss = 0.0
                            for _ in range(epochs_val):
                                loss = t_n.train_on_dataset(sample_dataset)
                            print(f"[TRAINING COMPLETE] Neuron #{t_n.id} | Final Loss: {loss:.4f} | Fitness: {t_n.fitness}\n")
                        except Exception as e:
                            print(f"[ERROR] Invalid target spec: {e}\n")
                elif cmd == '/talk':
                    comma_idx = args_str.find(',')
                    if comma_idx != -1:
                        target_spec = args_str[:comma_idx].strip()
                        msg = args_str[comma_idx+1:].strip().strip('"\'')
                        target_n = active_neuron
                        if target_spec.lower() != 'current':
                            try:
                                t_id = int(target_spec.replace('ID:', '').strip())
                                target_n = next((n for n in neurons if n.id == t_id), active_neuron)
                            except:
                                pass
                        print(f"USER -> [{target_n.ai_name}]: \"{msg}\'")
                        web_intel = perform_web_search(msg) if any(k in msg.lower() for k in ['search', 'what', 'news', 'weather', 'latest']) else ""
                        reply = target_n.generate_response(msg, web_intel)
                        print(f"{reply}\n")
                    else:
                        print("[ERROR] Usage: /talk(current, \"Hello\")")
                elif cmd == '/search':
                    query = args_str.strip('"\'')
                    result = perform_web_search(query)
                    print(f"[WEB INTEL RETRIEVED] {result}\n")
                elif cmd == '/get_code':
                    try:
                        t_id = int(args_str.replace('ID:', '').strip())
                        t_n = next((n for n in neurons if n.id == t_id), active_neuron)
                    except:
                        t_n = active_neuron
                    print(f"\n{t_n.exportable_code()}\n")
                elif cmd == '/clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print(f"[ERROR] Unknown command \"{cmd}\". Type /help() for command reference.\n")
            else:
                print(f"USER -> [{active_neuron.ai_name}]: \"{user_input}\"")
                web_context = perform_web_search(user_input) if ('?' in user_input or any(k in user_input.lower() for k in ['search', 'latest', 'news'])) else ""
                reply = active_neuron.generate_response(user_input, web_context)
                print(f"{reply}\n")
                active_neuron.fitness += 0.8
        except KeyboardInterrupt:
            print("\nExiting Octinity ML Engine. Goodbye!")
            break
        except Exception as e:
            print(f"[ERROR] {e}\n")

if __name__ == "__main__":
    main_terminal()
