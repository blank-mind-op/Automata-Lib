import automata

def nfa_to_dfa(aut : automata.Non_deterministic_automata) -> automata.Non_deterministic_automata:
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
        #The accept tates are the subsets containing at east one accept state from the original automata
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

        #Last thing to define is the set of transitions for the deterministic automata
        transition_table = {}
        for set_state in power_set:
            for sym in aut.get_automata_alphabet().get_symbols():
                reachable_from_sym = []
                for label in set_state:
                    if aut.reachable_states_from_sym(label,sym) != []:
                        reachable_from_sym.append(aut.reachable_states_from_sym(label,sym))
                flattened_list = [item for sublist in reachable_from_sym for item in sublist]
                transition_table[(frozenset(set_state),sym)] = set(flattened_list)
        


        #creating transition tuples

        transition_tuples = []
        for key,value in transition_table.items():
            key_str = "{"+",".join(sorted(str(i) for i in key[0])) +"}"
            value_str = "{"+",".join(sorted(str(i) for i in value)) +"}"

            transition_tuples.append((key_str,key[1],value_str))
        print(transition_table)
        print(transition_tuples)

        #Making Transition objects , remember that you need states to make transitions
        transiton_set = set()
        for tr_tuple in transition_tuples:
            initial_state = state_dict[tr_tuple[0]]
            destination_state = state_dict[tr_tuple[2]]
            label = tr_tuple[1]
            transiton_set.add(automata.Transition(initial_state,label,destination_state,aut.alphabet))
        
    
        
        automata_by_parts = automata.Non_deterministic_automata(automata.Alphabet,state_set,{state_dict[l[0].get_state_label()]},accept_states_set,transiton_set)

        return automata_by_parts


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



b = nfa_to_dfa(a)
#b.render_automata()

#print(a.get_state_by_label('s1').get_state_label())
#print(a.reachable_states_table_labels())
#print(a.transition_function())

#print(a.reachable_states_from_sym('s1','b'))



b.render_automata()






