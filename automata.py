import uuid
import pygraphviz as pgv
import matplotlib.pyplot as plt
import math



epsilon = '\u03B5'
empty_set = '\u2205'



class Alphabet:
    """
    Class to define the alpabet where the automata is defined and the symbols allowed to use
    """
    def __init__(self,symbols : set[str]) -> None:
        self.alphabet_id = uuid.uuid4().hex
        self.symbols = symbols
    
    def get_alphabet_id(self) -> str:
        """
        This method returns the alphabet id
        """
        return self.alphabet_id

    def get_symbols(self) -> set[str]:
        """
        This method returns a list of all symbols within the alphabet
        """
        return self.symbols
    
    def set_symbols(self,new_symbols : set[str]) -> None:
        """
        Method to set a new list of symbols
        """
        self.symbols = new_symbols
    
    def add_symbol(self,new_symbol : str) -> None:
        """
        This method allows to add one symbol to the list of symbols
        args : new_symbol :str
        return : None 
        """
        self.symbols.add(new_symbol)
    
    def remove_symbol(self,symbol : str) -> None:
        """
        Method to remove a symbol from the alphabet
        args : symbol_to_remove :str
        return : None
        """
        try:
            self.symbols.remove(symbol)
        except KeyError as e:
            print(f"Element does not exist: {e}")




possible_states = {0:'start',1:'end',2:'normal'}

class State:
    def  __init__(self,state_type :int ,state_label : str) -> None:
        self.state_id = uuid.uuid4().hex

        possible_states = {0:'start',1:'end',2:'normal'}
        if state_type not in possible_states.keys():
            raise ValueError('This type doesn\'t exist')
        else:
            self.state_type = state_type
        
        self.state_label = state_label
    
    def __eq__(self, other) -> bool:
        return (self.state_label == other.state_label)
    
    def __hash__(self) -> int:
        return hash(self.state_id)

    def get_state_id(self) -> str:
        """
        Returns the state id
        args : None
        return : state_id
        """
        return self.state_id

    def get_state_type(self) -> int:
        """
        Returns the state type
        args : None
        return : state_type : int
        """
        return self.state_type
    
    def get_state_label(self) -> str:
        """
        Returns the state label
        args : None
        return : state_label : str
        """
        return self.state_label
    
    def set_state_type(self,new_type : int) ->None:
        """
        Allows to change the state_type of a state
        args : new_type : int
        return  : None
        """
        self.state_type = new_type
    
    def set_state_label(self,new_label : str) ->None:
        """
        Allows to set the state label
        args : new_label : str
        return : None
        """
        self.state_label = new_label

    def state_info(self) -> dict:
        """
        Returns a dictionnary containing the state attributes
        args : None
        return : dict_info : dict
        """
        return {'state_id':self.state_id,'state_type':self.state_type,'state_label':self.state_label}
    




class Transition:
    def __init__(self, origin_state : State ,label :str ,  destination_state : State , alphabet : Alphabet) -> None:
        self.transition_id = uuid.uuid4().hex
        self.origin_state = origin_state

        if label not in alphabet.get_symbols() and label != epsilon:
            raise ValueError('This symbol does not belong to the alphabet')
        else:
            self.label = label
        
        self.destination_state = destination_state
        self.alphabet = alphabet

    def __eq__(self, other) -> bool:
        return (self.origin_state == other.origin_state and self.destination_state == other.destination_state and self.label == other.label)
    
    def __hash__(self) -> int:
        return hash(self.transition_id)

    def get_transition_id(self) -> str:
        """
        Returns the transition id
        args : None
        return : id : str
        """
        return self.transition_id
    
    def get_transition_litteral(self) -> tuple:
        """
        Returns a tuple containing the start state, label, and destination state of the transition
        args : None
        return  : transition+_litteral : tuple
        """
        return (self.origin_state.get_state_label(),self.label,self.destination_state.get_state_label())
    
    def get_tansition_origin_state(self) -> State:
        return self.origin_state
    
    def get_transition_destination_state(self) -> State:
        return self.destination_state
    
    def get_alphabet(self) -> Alphabet:
        return self.alphabet
    
    def get_transition_label(self) -> str:
        return self.label
    
    def set_transition_origin_state(self,new_origin : State) -> None:
        self.origin_state = new_origin
    
    def set_transition_destination_state(self,new_destination : State) -> None:
        self.destination_state = new_destination
    
    def set_transition_label(self,new_label : str) -> None:
        if new_label not in self.alphabet.get_symbols():
            raise ValueError('This symbol does not exist in the alphabet')
        else:
            self.label = new_label
    
    



class Non_deterministic_automata:
    def __init__(self,alphabet :Alphabet , states : set[State], initial_states : set[State] , accept_states : set[State] , transitions : set[Transition]) -> None:
        self.automata_id = uuid.uuid4().hex
        self.alphabet = alphabet
        self.states = states
        self.initial_states = initial_states
        self.accept_states = accept_states
        self.transitions = transitions
    
    def get_automata_id(self) -> str:
        return self.automata_id
    
    def get_automata_alphabet(self) -> Alphabet:
        return self.alphabet
    
    def get_states(self) -> set[State]:
        return self.states
    
    def get_initial_states(self) -> set[State]:
        return self.initial_states
    
    def get_accept_states(self) -> set[State]:
        return self.accept_states
    
    def get_transitions(self) -> set[Transition]:
        return self.transitions
    
    
    def add_transition(self,new_transition :Transition) ->None:
        self.transitions.add(new_transition)
    
    def remove_transition(self,transition : Transition) ->None:
        try:
            self.transitions.remove(transition)
        except KeyError as e:
            print(f"This transition does not exist: {e}")

    def get_transition_list(self) -> list[tuple]:
        return [transition.get_transition_litteral() for transition in self.transitions]

    
    def get_initial_states_list(self) -> list[str]:
        return [state.get_state_label() for state in self.initial_states]
    
    def get_accept_states_list(self) -> list[str]:
        return [state.get_state_label() for state in self.accept_states]

    def get_states_list(self) -> list[str]:
        return [state.get_state_label() for state in self.states]

    def add_state(self,new_state : State) -> None:
        self.states.add(new_state)
    
    def remove_state(self, state: State) -> None:
        try:
            self.states.remove(state)
        except (KeyError, TypeError) as e:
            raise ValueError(f"This state does not exist: {e}")

    

    def render_automata(self):

        G = pgv.AGraph(strict=False, directed=True,center = True)

        

        for state in self.states:
            if state in self.accept_states and state in self.initial_states:
                G.add_node(state.get_state_label(), shape='doublecircle',color='red')
                G.add_node('null', style ='invisible')
                G.add_edge('null', state.get_state_label(),len = 0.5)
            elif state in self.accept_states:
                G.add_node(state.get_state_label(), shape='doublecircle',color='red',order=len(self.states))
            
            elif state in self.initial_states:
                G.add_node(state.get_state_label(),shape='circle')
                G.add_node('null', style ='invisible')
                G.add_edge('null', state.get_state_label(),len = 0.5)
            else:
                G.add_node(state.get_state_label(), shape='circle')
            
        

        for transition in self.transitions:
            origin_state = transition.get_tansition_origin_state()
            destination_state = transition.get_transition_destination_state()
            transition_label = transition.get_transition_label()
            G.add_edge(origin_state.get_state_label(), destination_state.get_state_label(), label=transition_label)
            
        

        G.graph_attr['rankdir'] = 'LR'
        G.graph_attr['fontname'] = 'Helvetica,Arial,sans-serif'
        G.node_attr['fontname'] = 'Helvetica,Arial,sans-serif'
        G.edge_attr['fontname'] = 'Helvetica,Arial,sans-serif'

        
        G.graph_attr.update(dpi='300', size='15', nodesep='0.4')
        G.layout(prog='dot')
        G.draw(f"images/{self.get_automata_id()}.png")
        print("Finite state machine graph saved")

        
        plt.figure(figsize=(8, 6))
        plt.imshow(plt.imread(f'images/{self.get_automata_id()}.png'))
        plt.axis('off')
        plt.show()

    def transition_function(self) -> list:
        transitions = self.get_transition_list()
        transition_function = []
        for transition in transitions:
            transition_function.append([(transition[0],transition[1]),transition[2]])
        return transition_function
    
    def get_transitions_from_state(self,state : State) -> list[Transition]:
        transitions = self.transitions
        related_transitions = []
        for transition in transitions:
            if transition.get_tansition_origin_state().get_state_label() == state.get_state_label():
                related_transitions.append(transition)
        return related_transitions
    
    def get_transition_litterals_from_state(self,state :State) -> list[tuple]:
        related_transitions = self.get_transitions_from_state(state)
        return [transition.get_transition_litteral() for transition in related_transitions]

    def get_possible_symbols_from_state(self,state : State) -> list[str]:
        related_transition_litterals = self.get_transition_litterals_from_state(state)
        symbols_from_state = []
        for related_transition in related_transition_litterals:
            symbols_from_state.append(related_transition[1])

        return symbols_from_state
    
    def get_dict_label_state(self) ->dict:
        states = self.states
        dict = {}

        for state in states:
            dict[state.get_state_label()] = state
        
        return dict

    def get_state_by_label(self,label : str) -> State:
        table =self.get_dict_label_state()

        if label in table.keys():
            state = table[label]
        else:
            raise IndexError("Thius key does not exist")

        return state
    
    def reachable_states_table(self) -> dict:
        """
        Generate a table of reachable states from a given set of states and alphabet symbols.

        Args:
        - states (set[State]): The set of states from which to generate the table.
        - symbols (set[str]): The set of alphabet symbols.

        Returns:
        - dict: A dictionary representing the table with state pairs as keys and sets of reachable states as values.
        """
        states = self.get_states()
        symbols = self.alphabet.get_symbols()

        
        table = {}

        
        for state in states:
            
            reachable_states = set()

            
            for symbol in symbols:
                transitions = self.get_transitions_from_state(state)
                for transition in transitions:
                    if transition.get_transition_label() == symbol:
                        
                        reachable_states.add(transition.get_transition_destination_state())

            
            table[state] = reachable_states

        return table
    

    def reachable_states_table_labels(self) -> dict:
        """
        Generate a table of reachable states from a given set of state labels and alphabet symbols.

        Args:
        - state_labels (set[str]): The set of state labels from which to generate the table.
        - symbols (set[str]): The set of alphabet symbols.

        Returns:
        - dict: A dictionary representing the table with state label pairs as keys and sets of reachable state labels as values.
        """
        state_labels = self.get_initial_states_list()
        symbols = self.alphabet.get_symbols()
        
        table = {}

        
        for state_label in state_labels:
            
            reachable_state_labels = set()

            
            state = self.get_state_by_label(state_label)

            
            for symbol in symbols:
                transitions = self.get_transitions_from_state(state)
                for transition in transitions:
                    if transition.get_transition_label() == symbol:
                        
                        reachable_state_labels.add(transition.get_transition_destination_state().get_state_label())

            
            table[state_label] = reachable_state_labels

        return table

    def reachable_states_from_sym(self,label : str , sym : str):
        tuple_transition = (label,sym)

        delta = self.transition_function()
        result = []
        for transition in delta:
            if transition[0] == tuple_transition:
                result.append(transition[1])
        
        return result
    

    def get_power_set_of_states(self) -> list[set[str]]:
        labels = self.get_states_list()
        set_size = len(labels)
        pow_set_size = int(math.pow(2, set_size))
        
        power_set = []
        
        for counter in range(0, pow_set_size):
            subset = set()
            for j in range(0, set_size):
                if counter & (1 << j):
                    subset.add(list(labels)[j])
            power_set.append(subset)
        
        return power_set
    






class Deterministic_automata(Non_deterministic_automata):
    def __init__(self, alphabet: Alphabet, states: set[State], initial_states: set[State], accept_states: set[State], transitions: set[Transition]) -> None:

        

        if epsilon in alphabet.get_symbols():
            raise ValueError(f'A finite state automata cannot use {epsilon} as a caracter')
        else:
            self.alphabet = alphabet

        
        transition_list = [transition.get_transition_litteral() for transition in transitions]
        transitions_dict = {}

        for transition in transition_list:
            transitions_dict[(transition[0],transition[1])] = transition[2]
        
        if len(transition_list) == len(transitions_dict):
            self.transitions = transitions
        else:
            raise ValueError('the list of transitions is incompatible with a finite automata (there exist a couple (state,symbol) with more than one destination)')
        
        if len(initial_states) != 1:
            raise ValueError('A deterministic finite automata can only have one initial state')
        else:
            self.initial_states = initial_states 

        super().__init__(alphabet,states, initial_states, accept_states,transitions)
    







