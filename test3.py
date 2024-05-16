from automata import *

sigma = Alphabet({'a','b'})
print(sigma.get_alphabet_id())
s1 = State(2,'q1')
s2 = State(2,'q2')
s3 = State(2,'q3') 
s4 = State(2,'q4')

t1 = Transition(s1,'a',s1,sigma)
t2 = Transition(s2,'b',s1,sigma)
t3 = Transition(s2,'a',s3,sigma)
t5 = Transition(s4,'b',s1,sigma)
t6 = Transition(s3,'b',s1,sigma)
t7 = Transition(s1,'b',s3,sigma)

a = Non_deterministic_automata(sigma,{s1,s2,s3,s4},{s4,s1,s2},{s3,s4},{t1,t2,t3,t5,t6,t7})

aa  = a.get_accept_states()

print(a.get_accept_states_list())
print(a.get_transition_litterals_from_state(s1))
print(a.get_possible_symbols_from_state(s1))

print(a.get_states_list())
print(a.get_power_set_of_states())
b= a.give_automata_by_parts()
b.render_automta()