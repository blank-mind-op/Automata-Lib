import automata

def nfa_to_dfa(aut: automata.Non_deterministic_automata) -> automata.Non_deterministic_automata:
    power_set = aut.get_power_set_of_states()
    initial_states = aut.get_initial_states_list()
    accept_states = aut.get_accept_states_list()
    state_set = set()
    initial_states_set = set()
    accept_states_set = set()
    transitions_set = set()

    initial_set = set(aut.get_initial_states_list())

    for elements in power_set:
        state_set.add(automata.State(2, "{" + ",".join(str(elem) for elem in elements) + "}"))
        if set(initial_set) == elements:
            initial_states_set.add(automata.State(2, "{" + ",".join(str(elem) for elem in elements) + "}"))

    # Dictionary to map the original state labels to state objects in the power set
    state_dict_orig_to_new = {}
    for orig_state_label, new_state in zip(aut.get_states_list(), state_set):
        state_dict_orig_to_new[orig_state_label] = new_state

    l = []
    for state in initial_states_set:
        l.append(state)

    # The accept states are the subsets containing at least one accept state from the original automata
    for elem in power_set:
        for label in accept_states:
            if label in elem:
                accept_states_set.add(tuple(elem))

    new_accept_states_set = set()

    for elem in accept_states_set:
        new_accept_states_set.add(automata.State(2, "{" + ",".join(str(i) for i in elem) + "}"))

    new_accept_state_list_str = [i.get_state_label() for i in new_accept_states_set]

    values = []
    for key in new_accept_state_list_str:
        try:
            value = state_dict_orig_to_new[key]
            values.append(value)
        except KeyError:
            print(f"KeyError: Key '{key}' not found in state_dict_orig_to_new")

    accept_states_set = set(values)

    # Set to store transitions for the new DFA
    dfa_transitions = set()

    # Iterate through each state set in the power set
    for state_set in power_set:
        # Iterate through each symbol in the alphabet
        for symbol in aut.alphabet.get_symbols():
            state_dict_orig_to_new = {} # Get the state object corresponding to the label
            # Get the set of states reachable from the current state set using the symbol
            destination_state_set = set()
            for state_label in state_set:
                state = state_dict_orig_to_new[state_label]  # Get the state object corresponding to the label
                transitions_from_state = aut.get_transitions_from_state(state)
                for transition in transitions_from_state:
                    if transition.get_transition_label() == symbol:
                        destination_state_set.add(transition.get_transition_destination_state().get_state_label())  # Get the label of the destination state

            # Determine the label of the destination state set
            destination_state_label = "{" + ",".join(sorted(destination_state_set)) + "}"

            # Create a transition object and add it to the set of transitions for the new DFA
            origin_state_label = "{" + ",".join(sorted(state_set)) + "}"
            origin_state = state_dict_orig_to_new[origin_state_label]  # Get the state object corresponding to the label
            destination_state = state_dict_orig_to_new[destination_state_label]  # Get the state object corresponding to the label
            dfa_transitions.add(automata.Transition(origin_state, symbol, destination_state, aut.alphabet))

    automata_by_parts = automata.Non_deterministic_automata(aut.alphabet, state_set, {state_dict_orig_to_new[l[0].get_state_label()]}, accept_states_set, dfa_transitions)

    return automata_by_parts





sigma = automata.Alphabet({'a','b'})
print(sigma.get_alphabet_id())
s1 = automata.State(2,'q1')
s2 = automata.State(2,'q2')
s3 = automata.State(2,'q3') 
s4 = automata.State(2,'q4')

t1 = automata.Transition(s1,'a',s1,sigma)
t2 = automata.Transition(s2,'b',s1,sigma)
t3 = automata.Transition(s2,'a',s3,sigma)
t5 = automata.Transition(s4,'b',s1,sigma)
t6 = automata.Transition(s3,'b',s1,sigma)
t7 = automata.Transition(s1,'b',s3,sigma)

a = automata.Non_deterministic_automata(sigma,{s1,s2,s3,s4},{s4,s1,s2},{s3,s4},{t1,t2,t3,t5,t6,t7})



b = nfa_to_dfa(a)



#b.render_automata()





sigma = automata.Alphabet({'a','b'})
print(sigma.get_alphabet_id())
s1 = automata.State(2,'q1')
s2 = automata.State(2,'q2')
s3 = automata.State(2,'q3') 
s4 = automata.State(2,'q4')

t1 = automata.Transition(s1,'a',s1,sigma)
t2 = automata.Transition(s2,'b',s1,sigma)
t3 = automata.Transition(s2,'a',s3,sigma)
t5 = automata.Transition(s4,'b',s1,sigma)
t6 = automata.Transition(s3,'b',s1,sigma)
t7 = automata.Transition(s1,'b',s3,sigma)

a = automata.Non_deterministic_automata(sigma,{s1,s2,s3,s4},{s4,s1,s2},{s3,s4},{t1,t2,t3,t5,t6,t7})



b = nfa_to_dfa(a)



#b.render_automata()


