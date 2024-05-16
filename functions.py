import automata

def nfa_to_dfa(aut : automata.Non_deterministic_automata) -> automata.Non_deterministic_automata:
        power_set = aut.get_power_set_of_states()
        initial_states = aut.get_initial_states_list()
        accept_states = aut.get_accept_states_list()
        state_set = set()
        initial_states_set = set()
        accept_states_set = set()
        transitions_set = set()

        initial_set = set(aut.get_initial_states_list())

        for elements in power_set:
            state_set.add(automata.State(2,"{"+",".join(str(elem) for elem in elements) +"}"))
            if(set(initial_set) == elements):
                initial_states_set.add(automata.State(2,"{"+",".join(str(elem) for elem in elements) +"}"))


        state_dict = {state.get_state_label() : state for state in state_set}
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
             new_accept_states_set.add(automata.State(2,"{"+",".join(str(i) for i in elem) +"}"))

        new_accept_state_list_str = [i.get_state_label() for i in new_accept_states_set]


        values = []
        for key in new_accept_state_list_str:
            values.append(state_dict[key])

        accept_states_set = set(values)

        #Last thing to define is the set of transitions for the deterministic automata

        for set_state in power_set:
             for sym in aut.get_automata_alphabet().get_symbols():
                  for label in set_state:
                       pass
                       
                       


        
        automata_by_parts = automata.Non_deterministic_automata(automata.Alphabet,state_set,{state_dict[l[0].get_state_label()]},accept_states_set,set())

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



#b = nfa_to_dfa(a)

print(a.reachable_states_table())
print(a.get_dict_label_state())


#b.render_automata()


