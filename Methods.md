# Methods

## class Alphabet:

def get_alphabet_id(self) -> str:

def get_symbols(self) -> set[str]:

def set_symbols(self,new_symbols : set[str]) -> None:

def add_symbol(self,new_symbol : str) -> None:

def remove_symbol(self,symbol : str) -> None:

## class State

def get_state_id(self) -> str:

def get_state_type(self) -> int:

def get_state_label(self) -> str:

def set_state_type(self,new_type : int) ->None:

def set_state_label(self,new_label : str) ->None:

def state_info(self) -> dict:

## class Transition

def get_transition_id(self) -> str:

def get_transition_litteral(self) -> tuple:

def get_tansition_origin_state(self) -> State:

def get_transition_destination_state(self) -> State:

def get_alphabet(self) -> Alphabet:

def get_transition_label(self) -> str:

def set_transition_origin_state(self,new_origin : State) -> None:

def set_transition_destination_state(self,new_destination : State) -> None:

def set_transition_label(self,new_label : str) -> None:

## class Non_deterministic_automata

def get_automata_id(self) -> str:

def get_automata_alphabet(self) -> Alphabet:

def get_states(self) -> set[State]:

def get_initial_states(self) -> set[State]:

def get_accept_states(self) -> set[State]:

def get_transitions(self) -> set[Transition]:

def add_transition(self,new_transition :Transition) ->None:

def remove_transition(self,transition : Transition) ->None:

def get_transition_list(self) -> list[tuple]:

def get_initial_states_list(self) -> list[str]:

def get_accept_states_list(self) -> list[str]:

def get_states_list(self) -> list[str]:

def add_state(self,new_state : State) -> None:

def remove_state(self, state: State) -> None:

def render_automata(self):

def transition_function(self) -> list:

def get_transitions_from_state(self,state : State) -> list[Transition]:

def get_transition_litterals_from_state(self,state :State) -> list[tuple]:

def get_possible_symbols_from_state(self,state : State) -> list[str]:

def get_dict_label_state(self) ->dict:

def get_state_by_label(self,label : str) -> State:

def reachable_states_table(self) -> dict:

def reachable_states_table_labels(self) -> dict:

def get_power_set_of_states(self) -> list[set[str]]: