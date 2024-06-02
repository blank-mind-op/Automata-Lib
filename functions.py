import automata
from copy import deepcopy



epsilon = '\u03B5'
empty_set = '\u2205'



def nfa_to_dfa(aut : automata.Non_deterministic_automata) -> automata.Deterministic_automata:
        power_set = aut.get_power_set_of_states()
        accept_states = aut.get_accept_states_list()
        state_set = set()
        initial_states_set = set()
        accept_states_set = set()

        initial_set = set(aut.get_initial_states_list())

        for elements in power_set:
            state_set.add(automata.State(2,"{"+",".join(sorted(str(elem) for elem in elements)) +"}"))
            if(set(initial_set) == elements):
                initial_states_set.add(automata.State(2,"{"+",".join(sorted(str(elem) for elem in elements)) +"}"))


        state_dict = {state.get_state_label() : state for state in state_set}
        state_dict_inv = {state : state.get_state_label() for state in state_set}
        
        l = []
        for state in initial_states_set:
            l.append(state)
        
        for elem in power_set:
            for label  in accept_states:
                if label in elem:
                    accept_states_set.add(tuple(elem))

        new_accept_states_set = set()
        
        for elem in accept_states_set:
            new_accept_states_set.add(automata.State(2,"{"+",".join(sorted(str(i) for i in elem)) +"}"))

        new_accept_state_list_str = [i.get_state_label() for i in new_accept_states_set]


        values = []
        for key in new_accept_state_list_str:
            values.append(state_dict[key])

        accept_states_set = set(values)

        
        transition_table = {}
        for set_state in power_set:
            for sym in aut.get_automata_alphabet().get_symbols():
                reachable_from_sym = []
                for label in set_state:
                    if aut.reachable_states_from_sym(label,sym) != []:
                        reachable_from_sym.append(aut.reachable_states_from_sym(label,sym))
                flattened_list = [item for sublist in reachable_from_sym for item in sublist]
                transition_table[(frozenset(set_state),sym)] = set(flattened_list)
        


        

        transition_tuples = []
        for key,value in transition_table.items():
            key_str = "{"+",".join(sorted(str(i) for i in key[0])) +"}"
            value_str = "{"+",".join(sorted(str(i) for i in value)) +"}"

            transition_tuples.append((key_str,key[1],value_str))
        print(transition_table)
        print(transition_tuples)

        
        transiton_set = set()
        for tr_tuple in transition_tuples:
            initial_state = state_dict[tr_tuple[0]]
            destination_state = state_dict[tr_tuple[2]]
            label = tr_tuple[1]
            transiton_set.add(automata.Transition(initial_state,label,destination_state,aut.alphabet))
        
    
        
        automata_by_parts = automata.Deterministic_automata(aut.alphabet,state_set,{state_dict[l[0].get_state_label()]},accept_states_set,transiton_set)

        return automata_by_parts


def complete_dfa(aut : automata.Deterministic_automata):
    
    states = set(aut.get_states_list())
    symbols = aut.alphabet.get_symbols()
    start_state =set(aut.get_initial_states_list())
    transitions = set(aut.get_transition_list())
    final_states = set(aut.get_accept_states_list())
    
    
    trap_state = 'trap'
    states.add(trap_state)
    
    
    transition_dict = {}
    for (from_state, input_symbol, to_state) in transitions:
        transition_dict[(from_state, input_symbol)] = to_state
    
    
    for state in states:
        for terminal in symbols:
            if (state, terminal) not in transition_dict:
                transition_dict[(state, terminal)] = trap_state
    
    
    for terminal in symbols:
        transition_dict[(trap_state, terminal)] = trap_state
    
    
    completed_transitions = [(from_state, input_symbol, to_state) for ((from_state, input_symbol), to_state) in transition_dict.items()]
    
    
    final_states.discard(trap_state)
    
    return states, symbols, start_state, completed_transitions, final_states






def complete_nfa(aut : automata.Non_deterministic_automata):
    
    states = set(aut.get_states_list())
    symbols = aut.alphabet.get_symbols()
    start_states =set(aut.get_initial_states_list())
    transitions = set(aut.get_transition_list())
    final_states = set(aut.get_accept_states_list())
    
    
    
    print(states)
    trap_state = 'trap'
    states.add(trap_state)
    
    
    transition_dict = {}
    for (from_state, input_symbol, to_state) in transitions:
        if (from_state, input_symbol) not in transition_dict:
            transition_dict[(from_state, input_symbol)] = set()
        transition_dict[(from_state, input_symbol)].add(to_state)
    
    
    for state in states:
        for terminal in symbols:
            if (state, terminal) not in transition_dict:
                transition_dict[(state, terminal)] = {trap_state}
    
    
    for terminal in symbols:
        transition_dict[(trap_state, terminal)] = {trap_state}
    
    
    completed_transitions = [(from_state, input_symbol, to_state) for ((from_state, input_symbol), to_states) in transition_dict.items() for to_state in to_states]
    
    
    final_states.discard(trap_state)
    
    return states, symbols, start_states, completed_transitions, final_states


def minimize_dfa(alphabet, states, initial_state, accept_states, transitions):
    
    partition = {0: accept_states, 1: states - accept_states}

    
    distinguished = {(i, j) for i in partition for j in partition if i < j}

    
    while distinguished:
        new_distinguished = set()
        for pair in distinguished:
            for symbol in alphabet:
                next_states = {}
                for i, state_set in partition.items():
                    next_state_set = set()
                    for state in state_set:
                        next_state_set.update(transitions.get((state, symbol), set()))
                    next_states[i] = next_state_set

                for i in partition:
                    for j in partition:
                        if i != j and next_states[i] & next_states[j]:
                            partition[i] |= partition[j]
                            partition[j] = partition[i]
                            new_distinguished.add((i, j))
                            break
                    else:
                        continue
                    break

        distinguished = new_distinguished

    
    minimized_states = set()
    minimized_initial_state = None
    minimized_accept_states = set()
    minimized_transitions = {}

    for i, state_set in partition.items():
        minimized_states.add(frozenset(state_set))
        if initial_state in state_set:
            minimized_initial_state = frozenset(state_set)
        if accept_states & state_set:
            minimized_accept_states.add(frozenset(state_set))

    for state_set in minimized_states:
        for symbol in alphabet:
            next_state = None
            for state in state_set:
                next_state_set = transitions.get((state, symbol), set())
                if next_state_set:
                    next_state = frozenset(next_state_set)
                    break
            if next_state:
                minimized_transitions[(tuple(state_set), symbol)] = tuple(next_state)

    return alphabet, minimized_states, minimized_initial_state, minimized_accept_states, minimized_transitions



sigma = automata.Alphabet({'a','b'})
print(sigma.get_alphabet_id())
s1 = automata.State(2,'s1')
s2 = automata.State(2,'s2')
s3 = automata.State(2,'s3')


t1 = automata.Transition(s1,'a',s1,sigma)
t2 = automata.Transition(s1,'b',s1,sigma)
t3 = automata.Transition(s1,'b',s2,sigma)
t4 = automata.Transition(s3,'a',s1,sigma)
t5 = automata.Transition(s3,'b',s3,sigma)
t6 = automata.Transition(s2,'a',s3,sigma)





a = automata.Non_deterministic_automata(sigma,{s1,s2,s3},{s1,s3},{s2},{t1,t2,t3,t4,t5,t6})

a.render_automata()

b = nfa_to_dfa(a)
b.render_automata()
















